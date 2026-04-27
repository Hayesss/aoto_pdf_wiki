# LLM-Wiki Phase 3-5 实施计划

> 创建时间: 2026-04-27
> 目标: 实现 AI 增强解析、RSS 定时扫描、来源去重与漂移检测

---

## 目标

1. **Kimi/Moonshot API 集成** — AI 增强 PDF 解析，生成高质量 AIMRaD 结构化笔记
2. **cronjob 定时扫描 RSS** — 自动化内容采集流水线
3. **来源去重与漂移检测** — 防止重复摄入，检测内容变更

---

## 当前上下文

- 项目: `/mnt/i/projects/obsidian_projects/llm-wiki`
- 包管理: pixi (Python 3.13) + 系统 Python 3.12 (marker-pdf)
- 核心脚本: `_meta/wiki_pipeline.py` (PDF 处理)
- 配置文件: `_meta/config.yaml` (已创建，待扩展)
- 验证脚本: `_meta/verify-setup.py` (6/6 通过)
- GitHub: `Hayesss/aoto_pdf_wiki` (main 分支已推送)

---

## 计划 A: Kimi/Moonshot API 集成 (Phase 3)

### 概述
使用 Kimi API 替代/增强 marker-pdf 的启发式提取，直接输出结构化 AIMRaD 笔记。

### 方案对比

| 方案 | 描述 | 优点 | 缺点 | 推荐度 |
|------|------|------|------|--------|
| A1: 纯 API | PDF → pypdf 读文本 → Kimi API → 笔记 | 高质量结构化输出 | 依赖 API 可用性、费用 | ⭐⭐⭐⭐ |
| A2: 混合 | marker-pdf 提取 → Kimi 精炼 → 笔记 | 结合两者优势 | 流程复杂 | ⭐⭐⭐⭐⭐ |
| A3: 本地 LLM | 用 llama.cpp 本地模型解析 | 无费用、隐私好 | 质量不如 API、需 GPU | ⭐⭐⭐ |

**推荐: A2 混合方案**

### 实施步骤

1. **扩展 `config.yaml`**
   ```yaml
   moonshot_api_key: sk-xxx
   moonshot_base_url: https://api.moonshot.cn/v1
   moonshot_model: kimi-latest
   ai_enhancement: true  # 是否启用 AI 增强
   ```

2. **创建 `_meta/ai_enhancer.py`**
   - 封装 Kimi API 调用
   - 实现 `enhance_paper_note(raw_text: str) -> dict` 函数
   - 输出 AIMRaD 结构: Abstract/Introduction/Methods/Results/Discussion
   - 提取实体、关键词、交叉引用建议
   - 错误处理: API 失败时回退到启发式提取

3. **修改 `wiki_pipeline.py`**
   - 在 `extract_structured_content()` 后添加 AI 增强分支
   - 如果 `ai_enhancement: true` 且 API key 存在，调用 `_meta/ai_enhancer.py`
   - 保留启发式提取作为 fallback

4. **Prompt 工程**
   - 设计结构化提取 prompt（保存在 `_meta/prompts/`）
   - 要求输出 JSON 格式，包含 AIMRaD 字段
   - 包含示例 few-shot

5. **成本与缓存**
   - 基于 sha256 缓存 API 结果，避免重复调用
   - 记录 token 使用量到 `log.md`

### 文件变更

- `_meta/config.yaml` — 添加 API 配置
- `_meta/ai_enhancer.py` — 新建
- `_meta/prompts/paper_extraction.md` — 新建
- `_meta/wiki_pipeline.py` — 修改，集成 AI 分支
- `pixi.toml` — 添加 `openai` 或 `httpx` 依赖（Kimi API 兼容 OpenAI SDK）

---

## 计划 B: cronjob 定时扫描 RSS (Phase 4)

### 概述
使用 `feedparser` + `cronjob` 工具定期扫描 RSS/Atom feed，自动摄入新文章。

### 实施步骤

1. **创建 `_meta/rss_watcher.py`**
   - 读取订阅列表（`_meta/subscriptions.yaml`）
   - 解析 feed，提取新文章（基于 `pubDate` + URL hash）
   - 用 `trafilatura` 提取正文
   - 保存到 `raw/articles/`，生成 frontmatter
   - 更新索引

