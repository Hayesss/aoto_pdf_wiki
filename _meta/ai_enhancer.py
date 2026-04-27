#!/usr/bin/env python3
"""
Kimi AI Enhancer - LLM-Wiki AI 精炼模块

功能:
1. 调用 Kimi API (Moonshot) 精炼提取的论文内容
2. 生成高质量的 AIMRaD 结构化笔记
3. 支持 fallback 到启发式提取
4. 支持流式输出和错误重试

使用方式:
    from ai_enhancer import KimiEnhancer
    
    enhancer = KimiEnhancer(api_key="sk-...")
    result = enhancer.enhance_paper(raw_text, title="Paper Title")
    
    # 或使用配置文件
    enhancer = KimiEnhancer.from_config()
    result = enhancer.enhance_paper(raw_text)
"""

import os
import re
import json
import time
import urllib.request
import urllib.error
import ssl
from pathlib import Path
from typing import Optional, Dict, Any, Callable
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EnhancementResult:
    """AI 精炼结果"""
    title: str
    abstract: str
    background: str
    findings: str
    methods: str
    discussion: str
    keywords: list
    entities: Dict[str, list]
    confidence: str  # high, medium, low
    model_used: str
    tokens_used: int
    raw_response: str
    success: bool
    error: Optional[str] = None


