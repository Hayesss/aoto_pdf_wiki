#!/usr/bin/env python3
"""
LLM-Wiki PDF 自动处理流水线

功能:
1. 监控 inbox/ 目录的新 PDF
2. 自动提取文本 (marker-pdf)
3. 生成结构化笔记 (AIMRaD)
4. 提取关键词和实体
5. 更新索引和链接图谱

使用方式:
    # 监控模式 (后台运行)
    python wiki_pipeline.py --watch --wiki-dir /path/to/llm-wiki

    # 单次处理 (处理 inbox/ 中所有待处理 PDF)
    python wiki_pipeline.py --process --wiki-dir /path/to/llm-wiki

    # 处理单个文件
    python wiki_pipeline.py --file /path/to/paper.pdf --wiki-dir /path/to/llm-wiki

依赖:
    - marker-pdf (PDF 文本提取)
    - watchdog (文件监控, 可选)
"""

import os
import sys
import re
import json
import hashlib
import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

# 尝试导入 watchdog
WATCHDOG_AVAILABLE = False
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    pass


class WikiPipeline:
    """LLM-Wiki PDF 处理流水线"""

    def __init__(self, wiki_dir: str, marker_cmd: str = "marker-pdf"):
        self.wiki_dir = Path(wiki_dir)
        self.marker_cmd = marker_cmd
        self.inbox_dir = self.wiki_dir / "inbox"
        self.raw_dir = self.wiki_dir / "raw" / "papers"
        self.papers_dir = self.wiki_dir / "papers"
        self.failed_dir = self.wiki_dir / "failed"
        self.processed_dir = self.wiki_dir / "processed"

        # 确保目录存在
        for d in [self.inbox_dir, self.raw_dir, self.papers_dir,
                  self.failed_dir, self.processed_dir]:
            d.mkdir(parents=True, exist_ok=True)

        # 实体识别规则
        self.AARS_PATTERN = re.compile(r'\b([A-Z][a-zA-Z]{1,3}RS[0-9]?)\b')
        self.CELL_TYPE_PATTERN = re.compile(
            r'\b(HSC|LSC|AML|CML|MDS|MPN|ALL|CLL|NK\s+cell|T\s+cell|B\s+cell|'
            r'monocyte|macrophage|neutrophil|dendritic\s+cell|'
            r'hematopoietic\s+stem\s+cell|leukemia\s+stem\s+cell|progenitor|'
            r'erythroid|myeloid|lymphoid|megakaryocyte)\b', re.I)
        self.PATHWAY_PATTERN = re.compile(
            r'\b(JAK-STAT|MAPK|PI3K-AKT|Wnt|Notch|Hedgehog|TGF-β|NF-κB|mTOR|'
            r'RAS-RAF|p53|cell\s+cycle|apoptosis|autophagy|inflammation|'
            r'differentiation|self-renewal|quiescence)\b', re.I)
        self.METHOD_PATTERN = re.compile(
            r'\b(scRNA-seq|RNA-seq|ATAC-seq|ChIP-seq|CRISPR|FACS|MACS|'
            r'flow\s+cytometry|single-cell|bulk\s+RNA-seq|microarray|qPCR|'
            r'Western\s+blot|mass\s+spectrometry|scRNA-Seq|scRNA)\b', re.I)
        self.DISEASE_PATTERN = re.compile(
            r'\b(leukemia|cancer|carcinoma|tumor|melanoma|lymphoma|myeloma|'
            r'sarcoma|fibrosis|inflammation|infection|disease|disorder|syndrome)\b', re.I)

    def log(self, message: str, level: str = "INFO"):
        """记录日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{level}] {message}"
        print(log_line)

        # 追加到 log.md
        log_file = self.wiki_dir / "log.md"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{log_line}")

    def extract_pdf_with_marker(self, pdf_path: Path) -> dict:
        """使用 marker-pdf 提取 PDF 内容 (通过系统 Python 3.12)"""
        self.log(f"提取 PDF: {pdf_path.name}")

        # 生成输出目录
        output_dir = self.raw_dir / pdf_path.stem

        try:
            # marker-pdf 安装在系统 Python 3.12 中，显式调用
            result = subprocess.run(
                ["python3.12", "-m", "marker.scripts.convert_single", str(pdf_path), "--output_dir", str(output_dir)],
                capture_output=True,
                text=True,
                timeout=300  # 5分钟超时
            )

            if result.returncode != 0:
                raise RuntimeError(f"marker-pdf 失败: {result.stderr}")

            # 读取提取的 markdown
            md_files = list(output_dir.glob("*.md"))
            if not md_files:
                raise FileNotFoundError("marker-pdf 未生成 markdown 文件")

            extracted_md = md_files[0]
            with open(extracted_md, 'r', encoding='utf-8') as f:
                content = f.read()

            # 计算 sha256
            sha256 = hashlib.sha256(content.encode()).hexdigest()[:16]

            return {
                "content": content,
                "sha256": sha256,
                "output_dir": output_dir,
                "success": True
            }

        except Exception as e:
            self.log(f"提取失败: {str(e)}", "ERROR")
            return {"success": False, "error": str(e)}

    def generate_raw_frontmatter(self, pdf_path: Path, extracted: dict) -> str:
        """生成 raw/papers/ 的 frontmatter"""
        safe_name = self._safe_filename(pdf_path.stem)

        frontmatter = f"""---
