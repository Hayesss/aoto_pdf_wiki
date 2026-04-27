# Wiki Schema

## Domain
LLM / AI Agent / 知识管理方法论（可扩展至通用 AI 基础设施与工具链）

## Conventions
- 文件名：全小写，连字符分隔，无空格（例：`transformer-architecture.md`）
- 每个 wiki 页面必须以 YAML frontmatter 开头
- 使用 `[[wikilinks]]` 在页面间建立链接（每页至少 2 个出站链接）
- 更新页面时必须修改 `updated` 日期
- 每个新页面必须按正确分区加入 `index.md`
- 每个动作必须追加到 `log.md`
- **来源标记**：当页面综合 3 个以上来源时，在段落末尾追加 `^[raw/articles/source-file.md]`，让读者能追溯到具体来源。单来源页面可仅用 frontmatter 中的 `sources` 字段。

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [来自下方 taxonomy]
sources: [raw/articles/source-name.md]
# 可选质量信号：
confidence: high | medium | low        # 主张的支持程度
contested: true                        # 存在未解决的矛盾时设置
contradictions: [other-page-slug]      # 与本页冲突的页面
---
```

`confidence` 与 `contested` 为可选字段，推荐用于观点性强或变化快的主题。lint 时会主动标出 `contested: true` 和 `confidence: low` 的页面供复查。

### raw/ Frontmatter
原始资料也需 frontmatter，用于检测重复摄入和内容漂移：

```yaml
---
source_url: https://example.com/article   # 原始 URL（如有）
ingested: YYYY-MM-DD
sha256: <正文内容的 hex 摘要>
---
```

`sha256` 基于正文（`---` 之后的内容）计算。再次摄入同一 URL 时重新计算并比对：相同则跳过，不同则标记漂移并更新。

## Tag Taxonomy
新增标签前必须先在此登记，防止标签膨胀。

### 模型与架构
- `model` — 具体模型（GPT-4, Claude, LLaMA 等）
- `architecture` — 架构设计（Transformer, MoE, Diffusion 等）
- `benchmark` — 评测基准与方法
- `training` — 训练方法、流程、基础设施

### 技术与方法
- `optimization` — 优化算法与效率提升
- `fine-tuning` — 微调技术（SFT, LoRA, QLoRA 等）
- `inference` — 推理加速、部署、服务化
- `alignment` — 对齐技术（RLHF, DPO, Constitutional AI 等）
- `prompt-engineering` — 提示工程
- `rag` — 检索增强生成

### Agent 与系统
- `agent` — AI Agent 架构与设计
- `tool-use` — 工具调用与外部系统交互
- `multi-agent` — 多智能体系统
- `workflow` — 工作流编排

### 数据与评估
- `data` — 数据集、数据工程、合成数据
- `evaluation` — 评估方法论
- `interpretability` — 可解释性

### 组织与人物
- `person` — 研究人员、工程师
- `company` — 公司、实验室
- `open-source` — 开源项目与社区

### 元信息
- `comparison` — 对比分析
- `timeline` — 时间线与里程碑
- `controversy` — 争议与讨论
- `prediction` — 预测与趋势判断
- `methodology` — 知识管理方法论

## Page Thresholds
- **新建页面**：实体/概念在 2 个以上来源中出现，或在单个来源中处于核心位置
- **并入现有页面**：来源提及的内容已有对应页面时，追加到该页面
- **不新建页面**：仅被顺带提及、细节过于琐碎、或超出当前 Domain 范围的内容
- **拆分页面**：页面超过约 200 行时，拆分为子主题并建立交叉链接
- **归档页面**：内容被完全替代时，移至 `_archive/`，并从 index.md 移除

## Entity Pages
每个值得记录的实体单独成页，包含：
- 概述 / 定义
- 关键事实与时间节点
- 与其他实体的关系（[[wikilinks]]）
- 来源引用

## Concept Pages
每个概念或主题单独成页，包含：
- 定义 / 解释
- 当前知识状态
- 开放问题或争议
- 相关概念（[[wikilinks]]）

## Comparison Pages
并排分析，包含：
- 对比对象与对比目的
- 对比维度（优先表格形式）
- 结论或综合判断
- 来源

## Update Policy
新信息与现有内容冲突时的处理流程：
1. 核对日期 — 较新的来源通常优先
2. 若确实矛盾，记录双方立场并标注日期和来源
3. 在 frontmatter 标记：`contradictions: [page-name]`
4. 在 lint 报告中标记供用户复查
5. **绝不直接覆盖旧信息** — 追加、标注、标记冲突
