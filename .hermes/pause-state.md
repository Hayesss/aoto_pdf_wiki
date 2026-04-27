# LLM-Wiki 项目暂停文档

> **状态**: Phase 3 已完成，Phase 4/5 待启动  
> **暂停时间**: 2026-04-27  
> **最后提交**: `9d31c3e` (chore: add __pycache__ to gitignore)

---

## 已完成工作

### Phase 1-2: 基础设施 (已完成)
- [x] marker-pdf 集成（PDF 文本提取）
- [x] 启发式内容提取（AIMRaD 结构）
- [x] 实体识别（蛋白、细胞类型、通路、方法）
- [x] 索引自动生成
- [x] GitHub 仓库同步

### Phase 3: Kimi AI 增强 (已完成)
- [x] `ai_enhancer.py` — Kimi API 客户端
  - 自动重试（3 次，指数退避）
  - 429/402 错误识别
  - 文本截断（保留头尾）
  - 流式输出支持
  - 批量处理
  - 统计信息
- [x] Prompt 模板系统
  - `prompts/aimrad.txt` — AIMRaD 精炼
  - `prompts/entity_extraction.txt` — 实体提取
- [x] Pipeline 集成
  - `--ai` 启用 AI 增强
  - `--no-ai` 强制启发式提取
  - Fallback 自动降级
- [x] 端到端测试通过
  - 所有 AIMRaD 字段提取成功
  - 实体识别准确率验证

---

## 当前项目结构

```
llm-wiki/
├── inbox/                  # 待处理 PDF 放入此处
├── processed/              # 处理完成的 PDF
├── failed/                 # 处理失败的 PDF
├── raw/papers/             # marker-pdf 提取的原始文本
├── papers/                 # AI 增强的结构化笔记
├── _meta/
│   ├── ai_enhancer.py      # Kimi API 客户端
│   ├── wiki_pipeline.py    # 主处理流水线
│   ├── test_ai_pipeline.py # 端到端测试
│   ├── config.json         # 配置模板
│   ├── prompts/
│   │   ├── aimrad.txt      # AIMRaD 精炼 prompt
│   │   └── entity_extraction.txt
│   └── verify-setup.py     # 环境验证
├── index.md                # 论文索引（自动生成）
├── log.md                  # 处理日志
└── .gitignore
```

---

## 待启动工作

### Phase 4: RSS 定时扫描 (计划中)
**目标**: 自动监控学术博客和预印本更新

**待实现**:
- [ ] `rss_watcher.py` — RSS/Atom feed 解析器
- [ ] 支持 feed 源:
  - arXiv 特定分类 (cs.LG, cs.CL, q-bio.GN)
  - Distill.pub
  - OpenAI Blog
  - Google Research Blog
  - 自定义 OPML 导入
- [ ] 内容去重（URL + 标题 hash）
- [ ] 自动摄入新文章到 inbox/
- [ ] cronjob 定时任务（每 6 小时）
- [ ] 通知机制（可选：Telegram/Discord webhook）

**技术选型**:
- `feedparser` — RSS/Atom 解析
- `cronjob` — 定时调度
- `sqlite` — 本地已处理 URL 数据库

**预估工时**: 2-3 小时

---

### Phase 5: 去重与内容漂移检测 (计划中)
**目标**: 防止重复摄入，检测内容更新

**待实现**:
- [ ] `dedup.py` — 去重引擎
  - URL sha256 去重（已有基础）
  - 标题相似度检测（fuzzy matching）
  - 内容指纹（simhash/minhash）
- [ ] `content_db.json` — 内容元数据数据库
  - 摄入时间、来源、版本
  - 内容 hash、标题、作者
- [ ] 漂移检测
  - 定期重抓取已处理内容
  - 对比 hash 检测更新
  - 版本链管理（v1 → v2）
- [ ] 冲突解决策略
  - 保留最新版本
  - 标记修订历史

**技术选型**:
- `difflib` / `fuzzywuzzy` — 文本相似度
- `simhash` — 内容指纹
- `json` — 本地数据库

**预估工时**: 3-4 小时

---

## 环境配置备忘

### 必需环境变量
```bash
# Kimi API（AI 增强功能必需）
export KIMI_API_KEY="sk-..."

# 可选：自定义 wiki 目录
export LLM_WIKI_DIR="/mnt/i/projects/obsidian_projects/llm-wiki"
```

### 依赖工具
- `marker-pdf` — 安装在系统 Python 3.12
- `python3` — 运行 pipeline（WSL 自带）
- `git` — 版本控制

### 验证环境
```bash
cd /mnt/i/projects/obsidian_projects/llm-wiki/_meta
python3 verify-setup.py
```

---

## 快速恢复指南

### 1. 验证当前状态
```bash
cd /mnt/i/projects/obsidian_projects/llm-wiki
git log --oneline -5
python3 _meta/test_ai_pipeline.py
```

### 2. 处理新 PDF（手动）
```bash
# 放入 inbox
cp new_paper.pdf inbox/

# 启用 AI 增强处理
cd _meta
export KIMI_API_KEY="sk-..."
python3 wiki_pipeline.py --process --ai
```

### 3. 继续开发 Phase 4
```bash
# 从计划文档恢复上下文
cat .hermes/plans/2026-04-27_llm-wiki-phase-3-5.md
```

---

## 已知问题

| 问题 | 状态 | 解决方案 |
|------|------|----------|
| marker-pdf 需系统 Python 3.12 | 已解决 | 显式调用 `python3.12 -m marker` |
| Kimi API 余额不足 | 已解决 | 账户已充值 |
| 长文本截断可能丢失信息 | 已知 | 保留头尾 60/40，未来可优化为智能分段 |
| 启发式提取准确率有限 | 已知 | AI 增强模式已解决 |

---

## 关键文件路径

| 文件 | 路径 |
|------|------|
| 主流水线 | `_meta/wiki_pipeline.py` |
| AI 增强器 | `_meta/ai_enhancer.py` |
| 配置文件 | `_meta/config.json` |
| Prompt 模板 | `_meta/prompts/` |
| 测试脚本 | `_meta/test_ai_pipeline.py` |
| 实施计划 | `.hermes/plans/2026-04-27_llm-wiki-phase-3-5.md` |
| 本暂停文档 | `.hermes/pause-state.md` |

---

## 联系/恢复

要继续项目：
1. 查看实施计划: `.hermes/plans/2026-04-27_llm-wiki-phase-3-5.md`
2. 运行测试验证: `python3 _meta/test_ai_pipeline.py`
3. 选择继续 Phase 4 或 Phase 5

---

*文档由 Hermes Agent 自动生成于 2026-04-27*