title: "{pdf_path.stem}"
source_file: "{pdf_path.name}"
ingested: {datetime.now().strftime('%Y-%m-%d')}
sha256: {extracted['sha256']}
marker_extracted: true
---

"""
        return frontmatter + extracted["content"]

    def extract_structured_content(self, raw_content: str, use_ai: bool = False) -> dict:
        """从原始内容提取结构化信息 (AIMRaD)
        
        Args:
            raw_content: 原始文本内容
            use_ai: 是否使用 AI 增强（需要配置 KIMI_API_KEY）
        """
        # 如果启用 AI 增强
        if use_ai:
            try:
                from ai_enhancer import KimiEnhancer
                enhancer = KimiEnhancer.from_config()
                result = enhancer.enhance_paper(raw_content)
                
                if result.success:
                    return {
                        "title": result.title,
                        "abstract": result.abstract,
                        "background": result.background,
                        "findings": result.findings,
                        "methods": result.methods,
                        "discussion": result.discussion,
                        "keywords": result.keywords,
                        "entities": result.entities,
                        "ai_enhanced": True,
                        "confidence": result.confidence,
                        "model_used": result.model_used,
                        "tokens_used": result.tokens_used
                    }
            except Exception as e:
                self.log(f"AI 增强失败，回退到启发式提取: {str(e)}", "WARN")
        
        # 启发式提取（fallback）
        sections = {
            "title": "",
            "abstract": "",
            "background": "",
            "findings": "",
            "methods": "",
            "discussion": "",
            "keywords": [],
            "entities": {},
            "ai_enhanced": False,
            "confidence": "low",
            "model_used": "heuristic",
            "tokens_used": 0
        }

        # 尝试提取标题
        lines = raw_content.split('\n')
        for line in lines[:10]:
            if line.strip() and len(line.strip()) < 200:
                sections["title"] = line.strip()
                break

        # 尝试提取摘要 (通常在前 500 字符)
        abstract_lines = []
        for line in lines[:50]:
            if len(line.strip()) > 50 and not line.startswith('#'):
                abstract_lines.append(line.strip())
            if len(' '.join(abstract_lines)) > 500:
                break
        sections["abstract"] = ' '.join(abstract_lines)[:800]

        # 尝试识别方法部分
        method_keywords = ['method', 'protocol', 'procedure', 'assay',
                          'sequencing', 'RNA-seq', 'scRNA-seq', 'CRISPR']
        method_lines = []
        for line in lines:
            if any(kw in line.lower() for kw in method_keywords):
                method_lines.append(line.strip())
        sections["methods"] = ' '.join(method_lines[:10])[:500]

        return sections

    def generate_paper_note(self, pdf_path: Path, raw_content: str,
                           structured: dict) -> str:
        """生成 papers/ 目录的结构化笔记"""
        safe_name = self._safe_filename(pdf_path.stem)
        today = datetime.now().strftime('%Y-%m-%d')

        # 提取标题 (优先使用 AI 提取的标题，或从内容提取)
        title = structured.get("title", "")
        if not title:
            title = pdf_path.stem.replace('_', ' ').replace('-', ' ')
            # 尝试从第一行提取标题
            first_lines = raw_content.split('\n')[:5]
            for line in first_lines:
                if line.strip() and len(line.strip()) < 200:
                    title = line.strip()
                    break

        # 提取实体（优先使用 AI 提取的实体）
        ai_entities = structured.get("entities", {})
        if ai_entities:
            entities = {k: set(v) if isinstance(v, list) else set() 
                       for k, v in ai_entities.items()}
            # 确保所有键存在
            for key in ['proteins', 'cell_types', 'pathways', 'methods', 'diseases', 'keywords']:
                if key not in entities:
                    entities[key] = set()
        else:
            entities = self._extract_entities(title, structured["abstract"], structured["methods"])

        # 生成 frontmatter
        ai_meta = ""
        if structured.get("ai_enhanced"):
            ai_meta = f"""ai_enhanced: true
