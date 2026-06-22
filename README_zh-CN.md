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

- **89 个精选 GLM-5.2 案例**，来自公开创作者、评测团队、工具开发者、服务商和一线使用者。
- Covers Benchmark 与前沿评测, Coding Agent 与长上下文工作流, 上手 Demo 与 Showcase, 供应商与工具集成, 成本、定价与本地部署, 限制、Caveat 与安全信号.
- Each case includes the original source, creator attribution, concise usage takeaway, evidence type, and publication date.
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
| [📏 Benchmark 与前沿评测](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76 |
| [💻 Coding Agent 与长上下文工作流](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80 |
| [🎮 上手 Demo 与 Showcase](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82 |
| [🔌 供应商与工具集成](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87 |
| [💸 成本、定价与本地部署](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89 |
| [🧭 限制、Caveat 与安全信号](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75 |
| [🙏 致谢](#acknowledge) | 来源致谢与修正政策 |

### [📏 Benchmark 与前沿评测](#benchmarks-frontier-evaluation)

| Case | 展示重点 | 类型 |
|---|---|---|
| [Artificial Analysis Intelligence Index](#case-1) | Use the Artificial Analysis post to compare GLM-5.2 against other open-weight and proprietary frontier models on intelligence and cost per task. | Benchmark |
| [Code Arena Frontend Ranking](#case-2) | Use this case to evaluate GLM-5.2 on real front-end coding tasks judged by arena-style comparisons. | Benchmark |
| [Design Arena First Place](#case-3) | Use this case to judge whether GLM-5.2 can handle design-plus-code tasks rather than only text-heavy coding benchmarks. | Benchmark |
| [FrontierSWE Result](#case-4) | Use the FrontierSWE post to compare GLM-5.2 against GPT-5.5, Opus, and Fable-style models on software-engineering tasks. | Benchmark |
| [DeepSWE Open-Source Lead](#case-5) | Use the DeepSWE case to understand GLM-5.2 as a strong open model for difficult software-engineering evaluation tasks. | Benchmark |
| [Terminal-Bench Over 80 Percent](#case-6) | Use this case when evaluating GLM-5.2 for terminal-oriented coding and agent workflows. | Benchmark |
| [SWELancer Comparison Against GPT-5.5](#case-7) | Use this SWELancer case as a concrete multi-metric comparison between GLM-5.2 and GPT-5.5 on task success, reward, and completion time. | Evaluation |
| [BridgeBench Perfect Score Signal](#case-8) | Use this case to inspect GLM-5.2 on grounded multi-step reasoning rather than only coding leaderboards. | Benchmark |
| [BridgeBench Reasoning Number One](#case-9) | Use this case to compare GLM-5.2 with closed frontier models on grounded reasoning tasks. | Benchmark |
| [KernelBench-Hard Without Shortcutting](#case-10) | Use this case when checking whether benchmark gains come from valid implementation behavior instead of shortcutting. | Evaluation |
| [Runescape Bench Catch-Up](#case-11) | Use this case as a fast signal for open-weight model progress on game-like benchmark tasks. | Benchmark |
| [BridgeBench Speed Improvement](#case-12) | Use this case to evaluate latency-sensitive workflows where speed matters alongside intelligence. | Benchmark |
| [Case 60: KernelBench Hard And Mega GPU Coding](#case-60) | Use this case to evaluate GLM-5.2 on GPU-kernel coding across KernelBench-Hard and KernelBench-Mega, where open agent traces make the result inspectable. | Benchmark |
| [Case 70: DeepSWE 高强度模式开源领先](#case-70) | 用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。 | Benchmark |
| [Case 72: LLM 辩论基准第二名](#case-72) | 用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。 | Benchmark |
| [Case 76: AA-Omniscience 幻觉率](#case-76) | 用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。 | Evaluation |

### [💻 Coding Agent 与长上下文工作流](#coding-agents-long-context-workflows)

| Case | 展示重点 | 类型 |
|---|---|---|
| [One Hour Forty Two Minute Refactor Loop](#case-13) | Use this case as a pattern for long autonomous front-end refactoring with TDD, reviewer feedback, and regression checks. | Demo |
| [OpenCode Bug Fix And Implementation Test](#case-14) | Use this case to test GLM-5.2 as an OpenCode coding agent for bug fixes plus a small implementation task. | Demo |
| [OpenCode Retro Video Game Walkthrough](#case-15) | Use this walkthrough to build a small game with GLM-5.2 and OpenCode from a single prompt, then inspect how the model handles implementation details. | Tutorial |
| [HTML5 Physics Simulations Contest](#case-16) | Use this case to compare GLM-5.2 and Kimi K2.7 Code on self-contained HTML5 physics simulations without libraries. | Evaluation |
| [Personal Site UI UX Build](#case-17) | Use this case to prompt GLM-5.2 for a polished personal site and inspect how far multiple turns can improve UI/UX. | Demo |
| [AI Contract Review Product Build](#case-18) | Use this case to evaluate GLM-5.2 on a product-building task with a PRD, time budget, step count, usage quota, and code-quality comparison. | Evaluation |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | Use this case to understand how GLM-5.2 is integrated into ZCode 3.0 for larger agentic development tasks. | Integration |
| [Linux Wrapper For ZCode Built With GLM-5.2](#case-20) | Use this case as an example of GLM-5.2 assisting with tooling around coding-agent environments. | Demo |
| [Computer Use Skill Packaging](#case-21) | Use this case to study GLM-5.2 as a helper for turning an open-source computer-use repo into a reusable skill. | Demo |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | Use this case to evaluate GLM-5.2 inside a full agentic development environment rather than a single chat session. | Demo |
| [Case 62: OpenCode Harness With Local Serving](#case-62) | Use this case to test GLM-5.2 with the OpenCode harness, local serving, and tool-heavy coding workflows before comparing it with Claude Opus. | Evaluation |
| [Case 65: Fast-RLM Long-Context Instruction Injection](#case-65) | Use this case to improve GLM-5.2 long-context counting and REPL-agent behavior by moving instructions into the RLM system prompt. | Integration |
| [Case 66: DeepAgents Code Open Harness Trial](#case-66) | Use this case to try GLM-5.2 with an open coding-agent harness and compare the model under a reproducible agent shell. | Demo |
| [Case 77: 生产级营销 Agent 栈路由策略](#case-77) | 用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。 | Evaluation |
| [Case 80: M3 Ultra Pokemon Red Goal Run](#case-80) | 用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。 | Demo |

### [🎮 上手 Demo 与 Showcase](#hands-on-demos-showcase-builds)

| Case | 展示重点 | 类型 |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | Use this case to compare same-prompt game-building output, runtime, and cost between GLM-5.2 and Opus 4.8. | Demo |
| [Three Real Builds With Mixed Results](#case-24) | Use this case as a cautionary demo set: test multiple real builds before trusting a model for production game or video tasks. | Evaluation |
| [Super Mario Clone In ZCode](#case-25) | Use this case to evaluate iterative game-building with GLM-5.2 and ZCode over several fix-and-feature passes. | Demo |
| [Lunar Lander Contest](#case-26) | Use this case to compare GLM-5.2, MiniMax M3, and Kimi K2.7 Code on an interactive game-style task. | Evaluation |
| [One-Prompt Design Arena Creation](#case-27) | Use this case to inspect what GLM-5.2 can generate from a single design prompt in an arena context. | Demo |
| [Research Paper Understanding Workflow](#case-28) | Use this case to apply GLM-5.2 to paper-reading workflows with contextual questions and cross-paper references. | Integration |
| [Constrained Poem Comparison](#case-29) | Use this case to separate correctness from creative quality when comparing GLM-5.2 with Fable-style models. | Evaluation |
| [Design Sense Example](#case-30) | Use this case as a lightweight visual-design signal, then verify with your own prompt and UI review. | Demo |
| [Case 71: Temple Run 体素游戏单次生成](#case-71) | 用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。 | Demo |
| [Case 78: OpenCode Go 单次生成案例集](#case-78) | 用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。 | Demo |
| [Case 81: Space Invaders One-Prompt Build](#case-81) | 用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。 | Demo |
| [Case 82: OpenCode Recovery Lab One-Shot](#case-82) | 用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。 | Demo |

### [🔌 供应商与工具集成](#provider-tool-integrations)

| Case | 展示重点 | 类型 |
|---|---|---|
| [OpenCode Go Availability](#case-31) | Use this case to track GLM-5.2 availability inside OpenCode Go workflows with text, 1M context, and GLM-5.1-like pricing. | Integration |
| [Ollama Cloud Availability](#case-32) | Use this case to route GLM-5.2 into Ollama Cloud for accessible open-source coding-model experiments. | Integration |
| [OpenRouter One API Call Access](#case-33) | Use this case to access GLM-5.2 through OpenRouter when comparing provider routing or multi-model stacks. | Integration |
| [vLLM Day-Zero Support](#case-34) | Use this case to self-host or serve GLM-5.2 through vLLM with day-zero support. | Integration |
| [Notion Availability Via Baseten](#case-35) | Use this case to identify GLM-5.2 as an open-weight model available inside Notion workflows. | Integration |
| [Fireworks Day-Zero Serving](#case-36) | Use this case to evaluate Fireworks as a serving route for GLM-5.2 workloads that need hosted infrastructure. | Integration |
| [Google Cloud Model Garden Link](#case-37) | Use this case to find GLM-5.2 in Google Cloud-oriented deployment and agent-platform contexts. | Integration |
| [Venice Privacy Mode](#case-38) | Use this case when privacy mode, TEE, or end-to-end encryption is a deciding factor in trying GLM-5.2. | Integration |
| [Command Code Availability](#case-39) | Use this case to try GLM-5.2 in Command Code with a low-cost entry plan and long-context coding features. | Integration |
| [Hermes Agent From Nous Portal](#case-40) | Use this case to connect GLM-5.2 into Hermes Agent workflows through Nous Portal and OpenRouter. | Integration |
| [io.net Day-Zero Launch Partner](#case-41) | Use this case when evaluating compute-backed serving for a 753B-parameter long-context model. | Integration |
| [Modular Cloud Day-Zero Serving](#case-42) | Use this case to consider Modular Cloud for long-context GLM-5.2 serving at provider scale. | Integration |
| [Case 61: Cursor Setup Through OpenRouter](#case-61) | Use this case to configure GLM-5.2 in Cursor through OpenRouter for a low-cost open-model coding workflow. | Tutorial |
| [Case 63: Amp Agentic Eyes For Visual Design](#case-63) | Use this case to pair GLM-5.2 with Amp custom agents when a text-only model needs visual-review support for design tasks. | Integration |
| [Case 69: Baseten Faster One-Million-Context Serving](#case-69) | Use this case to route GLM-5.2 through Baseten when long-context serving speed matters for Factory Droid, OpenCode, and coding harnesses. | Integration |
| [Case 74: 面向网页设计的 Browser Use QA 子代理](#case-74) | 当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。 | Integration |
| [Case 79: ZCode 官方 IDE 每日免费额度](#case-79) | 当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。 | Tutorial |
| [Case 83: Cursor Setup Through Fireworks](#case-83) | 用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。 | Tutorial |
| [Case 84: VulcanBench ZAI Provider Support](#case-84) | 用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。 | Integration |
| [Case 85: OpenCode High/Max Reasoning Variants](#case-85) | 用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。 | Integration |
| [Case 86: Z.ai Coding Endpoint Selection](#case-86) | 用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。 | Tutorial |
| [Case 87: ZenMux Free GLM-5.2 API Setup](#case-87) | 用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。 | Tutorial |

### [💸 成本、定价与本地部署](#cost-pricing-local-deployment)

| Case | 展示重点 | 类型 |
|---|---|---|
| [Output Token Cost Comparison](#case-43) | Use this case to compare GLM-5.2 output-token economics against Opus, Fable, and GPT-5.5-style models. | Evaluation |
| [Local Near-Frontier Hardware ROI](#case-44) | Use this case to reason about whether self-hosting GLM-5.2-like models can repay hardware costs for heavy agent users. | Evaluation |
| [MLX On Two Mac Studios](#case-45) | Use this case to explore local GLM-5.2 runs on Apple hardware and MLX-oriented setups. | Demo |
| [H100 Monthly Local Deployment Claim](#case-46) | Use this case as a cost-comparison prompt for checking local deployment assumptions before choosing between subscription and self-hosting. | Evaluation |
| [Daily Credits And Claude Replacement Claim](#case-47) | Use this case to inspect the free-credit and replacement-agent narrative around GLM-5.2, while separating marketing claims from verified workload fit. | Evaluation |
| [Free ZCode Token Window](#case-48) | Use this case to test GLM-5.2 through a free ZCode allowance before committing to a paid provider or local deployment. | Integration |
| [ZenMux Free Week Offer](#case-49) | Use this case to find time-boxed free-access windows for GLM-5.2 testing. | Integration |
| [crofAI Per-Token Pricing](#case-50) | Use this case to compare third-party provider pricing for GLM-5.2 before selecting a route. | Integration |
| [API Price Margin Comparison](#case-51) | Use this case as a market-pricing critique when comparing GLM-5.2 to other frontier labs and open models. | Evaluation |
| [Case 64: Basement Local Inference Speed](#case-64) | Use this case to estimate local GLM-5.2 inference throughput on large-memory Apple hardware before planning an offline coding setup. | Demo |
| [Case 68: Unsloth Quantized Local Deployment](#case-68) | Use this case to evaluate quantized GLM-5.2 deployment paths when full model weights are too large for ordinary local hardware. | Tutorial |
| [Case 88: Two M3 Ultra MLX Distributed Run](#case-88) | 用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。 | Demo |
| [Case 89: ZCode Multiplier Cut Through September](#case-89) | 用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。 | Integration |

### [🧭 限制、Caveat 与安全信号](#limits-caveats-safety-signals)

| Case | 展示重点 | 类型 |
|---|---|---|
| [No Vision Caveat](#case-52) | Use this case to remember that GLM-5.2 may be less useful for workflows requiring native vision capability. | Limit |
| [Real-World Agent Gap Caveat](#case-53) | Use this case to avoid over-reading benchmark wins as proof that GLM-5.2 matches the best proprietary models on all deployed agentic tasks. | Limit |
| [Safety Guardrail Concern](#case-54) | Use this case as a reminder to run safety evaluations before deploying GLM-5.2 in sensitive domains. | Limit |
| [Benchmark Methodology Critique](#case-55) | Use this case to question benchmark methodology even when the headline result favors GLM-5.2. | Limit |
| [Peak-Time Latency Concern](#case-56) | Use this case to test provider latency before switching coding plans or routing Claude Code-style workflows to GLM-5.2. | Limit |
| [FutureSim Non-Improvement Result](#case-57) | Use this case to check whether coding gains generalize to non-coding domains before broad deployment. | Limit |
| [Launch Readiness Critique](#case-58) | Use this case to separate model capability from launch execution, documentation, and API readiness. | Limit |
| [Coding Plan Price Increase](#case-59) | Use this case to verify plan pricing before recommending GLM-5.2 as a low-cost replacement. | Limit |
| [Case 67: Short Parallel Work Versus Long Agent Runs](#case-67) | Use this case to route GLM-5.2 toward short bounded coding tasks while reserving stronger models for deeper multi-hour agent runs. | Limit |
| [Case 73: 代码审查与偏见检查](#case-73) | 用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。 | Limit |
| [Case 75: 高难推理计费异常](#case-75) | 用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。 | Limit |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 Benchmark 与前沿评测

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use the Artificial Analysis post to compare GLM-5.2 against other open-weight and proprietary frontier models on intelligence and cost per task.**

Artificial Analysis reported GLM-5.2 as the leading open-weights model on its Intelligence Index, with a score of 51 and a Pareto-frontier position on intelligence versus cost per task. The post also records model size, context window, pricing, and provider availability.

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (by [@arena](https://x.com/arena))

**Use this case to evaluate GLM-5.2 on real front-end coding tasks judged by arena-style comparisons.**

The Arena account reported GLM-5.2 Max ranking second in Code Arena Frontend, ahead of other open models and close to the top frontier entry. The post is especially useful for front-end, React, HTML, gaming, simulation, and reference-based design use cases.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (by [@Designarena](https://x.com/Designarena))

**Use this case to judge whether GLM-5.2 can handle design-plus-code tasks rather than only text-heavy coding benchmarks.**

Design Arena reported GLM-5.2 reaching first place with an Elo score of 1360, highlighting a jump in design-code performance for an open-weights model. Treat it as a design benchmark signal, not as a substitute for project-specific UI review.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Use the FrontierSWE post to compare GLM-5.2 against GPT-5.5, Opus, and Fable-style models on software-engineering tasks.**

The post reports GLM-5.2 ranking third on FrontierSWE and frames it as one of the first open-weight models to narrow the gap with top proprietary models on implementation-heavy engineering work.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (by [@AiBattle_](https://x.com/AiBattle_))

**Use the DeepSWE case to understand GLM-5.2 as a strong open model for difficult software-engineering evaluation tasks.**

AiBattle reported a 46.2% DeepSWE score for GLM-5.2 and described it as the highest score for an open-source model in that benchmark context.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (by [@cline](https://x.com/cline))

**Use this case when evaluating GLM-5.2 for terminal-oriented coding and agent workflows.**

Cline highlighted GLM-5.2 as the first open-weights model to cross 80% on Terminal-Bench and positioned it as a frontier-level option for accessible tool-based development.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer Comparison Against GPT-5.5](https://x.com/gosrum/status/2067153091842203676) (by [@gosrum](https://x.com/gosrum))

**Use this SWELancer case as a concrete multi-metric comparison between GLM-5.2 and GPT-5.5 on task success, reward, and completion time.**

The author shared a Japanese benchmark update where GLM-5.2 unexpectedly led GPT-5.5 on the latest SWELancer results across task success, earned reward, and time to complete, with two inaccessible tasks excluded.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (by [@bridgemindai](https://x.com/bridgemindai))

**Use this case to inspect GLM-5.2 on grounded multi-step reasoning rather than only coding leaderboards.**

BridgeMind reported GLM-5.2 as the first model to receive a perfect score on the BridgeBench BS benchmark, making it a useful source for reasoning-heavy evaluation claims.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (by [@bridgebench](https://x.com/bridgebench))

**Use this case to compare GLM-5.2 with closed frontier models on grounded reasoning tasks.**

BridgeBench reported GLM-5.2 taking the number one spot on a reasoning benchmark and beating Claude Fable 5 in that measurement context.

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (by [@elliotarledge](https://x.com/elliotarledge))

**Use this case when checking whether benchmark gains come from valid implementation behavior instead of shortcutting.**

The KernelBench-Hard post says the interesting result was not just score, but that GLM-5.2 stopped using an inappropriate shortcut on an fp8 GEMM problem, making it relevant for benchmark integrity.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (by [@maxbittker](https://x.com/maxbittker))

**Use this case as a fast signal for open-weight model progress on game-like benchmark tasks.**

The post reports GLM-5.2 scoring better than recent proprietary models on Runescape bench, using that result to frame how quickly open-source frontier capability is catching up.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (by [@bridgebench](https://x.com/bridgebench))

**Use this case to evaluate latency-sensitive workflows where speed matters alongside intelligence.**

BridgeBench reported GLM-5.2 as three times faster than GLM-5.1 and fourth on its speed benchmark, making it relevant for workflows where iteration speed affects usability.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench Hard And Mega GPU Coding](https://x.com/elliotarledge/status/2068177175640240323) (作者 [@elliotarledge](https://x.com/elliotarledge))

**Use this case to evaluate GLM-5.2 on GPU-kernel coding across KernelBench-Hard and KernelBench-Mega, where open agent traces make the result inspectable.**

The KernelBench update reports H100, B200, and RTX PRO 6000 tests, open-sourced agent traces, and GLM-5.2 as the top open model in the comparison.

类型: Benchmark | 日期: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE 高强度模式开源领先](https://x.com/datacurve/status/2068473057107476680) (作者 [@datacurve](https://x.com/datacurve))

**用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。**

DataCurve 分享的 DeepSWE 榜单更新显示，GLM-5.2 在开源模型中达到 44% pass@1，并领先 Kimi K2.7 Code 17 个点。应将其视为一次 benchmark 更新，而不是所有真实世界 agent 工作流都已被解决的证明。

类型: Benchmark | 日期: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM 辩论基准第二名](https://x.com/LechMazur/status/2068428300460974279) (作者 [@LechMazur](https://x.com/LechMazur))

**用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。**

Lech Mazur 分享了一项 LLM Debate Benchmark 结果，其中 GLM-5.2 Max 排名第二。这个基准衡量的是跨广泛主题的对抗式多轮辩论能力，因此它提供的是编码榜单之外的推理信号。

类型: Benchmark | 日期: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience 幻觉率](https://x.com/yuhasbeentaken/status/2068259921519423855) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。**

帖子报告 GLM-5.2 在 AA-Omniscience 上的幻觉率为 28%，低于 Fable 5 和 DeepSeek V4 Pro 的对应结果。这个基准关注的是模型在不确定时是否会拒答或承认不确定，而不是继续猜测。

类型: Evaluation | 日期: 2026-06-20

---


<a id="coding-agents-long-context-workflows"></a>
## 💻 Coding Agent 与长上下文工作流

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (by [@KELMAND1](https://x.com/KELMAND1))

**Use this case as a pattern for long autonomous front-end refactoring with TDD, reviewer feedback, and regression checks.**

The post describes a 1 hour 42 minute GLM-5.2 refactor task with 88 model turns and 102 tool calls. The workflow included a handoff, four blocker fixes, TDD implementation of 12 tests, two rounds of P2 fixes, and final regression.

Type: Demo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (by [@altudev](https://x.com/altudev))

**Use this case to test GLM-5.2 as an OpenCode coding agent for bug fixes plus a small implementation task.**

The author reports testing GLM-5.2 with six bug fixes and one implementation in OpenCode, saying the changes went through cleanly with solid planning and better speed than GLM-5.1.

Type: Demo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (by [@AskVenice](https://x.com/AskVenice))

**Use this walkthrough to build a small game with GLM-5.2 and OpenCode from a single prompt, then inspect how the model handles implementation details.**

Venice shared a full walkthrough for building a retro video game with GLM-5.2 and OpenCode, positioning it as a private, open-source, long-horizon coding workflow.

Type: Tutorial | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Use this case to compare GLM-5.2 and Kimi K2.7 Code on self-contained HTML5 physics simulations without libraries.**

Atomic Chat reported asking both models to build pool break, spring block, and Galton board simulations. Their post says GLM-5.2 handled all three with more detail and polish, while Kimi struggled with physical behavior.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (by [@anshuc](https://x.com/anshuc))

**Use this case to prompt GLM-5.2 for a polished personal site and inspect how far multiple turns can improve UI/UX.**

The author says GLM-5.2 produced a creative personal site after being pushed with the right prompting, and shared a video of the result. It is useful for front-end design iteration rather than single-shot benchmark claims.

Type: Demo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (by [@laozhang2579](https://x.com/laozhang2579))

**Use this case to evaluate GLM-5.2 on a product-building task with a PRD, time budget, step count, usage quota, and code-quality comparison.**

The Chinese post compares GLM-5.2, Kimi K2.7, and Claude Opus 4.8 on an AI contract-review product PRD. It reports build duration, step count, five-hour quota usage, and code-quality scoring.

Type: Evaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (by [@zcode_ai](https://x.com/zcode_ai))

**Use this case to understand how GLM-5.2 is integrated into ZCode 3.0 for larger agentic development tasks.**

ZCode announced GLM-5.2 availability for Coding Plan users, stronger agent task execution, better long-context coding, and a Goal feature for managing larger objectives from planning to completion.

Type: Integration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [Linux Wrapper For ZCode Built With GLM-5.2](https://x.com/gosrum/status/2066484949755269510) (by [@gosrum](https://x.com/gosrum))

**Use this case as an example of GLM-5.2 assisting with tooling around coding-agent environments.**

The author reports completing zcode-linux using GLM-5.2 and Claude Code so Linux users can run ZCode in a Linux environment and add arbitrary API endpoints, including local LLM endpoints.

Type: Demo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (by [@0xSero](https://x.com/0xSero))

**Use this case to study GLM-5.2 as a helper for turning an open-source computer-use repo into a reusable skill.**

The post says GLM-5.2 was setting up computer use, found an advanced open-source repository, and converted it into a skill. It is a hands-on signal for tool-wrapping and agent integration work.

Type: Demo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (by [@laogui](https://x.com/laogui))

**Use this case to evaluate GLM-5.2 inside a full agentic development environment rather than a single chat session.**

The Chinese review says ZCode 3.0 was rewritten from shell-like earlier versions into a self-developed agent core paired with GLM-5.2, with a better experience among domestic agentic development environments.

Type: Demo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [OpenCode Harness With Local Serving](https://x.com/PatrickToulme/status/2068134212587184442) (作者 [@PatrickToulme](https://x.com/PatrickToulme))

**Use this case to test GLM-5.2 with the OpenCode harness, local serving, and tool-heavy coding workflows before comparing it with Claude Opus.**

The author reports a local deployment, nested subagents, research/planning behavior, and a working application build.

类型: Evaluation | 日期: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (作者 [@neural_avb](https://x.com/neural_avb))

**Use this case to improve GLM-5.2 long-context counting and REPL-agent behavior by moving instructions into the RLM system prompt.**

The release notes describe a concrete agent-scaffolding change and a GLM-5.2 long-context benchmark effect.

类型: Integration | 日期: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (作者 [@sydneyrunkle](https://x.com/sydneyrunkle))

**Use this case to try GLM-5.2 with an open coding-agent harness and compare the model under a reproducible agent shell.**

The author reports using GLM-5.2 with DeepAgents Code and frames open model plus open harness as the testing pattern.

类型: Demo | 日期: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [生产级营销 Agent 栈路由策略](https://x.com/DeRonin_/status/2068303752671477820) (作者 [@DeRonin_](https://x.com/DeRonin_))

**用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。**

作者在一个代理机构栈里做了 6 天并行对比后表示，GLM-5.2 在开始漂移前可稳定执行 60 多个 agent 步骤，连续 800 多次匹配结构化格式，并提供低延迟的自托管响应。同一条帖子仍然更偏好用 Opus 处理语音关键或高歧义任务，因此真正有价值的是这条路由规则本身。

类型: Evaluation | 日期: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。**

作者把 Claude Code 的模型切到本地 GLM 5.2，在一台 M3 Ultra 512GB 机器上跑了 12 小时的 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 任务。帖文公开了运行时长、token 消耗、代码 churn、RAM 使用量以及 GGUF 和 KV-cache 配置，并指出模型质量感觉接近 frontier，但本地推理速度仍是主要瓶颈。

Type: Demo | Date: 2026-06-21

---


<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手 Demo 与 Showcase

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (by [@aimlapi](https://x.com/aimlapi))

**Use this case to compare same-prompt game-building output, runtime, and cost between GLM-5.2 and Opus 4.8.**

AI/ML API reported asking GLM-5.2 and Opus 4.8 to one-shot a playable Backrooms game. Their post says GLM-5.2 built fuller mechanics in 1:08 at $0.37, while Opus took 2:14 at $1.94.

Type: Demo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [Three Real Builds With Mixed Results](https://x.com/bridgemindai/status/2065840871929442319) (by [@bridgemindai](https://x.com/bridgemindai))

**Use this case as a cautionary demo set: test multiple real builds before trusting a model for production game or video tasks.**

BridgeMind tested GLM-5.2 on a horror house game, a 3D stealth game, and a Remotion marketing video. The post reports mixed results, including broken game logic, making it useful as a grounded limitation signal.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use this case to evaluate iterative game-building with GLM-5.2 and ZCode over several fix-and-feature passes.**

The author tested ZCode 3.0 with GLM-5.2 by creating a Super Mario-style clone, then shared the result after five iterations of issue fixes and feature additions.

Type: Demo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Use this case to compare GLM-5.2, MiniMax M3, and Kimi K2.7 Code on an interactive game-style task.**

The post describes a Lunar Lander contest among MiniMax M3, GLM-5.2, and Kimi K2.7 Code, using a video result as a practical benchmark before returning to local-model development.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (by [@grx_xce](https://x.com/grx_xce))

**Use this case to inspect what GLM-5.2 can generate from a single design prompt in an arena context.**

The author shared an example of a GLM-5.2 creation on Design Arena made from one prompt, using it to show the narrowing gap between open and closed-weight models.

Type: Demo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [Research Paper Understanding Workflow](https://x.com/askalphaxiv/status/2066996976445706745) (by [@askalphaxiv](https://x.com/askalphaxiv))

**Use this case to apply GLM-5.2 to paper-reading workflows with contextual questions and cross-paper references.**

AlphaXiv introduced GLM-5.2 for understanding research papers, where users highlight a section, ask questions, and reference other papers for context, comparisons, and benchmark references.

Type: Integration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (by [@emollick](https://x.com/emollick))

**Use this case to separate correctness from creative quality when comparing GLM-5.2 with Fable-style models.**

Ethan Mollick credited GLM-5.2 Max for producing a correct constrained poem, while noting that Fable incorporated the disappearing-letter constraint into the poem theme more creatively.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (by [@0xSero](https://x.com/0xSero))

**Use this case as a lightweight visual-design signal, then verify with your own prompt and UI review.**

The author says they enjoyed GLM-5.2's design sense and shared a visual example. It is useful as a pointer to inspect, not as standalone proof of production design quality.

Type: Demo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 体素游戏单次生成](https://x.com/pseudokid/status/2068431546143649829) (作者 [@pseudokid](https://x.com/pseudokid))

**用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。**

作者表示，首轮提示就生成出了大部分 Temple Run 风格的体素摩托游戏，之后只用少量补充轮次修正镜头和移动逻辑。帖子还提到 Z.ai 工具链可以生成截图和实机视频，帮助文本模型评估结果。

类型: Demo | 日期: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 单次生成案例集](https://x.com/LyalinDotCom/status/2068378281636982990) (作者 [@LyalinDotCom](https://x.com/LyalinDotCom))

**用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。**

作者展示了一组通过 OpenCode Go 完成的单次生成案例，包括太阳系 Web 应用、系统信息 Electron 应用，以及一个简单的探索小岛 Web 游戏。同一条帖子也表示，GLM-5.2 是他用过最强的开源模型，但还没有把它称作与最前沿闭源模型完全同级。

类型: Demo | 日期: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。**

作者表示，GLM-5.2 用一个主提示词就生成了可玩的 Space Invaders 风格游戏，随后又用三轮后续提示完成 sprite 替换和 leaderboard 等小增强。这个公开结果更适合作为轻量游戏生成样例，而不是完整 benchmark。

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。**

作者在输入一份 4,000 字分析和 Agents SDK 仓库后，用 OpenCode 搭配 GLM-5.2 构建了一个完全可交互的 recovery lab。帖文给出了 176k token 的运行、一轮成型的结果，以及打磨前端到端约 3.50 美元的成本。

Type: Demo | Date: 2026-06-21

---


<a id="provider-tool-integrations"></a>
## 🔌 供应商与工具集成

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (by [@opencode](https://x.com/opencode))

**Use this case to track GLM-5.2 availability inside OpenCode Go workflows with text, 1M context, and GLM-5.1-like pricing.**

OpenCode announced GLM-5.2 availability in Go, highlighting text support, a 1M context window, and same pricing as 5.1.

Type: Integration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (by [@ollama](https://x.com/ollama))

**Use this case to route GLM-5.2 into Ollama Cloud for accessible open-source coding-model experiments.**

Ollama announced GLM-5.2 availability, describing it as a long-horizon coding and agentic-task model with 1M context.

Type: Integration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (by [@OpenRouter](https://x.com/OpenRouter))

**Use this case to access GLM-5.2 through OpenRouter when comparing provider routing or multi-model stacks.**

OpenRouter announced GLM-5.2 availability as a 1M-token long-horizon model, giving users a provider-neutral path to call it.

Type: Integration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (by [@vllm_project](https://x.com/vllm_project))

**Use this case to self-host or serve GLM-5.2 through vLLM with day-zero support.**

The vLLM project announced GLM-5.2 support in v0.23.0, framing it as a flagship model for long-horizon coding agents with 1M context.

Type: Integration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (by [@NotionHQ](https://x.com/NotionHQ))

**Use this case to identify GLM-5.2 as an open-weight model available inside Notion workflows.**

Notion announced GLM-5.2 availability as an open-weight model built for long-horizon tasks and served via Baseten.

Type: Integration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Use this case to evaluate Fireworks as a serving route for GLM-5.2 workloads that need hosted infrastructure.**

Fireworks announced GLM-5.2 live on day zero, emphasizing 1M context, coding-first positioning, and independent validation on SWE-Bench, Terminal-Bench, GPQA, and AIME.

Type: Integration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Google Cloud Model Garden Link](https://x.com/CarolGLMs/status/2067127223216419088) (by [@CarolGLMs](https://x.com/CarolGLMs))

**Use this case to find GLM-5.2 in Google Cloud-oriented deployment and agent-platform contexts.**

CarolGLMs shared a Google Cloud link for GLM-5.2, making it a direct pointer for teams working through cloud model catalogs.

Type: Integration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (by [@AskVenice](https://x.com/AskVenice))

**Use this case when privacy mode, TEE, or end-to-end encryption is a deciding factor in trying GLM-5.2.**

Venice announced GLM-5.2 availability in privacy mode with TEE/E2EE framing, aimed at private agentic coding and long-horizon tasks.

Type: Integration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Use this case to try GLM-5.2 in Command Code with a low-cost entry plan and long-context coding features.**

Command Code announced GLM-5.2 availability, noting 1M context, strong reasoning, open-source status, and access through its one-dollar Go plan.

Type: Integration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Hermes Agent From Nous Portal](https://x.com/Teknium/status/2066954081575592282) (by [@Teknium](https://x.com/Teknium))

**Use this case to connect GLM-5.2 into Hermes Agent workflows through Nous Portal and OpenRouter.**

Teknium reported GLM-5.2 availability in Hermes Agent from Nous Portal and OpenRouter, useful for agent-framework routing experiments.

Type: Integration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (by [@ionet](https://x.com/ionet))

**Use this case when evaluating compute-backed serving for a 753B-parameter long-context model.**

io.net announced itself as a day-zero launch partner for GLM-5.2, emphasizing 1M context, agentic-first design, long-horizon coding, and the compute needs of a 753B-parameter model.

Type: Integration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (by [@clattner_llvm](https://x.com/clattner_llvm))

**Use this case to consider Modular Cloud for long-context GLM-5.2 serving at provider scale.**

Chris Lattner posted that GLM-5.2 was live on Modular Cloud on day zero, highlighting open weights, coding, long-horizon agents, and 1M context.

Type: Integration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (作者 [@agentnative_](https://x.com/agentnative_))

**Use this case to configure GLM-5.2 in Cursor through OpenRouter for a low-cost open-model coding workflow.**

The source gives a concrete Cursor/OpenRouter setup path rather than only announcing model availability.

类型: Tutorial | 日期: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (作者 [@beyang](https://x.com/beyang))

**Use this case to pair GLM-5.2 with Amp custom agents when a text-only model needs visual-review support for design tasks.**

The post connects a GLM-5.2 visual design benchmark result with Amp plugin agents that can provide a review layer.

类型: Integration | 日期: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (作者 [@alphatozeta8148](https://x.com/alphatozeta8148))

**Use this case to route GLM-5.2 through Baseten when long-context serving speed matters for Factory Droid, OpenCode, and coding harnesses.**

The source reports GLM-5.2 running four times faster at full 1M context and shows it in coding harnesses.

类型: Integration | 日期: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [面向网页设计的 Browser Use QA 子代理](https://x.com/browser_use/status/2068405699340853541) (作者 [@browser_use](https://x.com/browser_use))

**当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。**

Browser Use 表示，GLM-5.2 在一个网站设计任务中超过了 Fable 5，随后又加入 QA 子代理来检查结果、判断美感、查找 bug，并把定向修复建议回传给 GLM。整套 build 加 QA 的循环据称成本低于 0.75 美元。

类型: Integration | 日期: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 官方 IDE 每日免费额度](https://x.com/Alan_Earn/status/2068223665268006924) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。**

帖子将 ZCode 描述为智谱官方编码 IDE，默认模型就是 GLM-5.2，并提供每日 300 万 token、100 万上下文窗口，以及 Mac 和 Windows 客户端。它还包含一段简短的上手流程，因此比普通的上线公告更具可操作性。

类型: Tutorial | 日期: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。**

Skirano 展示了最简 Cursor 配置流程：把 Fireworks key 填到 OpenAI API key 字段，base URL 用 `https://api.fireworks.ai/inference/v1`，模型选择 `accounts/fireworks/models/glm-5p2`，然后重启 Cursor。对于想在熟悉的 coding IDE 里试用 GLM-5.2 的人，这是一条很具体的接入路径。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。**

VulcanBench v0.2.0 新增了一等公民级别的 ZAI 支持，让用户可以把 GLM-5.2 作为 `zai:glm-5.2` 与 OpenAI、Anthropic 模型并排运行，并配有独立的 `ZAI_API_KEY`。如果你要的是开放、可重复的 benchmark harness，而不是单张截图，这个案例更有用。

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。**

OpenCode v1.17.9 为 GLM-5.2 新增了 High 和 Max thinking 变体，覆盖 OpenAI 兼容与 Anthropic 兼容 provider，并原生支持 OpenRouter 的 effort 映射。同一版本也修复了 agent step-limit 行为，让这个集成更适合更长的运行。

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。**

帖文建议，对于 coding plan 工作负载，应优先使用 `https://api.z.ai/api/coding/paas/v4`，而不是通用的 `https://api.z.ai/api/paas/v4/`。作者还补充说，Claude Code、OpenCode 等工具在支持时通常会走 `https://api.z.ai/api/anthropic`。如果你感觉 GLM-5.2 路由不对，这是一条很具体的配置修正。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。**

作者分享了一条大约五分钟的配置流程：获取免费的 ZenMux API key 与 base URL，然后把 GLM-5.2 接到 Claude、Cursor、Hermes 等工具上。帖文也提醒免费 tier 很快会触发 rate limit，所以它更适合作为 access note，而不是长期稳定性保证。

Type: Tutorial | Date: 2026-06-21

---


<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定价与本地部署

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (by [@Hesamation](https://x.com/Hesamation))

**Use this case to compare GLM-5.2 output-token economics against Opus, Fable, and GPT-5.5-style models.**

The post compares 1M output token prices and argues that GLM-5.2 can be meaningfully cheaper than frontier closed models. Treat the numbers as a source-linked pricing comparison that should be rechecked before budgeting.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (by [@Jeyffre](https://x.com/Jeyffre))

**Use this case to reason about whether self-hosting GLM-5.2-like models can repay hardware costs for heavy agent users.**

The author estimates that multiple DGX Spark-class machines could run a 700B-class model and compares a roughly $20K hardware purchase against high monthly API spending for coding and agent workloads.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (by [@pcuenq](https://x.com/pcuenq))

**Use this case to explore local GLM-5.2 runs on Apple hardware and MLX-oriented setups.**

The post says GLM-5.2 had just been released and was already running with MLX on two Mac Studio M3 Ultra machines, framing it as comparable to recent closed models with open weights.

Type: Demo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (by [@ai_xiaomu](https://x.com/ai_xiaomu))

**Use this case as a cost-comparison prompt for checking local deployment assumptions before choosing between subscription and self-hosting.**

The Chinese post compares claimed SWE-Bench numbers, commercial open-source use, and an estimated single-H100 local deployment cost against a Claude Pro subscription. The numbers should be revalidated for current infrastructure pricing.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Use this case to inspect the free-credit and replacement-agent narrative around GLM-5.2, while separating marketing claims from verified workload fit.**

The post frames GLM-5.2 as a lower-cost Claude competitor with daily credits, open-source control, self-hosting, and stronger value for long coding sessions.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (by [@0xSero](https://x.com/0xSero))

**Use this case to test GLM-5.2 through a free ZCode allowance before committing to a paid provider or local deployment.**

The author describes GLM-5.2 availability through ZCode with a large free daily token allowance and notes possible use for setting up vLLM Studio or local hosting.

Type: Integration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (by [@JZiyue_](https://x.com/JZiyue_))

**Use this case to find time-boxed free-access windows for GLM-5.2 testing.**

The post advertises GLM-5.2 live on ZenMux with a one-week free window, 1M context, coding and agentic improvements, and same-price-as-5.1 positioning.

Type: Integration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAI Per-Token Pricing](https://x.com/nahcrof/status/2067166596523765781) (by [@nahcrof](https://x.com/nahcrof))

**Use this case to compare third-party provider pricing for GLM-5.2 before selecting a route.**

The post announces GLM-5.2 on crofAI with listed input, output, and cache prices, positioning it as cheap frontier intelligence.

Type: Integration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (by [@scaling01](https://x.com/scaling01))

**Use this case as a market-pricing critique when comparing GLM-5.2 to other frontier labs and open models.**

The author compares GLM-5.2 and other large open models on output-token pricing and uses the comparison to argue that some frontier-lab API margins are high.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://x.com/volatilemrkts/status/2068077319986516031) (作者 [@volatilemrkts](https://x.com/volatilemrkts))

**Use this case to estimate local GLM-5.2 inference throughput on large-memory Apple hardware before planning an offline coding setup.**

The source reports 44.1 tokens per second on a local high-memory Mac setup and mentions decode-repeat issues with heavy tool calls.

类型: Demo | 日期: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (作者 [@mrblock](https://x.com/mrblock))

**Use this case to evaluate quantized GLM-5.2 deployment paths when full model weights are too large for ordinary local hardware.**

The post describes Unsloth dynamic 2-bit and 1-bit GGUF options, memory reductions, and llama.cpp or Unsloth Studio deployment routes.

类型: Tutorial | 日期: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。**

帖文展示了 GLM-5.2 8-bit 在两台 M3 Ultra 512GB 机器上通过 MLX distributed 运行的情况，速度约 17.9 tokens/sec，总内存占用约 760GB。作者也明确说明这仍是一个进行中的 PR，因此它更适合作为 deployment signal，而不是完整部署指南。

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。**

这条帖文表示，ZCode 已把 GLM coding plan multiplier 在高峰时段从 3x 下调到 2x，在非高峰时段从 2x 下调到 0.67x，而且新窗口会持续到 9 月底。对于想在 GLM-5.2 上尽量拉长 credits 的人来说，这是一个非常具体的 access / pricing note。

Type: Integration | Date: 2026-06-21

---


<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、Caveat 与安全信号

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (by [@sawyerhood](https://x.com/sawyerhood))

**Use this case to remember that GLM-5.2 may be less useful for workflows requiring native vision capability.**

The author notes that GLM models lacking vision reduces usefulness, quoting a Design Arena ranking post. This is a practical caveat for multimodal product planning.

Type: Limit | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [Real-World Agent Gap Caveat](https://x.com/ml_angelopoulos/status/2067013545431269405) (by [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**Use this case to avoid over-reading benchmark wins as proof that GLM-5.2 matches the best proprietary models on all deployed agentic tasks.**

The author says GLM-5.2 is impressive but not yet close to Fable-level or Opus 4.8 thinking-level performance on the general distribution of real-world agentic tasks, based on an Agent Arena methodology.

Type: Limit | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (by [@VittoStack](https://x.com/VittoStack))

**Use this case as a reminder to run safety evaluations before deploying GLM-5.2 in sensitive domains.**

The post reports a harmful-content refusal failure in a comparative safety test. The repository records only the safety signal, not the unsafe details, and treats this as a deployment-risk caveat.

Type: Limit | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [Benchmark Methodology Critique](https://x.com/josepha_mayo/status/2066951013337112661) (by [@josepha_mayo](https://x.com/josepha_mayo))

**Use this case to question benchmark methodology even when the headline result favors GLM-5.2.**

The author criticizes Design Arena methodology while still acknowledging GLM-5.2 as strong, making it useful for readers who want benchmark skepticism alongside leaderboard claims.

Type: Limit | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (by [@k_matsumaru](https://x.com/k_matsumaru))

**Use this case to test provider latency before switching coding plans or routing Claude Code-style workflows to GLM-5.2.**

The Japanese post considers using GLM-5.2 inside a coding plan but notes prior concern about peak-time response latency.

Type: Limit | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**Use this case to check whether coding gains generalize to non-coding domains before broad deployment.**

The post reports GLM-5.2 as no better than GLM-5.1 on FutureSim and uses the result to caution that coding improvements may not generalize equally across all domains.

Type: Limit | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (by [@bridgemindai](https://x.com/bridgemindai))

**Use this case to separate model capability from launch execution, documentation, and API readiness.**

The post calls the early release messy because benchmarks and API access were not yet available at the time, making it relevant for launch-readiness review rather than model-quality judgment.

Type: Limit | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [Coding Plan Price Increase](https://x.com/bridgemindai/status/2065799843658793092) (by [@bridgemindai](https://x.com/bridgemindai))

**Use this case to verify plan pricing before recommending GLM-5.2 as a low-cost replacement.**

The author reports paying $65 per month for a GLM Coding Pro plan and says the plan had nearly doubled since their last subscription. Use it as a reminder to check current pricing.

Type: Limit | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [Short Parallel Work Versus Long Agent Runs](https://x.com/thekuchh/status/2068010332501479865) (作者 [@thekuchh](https://x.com/thekuchh))

**Use this case to route GLM-5.2 toward short bounded coding tasks while reserving stronger models for deeper multi-hour agent runs.**

The post reports a practical split: GLM-5.2 works well for short parallel tasks but drifted on a longer agent run.

类型: Limit | 日期: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [代码审查与偏见检查](https://x.com/wongmjane/status/2068424945663893936) (作者 [@wongmjane](https://x.com/wongmjane))

**用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。**

作者称，GLM-5.2 没有把中国政治审查内容注入到代码中；同时它还纠正了一个关于越南战争的错误“美国偏见”说法，而对偏意见解类问题保持不变。这使它成为测试政治敏感编码行为和事实性表现的一个具体公开案例。

类型: Limit | 日期: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高难推理计费异常](https://x.com/s_batzoglou/status/2068297051247350154) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。**

作者运行了 11 个归纳推理题，只报告 4 个完成、2 个答对、多小时级运行时间，以及明显高于可见 token 数的收费。这是关于推理效率和计费行为的具体警示，不只是 benchmark 分数问题。

类型: Limit | 日期: 2026-06-20

---


<a id="acknowledge"></a>
## 🙏 致谢

本仓库来自公开分享 GLM-5.2 使用证据的创作者、开发者、benchmark 团队、供应商和社区。

感谢这些高信号来源创作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)。

*我们无法保证每个案例都已归属到最初原创者。如果需要修正来源或署名，请联系我们，我们会更新。*

如果你有更多值得收录的 GLM-5.2 使用案例，欢迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
