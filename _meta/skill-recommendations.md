# LLM Wiki 扩展技能推荐清单

> 本文件记录可用于增强 LLM Wiki 知识库维护的扩展技能和自动化方案。
> 分为「已集成」「推荐集成」「待评估」三类。
> 完整评估见 skill: `llm-wiki-ingestion-toolchain`

---

## 已集成技能（7 项）

| # | 技能/工具 | 用途 | 状态 | 安装方式 |
|---|-----------|------|------|----------|
| 1 | youtube-content | YouTube 字幕提取 | ✅ 就绪 | pip |
| 2 | yt-dlp | B站/视频下载 | ✅ 推荐 | `pixi add yt-dlp` |
| 3 | blogwatcher | RSS/博客监控 | ✅ 技能就绪 | pip |
| 4 | trafilatura | 网页批量摄入 | ✅ 推荐 | `pixi add trafilatura` |
| 5 | arxiv | 论文搜索下载 | ✅ 技能就绪 | 内置 |
| 6 | marker-pdf | PDF 高质量提取 | ✅ 已使用 | `pixi add --pypi marker-pdf` |
| 7 | faster-whisper | 音频转录 | ✅ 推荐 | `pixi add faster-whisper` |

---

## 强烈推荐集成（3 项）

### 8. PDF 自动处理流水线（wiki_pipeline.py）⭐⭐⭐⭐⭐
- **用途**: 自动监控 inbox/ 目录，处理新 PDF
- **场景**: 
  - 监控模式：后台运行，自动处理新放入的 PDF
  - 批量模式：处理 inbox/ 中所有待处理 PDF
  - 生成结构化笔记（AIMRaD）并更新索引
- **存放**: `_meta/wiki_pipeline.py`
- **依赖**: marker-pdf, watchdog
- **用法**:
  ```bash
  pixi run python _meta/wiki_pipeline.py --watch    # 监控模式
  pixi run python _meta/wiki_pipeline.py --process  # 批量处理
  ```

### 9. AI 增强解析（Kimi/Moonshot API）⭐⭐⭐⭐⭐
- **用途**: 用 AI 替代启发式提取，生成高质量结构化笔记
- **场景**: 
  - PDF → pypdf 读取文本 → Kimi API 解析 → AIMRaD 笔记
  - 自动提取实体、标签、交叉链接
- **优势**: 比 marker-pdf + 本地脚本理解更深，输出质量更高
- **配置**: 在 `_meta/config.yaml` 存放 `MOONSHOT_API_KEY`
- **优先级**: ⭐⭐⭐⭐⭐

### 10. 自动定时摄入（cronjob）⭐⭐⭐⭐
- **用途**: 定期扫描订阅源，自动摄入新内容
- **场景**: 
  - 每天扫描 RSS，新文章自动摄入
  - 每周扫描 arXiv 关键词，新论文自动下载
  - 每月运行 lint，生成健康报告
- **实现**: Hermes 内置 cronjob 工具
- **优先级**: ⭐⭐⭐⭐

---

## 可选增强（5 项）

### 11. Webhook 自动摄入（webhook-subscriptions）
- **用途**: 外部服务推送内容到 wiki
- **场景**: 
  - GitHub 新 star 的 repo 自动摄入
  - RSS 新文章自动触发摄入
  - 浏览器插件发送网页到 wiki
- **原理**: 外部服务 POST → webhook → agent 自动摄入
- **优先级**: ⭐⭐⭐

### 12. 微信文章解析
- **用途**: 提取微信公众号文章
- **场景**: 中文技术博客、行业分析
- **挑战**: 防盗链、需要 Cookie 或专用解析器
- **方案**: 使用 wechat-spider 或手动复制链接用 trafilatura
- **优先级**: ⭐⭐⭐

### 13. Notion 双向同步（notion skill）
- **用途**: 将 wiki 内容同步到 Notion 数据库
- **场景**: 团队协作、移动端查看
- **安装**: `pip install notion-client`
- **优先级**: ⭐⭐⭐

### 14. X/Twitter 监控（xurl skill）
- **用途**: 监控特定账号或关键词的推文
- **场景**: 跟踪研究者、公司的最新动态
- **优先级**: ⭐⭐⭐

### 15. 来源去重与漂移检测
- **用途**: 避免重复摄入，检测原文变更
- **实现**: 
  - 基于 URL 去重（已存在于 raw/ 则跳过）
  - 基于 sha256 检测内容漂移
  - 已在 SCHEMA.md 中定义 frontmatter 规范
- **优先级**: ⭐⭐⭐

---

## 推荐集成路线图（更新）

```
Phase 1（现在）: 基础工具链就绪
  ├─ pixi 环境配置完成
  ├─ marker-pdf + wiki_pipeline.py 启用
  ├─ faster-whisper 安装就绪
  └─ 更新 _meta/ingestion-skills.md

Phase 2（本周）: AI 增强 + 自动化
  ├─ 配置 Kimi API 密钥
  ├─ 更新 wiki_pipeline.py 支持 API 解析
  └─ 配置 cronjob 定期扫描 RSS

Phase 3（本月）: 扩展来源
  ├─ Webhook 接收浏览器推送
  ├─ 微信文章解析方案
  └─ 来源去重实现

Phase 4（持续）: 维护优化
  ├─ 定期 lint 报告
  ├─ 索引自动更新
  └─ 知识图谱可视化
```

---

## 工具链评估速查表

| 工具 | pixi | pip | 推荐度 | llm-wiki 角色 |
|------|------|-----|--------|---------------|
| marker-pdf | ❌ | ✅ | ⭐⭐⭐⭐⭐ | PDF→Markdown 核心 |
| yt-dlp | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 视频下载/字幕 |
| trafilatura | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 网页提取 |
| faster-whisper | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 音频转录 |
| feedparser | ✅ | ✅ | ⭐⭐⭐⭐⭐ | RSS 解析 |
| pypdf | ✅ | ✅ | ⭐⭐⭐⭐ | PDF 轻量读取 |
| markdownify | ✅ | ✅ | ⭐⭐⭐⭐ | HTML→MD |
| notion-client | ❌ | ✅ | ⭐⭐⭐ | Notion 同步 |
| you-get | ❌ | ✅ | ⭐⭐⭐ | 国内平台补充 |
| bilibili-api-python | ❌ | ✅ | ⭐⭐⭐ | B站 API |
| pdfplumber | ❌ | ✅ | ⭐⭐⭐ | 表格提取 |
| readability-lxml | ❌ | ✅ | ⭐⭐⭐ | 可被替代 |
| openai-whisper | ❌ | ✅ | ⭐⭐⭐ | 备选转录 |
| podcastparser | ❌ | ✅ | ⭐⭐ | 可被覆盖 |
| newspaper3k | ❌ | ✅ | ⭐⭐ | 不推荐新用 |

---

## 当前待扩展技能（来自 ingestion-skills.md）

- [x] **播客/音频转录**: faster-whisper 已就绪
- [x] **PDF 批量提取**: marker-pdf + wiki_pipeline.py 已启用
- [ ] **微信文章**: 需处理防盗链，可能需要专用解析器
- [ ] **PDF OCR**: marker-pdf 已支持 OCR，需开启 `--ocr` 选项
- [ ] **自动定时摄入**: cronjob 定期扫描 RSS 和订阅源
- [ ] **来源去重**: 基于 URL 或内容 hash 的重复检测
- [ ] **AI 增强解析**: Kimi/Moonshot API 解析 PDF → 高质量 AIMRaD 笔记