confidence: {structured.get("confidence", "medium")}
model_used: {structured.get("model_used", "unknown")}
tokens_used: {structured.get("tokens_used", 0)}
"""

        note = f"""---
title: "{title}"
created: {today}
updated: {today}
type: paper
tags: ["paper"]
sources: ["raw/papers/{safe_name}.md"]
confidence: {structured.get("confidence", "medium")}
marker_extracted: true
{ai_meta}---

# {title}

> 原文: [[{safe_name}]]
> 提取方式: {"AI 增强 (" + structured.get("model_used", "") + ")" if structured.get("ai_enhanced") else "启发式提取"}

## 摘要

{structured["abstract"]}

## 背景与目的

{structured.get("background", "（待补充 - 从原文提取研究背景）")}

## 主要发现

{structured.get("findings", "（待补充 - 从原文提取关键发现）")}

## 方法概述

{structured.get("methods", "（待补充）")}

## 讨论与结论

{structured.get("discussion", "（待补充）")}

## 关键词

{', '.join(sorted(structured.get("keywords", []))[:10]) if structured.get("keywords") else '（待补充）'}

## 相关实体

{self._format_entities(entities)}

---

> 本笔记{"基于 AI 精炼生成" if structured.get("ai_enhanced") else "基于自动提取生成"}，已标准化为 AIMRaD 结构。
"""
        return note

    def _extract_entities(self, title: str, abstract: str, methods: str) -> dict:
        """提取实体"""
        text = f"{title} {abstract} {methods}"
        entities = {
            'proteins': set(),
            'cell_types': set(),
            'pathways': set(),
            'methods': set(),
            'diseases': set(),
            'keywords': set()
        }

        # 提取蛋白
        entities['proteins'].update(self.AARS_PATTERN.findall(text))

        # 提取细胞类型
        entities['cell_types'].update(
            [m for m in self.CELL_TYPE_PATTERN.findall(text) if len(m) > 1]
        )

        # 提取通路
        entities['pathways'].update(self.PATHWAY_PATTERN.findall(text))

        # 提取方法
        entities['methods'].update(self.METHOD_PATTERN.findall(text))

        # 提取疾病
        entities['diseases'].update(self.DISEASE_PATTERN.findall(text))

        # 关键词
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
                    'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is',
                    'was', 'are', 'were', 'be', 'been', 'have', 'has', 'had'}
        title_words = re.findall(r'\b[A-Za-z][a-zA-Z0-9\-]+\b', title)
        keywords = [w for w in title_words
                   if w.lower() not in stopwords and len(w) > 2]
        chinese_keywords = re.findall(r'[\u4e00-\u9fff]{2,8}', title)
        entities['keywords'] = set(keywords + chinese_keywords)

        return entities

    def _format_entities(self, entities: dict) -> str:
        """格式化实体输出"""
        parts = []
        if entities['proteins']:
            parts.append(f"蛋白: {', '.join(sorted(entities['proteins']))}")
        if entities['cell_types']:
            parts.append(f"细胞类型: {', '.join(sorted(entities['cell_types']))}")
        if entities['pathways']:
            parts.append(f"通路: {', '.join(sorted(entities['pathways']))}")
        if entities['methods']:
            parts.append(f"方法: {', '.join(sorted(entities['methods']))}")
        if entities['diseases']:
            parts.append(f"疾病: {', '.join(sorted(entities['diseases']))}")

        return '\n'.join(parts) if parts else '（待补充）'

    def _safe_filename(self, name: str) -> str:
        """生成安全的文件名"""
        # 移除或替换不安全字符
        safe = re.sub(r'[^\w\s\-]', '', name)
        safe = re.sub(r'\s+', '-', safe.strip())
        safe = safe.lower()[:80]  # 限制长度
        return safe

    def update_index(self):
        """更新索引文件"""
        self.log("更新索引...")

        # 收集所有论文
        paper_files = sorted([f for f in self.papers_dir.iterdir()
                             if f.suffix == '.md'])

        # 统计标签
        tag_counter = Counter()
        for f in paper_files:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
            if tags_match:
                tags = [t.strip().strip('"').strip("'")
                       for t in tags_match.group(1).split(',') if t.strip()]
                for tag in tags:
                    if tag != 'paper':
                        tag_counter[tag] += 1

        # 生成索引
        index_content = f"""# LLM Wiki 论文索引

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 总计论文: {len(paper_files)} 篇