2. **创建 `_meta/subscriptions.yaml`**
   ```yaml
   feeds:
     - name: " distill.pub"
       url: "https://distill.pub/rss.xml"
       tags: ["visualization", "ml"]
     - name: "OpenAI Blog"
       url: "https://openai.com/blog/rss.xml"
       tags: ["openai", "announcement"]
   ```

3. **配置 cronjob**
   ```bash
   # 每 6 小时扫描一次
   cronjob create --name rss-scan --schedule "0 */6 * * *" \
     --prompt "cd /mnt/i/projects/obsidian_projects/llm-wiki && pixi run python _meta/rss_watcher.py"
   ```

4. **去重机制**
   - 基于 URL sha256 检测重复
   - 已处理 URL 记录到 `_meta/processed_urls.json`

### 文件变更

- `_meta/rss_watcher.py` — 新建
- `_meta/subscriptions.yaml` — 新建
- `_meta/processed_urls.json` — 新建（自动维护）
- `pixi.toml` — 确认 `feedparser` 已存在

---

## 计划 C: 来源去重与漂移检测 (Phase 5)

### 概述
防止同一来源被重复摄入，检测已摄入内容是否发生变更（内容漂移）。

### 实施步骤

1. **建立内容指纹系统**
   - 每个 raw 文件 frontmatter 中已有 `sha256` 字段
   - 扩展为 `_meta/content_db.json`:
     ```json
     {
       "sha256": "abc123...",
       "source_url": "https://...",
       "ingested": "2026-04-27",
       "file_path": "raw/articles/xxx.md",
       "version": 1
     }
     ```

2. **去重检测**
   - 摄入前计算内容 sha256
   - 查询 `content_db.json`
   - 如果存在 → 跳过，记录 "duplicate skipped"
   - 如果不存在 → 继续处理

3. **漂移检测**
   - 定期（每周）重新抓取已标记的来源 URL
   - 计算新 sha256，与旧值比对
   - 如果不同 → 标记 `drift_detected: true`，创建新版本
   - 旧版本保留在 `raw/articles/xxx_v1.md`，新版本 `xxx_v2.md`
   - 在 frontmatter 中记录 `previous_version: xxx_v1.md`

4. **手动触发**
   ```bash
   pixi run check-drift    # 检查所有来源的漂移
   pixi run dedup           # 手动去重扫描
   ```

### 文件变更

- `_meta/content_db.json` — 新建（内容指纹数据库）
- `_meta/dedup.py` — 新建（去重 + 漂移检测逻辑）
- `_meta/wiki_pipeline.py` — 修改，摄入前调用去重检查
- `pixi.toml` — 添加 `check-drift` 和 `dedup` tasks

---

## 实施优先级与时间表

| 阶段 | 任务 | 预估工时 | 依赖 |
|------|------|----------|------|
| Phase 3 | Kimi API 集成 | 4-6h | 需 API key |
| Phase 4 | RSS cronjob | 2-3h | Phase 3 可选 |
| Phase 5 | 去重与漂移 | 3-4h | Phase 4 可选 |

**推荐顺序**: Phase 3 → Phase 4 → Phase 5（串行，降低复杂度）

---

## 风险与对策

| 风险 | 影响 | 对策 |
|------|------|------|
| Kimi API 费用 | 高 | 添加 token 预算限制，超限时自动关闭 AI 增强 |
| API 不可用 | 中 | 始终保留启发式 fallback |
| RSS 源失效 | 低 | 记录失败次数，超过 3 次自动暂停该源 |
| content_db 膨胀 | 低 | 定期归档旧记录到 `_meta/archive/` |

---

## 下一步行动

1. **确认 Kimi API key** — 用户需提供 `sk-xxx` 或确认使用其他模型
2. **确认 RSS 订阅源** — 用户提供想监控的博客/feed 列表
3. **开始 Phase 3 实施** — 创建 `_meta/ai_enhancer.py` 和 prompt

---

*计划保存于: `.hermes/plans/2026-04-27_llm-wiki-phase-3-5.md`*