class KimiEnhancer:
    """Kimi API 论文精炼器"""
    
    # Kimi API 端点
    API_BASE = "https://api.moonshot.cn/v1"
    
    # 可用模型
    MODELS = {
        "8k": "moonshot-v1-8k",
        "32k": "moonshot-v1-32k", 
        "128k": "moonshot-v1-128k",
        "auto": "moonshot-v1-32k",  # 默认
    }
    
    # 默认配置
    DEFAULT_MAX_TOKENS = 4096
    DEFAULT_TEMPERATURE = 0.3
    DEFAULT_TIMEOUT = 120
    MAX_RETRIES = 3
    RETRY_DELAY = 5
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "auto",
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        timeout: int = DEFAULT_TIMEOUT,
        prompt_dir: Optional[str] = None,
        fallback_enabled: bool = True,
        verbose: bool = True
    ):
        """
        初始化 Kimi Enhancer
        
        Args:
            api_key: Kimi API Key (默认从环境变量 KIMI_API_KEY 读取)
            model: 模型选择 (8k/32k/128k/auto)
            max_tokens: 最大生成 token 数
            temperature: 温度 (0-1, 越低越确定)
            timeout: API 请求超时秒数
            prompt_dir: 自定义 prompt 模板目录
            fallback_enabled: 是否启用启发式 fallback
            verbose: 是否打印日志
        """
        self.api_key = api_key or os.environ.get("KIMI_API_KEY")
        self.model = self.MODELS.get(model, model)
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.timeout = timeout
        self.fallback_enabled = fallback_enabled
        self.verbose = verbose
        
        # Prompt 目录
        if prompt_dir:
            self.prompt_dir = Path(prompt_dir)
        else:
            # 默认在 _meta/prompts/ 目录
            self.prompt_dir = Path(__file__).parent / "prompts"
        
        # SSL 上下文
        self._ssl_context = ssl.create_default_context()
        
        # 加载 prompt 模板
        self._prompts = {}
        self._load_prompts()
        
        # 统计
        self.stats = {
            "total_requests": 0,
            "successful": 0,
            "failed": 0,
            "fallback_used": 0,
            "total_tokens": 0,
        }
    
    def _log(self, message: str, level: str = "INFO"):
        """打印日志"""
        if self.verbose:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [KimiEnhancer] [{level}] {message}")
    
    def _load_prompts(self):
        """加载 prompt 模板"""
        # 内置默认 prompt
        self._prompts["aimrad"] = self._default_aimrad_prompt()
        self._prompts["entity_extraction"] = self._default_entity_prompt()
        
        # 从文件加载（如果存在）
        if self.prompt_dir.exists():
            for prompt_file in self.prompt_dir.glob("*.txt"):
                name = prompt_file.stem
                try:
                    with open(prompt_file, 'r', encoding='utf-8') as f:
                        self._prompts[name] = f.read()
                    self._log(f"加载 prompt 模板: {name}")
                except Exception as e:
                    self._log(f"加载 prompt 失败 {name}: {e}", "WARN")
    
    def _default_aimrad_prompt(self) -> str:
        """默认 AIMRaD 精炼 prompt"""
        return """你是一位专业的学术文献分析助手。请仔细阅读以下从PDF提取的论文文本，将其精炼为结构化的学术笔记。

## 任务要求

1. **标题**: 提取论文的完整标题（保持原语言）
2. **摘要 (Abstract)**: 用2-3句话概括研究的核心内容
3. **背景与目的 (Background)**: 
   - 研究领域和问题的背景
   - 研究动机和假设
   - 研究目标
4. **主要发现 (Findings/Results)**: 
   - 关键实验结果（用 bullet points）
   - 重要数据和统计显著性
   - 主要图表的发现
5. **方法概述 (Methods)**: 
   - 实验设计
   - 样本/数据来源
   - 关键技术方法
6. **讨论与结论 (Discussion)**: 
   - 结果的意义和解释
   - 与已有研究的对比
   - 局限性和未来方向
   - 结论性陈述
7. **关键词**: 提取5-10个核心学术关键词
8. **实体识别**: 
   - 蛋白质/基因名称
   - 细胞类型
   - 信号通路
   - 实验方法
   - 疾病/表型

## 输出格式

请严格按以下 JSON 格式输出（不要添加 markdown 代码块标记，直接输出 JSON）：

{
  "title": "论文标题",
  "abstract": "摘要文本",
  "background": "背景与目的",
  "findings": "主要发现",
  "methods": "方法概述",
  "discussion": "讨论与结论",
  "keywords": ["关键词1", "关键词2", ...],
  "entities": {
    "proteins": ["蛋白1", ...],
    "cell_types": ["细胞类型1", ...],
    "pathways": ["通路1", ...],
    "methods": ["方法1", ...],
    "diseases": ["疾病1", ...]
  }
}

## 注意事项

- 保持学术准确性，不要编造信息
- 如果某部分信息在原文中找不到，用 "（原文未明确提及）" 标注
- 对于数字和统计数据，尽量保留具体数值
- 输出必须是合法的 JSON，不要包含注释

## 待处理文本

{paper_text}
"""
    
    def _default_entity_prompt(self) -> str:
        """默认实体提取 prompt"""
        return """从以下学术文本中提取关键实体，按 JSON 格式输出：

{
  "proteins": ["蛋白质/基因名称"],
  "cell_types": ["细胞类型"],
  "pathways": ["信号通路"],
  "methods": ["实验方法"],
  "diseases": ["疾病/表型"],
  "chemicals": ["化合物/药物"],
  "organisms": ["生物体/模式生物"]
}

文本：
{text}

只输出 JSON，不要其他内容。"""
    
    def _call_api(
        self,
        messages: list,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        stream: bool = False,
        stream_callback: Optional[Callable[[str], None]] = None
    ) -> Dict[str, Any]:
        """
        调用 Kimi API
        
        Args:
            messages: 消息列表 [{"role": "user", "content": "..."}]
            max_tokens: 最大 token 数
            temperature: 温度
            stream: 是否流式输出
            stream_callback: 流式回调函数
            
        Returns:
            API 响应字典
        """
        if not self.api_key:
            raise ValueError("API Key 未设置。请提供 api_key 参数或设置 KIMI_API_KEY 环境变量。")
        
        url = f"{self.API_BASE}/chat/completions"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens or self.max_tokens,
            "temperature": temperature or self.temperature,
            "stream": stream
        }
        
        data = json.dumps(payload).encode('utf-8')
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, data=data, headers=headers)
        
        # 重试逻辑
        for attempt in range(self.MAX_RETRIES):
            try:
                self._log(f"API 请求 (尝试 {attempt + 1}/{self.MAX_RETRIES})...")
                self.stats["total_requests"] += 1
                
                resp = urllib.request.urlopen(
                    req, 
                    context=self._ssl_context, 
                    timeout=self.timeout
                )
                
                result = json.loads(resp.read().decode('utf-8'))
                
                # 更新统计
                self.stats["successful"] += 1
                if "usage" in result and "total_tokens" in result["usage"]:
                    self.stats["total_tokens"] += result["usage"]["total_tokens"]
                
                self._log(f"API 请求成功")
                return result
                
            except urllib.error.HTTPError as e:
                error_body = e.read().decode('utf-8') if e.fp else ""
                self._log(f"HTTP {e.code}: {error_body}", "ERROR")
                
                # 检查特定错误
                if e.code == 401:
                    raise ValueError(f"API Key 无效: {error_body}")
                elif e.code == 429:
                    self._log(f"请求频率限制，等待 {self.RETRY_DELAY} 秒...", "WARN")
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                    continue
                elif e.code == 402:
                    raise ValueError(f"账户余额不足: {error_body}")
                elif e.code >= 500:
                    self._log(f"服务器错误，等待后重试...", "WARN")
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                    continue
                else:
                    raise
                    
            except urllib.error.URLError as e:
                self._log(f"网络错误: {e.reason}", "ERROR")
                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                    continue
                raise
                
            except Exception as e:
                self._log(f"请求异常: {str(e)}", "ERROR")
                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                    continue
                raise
        
        self.stats["failed"] += 1
        raise RuntimeError(f"API 请求在 {self.MAX_RETRIES} 次尝试后仍然失败")
    
    def _parse_json_response(self, text: str) -> Optional[Dict]:
        """从 API 响应中提取 JSON"""
        # 尝试直接解析
        try:
            return json.loads(text.strip())
        except json.JSONDecodeError:
            pass
        
        # 尝试从 markdown 代码块中提取
        patterns = [
            r'```json\s*(.*?)\s*```',
            r'```\s*(.*?)\s*```',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1).strip())
                except json.JSONDecodeError:
                    continue
        
        # 尝试找到 JSON 对象
        try:
            start = text.find('{')
            end = text.rfind('}')
            if start != -1 and end != -1 and end > start:
                return json.loads(text[start:end+1])
        except json.JSONDecodeError:
            pass
        
        return None
    
    def _fallback_extraction(self, raw_text: str, title: str = "") -> EnhancementResult:
        """启发式 fallback 提取（当 API 失败时使用）"""
        self._log("使用启发式 fallback 提取", "WARN")
        self.stats["fallback_used"] += 1
        
        # 简单的启发式提取逻辑
        lines = raw_text.split('\n')
        
        # 提取标题
        extracted_title = title
        if not extracted_title:
            for line in lines[:10]:
                if line.strip() and len(line.strip()) < 200:
                    extracted_title = line.strip()
                    break
        
        # 提取摘要（前 500 字符的非标题文本）
        abstract_lines = []
        for line in lines[:50]:
            if len(line.strip()) > 50 and not line.startswith('#'):
                abstract_lines.append(line.strip())
            if len(' '.join(abstract_lines)) > 500:
                break
        abstract = ' '.join(abstract_lines)[:800]
        
        # 提取方法关键词
        method_keywords = ['method', 'protocol', 'procedure', 'assay',
                          'sequencing', 'RNA-seq', 'scRNA-seq', 'CRISPR',
                          'FACS', 'flow cytometry', 'mass spectrometry']
        method_lines = []
        for line in lines:
            if any(kw in line.lower() for kw in method_keywords):
                method_lines.append(line.strip())
        methods = ' '.join(method_lines[:10])[:500]
        
        # 基础实体提取
        entities = {
            'proteins': [],
            'cell_types': [],
            'pathways': [],
            'methods': [],
            'diseases': []
        }
        
        # 简单的正则匹配
        text = f"{extracted_title} {abstract} {methods}"
        
        # 蛋白 (AARS 模式)
        entities['proteins'] = list(set(re.findall(r'\b([A-Z][a-zA-Z]{1,3}RS[0-9]?)\b', text)))
        
        # 细胞类型
        cell_types = re.findall(
            r'\b(HSC|LSC|AML|CML|MDS|MPN|ALL|CLL|NK\s+cell|T\s+cell|B\s+cell|'
            r'monocyte|macrophage|neutrophil|dendritic\s+cell|'
            r'hematopoietic\s+stem\s+cell|leukemia\s+stem\s+cell|progenitor|'
            r'erythroid|myeloid|lymphoid|megakaryocyte)\b', 
            text, re.I
        )
        entities['cell_types'] = list(set([m for m in cell_types if len(m) > 1]))
        
        # 通路
        pathways = re.findall(
            r'\b(JAK-STAT|MAPK|PI3K-AKT|Wnt|Notch|Hedgehog|TGF-β|NF-κB|mTOR|'
            r'RAS-RAF|p53|cell\s+cycle|apoptosis|autophagy|inflammation|'
            r'differentiation|self-renewal|quiescence)\b', 
            text, re.I
        )
        entities['pathways'] = list(set(pathways))
        
        # 关键词
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
                    'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is',
                    'was', 'are', 'were', 'be', 'been', 'have', 'has', 'had'}
        title_words = re.findall(r'\b[A-Za-z][a-zA-Z0-9\-]+\b', extracted_title)
        keywords = [w for w in title_words if w.lower() not in stopwords and len(w) > 2]
        
        return EnhancementResult(
            title=extracted_title,
            abstract=abstract,
            background="（启发式提取 - 需手动补充）",
            findings="（启发式提取 - 需手动补充）",
            methods=methods or "（启发式提取 - 需手动补充）",
            discussion="（启发式提取 - 需手动补充）",
            keywords=keywords[:10],
            entities=entities,
            confidence="low",
            model_used="fallback_heuristic",
            tokens_used=0,
            raw_response="",
            success=True,
            error="API 不可用，使用启发式 fallback"
        )
    
    def enhance_paper(
        self,
        raw_text: str,
        title: str = "",
        prompt_name: str = "aimrad",
        max_tokens: Optional[int] = None,
        stream: bool = False,
        stream_callback: Optional[Callable[[str], None]] = None
    ) -> EnhancementResult:
        """
        精炼论文内容
        
        Args:
            raw_text: 从 PDF 提取的原始文本
            title: 论文标题（可选，用于 fallback）
            prompt_name: 使用的 prompt 模板名称
            max_tokens: 最大生成 token 数
            stream: 是否流式输出
            stream_callback: 流式回调函数
            
        Returns:
            EnhancementResult 对象
        """
        # 检查文本长度
        text_length = len(raw_text)
        self._log(f"待精炼文本长度: {text_length} 字符")
        
        # 如果文本过长，截断（保留开头和结尾）
        max_input_length = 100000  # 约 25k tokens
        if text_length > max_input_length:
            self._log(f"文本过长，截断至 {max_input_length} 字符")
            # 保留前 60% 和后 40%
            head_len = int(max_input_length * 0.6)
            tail_len = int(max_input_length * 0.4)
            raw_text = raw_text[:head_len] + "\n\n...[中间内容省略]...\n\n" + raw_text[-tail_len:]
        
        # 获取 prompt 模板
        prompt_template = self._prompts.get(prompt_name, self._prompts["aimrad"])
        # 使用 replace 而不是 format，避免 raw_text 中的花括号被误解析
        prompt = prompt_template.replace("{paper_text}", raw_text)
        
        # 调用 API
        try:
            messages = [{"role": "user", "content": prompt}]
            
            response = self._call_api(
                messages=messages,
                max_tokens=max_tokens,
                stream=stream,
                stream_callback=stream_callback
            )
            
            # 提取生成的文本
            generated_text = response["choices"][0]["message"]["content"]
            
            # 解析 JSON
            parsed = self._parse_json_response(generated_text)
            
            if not parsed:
                raise ValueError("无法从 API 响应中解析 JSON")
            
            # 构建结果
            tokens_used = response.get("usage", {}).get("total_tokens", 0)
            
            result = EnhancementResult(
                title=parsed.get("title", title or "未命名论文"),
                abstract=parsed.get("abstract", ""),
                background=parsed.get("background", ""),
                findings=parsed.get("findings", ""),
                methods=parsed.get("methods", ""),
                discussion=parsed.get("discussion", ""),
                keywords=parsed.get("keywords", []),
                entities=parsed.get("entities", {}),
                confidence="high",
                model_used=self.model,
                tokens_used=tokens_used,
                raw_response=generated_text,
                success=True
            )
            
            self._log(f"精炼完成: {result.title} (使用 {tokens_used} tokens)")
            return result
            
        except Exception as e:
            self._log(f"AI 精炼失败: {str(e)}", "ERROR")
            
            if self.fallback_enabled:
                self._log("启用 fallback 模式", "WARN")
                return self._fallback_extraction(raw_text, title)
            else:
                return EnhancementResult(
                    title=title or "处理失败",
                    abstract="",
                    background="",
                    findings="",
                    methods="",
                    discussion="",
                    keywords=[],
                    entities={},
                    confidence="none",
                    model_used="none",
                    tokens_used=0,
                    raw_response="",
                    success=False,
                    error=str(e)
                )
    
    def batch_enhance(
        self,
        papers: list,
        delay: float = 1.0,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> list:
        """
        批量精炼论文
        
        Args:
            papers: [(raw_text, title), ...] 列表
            delay: 请求间隔秒数（避免频率限制）
            progress_callback: 进度回调函数 (current, total)
            
        Returns:
            EnhancementResult 列表
        """
        results = []
        total = len(papers)
        
        for i, (raw_text, title) in enumerate(papers):
            self._log(f"处理 {i+1}/{total}: {title or '未命名'}")
            
            result = self.enhance_paper(raw_text, title)
            results.append(result)
            
            if progress_callback:
                progress_callback(i + 1, total)
            
            # 延迟（除了最后一个）
            if i < total - 1 and delay > 0:
                time.sleep(delay)
        
        # 汇总统计
        success_count = sum(1 for r in results if r.success)
        fallback_count = sum(1 for r in results if r.confidence == "low")
        
        self._log(f"批量处理完成: {success_count}/{total} 成功, {fallback_count} 使用 fallback")
        
        return results
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        return self.stats.copy()
    
    def reset_stats(self):
        """重置统计"""
        self.stats = {
            "total_requests": 0,
            "successful": 0,
            "failed": 0,
            "fallback_used": 0,
            "total_tokens": 0,
        }
    
    @classmethod
    def from_config(cls, config_path: Optional[str] = None) -> "KimiEnhancer":
        """
        从配置文件创建实例
        
        配置文件格式 (JSON):
        {
            "api_key": "sk-...",
            "model": "32k",
            "max_tokens": 4096,
            "temperature": 0.3,
            "fallback_enabled": true,
            "prompt_dir": "./prompts"
        }
        """
        if not config_path:
            # 默认配置文件路径
            config_path = Path(__file__).parent / "config.json"
        else:
            config_path = Path(config_path)
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return cls(**config)
        else:
            # 使用环境变量和默认值
            return cls()


def test_enhancer():
    """测试 enhancer"""
    print("=" * 60)
    print("KimiEnhancer 测试")
    print("=" * 60)
    
    # 检查 API Key
    api_key = os.environ.get("KIMI_API_KEY")
    if not api_key:
        print("警告: KIMI_API_KEY 环境变量未设置")
        print("将测试 fallback 模式")
    
    # 创建实例
    enhancer = KimiEnhancer(
        api_key=api_key,
        verbose=True,
        fallback_enabled=True
    )
    
    # 测试文本
    test_text = """
    Title: Single-cell analysis reveals the intracellular signaling and 
    transcriptional regulation in leukemia stem cells
    
    Abstract:
    Leukemia stem cells (LSCs) are responsible for disease initiation and 
    relapse. Here we performed single-cell RNA sequencing (scRNA-seq) on 
    3847 cells from 8 AML patients to characterize the transcriptional 
    heterogeneity of LSCs. We identified a distinct LSC population with 
    enhanced self-renewal capacity and activated JAK-STAT and PI3K-AKT 
    signaling pathways. CRISPR screening revealed that AARS1 is essential 
    for LSC maintenance. Targeting AARS1 with shRNA significantly reduced 
    LSC frequency in xenograft models.
    
    Methods:
    - scRNA-seq using 10x Genomics platform
    - CRISPR-Cas9 knockout screening
    - Flow cytometry for LSC quantification
    - Xenograft transplantation assays
    """
    
    print("\n测试论文精炼...")
    result = enhancer.enhance_paper(test_text, title="Test Paper")
    
    print(f"\n结果:")
    print(f"  成功: {result.success}")
    print(f"  标题: {result.title}")
    print(f"  置信度: {result.confidence}")
    print(f"  模型: {result.model_used}")
    print(f"  Tokens: {result.tokens_used}")
    print(f"  关键词: {result.keywords[:5]}")
    
    print(f"\n统计:")
    print(f"  {enhancer.get_stats()}")
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    test_enhancer()
