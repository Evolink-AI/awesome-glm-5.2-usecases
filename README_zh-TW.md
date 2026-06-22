<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="GLM-5.2 高訊號使用案例倉庫 banner" width="760"></a>

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

# GLM-5.2 高訊號使用案例倉庫

## 🍌 介紹

歡迎來到 GLM-5.2 高訊號使用案例倉庫。

**我們從公開 demo 與創作者社群整理 GLM-5.2 的真實使用案例、教學、整合、評測、價格訊號與限制。**

這份繁體中文 README 聚焦有具體工作流、公開 benchmark 證據、實測 demo、整合方式、成本資訊或實務限制的案例。

每個案例標題都連回公開來源，作者 handle 會連到創作者個人頁。

[在 Evolink 上試用 GLM-5.2](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 總覽

- **89 個精選 GLM-5.2 案例**，來自公開創作者、評測團隊、工具開發者、服務商與一線使用者。
- Covers Benchmark 與前沿評測, Coding Agent 與長上下文工作流, 上手 Demo 與 Showcase, 供應商與工具整合, 成本、定價與本地部署, 限制、Caveat 與安全訊號.
- Each case includes the original source, creator attribution, concise usage takeaway, evidence type, and publication date.
- 你可以用這個 repo 尋找實用工作流、比較優勢與限制、探索供應商路徑，並追蹤真實上手實驗。

> [!NOTE]
> 本倉庫重視具體證據，而不是 hype：已發布 demo、benchmark 方法、整合筆記、成本資料與明確 caveat。

> [!NOTE]
> 多語 README 會保持與英文源相同的案例順序、連結、anchor 與署名；為了可追溯性，部分標題會保留接近原文的寫法。

<a id="-quick-api-access"></a>
## ⚡ 快速 API 接入

透過 Evolink 的 OpenAI 相容 Chat Completions API 使用 GLM-5.2。先在 [Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases) 取得 API key，然後在執行請求前設定為 `EVOLINK_API_KEY`。

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

閱讀完整 GLM-5.2 API 參考：[開啟 GLM-5.2 API docs](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api).

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [📏 Benchmark 與前沿評測](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76 |
| [💻 Coding Agent 與長上下文工作流](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80 |
| [🎮 上手 Demo 與 Showcase](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82 |
| [🔌 供應商與工具整合](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87 |
| [💸 成本、定價與本地部署](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89 |
| [🧭 限制、Caveat 與安全訊號](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75 |
| [🙏 致謝](#acknowledge) | 來源致謝與修正政策 |

### [📏 Benchmark 與前沿評測](#benchmarks-frontier-evaluation)

| Case | 展示重點 | 類型 |
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
| [Case 70: DeepSWE 高強度模式開源領先](#case-70) | 用這個案例追蹤 GLM-5.2 在 DeepSWE 高強度設定下的表現；貼文榜單顯示它以 44% pass@1 位列開源模型第一。 | Benchmark |
| [Case 72: LLM 辯論基準第二名](#case-72) | 用這個案例評估 GLM-5.2 在編碼之外的對抗式多輪辯論表現；max-reasoning 版本在結果中位列 Claude 系列之後的第二名。 | Benchmark |
| [Case 76: AA-Omniscience 幻覺率](#case-76) | 用這個案例比較 GLM-5.2 的不確定性處理能力；貼文中的 AA-Omniscience 結果顯示，它的幻覺率低於若干其他前沿模型。 | Evaluation |

### [💻 Coding Agent 與長上下文工作流](#coding-agents-long-context-workflows)

| Case | 展示重點 | 類型 |
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
| [Case 77: 生產級行銷 Agent 棧路由策略](#case-77) | 用這個案例把 GLM-5.2 路由到重視結構化、速度與自託管的生產 Agent 工作流中，同時把更強的閉源模型留給模糊判斷任務。 | Evaluation |
| [Case 80: M3 Ultra Pokemon Red Goal Run](#case-80) | 用這個案例評估 GLM-5.2 在長時間本地 coding agent 執行中的表現，追蹤它在 M3 Ultra 上花接近半天重建 Pokemon Red HTML 版本的嘗試。 | Demo |

### [🎮 上手 Demo 與 Showcase](#hands-on-demos-showcase-builds)

| Case | 展示重點 | 類型 |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | Use this case to compare same-prompt game-building output, runtime, and cost between GLM-5.2 and Opus 4.8. | Demo |
| [Three Real Builds With Mixed Results](#case-24) | Use this case as a cautionary demo set: test multiple real builds before trusting a model for production game or video tasks. | Evaluation |
| [Super Mario Clone In ZCode](#case-25) | Use this case to evaluate iterative game-building with GLM-5.2 and ZCode over several fix-and-feature passes. | Demo |
| [Lunar Lander Contest](#case-26) | Use this case to compare GLM-5.2, MiniMax M3, and Kimi K2.7 Code on an interactive game-style task. | Evaluation |
| [One-Prompt Design Arena Creation](#case-27) | Use this case to inspect what GLM-5.2 can generate from a single design prompt in an arena context. | Demo |
| [Research Paper Understanding Workflow](#case-28) | Use this case to apply GLM-5.2 to paper-reading workflows with contextual questions and cross-paper references. | Integration |
| [Constrained Poem Comparison](#case-29) | Use this case to separate correctness from creative quality when comparing GLM-5.2 with Fable-style models. | Evaluation |
| [Design Sense Example](#case-30) | Use this case as a lightweight visual-design signal, then verify with your own prompt and UI review. | Demo |
| [Case 71: Temple Run 體素遊戲單次生成](#case-71) | 用這個案例高壓測試 GLM-5.2 的單提示詞遊戲生成能力，再查看一個視覺元素較多的建置仍需要哪些迭代修正。 | Demo |
| [Case 78: OpenCode Go 單次生成案例集](#case-78) | 用這個案例在 OpenCode Go 裡快速基準測試 GLM-5.2 的單次生成建置能力，再決定是否投入更開放式的 Agent 迴圈。 | Demo |
| [Case 81: Space Invaders One-Prompt Build](#case-81) | 用這個案例測試 GLM-5.2 的單提示詞遊戲生成能力，並觀察少量後續回合如何完成素材替換與輕量打磨。 | Demo |
| [Case 82: OpenCode Recovery Lab One-Shot](#case-82) | 用這個案例快速原型化互動式 agent failure simulation；作者回報約 3.50 美元就一輪做出了可運作的 recovery lab。 | Demo |

### [🔌 供應商與工具整合](#provider-tool-integrations)

| Case | 展示重點 | 類型 |
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
| [Case 74: 面向網頁設計的 Browser Use QA 子代理](#case-74) | 當純文字模型需要視覺檢查與迭代式網站修復時，可用這個案例把 GLM-5.2 與 Browser Use v2 多模態 QA 子代理搭配起來。 | Integration |
| [Case 79: ZCode 官方 IDE 每日免費額度](#case-79) | 當你想要一個帶大額每日免費 token、互動體驗類似 Cursor 的官方編碼 IDE 時，可用這個案例透過 ZCode 存取 GLM-5.2。 | Tutorial |
| [Case 83: Cursor Setup Through Fireworks](#case-83) | 用這個案例透過 Fireworks 以最小 OpenAI 相容設定把 GLM-5.2 接入 Cursor，無須撰寫自訂客戶端程式。 | Tutorial |
| [Case 84: VulcanBench ZAI Provider Support](#case-84) | 用這個案例在開放 benchmark harness 中透過一級支援的 ZAI provider 與專用 API key 路徑執行 GLM-5.2。 | Integration |
| [Case 85: OpenCode High/Max Reasoning Variants](#case-85) | 用這個案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 變體，同時取得更可靠的 step-limit 處理。 | Integration |
| [Case 86: Z.ai Coding Endpoint Selection](#case-86) | 用這個案例把 GLM-5.2 coding plan 流量從通用 API 路徑切到針對 coding 最佳化的 Z.ai endpoint。 | Tutorial |
| [Case 87: ZenMux Free GLM-5.2 API Setup](#case-87) | 用這個案例取得免費的 GLM-5.2 API key 與 base URL，再接入 Claude、Cursor、Hermes 等工具。 | Tutorial |

### [💸 成本、定價與本地部署](#cost-pricing-local-deployment)

| Case | 展示重點 | 類型 |
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
| [Case 88: Two M3 Ultra MLX Distributed Run](#case-88) | 用這個案例估算 GLM-5.2 8-bit 在兩台 M3 Ultra 上進行分散式 MLX 推理時的實際部署表現，再決定是否擴大 Apple Silicon 配置。 | Demo |
| [Case 89: ZCode Multiplier Cut Through September](#case-89) | 用這個案例透過更低的 ZCode 尖峰與離峰 multiplier，在 9 月前盡量拉長 GLM-5.2 的 plan credits。 | Integration |

### [🧭 限制、Caveat 與安全訊號](#limits-caveats-safety-signals)

| Case | 展示重點 | 類型 |
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
| [Case 73: 程式碼審查與偏見檢查](#case-73) | 用這個案例作為程式碼與政治偏見測試的實務安全訊號，而不是把它當成更廣泛對齊問題已經解決的證明。 | Limit |
| [Case 75: 高難推理計費異常](#case-75) | 用這個案例謹慎測試 GLM-5.2 在高難推理負載上的表現，因為公開報告顯示它執行時間長、完成率低，而且計費輸出異常偏高。 | Limit |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 Benchmark 與前沿評測

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

類型: Benchmark | 日期: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE 高強度模式開源領先](https://x.com/datacurve/status/2068473057107476680) (作者 [@datacurve](https://x.com/datacurve))

**用這個案例追蹤 GLM-5.2 在 DeepSWE 高強度設定下的表現；貼文榜單顯示它以 44% pass@1 位列開源模型第一。**

DataCurve 分享的 DeepSWE 榜單更新顯示，GLM-5.2 在開源模型中達到 44% pass@1，並領先 Kimi K2.7 Code 17 個點。應把它視為一次 benchmark 更新，而不是所有真實世界 agent 工作流都已被解決的證明。

類型: Benchmark | 日期: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM 辯論基準第二名](https://x.com/LechMazur/status/2068428300460974279) (作者 [@LechMazur](https://x.com/LechMazur))

**用這個案例評估 GLM-5.2 在編碼之外的對抗式多輪辯論表現；max-reasoning 版本在結果中位列 Claude 系列之後的第二名。**

Lech Mazur 分享了一項 LLM Debate Benchmark 結果，其中 GLM-5.2 Max 排名第二。這個基準衡量的是跨廣泛主題的對抗式多輪辯論能力，因此它提供的是編碼榜單之外的推理訊號。

類型: Benchmark | 日期: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience 幻覺率](https://x.com/yuhasbeentaken/status/2068259921519423855) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**用這個案例比較 GLM-5.2 的不確定性處理能力；貼文中的 AA-Omniscience 結果顯示，它的幻覺率低於若干其他前沿模型。**

貼文報告 GLM-5.2 在 AA-Omniscience 上的幻覺率為 28%，低於 Fable 5 與 DeepSeek V4 Pro 的對應結果。這個基準關注的是模型在不確定時是否會拒答或承認不確定，而不是繼續猜測。

類型: Evaluation | 日期: 2026-06-20

---


<a id="coding-agents-long-context-workflows"></a>
## 💻 Coding Agent 與長上下文工作流

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

類型: Evaluation | 日期: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (作者 [@neural_avb](https://x.com/neural_avb))

**Use this case to improve GLM-5.2 long-context counting and REPL-agent behavior by moving instructions into the RLM system prompt.**

The release notes describe a concrete agent-scaffolding change and a GLM-5.2 long-context benchmark effect.

類型: Integration | 日期: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (作者 [@sydneyrunkle](https://x.com/sydneyrunkle))

**Use this case to try GLM-5.2 with an open coding-agent harness and compare the model under a reproducible agent shell.**

The author reports using GLM-5.2 with DeepAgents Code and frames open model plus open harness as the testing pattern.

類型: Demo | 日期: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [生產級行銷 Agent 棧路由策略](https://x.com/DeRonin_/status/2068303752671477820) (作者 [@DeRonin_](https://x.com/DeRonin_))

**用這個案例把 GLM-5.2 路由到重視結構化、速度與自託管的生產 Agent 工作流中，同時把更強的閉源模型留給模糊判斷任務。**

作者在代理機構棧中做了 6 天並行對比後表示，GLM-5.2 在開始漂移前可穩定執行 60 多個 agent 步驟，連續 800 多次匹配結構化格式，並提供低延遲的自託管回應。同一則貼文仍偏好用 Opus 處理語音關鍵或高歧義任務，因此真正有價值的是這條路由規則本身。

類型: Evaluation | 日期: 2026-06-20

---


<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手 Demo 與 Showcase

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
### Case 71: [Temple Run 體素遊戲單次生成](https://x.com/pseudokid/status/2068431546143649829) (作者 [@pseudokid](https://x.com/pseudokid))

**用這個案例高壓測試 GLM-5.2 的單提示詞遊戲生成能力，再查看一個視覺元素較多的建置仍需要哪些迭代修正。**

作者表示，首輪提示就生成出大部分 Temple Run 風格的體素摩托遊戲，之後只用少量補充輪次修正鏡頭與移動邏輯。貼文也提到 Z.ai 工具鏈可以生成截圖與實機影片，幫助文字模型評估結果。

類型: Demo | 日期: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 單次生成案例集](https://x.com/LyalinDotCom/status/2068378281636982990) (作者 [@LyalinDotCom](https://x.com/LyalinDotCom))

**用這個案例在 OpenCode Go 裡快速基準測試 GLM-5.2 的單次生成建置能力，再決定是否投入更開放式的 Agent 迴圈。**

作者展示了一組透過 OpenCode Go 完成的單次生成案例，包括太陽系 Web 應用、系統資訊 Electron 應用，以及一個簡單的探索小島 Web 遊戲。同一則貼文也表示，GLM-5.2 是他用過最強的開源模型，但還沒有把它稱作與最前沿閉源模型完全同級。

類型: Demo | 日期: 2026-06-20

---


<a id="provider-tool-integrations"></a>
## 🔌 供應商與工具整合

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

類型: Tutorial | 日期: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (作者 [@beyang](https://x.com/beyang))

**Use this case to pair GLM-5.2 with Amp custom agents when a text-only model needs visual-review support for design tasks.**

The post connects a GLM-5.2 visual design benchmark result with Amp plugin agents that can provide a review layer.

類型: Integration | 日期: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (作者 [@alphatozeta8148](https://x.com/alphatozeta8148))

**Use this case to route GLM-5.2 through Baseten when long-context serving speed matters for Factory Droid, OpenCode, and coding harnesses.**

The source reports GLM-5.2 running four times faster at full 1M context and shows it in coding harnesses.

類型: Integration | 日期: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [面向網頁設計的 Browser Use QA 子代理](https://x.com/browser_use/status/2068405699340853541) (作者 [@browser_use](https://x.com/browser_use))

**當純文字模型需要視覺檢查與迭代式網站修復時，可用這個案例把 GLM-5.2 與 Browser Use v2 多模態 QA 子代理搭配起來。**

Browser Use 表示，GLM-5.2 在一個網站設計任務中超過了 Fable 5，接著又加入 QA 子代理來檢查結果、判斷美感、找出 bug，並把定向修復建議回傳給 GLM。整套 build 加 QA 的循環據稱成本低於 0.75 美元。

類型: Integration | 日期: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 官方 IDE 每日免費額度](https://x.com/Alan_Earn/status/2068223665268006924) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**當你想要一個帶大額每日免費 token、互動體驗類似 Cursor 的官方編碼 IDE 時，可用這個案例透過 ZCode 存取 GLM-5.2。**

貼文將 ZCode 描述為智譜官方編碼 IDE，預設模型就是 GLM-5.2，並提供每日 300 萬 token、100 萬上下文視窗，以及 Mac 和 Windows 用戶端。它還包含一段簡短的上手流程，因此比一般的上線公告更具可操作性。

類型: Tutorial | 日期: 2026-06-20

---


<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定價與本地部署

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

類型: Demo | 日期: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (作者 [@mrblock](https://x.com/mrblock))

**Use this case to evaluate quantized GLM-5.2 deployment paths when full model weights are too large for ordinary local hardware.**

The post describes Unsloth dynamic 2-bit and 1-bit GGUF options, memory reductions, and llama.cpp or Unsloth Studio deployment routes.

類型: Tutorial | 日期: 2026-06-20

---


<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、Caveat 與安全訊號

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

類型: Limit | 日期: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [程式碼審查與偏見檢查](https://x.com/wongmjane/status/2068424945663893936) (作者 [@wongmjane](https://x.com/wongmjane))

**用這個案例作為程式碼與政治偏見測試的實務安全訊號，而不是把它當成更廣泛對齊問題已經解決的證明。**

作者稱，GLM-5.2 沒有把中國政治審查內容注入到程式碼中；同時它也糾正了一個關於越南戰爭的錯誤「美國偏見」說法，而對偏意見類問題保持不變。這使它成為測試政治敏感編碼行為與事實性表現的一個具體公開案例。

類型: Limit | 日期: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高難推理計費異常](https://x.com/s_batzoglou/status/2068297051247350154) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**用這個案例謹慎測試 GLM-5.2 在高難推理負載上的表現，因為公開報告顯示它執行時間長、完成率低，而且計費輸出異常偏高。**

作者執行了 11 個歸納推理題，只回報 4 個完成、2 個答對、多小時級執行時間，以及明顯高於可見 token 數的收費。這是關於推理效率與計費行為的具體警示，不只是 benchmark 分數問題。

類型: Limit | 日期: 2026-06-20

---


<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**用這個案例評估 GLM-5.2 在長時間本地 coding agent 執行中的表現，追蹤它在 M3 Ultra 上花接近半天重建 Pokemon Red HTML 版本的嘗試。**

作者把 Claude Code 的 model 切到本地 GLM 5.2，並在一台 M3 Ultra 512GB 機器上跑了 12 小時的 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 任務。貼文公開了執行時間、token 用量、code churn、RAM 使用量，以及 GGUF 與 KV-cache 配置，也指出模型品質感覺接近 frontier，但本地推理速度仍是主要瓶頸。

Type: Demo | Date: 2026-06-21

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**用這個案例測試 GLM-5.2 的單提示詞遊戲生成能力，並觀察少量後續回合如何完成素材替換與輕量打磨。**

作者表示，GLM-5.2 用一個主提示詞就生成了可玩的 Space Invaders 風格遊戲，接著再用三輪後續提示完成 sprite 替換與 leaderboard 等小幅增補。這個公開結果更適合作為輕量遊戲生成樣例，而不是完整 benchmark。

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**用這個案例快速原型化互動式 agent failure simulation；作者回報約 3.50 美元就一輪做出了可運作的 recovery lab。**

作者在輸入一份 4,000 字分析與 Agents SDK repository 後，用 OpenCode 搭配 GLM-5.2 建出一個完全可互動的 recovery lab。貼文列出了 176k token 的執行、一輪成型的結果，以及打磨前端到端約 3.50 美元的成本。

Type: Demo | Date: 2026-06-21

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**用這個案例透過 Fireworks 以最小 OpenAI 相容設定把 GLM-5.2 接入 Cursor，無須撰寫自訂客戶端程式。**

Skirano 展示了最簡 Cursor 設定流程：把 Fireworks key 填進 OpenAI API key 欄位，base URL 使用 `https://api.fireworks.ai/inference/v1`，模型選擇 `accounts/fireworks/models/glm-5p2`，然後重新啟動 Cursor。對想在熟悉的 coding IDE 裡試用 GLM-5.2 的人來說，這是一條相當具體的接入路徑。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**用這個案例在開放 benchmark harness 中透過一級支援的 ZAI provider 與專用 API key 路徑執行 GLM-5.2。**

VulcanBench v0.2.0 新增了一級支援的 ZAI provider，讓使用者能把 GLM-5.2 作為 `zai:glm-5.2` 與 OpenAI、Anthropic 模型並排執行，並提供獨立的 `ZAI_API_KEY`。如果你要的是開放、可重現的 benchmark harness，而不是單張截圖，這個案例更有用。

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**用這個案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 變體，同時取得更可靠的 step-limit 處理。**

OpenCode v1.17.9 為 GLM-5.2 新增了 High 與 Max thinking 變體，覆蓋 OpenAI 相容與 Anthropic 相容 provider，並原生支援 OpenRouter 的 effort 映射。相同版本也修正了 agent step-limit 行為，讓這個整合更適合較長的執行。

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用這個案例把 GLM-5.2 coding plan 流量從通用 API 路徑切到針對 coding 最佳化的 Z.ai endpoint。**

貼文建議，對於 coding plan 工作負載，應優先使用 `https://api.z.ai/api/coding/paas/v4`，而不是通用的 `https://api.z.ai/api/paas/v4/`。作者也補充說，Claude Code、OpenCode 等工具在支援時通常會走 `https://api.z.ai/api/anthropic`。如果你感覺 GLM-5.2 路由不對，這是一條非常具體的設定修正。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**用這個案例取得免費的 GLM-5.2 API key 與 base URL，再接入 Claude、Cursor、Hermes 等工具。**

作者分享了一條大約五分鐘的設定流程：取得免費的 ZenMux API key 與 base URL，然後把 GLM-5.2 接到 Claude、Cursor、Hermes 等工具上。貼文也提醒免費 tier 很快就會碰到 rate limit，因此它更適合作為 access note，而不是長期穩定性保證。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用這個案例估算 GLM-5.2 8-bit 在兩台 M3 Ultra 上進行分散式 MLX 推理時的實際部署表現，再決定是否擴大 Apple Silicon 配置。**

貼文展示了 GLM-5.2 8-bit 在兩台 M3 Ultra 512GB 機器上透過 MLX distributed 執行的情況，速度約 17.9 tokens/sec，總記憶體占用約 760GB。作者也明確說明這仍是一個進行中的 PR，因此它更適合作為 deployment signal，而不是完整部署指南。

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**用這個案例透過更低的 ZCode 尖峰與離峰 multiplier，在 9 月前盡量拉長 GLM-5.2 的 plan credits。**

這則貼文表示，ZCode 已把 GLM coding plan multiplier 在尖峰時段從 3x 下調到 2x，在離峰時段從 2x 下調到 0.67x，而且新窗口會持續到 9 月底。對想在 GLM-5.2 上盡量延長 credits 的人來說，這是一個非常具體的 access / pricing note。

Type: Integration | Date: 2026-06-21

---


<a id="acknowledge"></a>
## 🙏 致謝

本倉庫來自公開分享 GLM-5.2 使用證據的創作者、開發者、benchmark 團隊、供應商與社群。

感謝這些高訊號來源創作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)。

*我們無法保證每個案例都已歸屬到最初原創者。如果需要修正來源或署名，請聯絡我們，我們會更新。*

如果你有更多值得收錄的 GLM-5.2 使用案例，歡迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
