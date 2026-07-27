# McCloskey Writing Agent

一个面向经济学论文写作与学术表达优化的 AI 工具包，灵感来自 Deirdre McCloskey 的《Economical Writing》。它的目标是帮助作者把冗长、抽象、被动、充满术语的文字，改写为清晰、直接、具体、具有说服力的表达。

> “Writing is thinking.” 这句原则体现了 McCloskey 的核心观念：好的写作不是装饰，而是思考的清晰外化。

## 项目定位

这个仓库提供了三个核心部分：

- 可复用的系统提示词，指导模型按 McCloskey 的写作标准进行修改
- 一个农业经济与供应链领域的示例案例，展示“差异化改写”效果
- 一个轻量级 Python 脚本，用于把 Markdown 草稿送入模型并输出重写结果

## 4 维修改清单

| 维度 | 目标 | 示例改法 |
| --- | --- | --- |
| Audience | 让读者明确知道为什么这段话重要 | 用更直接的方式说明对象、背景与意义 |
| Sentence Structure | 以主动语态和清晰句法替代拖沓句子 | 把被动句改成明确的主语 + 动词 |
| Diction | 优先使用简单、准确的词汇 | 用普通词替代空泛术语 |
| Anti-AI Jargon | 去除虚假客观性、套话和修辞堆砌 | 删除“it is important to note that”这类空洞表达 |

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