## 按主题标签分布

"""
        for tag, count in tag_counter.most_common(50):
            index_content += f"- **#{tag}**: {count} 篇\n"

        index_content += """
## 最近更新

"""
        # 添加最近10篇
        for f in sorted(paper_files, key=lambda x: x.stat().st_mtime,
                       reverse=True)[:10]:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else f.stem
            index_content += f"- [[{title}]]\n"

        # 写入
        with open(self.wiki_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_content)

        self.log(f"索引更新完成: {len(paper_files)} 篇论文")

    def process_pdf(self, pdf_path: Path, use_ai: bool = False) -> bool:
        """处理单个 PDF 的完整流程
        
        Args:
            pdf_path: PDF 文件路径
            use_ai: 是否启用 AI 增强提取
        """
        self.log(f"开始处理: {pdf_path.name} (AI增强: {use_ai})")

        try:
            # Step 1: 提取 PDF 内容
            extracted = self.extract_pdf_with_marker(pdf_path)
            if not extracted["success"]:
                raise RuntimeError(extracted.get("error", "未知错误"))

            # Step 2: 保存到 raw/papers/
            safe_name = self._safe_filename(pdf_path.stem)
            raw_file = self.raw_dir / f"{safe_name}.md"
            raw_content = self.generate_raw_frontmatter(pdf_path, extracted)

            with open(raw_file, 'w', encoding='utf-8') as f:
                f.write(raw_content)

            self.log(f"原始内容已保存: {raw_file}")

            # Step 3: 生成结构化笔记（支持 AI 增强）
            structured = self.extract_structured_content(extracted["content"], use_ai=use_ai)
            note_content = self.generate_paper_note(pdf_path, raw_content, structured)

            note_file = self.papers_dir / f"{safe_name}.md"
            with open(note_file, 'w', encoding='utf-8') as f:
                f.write(note_content)

            self.log(f"结构化笔记已生成: {note_file}")

            # Step 4: 移动已处理的 PDF
            processed_pdf = self.processed_dir / pdf_path.name
            shutil.move(str(pdf_path), str(processed_pdf))
            self.log(f"PDF 已移动到: {processed_pdf}")

            return True

        except Exception as e:
            self.log(f"处理失败: {str(e)}", "ERROR")

            # 移动到失败目录
            failed_pdf = self.failed_dir / pdf_path.name
            if pdf_path.exists():
                shutil.move(str(pdf_path), str(failed_pdf))
            self.log(f"PDF 已移动到失败目录: {failed_pdf}")

            return False

    def process_all_pending(self, use_ai: bool = False):
        """处理 inbox/ 中所有待处理的 PDF
        
        Args:
            use_ai: 是否启用 AI 增强提取
        """
        pdf_files = list(self.inbox_dir.glob("*.pdf"))

        if not pdf_files:
            self.log("inbox/ 中没有待处理的 PDF")
            return

        self.log(f"发现 {len(pdf_files)} 个待处理 PDF (AI增强: {use_ai})")

        success_count = 0
        for pdf in pdf_files:
            if self.process_pdf(pdf, use_ai=use_ai):
                success_count += 1

        self.log(f"处理完成: {success_count}/{len(pdf_files)} 成功")

        # 更新索引
        self.update_index()

    def watch(self):
        """监控 inbox/ 目录"""
        if not WATCHDOG_AVAILABLE:
            self.log("watchdog 未安装，无法使用监控模式", "ERROR")
            self.log("请安装: pip install watchdog", "INFO")
            sys.exit(1)

        class PDFHandler(FileSystemEventHandler):
            def __init__(self, pipeline):
                self.pipeline = pipeline

            def on_created(self, event):
                if not event.is_directory and event.src_path.endswith('.pdf'):
                    self.pipeline.log(f"检测到新 PDF: {event.src_path}")
                    # 延迟处理，等待文件写入完成
                    import time
                    time.sleep(2)
                    self.pipeline.process_pdf(Path(event.src_path))
                    self.pipeline.update_index()

        self.log(f"开始监控: {self.inbox_dir}")
        self.log("将新 PDF 放入 inbox/ 目录即可自动处理")
        self.log("按 Ctrl+C 停止")

        event_handler = PDFHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.inbox_dir), recursive=False)
        observer.start()

        try:
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            self.log("监控已停止")

        observer.join()


def main():
    parser = argparse.ArgumentParser(
        description="LLM-Wiki PDF 自动处理流水线"
    )
    parser.add_argument(
        "--wiki-dir",
        default=os.environ.get("LLM_WIKI_DIR", os.getcwd()),
        help="llm-wiki 目录路径 (默认: 当前目录或 LLM_WIKI_DIR 环境变量)"
    )
    parser.add_argument(
        "--marker-cmd",
        default="marker-pdf",
        help="marker-pdf 命令名称"
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--watch",
        action="store_true",
        help="监控模式: 持续监控 inbox/ 目录"
    )
    mode.add_argument(
        "--process",
        action="store_true",
        help="处理模式: 处理 inbox/ 中所有待处理 PDF"
    )
    mode.add_argument(
        "--file",
        help="处理单个 PDF 文件"
    )

    # AI 增强选项
    parser.add_argument(
        "--ai",
        action="store_true",
        help="启用 AI 增强提取（需要 KIMI_API_KEY 环境变量）"
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="强制禁用 AI 增强（使用启发式提取）"
    )

    args = parser.parse_args()

    # 确定是否使用 AI
    use_ai = args.ai
    if args.no_ai:
        use_ai = False

    # 初始化流水线
    pipeline = WikiPipeline(args.wiki_dir, args.marker_cmd)

    if args.watch:
        pipeline.watch()
    elif args.process:
        pipeline.process_all_pending(use_ai=use_ai)
    elif args.file:
        pipeline.process_pdf(Path(args.file), use_ai=use_ai)
        pipeline.update_index()


if __name__ == "__main__":
    main()
