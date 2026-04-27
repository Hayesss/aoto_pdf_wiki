# LLM Wiki 摄入技能清单

> 本文件记录所有可用于向 LLM Wiki 摄入内容的技能和工具。
> 新增技能时在此登记，注明用途和存放路径。
> 完整评估见 skill: `llm-wiki-ingestion-toolchain`

## 已启用技能

### 1. YouTube 视频转录
- **技能**: youtube-content
- **用途**: 提取 YouTube 视频字幕，转为结构化内容（章节、摘要、博客格式）
- **输出**: raw/transcripts/youtube-<video-id>.md
- **前置**: `pip install youtube-transcript-api`
- **用法**: `python3 ~/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py "URL" --text-only --timestamps`

### 2. B站视频下载与转录
- **工具**: yt-dlp ⭐⭐⭐⭐⭐
- **用途**: 下载 B站视频音频/字幕，提取字幕文本
- **输出**: raw/transcripts/bilibili-<bvid>.md
- **安装**: `pixi add yt-dlp`
- **用法**:
  ```bash
  # 下载字幕（如有）
  pixi run yt-dlp --list-subs "https://www.bilibili.com/video/BVxxxxxx"
  pixi run yt-dlp --write-subs --sub-langs zh-CN --skip-download -o "raw/transcripts/bilibili-%(id)s.%(ext)s" "URL"
  
  # 无字幕时：下载音频后用 faster-whisper 转录
  pixi run yt-dlp -x --audio-format mp3 -o "raw/assets/bilibili-%(id)s.%(ext)s" "URL"
  pixi run python -m faster_whisper "raw/assets/bilibili-xxx.mp3" --model medium --language zh --output_format txt
  ```

### 3. RSS/博客监控
- **技能**: blogwatcher / feedparser ⭐⭐⭐⭐⭐
- **用途**: 监控博客和 RSS/Atom feed，新文章自动标出
- **输出**: 扫描结果列表，手动或自动摄入到 raw/articles/
- **前置**: `pixi add feedparser`（blogwatcher-cli 需另行安装）
- **用法**:
  ```bash
  blogwatcher-cli add "Blog Name" https://example.com
  blogwatcher-cli scan
  blogwatcher-cli articles  # 查看未读
  ```

### 4. 网页批量摄入
- **工具**: trafilatura ⭐⭐⭐⭐⭐ (替代 web_extract)
- **用途**: 提取网页正文为 markdown，批量保存
- **输出**: raw/articles/<描述性文件名>.md
- **安装**: `pixi add trafilatura markdownify`
- **用法**:
  ```bash
  pixi run python -c "
  import trafilatura, markdownify
  from trafilatura import fetch_url, extract
  downloaded = fetch_url('https://example.com/article')
  text = extract(downloaded, output_format='markdown')
  # 保存到 raw/articles/
  "
  ```

### 5. arXiv 论文
- **技能**: arxiv
- **用途**: 搜索和下载学术论文
- **输出**: raw/papers/<paper-id>.md 或 PDF
- **用法**:
  ```bash
  # 搜索
  给我 arxiv 论文 ID 或关键词，我用 arxiv skill 获取
  
  # 直接下载
  curl -L "https://arxiv.org/pdf/2401.00001.pdf" -o raw/papers/2401.00001.pdf
  ```

### 6. PDF 自动处理流水线 ⭐⭐⭐⭐⭐
- **工具**: marker-pdf + wiki_pipeline.py
- **用途**: 自动提取 PDF 文本，生成结构化笔记
- **输出**: raw/papers/*.md + papers/*.md
- **安装**: `pixi add --pypi marker-pdf`
- **用法**:
  ```bash
  # 监控模式（后台运行）
  pixi run python _meta/wiki_pipeline.py --watch
  
  # 批量处理 inbox/ 中所有 PDF
  pixi run python _meta/wiki_pipeline.py --process
  
  # 处理单个文件
  pixi run python _meta/wiki_pipeline.py --file raw/papers/paper.pdf
  ```

### 7. 音频转录 ⭐⭐⭐⭐⭐
- **工具**: faster-whisper
- **用途**: 音频/播客/无字幕视频转录为文本
- **输出**: raw/transcripts/*.md
- **安装**: `pixi add faster-whisper`
- **用法**:
  ```bash
  pixi run python -m faster_whisper audio.mp3 --model medium --output_format txt
  ```

## 待扩展技能

- [x] **播客/音频转录**: faster-whisper 已就绪
- [x] **PDF 批量提取**: marker-pdf + wiki_pipeline.py 已启用
- [ ] **微信文章**: 需处理防盗链，可能需要专用解析器
- [ ] **PDF OCR**: marker-pdf 已支持 OCR，需开启 `--ocr` 选项
- [ ] **自动定时摄入**: cronjob 定期扫描 RSS 和订阅源
- [ ] **来源去重**: 基于 URL 或内容 hash 的重复检测
- [ ] **AI 增强解析**: Kimi/Moonshot API 解析 PDF → 高质量 AIMRaD 笔记

## 摄入工作流速查

```
来源类型          →  工具/技能           →  存放路径
─────────────────────────────────────────────────────────
YouTube 视频      →  youtube-content     →  raw/transcripts/youtube-*.md
B站视频           →  yt-dlp              →  raw/transcripts/bilibili-*.md
网页文章          →  trafilatura         →  raw/articles/*.md
RSS/博客          →  blogwatcher         →  raw/articles/*.md
arXiv 论文        →  arxiv skill         →  raw/papers/*.md / *.pdf
PDF 文件          →  marker-pdf          →  raw/papers/*.md + papers/*.md
PDF 批量处理      →  wiki_pipeline.py    →  自动处理 inbox/ → raw/ + papers/
音频/播客         →  faster-whisper      →  raw/transcripts/*.md
图片/图表         →  直接存放            →  raw/assets/*
```

## 规范提醒

- 所有原始资料放入 `raw/` 对应子目录，**不修改原文**
- raw 文件必须带 frontmatter（source_url, ingested, sha256）
- 摄入后必须更新 index.md 和 log.md
- 视频/音频类来源优先提取**字幕/转录文本**，而非保存原始媒体文件
- PDF 处理优先使用 marker-pdf，扫描件开启 OCR 选项
- 优先使用 pixi 管理依赖：`pixi add <package>`，fallback 到 `pixi add --pypi <package>`
