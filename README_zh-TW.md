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

- **109 個精選 GLM-5.2 案例**，來自公開創作者、評測團隊、工具開發者、服務商與一線使用者。
- 覆蓋基準與前沿評測、編碼代理與長上下文工作流、上手演示與作品展示、供應商與工具整合、成本、定價與本地部署、限制、注意事項與安全訊號。
- 每個案例都包含原始來源、創作者署名、精簡的使用結論、證據類型與發布日期。
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
| [📏 基準與前沿評測](#benchmarks-frontier-evaluation) | 案例 1-12, 60, 70, 72, 76, 90, 94 |
| [💻 編碼代理與長上下文工作流](#coding-agents-long-context-workflows) | 案例 13-22, 62, 65, 66, 77, 80, 91, 102 |
| [🎮 上手演示與作品展示](#hands-on-demos-showcase-builds) | 案例 23-30, 71, 78, 81-82, 92, 99-100 |
| [🔌 供應商與工具整合](#provider-tool-integrations) | 案例 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109 |
| [💸 成本、定價與本地部署](#cost-pricing-local-deployment) | 案例 43-51, 64, 68, 88-89, 97-98, 106-107 |
| [🧭 限制、注意事項與安全訊號](#limits-caveats-safety-signals) | 案例 52-59, 67, 73, 75, 103, 108 |
| [🙏 致謝](#acknowledge) | 來源致謝與修正政策 |

### [📏 基準與前沿評測](#benchmarks-frontier-evaluation)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [Artificial Analysis Intelligence Index](#case-1) | 使用人工分析貼文將 GLM-5.2 與其他開放權重和專有前沿模型在智慧和每項任務成本方面進行比較。 | 基準 |
| [Code Arena Frontend Ranking](#case-2) | 使用此案例在透過競技場式比較判斷的真實前端編碼任務上評估 GLM-5.2。 | 基準 |
| [Design Arena First Place](#case-3) | 使用此案例來判斷 GLM-5.2 是否可以處理設計加代碼任務，而不僅僅是文字密集型編碼基準。 | 基準 |
| [FrontierSWE Result](#case-4) | 使用 FrontierSWE 貼文將 GLM-5.2 與 GPT-5.5、Opus 和 Fable 風格的模型在軟體工程任務上進行比較。 | 基準 |
| [DeepSWE Open-Source Lead](#case-5) | 使用 DeepSWE 案例了解 GLM-5.2 作為用於困難的軟體工程評估任務的強大開放模型。 | 基準 |
| [Terminal-Bench Over 80 Percent](#case-6) | 在評估面向終端的編碼和代理工作流程的 GLM-5.2 時使用此案例。 | 基準 |
| [SWELancer 與 GPT-5.5 的比較](#case-7) | 使用此 SWELancer 案例作為 GLM-5.2 和 GPT-5.5 在任務成功、獎勵和完成時間方面的具體多指標比較。 | 評測 |
| [BridgeBench Perfect Score Signal](#case-8) | 使用此案例來檢查基於多步驟推理的 GLM-5.2，而不僅僅是編碼排行榜。 | 基準 |
| [BridgeBench Reasoning Number One](#case-9) | 使用此案例在紮根推理任務上將 GLM-5.2 與封閉邊界模型進行比較。 | 基準 |
| [KernelBench-Hard Without Shortcutting](#case-10) | 在檢查基準測試收益是否來自有效的實現行為而不是捷徑時使用此案例。 | 評測 |
| [Runescape Bench Catch-Up](#case-11) | 使用此案例作為開放權重模型在類似遊戲的基準任務上取得進展的快速訊號。 | 基準 |
| [BridgeBench Speed Improvement](#case-12) | 使用此案例來評估對延遲敏感的工作流程，其中速度與智慧同樣重要。 | 基準 |
| [KernelBench 硬核與巨型 GPU 編碼](#case-60) | 使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 評估 GPU 核心編碼上的 GLM-5.2，其中開放代理追蹤使結果可檢查。 | 基準 |
| [DeepSWE 高強度模式開源領先](#case-70) | 用這個案例追蹤 GLM-5.2 在 DeepSWE 高強度設定下的表現；貼文榜單顯示它以 44% pass@1 位列開源模型第一。 | 基準 |
| [LLM 辯論基準第二名](#case-72) | 用這個案例評估 GLM-5.2 在編碼之外的對抗式多輪辯論表現；max-reasoning 版本在結果中位列 Claude 系列之後的第二名。 | 基準 |
| [AA-Omniscience 幻覺率](#case-76) | 用這個案例比較 GLM-5.2 的不確定性處理能力；貼文中的 AA-Omniscience 結果顯示，它的幻覺率低於若干其他前沿模型。 | 評測 |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | 如果你想比較 GLM-5.2 在長期知識工作中的表現，而不只是看編碼榜單，可以用這個案例。 | 評測 |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | 如果你想判斷 GLM-5.2 的遊戲建構品質，可以用這個案例。它在 Game Dev Arena 拿到第二名，並成為該榜單中開放權重陣營的第一名。 | 評測 |

### [💻 編碼代理與長上下文工作流](#coding-agents-long-context-workflows)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [One Hour Forty Two Minute Refactor Loop](#case-13) | 使用此案例作為使用 TDD、審閱者回饋和回歸檢查進行長時間自主前端重構的模式。 | 演示 |
| [OpenCode Bug Fix And Implementation Test](#case-14) | 使用此案例來測試 GLM-5.2 作為 OpenCode 編碼代理程式的錯誤修復以及小型實作任務。 | 演示 |
| [OpenCode Retro Video Game Walkthrough](#case-15) | 使用此演練透過單一提示使用 GLM-5.2 和 OpenCode 建立一個小遊戲，然後檢查模型如何處理實作細節。 | 教程 |
| [HTML5 Physics Simulations Contest](#case-16) | 使用此案例在沒有庫的獨立 HTML5 物理模擬上比較 GLM-5.2 和 Kimi K2.7 程式碼。 | 評測 |
| [Personal Site UI UX Build](#case-17) | 使用此案例提示 GLM-5.2 打造一個精美的個人網站，並檢查多次轉動可以在多大程度上改善 UI/UX。 | 演示 |
| [AI Contract Review Product Build](#case-18) | 使用此案例透過 PRD、時間預算、步驟計數、使用配額和程式碼品質比較來評估產品建置任務上的 GLM-5.2。 | 評測 |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | 使用此案例了解如何將 GLM-5.2 整合到 ZCode 3.0 中以執行更大的代理開發任務。 | 整合 |
| [使用 GLM-5.2 建構的 ZCode 的 Linux 包裝器](#case-20) | 使用此案例作為 GLM-5.2 協助編碼代理環境工具的範例。 | 演示 |
| [Computer Use Skill Packaging](#case-21) | 使用此案例來研究 GLM-5.2，將其作為將開源電腦使用儲存庫轉變為可重複使用技能的助手。 | 演示 |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | 使用此案例在完整的代理開發環境而不是單一聊天會話中評估 GLM-5.2。 | 演示 |
| [具有本地服務的 OpenCode Harness](#case-62) | 使用此案例透過 OpenCode 工具、本機服務和工具密集型編碼工作流程來測試 GLM-5.2，然後將其與 Claude Opus 進行比較。 | 評測 |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | 使用此案例透過將指令移至 RLM 系統提示字元來改進 GLM-5.2 長上下文計數和 REPL 代理行為。 | 整合 |
| [DeepAgents Code Open Harness Trial](#case-66) | 使用此案例嘗試使用開放式編碼代理工具的 GLM-5.2，並在可重現的代理 shell 下比較模型。 | 演示 |
| [生產級行銷 Agent 棧路由策略](#case-77) | 用這個案例把 GLM-5.2 路由到重視結構化、速度與自託管的生產 Agent 工作流中，同時把更強的閉源模型留給模糊判斷任務。 | 評測 |
| [M3 Ultra Pokemon Red Goal Run](#case-80) | 用這個案例評估 GLM-5.2 在長時間本地 coding agent 執行中的表現，追蹤它在 M3 Ultra 上花接近半天重建 Pokemon Red HTML 版本的嘗試。 | 演示 |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | 如果你想比較 GLM-5.2 與 Opus 4.8 在真實儲存庫 bug 修復中的表現，可以用這個案例。GLM 雖然用了更多 token，但最後產出的 patch 更便宜也更乾淨。 | 評測 |
| [Case 102: OpenInspect FP8 Background Agent](#case-102) | 如果你想研究自託管的 GLM-5.2 背景 agent 棧，而不是託管聊天工作流，可以用這個案例。 | 整合 |

### [🎮 上手演示與作品展示](#hands-on-demos-showcase-builds)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | 使用此案例來比較 GLM-5.2 和 Opus 4.8 之間相同提示的遊戲建立輸出、運行時間和成本。 | 演示 |
| [三個真實的構建結果參差不齊](#case-24) | 將此案例用作警示演示集：在信任用於生產遊戲或視訊任務的模型之前測試多個真實構建。 | 評測 |
| [Super Mario Clone In ZCode](#case-25) | 使用此案例來評估使用 GLM-5.2 和 ZCode 在多個修復和功能過程中進行的迭代遊戲建置。 | 演示 |
| [Lunar Lander Contest](#case-26) | 使用此案例在互動式遊戲類型任務上比較 GLM-5.2、MiniMax M3 和 Kimi K2.7 代碼。 | 評測 |
| [One-Prompt Design Arena Creation](#case-27) | 使用此案例來檢查 GLM-5.2 可以從競技場上下文中的單一設計提示產生什麼。 | 演示 |
| [研究論文理解工作流程](#case-28) | 使用此案例將 GLM-5.2 應用於包含上下文問題和跨論文參考的論文閱讀工作流程。 | 整合 |
| [Constrained Poem Comparison](#case-29) | 在將 GLM-5.2 與寓言風格模型進行比較時，使用此案例將正確性與創意品質分開。 | 評測 |
| [Design Sense Example](#case-30) | 使用此案例作為輕量級視覺設計訊號，然後使用您自己的提示和 UI 審查進行驗證。 | 演示 |
| [Temple Run 體素遊戲單次生成](#case-71) | 用這個案例高壓測試 GLM-5.2 的單提示詞遊戲生成能力，再查看一個視覺元素較多的建置仍需要哪些迭代修正。 | 演示 |
| [OpenCode Go 單次生成案例集](#case-78) | 用這個案例在 OpenCode Go 裡快速基準測試 GLM-5.2 的單次生成建置能力，再決定是否投入更開放式的 Agent 迴圈。 | 演示 |
| [Space Invaders One-Prompt Build](#case-81) | 用這個案例測試 GLM-5.2 的單提示詞遊戲生成能力，並觀察少量後續回合如何完成素材替換與輕量打磨。 | 演示 |
| [OpenCode Recovery Lab One-Shot](#case-82) | 用這個案例快速原型化互動式 agent failure simulation；作者回報約 3.50 美元就一輪做出了可運作的 recovery lab。 | 演示 |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | 如果你想測試 GLM-5.2 在參考驅動網站重建上的能力，可以用這個案例。只給一個來源 URL 和一條提示詞，就幾乎像素級重現了網站。 | 演示 |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | 如果你想比較 GLM-5.2 在全端 UI 建構上的表現，可以用這個案例。它做出的交易桌面結果接近最精緻的版本，但成本只占頂尖結果的一小部分。 | 評測 |
| [Case 100: Luddite Game After Claude Refusal](#case-100) | 如果閉源模型因政策原因拒絕請求，而你又想原型化帶政策敏感性的遊戲概念，可以用這個案例測試 GLM-5.2。 | 演示 |

### [🔌 供應商與工具整合](#provider-tool-integrations)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [OpenCode Go Availability](#case-31) | 使用此案例透過文字、1M 上下文和類似 GLM-5.1 的定價來追蹤 OpenCode Go 工作流程中的 GLM-5.2 可用性。 | 整合 |
| [Ollama Cloud Availability](#case-32) | 使用此案例將 GLM-5.2 路由到 Ollama Cloud 中，以進行可存取的開源編碼模型實驗。 | 整合 |
| [OpenRouter One API Call Access](#case-33) | 在比較提供者路由或多模型堆疊時，使用此案例透過 OpenRouter 存取 GLM-5.2。 | 整合 |
| [vLLM Day-Zero Support](#case-34) | 使用此案例透過 vLLM 自行託管或提供 GLM-5.2 服務，並提供零日支援。 | 整合 |
| [Notion Availability Via Baseten](#case-35) | 使用此案例將 GLM-5.2 識別為 Notion 工作流程中可用的開放權重模型。 | 整合 |
| [Fireworks Day-Zero Serving](#case-36) | 使用此案例來評估 Fireworks 作為需要託管基礎架構的 GLM-5.2 工作負載的服務路徑。 | 整合 |
| [谷歌雲模型花園鏈接](#case-37) | 使用此案例在 Google Cloud 導向的部署和代理平台上下文中尋找 GLM-5.2。 | 整合 |
| [Venice Privacy Mode](#case-38) | 當隱私模式、TEE 或端對端加密是嘗試 GLM-5.2 的決定因素時，請使用此案例。 | 整合 |
| [Command Code Availability](#case-39) | 使用此案例嘗試命令代碼中的 GLM-5.2，具有低成本入門計劃和長上下文編碼功能。 | 整合 |
| [來自 Nous Portal 的赫爾墨斯特工](#case-40) | 使用此案例透過 Nous Portal 和 OpenRouter 將 GLM-5.2 連接到 Hermes Agent 工作流程。 | 整合 |
| [io.net Day-Zero Launch Partner](#case-41) | 在評估 753B 參數長上下文模型的計算支援服務時使用此案例。 | 整合 |
| [Modular Cloud Day-Zero Serving](#case-42) | 使用此案例來考慮在提供者規模提供長上下文 GLM-5.2 服務的模組化雲端。 | 整合 |
| [Cursor Setup Through OpenRouter](#case-61) | 使用此案例透過 OpenRouter 在 Cursor 中設定 GLM-5.2，以實現低成本的開放模型編碼工作流程。 | 教程 |
| [Amp Agentic Eyes For Visual Design](#case-63) | 當純文字模型需要視覺審核支援來完成設計任務時，可以使用此案例將 GLM-5.2 與 Amp 自訂代理程式配對。 | 整合 |
| [Baseten Faster One-Million-Context Serving](#case-69) | 當長上下文服務速度對於 Factory Droid、OpenCode 和編碼工具很重要時，可以使用此案例透過 Baseten 路由 GLM-5.2。 | 整合 |
| [面向網頁設計的 Browser Use QA 子代理](#case-74) | 當純文字模型需要視覺檢查與迭代式網站修復時，可用這個案例把 GLM-5.2 與 Browser Use v2 多模態 QA 子代理搭配起來。 | 整合 |
| [ZCode 官方 IDE 每日免費額度](#case-79) | 當你想要一個帶大額每日免費 token、互動體驗類似 Cursor 的官方編碼 IDE 時，可用這個案例透過 ZCode 存取 GLM-5.2。 | 教程 |
| [Cursor Setup Through Fireworks](#case-83) | 用這個案例透過 Fireworks 以最小 OpenAI 相容設定把 GLM-5.2 接入 Cursor，無須撰寫自訂客戶端程式。 | 教程 |
| [VulcanBench ZAI Provider Support](#case-84) | 用這個案例在開放 benchmark harness 中透過一級支援的 ZAI provider 與專用 API key 路徑執行 GLM-5.2。 | 整合 |
| [OpenCode High/Max Reasoning Variants](#case-85) | 用這個案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 變體，同時取得更可靠的 step-limit 處理。 | 整合 |
| [Z.ai Coding Endpoint Selection](#case-86) | 用這個案例把 GLM-5.2 coding plan 流量從通用 API 路徑切到針對 coding 最佳化的 Z.ai endpoint。 | 教程 |
| [ZenMux Free GLM-5.2 API Setup](#case-87) | 用這個案例取得免費的 GLM-5.2 API key 與 base URL，再接入 Claude、Cursor、Hermes 等工具。 | 教程 |
| [Case 93: Noumena ncode GLM Default](#case-93) | 如果你想把 GLM-5.2 導入 ncode 與 Noumena 風格的 agent 環境，並同時使用標準版與 1M 上下文端點以及預設模型支援，可以用這個案例。 | 整合 |
| [Case 95: Claude Code Through Baseten](#case-95) | 如果你想透過 Baseten key、自訂 base URL，以及 `~/.claude/settings.json` 裡的模型映射，在 Claude Code 中執行 GLM-5.2，可以用這個案例。 | 教學 |
| [Case 96: Deepsec Pi Agent Default](#case-96) | 如果你想在安全 harness 中測試 GLM-5.2，可以用這個案例。`deepsec` 把它設成 Pi agent 的預設模型，並回報了具競爭力的 eval 結果。 | 整合 |
| [Case 101: Baseten + Droid Harness Quickstart](#case-101) | 如果你想透過 Baseten 與 Droid harness 快速跑通 GLM-5.2，並重用一套也適用於其他 IDE 的短設定流程，可以用這個案例。 | 教學 |
| [Case 104: OpenAI-Compatible GLM API Workflow](#case-104) | 如果你想在 Python 裡用一個 OpenAI 相容客戶端統一接入 GLM-5.2 的推理控制、tool calling、長上下文檢索與成本統計，可以用這個案例。 | 教學 |
| [Case 105: Perplexity Agent API Search Sandbox](#case-105) | 如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，並透過單一 API 呼叫取得帶搜尋能力的沙盒 agent，可以用這個案例。 | 整合 |
| [Case 109: Baseten 280 TPS GLM API](#case-109) | 如果你在意 provider 延遲表現，可以用這個案例查看 Baseten 對 GLM-5.2 高吞吐、低首 token 延遲的公開效能說法。 | 整合 |

### [💸 成本、定價與本地部署](#cost-pricing-local-deployment)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [Output Token Cost Comparison](#case-43) | 使用此案例將 GLM-5.2 輸出代幣經濟學與 Opus、Fable 和 GPT-5.5 風格的模型進行比較。 | 評測 |
| [Local Near-Frontier Hardware ROI](#case-44) | 使用此案例來推理自託管類似 GLM-5.2 的模型是否可以為重度代理用戶償還硬體成本。 | 評測 |
| [MLX On Two Mac Studios](#case-45) | 使用此案例探索在 Apple 硬體和麵向 MLX 的設定上運行的本機 GLM-5.2。 | 演示 |
| [H100 Monthly Local Deployment Claim](#case-46) | 使用此案例作為成本比較提示，用於在訂閱和自託管之間進行選擇之前檢查本地部署假設。 | 評測 |
| [Daily Credits And Claude Replacement Claim](#case-47) | 使用此案例來檢查圍繞 GLM-5.2 的免費信用和替代代理敘述，同時將行銷聲明與經過驗證的工作負載適合度分開。 | 評測 |
| [Free ZCode Token Window](#case-48) | 在承諾付費提供者或本地部署之前，使用此案例透過免費 ZCode 津貼測試 GLM-5.2。 | 整合 |
| [ZenMux Free Week Offer](#case-49) | 使用此案例來尋找用於 GLM-5.2 測試的時間限制的自由存取視窗。 | 整合 |
| [crofAI 每代幣定價](#case-50) | 在選擇路線之前，使用此案例比較 GLM-5.2 的第三方提供者定價。 | 整合 |
| [API Price Margin Comparison](#case-51) | 將 GLM-5.2 與其他前沿實驗室和開放模型進行比較時，請使用此案例作為市場定價批評。 | 評測 |
| [Basement Local Inference Speed](#case-64) | 在規劃離線編碼設定之前，使用此案例來估計大內存 Apple 硬體上的本地 GLM-5.2 推理吞吐量。 | 演示 |
| [Unsloth Quantized Local Deployment](#case-68) | 當完整模型權重對於普通本地硬體來說太大時，使用此案例來評估量化的 GLM-5.2 部署路徑。 | 教程 |
| [Two M3 Ultra MLX Distributed Run](#case-88) | 用這個案例估算 GLM-5.2 8-bit 在兩台 M3 Ultra 上進行分散式 MLX 推理時的實際部署表現，再決定是否擴大 Apple Silicon 配置。 | 演示 |
| [ZCode Multiplier Cut Through September](#case-89) | 用這個案例透過更低的 ZCode 尖峰與離峰 multiplier，在 9 月前盡量拉長 GLM-5.2 的 plan credits。 | 整合 |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | 如果你想估算高階本地 GLM-5.2 工作站的規模，可以用這個案例。雙 Blackwell 桌機在 4-bit 量化版本上維持了雙位數 decode 速度。 | 演示 |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | 如果你想判斷為了本地 GLM-5.2 推論購買 Mac Studio 是否划算，可以用這個案例。貼文中的回本計算明顯更偏向 API 或方案存取。 | 評測 |
| [Case 106: LiteLLM Local Outage Save](#case-106) | 如果託管前沿 API 宕機或額度耗盡，而你又要確保交付不中斷，可以用這個案例參考本地部署的 GLM-5.2 搭配 LiteLLM 兜底。 | 演示 |
| [Case 107: Individual Versus Team Local ROI](#case-107) | 如果你想判斷本地部署 GLM-5.2 更適合個人還是團隊，可以用這個案例做成本與組織規模判斷。 | 評測 |

### [🧭 限制、注意事項與安全訊號](#limits-caveats-safety-signals)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [No Vision Caveat](#case-52) | 使用此案例請記住，GLM-5.2 對於需要本機視覺功能的工作流程可能不太有用。 | 限制 |
| [現實世界的代理差距警告](#case-53) | 使用此案例可以避免過度閱讀基準測試勝利，以證明 GLM-5.2 與所有已部署的代理任務上的最佳專有模型相符。 | 限制 |
| [Safety Guardrail Concern](#case-54) | 使用此案例提醒您在敏感網域中部署 GLM-5.2 之前執行安全性評估。 | 限制 |
| [基準方法論批評](#case-55) | 即使整體結果有利於 GLM-5.2，也可以使用此案例來質疑基準方法。 | 限制 |
| [Peak-Time Latency Concern](#case-56) | 在切換編碼計劃或將 Claude 代碼式工作流程路由到 GLM-5.2 之前，使用此案例測試提供程式延遲。 | 限制 |
| [FutureSim Non-Improvement Result](#case-57) | 在廣泛部署之前，使用此案例檢查編碼增益是否推廣到非編碼領域。 | 限制 |
| [Launch Readiness Critique](#case-58) | 使用此案例將模型功能與啟動執行、文件和 API 準備分開。 | 限制 |
| [編碼計劃價格上漲](#case-59) | 在推薦 GLM-5.2 作為低成本替代品之前，請使用此案例驗證計劃定價。 | 限制 |
| [短時間並行工作與長代理運行](#case-67) | 使用此案例將 GLM-5.2 路由到短邊界編碼任務，同時為更深的多小時代理運行保留更強的模型。 | 限制 |
| [程式碼審查與偏見檢查](#case-73) | 用這個案例作為程式碼與政治偏見測試的實務安全訊號，而不是把它當成更廣泛對齊問題已經解決的證明。 | 限制 |
| [高難推理計費異常](#case-75) | 用這個案例謹慎測試 GLM-5.2 在高難推理負載上的表現，因為公開報告顯示它執行時間長、完成率低，而且計費輸出異常偏高。 | 限制 |
| [Case 103: HalluHard Multiturn Hallucination Signal](#case-103) | 如果你想在信任其他強基準結果前，先測試 GLM-5.2 在多輪幻覺敏感任務上的表現，可以用這個案例。 | 限制 |
| [Case 108: Open-Weight Security Emergency Warning](#case-108) | 如果你在做安全規劃，可以用這個案例理解開放權重 GLM-5.2 如何降低進攻性安全 agent 的實際操作門檻。 | 限制 |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 基準與前沿評測

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**使用人工分析貼文將 GLM-5.2 與其他開放權重和專有前沿模型在智慧和每項任務成本方面進行比較。**

Artificial Analysis 將 GLM-5.2 報告為其智慧指數中領先的開放權重模型，得分為 51，在智慧與每項任務成本方面處於帕累托前沿位置。該帖子還記錄了模型大小、上下文視窗、定價和提供者可用性。

類型: 基準 | 日期: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (作者 [@arena](https://x.com/arena))

**使用此案例在透過競技場式比較判斷的真實前端編碼任務上評估 GLM-5.2。**

Arena 帳戶報告稱，GLM-5.2 Max 在 Code Arena 前端排名第二，領先其他開放型號，接近頂級前沿入口。這篇文章對於前端、React、HTML、遊戲、模擬和基於參考的設計用例特別有用。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (作者 [@Designarena](https://x.com/Designarena))

**使用此案例來判斷 GLM-5.2 是否可以處理設計加代碼任務，而不僅僅是文字密集型編碼基準。**

Design Arena 報告稱，GLM-5.2 以 1360 的 Elo 分數排名第一，凸顯了開放權重模型設計程式碼效能的飛躍。將其視為設計基準訊號，而不是取代特定於專案的 UI 審查。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (作者 [@ProximalHQ](https://x.com/ProximalHQ))

**使用 FrontierSWE 貼文將 GLM-5.2 與 GPT-5.5、Opus 和 Fable 風格的模型在軟體工程任務上進行比較。**

該貼文報告指出 GLM-5.2 在 FrontierSWE 上排名第三，並將其定義為首批開放權重模型之一，以縮小與實施繁重的工程工作中頂級專有模型的差距。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (作者 [@AiBattle_](https://x.com/AiBattle_))

**使用 DeepSWE 案例了解 GLM-5.2 作為用於困難的軟體工程評估任務的強大開放模型。**

AiBattle 報告 GLM-5.2 的 DeepSWE 得分為 46.2%，並將其描述為該基準測試環境中開源模型的最高得分。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (作者 [@cline](https://x.com/cline))

**在評估面向終端的編碼和代理工作流程的 GLM-5.2 時使用此案例。**

Cline 強調 GLM-5.2 是第一個在 Terminal-Bench 上突破 80% 的開放權重模型，並將其定位為可訪問的基於工具的開發的前沿選項。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer 與 GPT-5.5 的比較](https://x.com/gosrum/status/2067153091842203676) (作者 [@gosrum](https://x.com/gosrum))

**使用此 SWELancer 案例作為 GLM-5.2 和 GPT-5.5 在任務成功、獎勵和完成時間方面的具體多指標比較。**

作者分享了日本基準更新，其中 GLM-5.2 在最新的 SWELancer 結果上意外領先 GPT-5.5，包括任務成功率、獲得的獎勵和完成時間，其中排除了兩項無法完成的任務。

類型: 評測 | 日期: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (作者 [@bridgemindai](https://x.com/bridgemindai))

**使用此案例來檢查基於多步驟推理的 GLM-5.2，而不僅僅是編碼排行榜。**

BridgeMind 報告稱，GLM-5.2 是第一個在 BridgeBench BS 基準測試中獲得滿分的模型，這使其成為推理密集型評估聲明的有用來源。

類型: 基準 | 日期: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (作者 [@bridgebench](https://x.com/bridgebench))

**使用此案例在紮根推理任務上將 GLM-5.2 與封閉邊界模型進行比較。**

BridgeBench 報告稱，GLM-5.2 在推理基準測試中排名第一，並在該測量環境中擊敗了 Claude Fable 5。

類型: 基準 | 日期: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (作者 [@elliotarledge](https://x.com/elliotarledge))

**在檢查基準測試收益是否來自有效的實現行為而不是捷徑時使用此案例。**

KernelBench-Hard 貼文表示，有趣的結果不僅僅是分數，而且 GLM-5.2 停止在 fp8 GEMM 問題上使用不適當的快捷方式，使其與基準完整性相關。

類型: 評測 | 日期: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (作者 [@maxbittker](https://x.com/maxbittker))

**使用此案例作為開放權重模型在類似遊戲的基準任務上取得進展的快速訊號。**

該貼文報告稱，GLM-5.2 在 Runescape 平台上的得分優於最新的專有模型，並使用該結果來衡量開源前緣功能的追趕速度。

類型: 基準 | 日期: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (作者 [@bridgebench](https://x.com/bridgebench))

**使用此案例來評估對延遲敏感的工作流程，其中速度與智慧同樣重要。**

BridgeBench 報告稱，GLM-5.2 比 GLM-5.1 快三倍，在其速度基準上排名第四，這使其與迭代速度影響可用性的工作流程相關。

類型: 基準 | 日期: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench 硬核與巨型 GPU 編碼](https://x.com/elliotarledge/status/2068177175640240323) (作者 [@elliotarledge](https://x.com/elliotarledge))

**使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 評估 GPU 核心編碼上的 GLM-5.2，其中開放代理追蹤使結果可檢查。**

KernelBench 更新報告了 H100、B200 和 RTX PRO 6000 測試、開源代理追蹤以及 GLM-5.2 作為比較中排名最高的開放模型。

類型: 基準 | 日期: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE 高強度模式開源領先](https://x.com/datacurve/status/2068473057107476680) (作者 [@datacurve](https://x.com/datacurve))

**用這個案例追蹤 GLM-5.2 在 DeepSWE 高強度設定下的表現；貼文榜單顯示它以 44% pass@1 位列開源模型第一。**

DataCurve 分享的 DeepSWE 榜單更新顯示，GLM-5.2 在開源模型中達到 44% pass@1，並領先 Kimi K2.7 Code 17 個點。應把它視為一次 benchmark 更新，而不是所有真實世界 agent 工作流都已被解決的證明。

類型: 基準 | 日期: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM 辯論基準第二名](https://x.com/LechMazur/status/2068428300460974279) (作者 [@LechMazur](https://x.com/LechMazur))

**用這個案例評估 GLM-5.2 在編碼之外的對抗式多輪辯論表現；max-reasoning 版本在結果中位列 Claude 系列之後的第二名。**

Lech Mazur 分享了一項 LLM Debate Benchmark 結果，其中 GLM-5.2 Max 排名第二。這個基準衡量的是跨廣泛主題的對抗式多輪辯論能力，因此它提供的是編碼榜單之外的推理訊號。

類型: 基準 | 日期: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience 幻覺率](https://x.com/yuhasbeentaken/status/2068259921519423855) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**用這個案例比較 GLM-5.2 的不確定性處理能力；貼文中的 AA-Omniscience 結果顯示，它的幻覺率低於若干其他前沿模型。**

貼文報告 GLM-5.2 在 AA-Omniscience 上的幻覺率為 28%，低於 Fable 5 與 DeepSeek V4 Pro 的對應結果。這個基準關注的是模型在不確定時是否會拒答或承認不確定，而不是繼續猜測。

類型: 評測 | 日期: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想比較 GLM-5.2 在長期知識工作中的表現，而不只是看編碼榜單，可以用這個案例。**

Artificial Analysis 指出，GLM-5.2 在 GDPval-AA 上拿到 1524 Elo，綜合排名第 3，落後 Claude Fable 5 和 Opus 4.8，並略高於 1509 的 GPT-5.5 xhigh。它也是開放權重模型中的斷層第一。貼文還提到，這個 benchmark 在 1,999 場對戰中平均每個任務約有 31 輪互動。

類型: 評測 | 日期: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (作者 [@Designarena](https://x.com/Designarena))

**如果你想判斷 GLM-5.2 的遊戲建構品質，可以用這個案例。它在 Game Dev Arena 拿到第二名，並成為該榜單中開放權重陣營的第一名。**

Design Arena 報告指出，GLM-5.2 在 Game Dev Arena 上拿到 1368 Elo，比 GLM-5.1 提升 29 分，排名前進 6 位。貼文表示，它已進入與 Claude Fable 5 相同的表現區間，並拿下綜合第二名；若以實驗室維度來看，它超過了 OpenAI，只落後 Anthropic。

類型: 評測 | 日期: 2026-06-22

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 編碼代理與長上下文工作流

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (作者 [@KELMAND1](https://x.com/KELMAND1))

**使用此案例作為使用 TDD、審閱者回饋和回歸檢查進行長時間自主前端重構的模式。**

該文章描述了一項耗時 1 小時 42 分鐘的 GLM-5.2 重構任務，其中包含 88 次模型轉換和 102 次工具呼叫。工作流程包括交接、四個阻止程序修復、12 項測試的 TDD 實施、兩輪 P2 修復和最終回歸。

類型: 演示 | 日期: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (作者 [@altudev](https://x.com/altudev))

**使用此案例來測試 GLM-5.2 作為 OpenCode 編碼代理程式的錯誤修復以及小型實作任務。**

作者報告稱，測試 GLM-5.2 時修復了 6 個錯誤，並在 OpenCode 中實現了一項，並稱這些更改通過可靠的規劃和比 GLM-5.1 更快的速度順利完成。

類型: 演示 | 日期: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (作者 [@AskVenice](https://x.com/AskVenice))

**使用此演練透過單一提示使用 GLM-5.2 和 OpenCode 建立一個小遊戲，然後檢查模型如何處理實作細節。**

Venice 分享了使用 GLM-5.2 和 OpenCode 建立復古電玩遊戲的完整演練，將其定位為私人、開源、長期編碼工作流程。

類型: 教程 | 日期: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**使用此案例在沒有庫的獨立 HTML5 物理模擬上比較 GLM-5.2 和 Kimi K2.7 程式碼。**

Atomic Chat 報告要求兩個模型建造泳池休息、彈簧塊和高爾頓板模擬。他們的貼文稱，GLM-5.2 以更詳細和完善的方式處理了這三個問題，而 Kimi 則在身體行為方面遇到了困難。

類型: 評測 | 日期: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (作者 [@anshuc](https://x.com/anshuc))

**使用此案例提示 GLM-5.2 打造一個精美的個人網站，並檢查多次轉動可以在多大程度上改善 UI/UX。**

作者表示，GLM-5.2 在正確的提示下產生了一個富有創意的個人網站，並分享了結果的影片。它對於前端設計迭代而不是單次基準測試很有用。

類型: 演示 | 日期: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (作者 [@laozhang2579](https://x.com/laozhang2579))

**使用此案例透過 PRD、時間預算、步驟計數、使用配額和程式碼品質比較來評估產品建置任務上的 GLM-5.2。**

這篇中文文章在人工智慧合約審查產品 PRD 上比較了 GLM-5.2、Kimi K2.7 和 Claude Opus 4.8。它報告構建持續時間、步驟計數、五小時配額使用情況和代碼品質評分。

類型: 評測 | 日期: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (作者 [@zcode_ai](https://x.com/zcode_ai))

**使用此案例了解如何將 GLM-5.2 整合到 ZCode 3.0 中以執行更大的代理開發任務。**

ZCode 宣佈為編碼計劃用戶提供 GLM-5.2、更強大的代理任務執行、更好的長上下文編碼以及用於管理從計劃到完成的更大目標的目標功能。

類型: 整合 | 日期: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [使用 GLM-5.2 建構的 ZCode 的 Linux 包裝器](https://x.com/gosrum/status/2066484949755269510) (作者 [@gosrum](https://x.com/gosrum))

**使用此案例作為 GLM-5.2 協助編碼代理環境工具的範例。**

作者報告使用 GLM-5.2 和 Claude Code 完成 zcode-linux，以便 Linux 使用者可以在 Linux 環境中執行 ZCode 並新增任意 API 端點，包括本機 LLM 端點。

類型: 演示 | 日期: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (作者 [@0xSero](https://x.com/0xSero))

**使用此案例來研究 GLM-5.2，將其作為將開源電腦使用儲存庫轉變為可重複使用技能的助手。**

該貼文稱 GLM-5.2 正在設定電腦使用，找到了一個高級開源儲存庫，並將其轉換為技能。它是工具包裝和代理整合工作的實際操作訊號。

類型: 演示 | 日期: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (作者 [@laogui](https://x.com/laogui))

**使用此案例在完整的代理開發環境而不是單一聊天會話中評估 GLM-5.2。**

國內評測稱，ZCode 3.0由類似shell的早期版本重寫為自主開發的代理核心，搭配GLM-5.2，在國內代理開發環境中具有更好的體驗。

類型: 演示 | 日期: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [具有本地服務的 OpenCode Harness](https://x.com/PatrickToulme/status/2068134212587184442) (作者 [@PatrickToulme](https://x.com/PatrickToulme))

**使用此案例透過 OpenCode 工具、本機服務和工具密集型編碼工作流程來測試 GLM-5.2，然後將其與 Claude Opus 進行比較。**

作者報告了本地部署、嵌套子代理、研究/規劃行為和工作應用程式建置。

類型: 評測 | 日期: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (作者 [@neural_avb](https://x.com/neural_avb))

**使用此案例透過將指令移至 RLM 系統提示字元來改進 GLM-5.2 長上下文計數和 REPL 代理行為。**

發行說明描述了具體的代理腳手架變更和 GLM-5.2 長上下文基準測試效果。

類型: 整合 | 日期: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (作者 [@sydneyrunkle](https://x.com/sydneyrunkle))

**使用此案例嘗試使用開放式編碼代理工具的 GLM-5.2，並在可重現的代理 shell 下比較模型。**

作者報告使用 GLM-5.2 和 DeepAgents 程式碼，並將開放模型和開放線束作為測試模式。

類型: 演示 | 日期: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [生產級行銷 Agent 棧路由策略](https://x.com/DeRonin_/status/2068303752671477820) (作者 [@DeRonin_](https://x.com/DeRonin_))

**用這個案例把 GLM-5.2 路由到重視結構化、速度與自託管的生產 Agent 工作流中，同時把更強的閉源模型留給模糊判斷任務。**

作者在代理機構棧中做了 6 天並行對比後表示，GLM-5.2 在開始漂移前可穩定執行 60 多個 agent 步驟，連續 800 多次匹配結構化格式，並提供低延遲的自託管回應。同一則貼文仍偏好用 Opus 處理語音關鍵或高歧義任務，因此真正有價值的是這條路由規則本身。

類型: 評測 | 日期: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (作者 [@hxiao](https://x.com/hxiao))

**用這個案例評估 GLM-5.2 在長時間本地 coding agent 執行中的表現，追蹤它在 M3 Ultra 上花接近半天重建 Pokemon Red HTML 版本的嘗試。**

作者把 Claude Code 的 model 切到本地 GLM 5.2，並在一台 M3 Ultra 512GB 機器上跑了 12 小時的 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 任務。貼文公開了執行時間、token 用量、code churn、RAM 使用量，以及 GGUF 與 KV-cache 配置，也指出模型品質感覺接近 frontier，但本地推理速度仍是主要瓶頸。

類型: 演示 | 日期: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (作者 [@cline](https://x.com/cline))

**如果你想比較 GLM-5.2 與 Opus 4.8 在真實儲存庫 bug 修復中的表現，可以用這個案例。GLM 雖然用了更多 token，但最後產出的 patch 更便宜也更乾淨。**

Cline 在相同的 harness 與工具條件下，用 Cline 儲存庫中的同一個 bug 測試了兩個模型。貼文指出，GLM 使用約 110 萬 token，Opus 使用 66 萬；成本分別為 0.41 美元與 0.81 美元；耗時則是 4.7 分鐘與 28 次工具呼叫，對比 1.6 分鐘與 12 次工具呼叫。最後 GLM 還清理了 dead code 並成功完成 production build，而 Opus 則留下了雖然測試通過、但仍存在的型別錯誤。

類型: 評測 | 日期: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 Background Agent](https://x.com/colemurray/status/2069485572339707938) (作者 [@colemurray](https://x.com/colemurray))

**如果你想研究自託管的 GLM-5.2 背景 agent 棧，而不是託管聊天工作流，可以用這個案例。**

colemurray 分享了一個由 OpenInspect 與 Modal Inference 組成的完全自託管背景 agent 系統，使用 FP8 版本的 GLM-5.2 執行，並強調速度與對關鍵基礎設施的控制權。原貼內容不長，但清楚點出了工具棧與部署方式。

類型: 整合 | 日期: 2026-06-23

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手演示與作品展示

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (作者 [@aimlapi](https://x.com/aimlapi))

**使用此案例來比較 GLM-5.2 和 Opus 4.8 之間相同提示的遊戲建立輸出、運行時間和成本。**

AI/ML API 報告要求 GLM-5.2 和 Opus 4.8 一次製作一款可玩的 Backrooms 遊戲。他們的貼文稱，GLM-5.2 在 1 分 08 秒內以 0.37 美元的價格構建了更完整的機制，而 Opus 用了 2 分 14 秒以 1.94 美元的價格構建了更完整的機制。

類型: 演示 | 日期: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [三個真實的構建結果參差不齊](https://x.com/bridgemindai/status/2065840871929442319) (作者 [@bridgemindai](https://x.com/bridgemindai))

**將此案例用作警示演示集：在信任用於生產遊戲或視訊任務的模型之前測試多個真實構建。**

BridgeMind 在恐怖屋遊戲、3D 潛行遊戲和 Remotion 行銷影片上測試了 GLM-5.2。這篇文章報告了好壞參半的結果，包括破壞的遊戲邏輯，使其成為有用的接地限制訊號。

類型: 評測 | 日期: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例來評估使用 GLM-5.2 和 ZCode 在多個修復和功能過程中進行的迭代遊戲建置。**

作者透過創建超級瑪利歐風格的克隆來使用 GLM-5.2 測試 ZCode 3.0，然後在問題修復和功能添加五次迭代後分享結果。

類型: 演示 | 日期: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例在互動式遊戲類型任務上比較 GLM-5.2、MiniMax M3 和 Kimi K2.7 代碼。**

這篇文章描述了 MiniMax M3、GLM-5.2 和 Kimi K2.7 Code 之間的月球登陸器競賽，在返回本地模型開發之前使用視訊結果作為實際基準。

類型: 評測 | 日期: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (作者 [@grx_xce](https://x.com/grx_xce))

**使用此案例來檢查 GLM-5.2 可以從競技場上下文中的單一設計提示產生什麼。**

作者在 Design Arena 上分享了一個根據一個提示創建的 GLM-5.2 範例，用它來展示開放權重模型和封閉權重模型之間縮小的差距。

類型: 演示 | 日期: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [研究論文理解工作流程](https://x.com/askalphaxiv/status/2066996976445706745) (作者 [@askalphaxiv](https://x.com/askalphaxiv))

**使用此案例將 GLM-5.2 應用於包含上下文問題和跨論文參考的論文閱讀工作流程。**

AlphaXiv 引入了 GLM-5.2 來理解研究論文，使用者可以突出顯示一個部分、提出問題並參考其他論文以了解上下文、比較和基準參考。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (作者 [@emollick](https://x.com/emollick))

**在將 GLM-5.2 與寓言風格模型進行比較時，使用此案例將正確性與創意品質分開。**

伊森·莫里克 (Ethan Mollick) 稱讚 GLM-5.2 Max 創作了一首正確的受限詩，同時指出《寓言》更有創意地將消失字母約束融入詩歌主題中。

類型: 評測 | 日期: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (作者 [@0xSero](https://x.com/0xSero))

**使用此案例作為輕量級視覺設計訊號，然後使用您自己的提示和 UI 審查進行驗證。**

作者表示他們很喜歡 GLM-5.2 的設計感，並分享了一個視覺範例。它可用作檢查指針，而不是作為生產設計品質的獨立證明。

類型: 演示 | 日期: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 體素遊戲單次生成](https://x.com/pseudokid/status/2068431546143649829) (作者 [@pseudokid](https://x.com/pseudokid))

**用這個案例高壓測試 GLM-5.2 的單提示詞遊戲生成能力，再查看一個視覺元素較多的建置仍需要哪些迭代修正。**

作者表示，首輪提示就生成出大部分 Temple Run 風格的體素摩托遊戲，之後只用少量補充輪次修正鏡頭與移動邏輯。貼文也提到 Z.ai 工具鏈可以生成截圖與實機影片，幫助文字模型評估結果。

類型: 演示 | 日期: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 單次生成案例集](https://x.com/LyalinDotCom/status/2068378281636982990) (作者 [@LyalinDotCom](https://x.com/LyalinDotCom))

**用這個案例在 OpenCode Go 裡快速基準測試 GLM-5.2 的單次生成建置能力，再決定是否投入更開放式的 Agent 迴圈。**

作者展示了一組透過 OpenCode Go 完成的單次生成案例，包括太陽系 Web 應用、系統資訊 Electron 應用，以及一個簡單的探索小島 Web 遊戲。同一則貼文也表示，GLM-5.2 是他用過最強的開源模型，但還沒有把它稱作與最前沿閉源模型完全同級。

類型: 演示 | 日期: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (作者 [@DeryaTR_](https://x.com/DeryaTR_))

**用這個案例測試 GLM-5.2 的單提示詞遊戲生成能力，並觀察少量後續回合如何完成素材替換與輕量打磨。**

作者表示，GLM-5.2 用一個主提示詞就生成了可玩的 Space Invaders 風格遊戲，接著再用三輪後續提示完成 sprite 替換與 leaderboard 等小幅增補。這個公開結果更適合作為輕量遊戲生成樣例，而不是完整 benchmark。

類型: 演示 | 日期: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (作者 [@threepointone](https://x.com/threepointone))

**用這個案例快速原型化互動式 agent failure simulation；作者回報約 3.50 美元就一輪做出了可運作的 recovery lab。**

作者在輸入一份 4,000 字分析與 Agents SDK repository 後，用 OpenCode 搭配 GLM-5.2 建出一個完全可互動的 recovery lab。貼文列出了 176k token 的執行、一輪成型的結果，以及打磨前端到端約 3.50 美元的成本。

類型: 演示 | 日期: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (作者 [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**如果你想測試 GLM-5.2 在參考驅動網站重建上的能力，可以用這個案例。只給一個來源 URL 和一條提示詞，就幾乎像素級重現了網站。**

Open Design 表示，它在內建 AMR 中只用一個參考 URL 與一條簡單提示詞測試了 GLM-5.2，結果在 demo 裡幾乎完美重建了原網站。這個案例更適合作為參考式 UI 生成的實測證據，而不是完整 benchmark。

類型: 演示 | 日期: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**如果你想比較 GLM-5.2 在全端 UI 建構上的表現，可以用這個案例。它做出的交易桌面結果接近最精緻的版本，但成本只占頂尖結果的一小部分。**

Atomic Chat 用同一條即時 Trader Desk 建構提示，比較了四個模型，任務包含前端、後端、8 個交易標的的市場資料，以及自訂深色主題 UI。貼文指出，GLM-5.2 消耗 13,677 token、成本 0.03 美元；Fugu Ultra 則是 22,225 token、成本 0.51 美元。貼文認為，GLM 以遠低得多的成本做出了同樣相當完整、且帶有即時資料的多面板介面。

類型: 評測 | 日期: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Luddite Game After Claude Refusal](https://x.com/atmoio/status/2069559053114577088) (作者 [@atmoio](https://x.com/atmoio))

**如果閉源模型因政策原因拒絕請求，而你又想原型化帶政策敏感性的遊戲概念，可以用這個案例測試 GLM-5.2。**

atmoio 表示，Claude 把一個關於摧毀 AI 的幽默版 Plague Inc 風格遊戲請求判定為違反可接受使用政策，因此作者改用 GLM 5.2 做出了名為 Luddite 的遊戲，並附上了 demo 片段。這個案例更適合被視為創意編碼任務在閉源模型拒絕後的實作替代路徑，最終可玩性仍應自行檢查。

類型: 演示 | 日期: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 供應商與工具整合

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (作者 [@opencode](https://x.com/opencode))

**使用此案例透過文字、1M 上下文和類似 GLM-5.1 的定價來追蹤 OpenCode Go 工作流程中的 GLM-5.2 可用性。**

OpenCode 宣布 GLM-5.2 在 Go 中可用，強調文字支援、1M 上下文視窗以及與 5.1 相同的定價。

類型: 整合 | 日期: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (作者 [@ollama](https://x.com/ollama))

**使用此案例將 GLM-5.2 路由到 Ollama Cloud 中，以進行可存取的開源編碼模型實驗。**

Ollama 宣布推出 GLM-5.2，將其描述為具有 1M 上下文的長視野編碼和代理任務模型。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (作者 [@OpenRouter](https://x.com/OpenRouter))

**在比較提供者路由或多模型堆疊時，使用此案例透過 OpenRouter 存取 GLM-5.2。**

OpenRouter 宣布 GLM-5.2 作為 1M 代幣長期模型可用，為用戶提供了一個與提供者無關的呼叫路徑。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (作者 [@vllm_project](https://x.com/vllm_project))

**使用此案例透過 vLLM 自行託管或提供 GLM-5.2 服務，並提供零日支援。**

vLLM 專案宣佈在 v0.23.0 中支援 GLM-5.2，將其定位為具有 1M 上下文的長視野編碼代理的旗艦模型。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (作者 [@NotionHQ](https://x.com/NotionHQ))

**使用此案例將 GLM-5.2 識別為 Notion 工作流程中可用的開放權重模型。**

Notion 宣布 GLM-5.2 作為開放權重模型推出，專為長期任務而構建，並透過 Baseten 提供服務。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**使用此案例來評估 Fireworks 作為需要託管基礎架構的 GLM-5.2 工作負載的服務路徑。**

Fireworks 在第 0 天宣布推出 GLM-5.2，強調 1M 上下文、編碼優先定位以及在 SWE-Bench、Terminal-Bench、GPQA 和 AIME 上的獨立驗證。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [谷歌雲模型花園鏈接](https://x.com/CarolGLMs/status/2067127223216419088) (作者 [@CarolGLMs](https://x.com/CarolGLMs))

**使用此案例在 Google Cloud 導向的部署和代理平台上下文中尋找 GLM-5.2。**

CarolGLMs 分享了 GLM-5.2 的 Google Cloud 鏈接，使其成為團隊處理雲端模型目錄的直接指針。

類型: 整合 | 日期: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (作者 [@AskVenice](https://x.com/AskVenice))

**當隱私模式、TEE 或端對端加密是嘗試 GLM-5.2 的決定因素時，請使用此案例。**

Venice 宣布 GLM-5.2 在具有 TEE/E2EE 框架的隱私模式下可用，旨在實現私有代理程式碼和長期任務。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**使用此案例嘗試命令代碼中的 GLM-5.2，具有低成本入門計劃和長上下文編碼功能。**

Command Code 宣布 GLM-5.2 可用，並指出 1M 上下文、強大的推理、開源狀態以及透過其一美元 Go 計劃進行存取。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [來自 Nous Portal 的赫爾墨斯特工](https://x.com/Teknium/status/2066954081575592282) (作者 [@Teknium](https://x.com/Teknium))

**使用此案例透過 Nous Portal 和 OpenRouter 將 GLM-5.2 連接到 Hermes Agent 工作流程。**

Teknium 報告了來自 Nous Portal 和 OpenRouter 的 Hermes Agent 中 GLM-5.2 的可用性，這對於代理框架路由實驗非常有用。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (作者 [@ionet](https://x.com/ionet))

**在評估 753B 參數長上下文模型的計算支援服務時使用此案例。**

io.net 宣布自己是 GLM-5.2 的零日發布合作夥伴，強調 1M 上下文、代理優先設計、長視野編碼以及 753B 參數模型的計算需求。

類型: 整合 | 日期: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (作者 [@clattner_llvm](https://x.com/clattner_llvm))

**使用此案例來考慮在提供者規模提供長上下文 GLM-5.2 服務的模組化雲端。**

Chris Lattner 發布稱，GLM-5.2 在第 0 天就在 Modular Cloud 上上線，強調了開放權重、編碼、長視野代理和 1M 上下文。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (作者 [@agentnative_](https://x.com/agentnative_))

**使用此案例透過 OpenRouter 在 Cursor 中設定 GLM-5.2，以實現低成本的開放模型編碼工作流程。**

原始碼給出了具體的 Cursor/OpenRouter 設定路徑，而不僅僅是宣布模型可用性。

類型: 教程 | 日期: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (作者 [@beyang](https://x.com/beyang))

**當純文字模型需要視覺審核支援來完成設計任務時，可以使用此案例將 GLM-5.2 與 Amp 自訂代理程式配對。**

該貼文將 GLM-5.2 視覺設計基準測試結果與可提供審查層的 Amp 插件代理連接起來。

類型: 整合 | 日期: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (作者 [@alphatozeta8148](https://x.com/alphatozeta8148))

**當長上下文服務速度對於 Factory Droid、OpenCode 和編碼工具很重要時，可以使用此案例透過 Baseten 路由 GLM-5.2。**

來源報告 GLM-5.2 在完整的 1M 上下文中運行速度提高了四倍，並在編碼工具中顯示了它。

類型: 整合 | 日期: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [面向網頁設計的 Browser Use QA 子代理](https://x.com/browser_use/status/2068405699340853541) (作者 [@browser_use](https://x.com/browser_use))

**當純文字模型需要視覺檢查與迭代式網站修復時，可用這個案例把 GLM-5.2 與 Browser Use v2 多模態 QA 子代理搭配起來。**

Browser Use 表示，GLM-5.2 在一個網站設計任務中超過了 Fable 5，接著又加入 QA 子代理來檢查結果、判斷美感、找出 bug，並把定向修復建議回傳給 GLM。整套 build 加 QA 的循環據稱成本低於 0.75 美元。

類型: 整合 | 日期: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 官方 IDE 每日免費額度](https://x.com/Alan_Earn/status/2068223665268006924) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**當你想要一個帶大額每日免費 token、互動體驗類似 Cursor 的官方編碼 IDE 時，可用這個案例透過 ZCode 存取 GLM-5.2。**

貼文將 ZCode 描述為智譜官方編碼 IDE，預設模型就是 GLM-5.2，並提供每日 300 萬 token、100 萬上下文視窗，以及 Mac 和 Windows 用戶端。它還包含一段簡短的上手流程，因此比一般的上線公告更具可操作性。

類型: 教程 | 日期: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (作者 [@skirano](https://x.com/skirano))

**用這個案例透過 Fireworks 以最小 OpenAI 相容設定把 GLM-5.2 接入 Cursor，無須撰寫自訂客戶端程式。**

Skirano 展示了最簡 Cursor 設定流程：把 Fireworks key 填進 OpenAI API key 欄位，base URL 使用 `https://api.fireworks.ai/inference/v1`，模型選擇 `accounts/fireworks/models/glm-5p2`，然後重新啟動 Cursor。對想在熟悉的 coding IDE 裡試用 GLM-5.2 的人來說，這是一條相當具體的接入路徑。

類型: 教程 | 日期: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (作者 [@vulcanbench](https://x.com/vulcanbench))

**用這個案例在開放 benchmark harness 中透過一級支援的 ZAI provider 與專用 API key 路徑執行 GLM-5.2。**

VulcanBench v0.2.0 新增了一級支援的 ZAI provider，讓使用者能把 GLM-5.2 作為 `zai:glm-5.2` 與 OpenAI、Anthropic 模型並排執行，並提供獨立的 `ZAI_API_KEY`。如果你要的是開放、可重現的 benchmark harness，而不是單張截圖，這個案例更有用。

類型: 整合 | 日期: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (作者 [@OpenCodeLog](https://x.com/OpenCodeLog))

**用這個案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 變體，同時取得更可靠的 step-limit 處理。**

OpenCode v1.17.9 為 GLM-5.2 新增了 High 與 Max thinking 變體，覆蓋 OpenAI 相容與 Anthropic 相容 provider，並原生支援 OpenRouter 的 effort 映射。相同版本也修正了 agent step-limit 行為，讓這個整合更適合較長的執行。

類型: 整合 | 日期: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**用這個案例把 GLM-5.2 coding plan 流量從通用 API 路徑切到針對 coding 最佳化的 Z.ai endpoint。**

貼文建議，對於 coding plan 工作負載，應優先使用 `https://api.z.ai/api/coding/paas/v4`，而不是通用的 `https://api.z.ai/api/paas/v4/`。作者也補充說，Claude Code、OpenCode 等工具在支援時通常會走 `https://api.z.ai/api/anthropic`。如果你感覺 GLM-5.2 路由不對，這是一條非常具體的設定修正。

類型: 教程 | 日期: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (作者 [@0x_kaize](https://x.com/0x_kaize))

**用這個案例取得免費的 GLM-5.2 API key 與 base URL，再接入 Claude、Cursor、Hermes 等工具。**

作者分享了一條大約五分鐘的設定流程：取得免費的 ZenMux API key 與 base URL，然後把 GLM-5.2 接到 Claude、Cursor、Hermes 等工具上。貼文也提醒免費 tier 很快就會碰到 rate limit，因此它更適合作為 access note，而不是長期穩定性保證。

類型: 教程 | 日期: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (作者 [@_xjdr](https://x.com/_xjdr))

**如果你想把 GLM-5.2 導入 ncode 與 Noumena 風格的 agent 環境，並同時使用標準版與 1M 上下文端點以及預設模型支援，可以用這個案例。**

Noumena 的更新表示，團隊已經在 tool calling、函式解析、app routing 與 reasoning traces 等鏈路上把 GLM 納入一級支援。之後他們又把 API 拆成 `glm-5.2` 與 `glm-5.2[1m]` 兩個端點，用來在 1M 上下文高流量下控制 TTFT。更新也提到，新的 ncode 版本因為使用回饋正面，已把預設的 opus 級模型從 Kimi 改成 GLM。

類型: 整合 | 日期: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (作者 [@thealexker](https://x.com/thealexker))

**如果你想透過 Baseten key、自訂 base URL，以及 `~/.claude/settings.json` 裡的模型映射，在 Claude Code 中執行 GLM-5.2，可以用這個案例。**

這篇教學示範如何安裝 Claude Code、建立 Baseten 帳號、取得 API key，並編輯 `~/.claude/settings.json`，讓三個 Claude 模型層級都透過自訂 Anthropic 環境變數指向 `zai-org/GLM-5.2`。這是一個把 GLM-5.2 作為 Claude Code 用戶端替代模型接入的具體設定模式。

類型: 教學 | 日期: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (作者 [@cramforce](https://x.com/cramforce))

**如果你想在安全 harness 中測試 GLM-5.2，可以用這個案例。`deepsec` 把它設成 Pi agent 的預設模型，並回報了具競爭力的 eval 結果。**

貼文宣布，`deepsec` 已支援 `@badlogicgames` 的 Pi agent，並把 GLM-5.2 設為預設模型，同時提供可直接執行的命令 `pnpm deepsec process --agent pi`。作者也表示自己跑了 Deepsec evals，結果和其他 frontier model 相比也相當有競爭力，因此這是一個很具體的安全導向整合面。

類型: 整合 | 日期: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid Harness Quickstart](https://x.com/RayFernando1337/status/2069523126384525639) (作者 [@RayFernando1337](https://x.com/RayFernando1337))

**如果你想透過 Baseten 與 Droid harness 快速跑通 GLM-5.2，並重用一套也適用於其他 IDE 的短設定流程，可以用這個案例。**

RayFernando1337 給出了一套帶時間戳的教學步驟：取得 Baseten API key、自動化設定 Droid AI、測試 GLM-5.2 整合、查看替代設定與限制，最後再補充其他 IDE 的額外設定說明。

類型: 教學 | 日期: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI-Compatible GLM API Workflow](https://x.com/Marktechpost/status/2069308807570915500) (作者 [@Marktechpost](https://x.com/Marktechpost))

**如果你想在 Python 裡用一個 OpenAI 相容客戶端統一接入 GLM-5.2 的推理控制、tool calling、長上下文檢索與成本統計，可以用這個案例。**

Marktechpost 分享了一篇教學與配套程式碼 notebook，示範如何把 GLM-5.2 封裝進一個 OpenAI 相容客戶端。貼文指出，這套工作流涵蓋 thinking effort 控制（`off`/`high`/`max`）、串流 reasoning 與 answer 通道、帶多步 agent 的 tool calling、結構化 JSON 輸出、長上下文檢索，以及 token 成本追蹤。

類型: 教學 | 日期: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API Search Sandbox](https://x.com/perplexitydevs/status/2069252848647606584) (作者 [@perplexitydevs](https://x.com/perplexitydevs))

**如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，並透過單一 API 呼叫取得帶搜尋能力的沙盒 agent，可以用這個案例。**

Perplexity Devs 宣布在 Agent API 中加入 GLM-5.2，並將其描述為適合長時程 coding 與 agentic workflow 的模型。貼文也特別強調了 Search as Code、OpenAI 相容介面，以及不加價的一方定價。

類型: 整合 | 日期: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (作者 [@aqaderb](https://x.com/aqaderb))

**如果你在意 provider 延遲表現，可以用這個案例查看 Baseten 對 GLM-5.2 高吞吐、低首 token 延遲的公開效能說法。**

aqaderb 宣布 Baseten 的 GLM-5.2 API 可達 280 tokens per second，TTFT 低於 0.8 秒。貼文把結果歸因於 PD disaggregation、結合 multi-token prediction heads 的 speculative decoding、KV-cache-aware routing 等服務優化，並附上一篇工程說明文章。

類型: 整合 | 日期: 2026-06-23

---

<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定價與本地部署

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (作者 [@Hesamation](https://x.com/Hesamation))

**使用此案例將 GLM-5.2 輸出代幣經濟學與 Opus、Fable 和 GPT-5.5 風格的模型進行比較。**

該貼文比較了 100 萬個輸出代幣的價格，並認為 GLM-5.2 比前沿封閉模型便宜得多。將這些數字視為與來源相關的定價比較，應在預算之前重新檢查。

類型: 評測 | 日期: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (作者 [@Jeyffre](https://x.com/Jeyffre))

**使用此案例來推理自託管類似 GLM-5.2 的模型是否可以為重度代理用戶償還硬體成本。**

作者估計多台 DGX Spark 級機器可以運行 700B 級模型，並將大約 2 萬美元的硬體採購與每月用於編碼和代理工作負載的高額 API 支出進行了比較。

類型: 評測 | 日期: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (作者 [@pcuenq](https://x.com/pcuenq))

**使用此案例探索在 Apple 硬體和麵向 MLX 的設定上運行的本機 GLM-5.2。**

該帖子稱 GLM-5.2 剛剛發布，並且已經在兩台 Mac Studio M3 Ultra 機器上與 MLX 一起運行，將其與最近具有開放權重的封閉模型相媲美。

類型: 演示 | 日期: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (作者 [@ai_xiaomu](https://x.com/ai_xiaomu))

**使用此案例作為成本比較提示，用於在訂閱和自託管之間進行選擇之前檢查本地部署假設。**

這篇中文貼文將聲稱的 SWE-Bench 數據、商業開源使用以及估計的單一 H100 本地部署成本與 Claude Pro 訂閱進行了比較。应针对当前基础设施定价重新验证这些数字。

類型: 評測 | 日期: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**使用此案例來檢查圍繞 GLM-5.2 的免費信用和替代代理敘述，同時將行銷聲明與經過驗證的工作負載適合度分開。**

該貼文將 GLM-5.2 描述為 Claude 的低成本競爭對手，具有每日積分、開源控制、自託管以及長時間編碼會話的更大價值。

類型: 評測 | 日期: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (作者 [@0xSero](https://x.com/0xSero))

**在承諾付費提供者或本地部署之前，使用此案例透過免費 ZCode 津貼測試 GLM-5.2。**

作者透過 ZCode 描述了 GLM-5.2 的可用性，並提供了大量免費的每日代幣津貼，並指出了設定 vLLM Studio 或本地託管的可能用途。

類型: 整合 | 日期: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (作者 [@JZiyue_](https://x.com/JZiyue_))

**使用此案例來尋找用於 GLM-5.2 測試的時間限制的自由存取視窗。**

該帖子在 ZenMux 上宣傳 GLM-5.2，提供一周免費窗口、100 萬上下文、編碼和代理改進以及與 5.1 相同的價格定位。

類型: 整合 | 日期: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAI 每代幣定價](https://x.com/nahcrof/status/2067166596523765781) (作者 [@nahcrof](https://x.com/nahcrof))

**在選擇路線之前，使用此案例比較 GLM-5.2 的第三方提供者定價。**

該貼文宣布了 crofAI 上的 GLM-5.2，列出了輸入、輸出和快取價格，將其定位為廉價的前沿智慧。

類型: 整合 | 日期: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (作者 [@scaling01](https://x.com/scaling01))

**將 GLM-5.2 與其他前沿實驗室和開放模型進行比較時，請使用此案例作為市場定價批評。**

作者在輸出代幣定價方面比較了 GLM-5.2 和其他大型開放模型，並透過比較來論證一些前沿實驗室 API 利潤率很高。

類型: 評測 | 日期: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://x.com/volatilemrkts/status/2068077319986516031) (作者 [@volatilemrkts](https://x.com/volatilemrkts))

**在規劃離線編碼設定之前，使用此案例來估計大內存 Apple 硬體上的本地 GLM-5.2 推理吞吐量。**

消息來源報告在本地高內存 Mac 設定上每秒 44.1 個令牌，並提到大量工具調用的解碼重複問題。

類型: 演示 | 日期: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (作者 [@mrblock](https://x.com/mrblock))

**當完整模型權重對於普通本地硬體來說太大時，使用此案例來評估量化的 GLM-5.2 部署路徑。**

這篇文章介紹了 Unsloth 動態 2 位元和 1 位元 GGUF 選項、記憶體減少以及 llama.cpp 或 Unsloth Studio 部署路線。

類型: 教程 | 日期: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**用這個案例估算 GLM-5.2 8-bit 在兩台 M3 Ultra 上進行分散式 MLX 推理時的實際部署表現，再決定是否擴大 Apple Silicon 配置。**

貼文展示了 GLM-5.2 8-bit 在兩台 M3 Ultra 512GB 機器上透過 MLX distributed 執行的情況，速度約 17.9 tokens/sec，總記憶體占用約 760GB。作者也明確說明這仍是一個進行中的 PR，因此它更適合作為 deployment signal，而不是完整部署指南。

類型: 演示 | 日期: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (作者 [@buildwithhassan](https://x.com/buildwithhassan))

**用這個案例透過更低的 ZCode 尖峰與離峰 multiplier，在 9 月前盡量拉長 GLM-5.2 的 plan credits。**

這則貼文表示，ZCode 已把 GLM coding plan multiplier 在尖峰時段從 3x 下調到 2x，在離峰時段從 2x 下調到 0.67x，而且新窗口會持續到 9 月底。對想在 GLM-5.2 上盡量延長 credits 的人來說，這是一個非常具體的 access / pricing note。

類型: 整合 | 日期: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想估算高階本地 GLM-5.2 工作站的規模，可以用這個案例。雙 Blackwell 桌機在 4-bit 量化版本上維持了雙位數 decode 速度。**

CardilloSamuel 表示，他在 2x RTX PRO 6000 Blackwell、Threadripper PRO 9995WX 和 1TB DDR5 的配置上運行了 GLM-5.2 UD-Q4_K_XL。貼文列出的數據包括約 64 tok/s 的 prefill、13-15 tok/s 的 decode、69.7% 的 Aider Polyglot 分數，且與 BF16 僅差 2 分以內。貼文也指出，系統 RAM 頻寬才是真正瓶頸，因此沒有把不匹配的 5090 納入分卡配置。

類型: 演示 | 日期: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (作者 [@karminski3](https://x.com/karminski3))

**如果你想判斷為了本地 GLM-5.2 推論購買 Mac Studio 是否划算，可以用這個案例。貼文中的回本計算明顯更偏向 API 或方案存取。**

貼文估算，一台 32,999 RMB 的 Mac Studio，大致等於按照文中定價購買約 11.78 億個 GLM-5.2 API token。它也主張，即使是更小的 Qwen 本地配置，回本期也大約要 209 天。接著貼文進一步指出，一台 512GB 的 Mac Studio 就算以約 17 tok/s 跑量化版 GLM-5.2，可能也要約 7 年才能回本，因此只有在你已經擁有這台機器，或能有效利用閒置時間時，本地持有才比較合理。

類型: 評測 | 日期: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM Local Outage Save](https://x.com/CardilloSamuel/status/2069431311463236078) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果託管前沿 API 宕機或額度耗盡，而你又要確保交付不中斷，可以用這個案例參考本地部署的 GLM-5.2 搭配 LiteLLM 兜底。**

CardilloSamuel 表示，一位朋友先是用光了 token，又碰上 Claude 宕機，於是他發出一個指向自己本地 GLM-5.2 部署的 LiteLLM API key。貼文指出，對方之後以 0 美元生成了約 500 萬 token，按時完成交付，並接受較慢速度來換取持續可用性。

類型: 演示 | 日期: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [Individual Versus Team Local ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想判斷本地部署 GLM-5.2 更適合個人還是團隊，可以用這個案例做成本與組織規模判斷。**

貼文認為，個人本地方案往往需要 512GB 系統記憶體、多張 GPU 與強 CPU，但速度仍可能只有約 6-10 tokens per second。它進一步指出，對於重視隱私、無限 token、沒有每週上限，以及不受 provider 宕機或政策變化影響的 10 人以上團隊，共享的內部伺服器會更合理。

類型: 評測 | 日期: 2026-06-23

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、注意事項與安全訊號

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (作者 [@sawyerhood](https://x.com/sawyerhood))

**使用此案例請記住，GLM-5.2 對於需要本機視覺功能的工作流程可能不太有用。**

作者引用 Design Arena 排名文章指出，缺乏遠見的 GLM 模型降低了實用性。這是多模式產品規劃的實際警告。

類型: 限制 | 日期: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [現實世界的代理差距警告](https://x.com/ml_angelopoulos/status/2067013545431269405) (作者 [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**使用此案例可以避免過度閱讀基準測試勝利，以證明 GLM-5.2 與所有已部署的代理任務上的最佳專有模型相符。**

作者表示，GLM-5.2 令人印象深刻，但基於 Agent Arena 方法論，在現實世界代理任務的一般分佈上尚未接近寓言級或 Opus 4.8 思維級表現。

類型: 限制 | 日期: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (作者 [@VittoStack](https://x.com/VittoStack))

**使用此案例提醒您在敏感網域中部署 GLM-5.2 之前執行安全性評估。**

該貼文報告了比較安全測試中有害內容拒絕失敗的情況。此儲存庫僅記錄安全訊號，而不記錄不安全的詳細信息，並將其視為部署風險警告。

類型: 限制 | 日期: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [基準方法論批評](https://x.com/josepha_mayo/status/2066951013337112661) (作者 [@josepha_mayo](https://x.com/josepha_mayo))

**即使整體結果有利於 GLM-5.2，也可以使用此案例來質疑基準方法。**

作者批評了 Design Arena 方法，但仍然承認 GLM-5.2 很強大，這對於那些想要對基準懷疑論和排行榜主張的讀者有用。

類型: 限制 | 日期: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (作者 [@k_matsumaru](https://x.com/k_matsumaru))

**在切換編碼計劃或將 Claude 代碼式工作流程路由到 GLM-5.2 之前，使用此案例測試提供程式延遲。**

日本貼文考慮在編碼計劃中使用 GLM-5.2，但指出了先前對高峰時間響應延遲的擔憂。

類型: 限制 | 日期: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (作者 [@nikhilchandak29](https://x.com/nikhilchandak29))

**在廣泛部署之前，使用此案例檢查編碼增益是否推廣到非編碼領域。**

該貼文報告 GLM-5.2 在 FutureSim 上並不比 GLM-5.1 更好，並使用結果來警告編碼改進可能不會在所有領域中同等推廣。

類型: 限制 | 日期: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (作者 [@bridgemindai](https://x.com/bridgemindai))

**使用此案例將模型功能與啟動執行、文件和 API 準備分開。**

這篇文章稱早期版本很混亂，因為當時尚未提供基準測試和 API 訪問，這使得它與發布準備審查相關，而不是模型品質判斷。

類型: 限制 | 日期: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [編碼計劃價格上漲](https://x.com/bridgemindai/status/2065799843658793092) (作者 [@bridgemindai](https://x.com/bridgemindai))

**在推薦 GLM-5.2 作為低成本替代品之前，請使用此案例驗證計劃定價。**

作者報告稱每月支付 65 美元購買 GLM Coding Pro 計劃，並表示該計劃自上次訂閱以來幾乎翻了一番。使用它作為檢查當前定價的提醒。

類型: 限制 | 日期: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [短時間並行工作與長代理運行](https://x.com/thekuchh/status/2068010332501479865) (作者 [@thekuchh](https://x.com/thekuchh))

**使用此案例將 GLM-5.2 路由到短邊界編碼任務，同時為更深的多小時代理運行保留更強的模型。**

這篇文章報告了一個實際的劃分：GLM-5.2 對於短期並行任務效果很好，但在較長的代理運行上會出現偏差。

類型: 限制 | 日期: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [程式碼審查與偏見檢查](https://x.com/wongmjane/status/2068424945663893936) (作者 [@wongmjane](https://x.com/wongmjane))

**用這個案例作為程式碼與政治偏見測試的實務安全訊號，而不是把它當成更廣泛對齊問題已經解決的證明。**

作者稱，GLM-5.2 沒有把中國政治審查內容注入到程式碼中；同時它也糾正了一個關於越南戰爭的錯誤「美國偏見」說法，而對偏意見類問題保持不變。這使它成為測試政治敏感編碼行為與事實性表現的一個具體公開案例。

類型: 限制 | 日期: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高難推理計費異常](https://x.com/s_batzoglou/status/2068297051247350154) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**用這個案例謹慎測試 GLM-5.2 在高難推理負載上的表現，因為公開報告顯示它執行時間長、完成率低，而且計費輸出異常偏高。**

作者執行了 11 個歸納推理題，只回報 4 個完成、2 個答對、多小時級執行時間，以及明顯高於可見 token 數的收費。這是關於推理效率與計費行為的具體警示，不只是 benchmark 分數問題。

類型: 限制 | 日期: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard Multiturn Hallucination Signal](https://x.com/dyfan22/status/2069335764295438532) (作者 [@dyfan22](https://x.com/dyfan22))

**如果你想在信任其他強基準結果前，先測試 GLM-5.2 在多輪幻覺敏感任務上的表現，可以用這個案例。**

HalluHard 在啟用 maximum reasoning effort 的 adaptive thinking 設定下，把 GLM-5.2 加入了排行榜。更新指出，儘管它在其他 benchmark 上成績很強，但在 HalluHard 這種高難多輪 benchmark 上，GLM-5.2 仍然經常出現幻覺。

類型: 限制 | 日期: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Open-Weight Security Emergency Warning](https://x.com/joshua_saxe/status/2069289170107842572) (作者 [@joshua_saxe](https://x.com/joshua_saxe))

**如果你在做安全規劃，可以用這個案例理解開放權重 GLM-5.2 如何降低進攻性安全 agent 的實際操作門檻。**

Joshua Saxe 認為，GLM-5.2 減少了先前對使用前沿 coding agent 的攻擊者構成約束的監控與帳號摩擦。該串把開放權重加私有部署視為進攻能力上的一次顯著變化，並主張防守端應更快採用相應能力，而不是繼續依賴 API 閘門。

類型: 限制 | 日期: 2026-06-23

---


<a id="acknowledge"></a>
## 🙏 致謝

本倉庫來自公開分享 GLM-5.2 使用證據的創作者、開發者、benchmark 團隊、供應商與社群。

感謝這裡收錄的高訊號來源創作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)、[@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)。

*我們無法保證每個案例都已歸屬到最初原創者。如果需要修正，請聯絡我們，我們會更新。*

如果你有更多值得收錄的 GLM-5.2 使用案例，歡迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
