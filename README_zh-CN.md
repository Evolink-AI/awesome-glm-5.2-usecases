<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="GLM-5.2 高信号使用案例仓库 banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=badge&utm_campaign=awesome-glm-5.2-usecases)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=badge&utm_campaign=awesome-glm-5.2-usecases)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

# GLM-5.2 高信号使用案例仓库

## 🍌 介绍

欢迎来到 GLM-5.2 高信号使用案例仓库。

**我们从公开 demo 和创作者社区整理 GLM-5.2 的真实使用案例、教程、集成、评测、价格信号和限制。**

这份简体中文 README 聚焦有具体工作流、公开 benchmark 证据、上手 demo、集成方式、成本信息或实践 caveat 的案例。

每个案例标题都会链接到公开来源，作者 handle 会链接到创作者主页。

[在 Evolink 上试用 GLM-5.2](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 总览

- **99 个精选 GLM-5.2 案例**，来自公开创作者、评测团队、工具开发者、服务商和一线使用者。
- 覆盖基准与前沿评测、编码代理与长上下文工作流、上手演示与作品展示、供应商与工具集成、成本、定价与本地部署、限制、注意事项与安全信号。
- 每个案例都包含原始来源、创作者署名、简洁的使用结论、证据类型和发布日期。
- 你可以用这个 repo 查找实用工作流、比较优势和限制、发现供应商路径，并跟踪真实上手实验。

> [!NOTE]
> 本仓库重视具体证据，而不是 hype：已发布 demo、benchmark 方法、集成笔记、成本数据和明确 caveat。

> [!NOTE]
> 多语言 README 会保持与英文源相同的案例顺序、链接、anchor 和署名；为了可追溯性，部分标题会保留接近原文的写法。

<a id="-quick-api-access"></a>
## ⚡ 快速 API 接入

通过 Evolink 的 OpenAI 兼容 Chat Completions API 使用 GLM-5.2。先在 [Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases) 获取 API key，然后在执行请求前设置为 `EVOLINK_API_KEY`。

```bash
export EVOLINK_API_KEY="your_api_key_here"

curl --request POST \
  --url https://direct.evolink.ai/v1/chat/completions \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "glm-5.2",
    "messages": [
      {
        "role": "user",
        "content": "Please introduce yourself"
      }
    ]
  }'
```

阅读完整 GLM-5.2 API 参考：[打开 GLM-5.2 API docs](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api).

## 📑 目录

| 章节 | 案例 |
|---|---|
| [📏 基准与前沿评测](#benchmarks-frontier-evaluation) | 案例 1-12, 60, 70, 72, 76, 90, 94 |
| [💻 编码代理与长上下文工作流](#coding-agents-long-context-workflows) | 案例 13-22, 62, 65, 66, 77, 80, 91 |
| [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds) | 案例 23-30, 71, 78, 81-82, 92, 99 |
| [🔌 供应商与工具集成](#provider-tool-integrations) | 案例 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96 |
| [💸 成本、定价与本地部署](#cost-pricing-local-deployment) | 案例 43-51, 64, 68, 88-89, 97-98 |
| [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals) | 案例 52-59, 67, 73, 75 |
| [🙏 致谢](#acknowledge) | 来源致谢与修正政策 |

### [📏 基准与前沿评测](#benchmarks-frontier-evaluation)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Artificial Analysis Intelligence Index](#case-1) | 使用人工分析帖子将 GLM-5.2 与其他开放权重和专有前沿模型在智能和每项任务成本方面进行比较。 | 基准 |
| [Code Arena Frontend Ranking](#case-2) | 使用此案例在通过竞技场式比较判断的真实前端编码任务上评估 GLM-5.2。 | 基准 |
| [Design Arena First Place](#case-3) | 使用此案例来判断 GLM-5.2 是否可以处理设计加代码任务，而不仅仅是文本密集型编码基准。 | 基准 |
| [FrontierSWE Result](#case-4) | 使用 FrontierSWE 帖子将 GLM-5.2 与 GPT-5.5、Opus 和 Fable 风格的模型在软件工程任务上进行比较。 | 基准 |
| [DeepSWE Open-Source Lead](#case-5) | 使用 DeepSWE 案例了解 GLM-5.2 作为用于困难的软件工程评估任务的强大开放模型。 | 基准 |
| [Terminal-Bench Over 80 Percent](#case-6) | 在评估面向终端的编码和代理工作流程的 GLM-5.2 时使用此案例。 | 基准 |
| [SWELancer 与 GPT-5.5 的比较](#case-7) | 使用此 SWELancer 案例作为 GLM-5.2 和 GPT-5.5 在任务成功、奖励和完成时间方面的具体多指标比较。 | 评测 |
| [BridgeBench Perfect Score Signal](#case-8) | 使用此案例来检查基于多步骤推理的 GLM-5.2，而不仅仅是编码排行榜。 | 基准 |
| [BridgeBench Reasoning Number One](#case-9) | 使用此案例在扎根推理任务上将 GLM-5.2 与封闭边界模型进行比较。 | 基准 |
| [KernelBench-Hard Without Shortcutting](#case-10) | 在检查基准测试收益是否来自有效的实现行为而不是捷径时使用此案例。 | 评测 |
| [Runescape Bench Catch-Up](#case-11) | 使用此案例作为开放权重模型在类似游戏的基准任务上取得进展的快速信号。 | 基准 |
| [BridgeBench Speed Improvement](#case-12) | 使用此案例来评估对延迟敏感的工作流程，其中速度与智能同样重要。 | 基准 |
| [KernelBench 硬核和巨型 GPU 编码](#case-60) | 使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 评估 GPU 内核编码上的 GLM-5.2，其中开放代理跟踪使结果可检查。 | 基准 |
| [DeepSWE 高强度模式开源领先](#case-70) | 用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。 | 基准 |
| [LLM 辩论基准第二名](#case-72) | 用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。 | 基准 |
| [AA-Omniscience 幻觉率](#case-76) | 用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。 | 评测 |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | 如果你想比较 GLM-5.2 在长期知识工作中的表现，而不是只看编码榜单，可以用这个案例。 | 评测 |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | 如果你想判断 GLM-5.2 的游戏构建质量，可以用这个案例。它在 Game Dev Arena 拿到第二名，并成为该榜单里开源权重阵营的第一名。 | 评测 |

### [💻 编码代理与长上下文工作流](#coding-agents-long-context-workflows)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [One Hour Forty Two Minute Refactor Loop](#case-13) | 使用此案例作为使用 TDD、审阅者反馈和回归检查进行长时间自主前端重构的模式。 | 演示 |
| [OpenCode Bug Fix And Implementation Test](#case-14) | 使用此案例来测试 GLM-5.2 作为 OpenCode 编码代理的错误修复以及小型实施任务。 | 演示 |
| [OpenCode Retro Video Game Walkthrough](#case-15) | 使用此演练通过单个提示使用 GLM-5.2 和 OpenCode 构建一个小游戏，然后检查模型如何处理实现细节。 | 教程 |
| [HTML5 Physics Simulations Contest](#case-16) | 使用此案例在没有库的独立 HTML5 物理模拟上比较 GLM-5.2 和 Kimi K2.7 代码。 | 评测 |
| [Personal Site UI UX Build](#case-17) | 使用此案例提示 GLM-5.2 打造一个精美的个人网站，并检查多次转动可以在多大程度上改善 UI/UX。 | 演示 |
| [AI Contract Review Product Build](#case-18) | 使用此案例通过 PRD、时间预算、步骤计数、使用配额和代码质量比较来评估产品构建任务上的 GLM-5.2。 | 评测 |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | 使用此案例了解如何将 GLM-5.2 集成到 ZCode 3.0 中以执行更大的代理开发任务。 | 集成 |
| [使用 GLM-5.2 构建的 ZCode 的 Linux 包装器](#case-20) | 使用此案例作为 GLM-5.2 协助编码代理环境工具的示例。 | 演示 |
| [Computer Use Skill Packaging](#case-21) | 使用此案例来研究 GLM-5.2，将其作为将开源计算机使用存储库转变为可重用技能的助手。 | 演示 |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | 使用此案例在完整的代理开发环境而不是单个聊天会话中评估 GLM-5.2。 | 演示 |
| [具有本地服务的 OpenCode Harness](#case-62) | 使用此案例通过 OpenCode 工具、本地服务和工具密集型编码工作流程来测试 GLM-5.2，然后将其与 Claude Opus 进行比较。 | 评测 |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | 使用此案例通过将指令移至 RLM 系统提示符来改进 GLM-5.2 长上下文计数和 REPL 代理行为。 | 集成 |
| [DeepAgents Code Open Harness Trial](#case-66) | 使用此案例尝试使用开放编码代理工具的 GLM-5.2，并在可重现的代理 shell 下比较模型。 | 演示 |
| [生产级营销 Agent 栈路由策略](#case-77) | 用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。 | 评测 |
| [M3 Ultra Pokemon Red Goal Run](#case-80) | 用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。 | 演示 |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | 如果你想比较 GLM-5.2 和 Opus 4.8 在真实仓库 bug 修复中的表现，可以用这个案例。GLM 虽然消耗了更多 token，但最终补丁更便宜也更干净。 | 评测 |

### [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | 使用此案例来比较 GLM-5.2 和 Opus 4.8 之间相同提示的游戏构建输出、运行时间和成本。 | 演示 |
| [三个真实的构建结果参差不齐](#case-24) | 将此案例用作警示演示集：在信任用于生产游戏或视频任务的模型之前测试多个真实构建。 | 评测 |
| [Super Mario Clone In ZCode](#case-25) | 使用此案例来评估使用 GLM-5.2 和 ZCode 在多个修复和功能过程中进行的迭代游戏构建。 | 演示 |
| [Lunar Lander Contest](#case-26) | 使用此案例在交互式游戏类型任务上比较 GLM-5.2、MiniMax M3 和 Kimi K2.7 代码。 | 评测 |
| [One-Prompt Design Arena Creation](#case-27) | 使用此案例来检查 GLM-5.2 可以从竞技场上下文中的单个设计提示生成什么。 | 演示 |
| [研究论文理解工作流程](#case-28) | 使用此案例将 GLM-5.2 应用于包含上下文问题和跨论文参考的论文阅读工作流程。 | 集成 |
| [Constrained Poem Comparison](#case-29) | 在将 GLM-5.2 与寓言风格模型进行比较时，使用此案例将正确性与创意质量分开。 | 评测 |
| [Design Sense Example](#case-30) | 使用此案例作为轻量级视觉设计信号，然后使用您自己的提示和 UI 审查进行验证。 | 演示 |
| [Temple Run 体素游戏单次生成](#case-71) | 用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。 | 演示 |
| [OpenCode Go 单次生成案例集](#case-78) | 用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。 | 演示 |
| [Space Invaders One-Prompt Build](#case-81) | 用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。 | 演示 |
| [OpenCode Recovery Lab One-Shot](#case-82) | 用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。 | 演示 |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | 如果你想测试 GLM-5.2 在参考驱动网页复刻上的能力，可以用这个案例。只给一个源 URL 和一条提示词，就几乎像素级复现了网站。 | 演示 |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | 如果你想比较 GLM-5.2 在全栈 UI 构建上的表现，可以用这个案例。它做出的交易终端效果接近最精致的结果，但成本只有头部结果的一小部分。 | 评测 |

### [🔌 供应商与工具集成](#provider-tool-integrations)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [OpenCode Go Availability](#case-31) | 使用此案例通过文本、1M 上下文和类似 GLM-5.1 的定价来跟踪 OpenCode Go 工作流程中的 GLM-5.2 可用性。 | 集成 |
| [Ollama Cloud Availability](#case-32) | 使用此案例将 GLM-5.2 路由到 Ollama Cloud 中，以进行可访问的开源编码模型实验。 | 集成 |
| [OpenRouter One API Call Access](#case-33) | 在比较提供商路由或多模型堆栈时，使用此案例通过 OpenRouter 访问 GLM-5.2。 | 集成 |
| [vLLM Day-Zero Support](#case-34) | 使用此案例通过 vLLM 自行托管或提供 GLM-5.2 服务，并提供零日支持。 | 集成 |
| [Notion Availability Via Baseten](#case-35) | 使用此案例将 GLM-5.2 识别为 Notion 工作流程中可用的开放权重模型。 | 集成 |
| [Fireworks Day-Zero Serving](#case-36) | 使用此案例来评估 Fireworks 作为需要托管基础设施的 GLM-5.2 工作负载的服务路径。 | 集成 |
| [谷歌云模型花园链接](#case-37) | 使用此案例在面向 Google Cloud 的部署和代理平台上下文中查找 GLM-5.2。 | 集成 |
| [Venice Privacy Mode](#case-38) | 当隐私模式、TEE 或端到端加密是尝试 GLM-5.2 的决定因素时，请使用此案例。 | 集成 |
| [Command Code Availability](#case-39) | 使用此案例尝试命令代码中的 GLM-5.2，具有低成本入门计划和长上下文编码功能。 | 集成 |
| [来自 Nous Portal 的赫尔墨斯特工](#case-40) | 使用此案例通过 Nous Portal 和 OpenRouter 将 GLM-5.2 连接到 Hermes Agent 工作流程。 | 集成 |
| [io.net Day-Zero Launch Partner](#case-41) | 在评估 753B 参数长上下文模型的计算支持服务时使用此案例。 | 集成 |
| [Modular Cloud Day-Zero Serving](#case-42) | 使用此案例来考虑在提供商规模提供长上下文 GLM-5.2 服务的模块化云。 | 集成 |
| [Cursor Setup Through OpenRouter](#case-61) | 使用此案例通过 OpenRouter 在 Cursor 中配置 GLM-5.2，以实现低成本的开放模型编码工作流程。 | 教程 |
| [Amp Agentic Eyes For Visual Design](#case-63) | 当纯文本模型需要视觉审核支持来完成设计任务时，可以使用此案例将 GLM-5.2 与 Amp 自定义代理配对。 | 集成 |
| [Baseten Faster One-Million-Context Serving](#case-69) | 当长上下文服务速度对于 Factory Droid、OpenCode 和编码工具很重要时，可以使用此案例通过 Baseten 路由 GLM-5.2。 | 集成 |
| [面向网页设计的 Browser Use QA 子代理](#case-74) | 当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。 | 集成 |
| [ZCode 官方 IDE 每日免费额度](#case-79) | 当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。 | 教程 |
| [Cursor Setup Through Fireworks](#case-83) | 用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。 | 教程 |
| [VulcanBench ZAI Provider Support](#case-84) | 用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。 | 集成 |
| [OpenCode High/Max Reasoning Variants](#case-85) | 用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。 | 集成 |
| [Z.ai Coding Endpoint Selection](#case-86) | 用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。 | 教程 |
| [ZenMux Free GLM-5.2 API Setup](#case-87) | 用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。 | 教程 |
| [Case 93: Noumena ncode GLM Default](#case-93) | 如果你想把 GLM-5.2 接入 ncode 和 Noumena 风格的 agent 环境，并同时使用标准版与 1M 上下文端点以及默认模型支持，可以用这个案例。 | 集成 |
| [Case 95: Claude Code Through Baseten](#case-95) | 如果你想通过 Baseten key、自定义 base URL 和 `~/.claude/settings.json` 里的模型映射，在 Claude Code 里运行 GLM-5.2，可以用这个案例。 | 教程 |
| [Case 96: Deepsec Pi Agent Default](#case-96) | 如果你想在安全 harness 中测试 GLM-5.2，可以用这个案例。`deepsec` 把它设成了 Pi agent 默认模型，并报告了有竞争力的 eval 结果。 | 集成 |

### [💸 成本、定价与本地部署](#cost-pricing-local-deployment)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Output Token Cost Comparison](#case-43) | 使用此案例将 GLM-5.2 输出代币经济学与 Opus、Fable 和 GPT-5.5 风格的模型进行比较。 | 评测 |
| [Local Near-Frontier Hardware ROI](#case-44) | 使用此案例来推理自托管类似 GLM-5.2 的模型是否可以为重度代理用户偿还硬件成本。 | 评测 |
| [MLX On Two Mac Studios](#case-45) | 使用此案例探索在 Apple 硬件和面向 MLX 的设置上运行的本地 GLM-5.2。 | 演示 |
| [H100 Monthly Local Deployment Claim](#case-46) | 使用此案例作为成本比较提示，用于在订阅和自托管之间进行选择之前检查本地部署假设。 | 评测 |
| [Daily Credits And Claude Replacement Claim](#case-47) | 使用此案例来检查围绕 GLM-5.2 的免费信用和替代代理叙述，同时将营销声明与经过验证的工作负载适合度分开。 | 评测 |
| [Free ZCode Token Window](#case-48) | 在承诺付费提供商或本地部署之前，使用此案例通过免费 ZCode 津贴测试 GLM-5.2。 | 集成 |
| [ZenMux Free Week Offer](#case-49) | 使用此案例来查找用于 GLM-5.2 测试的时间限制的自由访问窗口。 | 集成 |
| [crofAI 每代币定价](#case-50) | 在选择路线之前，使用此案例比较 GLM-5.2 的第三方提供商定价。 | 集成 |
| [API Price Margin Comparison](#case-51) | 将 GLM-5.2 与其他前沿实验室和开放模型进行比较时，请使用此案例作为市场定价批评。 | 评测 |
| [Basement Local Inference Speed](#case-64) | 在规划离线编码设置之前，使用此案例来估计大内存 Apple 硬件上的本地 GLM-5.2 推理吞吐量。 | 演示 |
| [Unsloth Quantized Local Deployment](#case-68) | 当完整模型权重对于普通本地硬件来说太大时，使用此案例来评估量化的 GLM-5.2 部署路径。 | 教程 |
| [Two M3 Ultra MLX Distributed Run](#case-88) | 用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。 | 演示 |
| [ZCode Multiplier Cut Through September](#case-89) | 用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。 | 集成 |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | 如果你想评估高端本地 GLM-5.2 工作站的规模，可以用这个案例。双 Blackwell 桌面机在 4-bit 量化版本上保持了两位数的 decode 速度。 | 演示 |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | 如果你想判断为了本地 GLM-5.2 推理购买 Mac Studio 是否划算，可以用这个案例。帖子里的回本测算明显更倾向于 API 或套餐访问。 | 评测 |

### [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [No Vision Caveat](#case-52) | 使用此案例请记住，GLM-5.2 对于需要本机视觉功能的工作流程可能不太有用。 | 限制 |
| [现实世界的代理差距警告](#case-53) | 使用此案例可以避免过度阅读基准测试胜利，以证明 GLM-5.2 与所有已部署的代理任务上的最佳专有模型相匹配。 | 限制 |
| [Safety Guardrail Concern](#case-54) | 使用此案例提醒您在敏感域中部署 GLM-5.2 之前运行安全评估。 | 限制 |
| [基准方法论批评](#case-55) | 即使总体结果有利于 GLM-5.2，也可以使用此案例来质疑基准方法。 | 限制 |
| [Peak-Time Latency Concern](#case-56) | 在切换编码计划或将 Claude 代码式工作流程路由到 GLM-5.2 之前，使用此案例测试提供程序延迟。 | 限制 |
| [FutureSim Non-Improvement Result](#case-57) | 在广泛部署之前，使用此案例检查编码增益是否推广到非编码领域。 | 限制 |
| [Launch Readiness Critique](#case-58) | 使用此案例将模型功能与启动执行、文档和 API 准备情况分开。 | 限制 |
| [编码计划价格上涨](#case-59) | 在推荐 GLM-5.2 作为低成本替代品之前，请使用此案例验证计划定价。 | 限制 |
| [短时间并行工作与长代理运行](#case-67) | 使用此案例将 GLM-5.2 路由到短边界编码任务，同时为更深的多小时代理运行保留更强的模型。 | 限制 |
| [代码审查与偏见检查](#case-73) | 用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。 | 限制 |
| [高难推理计费异常](#case-75) | 用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。 | 限制 |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 基准与前沿评测

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**使用人工分析帖子将 GLM-5.2 与其他开放权重和专有前沿模型在智能和每项任务成本方面进行比较。**

Artificial Analysis 将 GLM-5.2 报告为其智能指数中领先的开放权重模型，得分为 51，在智能与每项任务成本方面处于帕累托前沿位置。该帖子还记录了模型大小、上下文窗口、定价和提供商可用性。

类型: 基准 | 日期: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (作者 [@arena](https://x.com/arena))

**使用此案例在通过竞技场式比较判断的真实前端编码任务上评估 GLM-5.2。**

Arena 账户报告称，GLM-5.2 Max 在 Code Arena 前端排名第二，领先于其他开放型号，接近顶级前沿入口。这篇文章对于前端、React、HTML、游戏、模拟和基于参考的设计用例特别有用。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (作者 [@Designarena](https://x.com/Designarena))

**使用此案例来判断 GLM-5.2 是否可以处理设计加代码任务，而不仅仅是文本密集型编码基准。**

Design Arena 报告称，GLM-5.2 以 1360 的 Elo 分数排名第一，凸显了开放权重模型设计代码性能的飞跃。将其视为设计基准信号，而不是替代特定于项目的 UI 审查。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (作者 [@ProximalHQ](https://x.com/ProximalHQ))

**使用 FrontierSWE 帖子将 GLM-5.2 与 GPT-5.5、Opus 和 Fable 风格的模型在软件工程任务上进行比较。**

该帖子报告称 GLM-5.2 在 FrontierSWE 上排名第三，并将其定义为首批开放权重模型之一，以缩小与实施繁重的工程工作中顶级专有模型的差距。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (作者 [@AiBattle_](https://x.com/AiBattle_))

**使用 DeepSWE 案例了解 GLM-5.2 作为用于困难的软件工程评估任务的强大开放模型。**

AiBattle 报告 GLM-5.2 的 DeepSWE 得分为 46.2%，并将其描述为该基准测试环境中开源模型的最高得分。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (作者 [@cline](https://x.com/cline))

**在评估面向终端的编码和代理工作流程的 GLM-5.2 时使用此案例。**

Cline 强调 GLM-5.2 是第一个在 Terminal-Bench 上突破 80% 的开放权重模型，并将其定位为可访问的基于工具的开发的前沿选项。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer 与 GPT-5.5 的比较](https://x.com/gosrum/status/2067153091842203676) (作者 [@gosrum](https://x.com/gosrum))

**使用此 SWELancer 案例作为 GLM-5.2 和 GPT-5.5 在任务成功、奖励和完成时间方面的具体多指标比较。**

作者分享了日本基准更新，其中 GLM-5.2 在最新的 SWELancer 结果上意外领先 GPT-5.5，包括任务成功率、获得的奖励和完成时间，其中排除了两项无法完成的任务。

类型: 评测 | 日期: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (作者 [@bridgemindai](https://x.com/bridgemindai))

**使用此案例来检查基于多步骤推理的 GLM-5.2，而不仅仅是编码排行榜。**

BridgeMind 报告称，GLM-5.2 是第一个在 BridgeBench BS 基准测试中获得满分的模型，这使其成为推理密集型评估声明的有用来源。

类型: 基准 | 日期: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (作者 [@bridgebench](https://x.com/bridgebench))

**使用此案例在扎根推理任务上将 GLM-5.2 与封闭边界模型进行比较。**

BridgeBench 报告称，GLM-5.2 在推理基准测试中排名第一，并在该测量环境中击败了 Claude Fable 5。

类型: 基准 | 日期: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (作者 [@elliotarledge](https://x.com/elliotarledge))

**在检查基准测试收益是否来自有效的实现行为而不是捷径时使用此案例。**

KernelBench-Hard 帖子表示，有趣的结果不仅仅是分数，而且 GLM-5.2 停止在 fp8 GEMM 问题上使用不适当的快捷方式，使其与基准完整性相关。

类型: 评测 | 日期: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (作者 [@maxbittker](https://x.com/maxbittker))

**使用此案例作为开放权重模型在类似游戏的基准任务上取得进展的快速信号。**

该帖子报告称，GLM-5.2 在 Runescape 平台上的得分优于最新的专有模型，并使用该结果来衡量开源前沿功能的追赶速度。

类型: 基准 | 日期: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (作者 [@bridgebench](https://x.com/bridgebench))

**使用此案例来评估对延迟敏感的工作流程，其中速度与智能同样重要。**

BridgeBench 报告称，GLM-5.2 比 GLM-5.1 快三倍，在其速度基准上排名第四，这使其与迭代速度影响可用性的工作流程相关。

类型: 基准 | 日期: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench 硬核和巨型 GPU 编码](https://x.com/elliotarledge/status/2068177175640240323) (作者 [@elliotarledge](https://x.com/elliotarledge))

**使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 评估 GPU 内核编码上的 GLM-5.2，其中开放代理跟踪使结果可检查。**

KernelBench 更新报告了 H100、B200 和 RTX PRO 6000 测试、开源代理跟踪以及 GLM-5.2 作为比较中排名最高的开放模型。

类型: 基准 | 日期: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE 高强度模式开源领先](https://x.com/datacurve/status/2068473057107476680) (作者 [@datacurve](https://x.com/datacurve))

**用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。**

DataCurve 分享的 DeepSWE 榜单更新显示，GLM-5.2 在开源模型中达到 44% pass@1，并领先 Kimi K2.7 Code 17 个点。应将其视为一次 benchmark 更新，而不是所有真实世界 agent 工作流都已被解决的证明。

类型: 基准 | 日期: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM 辩论基准第二名](https://x.com/LechMazur/status/2068428300460974279) (作者 [@LechMazur](https://x.com/LechMazur))

**用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。**

Lech Mazur 分享了一项 LLM Debate Benchmark 结果，其中 GLM-5.2 Max 排名第二。这个基准衡量的是跨广泛主题的对抗式多轮辩论能力，因此它提供的是编码榜单之外的推理信号。

类型: 基准 | 日期: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience 幻觉率](https://x.com/yuhasbeentaken/status/2068259921519423855) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。**

帖子报告 GLM-5.2 在 AA-Omniscience 上的幻觉率为 28%，低于 Fable 5 和 DeepSeek V4 Pro 的对应结果。这个基准关注的是模型在不确定时是否会拒答或承认不确定，而不是继续猜测。

类型: 评测 | 日期: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想比较 GLM-5.2 在长期知识工作中的表现，而不是只看编码榜单，可以用这个案例。**

Artificial Analysis 报告称，GLM-5.2 在 GDPval-AA 上拿到 1524 Elo，综合排名第 3，落后于 Claude Fable 5 和 Opus 4.8，略高于 1509 的 GPT-5.5 xhigh。它也是断层领先的开源权重模型第一名。帖子还提到，这个 benchmark 在 1,999 场对局中平均每个任务大约进行了 31 轮交互。

类型: 评测 | 日期: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (作者 [@Designarena](https://x.com/Designarena))

**如果你想判断 GLM-5.2 的游戏构建质量，可以用这个案例。它在 Game Dev Arena 拿到第二名，并成为该榜单里开源权重阵营的第一名。**

Design Arena 报告称，GLM-5.2 在 Game Dev Arena 上拿到 1368 Elo，比 GLM-5.1 提高 29 分，排名提升 6 位。帖子表示，它已经进入与 Claude Fable 5 相同的性能区间，并且综合排名第二；如果按实验室维度看，它超过了 OpenAI，仅次于 Anthropic。

类型: 评测 | 日期: 2026-06-22

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 编码代理与长上下文工作流

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (作者 [@KELMAND1](https://x.com/KELMAND1))

**使用此案例作为使用 TDD、审阅者反馈和回归检查进行长时间自主前端重构的模式。**

该帖子描述了一项耗时 1 小时 42 分钟的 GLM-5.2 重构任务，其中包含 88 次模型转换和 102 次工具调用。工作流程包括交接、四个阻止程序修复、12 项测试的 TDD 实施、两轮 P2 修复和最终回归。

类型: 演示 | 日期: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (作者 [@altudev](https://x.com/altudev))

**使用此案例来测试 GLM-5.2 作为 OpenCode 编码代理的错误修复以及小型实施任务。**

作者报告称，测试 GLM-5.2 时修复了 6 个错误，并在 OpenCode 中实现了一项，并称这些更改通过可靠的规划和比 GLM-5.1 更快的速度顺利完成。

类型: 演示 | 日期: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (作者 [@AskVenice](https://x.com/AskVenice))

**使用此演练通过单个提示使用 GLM-5.2 和 OpenCode 构建一个小游戏，然后检查模型如何处理实现细节。**

Venice 分享了使用 GLM-5.2 和 OpenCode 构建复古视频游戏的完整演练，将其定位为私有、开源、长期编码工作流程。

类型: 教程 | 日期: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**使用此案例在没有库的独立 HTML5 物理模拟上比较 GLM-5.2 和 Kimi K2.7 代码。**

Atomic Chat 报告要求两个模型构建泳池休息、弹簧块和高尔顿板模拟。他们的帖子称，GLM-5.2 以更详细和完善的方式处理了这三个问题，而 Kimi 则在身体行为方面遇到了困难。

类型: 评测 | 日期: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (作者 [@anshuc](https://x.com/anshuc))

**使用此案例提示 GLM-5.2 打造一个精美的个人网站，并检查多次转动可以在多大程度上改善 UI/UX。**

作者表示，GLM-5.2 在正确的提示下生成了一个富有创意的个人网站，并分享了结果的视频。它对于前端设计迭代而不是单次基准测试很有用。

类型: 演示 | 日期: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (作者 [@laozhang2579](https://x.com/laozhang2579))

**使用此案例通过 PRD、时间预算、步骤计数、使用配额和代码质量比较来评估产品构建任务上的 GLM-5.2。**

这篇中文文章在人工智能合同审查产品 PRD 上比较了 GLM-5.2、Kimi K2.7 和 Claude Opus 4.8。它报告构建持续时间、步骤计数、五小时配额使用情况和代码质量评分。

类型: 评测 | 日期: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (作者 [@zcode_ai](https://x.com/zcode_ai))

**使用此案例了解如何将 GLM-5.2 集成到 ZCode 3.0 中以执行更大的代理开发任务。**

ZCode 宣布为编码计划用户提供 GLM-5.2、更强大的代理任务执行、更好的长上下文编码以及用于管理从计划到完成的更大目标的目标功能。

类型: 集成 | 日期: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [使用 GLM-5.2 构建的 ZCode 的 Linux 包装器](https://x.com/gosrum/status/2066484949755269510) (作者 [@gosrum](https://x.com/gosrum))

**使用此案例作为 GLM-5.2 协助编码代理环境工具的示例。**

作者报告使用 GLM-5.2 和 Claude Code 完成 zcode-linux，以便 Linux 用户可以在 Linux 环境中运行 ZCode 并添加任意 API 端点，包括本地 LLM 端点。

类型: 演示 | 日期: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (作者 [@0xSero](https://x.com/0xSero))

**使用此案例来研究 GLM-5.2，将其作为将开源计算机使用存储库转变为可重用技能的助手。**

该帖子称 GLM-5.2 正在设置计算机使用，找到了一个高级开源存储库，并将其转换为一项技能。它是工具包装和代理集成工作的实际操作信号。

类型: 演示 | 日期: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (作者 [@laogui](https://x.com/laogui))

**使用此案例在完整的代理开发环境而不是单个聊天会话中评估 GLM-5.2。**

国内评测称，ZCode 3.0由类似shell的早期版本重写为自主开发的代理核心，搭配GLM-5.2，在国内代理开发环境中具有更好的体验。

类型: 演示 | 日期: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [具有本地服务的 OpenCode Harness](https://x.com/PatrickToulme/status/2068134212587184442) (作者 [@PatrickToulme](https://x.com/PatrickToulme))

**使用此案例通过 OpenCode 工具、本地服务和工具密集型编码工作流程来测试 GLM-5.2，然后将其与 Claude Opus 进行比较。**

作者报告了本地部署、嵌套子代理、研究/规划行为和工作应用程序构建。

类型: 评测 | 日期: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (作者 [@neural_avb](https://x.com/neural_avb))

**使用此案例通过将指令移至 RLM 系统提示符来改进 GLM-5.2 长上下文计数和 REPL 代理行为。**

发行说明描述了具体的代理脚手架更改和 GLM-5.2 长上下文基准测试效果。

类型: 集成 | 日期: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (作者 [@sydneyrunkle](https://x.com/sydneyrunkle))

**使用此案例尝试使用开放编码代理工具的 GLM-5.2，并在可重现的代理 shell 下比较模型。**

作者报告使用 GLM-5.2 和 DeepAgents 代码，并框架开放模型和开放线束作为测试模式。

类型: 演示 | 日期: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [生产级营销 Agent 栈路由策略](https://x.com/DeRonin_/status/2068303752671477820) (作者 [@DeRonin_](https://x.com/DeRonin_))

**用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。**

作者在一个代理机构栈里做了 6 天并行对比后表示，GLM-5.2 在开始漂移前可稳定执行 60 多个 agent 步骤，连续 800 多次匹配结构化格式，并提供低延迟的自托管响应。同一条帖子仍然更偏好用 Opus 处理语音关键或高歧义任务，因此真正有价值的是这条路由规则本身。

类型: 评测 | 日期: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (作者 [@hxiao](https://x.com/hxiao))

**用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。**

作者把 Claude Code 的模型切到本地 GLM 5.2，在一台 M3 Ultra 512GB 机器上跑了 12 小时的 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 任务。帖文公开了运行时长、token 消耗、代码 churn、RAM 使用量以及 GGUF 和 KV-cache 配置，并指出模型质量感觉接近 frontier，但本地推理速度仍是主要瓶颈。

类型: 演示 | 日期: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (作者 [@cline](https://x.com/cline))

**如果你想比较 GLM-5.2 和 Opus 4.8 在真实仓库 bug 修复中的表现，可以用这个案例。GLM 虽然消耗了更多 token，但最终补丁更便宜也更干净。**

Cline 在相同 harness 和相同工具条件下，用 Cline 仓库里的同一个 bug 测试了两个模型。帖子称，GLM 使用了约 110 万 token，而 Opus 使用了 66 万；成本分别是 0.41 美元和 0.81 美元；耗时分别是 4.7 分钟和 28 次工具调用，对比 1.6 分钟和 12 次工具调用。最终 GLM 还清理了死代码并成功完成 production build，而 Opus 留下了虽然能通过测试但仍存在的类型错误。

类型: 评测 | 日期: 2026-06-22

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手演示与作品展示

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (作者 [@aimlapi](https://x.com/aimlapi))

**使用此案例来比较 GLM-5.2 和 Opus 4.8 之间相同提示的游戏构建输出、运行时间和成本。**

AI/ML API 报告要求 GLM-5.2 和 Opus 4.8 一次性制作一款可玩的 Backrooms 游戏。他们的帖子称，GLM-5.2 在 1 分 08 秒内以 0.37 美元的价格构建了更完整的机制，而 Opus 用了 2 分 14 秒以 1.94 美元的价格构建了更完整的机制。

类型: 演示 | 日期: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [三个真实的构建结果参差不齐](https://x.com/bridgemindai/status/2065840871929442319) (作者 [@bridgemindai](https://x.com/bridgemindai))

**将此案例用作警示演示集：在信任用于生产游戏或视频任务的模型之前测试多个真实构建。**

BridgeMind 在恐怖屋游戏、3D 潜行游戏和 Remotion 营销视频上测试了 GLM-5.2。这篇文章报告了好坏参半的结果，包括破坏的游戏逻辑，使其成为有用的接地限制信号。

类型: 评测 | 日期: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例来评估使用 GLM-5.2 和 ZCode 在多个修复和功能过程中进行的迭代游戏构建。**

作者通过创建超级马里奥风格的克隆来使用 GLM-5.2 测试 ZCode 3.0，然后在问题修复和功能添加五次迭代后分享结果。

类型: 演示 | 日期: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例在交互式游戏类型任务上比较 GLM-5.2、MiniMax M3 和 Kimi K2.7 代码。**

这篇文章描述了 MiniMax M3、GLM-5.2 和 Kimi K2.7 Code 之间的月球着陆器竞赛，在返回本地模型开发之前使用视频结果作为实际基准。

类型: 评测 | 日期: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (作者 [@grx_xce](https://x.com/grx_xce))

**使用此案例来检查 GLM-5.2 可以从竞技场上下文中的单个设计提示生成什么。**

作者在 Design Arena 上分享了一个根据一个提示创建的 GLM-5.2 示例，用它来展示开放权重模型和封闭权重模型之间缩小的差距。

类型: 演示 | 日期: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [研究论文理解工作流程](https://x.com/askalphaxiv/status/2066996976445706745) (作者 [@askalphaxiv](https://x.com/askalphaxiv))

**使用此案例将 GLM-5.2 应用于包含上下文问题和跨论文参考的论文阅读工作流程。**

AlphaXiv 引入了 GLM-5.2 来理解研究论文，用户可以突出显示一个部分、提出问题并参考其他论文以了解上下文、比较和基准参考。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (作者 [@emollick](https://x.com/emollick))

**在将 GLM-5.2 与寓言风格模型进行比较时，使用此案例将正确性与创意质量分开。**

伊森·莫里克 (Ethan Mollick) 称赞 GLM-5.2 Max 创作了一首正确的受限诗，同时指出《寓言》更有创意地将消失字母约束融入到诗歌主题中。

类型: 评测 | 日期: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (作者 [@0xSero](https://x.com/0xSero))

**使用此案例作为轻量级视觉设计信号，然后使用您自己的提示和 UI 审查进行验证。**

作者表示他们很喜欢 GLM-5.2 的设计感，并分享了一个视觉示例。它可用作检查指针，而不是作为生产设计质量的独立证明。

类型: 演示 | 日期: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 体素游戏单次生成](https://x.com/pseudokid/status/2068431546143649829) (作者 [@pseudokid](https://x.com/pseudokid))

**用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。**

作者表示，首轮提示就生成出了大部分 Temple Run 风格的体素摩托游戏，之后只用少量补充轮次修正镜头和移动逻辑。帖子还提到 Z.ai 工具链可以生成截图和实机视频，帮助文本模型评估结果。

类型: 演示 | 日期: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 单次生成案例集](https://x.com/LyalinDotCom/status/2068378281636982990) (作者 [@LyalinDotCom](https://x.com/LyalinDotCom))

**用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。**

作者展示了一组通过 OpenCode Go 完成的单次生成案例，包括太阳系 Web 应用、系统信息 Electron 应用，以及一个简单的探索小岛 Web 游戏。同一条帖子也表示，GLM-5.2 是他用过最强的开源模型，但还没有把它称作与最前沿闭源模型完全同级。

类型: 演示 | 日期: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (作者 [@DeryaTR_](https://x.com/DeryaTR_))

**用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。**

作者表示，GLM-5.2 用一个主提示词就生成了可玩的 Space Invaders 风格游戏，随后又用三轮后续提示完成 sprite 替换和 leaderboard 等小增强。这个公开结果更适合作为轻量游戏生成样例，而不是完整 benchmark。

类型: 演示 | 日期: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (作者 [@threepointone](https://x.com/threepointone))

**用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。**

作者在输入一份 4,000 字分析和 Agents SDK 仓库后，用 OpenCode 搭配 GLM-5.2 构建了一个完全可交互的 recovery lab。帖文给出了 176k token 的运行、一轮成型的结果，以及打磨前端到端约 3.50 美元的成本。

类型: 演示 | 日期: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (作者 [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**如果你想测试 GLM-5.2 在参考驱动网页复刻上的能力，可以用这个案例。只给一个源 URL 和一条提示词，就几乎像素级复现了网站。**

Open Design 表示，它在内置 AMR 中只使用一个参考 URL 和一条简单提示词测试了 GLM-5.2，演示里模型几乎完美重建了原网站。这个案例更适合作为参考式 UI 生成的上手证明，而不是完整 benchmark。

类型: 演示 | 日期: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**如果你想比较 GLM-5.2 在全栈 UI 构建上的表现，可以用这个案例。它做出的交易终端效果接近最精致的结果，但成本只有头部结果的一小部分。**

Atomic Chat 用同一条实时 Trader Desk 构建提示，比较了四个模型，任务包含前端、后端、8 个交易标的的市场数据，以及自定义深色主题 UI。帖子称，GLM-5.2 消耗 13,677 token，成本 0.03 美元；Fugu Ultra 则是 22,225 token，成本 0.51 美元。帖子认为，GLM 以远低得多的成本做出了一个同样相当完整、带实时数据的多面板界面。

类型: 评测 | 日期: 2026-06-22

---

<a id="provider-tool-integrations"></a>
## 🔌 供应商与工具集成

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (作者 [@opencode](https://x.com/opencode))

**使用此案例通过文本、1M 上下文和类似 GLM-5.1 的定价来跟踪 OpenCode Go 工作流程中的 GLM-5.2 可用性。**

OpenCode 宣布 GLM-5.2 在 Go 中可用，强调文本支持、1M 上下文窗口以及与 5.1 相同的定价。

类型: 集成 | 日期: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (作者 [@ollama](https://x.com/ollama))

**使用此案例将 GLM-5.2 路由到 Ollama Cloud 中，以进行可访问的开源编码模型实验。**

Ollama 宣布推出 GLM-5.2，将其描述为具有 1M 上下文的长视野编码和代理任务模型。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (作者 [@OpenRouter](https://x.com/OpenRouter))

**在比较提供商路由或多模型堆栈时，使用此案例通过 OpenRouter 访问 GLM-5.2。**

OpenRouter 宣布 GLM-5.2 作为 1M 代币长期模型可用，为用户提供了一个与提供商无关的调用路径。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (作者 [@vllm_project](https://x.com/vllm_project))

**使用此案例通过 vLLM 自行托管或提供 GLM-5.2 服务，并提供零日支持。**

vLLM 项目宣布在 v0.23.0 中支持 GLM-5.2，将其定位为具有 1M 上下文的长视野编码代理的旗舰模型。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (作者 [@NotionHQ](https://x.com/NotionHQ))

**使用此案例将 GLM-5.2 识别为 Notion 工作流程中可用的开放权重模型。**

Notion 宣布 GLM-5.2 作为开放权重模型推出，专为长期任务而构建，并通过 Baseten 提供服务。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**使用此案例来评估 Fireworks 作为需要托管基础设施的 GLM-5.2 工作负载的服务路径。**

Fireworks 在第 0 天宣布推出 GLM-5.2，强调 1M 上下文、编码优先定位以及在 SWE-Bench、Terminal-Bench、GPQA 和 AIME 上的独立验证。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [谷歌云模型花园链接](https://x.com/CarolGLMs/status/2067127223216419088) (作者 [@CarolGLMs](https://x.com/CarolGLMs))

**使用此案例在面向 Google Cloud 的部署和代理平台上下文中查找 GLM-5.2。**

CarolGLMs 分享了 GLM-5.2 的 Google Cloud 链接，使其成为团队处理云模型目录的直接指针。

类型: 集成 | 日期: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (作者 [@AskVenice](https://x.com/AskVenice))

**当隐私模式、TEE 或端到端加密是尝试 GLM-5.2 的决定因素时，请使用此案例。**

Venice 宣布 GLM-5.2 在带有 TEE/E2EE 框架的隐私模式下可用，旨在实现私有代理编码和长期任务。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**使用此案例尝试命令代码中的 GLM-5.2，具有低成本入门计划和长上下文编码功能。**

Command Code 宣布 GLM-5.2 可用，并指出 1M 上下文、强大的推理、开源状态以及通过其一美元 Go 计划进行访问。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [来自 Nous Portal 的赫尔墨斯特工](https://x.com/Teknium/status/2066954081575592282) (作者 [@Teknium](https://x.com/Teknium))

**使用此案例通过 Nous Portal 和 OpenRouter 将 GLM-5.2 连接到 Hermes Agent 工作流程。**

Teknium 报告了来自 Nous Portal 和 OpenRouter 的 Hermes Agent 中 GLM-5.2 的可用性，这对于代理框架路由实验非常有用。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (作者 [@ionet](https://x.com/ionet))

**在评估 753B 参数长上下文模型的计算支持服务时使用此案例。**

io.net 宣布自己是 GLM-5.2 的零日发布合作伙伴，强调 1M 上下文、代理优先设计、长视野编码以及 753B 参数模型的计算需求。

类型: 集成 | 日期: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (作者 [@clattner_llvm](https://x.com/clattner_llvm))

**使用此案例来考虑在提供商规模提供长上下文 GLM-5.2 服务的模块化云。**

Chris Lattner 发布称，GLM-5.2 在第 0 天就在 Modular Cloud 上上线，强调了开放权重、编码、长视野代理和 1M 上下文。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (作者 [@agentnative_](https://x.com/agentnative_))

**使用此案例通过 OpenRouter 在 Cursor 中配置 GLM-5.2，以实现低成本的开放模型编码工作流程。**

源代码给出了具体的 Cursor/OpenRouter 设置路径，而不仅仅是宣布模型可用性。

类型: 教程 | 日期: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (作者 [@beyang](https://x.com/beyang))

**当纯文本模型需要视觉审核支持来完成设计任务时，可以使用此案例将 GLM-5.2 与 Amp 自定义代理配对。**

该帖子将 GLM-5.2 视觉设计基准测试结果与可提供审查层的 Amp 插件代理连接起来。

类型: 集成 | 日期: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (作者 [@alphatozeta8148](https://x.com/alphatozeta8148))

**当长上下文服务速度对于 Factory Droid、OpenCode 和编码工具很重要时，可以使用此案例通过 Baseten 路由 GLM-5.2。**

源报告 GLM-5.2 在完整的 1M 上下文中运行速度提高了四倍，并在编码工具中显示了它。

类型: 集成 | 日期: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [面向网页设计的 Browser Use QA 子代理](https://x.com/browser_use/status/2068405699340853541) (作者 [@browser_use](https://x.com/browser_use))

**当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。**

Browser Use 表示，GLM-5.2 在一个网站设计任务中超过了 Fable 5，随后又加入 QA 子代理来检查结果、判断美感、查找 bug，并把定向修复建议回传给 GLM。整套 build 加 QA 的循环据称成本低于 0.75 美元。

类型: 集成 | 日期: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 官方 IDE 每日免费额度](https://x.com/Alan_Earn/status/2068223665268006924) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。**

帖子将 ZCode 描述为智谱官方编码 IDE，默认模型就是 GLM-5.2，并提供每日 300 万 token、100 万上下文窗口，以及 Mac 和 Windows 客户端。它还包含一段简短的上手流程，因此比普通的上线公告更具可操作性。

类型: 教程 | 日期: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (作者 [@skirano](https://x.com/skirano))

**用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。**

Skirano 展示了最简 Cursor 配置流程：把 Fireworks key 填到 OpenAI API key 字段，base URL 用 `https://api.fireworks.ai/inference/v1`，模型选择 `accounts/fireworks/models/glm-5p2`，然后重启 Cursor。对于想在熟悉的 coding IDE 里试用 GLM-5.2 的人，这是一条很具体的接入路径。

类型: 教程 | 日期: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (作者 [@vulcanbench](https://x.com/vulcanbench))

**用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。**

VulcanBench v0.2.0 新增了一等公民级别的 ZAI 支持，让用户可以把 GLM-5.2 作为 `zai:glm-5.2` 与 OpenAI、Anthropic 模型并排运行，并配有独立的 `ZAI_API_KEY`。如果你要的是开放、可重复的 benchmark harness，而不是单张截图，这个案例更有用。

类型: 集成 | 日期: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (作者 [@OpenCodeLog](https://x.com/OpenCodeLog))

**用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。**

OpenCode v1.17.9 为 GLM-5.2 新增了 High 和 Max thinking 变体，覆盖 OpenAI 兼容与 Anthropic 兼容 provider，并原生支持 OpenRouter 的 effort 映射。同一版本也修复了 agent step-limit 行为，让这个集成更适合更长的运行。

类型: 集成 | 日期: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。**

帖文建议，对于 coding plan 工作负载，应优先使用 `https://api.z.ai/api/coding/paas/v4`，而不是通用的 `https://api.z.ai/api/paas/v4/`。作者还补充说，Claude Code、OpenCode 等工具在支持时通常会走 `https://api.z.ai/api/anthropic`。如果你感觉 GLM-5.2 路由不对，这是一条很具体的配置修正。

类型: 教程 | 日期: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (作者 [@0x_kaize](https://x.com/0x_kaize))

**用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。**

作者分享了一条大约五分钟的配置流程：获取免费的 ZenMux API key 与 base URL，然后把 GLM-5.2 接到 Claude、Cursor、Hermes 等工具上。帖文也提醒免费 tier 很快会触发 rate limit，所以它更适合作为 access note，而不是长期稳定性保证。

类型: 教程 | 日期: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (作者 [@_xjdr](https://x.com/_xjdr))

**如果你想把 GLM-5.2 接入 ncode 和 Noumena 风格的 agent 环境，并同时使用标准版与 1M 上下文端点以及默认模型支持，可以用这个案例。**

Noumena 的更新提到，团队已经在 tool calling、函数解析、应用路由和 reasoning trace 等链路上为 GLM 提供了一等支持。随后他们又把 API 拆分成 `glm-5.2` 和 `glm-5.2[1m]` 两个端点，用来在 1M 上下文高流量场景下控制 TTFT。更新还说，新的 ncode 版本在收到积极使用反馈后，已经把默认的 opus 级模型从 Kimi 切换成 GLM。

类型: 集成 | 日期: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (作者 [@thealexker](https://x.com/thealexker))

**如果你想通过 Baseten key、自定义 base URL 和 `~/.claude/settings.json` 里的模型映射，在 Claude Code 里运行 GLM-5.2，可以用这个案例。**

这篇教程演示了如何安装 Claude Code、创建 Baseten 账户、获取 API key，并编辑 `~/.claude/settings.json`，让三个 Claude 模型档位都通过自定义 Anthropic 环境变量指向 `zai-org/GLM-5.2`。这是一个把 GLM-5.2 作为 Claude Code 客户端替代模型接入的具体配置模式。

类型: 教程 | 日期: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (作者 [@cramforce](https://x.com/cramforce))

**如果你想在安全 harness 中测试 GLM-5.2，可以用这个案例。`deepsec` 把它设成了 Pi agent 默认模型，并报告了有竞争力的 eval 结果。**

帖子宣布，`deepsec` 已支持 `@badlogicgames` 的 Pi agent，并把 GLM-5.2 设为默认模型，同时给出了可直接运行的命令 `pnpm deepsec process --agent pi`。作者还说自己跑了 Deepsec evals，结果与其他 frontier 模型相比也有竞争力，因此这是一个很具体的安全场景集成入口。

类型: 集成 | 日期: 2026-06-22

---

<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定价与本地部署

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (作者 [@Hesamation](https://x.com/Hesamation))

**使用此案例将 GLM-5.2 输出代币经济学与 Opus、Fable 和 GPT-5.5 风格的模型进行比较。**

该帖子比较了 100 万个输出代币的价格，并认为 GLM-5.2 比前沿封闭模型便宜得多。将这些数字视为与来源相关的定价比较，应在预算之前重新检查。

类型: 评测 | 日期: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (作者 [@Jeyffre](https://x.com/Jeyffre))

**使用此案例来推理自托管类似 GLM-5.2 的模型是否可以为重度代理用户偿还硬件成本。**

作者估计多台 DGX Spark 级机器可以运行 700B 级模型，并将大约 2 万美元的硬件采购与每月用于编码和代理工作负载的高额 API 支出进行了比较。

类型: 评测 | 日期: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (作者 [@pcuenq](https://x.com/pcuenq))

**使用此案例探索在 Apple 硬件和面向 MLX 的设置上运行的本地 GLM-5.2。**

该帖子称 GLM-5.2 刚刚发布，并且已经在两台 Mac Studio M3 Ultra 机器上与 MLX 一起运行，将其与最近具有开放权重的封闭模型相媲美。

类型: 演示 | 日期: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (作者 [@ai_xiaomu](https://x.com/ai_xiaomu))

**使用此案例作为成本比较提示，用于在订阅和自托管之间进行选择之前检查本地部署假设。**

这篇中文帖子将声称的 SWE-Bench 数据、商业开源使用以及估计的单个 H100 本地部署成本与 Claude Pro 订阅进行了比较。应针对当前基础设施定价重新验证这些数字。

类型: 评测 | 日期: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**使用此案例来检查围绕 GLM-5.2 的免费信用和替代代理叙述，同时将营销声明与经过验证的工作负载适合度分开。**

该帖子将 GLM-5.2 描述为 Claude 的低成本竞争对手，具有每日积分、开源控制、自托管以及长时间编码会话的更大价值。

类型: 评测 | 日期: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (作者 [@0xSero](https://x.com/0xSero))

**在承诺付费提供商或本地部署之前，使用此案例通过免费 ZCode 津贴测试 GLM-5.2。**

作者通过 ZCode 描述了 GLM-5.2 的可用性，并提供了大量免费的每日代币津贴，并指出了设置 vLLM Studio 或本地托管的可能用途。

类型: 集成 | 日期: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (作者 [@JZiyue_](https://x.com/JZiyue_))

**使用此案例来查找用于 GLM-5.2 测试的时间限制的自由访问窗口。**

该帖子在 ZenMux 上宣传 GLM-5.2，提供一周免费窗口、100 万上下文、编码和代理改进以及与 5.1 相同的价格定位。

类型: 集成 | 日期: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAI 每代币定价](https://x.com/nahcrof/status/2067166596523765781) (作者 [@nahcrof](https://x.com/nahcrof))

**在选择路线之前，使用此案例比较 GLM-5.2 的第三方提供商定价。**

该帖子宣布了 crofAI 上的 GLM-5.2，列出了输入、输出和缓存价格，将其定位为廉价的前沿智能。

类型: 集成 | 日期: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (作者 [@scaling01](https://x.com/scaling01))

**将 GLM-5.2 与其他前沿实验室和开放模型进行比较时，请使用此案例作为市场定价批评。**

作者在输出代币定价方面比较了 GLM-5.2 和其他大型开放模型，并通过比较来论证一些前沿实验室 API 利润率很高。

类型: 评测 | 日期: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://x.com/volatilemrkts/status/2068077319986516031) (作者 [@volatilemrkts](https://x.com/volatilemrkts))

**在规划离线编码设置之前，使用此案例来估计大内存 Apple 硬件上的本地 GLM-5.2 推理吞吐量。**

消息来源报告在本地高内存 Mac 设置上每秒 44.1 个令牌，并提到大量工具调用的解码重复问题。

类型: 演示 | 日期: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (作者 [@mrblock](https://x.com/mrblock))

**当完整模型权重对于普通本地硬件来说太大时，使用此案例来评估量化的 GLM-5.2 部署路径。**

这篇文章介绍了 Unsloth 动态 2 位和 1 位 GGUF 选项、内存减少以及 llama.cpp 或 Unsloth Studio 部署路线。

类型: 教程 | 日期: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。**

帖文展示了 GLM-5.2 8-bit 在两台 M3 Ultra 512GB 机器上通过 MLX distributed 运行的情况，速度约 17.9 tokens/sec，总内存占用约 760GB。作者也明确说明这仍是一个进行中的 PR，因此它更适合作为 deployment signal，而不是完整部署指南。

类型: 演示 | 日期: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (作者 [@buildwithhassan](https://x.com/buildwithhassan))

**用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。**

这条帖文表示，ZCode 已把 GLM coding plan multiplier 在高峰时段从 3x 下调到 2x，在非高峰时段从 2x 下调到 0.67x，而且新窗口会持续到 9 月底。对于想在 GLM-5.2 上尽量拉长 credits 的人来说，这是一个非常具体的 access / pricing note。

类型: 集成 | 日期: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想评估高端本地 GLM-5.2 工作站的规模，可以用这个案例。双 Blackwell 桌面机在 4-bit 量化版本上保持了两位数的 decode 速度。**

CardilloSamuel 表示，他在 2x RTX PRO 6000 Blackwell、Threadripper PRO 9995WX 和 1TB DDR5 的配置上运行了 GLM-5.2 UD-Q4_K_XL。帖子给出的数据包括约 64 tok/s 的 prefill、13-15 tok/s 的 decode、69.7% 的 Aider Polyglot 分数，且与 BF16 只差 2 分以内。帖子还指出，系统 RAM 带宽是瓶颈，因此没有把不匹配的 5090 放进分卡运行里。

类型: 演示 | 日期: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (作者 [@karminski3](https://x.com/karminski3))

**如果你想判断为了本地 GLM-5.2 推理购买 Mac Studio 是否划算，可以用这个案例。帖子里的回本测算明显更倾向于 API 或套餐访问。**

帖子估算，一台 32,999 RMB 的 Mac Studio，大致相当于按文中定价购买约 11.78 亿个 GLM-5.2 API token。它还认为，即便是更小的 Qwen 本地方案，回本期也大约要 209 天。随后帖子进一步指出，一台 512GB 的 Mac Studio 即便以约 17 tok/s 跑量化版 GLM-5.2，可能也要约 7 年才能回本，因此只有在你已经拥有这台机器，或者能充分利用空闲时间时，本地持有才更合理。

类型: 评测 | 日期: 2026-06-22

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、注意事项与安全信号

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (作者 [@sawyerhood](https://x.com/sawyerhood))

**使用此案例请记住，GLM-5.2 对于需要本机视觉功能的工作流程可能不太有用。**

作者引用 Design Arena 排名文章指出，缺乏远见的 GLM 模型降低了实用性。这是多模式产品规划的一个实际警告。

类型: 限制 | 日期: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [现实世界的代理差距警告](https://x.com/ml_angelopoulos/status/2067013545431269405) (作者 [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**使用此案例可以避免过度阅读基准测试胜利，以证明 GLM-5.2 与所有已部署的代理任务上的最佳专有模型相匹配。**

作者表示，GLM-5.2 令人印象深刻，但基于 Agent Arena 方法论，在现实世界代理任务的一般分布上尚未接近寓言级或 Opus 4.8 思维级性能。

类型: 限制 | 日期: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (作者 [@VittoStack](https://x.com/VittoStack))

**使用此案例提醒您在敏感域中部署 GLM-5.2 之前运行安全评估。**

该帖子报告了比较安全测试中有害内容拒绝失败的情况。该存储库仅记录安全信号，而不记录不安全的详细信息，并将其视为部署风险警告。

类型: 限制 | 日期: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [基准方法论批评](https://x.com/josepha_mayo/status/2066951013337112661) (作者 [@josepha_mayo](https://x.com/josepha_mayo))

**即使总体结果有利于 GLM-5.2，也可以使用此案例来质疑基准方法。**

作者批评了 Design Arena 方法，但仍然承认 GLM-5.2 很强大，这对于那些想要对基准怀疑论和排行榜主张的读者有用。

类型: 限制 | 日期: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (作者 [@k_matsumaru](https://x.com/k_matsumaru))

**在切换编码计划或将 Claude 代码式工作流程路由到 GLM-5.2 之前，使用此案例测试提供程序延迟。**

日本帖子考虑在编码计划中使用 GLM-5.2，但指出了之前对高峰时间响应延迟的担忧。

类型: 限制 | 日期: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (作者 [@nikhilchandak29](https://x.com/nikhilchandak29))

**在广泛部署之前，使用此案例检查编码增益是否推广到非编码领域。**

该帖子报告 GLM-5.2 在 FutureSim 上并不比 GLM-5.1 更好，并使用结果来警告编码改进可能不会在所有领域中同等推广。

类型: 限制 | 日期: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (作者 [@bridgemindai](https://x.com/bridgemindai))

**使用此案例将模型功能与启动执行、文档和 API 准备情况分开。**

这篇文章称早期版本很混乱，因为当时尚未提供基准测试和 API 访问，这使得它与发布准备情况审查相关，而不是模型质量判断。

类型: 限制 | 日期: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [编码计划价格上涨](https://x.com/bridgemindai/status/2065799843658793092) (作者 [@bridgemindai](https://x.com/bridgemindai))

**在推荐 GLM-5.2 作为低成本替代品之前，请使用此案例验证计划定价。**

作者报告称每月支付 65 美元购买 GLM Coding Pro 计划，并表示该计划自上次订阅以来几乎翻了一番。使用它作为检查当前定价的提醒。

类型: 限制 | 日期: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [短时间并行工作与长代理运行](https://x.com/thekuchh/status/2068010332501479865) (作者 [@thekuchh](https://x.com/thekuchh))

**使用此案例将 GLM-5.2 路由到短边界编码任务，同时为更深的多小时代理运行保留更强的模型。**

这篇文章报告了一个实际的划分：GLM-5.2 对于短期并行任务效果很好，但在较长的代理运行上会出现偏差。

类型: 限制 | 日期: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [代码审查与偏见检查](https://x.com/wongmjane/status/2068424945663893936) (作者 [@wongmjane](https://x.com/wongmjane))

**用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。**

作者称，GLM-5.2 没有把中国政治审查内容注入到代码中；同时它还纠正了一个关于越南战争的错误“美国偏见”说法，而对偏意见解类问题保持不变。这使它成为测试政治敏感编码行为和事实性表现的一个具体公开案例。

类型: 限制 | 日期: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高难推理计费异常](https://x.com/s_batzoglou/status/2068297051247350154) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。**

作者运行了 11 个归纳推理题，只报告 4 个完成、2 个答对、多小时级运行时间，以及明显高于可见 token 数的收费。这是关于推理效率和计费行为的具体警示，不只是 benchmark 分数问题。

类型: 限制 | 日期: 2026-06-20

---


<a id="acknowledge"></a>
## 🙏 致谢

本仓库来自公开分享 GLM-5.2 使用证据的创作者、开发者、benchmark 团队、供应商和社区。

感谢这些高信号来源创作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)。

*我们无法保证每个案例都已归属到最初原创者。如果需要修正来源或署名，请联系我们，我们会更新。*

如果你有更多值得收录的 GLM-5.2 使用案例，欢迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
