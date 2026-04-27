# Auto PDF Wiki

基于 [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式构建的自动化知识库系统，专注于 PDF 论文的自动提取、结构化与知识管理。

## 定位
- **不是一次性笔记仓库**，而是可持续迭代、自我交叉引用的知识系统
- **与 RAG 的区别**：RAG 每次查询重新发现知识，Wiki 编译一次并持续维护
- **自动化优先**：PDF 放入 inbox/ 即可自动提取、结构化、建立索引
- 矛盾已标记，交叉引用已建立，综合反映所有已摄入来源

## 核心功能

### 1. PDF 自动处理流水线
```bash
# 监控模式：后台运行，自动处理新放入的 PDF
pixi run watch-inbox

# 批量处理：处理 inbox/ 中所有待处理 PDF
pixi run process-pdfs

# 处理单个文件
pixi run python _meta/wiki_pipeline.py --file paper.pdf
```

**处理流程**：
```
PDF → inbox/ → marker-pdf 提取 → raw/papers/*.md → 结构化笔记 → papers/*.md
```

### 2. 多来源内容采集
| 来源类型 | 工具 | 存放路径 |
|----------|------|----------|
| PDF 论文 | marker-pdf + wiki_pipeline.py | raw/papers/ + papers/ |
| YouTube 视频 | yt-dlp | raw/transcripts/youtube-*.md |
| B站视频 | yt-dlp + faster-whisper | raw/transcripts/bilibili-*.md |
| 网页文章 | trafilatura | raw/articles/*.md |
| RSS/博客 | feedparser | raw/articles/*.md |
| arXiv 论文 | arxiv skill | raw/papers/*.pdf |
| 音频/播客 | faster-whisper | raw/transcripts/*.md |

### 3. 结构化笔记生成
自动提取 AIMRaD 结构：
- **Abstract** - 摘要
- **Introduction** - 背景与目的
- **Methods** - 方法概述
- **Results** - 主要发现
- **Discussion** - 讨论与结论

## 快速开始

### 前置要求
- [pixi](https://pixi.sh/) 包管理器
- Python >= 3.11
- (可选) Kimi/Moonshot API Key 用于 AI 增强解析

### 安装

```bash
# 克隆仓库
git clone git@github.com:Hayesss/aoto_pdf_wiki.git
cd aoto_pdf_wiki

# 安装所有依赖
pixi install

# 验证安装
pixi run python -c "import trafilatura, feedparser, pypdf; print('OK')"
```

### 使用

```bash
# 1. 将 PDF 放入 inbox/ 目录
cp ~/Downloads/paper.pdf inbox/

# 2. 批量处理
pixi run process-pdfs

# 3. 或启动监控模式（自动处理新文件）
pixi run watch-inbox

# 4. 用 Obsidian 打开此目录作为 Vault 查看结果
```

## 目录结构

```
aoto_pdf_wiki/
├── README.md           # 本文件
├── SCHEMA.md           # 规范、标签体系、Domain 定义
├── index.md            # 分区内容目录
├── log.md              # 操作日志（仅追加）
├── pixi.toml           # pixi 环境配置
├── inbox/              # 待处理 PDF 放入此处
├── processed/          # 已处理的 PDF 归档
├── failed/             # 处理失败的 PDF
├── _meta/              # 元信息与自动化脚本
│   ├── wiki_pipeline.py        # PDF 自动处理流水线
│   ├── ingestion-skills.md     # 摄入技能清单
│   └── skill-recommendations.md # 扩展推荐
├── _templates/         # 页面模板
│   ├── concept-template.md
│   └── query-template.md
├── raw/                # Layer 1: 原始资料（只读，不覆盖）
│   ├── articles/       # 网页文章、剪报
│   ├── papers/         # 论文、PDF 提取内容
│   ├── transcripts/    # 视频/播客转录、会议记录
│   └── assets/         # 图片、图表
├── entities/           # Layer 2: 实体页面
├── concepts/           # Layer 2: 概念页面
├── comparisons/        # Layer 2: 对比分析
└── queries/            # Layer 2: 有价值的查询结果
```

## 工具链

| 工具 | 用途 | 安装 | 推荐度 |
|------|------|------|--------|
| marker-pdf | PDF→Markdown 高质量提取 | `pixi add --pypi marker-pdf` | ⭐⭐⭐⭐⭐ |
| yt-dlp | 视频下载/字幕提取 | `pixi add yt-dlp` | ⭐⭐⭐⭐⭐ |
| trafilatura | 网页正文提取 | `pixi add trafilatura` | ⭐⭐⭐⭐⭐ |
| faster-whisper | 音频转文字 | `pixi add faster-whisper` | ⭐⭐⭐⭐⭐ |
| feedparser | RSS/Feed 解析 | `pixi add feedparser` | ⭐⭐⭐⭐⭐ |
| pypdf | 轻量 PDF 读取 | `pixi add pypdf` | ⭐⭐⭐⭐ |
| markdownify | HTML→Markdown | `pixi add markdownify` | ⭐⭐⭐⭐ |
| notion-client | Notion 同步 | `pip install notion-client` | ⭐⭐⭐ |

完整评估见 skill: `llm-wiki-ingestion-toolchain`

## 工作流

1. **摄入 (ingest)** — 将来源放入对应目录，自动或手动提取要点
2. **处理 (process)** — PDF 自动提取、网页批量摄入、音频转录
3. **查询 (query)** — 基于已编译知识回答问题，有价值的答案归档到 queries/
4. **整理 (lint)** — 定期检查孤儿页面、断链、过期内容、标签合规性

## 规范速查
- 文件名：小写连字符（`transformer-architecture.md`）
- 每页必须有 frontmatter（title/created/updated/type/tags/sources）
- 每页至少 2 个 `[[wikilinks]]` 出站链接
- 标签必须来自 SCHEMA.md taxonomy
- 更新页面时修改 `updated` 日期
- 矛盾信息不覆盖，追加并标记 `contradictions:`

## 自动化任务

```bash
# 定义在 pixi.toml 中
pixi run process-pdfs    # 处理 inbox/ 中所有 PDF
pixi run watch-inbox     # 监控 inbox/ 目录
pixi run update-index    # 更新索引
```

## AI 增强（可选）

配置 Kimi/Moonshot API 实现更高质量的笔记生成：

```yaml
# _meta/config.yaml
moonshot_api_key: sk-xxx
```

启用后，PDF 处理流程变为：
```
PDF → pypdf 读取文本 → Kimi API 解析 → 高质量 AIMRaD 笔记
```

## 路线图

- [x] Phase 1: 基础工具链（marker-pdf, pixi, wiki_pipeline.py）
- [x] Phase 2: 扩展来源（yt-dlp, trafilatura, faster-whisper）
- [ ] Phase 3: AI 增强（Kimi API 解析）
- [ ] Phase 4: 自动化（cronjob 定时扫描）
- [ ] Phase 5: 来源去重与漂移检测

## 参考

- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [llm-wiki-ingestion-toolchain skill](https://github.com/Hayesss/aoto_pdf_wiki/blob/main/_meta/skill-recommendations.md)

---

*维护者：Hermes Agent + 人类策展*
