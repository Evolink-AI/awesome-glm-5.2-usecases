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

- **166 个精选 GLM-5.2 案例**，来自公开创作者、评测团队、工具开发者、服务商和一线使用者。
- 覆盖基准与前沿评测、编码代理与长上下文工作流、上手演示与作品展示、供应商与工具集成、成本、定价与本地部署、限制、注意事项与安全信号。
- 每个案例都包含原始来源、创作者署名、简洁的使用结论、证据类型和发布日期。
- 你可以用这个 repo 查找实用工作流、比较优势和限制、发现供应商路径，并跟踪真实上手实验。

> [!NOTE]
> 本仓库重视具体证据，而不是 hype：已发布 demo、benchmark 方法、集成笔记、成本数据和明确 caveat。

> [!NOTE]
> 多语言 README 会保持与英文源相同的案例顺序、链接、anchor 和署名；为了可追溯性，部分标题会保留接近原文的写法。

<a id="quick-start"></a>
## ⚡ Quick Start

通过 Evolink 的 OpenAI 兼容 Chat Completions API 使用 GLM-5.2。先在 [Evolink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) 获取 API key，然后在执行请求前设置为 `EVOLINK_API_KEY`。

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
| [📏 基准与前沿评测](#benchmarks-frontier-evaluation) | 案例 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162 |
| [💻 编码代理与长上下文工作流](#coding-agents-long-context-workflows) | 案例 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155 |
| [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds) | 案例 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161 |
| [🔌 供应商与工具集成](#provider-tool-integrations) | 案例 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165 |
| [💸 成本、定价与本地部署](#cost-pricing-local-deployment) | 案例 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166 |
| [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals) | 案例 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163 |
| [🙏 致谢](#acknowledge) | 来源致谢与修正政策 |

### [📏 基准与前沿评测](#benchmarks-frontier-evaluation)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 162: VulcanBench 10-Task 80 Percent Tie](#case-162) | 如果你想在成本和分数同样重要的 post-cutoff 真实工程任务中比较 GLM-5.2，可以看这个案例，因为 Morgan Linton 说 VulcanBench 让 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 个 repo 上都拿到 80%，而 GLM 的成本落在中间。 | 评测 |
| [Case 159: SWE-Rebench 51.1 Percent Checkpoint](#case-159) | 如果你想持续跟踪 GLM-5.2 在 SWE agent 榜单上的位置，可以看这个案例，因为最新一条 SWE rebench 帖子给出的成绩是 51.1%，消耗 262 万 token，明显高于新加入的 DeepSeek、MiMo、Qwen 和 Gemma。 | 评测 |
| [Case 154: LaunchDarkly Edge-Case Win At 40/41](#case-154) | 如果你想看 GLM-5.2 在企业工具型 agent 任务里的表现，而不是只看聊天评测，可以用这个案例，因为 Composio 说它在 GitHub、Jira 和 LaunchDarkly 的 41 个任务里做对了 40 个，而且只有 GLM 抓到了一个待审批边界条件。 | 评测 |
| [Case 110: AA-Briefcase 每任务耗时前沿](#case-110) | 用这个案例比较 GLM-5.2 在长周期知识工作上的表现，因为除了 benchmark 分数，单任务耗时同样关键。 | 基准 |
| [Case 111: Code Arena 前端对战优势](#case-111) | 用这个案例查看 GLM-5.2 在前端任务上的成对对战优势，而不是只看一张排名截图。 | 基准 |
| [Case 113: SWE Atlas 代码库问答亚军](#case-113) | 用这个案例跟踪 GLM-5.2 在代码库问答、测试编写和重构三条 SWE Atlas 榜单上的表现，而不是只看单项 SWE 榜单。 | 基准 |
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
| [Case 155: Cotal Four-Agent TUI Loop](#case-155) | 如果你想把一个编码循环拆给不同专长的 agent，可以看这个案例，因为作者用两个 GLM-5.2 worker，外加一个 Opus 负责人和一个 GPT reviewer，在 47 分钟内无人干预地做完了一个 lazygit 风格的完整 TUI。 | 演示 |
| [Case 153: Legacy Migration Cost-Cut Pilot](#case-153) | 如果你想评估 GLM-5.2 在遗留应用改造流程里能不能当更便宜的执行模型，可以看这个案例，因为 8090 的试点说 GLM 加 Software Factory 相比单跑 Opus 4.8 把成本压到了 1/16.4，但速度大约慢了 3 倍。 | 评测 |
| [Case 145: OpenCode + Fireworks 降本迁移](#case-145) | 如果你想测试只换 open-model harness 是否已经足够，可以用这个案例，因为作者把个人 coding 和 loop task 迁到 Fireworks 上的 GLM-5.2 + OpenCode 后，称 token 成本降到了三分之一，而且日常质量没有明显掉档。 | 评测 |
| [Case 143: Hermes MoA 的 GLM 聚合器工作流](#case-143) | 如果你愿意为高价值 agent 回合多做一层编排，可以用这个案例，因为 Hermes Agent 的 MoA 设置把 GLM-5.2 和其他模型组合后，在帖子里的 demo 中用很小的增量成本换来了更好的输出。 | 集成 |
| [Case 142: Cline 推理开关带来的 Harness 差值](#case-142) | 如果你想判断决定结果的是 harness 还是权重本身，可以用这个案例，因为同一个 GLM-5.2 在同一批 coding task 上，仅仅打开 reasoning，结果就从 57.3% 跳到 68.5%。 | 评测 |
| [Case 136: Cursor + Fireworks 4.55 亿 Token 实战测试](#case-136) | 如果你想判断 GLM-5.2 是否足以作为严肃的 Cursor 日常默认模型，可以用这个案例，因为作者报告了 4.55 亿 token 的真实使用量、快速的 Fireworks 服务体验，以及暂时不想切回 Opus 或 GPT-5.5。 | 评测 |
| [Case 135: Devin Desktop Harness 与 Skill 可移植性](#case-135) | 如果你觉得 Z.ai 自家的 coding surface 不稳定，想在 Devin Desktop 里测试 GLM-5.2，可以用这个案例，因为作者报告了更容易迁移 skill、更高速度和更好的可 hack 性。 | 评测 |
| [Case 127: Pi 内联 GLM 审阅者](#case-127) | 如果你想在 Pi 风格的 coding-agent loop 里加入第二位审阅者，可以用这个案例。作者表示，GLM-5.2 可以逐回合给 Opus 提建议，成本增幅大约只有 10%。 | 集成 |
| [Case 122: AgentRouter 一次成型 Telegram Bot](#case-122) | 如果你想测试 GLM-5.2 在 one-shot coding-agent build 里，是否能主动补上偏向生产环境的 defaults，而不是只写出最低限度可运行的路径，可以用这个案例。 | 演示 |
| [Case 117: OpenCode Go 重构首轮取胜](#case-117) | 用这个案例评估 GLM-5.2 在 OpenCode 中处理中等规模 Go 重构任务的表现，而不是只看 benchmark 宣传。 | 评测 |
| [Case 119: Claude Code + Cursor 默认运行成本 3.36 美元](#case-119) | 用这个案例判断 GLM-5.2 是否适合作为 Claude Code 和 Cursor 的日常默认模型，再决定是否把更多自主编码工作迁移到开放权重模型上。 | 评测 |
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
| [Case 102: OpenInspect FP8 Background Agent](#case-102) | 如果你想研究自托管的 GLM-5.2 后台 agent 栈，而不是托管聊天工作流，可以用这个案例。 | 集成 |

### [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 161: REAP NVFP4 Rubiks Cube One-Shot](#case-161) | 如果你想测试 GLM-5.2 在单一 prompt 的互动式 build 任务上的表现，可以看这个案例，因为 REAP-NVFP4 的 demo 说它只靠一个 prompt 就做出了 3D Rubiks Cube、真实 scramble、实时状态和 solve 按钮。 | 演示 |
| [Case 158: OMP Relay iPhone Client](#case-158) | 如果你想把一个本地 GLM-5.2 agent 很快包进移动端界面，可以看这个案例，因为作者说 Codex 的 build-ios-app plugin 只用了几个小时，就给一个已经接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很强的 iPhone 客户端。 | 演示 |
| [Case 144: 开源 DevRel 研究 Agent](#case-144) | 如果你想把 GLM-5.2 从通用聊天模型变成垂直研究助手，可以用这个案例，因为作者做了一个开源 DevRel agent，能把产品和受众输入转成带证据和提纲的选题列表。 | 演示 |
| [Case 123: Recast 六版本落地页迭代流程](#case-123) | 如果你想先用 GLM-5.2 生成多个版本，再把最佳结果交给 coding agent 继续做，以低成本试作 landing page，可以用这个案例。 | 教程 |
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
| [Case 100: Luddite Game After Claude Refusal](#case-100) | 如果闭源模型因策略原因拒绝请求，而你又想原型化带策略敏感性的游戏概念，可以用这个案例测试 GLM-5.2。 | 演示 |

### [🔌 供应商与工具集成](#provider-tool-integrations)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 165: ZCode Launch With Mobile Agent Control](#case-165) | 如果你想把 ZCode 当成 GLM-5.2 的官方 coding surface 来评估，可以看这个案例，因为 launch report 说这个免费的 agentic IDE 会上 Windows、macOS、Linux，还能通过 Telegram、WeChat、Feishu 跟踪项目进度。 | 集成 |
| [Case 160: OpenWiki Auto-Maintained Agent Docs](#case-160) | 如果你想让 agent 可读的文档自动保持最新，可以看这个案例，因为 LangChain 说 OpenWiki 会随着代码变化重建并维护 repo docs，而且能跑在 GLM 5.2 这类开源模型上。 | 集成 |
| [Case 152: Foundry PTUs Through FireConnect](#case-152) | 如果你想在不重写 agent 客户端的前提下，把 GLM-5.2 接到企业级 Foundry 预算里，可以用这个案例，因为 Fireworks 说 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。 | 集成 |
| [Case 141: ClinePass 开放权重模型统一订阅](#case-141) | 如果你想把多个开放权重 coding model 收拢到同一个 agent harness 里，可以用这个案例，因为 ClinePass 把 GLM-5.2 和相关模型打包成统一月付，而不是分别维护 provider key 和账单。 | 集成 |
| [Case 137: 面向 Coding Agents 的免费 GLM API 服务](#case-137) | 如果你想在 Hermes 或其他 coding agent 里无注册测试 GLM-5.2，可以用这个案例，因为共享服务会发放短时有效的 API key，整体接入足够轻量。 | 集成 |
| [Case 128: Cloudflare Workers AI OpenCode 设置](#case-128) | 如果你想在不自备模型主机的情况下，通过 Cloudflare Workers AI 这条免费的 OpenAI 兼容路线运行 GLM-5.2 做 coding agent，可以用这个案例。 | 教程 |
| [Case 129: Puter.js 零配置浏览器客户端](#case-129) | 如果你想在接触 API key、账单或后端配置之前，先用纯浏览器原型测试 GLM-5.2，可以用这个案例。 | 教程 |
| [Case 130: SiliconFlow 统一端点接入](#case-130) | 如果你想把 GLM-5.2 放进更大的多模型栈里，可以用这个案例，因为帖子描述了一个带 free trial credit 的单一 OpenAI 兼容 SiliconFlow endpoint，同时覆盖中文和西方模型。 | 集成 |
| [Case 124: HuggingChat 建站到 HF Space 部署](#case-124) | 如果你想在几乎免费的 personal-site flow 里试用 GLM-5.2，从 HuggingChat 搜集资料到部署到 Hugging Face Spaces，都可以参考这个案例。 | 教程 |
| [Case 125: DigitalOcean Inference Engine 上线](#case-125) | 如果你想通过 managed infrastructure 获得官方 provider access，而不自己托管 1M context 的模型，可以用这个案例接入 GLM-5.2。 | 集成 |
| [Case 115: Command Code Fast 120-250 Tok/S 档位](#case-115) | 如果你更在意长周期编码任务的响应速度，而不只是最低入门价格，可以用这个案例接入更快的 GLM-5.2 档位。 | 集成 |
| [Case 116: Vercel AI Gateway Fast GLM-5.2 API](#case-116) | 如果你需要 serverless 速度和明确的 token 定价，可以用这个案例通过 Vercel AI Gateway 接入 GLM-5.2 Fast。 | 集成 |
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
| [Case 101: Baseten + Droid Harness Quickstart](#case-101) | 如果你想通过 Baseten 和 Droid harness 快速跑通 GLM-5.2，并复用一套也适用于其他 IDE 的短配置流程，可以用这个案例。 | 教程 |
| [Case 104: OpenAI-Compatible GLM API Workflow](#case-104) | 如果你想在 Python 里用一个 OpenAI 兼容客户端统一接入 GLM-5.2 的推理控制、tool calling、长上下文检索和成本统计，可以用这个案例。 | 教程 |
| [Case 105: Perplexity Agent API Search Sandbox](#case-105) | 如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，并通过单个 API 调用获得带搜索能力的沙盒 agent，可以用这个案例。 | 集成 |
| [Case 109: Baseten 280 TPS GLM API](#case-109) | 如果你在意 provider 延迟表现，可以用这个案例查看 Baseten 对 GLM-5.2 高吞吐、低首 token 延迟的公开性能说法。 | 集成 |

### [💸 成本、定价与本地部署](#cost-pricing-local-deployment)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 166: Full 744B On 5x ASUS GX10s](#case-166) | 如果你想估一个极端 home-lab GLM-5.2 部署的规模，可以看这个案例，因为作者说完整 744B 模型已经能在 5 台 ASUS GX10 上带 full context 跑起来，而且已经接到处理真实 workload 的 causal harness。 | 演示 |
| [Case 164: Agent Route Swap In China Stack](#case-164) | 如果你更在乎成本压力而不是绝对最高质量，想把 GLM-5.2 放进 mixed-model stack 的 agent 层，可以看这个案例，因为作者说把 Sonnet 换成 GLM-5.2 之后，这个 slot 的输入成本降到五分之一，质量大约只掉了 3%。 | 评测 |
| [Case 156: 744B Local Hardware Floor](#case-156) | 如果你想更现实地评估 GLM-5.2 的本地部署门槛，可以看这个案例，因为原帖说即便量化后，2bit 也大约要 239GB、4bit 大约要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比较实际的起步线。 | 限制 |
| [Case 140: B300 x2 Agent 主导双栈 Bring-Up](#case-140) | 如果你想评估严肃的自托管 GLM-5.2 部署范围，可以用这个案例，因为线程展示了分析师在不到一天内就在裸金属 B300 上同时拉起了 vLLM 和 SGLang 的 NVFP4 推理。 | 评测 |
| [Case 139: oMLX 在 M3 Ultra 上的 Prefill 提速](#case-139) | 如果你想在最近的 kernel 工作之后重新判断 Apple Silicon 本地可行性，可以用这个案例，因为作者报告 M3 Ultra 512GB 上的 GLM-5.2 prefill 速度几乎翻倍，而且快速测试里没有明显质量崩塌。 | 评测 |
| [Case 138: 注册即送 2000 万 Token 爆发额度](#case-138) | 如果你想判断官方注册赠送额度是否足以支持一次真正的 GLM-5.2 试用，可以用这个案例，因为帖子声称新账号可获 2000 万免费 token、无需绑卡，并提供完整 OpenAI 兼容访问。 | 集成 |
| [Case 131: 4x DGX Spark 本地 GLM 操作手册](#case-131) | 如果你想判断 DGX Spark 集群是否是现实可行的本地 GLM-5.2 路线，可以用这个案例。整理出来的指南把具体硬件成本、集群拓扑和 vLLM 命令都对应到了 1M context 的 GLM 目标上。 | 教程 |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 跑分](#case-112) | 如果你在评估高端本地工作站方案，可以用这个案例把四卡 GLM-5.2 配置放到高难终端 benchmark 里衡量。 | 评测 |
| [Case 118: 2x RTX PRO 6000 Blackwell 本地 Crackme 解题](#case-118) | 如果你想判断严肃的本地 GLM-5.2 配置能否在没有 debugger 的情况下完成长时逆向任务，可以用这个案例。 | 演示 |
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
| [Case 106: LiteLLM Local Outage Save](#case-106) | 如果托管前沿 API 宕机或额度耗尽，而你又要保证交付不中断，可以用这个案例参考本地部署的 GLM-5.2 与 LiteLLM 兜底。 | 演示 |
| [Case 107: Individual Versus Team Local ROI](#case-107) | 如果你想判断本地部署 GLM-5.2 更适合个人还是团队，可以用这个案例做成本与组织规模判断。 | 评测 |

### [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 163: Preliminary Cyber Research Parity](#case-163) | 如果你想衡量 GLM-5.2 在漏洞研究子任务上的能力，可以看这个案例，因为 Irregular 报告说，在一组范围很窄的 cyber suite 上，它的早期内部评测可与 GPT-5.4 和 Opus 4.6 接近，同时也明确提醒 end-to-end 攻击场景尚未测试。 | 限制 |
| [Case 157: OpenRouter Spend-Cut Skill Rewrite](#case-157) | 如果你想在切换 agent 模型前把迁移成本算清楚，可以看这个案例，因为某个基金团队的 OpenRouter 试验里，GLM-5.2 的成本大约只有 Opus 的八分之一，但依然要重写 skill、补 routing 逻辑，还得接受更慢、更弱一些的输出。 | 限制 |
| [Case 134: Semgrep IDOR 窄胜场景提醒](#case-134) | 如果你想把真实安全信号和标题党式放大区分开，可以用这个案例，因为来源明确说 GLM-5.2 只是在一个 IDOR benchmark 上赢过 Claude Code，并没有直接测试 Mythos 本身。 | 限制 |
| [Case 132: LisanBench 推理效率差距](#case-132) | 如果你想先检查 GLM-5.2 在高推理负载任务上的表现，再决定是否把编码优势外推到其他场景，可以用这个案例。帖子里的 LisanBench 结果显示它虽然比 GLM-5 好，但相较其他开源模型仍然不够高效。 | 限制 |
| [Case 133: PrinzBench 领域错配提醒](#case-133) | 如果你想让 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用这个案例，因为帖子把它较弱的 PrinzBench 分数和更强的软件、工具使用 benchmark 做了对照。 | 限制 |
| [Case 126: Rust 错误修复通过但回合数高 7 倍](#case-126) | 如果你想把 GLM-5.2 的代码质量优势和当前 agent harness 开销区分开来看，可以用这个案例，因为它虽然能修好 bug，却可能比 Opus 消耗得多得多的回合数。 | 评测 |
| [Case 114: Braintrust 模型替换成本警示](#case-114) | 用这个案例避免想当然地认为，在真实 agentic coding workflow 里把模型换成更便宜的选项后，质量还能保持不变。 | 评测 |
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
| [Case 103: HalluHard Multiturn Hallucination Signal](#case-103) | 如果你想在信任其他强基准结果前，先测试 GLM-5.2 在多轮幻觉敏感任务上的表现，可以用这个案例。 | 限制 |
| [Case 108: Open-Weight Security Emergency Warning](#case-108) | 如果你在做安全规划，可以用这个案例理解开放权重 GLM-5.2 如何降低进攻性安全 agent 的实际操作门槛。 | 限制 |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 基准与前沿评测
<a id="case-162"></a>
### Case 162: [VulcanBench 10-Task 80 Percent Tie](https://x.com/morganlinton/status/2072689409011679642) (作者 [@morganlinton](https://x.com/morganlinton))

**如果你想在成本和分数同样重要的 post-cutoff 真实工程任务中比较 GLM-5.2，可以看这个案例，因为 Morgan Linton 说 VulcanBench 让 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 个 repo 上都拿到 80%，而 GLM 的成本落在中间。**

Morgan Linton 说，这个 benchmark 用了来自 Flask、aiohttp、sqlglot 等项目的 10 个真实工程任务，而且都被描述为 post-training-cutoff。Fable 5 Low、GLM 5.2 High 和 Sonnet 5 High 都拿到 80%，对应成本分别是 2.27、8.41、15.81 美元。这让它成为一个很有用的三方价格与质量检查点。

类型: 评测 | 日期: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-Rebench 51.1 Percent Checkpoint](https://x.com/ibragim_bad/status/2072318238407483593) (作者 [@ibragim_bad](https://x.com/ibragim_bad))

**如果你想持续跟踪 GLM-5.2 在 SWE agent 榜单上的位置，可以看这个案例，因为最新一条 SWE rebench 帖子给出的成绩是 51.1%，消耗 262 万 token，明显高于新加入的 DeepSeek、MiMo、Qwen 和 Gemma。**

ibragim_bad 说，这次 SWE rebench 更新把 GLM-5.2 和几款新的开源模型一起加进来了。帖文里的数字显示，GLM 用 262 万 token 跑到 51.1%，而 DeepSeek V4 Pro 是 42.7%，MiMo V2.5 Pro 是 42.4%，Qwen 和 Gemma 更低，因此它是一个很具体的公开榜单检查点。

类型: 评测 | 日期: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case Win At 40/41](https://x.com/composio/status/2072355937415827950) (作者 [@composio](https://x.com/composio))

**如果你想看 GLM-5.2 在企业工具型 agent 任务里的表现，而不是只看聊天评测，可以用这个案例，因为 Composio 说它在 GitHub、Jira 和 LaunchDarkly 的 41 个任务里做对了 40 个，而且只有 GLM 抓到了一个待审批边界条件。**

Composio 把 GLM-5.2、Claude Opus 4.8 和 GPT-5.5 放到 41 个真实工具型 agent 任务里对比，这些任务会用到 GitHub、Jira 和 LaunchDarkly。GLM 做对了 40 个，Opus 和 GPT 都是 39 个。其中一个 LaunchDarkly 任务里，GLM 会先检查待审批项，再判断某个 flag 是否 stale，而另外两个模型只看开关状态就停了。

类型: 评测 | 日期: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench Open-Weight Patch Runner-Up](https://x.com/ValsAI/status/2072099011398627639) (作者 [@ValsAI](https://x.com/ValsAI))

**如果你想衡量 GLM-5.2 在偏攻防式漏洞发现与补丁生成上的能力，可以用这个案例，因为 CyberBench 把它放在 60 个真实 OSS-Fuzz 漏洞上的总榜第二。**

ValsAI 解释说，CyberBench 同时考察两个任务：提交一个只会打崩漏洞版本的 PoC，以及在不破坏行为的前提下修补源码。帖子称，在 60 个来自 OSS-Fuzz 的内存安全漏洞上，GPT-5.5 总体第一，而 GLM 5.2 是表现最强的 open-weight 之一。

类型: 评测 | 日期: 2026-06-30

---

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

<a id="case-120"></a>
### Case 120: [PostTrainBench 可靠性领先](https://x.com/hrdkbhatnagar/status/2070244540108423427) (作者 [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**如果你想比较 GLM-5.2 Max，不只看 headline 分数，也看它在 84 个任务上 failed run 为 0 的 agent reliability，可以用这个案例。**

hrdkbhatnagar 分享了一张 PostTrainBench leaderboard，显示 GLM 5.2 Max reasoning 以 34.29% 略高于 Opus 4.8 Max 的 34.08%。同一条帖子还提到，GLM 在 84 次 runs 中 failed run 为 0，而 Opus agents 的 failure rate 大约在 10% 左右。对于既看重 raw pass rate、也重视 agent reliability 的团队来说，这是一个很有价值的 benchmark。

类型: 基准 | 日期: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211 项仓库任务评测](https://x.com/FireworksAI_HQ/status/2070181898962534570) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在 private repo 的真实 engineering task 上评估 GLM-5.2，而不是只看公开 benchmark，可以用这个案例；帖子同时给出了分数、速度和每任务成本。**

Fireworks 表示，他们与 Faros 联合进行的 211 项真实 engineering task 评测中，Claude Code + GLM-5.2 同时领先于 Claude Code + Opus 4.8 和 Codex + GPT-5.5。帖子给出的数字包括 judge score 0.568 对 0.521 / 0.466、每任务 321 秒 对 775 / 392，以及每任务 0.92 美元 对 1.76 / 2.06，并特别说明 Faros 使用的是自家 repositories 与实际工作，而不只是公开 benchmark。

类型: 评测 | 日期: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase 每任务耗时前沿](https://x.com/ArtificialAnlys/status/2069914443639635978) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用这个案例比较 GLM-5.2 在长周期知识工作上的表现，因为除了 benchmark 分数，单任务耗时同样关键。**

Artificial Analysis 表示，GLM-5.2 位于 AA-Briefcase 的 Pareto 前沿，得分为 1261，单任务平均耗时 16.3 分钟，分数高于 1159 的 GPT-5.5 xhigh，同时仍是该 benchmark 中表现最强的开放权重模型。对于要同时比较长周期交付质量与运行时长的团队来说，这个案例比单看排行榜名次更有参考价值。

类型: 基准 | 日期: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena 前端对战优势](https://x.com/arena/status/2069885722333769963) (作者 [@arena](https://x.com/arena))

**用这个案例查看 GLM-5.2 在前端任务上的成对对战优势，而不是只看一张排名截图。**

arena 拆解了 GLM-5.2 Max 为什么能登上 Code Arena: Frontend 榜首，称它在除一组之外的所有对战配对里都拿到了更高胜率。帖子点名了它对 Kimi-K2.6 的 61.0%、对 Sonnet 4.6 的 59.4%、对 Opus 4.7 Thinking 的 55.0%，以及对 GPT-5.5 xHigh 的 41.7% 对 40.0% 险胜，并提到它与 GLM-5.1 直接打成 45.5% 平手。

类型: 基准 | 日期: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas 代码库问答亚军](https://x.com/ScaleAILabs/status/2069864932913631617) (作者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**用这个案例跟踪 GLM-5.2 在代码库问答、测试编写和重构三条 SWE Atlas 榜单上的表现，而不是只看单项 SWE 榜单。**

Scale AI Labs 表示，GLM 5.2 已经上线 SWE Atlas 的三条榜单：Codebase QnA、Test Writing 和 Refactoring。帖子特别提到它在 Codebase QnA 上拿到第 2 名，并把这一结果描述为开放模型已经能在这些任务上全面逼近前沿闭源系统。

类型: 基准 | 日期: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 编码代理与长上下文工作流
<a id="case-155"></a>
### Case 155: [Cotal Four-Agent TUI Loop](https://x.com/silvanrec/status/2072335315822403656) (作者 [@silvanrec](https://x.com/silvanrec))

**如果你想把一个编码循环拆给不同专长的 agent，可以看这个案例，因为作者用两个 GLM-5.2 worker，外加一个 Opus 负责人和一个 GPT reviewer，在 47 分钟内无人干预地做完了一个 lazygit 风格的完整 TUI。**

silvanrec 说，Cotal 协调了四个模型：两个 GLM-5.2 实例分别做前端和后端开发，GPT-5.5 在后台做 reviewer，Claude Opus 负责领导整个 loop。系统从一个做出真实 TUI 控制台的单一 prompt 出发，跑了四轮，找出了渲染和 tab wiring 的 bug，管理了 agent 之间的 handoff，最后在 47 分钟内产出了可运行结果。帖子还给出了 open source 层的入口：npx cotal-ai setup --full。

类型: 演示 | 日期: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Legacy Migration Cost-Cut Pilot](https://x.com/chamath/status/2072390507628540213) (作者 [@chamath](https://x.com/chamath))

**如果你想评估 GLM-5.2 在遗留应用改造流程里能不能当更便宜的执行模型，可以看这个案例，因为 8090 的试点说 GLM 加 Software Factory 相比单跑 Opus 4.8 把成本压到了 1/16.4，但速度大约慢了 3 倍。**

Chamath 分享了一个把 PHP 迁到 Next.js 的初步试点。接入 8090 Software Factory 的 Opus 4.8 相比单跑 Opus，成本低了 1.4 倍、速度快了 1.5 倍；而同样的 factory 配上 GLM 5.2，则把成本压到了单跑 Opus 的 1/16.4，但运行速度大约慢了 3 倍。帖子也明确说这只是 n=1 的方向性结果，后面还要在 10 到 15 个真实遗留改造任务上重跑。

类型: 评测 | 日期: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio Browser-Use Local Loop](https://x.com/MaziyarPanahi/status/2071955191260151862) (作者 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想测试一套完全本地的 GLM-5.2 栈，是否已经能在消费级硬件上完成轻量 browser agent 工作，可以用这个案例，因为作者在 Mac Studio 上用 llama.cpp 和 browser-use 去 Hugging Face 找到了一个 PII 模型。**

MaziyarPanahi 表示，他先在 Mac Studio 上通过 llama.cpp 本地运行 GLM-5.2，再把它包进一个 browser-use agent loop。帖子里的例子是让模型去 Hugging Face 找 PII 模型，最终定位到了 `privacy-filter-nemotron`。

类型: 演示 | 日期: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop Agent Swap Cost Cut](https://x.com/aronkor/status/2072032854675218538) (作者 [@aronkor](https://x.com/aronkor))

**如果你想在现有 agent harness 里直接试一次模型替换，可以用这个案例，因为 Gumloop 表示把最常用的 agent 换成 GLM-5.2 后，用户几乎没感到质量下降，而 credits 消耗大约少了 50%。**

aronkor 描述了一次 Gumloop 内部实验：在保留同一套 harness 和同一份 prompt 的情况下，把最常用的一批 agent 直接换成了 GLM 5.2。结果是，几乎没人察觉输出质量差异，但 credits 消耗接近减半。

类型: 评测 | 日期: 2026-06-30

---

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

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 Background Agent](https://x.com/colemurray/status/2069485572339707938) (作者 [@colemurray](https://x.com/colemurray))

**如果你想研究自托管的 GLM-5.2 后台 agent 栈，而不是托管聊天工作流，可以用这个案例。**

colemurray 分享了一个由 OpenInspect 和 Modal Inference 组成的完全自托管后台 agent 系统，使用 FP8 版本的 GLM-5.2 运行，并强调速度与对关键基础设施的控制权。原帖内容不长，但明确给出了工具栈与部署方式。

类型: 集成 | 日期: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [OpenCode + Fireworks 降本迁移](https://x.com/SeekingN0rth/status/2071484711327985696) (作者 [@SeekingN0rth](https://x.com/SeekingN0rth))

**如果你想测试只换 open-model harness 是否已经足够，可以用这个案例，因为作者把个人 coding 和 loop task 迁到 Fireworks 上的 GLM-5.2 + OpenCode 后，称 token 成本降到了三分之一，而且日常质量没有明显掉档。**

SeekingN0rth 表示，他在一个周末里把个人 coding 和 loop task 迁到了 Fireworks 上的 GLM 5.2 + OpenCode，token 花费大约降到原来的三分之一。帖子认为真正决定体验的是 harness，而不是是否绝对前沿：OpenCode 的终端体验接近 Claude Code，日常任务没有感到明显质量下滑，而且这种换模型路径同样适用于那些更看重成本而不是极致 SOTA 的企业场景。

类型: 评测 | 日期: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA 的 GLM 聚合器工作流](https://x.com/IBuzovskyi/status/2071601107944571249) (作者 [@IBuzovskyi](https://x.com/IBuzovskyi))

**如果你愿意为高价值 agent 回合多做一层编排，可以用这个案例，因为 Hermes Agent 的 MoA 设置把 GLM-5.2 和其他模型组合后，在帖子里的 demo 中用很小的增量成本换来了更好的输出。**

IBuzovskyi 把 Hermes Agent 的 Mixture of Agents 模式解释为：一个拥有 tool access 的 aggregator 模型，加上若干只提供私有建议的参考模型。帖子给出了一次 coding 测试：单独用 GLM 5.2 花了 13 分钟、0.38 美元；改成 GLM 5.2 聚合 Kimi K2.6 和 MiniMax M3 后，花了 35 分钟、0.47 美元，但动画更顺滑、视觉更好、游戏机制也更干净。帖子还补充了 preset 设计、功能入口，以及什么场景值得承担额外延迟。

类型: 集成 | 日期: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline 推理开关带来的 Harness 差值](https://x.com/akshay_pachaar/status/2071638409022763292) (作者 [@akshay_pachaar](https://x.com/akshay_pachaar))

**如果你想判断决定结果的是 harness 还是权重本身，可以用这个案例，因为同一个 GLM-5.2 在同一批 coding task 上，仅仅打开 reasoning，结果就从 57.3% 跳到 68.5%。**

akshay_pachaar 引用了一个 Cline 测试：同样的 GLM 5.2、同样的 coding task，一次关闭 reasoning，结果是 57.3%；一次开启 reasoning，结果是 68.5%。这条帖子用这个差值说明，当目标是产出可交付代码而不只是文本时，上下文延续、工具可达性、编辑应用方式和验证 loop，可能和底层模型本身一样重要。

类型: 评测 | 日期: 2026-06-29

<a id="case-136"></a>
### Case 136: [Cursor + Fireworks 455M-Token Field Test](https://x.com/robinebers/status/2071246749210190132) (作者 [@robinebers](https://x.com/robinebers))

**如果你想判断 GLM-5.2 是否足以作为严肃的 Cursor 日常默认模型，可以用这个案例，因为作者报告了 4.55 亿 token 的真实使用量、快速的 Fireworks 服务体验，以及暂时不想切回 Opus 或 GPT-5.5。**

robinebers 表示，在 Cursor 里切到搭配 Fireworks 的 GLM 5.2 之后，短短 36 小时就改变了他对这个模型的看法。帖子特别点出它支持图像、宣称零数据保留、吞吐大约在每秒 80-100 tokens，以及 4.55 亿 tokens 大约花费 145 美元。这使它成为比泛泛 benchmark 夸赞更扎实的 harness 场景评测，也提供了一个很具体的证据：provider 选择会显著改变实际使用体验。

类型: Evaluation | 日期: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Devin Desktop Harness With Skill Portability](https://x.com/lily_gpupoor/status/2071297351801794850) (作者 [@lily_gpupoor](https://x.com/lily_gpupoor))

**如果你觉得 Z.ai 自家的 coding surface 不稳定，想在 Devin Desktop 里测试 GLM-5.2，可以用这个案例，因为作者报告了更容易迁移 skill、更高速度和更好的可 hack 性。**

lily_gpupoor 表示，在一段 API 不稳定时期，通过 Devin Desktop 重度使用 GLM-5.2 的体验，明显好于直接使用 Z.ai 的 coding plan。帖子强调了三个具体工作流收益：GLM 成功编辑了自定义 Solarized Green 主题 JSON 并顺利注册扩展、Devin 体感速度异常快，以及之前构建的 skills 在从默认 Windsurf Cascade agent 切换到 Devin Local 后大多都能继续沿用。

类型: Evaluation | 日期: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi 内联 GLM 审阅者](https://x.com/xpasky/status/2070831715518460177) (作者 [@xpasky](https://x.com/xpasky))

**如果你想在 Pi 风格的 coding-agent loop 里加入第二位审阅者，可以用这个案例。作者表示，GLM-5.2 可以逐回合给 Opus 提建议，成本增幅大约只有 10%。**

xpasky 表示，Pi 用户可以照搬一种 OMP 风格的模式，让第二个模型审阅每一回合，并把建议内联注入。帖子特别提到，GLM 5.2 会持续盯着 Opus，两个模型还会明显“拌嘴”，而额外这位 GLM reviewer 平均只会让 Opus API 成本增加约 10%。因此，这更像是一种具体的多模型监督模式，而不是完整的模型替换方案。

类型: 集成 | 日期: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter 一次成型 Telegram Bot](https://x.com/MatinSenPai/status/2070259817818812701) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**如果你想测试 GLM-5.2 在 one-shot coding-agent build 里，是否能主动补上偏向生产环境的 defaults，而不是只写出最低限度可运行的路径，可以用这个案例。**

MatinSenPai 表示，他用视频里相同的 prompt，让 GLM 5.2 一次完成了一个 Telegram bot，而且模型还主动补上了一些没有明说的实务细节。帖子特别提到，模型会在发送视频后自动清理文件、会考虑 Telegram Bot API 的大小限制并设置默认 50 MB cap、会在结束前反复 self-test，整体 structure 也比之前的 MiMo build 更干净。作者还补充，这次通过 AgentRouter 的执行大约用了 140K tokens、约 5 美元。

类型: 演示 | 日期: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go 重构首轮取胜](https://x.com/vedovelli74/status/2069889605969592500) (作者 [@vedovelli74](https://x.com/vedovelli74))

**用这个案例评估 GLM-5.2 在 OpenCode 中处理中等规模 Go 重构任务的表现，而不是只看 benchmark 宣传。**

vedovelli74 报告了自己第一次用 OpenCode 处理一个中等规模 GoLang 代码库重构，称 GLM-5.2 比 Opus 4.8 更快、更省 token，而且在第一轮就正确判断了需要重构的部分。作者还补充说，后续又用 Codex 和 Opus 做了交叉验证，但最终交付质量仍然是 GLM-5.2 更胜一筹。

类型: 评测 | 日期: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 默认运行成本 3.36 美元](https://x.com/clairevo/status/2069828122640548204) (作者 [@clairevo](https://x.com/clairevo))

**用这个案例判断 GLM-5.2 是否适合作为 Claude Code 和 Cursor 的日常默认模型，再决定是否把更多自主编码工作迁移到开放权重模型上。**

clairevo 表示，GLM 5.2 已经成为她在 Claude Code 和 Cursor 里的默认模型，目前累计成本只有 3.36 美元，同时却给出了类似 Opus 的编码体验。帖子还提到了通过 OpenRouter 的接入路径、前端设计感受，以及一项长时自主任务评测，这些都是它最终说服作者切换默认模型的原因。

类型: 评测 | 日期: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手演示与作品展示
<a id="case-161"></a>
### Case 161: [REAP NVFP4 Rubiks Cube One-Shot](https://x.com/RoundtableSpace/status/2072700573145788914) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想测试 GLM-5.2 在单一 prompt 的互动式 build 任务上的表现，可以看这个案例，因为 REAP-NVFP4 的 demo 说它只靠一个 prompt 就做出了 3D Rubiks Cube、真实 scramble、实时状态和 solve 按钮。**

RoundtableSpace 说，GLM-5.2-REAP-NVFP4 只收到一个 HTML prompt，就返回了一个可运行的 3D Rubiks Cube app，里面有实时状态、真实 scramble 逻辑和 solve 动作。帖文没有公开太多代码，但它依然是一个很具体的 one-shot build demo，而不是泛泛的 benchmark 截图。

类型: 演示 | 日期: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP Relay iPhone Client](https://x.com/mov_axbx/status/2072192903762288721) (作者 [@mov_axbx](https://x.com/mov_axbx))

**如果你想把一个本地 GLM-5.2 agent 很快包进移动端界面，可以看这个案例，因为作者说 Codex 的 build-ios-app plugin 只用了几个小时，就给一个已经接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很强的 iPhone 客户端。**

mov_axbx 说，他想给一个本地托管的 OMP agent 做个手机 app，于是用了 Codex 的 build-ios-app plugin，几个小时内就拿到了比较完整的版本。后端路径则是一个用 GLM-5.2 和 OMP 写的自定义 relay，Cloudflare 负责隧道。

类型: 演示 | 日期: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [开源 DevRel 研究 Agent](https://x.com/Astrodevil_/status/2071572680470655253) (作者 [@Astrodevil_](https://x.com/Astrodevil_))

**如果你想把 GLM-5.2 从通用聊天模型变成垂直研究助手，可以用这个案例，因为作者做了一个开源 DevRel agent，能把产品和受众输入转成带证据和提纲的选题列表。**

Astrodevil_ 用 GLM-5.2 做了一个 chat-first 的 DevRel 研究应用：输入产品和受众简介后，它会去 Hacker News 搜需求信号、去 DEV 找内容缺口，再通过 Engram memory 更新事实，最后返回带证据和提纲的排序选题。帖子还点明了技术栈：Agno、Weaviate Engram、Nebius inference，以及一个开源代码库。

类型: 演示 | 日期: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 六版本落地页迭代流程](https://x.com/nutlope/status/2070199649818779914) (作者 [@nutlope](https://x.com/nutlope))

**如果你想先用 GLM-5.2 生成多个版本，再把最佳结果交给 coding agent 继续做，以低成本试作 landing page，可以用这个案例。**

nutlope 描述了一个围绕 GLM 5.2 与 Recast 的 web iteration workflow：先用同一个 prompt 生成 6 个 landing page 版本，挑出最好的 design，下载那份 code，再交给另一个 coding agent 继续迭代。作者表示，GLM-5.2 在这个场景里表现很好，因为它又快、又便宜，而且很有 design sense；同样的预算通常可以做出 3 到 6 个 GLM 版本，才相当于 Opus 4.8 生成 1 个页面的成本。

类型: 教程 | 日期: 2026-06-25

---

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

<a id="case-100"></a>
### Case 100: [Luddite Game After Claude Refusal](https://x.com/atmoio/status/2069559053114577088) (作者 [@atmoio](https://x.com/atmoio))

**如果闭源模型因策略原因拒绝请求，而你又想原型化带策略敏感性的游戏概念，可以用这个案例测试 GLM-5.2。**

atmoio 表示，Claude 把一个关于摧毁 AI 的幽默版 Plague Inc 风格游戏请求判定为违反可接受使用政策，因此作者改用 GLM 5.2 做出了名为 Luddite 的游戏，并附上了 demo 片段。这个案例更适合被看作创意编码任务在闭源模型拒绝后的实操替代路径，最终可玩性仍应自行检查。

类型: 演示 | 日期: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 供应商与工具集成
<a id="case-165"></a>
### Case 165: [ZCode Launch With Mobile Agent Control](https://x.com/Digiato/status/2072663459850829985) (作者 [@Digiato](https://x.com/Digiato))

**如果你想把 ZCode 当成 GLM-5.2 的官方 coding surface 来评估，可以看这个案例，因为 launch report 说这个免费的 agentic IDE 会上 Windows、macOS、Linux，还能通过 Telegram、WeChat、Feishu 跟踪项目进度。**

Digiato 把 ZCode 描述成一个围绕 GLM-5.2 建立的免费 agentic development environment，定位上对标 Cursor、Claude Code 和 Copilot。帖文说它支持 Windows、macOS、Linux，与 GLM-5.2 深度集成，并能通过 Telegram、WeChat、Feishu 查看项目进度。这让它比一般的模型上线公告更有实际接入价值。

类型: 集成 | 日期: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki Auto-Maintained Agent Docs](https://x.com/LangChain/status/2072745455788933321) (作者 [@LangChain](https://x.com/LangChain))

**如果你想让 agent 可读的文档自动保持最新，可以看这个案例，因为 LangChain 说 OpenWiki 会随着代码变化重建并维护 repo docs，而且能跑在 GLM 5.2 这类开源模型上。**

LangChain 把 OpenWiki 描述成一层面向 coding agent 的开源文档维护工具。帖文说它把 open harness 和 open CLI workflows 结合起来，会在 codebase 变化时更新文档，并且能跑在 GLM 5.2、Kimi K2.7 这类开源模型上。对于想让 agent 读到最新 repo docs、而不是依赖人工维护 wiki 的团队来说，这是一个很实用的 file-based memory 模式。

类型: 集成 | 日期: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [Foundry PTUs Through FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在不重写 agent 客户端的前提下，把 GLM-5.2 接到企业级 Foundry 预算里，可以用这个案例，因为 Fireworks 说 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。**

Fireworks 表示，GLM 5.2 已经上线 Microsoft Foundry。启用 FireConnect 后，团队可以一边消耗 Foundry PTU，一边继续从 Codex、OpenCode 或 Pi 发请求，而不必为每个 agent 入口单独搭一套模型接入路径。

类型: 集成 | 日期: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM Eval Workbench](https://x.com/ankrgyl/status/2072042305108722040) (作者 [@ankrgyl](https://x.com/ankrgyl))

**如果你想把 GLM-5.2 和 Opus 放进同一套 eval 栈里比较，可以用这个案例，因为 Braintrust 联合 Baseten 给出了一个带长上下文成本与精度对照的接入样例。**

ankrgyl 表示，Braintrust 已把 GLM-5.2 接进平台，并由 Baseten 提供支持，团队可以直接在 eval 和 production trace 中跑这个模型。示例比较了 25K 与 50K tokens 的长上下文检索：Opus 4.8 大约高 3.5 分，但每条 trace 的成本约高 4.1 到 4.5 倍。

类型: 集成 | 日期: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass 开放权重模型统一订阅](https://x.com/iam_elias1/status/2071655509611151674) (作者 [@iam_elias1](https://x.com/iam_elias1))

**如果你想把多个开放权重 coding model 收拢到同一个 agent harness 里，可以用这个案例，因为 ClinePass 把 GLM-5.2 和相关模型打包成统一月付，而不是分别维护 provider key 和账单。**

iam_elias1 把 ClinePass 描述成一个月费 9.99 美元的入口，让 GLM-5.2、DeepSeek、Kimi、Qwen、MiniMax、MiMo 等开放权重模型直接进入 Cline 的 IDE 扩展和 CLI。帖子称它可以替代分散的 provider API key，提供 2-5 倍标准 API 限额，还能在同一会话里按编码阶段切换模型，并且通过 CLI 注册首月只要 1.99 美元。

类型: 集成 | 日期: 2026-06-29

<a id="case-137"></a>
### Case 137: [Free GLM API Service For Coding Agents](https://x.com/mcwangcn/status/2071261128575897901) (作者 [@mcwangcn](https://x.com/mcwangcn))

**如果你想在 Hermes 或其他 coding agent 里无注册测试 GLM-5.2，可以用这个案例，因为共享服务会发放短时有效的 API key，整体接入足够轻量。**

mcwangcn 分享了一个免费的 GLM-5.2 API 服务，据称无需注册或登录，就能从 Lobster、Hermes 或其他 coding agents 直接调用。帖子还说，每个生成的 API key 有效期为一小时，到期后需要续领；这是一条很具体的 anti-abuse 约束，也意味着这项服务更适合快速验证工作流，而不是无人值守的长期生产使用。

类型: Integration | 日期: 2026-06-28

---

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

<a id="case-101"></a>
### Case 101: [Baseten + Droid Harness Quickstart](https://x.com/RayFernando1337/status/2069523126384525639) (作者 [@RayFernando1337](https://x.com/RayFernando1337))

**如果你想通过 Baseten 和 Droid harness 快速跑通 GLM-5.2，并复用一套也适用于其他 IDE 的短配置流程，可以用这个案例。**

RayFernando1337 给出了一套带时间戳的教程步骤：获取 Baseten API key、自动化配置 Droid AI、测试 GLM-5.2 集成、查看替代配置与限制，最后再补充其他 IDE 的额外设置说明。

类型: 教程 | 日期: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI-Compatible GLM API Workflow](https://x.com/Marktechpost/status/2069308807570915500) (作者 [@Marktechpost](https://x.com/Marktechpost))

**如果你想在 Python 里用一个 OpenAI 兼容客户端统一接入 GLM-5.2 的推理控制、tool calling、长上下文检索和成本统计，可以用这个案例。**

Marktechpost 分享了一篇教程和配套代码 notebook，演示如何把 GLM-5.2 封装进一个 OpenAI 兼容客户端。帖子称，这套工作流覆盖 thinking effort 控制（`off`/`high`/`max`）、流式 reasoning 与 answer 通道、带多步 agent 的 tool calling、结构化 JSON 输出、长上下文检索，以及 token 成本追踪。

类型: 教程 | 日期: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API Search Sandbox](https://x.com/perplexitydevs/status/2069252848647606584) (作者 [@perplexitydevs](https://x.com/perplexitydevs))

**如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，并通过单个 API 调用获得带搜索能力的沙盒 agent，可以用这个案例。**

Perplexity Devs 宣布在 Agent API 中加入 GLM-5.2，并将其描述为适合长周期 coding 与 agentic workflow 的模型。帖子还特别强调了 Search as Code、OpenAI 兼容接口，以及不加价的一方定价。

类型: 集成 | 日期: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (作者 [@aqaderb](https://x.com/aqaderb))

**如果你在意 provider 延迟表现，可以用这个案例查看 Baseten 对 GLM-5.2 高吞吐、低首 token 延迟的公开性能说法。**

aqaderb 宣布 Baseten 的 GLM-5.2 API 可达到 280 tokens per second，TTFT 低于 0.8 秒。帖子把结果归因于 PD disaggregation、结合 multi-token prediction heads 的 speculative decoding、KV-cache-aware routing 等服务优化，并附上了一篇工程说明文章。

类型: 集成 | 日期: 2026-06-23

---

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI OpenCode 设置](https://x.com/RoundtableSpace/status/2070820686243959276) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想在不自备模型主机的情况下，通过 Cloudflare Workers AI 这条免费的 OpenAI 兼容路线运行 GLM-5.2 做 coding agent，可以用这个案例。**

RoundtableSpace 表示，你可以先注册一个免费的 Cloudflare account，复制 Account ID，创建 API token，再把 Cloudflare 作为 provider 加进 OpenCode，并指定模型 `@cf/zai-org/glm-5.2`。帖子还说，这条路线同样适用于 OpenCode、Cursor、Aider、Hermes Agent、Claude Code 等其他 OpenAI 兼容工具，是一条相当实用的 coding agent 托管接入捷径。

类型: 教程 | 日期: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js 零配置浏览器客户端](https://x.com/FareaNFts/status/2070848321212792945) (作者 [@FareaNFts](https://x.com/FareaNFts))

**如果你想在接触 API key、账单或后端配置之前，先用纯浏览器原型测试 GLM-5.2，可以用这个案例。**

FareaNFts 表示，Puter.js 通过一个 CDN script tag 就能在客户端暴露 GLM 系列模型，`z-ai/glm-5.2` 可以直接在浏览器代码里调用，不需要服务器，也不需要开发者侧的计费配置。帖子把它定位成个人工具、vibe coding app 和轻量 agent 的快速原型路径，同时也说明了代价：Puter 使用的是 user-pays 的浏览器模式，并不适合高吞吐的生产流量。

类型: 教程 | 日期: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 统一端点接入](https://x.com/FareaNFts/status/2070900056736379288) (作者 [@FareaNFts](https://x.com/FareaNFts))

**如果你想把 GLM-5.2 放进更大的多模型栈里，可以用这个案例，因为帖子描述了一个带 free trial credit 的单一 OpenAI 兼容 SiliconFlow endpoint，同时覆盖中文和西方模型。**

FareaNFts 表示，SiliconFlow 通过一个 OpenAI 兼容 endpoint，同时提供 GLM-5.2、DeepSeek、Qwen、Llama 4、Hunyuan、Mistral、Yi、Gemma、Phi 等 200 多个模型。帖子还提到，注册就送 1 美元 free credit、无需绑卡、部分模型持续免费、支持 spending limit，并且这套 key 可以直接塞进 Cursor、Claude Code、Aider 等工具里。

类型: 集成 | 日期: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [HuggingChat 建站到 HF Space 部署](https://x.com/victormustar/status/2070190742991994967) (作者 [@victormustar](https://x.com/victormustar))

**如果你想在几乎免费的 personal-site flow 里试用 GLM-5.2，从 HuggingChat 搜集资料到部署到 Hugging Face Spaces，都可以参考这个案例。**

victormustar 表示，只要有 Hugging Face account，就有足够的 free credits 可以在 HuggingChat 里让 GLM-5.2 帮你建网站，并由 Exa 补足关于用户的背景 research。帖子还提到，最终生成的网站可以免费部署成 static Hugging Face Space，对于 personal site 实验来说，是一条非常具体而且低成本的路线。

类型: 教程 | 日期: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 上线](https://x.com/digitalocean/status/2070177703911719301) (作者 [@digitalocean](https://x.com/digitalocean))

**如果你想通过 managed infrastructure 获得官方 provider access，而不自己托管 1M context 的模型，可以用这个案例接入 GLM-5.2。**

DigitalOcean 宣布在自家的 Inference Engine 上提供 GLM-5.1 和 GLM-5.2，并将它定位为适合长达 8 小时的 agentic coding workflow、拥有 1M-token context window 的模型。帖子也把这条路线描述成一种可直接接入现有 stack 的方案，具备 usage-based pricing 与 fully managed infrastructure。

类型: 集成 | 日期: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S 档位](https://x.com/CommandCodeAI/status/2069891896881857016) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**如果你更在意长周期编码任务的响应速度，而不只是最低入门价格，可以用这个案例接入更快的 GLM-5.2 档位。**

Command Code 宣布上线 GLM-5.2 Fast，称这是一个保持同样 frontier coding 定位、但速度提升到 120-250 tokens per second 的高吞吐版本。帖子还提到，这个档位保留了 1M 上下文、tool use 和 reasoning，并且从 1 美元 Go plan 加 10 美元 usage credits 起就能使用。

类型: 集成 | 日期: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI Gateway Fast GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (作者 [@wafer_ai](https://x.com/wafer_ai))

**如果你需要 serverless 速度和明确的 token 定价，可以用这个案例通过 Vercel AI Gateway 接入 GLM-5.2 Fast。**

wafer_ai 表示，GLM-5.2 Fast 已经上线 Vercel AI Gateway，速度为 150-250 tokens per second，上下文窗口为 1M token，标价为每 1M token 输入 3.00 美元、输出 10.25 美元、缓存 0.50 美元。对于优先考虑吞吐和网关定价可预期性的团队来说，这是一个很具体的托管接入信号。

类型: 集成 | 日期: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定价与本地部署
<a id="case-166"></a>
### Case 166: [Full 744B On 5x ASUS GX10s](https://x.com/thatcofffeeguy/status/2072525885077434743) (作者 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**如果你想估一个极端 home-lab GLM-5.2 部署的规模，可以看这个案例，因为作者说完整 744B 模型已经能在 5 台 ASUS GX10 上带 full context 跑起来，而且已经接到处理真实 workload 的 causal harness。**

thatcofffeeguy 说，完整 744B 的 GLM-5.2 现在已经能在五台 ASUS GX10 系统上带 full context 运行，token rate 也比预期更好，整个 stack 已经接上 causal harness。帖文还没公布精确 throughput 数字，但它已经是一个很具体的公开证据，说明这类本地集群可以承载完整模型，而不只是缩减版。

类型: 演示 | 日期: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Agent Route Swap In China Stack](https://x.com/0xluffy_eth/status/2072548580183900430) (作者 [@0xluffy_eth](https://x.com/0xluffy_eth))

**如果你更在乎成本压力而不是绝对最高质量，想把 GLM-5.2 放进 mixed-model stack 的 agent 层，可以看这个案例，因为作者说把 Sonnet 换成 GLM-5.2 之后，这个 slot 的输入成本降到五分之一，质量大约只掉了 3%。**

这条 thread 列出了 reasoning、code generation、agent calls、batch work、image、video 六个路由变更。对 agent 层来说，作者把 Sonnet 换成 GLM 5.2，并表示性能大约下降 3%，但输入成本便宜了 5 倍。30 天总结则说，整体 AI 运营成本下降了 87%，而收入没有变化。

类型: 评测 | 日期: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B Local Hardware Floor](https://x.com/devjuninho/status/2072151237840007399) (作者 [@devjuninho](https://x.com/devjuninho))

**如果你想更现实地评估 GLM-5.2 的本地部署门槛，可以看这个案例，因为原帖说即便量化后，2bit 也大约要 239GB、4bit 大约要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比较实际的起步线。**

devjuninho 明确反对 open weights 就等于普通用户本地能轻松跑 的说法。帖子里说，GLM-5.2 大约是 744B 参数、其中约 40B 激活，2bit 估算约 239GB、4bit 约 466GB，因此想真正把它本地跑起来，更需要服务器级内存、充足 SSD 和耐心，而不是一台普通游戏 PC。

类型: 限制 | 日期: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Local NVFP4 Rust Port At 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (作者 [@mov_axbx](https://x.com/mov_axbx))

**如果你想估算一套调优后的本地 GLM-5.2 部署在真实 coding 工作里能做到什么，可以用这个案例，因为作者报告了 140 tok/s 的 NVFP4 推理速度，以及几分钟内完成的 Python 到 Rust 全量移植。**

mov_axbx 报告说，一套运行在 OMP 上的本地 GLM-5.2 NVFP4 配置达到了每秒约 140 tokens。帖文还说，这个模型在大约 10 分钟内把一个 Python 卫星定位服务移植到 Rust，随后又在几分钟内搭出了一个 demo web app。

类型: 评测 | 日期: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 Agent-Led Dual-Stack Bring-Up](https://x.com/TheValueist/status/2071261052080148607) (作者 [@TheValueist](https://x.com/TheValueist))

**如果你想评估严肃的自托管 GLM-5.2 部署范围，可以用这个案例，因为线程展示了分析师在不到一天内就在裸金属 B300 上同时拉起了 vLLM 和 SGLang 的 NVFP4 推理。**

TheValueist 表示，一个 analyst-agent 工作流把 GLM 5.2 NVFP4 部署到了裸金属 NVIDIA B300 x2 集群上，并在 vLLM 与 SGLang 两套栈中都跑通了完整 benchmark suite，全部耗时不到 24 小时。线程还说，真正的限制因素是 HBM 容量而不是原始算力；当 KV cache 溢出时，DRAM 才会变得关键。因此，这更像是一条供团队评估本地推理经济性与硬件瓶颈的具体运维备注，而不只是硬件炫耀。

类型: Evaluation | 日期: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 Ultra Prefill Speedup](https://x.com/jundotkim/status/2071287585297887510) (作者 [@jundotkim](https://x.com/jundotkim))

**如果你想在最近的 kernel 工作之后重新判断 Apple Silicon 本地可行性，可以用这个案例，因为作者报告 M3 Ultra 512GB 上的 GLM-5.2 prefill 速度几乎翻倍，而且快速测试里没有明显质量崩塌。**

jundotkim 表示，oMLX 0.4.5.dev1 新增了自定义 MLX kernels，使 GLM-5.2-oQ4 在 32k prefill 场景下于 M3 Ultra 512GB 机器上的速度从 87.7 tok/s 提升到 174.4 tok/s，涨幅达到 98.9%。帖子也明确说这条路径仍然带实验性质，但无论是 needle-in-a-haystack 检查还是 Claude Code 风格的 coding tests，都没有看到明显回归，因此它更像是一条实用的本地推理更新，而不只是 release note。

类型: Evaluation | 日期: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [20M Token Signup Credit Burst](https://x.com/Bitbro4crypto/status/2071150218872283262) (作者 [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**如果你想判断官方注册赠送额度是否足以支持一次真正的 GLM-5.2 试用，可以用这个案例，因为帖子声称新账号可获 2000 万免费 token、无需绑卡，并提供完整 OpenAI 兼容访问。**

Bitbro4crypto 表示，当前 GLM 5.2 的注册路径会给出 2000 万免费 tokens、120 个图像与视频 credits、high 与 max thinking modes、1M context window，以及一个可直接接入 Cursor 或 Claude Code 等工具的 OpenAI 兼容 API，且无需订阅。可以把它视作一个非常具体的 access / pricing signal，用于短期试用判断，但也应假设这种促销额度随时可能变化。

类型: Integration | 日期: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark 本地 GLM 操作手册](https://x.com/TraffAlex/status/2071020631072616698) (作者 [@TraffAlex](https://x.com/TraffAlex))

**如果你想判断 DGX Spark 集群是否是现实可行的本地 GLM-5.2 路线，可以用这个案例。整理出来的指南把具体硬件成本、集群拓扑和 vLLM 命令都对应到了 1M context 的 GLM 目标上。**

TraffAlex 汇总了社区验证过的经验和 NVIDIA 官方资料，表示每台设备售价为 4,699 美元，其他模型用 2x Spark 集群最合适，而 4x Sparks 可以在 1M-token context 下以每秒大约 20 tokens 的速度运行 GLM 5.2 NVFP4。帖子里还给出了 CX7 网络配置、passwordless SSH、NCCL 检查以及示例 vLLM Docker 命令，所以它更像一份可落地的本地 deployment playbook，而不是泛泛的硬件观点。

类型: 教程 | 日期: 2026-06-27

---

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

<a id="case-106"></a>
### Case 106: [LiteLLM Local Outage Save](https://x.com/CardilloSamuel/status/2069431311463236078) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果托管前沿 API 宕机或额度耗尽，而你又要保证交付不中断，可以用这个案例参考本地部署的 GLM-5.2 与 LiteLLM 兜底。**

CardilloSamuel 表示，一位朋友先是用光了 token，又碰上 Claude 宕机，于是他发出一个指向自己本地 GLM-5.2 部署的 LiteLLM API key。帖子称，对方随后以 0 美元生成了约 500 万 token，按时完成交付，并接受了较慢速度来换取持续可用性。

类型: 演示 | 日期: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [Individual Versus Team Local ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想判断本地部署 GLM-5.2 更适合个人还是团队，可以用这个案例做成本与组织规模判断。**

帖子认为，个人本地方案往往需要 512GB 系统内存、多张 GPU 和强 CPU，但速度仍可能只有约 6-10 tokens per second。它进一步指出，对于重视隐私、无限 token、无每周上限，以及不受 provider 宕机或策略变化影响的 10 人以上团队，共享的内部服务器会更合理。

类型: 评测 | 日期: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 跑分](https://x.com/0xSero/status/2069871347010838586) (作者 [@0xSero](https://x.com/0xSero))

**如果你在评估高端本地工作站方案，可以用这个案例把四卡 GLM-5.2 配置放到高难终端 benchmark 里衡量。**

0xSero 报告称，GLM-5.2-REAP-NVFP4 在 Terminal Bench 2.0 上跑到了 69.1%，并把它描述为所有能装进 4x RTX PRO 6000 的模型里 terminal-bench 成绩最高的一档。对于权衡量化开放权重部署和托管前沿终端能力的团队来说，这是一个很具体的本地部署信号。

类型: 评测 | 日期: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell 本地 Crackme 解题](https://x.com/CardilloSamuel/status/2069887782508753302) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想判断严肃的本地 GLM-5.2 配置能否在没有 debugger 的情况下完成长时逆向任务，可以用这个案例。**

CardilloSamuel 表示，一个运行在 2x RTX PRO 6000 Blackwell 和约 300GB RAM 上的本地 GLM 5.2 实例，通过 OpenCode 在大约 78 分钟内、以约 14 tokens per second 的速度解出了一道 crackme 挑战。帖子还说，这套 harness 没有提供 debugger 或 MCP 访问权限，但模型依然会主动转储内存地址、验证假设，并遵循要求去解题，而不是直接 patch 二进制。

类型: 演示 | 日期: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、注意事项与安全信号
<a id="case-163"></a>
### Case 163: [Preliminary Cyber Research Parity](https://x.com/Irregular/status/2072682835798831168) (作者 [@Irregular](https://x.com/Irregular))

**如果你想衡量 GLM-5.2 在漏洞研究子任务上的能力，可以看这个案例，因为 Irregular 报告说，在一组范围很窄的 cyber suite 上，它的早期内部评测可与 GPT-5.4 和 Opus 4.6 接近，同时也明确提醒 end-to-end 攻击场景尚未测试。**

Irregular 说，在一组有限的内部漏洞研究任务中，GLM-5.2 在已测子集上的表现大致接近 GPT-5.4 和 Claude Opus 4.6。帖文同时补充，这组 suite 很窄，而且像 CyScenarioBench、FrontierCyber 这类 scenario-level benchmark 还没有跑。它更像是真实的早期 cyber 能力信号，而不是完整 offensive-agent 对等的证明。

类型: 限制 | 日期: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter Spend-Cut Skill Rewrite](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (作者 [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**如果你想在切换 agent 模型前把迁移成本算清楚，可以看这个案例，因为某个基金团队的 OpenRouter 试验里，GLM-5.2 的成本大约只有 Opus 的八分之一，但依然要重写 skill、补 routing 逻辑，还得接受更慢、更弱一些的输出。**

Rahul J Mathur 说，他们团队的 agent 之前基本只跑在 Opus 模型上，年化开销大约在 10 万美元级别，后来在 6 月开启了一次 OpenRouter 多模型试验，目标是把支出压低约 40%。按他的第一手观察，GLM-5.2 比 Opus 4.8 更慢，也更容易在边界条件或完整读取 skill file 这类地方出错，但从接收方视角看，输出质量在成本只有约八分之一时仍然可以接受。同一个帖子还提醒，面向 Opus 和 GPT 写的 skill 并不能直接平移，迁移过程需要更新 skill、重新建立使用习惯，并补上硬编码的 routing 逻辑。

类型: 限制 | 日期: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA Verbosity And Reasoning Tradeoff](https://x.com/ArtificialAnlys/status/2072022576394821859) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想把 GLM-5.2 的 frontier 级 open-weight 智力表现和它的推理效率成本拆开看，可以用这个案例，因为 Artificial Analysis 一边把它列为开源权重最强，一边也指出它消耗了异常多的输出 token。**

Artificial Analysis 表示，GLM-5.2 Max 为了跑完 Intelligence Index，大约用了 1.41 亿输出 tokens，其中 95% 是 reasoning tokens。这个数字高于 Opus 4.8 的 1.17 亿和 GPT-5.5 的 7200 万，但帖子依然把 GLM-5.2 视为最强 open-weight。

类型: 评测 | 日期: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR Narrow-Win Caveat](https://x.com/leploutos/status/2071121981551047039) (作者 [@leploutos](https://x.com/leploutos))

**如果你想把真实安全信号和标题党式放大区分开，可以用这个案例，因为来源明确说 GLM-5.2 只是在一个 IDOR benchmark 上赢过 Claude Code，并没有直接测试 Mythos 本身。**

leploutos 表示，病毒式传播的“GLM 等于 Mythos”解读是不对的：Semgrep 的结果只是一个 IDOR 检测 benchmark，GLM-5.2 的 F1 为 39%，高于 Claude Code 各配置约 28-37% 的范围，单个 bug 成本约 0.17 美元，大约只有前沿模型的六分之一。帖子也同时点出了实务上真正重要的限制：这只是一个 bug 类别、一份数据集、一次运行，而且还是 vendor-owned benchmark，所以更应该把它看成一个狭窄但真实的漏洞检测信号，而不是 GLM 已经匹敌 Anthropic 专用网络安全模型的证明。

类型: Limit | 日期: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 推理效率差距](https://x.com/scaling01/status/2070961852008509918) (作者 [@scaling01](https://x.com/scaling01))

**如果你想先检查 GLM-5.2 在高推理负载任务上的表现，再决定是否把编码优势外推到其他场景，可以用这个案例。帖子里的 LisanBench 结果显示它虽然比 GLM-5 好，但相较其他开源模型仍然不够高效。**

scaling01 表示，GLM-5.2-high 在 LisanBench 上排第 29，得分 1834，而 GLM-5 的得分是 986.83。帖子还说，Kimi-K2.5 Thinking 用平均约 19K tokens 就能达到相近分数，而 GLM-5.2 大约要消耗 32K tokens，这说明它相比过去的 GLM 代际确实进步了，但在推理效率上仍然偏弱。

类型: 限制 | 日期: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench 领域错配提醒](https://x.com/yuhasbeentaken/status/2070928066797351300) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想让 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用这个案例，因为帖子把它较弱的 PrinzBench 分数和更强的软件、工具使用 benchmark 做了对照。**

yuhasbeentaken 表示，GLM-5.2 在专注法律研究和困难 web search 的窄基准 PrinzBench 上只拿到 30/99，但在 SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0、MCP-Atlas 77.0、ProgramBench 63.7 等公开 benchmark 上表现更强。帖子把这种差异解释为 domain fit 问题，而不是前后矛盾，并建议法律研究优先用更强的 proprietary model，coding 和 agentic execution 则继续用 GLM-5.2。

类型: 限制 | 日期: 2026-06-27

---

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

<a id="case-103"></a>
### Case 103: [HalluHard Multiturn Hallucination Signal](https://x.com/dyfan22/status/2069335764295438532) (作者 [@dyfan22](https://x.com/dyfan22))

**如果你想在信任其他强基准结果前，先测试 GLM-5.2 在多轮幻觉敏感任务上的表现，可以用这个案例。**

HalluHard 在启用 maximum reasoning effort 的 adaptive thinking 设置下，把 GLM-5.2 加入了排行榜。更新指出，尽管它在其他 benchmark 上成绩很强，但在 HalluHard 这种高难多轮 benchmark 上，GLM-5.2 仍然频繁出现幻觉。

类型: 限制 | 日期: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Open-Weight Security Emergency Warning](https://x.com/joshua_saxe/status/2069289170107842572) (作者 [@joshua_saxe](https://x.com/joshua_saxe))

**如果你在做安全规划，可以用这个案例理解开放权重 GLM-5.2 如何降低进攻性安全 agent 的实际操作门槛。**

Joshua Saxe 认为，GLM-5.2 减少了此前对使用前沿 coding agent 的攻击者构成约束的监控与账号摩擦。该线程把开放权重加私有部署视为进攻能力上的一次显著变化，并主张防守侧应更快采用相应能力，而不是继续依赖 API 门禁。

类型: 限制 | 日期: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Rust 错误修复通过但回合数高 7 倍](https://x.com/BohuTANG/status/2069979942608425364) (作者 [@BohuTANG](https://x.com/BohuTANG))

**如果你想把 GLM-5.2 的 code quality 优势和当前的 agent harness overhead 分开来看，可以用这个案例。它能修好 bug，但会比 Opus 消耗得多得多。**

BohuTANG 用同一个 Rust bug，也就是 serde_json issue 979，在 evot、Claude Code、Pi 这 3 个 agents 上比较了 GLM-5.2 与 Opus 4.6。6 个 sessions 全部 pass，作者也表示 GLM 的 bug 理解与最终 code quality 都没有问题；但 GLM 分别用了 38、43、61 个 turns，而 Opus 在 3 个 agents 上大约 18 个 turns、80 秒左右就结束。trace notes 把这个差距归因于反复处理 cargo 与环境、收敛性不佳，以及明显更长的 self-verification loops。

类型: 评测 | 日期: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust 模型替换成本警示](https://x.com/ankrgyl/status/2069869387549446597) (作者 [@ankrgyl](https://x.com/ankrgyl))

**用这个案例避免想当然地认为，在真实 agentic coding workflow 里把模型换成更便宜的选项后，质量还能保持不变。**

ankrgyl 表示，Braintrust 对一个从仓库 commit 和 bug 描述出发、再评估最终修复结果的工作流，比较了 Opus 4.8 和 GLM-5.2。在这种基础替换实验里，GLM-5.2 的成本相近、运行时间更长、通过率更低，因此整体效率反而更差。

类型: 评测 | 日期: 2026-06-24

---


<a id="acknowledge"></a>
## 🙏 致谢

本仓库来自公开分享 GLM-5.2 使用证据的创作者、开发者、benchmark 团队、供应商和社区。

感谢这里收录的高信号来源创作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)、[@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)、[@ScaleAILabs](https://x.com/ScaleAILabs)、[@wafer_ai](https://x.com/wafer_ai)、[@ankrgyl](https://x.com/ankrgyl)、[@vedovelli74](https://x.com/vedovelli74)、[@clairevo](https://x.com/clairevo)。

最近新增的创作者：[@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)、[@TraffAlex](https://x.com/TraffAlex)、[@FareaNFts](https://x.com/FareaNFts)、[@xpasky](https://x.com/xpasky)。

*我们无法保证每个案例都已归属到最初原创者。如果需要修正，请联系我们，我们会更新。*

如果你有更多值得收录的 GLM-5.2 使用案例，欢迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)