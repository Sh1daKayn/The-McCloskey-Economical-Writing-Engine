# McCloskey Writing Agent

一个面向经济学论文写作与学术表达优化的 AI 工具包，灵感来自 Deirdre McCloskey 的《Economical Writing》。它的目标不只是把文字润色，而是帮助作者把冗长、抽象、被动、充满术语的表达，改写为清晰、直接、具体、具有说服力的作品，并进一步分析自己的写作风格与短板。

> “Writing is thinking.” 这句原则体现了 McCloskey 的核心观念：好的写作不是装饰，而是思考的清晰外化。

## 项目定位

这个仓库提供了一个更完整的写作工作流：

1. 文段优化：把原稿改写得更清楚、更有力
2. 风格诊断：分析当前写作风格、重复问题与潜在短板
3. 能力提升：给出具体练习与改进建议，帮助作者持续进步

## 4 维修改清单

| 维度 | 目标 | 示例改法 |
| --- | --- | --- |
| Audience | 让读者明确知道为什么这段话重要 | 用更直接的方式说明对象、背景与意义 |
| Sentence Structure | 以主动语态和清晰句法替代拖沓句子 | 把被动句改成明确的主语 + 动词 |
| Diction | 优先使用简单、准确的词汇 | 用普通词替代空泛术语 |
| Anti-AI Jargon | 去除虚假客观性、套话和修辞堆砌 | 删除“it is important to note that”这类空洞表达 |

## 工作流程

这个工具包的流程可以概括为三步：

- 输入一段 Markdown 草稿
- 由系统提示词驱动模型完成：改写、诊断、 coaching
- 输出一个结构化版本，包含修订稿、风格分析与提升建议

## 安装说明

1. 进入项目目录。
2. 安装依赖：

```bash
pip install openai
```

3. 设置 OpenAI API Key：

在 PowerShell 中：

```powershell
$env:OPENAI_API_KEY="your-key"
```

在 Bash 中：

```bash
export OPENAI_API_KEY="your-key"
```

## 使用方法

运行脚本将输入 Markdown 文件改写为输出文件：

```bash
python scripts/run_agent.py input.md output.md
```

脚本会读取 [prompts/system_prompt.md](prompts/system_prompt.md) 中的系统提示词，并将结果写入输出文件。

## 示例展示与解读

示例文件位于 [examples/ag_econ_case_study.md](examples/ag_econ_case_study.md)。它展示了三层内容：

- 修改前后的文段对比
- 对写作风格的诊断
- 针对短板的训练建议

### 示例解读

原始版本的问题通常包括：

- 把主体藏在抽象名词后面
- 用被动句掩盖动作和责任
- 用大量术语替代具体事实

改写后的版本则更强调：

- 明确的行为主体
- 主动语态与清晰节奏
- 具体场景与可见后果

## 项目结构

```text
.vscode/
  settings.json
prompts/
  system_prompt.md
examples/
  ag_econ_case_study.md
scripts/
  run_agent.py
```

## 适用场景

- 经济学论文初稿润色
- 研究报告与政策简报改写
- 学术写作训练与风格统一
- 用于提升文章的清晰度、节奏和说服力

## 设计原则

- 保留作者的原意，不随意改写结论
- 优先清晰、简洁、具体
- 用具体事实和可见行动替代抽象叙述
- 让句子像“思考”一样自然流出，而不是像“套模板”一样堆砌

