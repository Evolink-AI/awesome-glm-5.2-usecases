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

- **209 個精選 GLM-5.2 案例**，來自公開創作者、評測團隊、工具開發者、服務商與一線使用者。
- 覆蓋基準與前沿評測、編碼代理與長上下文工作流、上手演示與作品展示、供應商與工具整合、成本、定價與本地部署、限制、注意事項與安全訊號。
- 每個案例都包含原始來源、創作者署名、精簡的使用結論、證據類型與發布日期。
- 你可以用這個 repo 尋找實用工作流、比較優勢與限制、探索供應商路徑，並追蹤真實上手實驗。

> [!NOTE]
> 本倉庫重視具體證據，而不是 hype：已發布 demo、benchmark 方法、整合筆記、成本資料與明確 caveat。

> [!NOTE]
> 多語 README 會保持與英文源相同的案例順序、連結、anchor 與署名；為了可追溯性，部分標題會保留接近原文的寫法。

<a id="quick-start"></a>
## ⚡ Quick Start

透過 Evolink 的 OpenAI 相容 Chat Completions API 使用 GLM-5.2。先在 [Evolink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) 取得 API key，然後在執行請求前設定為 `EVOLINK_API_KEY`。

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

閱讀完整 GLM-5.2 API 參考：[開啟 GLM-5.2 API docs](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases).

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [📏 基準與前沿評測](#benchmarks-frontier-evaluation) | 案例 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207 |
| [💻 編碼代理與長上下文工作流](#coding-agents-long-context-workflows) | 案例 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194 |
| [🎮 上手演示與作品展示](#hands-on-demos-showcase-builds) | 案例 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202 |
| [🔌 供應商與工具整合](#provider-tool-integrations) | 案例 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208 |
| [💸 成本、定價與本地部署](#cost-pricing-local-deployment) | 案例 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209 |
| [🧭 限制、注意事項與安全訊號](#limits-caveats-safety-signals) | 案例 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205 |
| [🙏 致謝](#acknowledge) | 來源致謝與修正政策 |

### [📏 基準與前沿評測](#benchmarks-frontier-evaluation)

| 案例 | 展示重點 | 類型 |
|---|---|---|
| [Case 207: Stable Fluids Browser Benchmark](#case-207) | 如果你想比較 GLM-5.2 在高演算法密度的瀏覽器物理 build 上的表現，可以看這個案例，因為 AlicanKiraz0 跑了一個 Stable Fluids HTML benchmark，並給 GLM 5.2 Max 打了 88/100。 | 評估 |
| [Case 199: Epoch Open-Weight Index Lead](#case-199) | 如果你想把 GLM-5.2 放到一條更長期的能力曲線上看，可以看這個案例，因為 Epoch AI 給它的 Capabilities Index 估分是 152，並稱它是自己評估過的 open-weight model 裡最高的。 | 基準 |
| [Case 196: Databricks Internal Harness Eval](#case-196) | 如果你想看 GLM-5.2 在大型私有工程 codebase 上的表現，可以看這個案例，因為 Databricks 說，他們覆蓋 3000 多名工程師工作的內部評估發現 GLM 5.2 表現非常強，而且只靠 harness 選擇不同就能把成本壓到約 2x。 | 評測 |
| [Case 190: NatureBench Open-Weight Runner-Up](#case-190) | 如果你想看 GLM-5.2 在 scientific-agent 工作裡的基準表現，可以看這個案例，因為 NatureBench 說它在 6 個科學領域、90 個任務上首發即總榜第二，並拿到 open-weight 第一。 | 基準 |
| [Case 189: Terminal-Bench 45-Task Cost Tradeoff](#case-189) | 如果你想在同一套 agent harness 下比較 GLM-5.2 和 GPT-5.5，可以看這個案例，因為一組 45 個 Terminal-Bench 任務裡，GLM-5.2 解出 25 個，GPT-5.5 解出 29 個，但前者在 prompt caching 下便宜約 40%。 | 評測 |
| [Case 188: Harvey LAB-AA Legal-Agent Tie](#case-188) | 如果你想看 GLM-5.2 在真實法律 agent 工作裡的基準表現，可以看這個案例，因為 Harvey LAB-AA 顯示 GLM-5.2 Max 在 24 個法律領域、120 個私有任務上拿到 7.5% all-pass，並列 Claude Opus 4.8。 | 基準 |
| [Case 184: AutomationBench-AA Open-Weights Lead](#case-184) | 如果你想比較 GLM-5.2 在必須遵守 business rule 的 SaaS automation 裡的表現，而不只是看 coding benchmark，可以看這個案例，因為 Artificial Analysis 報告 GLM-5.2 Max 在 AutomationBench-AA 上拿到 27.8%，並稱它是 open weights 裡的第一名。 | 評測 |
| [Case 178: Three-Body Simulator Benchmark Win](#case-178) | 如果你想在帶數值物理約束的 coding benchmark 裡比較 GLM-5.2，可以看這個案例，因為 AlicanKiraz0 跑了一個混沌三體模擬器任務，並給 GLM 5.2 Max 打出 91/100 的最高分。 | 評測 |
| [Case 175: Cursor Double Pendulum Scorecard](#case-175) | 如果你想在一個受限的 Cursor coding benchmark 裡比較 GLM-5.2，可以看這個案例，因為 AlicanKiraz0 用 HTML double-pendulum simulator 跑了 6 個模型，給 GLM 5.2 Max 打了 88/100，雖然落後 Fable 和 Sonnet，但仍高於 GPT-5.5、Kimi K2.7 Code 和 Composer。 | 評測 |
| [Case 162: VulcanBench 10-Task 80 Percent Tie](#case-162) | 如果你想在成本和分數同樣重要的 post-cutoff 真實工程任務中比較 GLM-5.2，可以看這個案例，因為 Morgan Linton 說 VulcanBench 讓 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 個 repo 上都拿到 80%，而 GLM 的成本落在中間。 | 評測 |
| [Case 159: SWE-Rebench 51.1 Percent Checkpoint](#case-159) | 如果你想持續跟蹤 GLM-5.2 在 SWE agent 榜單上的位置，可以看這個案例，因為最新一條 SWE rebench 貼文給出的成績是 51.1%，消耗 262 萬 token，明顯高於新加入的 DeepSeek、MiMo、Qwen 和 Gemma。 | 評測 |
| [Case 154: LaunchDarkly Edge-Case Win At 40/41](#case-154) | 如果你想看 GLM-5.2 在企業工具型 agent 任務裡的表現，而不是只看聊天評測，可以用這個案例，因為 Composio 說它在 GitHub、Jira 和 LaunchDarkly 的 41 個任務裡做對了 40 個，而且只有 GLM 抓到了一个待審批邊界條件。 | 評測 |
| [Case 110: AA-Briefcase 每任務耗時前沿](#case-110) | 用這個案例比較 GLM-5.2 在長時程知識工作上的表現，因為除了 benchmark 分數，單任務耗時同樣重要。 | 基準 |
| [Case 111: Code Arena 前端對戰優勢](#case-111) | 用這個案例查看 GLM-5.2 在前端任務上的成對對戰優勢，而不是只看一張排名截圖。 | 基準 |
| [Case 113: SWE Atlas 程式庫問答亞軍](#case-113) | 用這個案例追蹤 GLM-5.2 在程式庫問答、測試撰寫與重構三條 SWE Atlas 榜單上的表現，而不是只看單項 SWE 榜單。 | 基準 |
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
| [Case 194: CuTeDSL Kernel Skill Open Source](#case-194) | 如果你想研究 GLM-5.2 在可重用 kernel 除錯 skill 裡的表現，可以看這個案例，因為作者把一個 CuTeDSL 的 Hermes skill 開源出來，並明確說 GLM-5.2 在除錯和編寫 kernels 時特別省成本。 | 教學 |
| [Case 180: Hermes SSD Recovery Skill Loop](#case-180) | 如果你想在面向修復的 agent loop 裡測試 GLM-5.2，可以看這個案例，因為 ShankhadeepSho1 說 Hermes 加 GLM 5.2 診斷了一塊故障 NAS SSD，修好了問題，然後把修復方案封裝成可重用 skill。 | 示範 |
| [Case 174: Role-Routed Heavy-Duty Coder Stack](#case-174) | 如果你想把 GLM-5.2 放進一套按角色路由的個人 stack，專門承擔較重的 coding 工作，可以看這個案例，因為 denizirgin 表示，在用 Codex 和 OpenCode 測了一個月之後，他把更重的 coding work 交給了 GLM 5.2，同時把總月預算控制在 120 到 140 美元左右。 | 評測 |
| [Case 155: Cotal Four-Agent TUI Loop](#case-155) | 如果你想把一個編碼循環拆給不同專長的 agent，可以看這個案例，因為作者用兩個 GLM-5.2 worker，外加一個 Opus 負責人和一個 GPT reviewer，在 47 分鐘內無人干預地做完了一個 lazygit 風格的完整 TUI。 | 演示 |
| [Case 153: Legacy Migration Cost-Cut Pilot](#case-153) | 如果你想評估 GLM-5.2 在遺留應用改造流程裡能不能當更便宜的執行模型，可以看這個案例，因為 8090 的試點說 GLM 加 Software Factory 相比單跑 Opus 4.8 把成本壓到了 1/16.4，但速度大約慢了 3 倍。 | 評測 |
| [Case 145: OpenCode + Fireworks 降本遷移](#case-145) | 如果你想測試只換 open-model harness 是否已經足夠，可以用這個案例，因為作者把個人 coding 與 loop task 遷到 Fireworks 上的 GLM-5.2 + OpenCode 後，稱 token 成本降到了三分之一，而且日常品質沒有明顯下滑。 | 評測 |
| [Case 143: Hermes MoA 的 GLM 聚合器工作流](#case-143) | 如果你願意為高價值 agent 回合多做一層編排，可以用這個案例，因為 Hermes Agent 的 MoA 設定把 GLM-5.2 和其他模型組合後，在貼文裡的 demo 中用很小的增量成本換來更好的輸出。 | 整合 |
| [Case 142: Cline 推理開關帶來的 Harness 差值](#case-142) | 如果你想判斷決定結果的是 harness 還是權重本身，可以用這個案例，因為同一個 GLM-5.2 在同一批 coding task 上，只是打開 reasoning，結果就從 57.3% 跳到 68.5%。 | 評測 |
| [Case 136: Cursor + Fireworks 4.55 億 Token 實戰測試](#case-136) | 如果你想判斷 GLM-5.2 能否成為 Cursor 的日常主力模型，可以用這個案例，因為作者回報在 Fireworks 服務下真實跑了 4.55 億 tokens，且暫時不想回到 Opus 或 GPT-5.5。 | 評測 |
| [Case 135: Devin Desktop Harness 與 Skill 可攜性](#case-135) | 如果你覺得 Z.ai 自家的 coding 介面不夠穩定，想測試 GLM-5.2 在 Devin Desktop 裡的表現，可以用這個案例，因為作者回報 skill 遷移更容易、速度更快，也更好 hack。 | 評測 |
| [Case 127: Pi 內聯 GLM 審閱者](#case-127) | 如果你想在 Pi 風格的 coding-agent loop 裡加入第二位審閱者，可以用這個案例。作者表示，GLM-5.2 可以逐回合給 Opus 提建議，成本增幅大約只有 10%。 | 整合 |
| [Case 122: AgentRouter 一次成型 Telegram Bot](#case-122) | 如果你想測試 GLM-5.2 在 one-shot coding-agent build 裡，是否能主動補上偏向生產環境的 defaults，而不是只寫出最低限度可運作的路徑，可以用這個案例。 | 演示 |
| [Case 117: OpenCode Go 重構首輪取勝](#case-117) | 用這個案例評估 GLM-5.2 在 OpenCode 中處理中等規模 Go 重構任務的表現，而不是只看 benchmark 宣傳。 | 評測 |
| [Case 119: Claude Code + Cursor 預設執行成本 3.36 美元](#case-119) | 用這個案例判斷 GLM-5.2 是否適合作為 Claude Code 與 Cursor 的日常預設模型，再決定是否把更多自主編碼工作遷移到開放權重模型上。 | 評測 |
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
| [Case 202: Command Code Space Shooter Feature Win](#case-202) | 如果你想看 GLM-5.2 在 one-shot 互動 UI build 裡的表現，可以看這個案例，因為 Command Code 把同一個 retro space-shooter prompt 跑在 Fable 5、GPT 5.5、GLM 5.2 與 DeepSeek V4 Pro 上，並把 GLM 排在 features 第一。 | 評測 |
| [Case 200: ZCode Nintendo DS Emulator](#case-200) | 如果你想看一個長時程、本地執行的 coding build，可以看這個案例，因為作者讓 GLM-5.2 在 4x RTX 6000 的 ZCode 裡，從零開始用 C++ 去做一個 Nintendo DS 模擬器。 | 示範 |
| [Case 192: Command Code Flappy Bird UX Split](#case-192) | 如果你想看 GLM-5.2 在輕量設計類小遊戲任務裡的性價比，可以看這個案例，因為作者用同一個 Flappy Bird prompt 跑了 Command Code，最後認為 Fable 5 雖然價格接近 GLM-5.2 的 9 倍，但在 UX 上並沒有明顯更好。 | 評測 |
| [Case 161: REAP NVFP4 Rubiks Cube One-Shot](#case-161) | 如果你想測試 GLM-5.2 在單一 prompt 的互動式 build 任務上的表現，可以看這個案例，因為 REAP-NVFP4 的 demo 說它只靠一個 prompt 就做出了 3D Rubiks Cube、真實 scramble、即時狀態和 solve 按鈕。 | 演示 |
| [Case 158: OMP Relay iPhone Client](#case-158) | 如果你想把一個本地 GLM-5.2 agent 很快包進移動端介面，可以看這個案例，因為作者說 Codex 的 build-ios-app plugin 只用了幾個小時，就給一個已經接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很強的 iPhone 客戶端。 | 演示 |
| [Case 144: 開源 DevRel 研究 Agent](#case-144) | 如果你想把 GLM-5.2 從通用聊天模型變成垂直研究助手，可以用這個案例，因為作者做了一個開源 DevRel agent，能把產品和受眾輸入轉成帶證據與提綱的選題列表。 | 示範 |
| [Case 123: Recast 六版本落地頁迭代流程](#case-123) | 如果你想先用 GLM-5.2 產出多個版本，再把最佳結果交給 coding agent 繼續做，以低成本試作 landing page，可以用這個案例。 | 教程 |
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
| [Case 208: Open Molecular Viewer Agent Stack](#case-208) | 如果你想把 GLM-5.2 接到一條開放的科學檢視 workflow，可以看這個案例，因為 MaziyarPanahi 把經由 Hugging Face Inference Providers 的 GLM-5.2，和跑在 llama.cpp 上的 Qwen3-VL、Mol*、PydanticAI 串在一起，用單一 prompt 就把 EGFR 加 erlotinib 的結構 render 並做出評論。 | 整合 |
| [Case 204: Perplexity Advisor WANDR Cost Baseline](#case-204) | 如果你想估算 GLM-5.2 在 routing 式 computer-use harness 裡的成本結構，可以看這個案例，因為 Perplexity 說它的 GLM 5.2 加 advisor 配置在 WANDR 上是 2.1x，而 Opus 是 6.1x，整體 benchmark 成本也接近一半。 | 評測 |
| [Case 203: Coworker Open Artifacts Routing](#case-203) | 如果你想把 GLM-5.2 放進企業 artifact 工作流，可以看這個案例，因為 Coworker 說 Open Artifacts 能做 docs、decks、PDF、spreadsheets、dashboards 和 apps，而且 optimized router 能把 token 使用量壓到約 5 分之 1，同時仍提供美國託管的 GLM 5.2。 | 整合 |
| [Case 201: DotCode Context Upload Workflow](#case-201) | 如果你想在私有 coding sandbox 裡給 GLM-5.2 更多專案上下文，可以看這個案例，因為 DotCode 給 GLM 5.2 加上了 screenshot、圖片、CSV、PDF、原始碼檔案和 zip 上傳，並把這些都接進同一條 filesystem + terminal 工作流。 | 整合 |
| [Case 198: Dahl 100M Free GLM Endpoint](#case-198) | 如果你想走一條不用綁卡、又相容 OpenAI 的路徑來試 GLM-5.2，可以看這個案例，因為 Dahl Inference 給 GLM 5.2 FP8 提供了 1 億免費 tokens，並且寫清了如何建 key、如何呼叫 `/v1/chat/completions`。 | 教學 |
| [Case 195: NVIDIA Free Endpoint GLM Setup](#case-195) | 如果你想在不 self-hosting 的情況下把 GLM-5.2 接進 coding tools 裡測試，可以看這個案例，因為原貼文給出了一條免費的 NVIDIA endpoint 路線，直接把 GLM-5.2 的 API key 用到 Claude Code、Cursor 或 Cline。 | 教學 |
| [Case 193: 0G TeeML Private Inference Route](#case-193) | 如果你想把 GLM-5.2 接到一條更重視隱私的 provider 路線上，可以看這個案例，因為 0G 說 GLM 5.2 已經跑在 TeeML 上，prompts 被封裝在 TEE enclave 裡，而且價格低於官方路線。 | 整合 |
| [Case 185: DuckDB Flock Open-SQL PR](#case-185) | 如果你想把 GLM-5.2 帶進完全開源的本地 SQL analysis，可以看這個案例，因為 lhoestq 說，一個 duckdb + flock 的 PR 已經讓 GLM-5.2 進入 100% open-source 的資料堆疊。 | 整合 |
| [Case 179: One-Key 26-Model API Access](#case-179) | 如果你想先透過單一 OpenAI 相容 provider 試用 GLM-5.2，可以看這個案例，因為 Alan_Earn 說一把 API key 就能存取 GLM-5.2 和另外 25 個模型，還附帶 26 美元起始 credits。 | 教學 |
| [Case 176: NVIDIA NIM OpenCode Thinking Setup](#case-176) | 如果你想透過 NVIDIA 免費 NIM endpoint 把 GLM-5.2 接進 OpenCode，並且走一條明確開啟 thinking 的零成本路線，可以看這個案例，因為 Dracoshowumore 分享了 API key 流程、base URL，以及一份由工具層接管 function calls、讓 GLM 以 enable_thinking=true 運行的 OpenCode 設定。 | 教程 |
| [Case 165: ZCode Launch With Mobile Agent Control](#case-165) | 如果你想把 ZCode 當成 GLM-5.2 的官方 coding surface 來評估，可以看這個案例，因為 launch report 說這個免費的 agentic IDE 會上 Windows、macOS、Linux，還能透過 Telegram、WeChat、Feishu 追蹤專案進度。 | 整合 |
| [Case 160: OpenWiki Auto-Maintained Agent Docs](#case-160) | 如果你想讓 agent 可讀的文件自動保持最新，可以看這個案例，因為 LangChain 說 OpenWiki 會隨著程式碼變動重建並維護 repo docs，而且能跑在 GLM 5.2 這類開源模型上。 | 整合 |
| [Case 152: Foundry PTUs Through FireConnect](#case-152) | 如果你想在不重寫 agent 用戶端的前提下，把 GLM-5.2 接到企業級 Foundry 預算裡，可以用這個案例，因為 Fireworks 說 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。 | 整合 |
| [Case 141: ClinePass 開放權重模型統一訂閱](#case-141) | 如果你想把多個開放權重 coding model 收攏到同一個 agent harness 裡，可以用這個案例，因為 ClinePass 把 GLM-5.2 和相關模型打包成統一月費，而不是分別維護 provider key 和帳單。 | 整合 |
| [Case 137: 供 Coding Agents 使用的免費 GLM API 服務](#case-137) | 如果你想在不註冊的情況下，把 GLM-5.2 接入 Hermes 或其他 coding agent，可以用這個案例，因為這個共享服務會發放短時效 API key，整體設定相當輕量。 | 整合 |
| [Case 128: Cloudflare Workers AI OpenCode 設定](#case-128) | 如果你想在不自備模型主機的情況下，透過 Cloudflare Workers AI 這條免費的 OpenAI 相容路線運行 GLM-5.2 做 coding agent，可以用這個案例。 | 教程 |
| [Case 129: Puter.js 零設定瀏覽器客戶端](#case-129) | 如果你想在接觸 API key、帳單或後端設定之前，先用純瀏覽器原型測試 GLM-5.2，可以用這個案例。 | 教程 |
| [Case 130: SiliconFlow 統一端點接入](#case-130) | 如果你想把 GLM-5.2 放進更大的多模型堆疊裡，可以用這個案例，因為貼文描述了一個帶 free trial credit 的單一 OpenAI 相容 SiliconFlow endpoint，同時覆蓋中文和西方模型。 | 整合 |
| [Case 124: HuggingChat 建站到 HF Space 部署](#case-124) | 如果你想在幾乎免費的 personal-site flow 裡試用 GLM-5.2，從 HuggingChat 搜集資料到部署到 Hugging Face Spaces，都可以參考這個案例。 | 教程 |
| [Case 125: DigitalOcean Inference Engine 上線](#case-125) | 如果你想透過 managed infrastructure 取得官方 provider access，而不自己托管 1M context 的模型，可以用這個案例接入 GLM-5.2。 | 整合 |
| [Case 115: Command Code Fast 120-250 Tok/S 檔位](#case-115) | 如果你更在意長時程編碼任務的回應速度，而不只是最低入門價格，可以用這個案例接入更快的 GLM-5.2 檔位。 | 整合 |
| [Case 116: Vercel AI Gateway Fast GLM-5.2 API](#case-116) | 如果你需要 serverless 速度和明確的 token 定價，可以用這個案例透過 Vercel AI Gateway 接入 GLM-5.2 Fast。 | 整合 |
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
| [Case 209: Colibri 25GB RAM Sparse Streaming](#case-209) | 如果你想理解本地 GLM-5.2 實驗的新下限，可以看這個案例，因為 techNmak 詳細說明 Colibrì 如何靠著從 NVMe 串流 experts，用大約 25GB RAM 跑起 744B MoE，不過最小配置只有大約 0.05 到 0.1 tok/s。 | 示範 |
| [Case 206: SGLang NVFP4 Production Throughput](#case-206) | 如果你想估算 GLM-5.2 NVFP4 的正式 SGLang serving 規模，可以看這個案例，因為官方 SGLang v0.5.15 release 說在 batch size 1 下，8x B300 可達每位使用者 500+ tok/s，4x GB300 可達 450 tok/s。 | 評估 |
| [Case 191: Hermes-Built LiteLLM Local Lab](#case-191) | 如果你想把 GLM-5.2 當作 coding agent 來搭一個本地 inference lab，可以看這個案例，因為原貼文說 Hermes Agent + GLM-5.2 把 LiteLLM、Postgres、Prometheus 和 Grafana 都接在了一套 M3 Ultra 環境上。 | 整合 |
| [Case 187: Dual M5 Max Offline Droneship Sim](#case-187) | 如果你想估算一套完全離線的 Apple Silicon GLM-5.2 agent 到底能做什麼，可以看這個案例，因為 XavierLocalAI 報告了一個 753B 配置：在兩台 128GB M5 Max 上以 26 tok/s 編寫 droneship landing simulator。 | 示範 |
| [Case 186: 5x DGX Spark Production Harness](#case-186) | 如果你想判斷 5 節點 DGX Spark 配置是否已經足夠支撐 production 級 GLM-5.2 工作，可以看這個案例，因為 thatcofffeeguy 報告了在 400K context 下單流約 13.9 tok/s，以及 3 條 lane 合計 19.9 tok/s 的 live harness 結果。 | 示範 |
| [Case 183: M3 Ultra ds4-eval Q4 Checkpoint](#case-183) | 如果你想用 ds4-eval 真正 benchmark 一台 Apple Silicon 單機上的 GLM-5.2，可以看這個案例，因為 ivanfioravanti 報告了一次 q4 運行：M3 Ultra 512GB 機器上約 16 tok/s，92 項裡過了 76 項，總時長 8 小時 53 分。 | 評測 |
| [Case 182: 4x RTX PRO 6000 Build Guide](#case-182) | 如果你想評估一套嚴肅的本地 GLM-5.2-594B 方案，可以看這個案例，因為 QingQ77 分享了一份完整的硬體與運維指南，核心是 4 張 RTX PRO 6000、透過 opencode 暴露的 API，以及給 agent 用的 sandbox VM。 | 教學 |
| [Case 181: 4x DGX Spark QuantTrio Run](#case-181) | 如果你想估算 4 節點 DGX Spark 叢集跑 GLM-5.2 QuantTrio 的上限，可以看這個案例，因為 Tech2Wild 給出了 200K context、單流 30 tok/s，以及 6 並發下總計 60.5 tok/s 的結果。 | 示範 |
| [Case 177: Single M3 Ultra 4-Bit Video Run](#case-177) | 如果你想估算 GLM-5.2 在 Apple Silicon 單機上的可行性，可以看這個案例，因為 ivanfioravanti 展示了在一台 M3 Ultra 512GB 機器上以約 16 tok/s 跑 4-bit 版本，並拿它和約 17 tok/s 的 q2 ds4-eval 影片做比較。 | 演示 |
| [Case 166: Full 744B On 5x ASUS GX10s](#case-166) | 如果你想估一個極端 home-lab GLM-5.2 部署的規模，可以看這個案例，因為作者說完整 744B 模型已經能在 5 台 ASUS GX10 上帶 full context 跑起來，而且已接到處理真實 workload 的 causal harness。 | 演示 |
| [Case 164: Agent Route Swap In China Stack](#case-164) | 如果你在乎的是成本壓力而不是絕對最高品質，想把 GLM-5.2 放進 mixed-model stack 的 agent 層，可以看這個案例，因為作者說把 Sonnet 換成 GLM-5.2 之後，這個 slot 的輸入成本降到五分之一，品質大約只掉了 3%。 | 評測 |
| [Case 156: 744B Local Hardware Floor](#case-156) | 如果你想更現實地評估 GLM-5.2 的本地部署門檻，可以看這個案例，因為原帖說即便量化後，2bit 也大約要 239GB、4bit 大約要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比較實際的起步線。 | 限制 |
| [Case 140: B300 x2 Agent 主導雙棧 Bring-Up](#case-140) | 如果你想評估一套嚴肅的自託管 GLM-5.2 部署範圍，可以用這個案例，因為整個 thread 展示了分析 agent 在不到一天內，於裸機 B300 上同時跑起 vLLM 與 SGLang 的 NVFP4 推理。 | 評測 |
| [Case 139: oMLX M3 Ultra Prefill 加速](#case-139) | 如果你想在最近的 kernel 更新後重新檢查 Apple Silicon 本地跑 GLM-5.2 的可行性，可以用這個案例，因為回報中的 M3 Ultra 512GB prefill 速度幾乎翻倍，而且快速測試裡沒有明顯品質崩塌。 | 評測 |
| [Case 138: 註冊即送 2000 萬 Token 額度爆發](#case-138) | 如果你想評估直接註冊拿到的免費額度，是否足夠支撐一次真正的 GLM-5.2 試用，可以用這個案例，因為貼文聲稱新帳號可拿到 2000 萬免費 tokens、免綁卡，並提供完整 OpenAI 相容接入。 | 整合 |
| [Case 131: 4x DGX Spark 本地 GLM 操作手冊](#case-131) | 如果你想判斷 DGX Spark 叢集是否是現實可行的本地 GLM-5.2 路線，可以用這個案例。整理出來的指南把具體硬體成本、叢集拓撲和 vLLM 命令都對應到了 1M context 的 GLM 目標上。 | 教程 |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 跑分](#case-112) | 如果你在評估高階本地工作站方案，可以用這個案例把四卡 GLM-5.2 配置放到高難終端 benchmark 裡衡量。 | 評測 |
| [Case 118: 2x RTX PRO 6000 Blackwell 本地 Crackme 解題](#case-118) | 如果你想判斷嚴肅的本地 GLM-5.2 配置能否在沒有 debugger 的情況下完成長時逆向任務，可以用這個案例。 | 演示 |
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
| [Case 205: Static HTML Rewrite Executor Misses](#case-205) | 如果你不想把 1:1 legacy rewrite 完全交給 GLM-5.2 當 executor，可以看這個案例，因為一個大型 static HTML 到 React/Vite 的遷移在 OpenCode Go 和 Cline 上仍掉了太多細節，讓作者更傾向把 GLM 當 planner 而不是 executor。 | 限制 |
| [Case 197: Composio 47-Task Agent Gaps](#case-197) | 如果你想看 GLM-5.2 在真實 SaaS agent 工作裡還會在哪裡出錯，可以看這個案例，因為 Composio 把它接到 17 個工具、47 個任務上後，只通過了 45 個，主要失誤點在完整性檢查和模糊 SLA 判斷。 | 評測 |
| [Case 163: Preliminary Cyber Research Parity](#case-163) | 如果你想衡量 GLM-5.2 在漏洞研究子任務上的能力，可以看這個案例，因為 Irregular 報告說，在一組範圍很窄的 cyber suite 上，它的早期內部評估可與 GPT-5.4 和 Opus 4.6 接近，同時也明確提醒 end-to-end 攻擊情境尚未測試。 | 限制 |
| [Case 157: OpenRouter Spend-Cut Skill Rewrite](#case-157) | 如果你想在切換 agent 模型前把遷移成本算清楚，可以看這個案例，因為某個基金團隊的 OpenRouter 試驗裡，GLM-5.2 的成本大約只有 Opus 的八分之一，但依然要重寫 skill、補 routing 邏輯，還得接受更慢、更弱一些的輸出。 | 限制 |
| [Case 134: Semgrep IDOR 狹義勝出提醒](#case-134) | 如果你想把真正的安全訊號和誇大的標題敘事分開來看，可以用這個案例，因為來源指出 GLM-5.2 只是在一個 IDOR benchmark 上贏過 Claude Code，並沒有直接對上 Mythos。 | 限制 |
| [Case 132: LisanBench 推理效率差距](#case-132) | 如果你想先檢查 GLM-5.2 在高推理負載任務上的表現，再決定是否把編碼優勢外推到其他場景，可以用這個案例。貼文裡的 LisanBench 結果顯示它雖然比 GLM-5 好，但相較其他開源模型仍然不夠高效。 | 限制 |
| [Case 133: PrinzBench 領域錯配提醒](#case-133) | 如果你想讓 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用這個案例，因為貼文把它較弱的 PrinzBench 分數和更強的軟體、工具使用 benchmark 做了對照。 | 限制 |
| [Case 126: Rust 錯誤修復通過但回合數高 7 倍](#case-126) | 如果你想把 GLM-5.2 的程式碼品質優勢和目前 agent harness 開銷區分開來看，可以用這個案例，因為它雖然能修好 bug，卻可能比 Opus 消耗得多得多的回合數。 | 評測 |
| [Case 114: Braintrust 模型替換成本警示](#case-114) | 用這個案例避免想當然地認為，在真實 agentic coding workflow 裡把模型換成更便宜的選項後，品質還能維持不變。 | 評測 |
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
---
<a id="case-207"></a>
### Case 207: [Stable Fluids Browser Benchmark](https://x.com/AlicanKiraz0/status/2075639232169705781) (作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在演算法負載很重的瀏覽器物理 build 上比較 GLM-5.2，可以看這個案例，因為 AlicanKiraz0 跑了一個 Stable Fluids HTML benchmark，給 GLM 5.2 Max 打了 88/100、成本約 1.17 美元，高於 Opus 4.8 與 Fable 5，但仍低於 GPT 5.6 Sol。**

這個 benchmark 要求每個模型交付一個單檔、self-contained 的 HTML，實作 Jos Stam stable fluids，並包含 semi-Lagrangian advection、iterative diffusion、pressure projection、即時 divergence 回報，以及互動式 paint 與 velocity injection。AlicanKiraz0 表示，GLM 5.2 Max 拿到 88/100，高於 Opus 4.8 的 86 分與 Fable 5 的 81 分，而且成本明顯更低，因此這更像是一條檢驗數值正確性與即時瀏覽器效能的 engineering-style 評測，而不是只看審美的 frontend 比較。

類型: 評測 | 日期: 2026-07-10

<a id="case-199"></a>
### Case 199: [Epoch Open-Weight Index Lead](https://x.com/EpochAIResearch/status/2074894535558300103) (作者 [@EpochAIResearch](https://x.com/EpochAIResearch))

**如果你想把 GLM-5.2 放到一條更長期的能力曲線上看，可以看這個案例，因為 Epoch AI 給它的 Capabilities Index 估分是 152，並稱它是自己評估過的 open-weight model 裡最高的。**

Epoch AI 說，GLM-5.2 在 Epoch Capabilities Index 上拿到了估算 152 分，而且這是他們評估過的 open-weight model 裡最高的分數。所以當你需要一個更總覽的能力定位訊號，而不只是狹義 coding 榜單時，這則貼文就很適合作為 benchmark 參考。

類型: 基準 | 日期: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Databricks Internal Harness Eval](https://x.com/alighodsi/status/2074996561306955958) (作者 [@alighodsi](https://x.com/alighodsi))

**如果你想看 GLM-5.2 在大型私有工程 codebase 上的表現，可以看這個案例，因為 Databricks 說，他們覆蓋 3000 多名工程師工作的內部評估發現 GLM 5.2 表現非常強，而且只靠 harness 選擇不同就能把成本壓到約 2x。**

Ali Ghodsi 說，Databricks 在自家任務、codebase 和基礎設施上做了一次全面評估，覆蓋 3000 多名 software engineer、三家 hyperscaler cloud，以及很多程式語言。貼文裡說 GLM 5.2 表現非常好，而且同一個 model 只要選對 harness，成本就能大約降低 2x，同時前面還用了 Omnigent 依任務去複用不同 model 和 harness。

類型: 評測 | 日期: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [NatureBench Open-Weight Runner-Up](https://x.com/OkhayIea/status/2074498200262889837) (作者 [@OkhayIea](https://x.com/OkhayIea))

**如果你想看 GLM-5.2 在 scientific-agent 工作裡的基準表現，可以看這個案例，因為 NatureBench 說它在 6 個科學領域、90 個任務上首發即總榜第二，並拿到 open-weight 第一。**

NatureBench 要回答的問題是：一個 coding agent 在不使用 web search 的情況下，能不能找到一個方法，超過真實 Nature 系論文裡公開發表的 SOTA。這個 benchmark 涵蓋 6 個科學領域、90 個任務。更新裡說，GLM-5.2 首發即排在 Claude Opus 4.7 之後的總榜第二，同時成為 open-weight 陣營第一，所以這是一條很具體的 scientific-agent workflow benchmark，而不只是普通 code generation 訊號。

類型: 基準 | 日期: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [Terminal-Bench 45-Task Cost Tradeoff](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (作者 [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**如果你想在同一套 agent harness 下比較 GLM-5.2 和 GPT-5.5，可以看這個案例，因為一組 45 個 Terminal-Bench 任務裡，GLM-5.2 解出 25 個，GPT-5.5 解出 29 個，但前者在 prompt caching 下便宜約 40%。**

這則 benchmark 貼文說，團隊用同一個 agent、同一套 prompts、同一套評測設定和同一個 harness 跑了 GPT-5.5 與 GLM-5.2，唯一變動的只有 model。GLM 解出 45 個任務中的 25 個，GPT-5.5 解出 29 個，但在 prompt caching 條件下，GLM 的成本大約低 40%。所以這是一條很具體的價格與成功率對照，而不是模糊的 workflow 偏好。

類型: 評測 | 日期: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Harvey LAB-AA Legal-Agent Tie](https://x.com/ArtificialAnlys/status/2074541975186165887) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想看 GLM-5.2 在真實法律 agent 工作裡的基準表現，可以看這個案例，因為 Harvey LAB-AA 顯示 GLM-5.2 Max 在 24 個法律領域、120 個私有任務上拿到 7.5% all-pass，並列 Claude Opus 4.8。**

Artificial Analysis 說，Harvey LAB-AA 用 24 個法律 practice area 的 120 個 private task 來評估真實法律工作，並以二元 rubric 打分。首發結果裡，GLM-5.2 Max 拿到 7.5% all-pass 和 91.0% criteria-pass，與 Claude Opus 4.8 並列，同時單任務成本大約只有 Claude Fable 5 的 6%。所以這既是一個 frontier 領域 benchmark，也是一條成本效率訊號。

類型: 基準 | 日期: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [AutomationBench-AA Open-Weights Lead](https://x.com/ArtificialAnlys/status/2074194764510208230) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想比較 GLM-5.2 在必須遵守 business rule 的 SaaS automation 裡的表現，而不只是看 coding benchmark，可以看這個案例，因為 Artificial Analysis 報告 GLM-5.2 Max 在 AutomationBench-AA 上拿到 27.8%，並稱它是 open weights 裡的第一名。**

Artificial Analysis 說，AutomationBench-AA 會在 40 個模擬 SaaS app 上跑 657 個 private workflow task，並用接近 12,000 條 objective 與 guardrail assertions 來評分。首發貼文裡，GLM-5.2 Max 以 27.8% 領先 open weights，但同時也明確指出，它仍然落後於更強的 closed models，而且每個 task 的 guardrail violation 明顯更高。所以這條案例既是 agentic business automation 的能力訊號，也是限制訊號。

類型: 評測 | 日期: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [Three-Body Simulator Benchmark Win](https://x.com/AlicanKiraz0/status/2073823792543998170) (作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在帶數值物理約束的 coding benchmark 裡比較 GLM-5.2，可以看這個案例，因為 AlicanKiraz0 跑了一個混沌三體模擬器任務，並給 GLM 5.2 Max 打出 91/100 的最高分。**

這個 benchmark 同時要求三體物理、真正的 RK4、近距離遭遇穩定性、守恆量即時圖表與互動控制。貼文說 GLM 5.2 Max 靠 Float64Array state、可重用 RK4 buffer、Plummer softening 與 adaptive substep 脫穎而出，所以它是一條很具體的工程品質評測，而不只是排行榜截圖。

類型: 評測 | 日期: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [GameDevBench 333-Task Open-Source Lead](https://x.com/iamwaynechi/status/2073081777091182633) (作者 [@iamwaynechi](https://x.com/iamwaynechi))

**如果你想在 agentic 遊戲開發 benchmark 裡追蹤 GLM-5.2，可以看這個案例，因為 GameDevBench 已擴充到 333 個任務，並表示即使沒有 vision，GLM-5.2 仍是排行榜上最強的 open-source model。**

iamwaynechi 表示，GameDevBench 的任務數量已增至 333，論文也同步更新，並把 GLM-5.2 與 Opus 4.8 加入排行榜。貼文指出，Opus 以小幅差距領先整體排名，而 GLM-5.2 則是最強的 open-source model，因此這不只是文字 coding 的訊號，也是一個實用的遊戲建構型 workflow benchmark 觀察點。

類型: 評測 | 日期: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [Cursor Double Pendulum Scorecard](https://x.com/AlicanKiraz0/status/2073386918813778143) (作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在一個受限的 Cursor coding benchmark 裡比較 GLM-5.2，可以看這個案例，因為 AlicanKiraz0 用 HTML double-pendulum simulator 跑了 6 個模型，給 GLM 5.2 Max 打了 88/100，雖然落後 Fable 和 Sonnet，但仍高於 GPT-5.5、Kimi K2.7 Code 和 Composer。**

AlicanKiraz0 在 Cursor 裡用一個 HTML double-pendulum simulator 任務比較了 6 個模型，並公開了總分與各模型的具體弱點。帖文把 GLM 5.2 Max 描述為在視覺表現和教學性上都不錯，但在 performance architecture 上不如 Fable 和 Sonnet 精緻，例如 RK4 wrapper 有額外 allocation 風險，trail buffer 在 resize 時的處理也不夠穩健。這讓它成為一條具體的 comparative evaluation，而不是模糊的主觀喜好判斷。

類型: 評測 | 日期: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10-Task 80 Percent Tie](https://x.com/morganlinton/status/2072689409011679642) (作者 [@morganlinton](https://x.com/morganlinton))

**如果你想在成本和分數同樣重要的 post-cutoff 真實工程任務中比較 GLM-5.2，可以看這個案例，因為 Morgan Linton 說 VulcanBench 讓 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 個 repo 上都拿到 80%，而 GLM 的成本落在中間。**

Morgan Linton 說，這個 benchmark 用了來自 Flask、aiohttp、sqlglot 等專案的 10 個真實工程任務，而且都被描述為 post-training-cutoff。Fable 5 Low、GLM 5.2 High 和 Sonnet 5 High 都拿到 80%，對應成本分別是 2.27、8.41、15.81 美元。這讓它成為一個很有用的三方價格與品質檢查點。

類型: 評測 | 日期: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-Rebench 51.1 Percent Checkpoint](https://x.com/ibragim_bad/status/2072318238407483593) (作者 [@ibragim_bad](https://x.com/ibragim_bad))

**如果你想持續跟蹤 GLM-5.2 在 SWE agent 榜單上的位置，可以看這個案例，因為最新一條 SWE rebench 貼文給出的成績是 51.1%，消耗 262 萬 token，明顯高於新加入的 DeepSeek、MiMo、Qwen 和 Gemma。**

ibragim_bad 說，這次 SWE rebench 更新把 GLM-5.2 和幾款新的開源模型一起加進來了。貼文裡的數字顯示，GLM 用 262 萬 token 跑到 51.1%，而 DeepSeek V4 Pro 是 42.7%，MiMo V2.5 Pro 是 42.4%，Qwen 和 Gemma 更低，因此它是一個很具體的公開榜單檢查點。

類型: 評測 | 日期: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case Win At 40/41](https://x.com/composio/status/2072355937415827950) (作者 [@composio](https://x.com/composio))

**如果你想看 GLM-5.2 在企業工具型 agent 任務裡的表現，而不是只看聊天評測，可以用這個案例，因為 Composio 說它在 GitHub、Jira 和 LaunchDarkly 的 41 個任務裡做對了 40 個，而且只有 GLM 抓到了一个待審批邊界條件。**

Composio 把 GLM-5.2、Claude Opus 4.8 和 GPT-5.5 放到 41 個真實工具型 agent 任務裡對比，這些任務會用到 GitHub、Jira 和 LaunchDarkly。GLM 做對了 40 個，Opus 和 GPT 都是 39 個。其中一個 LaunchDarkly 任務裡，GLM 會先檢查待審批項，再判斷某個 flag 是否 stale，而另外兩個模型只看開關狀態就停了。

類型: 評測 | 日期: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench Open-Weight Patch Runner-Up](https://x.com/ValsAI/status/2072099011398627639) (作者 [@ValsAI](https://x.com/ValsAI))

**如果你想衡量 GLM-5.2 在偏攻防式漏洞發現與補丁生成上的能力，可以用這個案例，因為 CyberBench 把它放在 60 個真實 OSS-Fuzz 漏洞上的總榜第二。**

ValsAI 解釋說，CyberBench 同時考察兩個任務：提交一個只會打崩漏洞版本的 PoC，以及在不破壞行為的前提下修補原始碼。貼文稱，在 60 個來自 OSS-Fuzz 的記憶體安全漏洞上，GPT-5.5 總體第一，而 GLM 5.2 是表現最強的 open-weight 之一。

類型: 評測 | 日期: 2026-06-30

---

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

<a id="case-120"></a>
### Case 120: [PostTrainBench 可靠性領先](https://x.com/hrdkbhatnagar/status/2070244540108423427) (作者 [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**如果你想比較 GLM-5.2 Max，不只看 headline 分數，也看它在 84 個任務上 failed run 為 0 的 agent reliability，可以用這個案例。**

hrdkbhatnagar 分享了一張 PostTrainBench leaderboard，顯示 GLM 5.2 Max reasoning 以 34.29% 略高於 Opus 4.8 Max 的 34.08%。同一則貼文也指出，GLM 在 84 次 runs 中 failed run 為 0，而 Opus agents 的 failure rate 大約在 10% 左右。對於既在意 raw pass rate、也在意 agent reliability 的團隊來說，這是一個很有價值的 benchmark。

類型: 基準 | 日期: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211 項儲存庫任務評測](https://x.com/FireworksAI_HQ/status/2070181898962534570) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在 private repo 的真實 engineering task 上評估 GLM-5.2，而不是只看公開 benchmark，可以用這個案例；貼文同時給出了分數、速度與每任務成本。**

Fireworks 表示，他們與 Faros 共同進行的 211 項真實 engineering task 評測中，Claude Code + GLM-5.2 同時勝過 Claude Code + Opus 4.8 與 Codex + GPT-5.5。貼文給出的數字是 judge score 0.568 對 0.521 / 0.466、每任務 321 秒 對 775 / 392，以及每任務 0.92 美元 對 1.76 / 2.06，並特別說明 Faros 使用的是自家 repositories 與真實工作，而不只是公開 benchmark。

類型: 評測 | 日期: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase 每任務耗時前沿](https://x.com/ArtificialAnlys/status/2069914443639635978) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用這個案例比較 GLM-5.2 在長時程知識工作上的表現，因為除了 benchmark 分數，單任務耗時同樣重要。**

Artificial Analysis 表示，GLM-5.2 位於 AA-Briefcase 的 Pareto 前沿，得分為 1261，單任務平均耗時 16.3 分鐘，分數高於 1159 的 GPT-5.5 xhigh，同時仍是該 benchmark 中表現最強的開放權重模型。對於要同時比較長時程交付品質與執行時長的團隊來說，這個案例比單看排行榜名次更有參考價值。

類型: 基準 | 日期: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena 前端對戰優勢](https://x.com/arena/status/2069885722333769963) (作者 [@arena](https://x.com/arena))

**用這個案例查看 GLM-5.2 在前端任務上的成對對戰優勢，而不是只看一張排名截圖。**

arena 拆解了 GLM-5.2 Max 為什麼能登上 Code Arena: Frontend 榜首，稱它在除一組之外的所有對戰配對裡都拿到了更高勝率。貼文點名了它對 Kimi-K2.6 的 61.0%、對 Sonnet 4.6 的 59.4%、對 Opus 4.7 Thinking 的 55.0%，以及對 GPT-5.5 xHigh 的 41.7% 對 40.0% 險勝，並提到它與 GLM-5.1 直接打成 45.5% 平手。

類型: 基準 | 日期: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas 程式庫問答亞軍](https://x.com/ScaleAILabs/status/2069864932913631617) (作者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**用這個案例追蹤 GLM-5.2 在程式庫問答、測試撰寫與重構三條 SWE Atlas 榜單上的表現，而不是只看單項 SWE 榜單。**

Scale AI Labs 表示，GLM 5.2 已經上線 SWE Atlas 的三條榜單：Codebase QnA、Test Writing 與 Refactoring。貼文特別提到它在 Codebase QnA 上拿到第 2 名，並把這一結果描述為開放模型已經能在這些任務上全面逼近前沿閉源系統。

類型: 基準 | 日期: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 編碼代理與長上下文工作流
<a id="case-168"></a>
### Case 168: [Synthwave Hard-Slice Ensemble At $2.66](https://x.com/TracNetwork/status/2073038214592360522) (作者 [@TracNetwork](https://x.com/TracNetwork))

**如果你想把 GLM-5.2 放進多模型 coding ensemble，而不是單獨使用，可以看這個案例，因為 TracNetwork 表示一個含 GLM 的 Synthwave 組合在 LiveCodeBench hard 上以約 2.66 美元拿到 46.3%，並超過每個單獨 generator。**

TracNetwork 表示，他們透過 OpenRouter 建立了一個 Synthwave ensemble，用 qwen3-coder-next 當 synthesizer，並以 GLM-5.2、qwen3.5-122b、qwen3-coder-next 作為 coding generator。在 82 個 LiveCodeBench hard 任務上，貼文報告成績為 46.3%，成本約 2.66 美元，且沒有任何單一 generator 能單獨達到這個分數。這是一個具體例子，說明 GLM-5.2 適合作為成本導向 ensemble 的一員，而不一定要當唯一的 coding model。

類型: 整合 | 日期: 2026-07-03

---

<a id="case-194"></a>
### Case 194: [CuTeDSL Kernel Skill Open Source](https://x.com/SubhoGhosh02/status/2074466050557739469) (作者 [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**如果你想研究 GLM-5.2 在可重用 kernel 除錯 skill 裡的表現，可以看這個案例，因為作者把一個 CuTeDSL 的 Hermes skill 開源出來，並明確說 GLM-5.2 在除錯和編寫 kernels 時特別省成本。**

貼文說，這個 skill 的大部分內容，是透過 Hermes 裡跨多個 model 的 agentic conversations 建立起來的，而 GLM-5.2 在 kernel debugging 和 kernel writing 過程中特別展現了成本效率。原貼文還給出了精確的安裝與啟動命令：`hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` 與 `hermes chat -s cutedsl-kernels`，所以這不是一句模糊推薦，而是一條可重用的 tutorial-style workflow。

類型: 教學 | 日期: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Hermes SSD Recovery Skill Loop](https://x.com/ShankhadeepSho1/status/2073658918937473444) (作者 [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**如果你想在面向修復的 agent loop 裡測試 GLM-5.2，可以看這個案例，因為 ShankhadeepSho1 說 Hermes 加 GLM 5.2 診斷了一塊故障 NAS SSD，修好了問題，然後把修復方案封裝成可重用 skill。**

作者說，一塊 QNAP NAS 的 SSD 壞了，他把它接到一台備用機器上，然後交給 Hermes 做診斷。這個結果很具體：貼文稱這套 stack 修好了問題，之後還替自己生成了一個 skill，並把恢復策略寫進 infrastructure wiki。

類型: 示範 | 日期: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [Role-Routed Heavy-Duty Coder Stack](https://x.com/denizirgin/status/2073462071639876004) (作者 [@denizirgin](https://x.com/denizirgin))

**如果你想把 GLM-5.2 放進一套按角色路由的個人 stack，專門承擔較重的 coding 工作，可以看這個案例，因為 denizirgin 表示，在用 Codex 和 OpenCode 測了一個月之後，他把更重的 coding work 交給了 GLM 5.2，同時把總月預算控制在 120 到 140 美元左右。**

denizirgin 表示，他目前的個人配置把 Codex、OpenCode、DeepSeek、OpenRouter，以及一套用來判斷 coding、review、research、speed、cost 的自製 sub-agent skill 和 decision table 組在一起。在這個 routing 方案裡，GLM 5.2 透過補充 provider 承擔 heavy-duty coder 的角色，Codex 保留為 main backbone，而 OpenRouter 則更偏向拿來做模型試驗。這使它成為一條來自一線使用者的成本敏感 workflow 筆記，而不是泛泛的模型排名。

類型: 評測 | 日期: 2026-07-04

<a id="case-155"></a>
### Case 155: [Cotal Four-Agent TUI Loop](https://x.com/silvanrec/status/2072335315822403656) (作者 [@silvanrec](https://x.com/silvanrec))

**如果你想把一個編碼循環拆給不同專長的 agent，可以看這個案例，因為作者用兩個 GLM-5.2 worker，外加一個 Opus 負責人和一個 GPT reviewer，在 47 分鐘內無人干預地做完了一個 lazygit 風格的完整 TUI。**

silvanrec 說，Cotal 協調了四個模型：兩個 GLM-5.2 實例分別做前端和後端開發，GPT-5.5 在背景做 reviewer，Claude Opus 負責領導整個 loop。系統從一個做出真實 TUI 控制台的單一 prompt 出發，跑了四輪，找出了渲染和 tab wiring 的 bug，管理了 agent 之間的 handoff，最後在 47 分鐘內產出了可運行結果。貼文還給出了 open source 層的入口：npx cotal-ai setup --full。

類型: 演示 | 日期: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Legacy Migration Cost-Cut Pilot](https://x.com/chamath/status/2072390507628540213) (作者 [@chamath](https://x.com/chamath))

**如果你想評估 GLM-5.2 在遺留應用改造流程裡能不能當更便宜的執行模型，可以看這個案例，因為 8090 的試點說 GLM 加 Software Factory 相比單跑 Opus 4.8 把成本壓到了 1/16.4，但速度大約慢了 3 倍。**

Chamath 分享了一個把 PHP 遷到 Next.js 的初步試點。接入 8090 Software Factory 的 Opus 4.8 相比單跑 Opus，成本低了 1.4 倍、速度快了 1.5 倍；而同樣的 factory 配上 GLM 5.2，則把成本壓到了單跑 Opus 的 1/16.4，但運行速度大約慢了 3 倍。貼文也明確說這只是 n=1 的方向性結果，後面還要在 10 到 15 個真實遺留改造任務上重跑。

類型: 評測 | 日期: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio Browser-Use Local Loop](https://x.com/MaziyarPanahi/status/2071955191260151862) (作者 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想測試一套完全本地的 GLM-5.2 棧，是否已能在消費級硬體上完成輕量 browser agent 工作，可以用這個案例，因為作者在 Mac Studio 上用 llama.cpp 和 browser-use 到 Hugging Face 找到了一個 PII 模型。**

MaziyarPanahi 表示，他先在 Mac Studio 上透過 llama.cpp 本地運行 GLM-5.2，再把它包進一個 browser-use agent loop。貼文中的例子是讓模型去 Hugging Face 找 PII 模型，最後定位到 `privacy-filter-nemotron`。

類型: 演示 | 日期: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop Agent Swap Cost Cut](https://x.com/aronkor/status/2072032854675218538) (作者 [@aronkor](https://x.com/aronkor))

**如果你想在現有 agent harness 裡直接試一次模型替換，可以用這個案例，因為 Gumloop 表示把最常用的 agent 換成 GLM-5.2 後，使用者幾乎沒感到品質下降，而 credits 消耗大約少了 50%。**

aronkor 描述了一次 Gumloop 內部實驗：在保留同一套 harness 與同一份 prompt 的情況下，把最常用的一批 agent 直接換成了 GLM 5.2。結果是，幾乎沒人察覺輸出品質差異，但 credits 消耗接近減半。

類型: 評測 | 日期: 2026-06-30

---

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

<a id="case-145"></a>
### Case 145: [OpenCode + Fireworks 降本遷移](https://x.com/SeekingN0rth/status/2071484711327985696) (作者 [@SeekingN0rth](https://x.com/SeekingN0rth))

**如果你想測試只換 open-model harness 是否已經足夠，可以用這個案例，因為作者把個人 coding 與 loop task 遷到 Fireworks 上的 GLM-5.2 + OpenCode 後，稱 token 成本降到了三分之一，而且日常品質沒有明顯下滑。**

SeekingN0rth 表示，他在一個週末裡把個人 coding 與 loop task 遷到了 Fireworks 上的 GLM 5.2 + OpenCode，token 花費大約降到原來的三分之一。貼文認為真正決定體驗的是 harness，而不是是否絕對前沿：OpenCode 的終端體驗接近 Claude Code，日常任務沒有感到明顯品質下降，而且這種換模型路徑同樣適用於那些更看重成本而不是極致 SOTA 的企業場景。

類型: 評測 | 日期: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA 的 GLM 聚合器工作流](https://x.com/IBuzovskyi/status/2071601107944571249) (作者 [@IBuzovskyi](https://x.com/IBuzovskyi))

**如果你願意為高價值 agent 回合多做一層編排，可以用這個案例，因為 Hermes Agent 的 MoA 設定把 GLM-5.2 和其他模型組合後，在貼文裡的 demo 中用很小的增量成本換來更好的輸出。**

IBuzovskyi 把 Hermes Agent 的 Mixture of Agents 模式解釋為：一個擁有 tool access 的 aggregator 模型，加上若干只提供私有建議的參考模型。貼文給出一次 coding 測試：單獨使用 GLM 5.2 花了 13 分鐘、0.38 美元；改成 GLM 5.2 聚合 Kimi K2.6 與 MiniMax M3 後，花了 35 分鐘、0.47 美元，但動畫更流暢、視覺更好、遊戲機制也更乾淨。貼文還補充了 preset 設計、功能入口，以及哪些情境值得承擔額外延遲。

類型: 整合 | 日期: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline 推理開關帶來的 Harness 差值](https://x.com/akshay_pachaar/status/2071638409022763292) (作者 [@akshay_pachaar](https://x.com/akshay_pachaar))

**如果你想判斷決定結果的是 harness 還是權重本身，可以用這個案例，因為同一個 GLM-5.2 在同一批 coding task 上，只是打開 reasoning，結果就從 57.3% 跳到 68.5%。**

akshay_pachaar 引用了 Cline 的一個測試：同樣的 GLM 5.2、同樣的 coding task，一次關閉 reasoning，結果是 57.3%；一次開啟 reasoning，結果是 68.5%。這則貼文用這個差值說明，當目標是交付可運行程式碼而不是只產出文字時，上下文延續、工具可達性、編輯應用方式與驗證 loop，可能和底層模型本身一樣重要。

類型: 評測 | 日期: 2026-06-29

<a id="case-136"></a>
### Case 136: [Cursor + Fireworks 4.55 億 Token 實戰測試](https://x.com/robinebers/status/2071246749210190132) (作者 [@robinebers](https://x.com/robinebers))

**如果你想判斷 GLM-5.2 能否成為 Cursor 的日常主力模型，可以用這個案例，因為作者回報在 Fireworks 服務下真實跑了 4.55 億 tokens，且暫時不想回到 Opus 或 GPT-5.5。**

robinebers 表示，自己在 Cursor 裡切到 GLM 5.2 36 小時後，因為配上 Fireworks 而徹底改觀。貼文特別提到 image support、宣稱的零資料保留、每秒約 80-100 tokens 的吞吐，以及 4.55 億 tokens 大約只花了 145 美元。這讓它成為比泛泛 benchmark 稱讚更有價值的特定 harness 評測，也顯示 provider 選擇確實會改變實際使用體驗。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Devin Desktop Harness 與 Skill 可攜性](https://x.com/lily_gpupoor/status/2071297351801794850) (作者 [@lily_gpupoor](https://x.com/lily_gpupoor))

**如果你覺得 Z.ai 自家的 coding 介面不夠穩定，想測試 GLM-5.2 在 Devin Desktop 裡的表現，可以用這個案例，因為作者回報 skill 遷移更容易、速度更快，也更好 hack。**

lily_gpupoor 表示，在 API 不穩定的一段時間裡，自己透過 Devin Desktop 重度使用 GLM-5.2，體感明顯優於直接使用 Z.ai 的 coding plan。貼文點出三個具體工作流收穫：GLM 成功修改了自訂 Solarized Green 主題 JSON 並順利註冊 extension、Devin 的整體體感速度異常快，以及先前從預設 Windsurf Cascade agent 轉過來後，大部分既有 skills 都能直接沿用。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi 內聯 GLM 審閱者](https://x.com/xpasky/status/2070831715518460177) (作者 [@xpasky](https://x.com/xpasky))

**如果你想在 Pi 風格的 coding-agent loop 裡加入第二位審閱者，可以用這個案例。作者表示，GLM-5.2 可以逐回合給 Opus 提建議，成本增幅大約只有 10%。**

xpasky 表示，Pi 使用者可以照搬一種 OMP 風格的模式，讓第二個模型審閱每一回合，並把建議內聯注入。貼文特別提到，GLM 5.2 會持續盯著 Opus，兩個模型還會明顯「拌嘴」，而額外這位 GLM reviewer 平均只會讓 Opus API 成本增加約 10%。因此，這更像是一種具體的多模型監督模式，而不是完整的模型替換方案。

類型: 整合 | 日期: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter 一次成型 Telegram Bot](https://x.com/MatinSenPai/status/2070259817818812701) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**如果你想測試 GLM-5.2 在 one-shot coding-agent build 裡，是否能主動補上偏向生產環境的 defaults，而不是只寫出最低限度可運作的路徑，可以用這個案例。**

MatinSenPai 表示，他用影片裡相同的 prompt，讓 GLM 5.2 一次完成一個 Telegram bot，而且模型還主動補上了一些沒有明講的實務細節。貼文特別提到，模型會在傳送影片後自動清理檔案、會考慮 Telegram Bot API 的大小限制並設下預設 50 MB cap、會在結束前反覆 self-test，整體 structure 也比先前的 MiMo build 更乾淨。作者還補充，透過 AgentRouter 的這次執行大約花了 140K tokens、約 5 美元。

類型: 演示 | 日期: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go 重構首輪取勝](https://x.com/vedovelli74/status/2069889605969592500) (作者 [@vedovelli74](https://x.com/vedovelli74))

**用這個案例評估 GLM-5.2 在 OpenCode 中處理中等規模 Go 重構任務的表現，而不是只看 benchmark 宣傳。**

vedovelli74 回報了自己第一次用 OpenCode 處理一個中等規模 GoLang 程式庫重構，稱 GLM-5.2 比 Opus 4.8 更快、更省 token，而且在第一輪就正確判斷了需要重構的部分。作者還補充說，後續又用 Codex 和 Opus 做了交叉驗證，但最終交付品質仍然是 GLM-5.2 更勝一籌。

類型: 評測 | 日期: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 預設執行成本 3.36 美元](https://x.com/clairevo/status/2069828122640548204) (作者 [@clairevo](https://x.com/clairevo))

**用這個案例判斷 GLM-5.2 是否適合作為 Claude Code 與 Cursor 的日常預設模型，再決定是否把更多自主編碼工作遷移到開放權重模型上。**

clairevo 表示，GLM 5.2 已經成為她在 Claude Code 與 Cursor 裡的預設模型，目前累計成本只有 3.36 美元，同時卻給出了類似 Opus 的編碼體驗。貼文也提到了透過 OpenRouter 的接入路徑、前端設計感受，以及一項長時自主任務評測，這些都是它最後說服作者切換預設模型的原因。

類型: 評測 | 日期: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手演示與作品展示
<a id="case-202"></a>
### Case 202: [Command Code Space Shooter Feature Win](https://x.com/CommandCodeAI/status/2075264795817972107) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**如果你想看 GLM-5.2 在 one-shot 互動 UI build 裡的表現，可以看這個案例，因為 Command Code 把同一個 retro space-shooter prompt 跑在 Fable 5、GPT 5.5、GLM 5.2 與 DeepSeek V4 Pro 上，並把 GLM 排在 features 第一。**

Command Code 說，同一個 `/design` prompt 在四個模型上都做出了相近的 retro pixel-art space-shooter 版面，但 GLM 5.2 在聲音、控制、關卡節奏和整體 UX 等 features 上特別突出，而且成本只有 $0.07，對比 Fable 5 的 $0.80。這讓它更像是一個輕量 game/UI build 的實戰對比，而不只是 benchmark 截圖。

類型: 評測 | 日期: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [ZCode Nintendo DS Emulator](https://x.com/0xSero/status/2074870153267818638) (作者 [@0xSero](https://x.com/0xSero))

**如果你想看一個長時程、本地執行的 coding build，可以看這個案例，因為作者讓 GLM-5.2 在 4x RTX 6000 的 ZCode 裡，從零開始用 C++ 去做一個 Nintendo DS 模擬器。**

原貼文展示的是 GLM-5.2 在四張 RTX 6000 GPU 的 ZCode 環境裡運行，並給了一個非常明確的目標：不要用現成模擬器，而是從零開始用 C++ 做一個 Nintendo DS emulator，並一直做下去直到 Mario 64 DS 的 ROM 能跑起來。這就讓它成為一個真正有硬終點的 coding-agent demo，而不是泛泛的「做了個小玩具應用」。

類型: 示範 | 日期: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [Command Code Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (作者 [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**如果你想看 GLM-5.2 在輕量設計類小遊戲任務裡的性價比，可以看這個案例，因為作者用同一個 Flappy Bird prompt 跑了 Command Code，最後認為 Fable 5 雖然價格接近 GLM-5.2 的 9 倍，但在 UX 上並沒有明顯更好。**

貼文說，這次實驗對 DeepSeek V4 Pro、GLM 5.2 和 Fable 5 使用了同一個遊戲 prompt，以及同一套 Command Code `/design` 設定。GLM 5.2 的價格落在 DeepSeek 和 Fable 之間，但作者認為 Fable 並沒有展示出足以證明價格差的 UX 優勢，所以這是一條很具體的 UX 對成本比較，而不是泛泛的 arena 說法。

類型: 評測 | 日期: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [REAP NVFP4 Rubiks Cube One-Shot](https://x.com/RoundtableSpace/status/2072700573145788914) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想測試 GLM-5.2 在單一 prompt 的互動式 build 任務上的表現，可以看這個案例，因為 REAP-NVFP4 的 demo 說它只靠一個 prompt 就做出了 3D Rubiks Cube、真實 scramble、即時狀態和 solve 按鈕。**

RoundtableSpace 說，GLM-5.2-REAP-NVFP4 只收到一個 HTML prompt，就回傳了一個可運作的 3D Rubiks Cube app，裡面有即時狀態、真實 scramble 邏輯和 solve 動作。貼文沒有公開太多程式碼，但它仍然是一個很具體的 one-shot build demo，而不是泛泛的 benchmark 截圖。

類型: 演示 | 日期: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP Relay iPhone Client](https://x.com/mov_axbx/status/2072192903762288721) (作者 [@mov_axbx](https://x.com/mov_axbx))

**如果你想把一個本地 GLM-5.2 agent 很快包進移動端介面，可以看這個案例，因為作者說 Codex 的 build-ios-app plugin 只用了幾個小時，就給一個已經接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很強的 iPhone 客戶端。**

mov_axbx 說，他想給一個本地託管的 OMP agent 做個手機 app，於是用了 Codex 的 build-ios-app plugin，幾個小時內就拿到了比較完整的版本。後端路徑則是一個用 GLM-5.2 和 OMP 寫的自訂 relay，Cloudflare 負責隧道。

類型: 演示 | 日期: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [開源 DevRel 研究 Agent](https://x.com/Astrodevil_/status/2071572680470655253) (作者 [@Astrodevil_](https://x.com/Astrodevil_))

**如果你想把 GLM-5.2 從通用聊天模型變成垂直研究助手，可以用這個案例，因為作者做了一個開源 DevRel agent，能把產品和受眾輸入轉成帶證據與提綱的選題列表。**

Astrodevil_ 用 GLM-5.2 做了一個 chat-first 的 DevRel 研究應用：輸入產品與受眾簡介後，它會去 Hacker News 搜需求訊號、去 DEV 找內容缺口，再透過 Engram memory 更新事實，最後回傳帶證據與提綱的排序選題。貼文也點明了技術棧：Agno、Weaviate Engram、Nebius inference，以及一個開源程式碼庫。

類型: 示範 | 日期: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 六版本落地頁迭代流程](https://x.com/nutlope/status/2070199649818779914) (作者 [@nutlope](https://x.com/nutlope))

**如果你想先用 GLM-5.2 產出多個版本，再把最佳結果交給 coding agent 繼續做，以低成本試作 landing page，可以用這個案例。**

nutlope 描述了一個圍繞 GLM 5.2 與 Recast 的 web iteration workflow：先用同一個 prompt 生成 6 個 landing page 版本，挑出最好的 design，下載那份 code，再交給另一個 coding agent 繼續迭代。作者表示，GLM-5.2 在這個場景裡表現很好，因為它又快、又便宜，而且很有 design sense；同樣的預算通常可以做出 3 到 6 個 GLM 版本，才等於 Opus 4.8 生成 1 個頁面的成本。

類型: 教程 | 日期: 2026-06-25

---

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
<a id="case-170"></a>
### Case 170: [NVIDIA Free API Plug-And-Play Access](https://x.com/hqmank/status/2072855265612030010) (作者 [@hqmank](https://x.com/hqmank))

**如果你想透過免費 hosted endpoint 快速試用 GLM-5.2，可以看這個案例，因為 hqmank 表示 NVIDIA 已開放 OpenAI 相容的 API 路徑，而且確認可以直接 plug-and-play 接上。**

hqmank 表示，GLM-5.2 已上線 NVIDIA 的免費 API，並且在快速 hands-on 測試中可以正常運作。貼文將它描述為 OpenAI 相容且可 plug-and-play，但也提醒免費 tier 往往會在需求升高後收緊限制。這讓它成為一個適合快速評估或暫時 agent routing 的實用 access note。

類型: 整合 | 日期: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [Free Workers AI Coding-Agent Route](https://x.com/ClaudeCode_UT/status/2072881775408456066) (作者 [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**如果你想為 coding agent 建立一條零成本的 GLM-5.2 路線，可以看這個案例，因為這篇教學用 OpenAI 相容的 `cf/zai-org/glm-5.2` endpoint，把 Workers AI 接到 Claude Code、OpenCode、Cursor 與 Aider。**

ClaudeCode_UT 給出六個步驟：建立免費 Cloudflare 帳號、複製 Workers AI 的 account ID、發出 API token、在 OpenAI 相容工具中加入 Cloudflare provider、選擇 `cf/zai-org/glm-5.2`，然後開始執行 Claude Code、Cursor、Aider 或 OpenCode。對想先測 coding-agent workflow、再決定是否承擔 token 計費的團隊來說，這是一個很實用的 access tutorial。

類型: 教程 | 日期: 2026-07-03

---

<a id="case-208"></a>
### Case 208: [Open Molecular Viewer Agent Stack](https://x.com/MaziyarPanahi/status/2075913552854933869) (作者 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想把 GLM-5.2 接到一條開放的科學檢視 workflow，可以看這個案例，因為 MaziyarPanahi 把經由 Hugging Face Inference Providers 的 GLM-5.2，和跑在 llama.cpp 上的 Qwen3-VL、Mol*、PydanticAI 串在一起，用單一 prompt 就把 EGFR 加 erlotinib 的結構 render 並做出評論。**

MaziyarPanahi 描述了一套完全開放的 stack：GLM-5.2 透過 Hugging Face Inference Providers 擔任語言核心，Qwen3-VL 透過 llama.cpp 做視覺檢查，Mol* 負責把結構 render 出來，而 PydanticAI 協調 agent layer。貼文說，這條 workflow 以 RCSB PDB 的 EGFR 加 erlotinib 範例為核心，用單一 prompt 產出六個 render，因此它不是單純的可用性公告，而是一條具體的多工具科學 agent 整合案例。

類型：整合 | 日期：2026-07-11

---
<a id="case-204"></a>
### Case 204: [Perplexity Advisor WANDR Cost Baseline](https://x.com/perplexity_ai/status/2075229779716973030) (作者 [@perplexity_ai](https://x.com/perplexity_ai))

**如果你想估算 GLM-5.2 在 routing 式 computer-use harness 裡的成本結構，可以看這個案例，因為 Perplexity 說它的 GLM 5.2 加 advisor 配置在 WANDR 上是 2.1x，而 Opus 是 6.1x，整體 benchmark 成本也接近一半。**

Perplexity 說，它是以 GLM 5.2 作為 baseline 來衡量每任務成本，而在 WANDR 上，GLM 5.2 加 advisor 的路線是 2.1x，Opus 則是 6.1x。這可以視為一個很具體的 open-weight-first computer agent routing 信號：不是每一步都跑更貴的 closed model，而是用較便宜的 GLM 核心配合選擇性升級。

類型: 評測 | 日期: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [Coworker Open Artifacts Routing](https://x.com/coworkerapp/status/2075233366266310905) (作者 [@coworkerapp](https://x.com/coworkerapp))

**如果你想把 GLM-5.2 放進企業 artifact 工作流，可以看這個案例，因為 Coworker 說 Open Artifacts 能做 docs、decks、PDF、spreadsheets、dashboards 和 apps，而且 optimized router 能把 token 使用量壓到約 5 分之 1，同時仍提供美國託管的 GLM 5.2。**

Coworker 說，Open Artifacts 可以生成 docs、decks、dashboards、spreadsheets、PDF 和完整 apps 這類可分享成果物。同一篇 launch 貼文也說，它的 optimized mode 會為每個 task 挑選合適模型，把 token 消耗壓到大約五分之一，同時仍讓團隊在美國託管、SOC 2、connector 豐富的環境裡使用 GLM 5.2。

類型: 整合 | 日期: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [DotCode Context Upload Workflow](https://x.com/stagedhappen/status/2074775356867789241) (作者 [@stagedhappen](https://x.com/stagedhappen))

**如果你想在私有 coding sandbox 裡給 GLM-5.2 更多專案上下文，可以看這個案例，因為 DotCode 給 GLM 5.2 加上了 screenshot、圖片、CSV、PDF、原始碼檔案和 zip 上傳，並把這些都接進同一條 filesystem + terminal 工作流。**

DotCode 說，GLM 5.2 現在已經能配合 contextual workspace uploads 使用，agent 可以檢查檔案、瀏覽專案結構、編輯程式碼、執行 terminal 命令，並且在同一個 sandbox 裡連續工作。貼文列出了支援的輸入類型，也寫出了從 prompt + files 到 sandbox execution 的流程，把這件事定義成朝「基於真實專案上下文的 coding agent 工作」邁出的一步。

類型: 整合 | 日期: 2026-07-08

---
<a id="case-209"></a>
### Case 209: [Colibri 25GB RAM Sparse Streaming](https://x.com/techNmak/status/2075872446197158361) (作者 [@techNmak](https://x.com/techNmak))

**如果你想理解本地 GLM-5.2 實驗的新下限，可以看這個案例，因為 techNmak 詳細說明 Colibrì 如何靠著從 NVMe 串流 experts，用大約 25GB RAM 跑起 744B MoE，不過最小配置只有大約 0.05 到 0.1 tok/s。**

techNmak 把 Colibrì 總結成一個純 C 的本地 inference engine：只把持續會用到的 hot weights 留在 RAM，把路由到的 experts 放在 NVMe，上線後大約有 9.9GB 長駐、聊天時 RAM 峰值約 20GB，而 int4 權重大約占 370GB 磁碟。貼文也明確把這件事定位成 systems proof of concept，而不是快速的 production serving，因為 25GB 機器上的 cold generation 只有大約 0.05 到 0.1 tok/s，而且 int4 量化對品質的影響還沒有被完整 benchmark。

類型：示範 | 日期：2026-07-11

---
<a id="case-206"></a>
### Case 206: [SGLang NVFP4 Production Throughput](https://x.com/sgl_project/status/2075721488456654861) (作者 [@sgl_project](https://x.com/sgl_project))

**如果你想估算 GLM-5.2 NVFP4 的正式生產 SGLang serving 規模，可以看這個案例，因為官方 SGLang v0.5.15 release 說它現在在 8x B300 上可達每位使用者 500+ tok/s，在 4x GB300 上則是 450 tok/s，batch size 為 1。**

SGLang v0.5.15 的官方公告表示，這一輪 release cycle 主要在做 GLM-5.2 NVFP4 的 production tuning。貼文指出，在 bs=1 下，8x B300 可達每位使用者每秒 500 多 token，4x GB300 則可達 450 token/s。對正在評估 hosted 或 self-managed inference stack 的團隊來說，這是一個很具體的 deployment throughput 檢查點。同一則公告也把這件事定位成 upstream 產品支援，而不是一次性的實驗室 hack。

類型: 評測 | 日期: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Dahl 100M Free GLM Endpoint](https://x.com/pengsonal/status/2074908680106180669) (作者 [@pengsonal](https://x.com/pengsonal))

**如果你想走一條不用綁卡、又相容 OpenAI 的路徑來試 GLM-5.2，可以看這個案例，因為 Dahl Inference 給 GLM 5.2 FP8 提供了 1 億免費 tokens，並且寫清了如何建 key、如何呼叫 `/v1/chat/completions`。**

貼文把 GLM 5.2 FP8 列進了 Dahl 的免費開源模型 endpoint，並說不需要註冊也不需要銀行卡。它還給出了一條很具體的配置流程：在 web UI 裡生成 key，使用相容 OpenAI 的 `/v1/chat/completions` endpoint，同時提醒直接用 `curl` 可能會撞上 Cloudflare 403，但 web chat 這條路是能用的。

類型: 教學 | 日期: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [NVIDIA Free Endpoint GLM Setup](https://x.com/undefinedKi/status/2074491917333655948) (作者 [@undefinedKi](https://x.com/undefinedKi))

**如果你想在不 self-hosting 的情況下把 GLM-5.2 接進 coding tools 裡測試，可以看這個案例，因為原貼文給出了一條免費的 NVIDIA endpoint 路線，直接把 GLM-5.2 的 API key 用到 Claude Code、Cursor 或 Cline。**

貼文說，NVIDIA 放出了包括 GLM-5.2 在內的多款頂級 model 免費 API key，並給出了一條直接的配置路徑：建立 NVIDIA 帳號，打開某個 free endpoint model 的 Build 頁面，生成 API key，然後把 base URL 和 key 貼到 Claude Code、Cursor 或 Cline 裡。所以這是一條很實用的 access tutorial，讓你不用按 token 計費，也不用本地 GPU stack，就能試用 GLM-5.2。

類型: 教學 | 日期: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [0G TeeML Private Inference Route](https://x.com/0G_labs/status/2074496704959676682) (作者 [@0G_labs](https://x.com/0G_labs))

**如果你想把 GLM-5.2 接到一條更重視隱私的 provider 路線上，可以看這個案例，因為 0G 說 GLM 5.2 已經跑在 TeeML 上，prompts 被封裝在 TEE enclave 裡，而且價格低於官方路線。**

0G 把 TeeML 定義成自己的 private inference 層，並表示 GLM 5.2 現在可以在 trusted execution environment 裡進行可驗證執行。雖然貼文很短，但它同時提供了具體的 provider integration，以及 privacy 和 pricing 角度，所以更適合作為一條部署路線訊號，而不是模型品質結論。

類型: 整合 | 日期: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [DuckDB Flock Open-SQL PR](https://x.com/lhoestq/status/2074143736624275629) (作者 [@lhoestq](https://x.com/lhoestq))

**如果你想把 GLM-5.2 帶進完全開源的本地 SQL analysis，可以看這個案例，因為 lhoestq 說，一個 duckdb + flock 的 PR 已經讓 GLM-5.2 進入 100% open-source 的資料堆疊。**

貼文說，作者開了一個 PR，把 GLM-5.2 接進 duckdb 與 flock，並把它描述成一種把 frontier 級 open intelligence 直接用在資料工作上的方式。因為這裡的來源是「PR 已開」而不是「已 merge 的 release note」，所以它更適合作為本地 analytics 與 SQL-native workflow 的 integration-in-progress 訊號。

類型: 整合 | 日期: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [One-Key 26-Model API Access](https://x.com/Alan_Earn/status/2073663239028924680) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**如果你想先透過單一 OpenAI 相容 provider 試用 GLM-5.2，可以看這個案例，因為 Alan_Earn 說一把 API key 就能存取 GLM-5.2 和另外 25 個模型，還附帶 26 美元起始 credits。**

這則貼文給出一條很短的 setup：註冊帳號、加卡、解鎖 dashboard、領取 credits、生成 API key，然後把它貼進 Codex、Cursor、OpenCode、OpenClaw、Hermes 等客戶端。貼文也寫明這是 pay as you go，而且大模型會很快吃掉免費額度，所以它更適合作為 access 與 pricing 說明。

類型: 教學 | 日期: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [NVIDIA NIM OpenCode Thinking Setup](https://x.com/Dracoshowumore/status/2073384581256929717) (作者 [@Dracoshowumore](https://x.com/Dracoshowumore), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI))

**如果你想透過 NVIDIA 免費 NIM endpoint 把 GLM-5.2 接進 OpenCode，並且走一條明確開啟 thinking 的零成本路線，可以看這個案例，因為 Dracoshowumore 分享了 API key 流程、base URL，以及一份由工具層接管 function calls、讓 GLM 以 enable_thinking=true 運行的 OpenCode 設定。**

Dracoshowumore 把整套配置路徑講得很清楚：先在 NVIDIA developer platform 註冊、生成 GLM-5.2 API key、把 OpenCode 指向公開的 base URL、關掉模型原生的 tool calling，並在 provider options 裡傳入 chat_template_kwargs.enable_thinking=true。同一篇貼文也指出，NIM 這條路預設不會暴露 function calling 或 reasoning traces，所以工具編排必須由 OpenCode 接手。這使它成為一條實用的 configuration note，而不只是又一條免費 endpoint 公告。

類型: 教程 | 日期: 2026-07-04

<a id="case-165"></a>
### Case 165: [ZCode Launch With Mobile Agent Control](https://x.com/Digiato/status/2072663459850829985) (作者 [@Digiato](https://x.com/Digiato))

**如果你想把 ZCode 當成 GLM-5.2 的官方 coding surface 來評估，可以看這個案例，因為 launch report 說這個免費的 agentic IDE 會上 Windows、macOS、Linux，還能透過 Telegram、WeChat、Feishu 追蹤專案進度。**

Digiato 把 ZCode 描述成一個圍繞 GLM-5.2 建立的免費 agentic development environment，定位上對標 Cursor、Claude Code 和 Copilot。貼文說它支援 Windows、macOS、Linux，與 GLM-5.2 深度整合，並能透過 Telegram、WeChat、Feishu 查看專案進度。這讓它比一般的模型上線公告更有實際接入價值。

類型: 整合 | 日期: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki Auto-Maintained Agent Docs](https://x.com/LangChain/status/2072745455788933321) (作者 [@LangChain](https://x.com/LangChain))

**如果你想讓 agent 可讀的文件自動保持最新，可以看這個案例，因為 LangChain 說 OpenWiki 會隨著程式碼變動重建並維護 repo docs，而且能跑在 GLM 5.2 這類開源模型上。**

LangChain 把 OpenWiki 描述成一層面向 coding agent 的開源文件維護工具。貼文說它把 open harness 和 open CLI workflows 結合起來，會在 codebase 變動時更新文件，並且能跑在 GLM 5.2、Kimi K2.7 這類開源模型上。對想讓 agent 讀到最新 repo docs、而不是依賴人工維護 wiki 的團隊來說，這是一個很實用的 file-based memory 模式。

類型: 整合 | 日期: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [Foundry PTUs Through FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在不重寫 agent 用戶端的前提下，把 GLM-5.2 接到企業級 Foundry 預算裡，可以用這個案例，因為 Fireworks 說 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。**

Fireworks 表示，GLM 5.2 已經上線 Microsoft Foundry。啟用 FireConnect 後，團隊可以一邊消耗 Foundry PTU，一邊繼續從 Codex、OpenCode 或 Pi 發請求，而不必為每個 agent 入口單獨搭一套模型接入路徑。

類型: 整合 | 日期: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM Eval Workbench](https://x.com/ankrgyl/status/2072042305108722040) (作者 [@ankrgyl](https://x.com/ankrgyl))

**如果你想把 GLM-5.2 和 Opus 放進同一套 eval 棧裡比較，可以用這個案例，因為 Braintrust 聯合 Baseten 給出了一個帶長上下文成本與精度對照的接入樣例。**

ankrgyl 表示，Braintrust 已把 GLM-5.2 接進平台，並由 Baseten 提供支援，團隊可以直接在 eval 與 production trace 中跑這個模型。示例比較了 25K 與 50K tokens 的長上下文檢索：Opus 4.8 大約高 3.5 分，但每條 trace 的成本約高 4.1 到 4.5 倍。

類型: 整合 | 日期: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass 開放權重模型統一訂閱](https://x.com/iam_elias1/status/2071655509611151674) (作者 [@iam_elias1](https://x.com/iam_elias1))

**如果你想把多個開放權重 coding model 收攏到同一個 agent harness 裡，可以用這個案例，因為 ClinePass 把 GLM-5.2 和相關模型打包成統一月費，而不是分別維護 provider key 和帳單。**

iam_elias1 把 ClinePass 描述成一個月費 9.99 美元的入口，讓 GLM-5.2、DeepSeek、Kimi、Qwen、MiniMax、MiMo 等開放權重模型直接進入 Cline 的 IDE 擴充與 CLI。貼文稱它可以取代分散的 provider API key，提供 2-5 倍標準 API 額度，還能在同一個 session 裡依照不同編碼階段切換模型，並且透過 CLI 註冊首月只要 1.99 美元。

類型: 整合 | 日期: 2026-06-29

<a id="case-137"></a>
### Case 137: [供 Coding Agents 使用的免費 GLM API 服務](https://x.com/mcwangcn/status/2071261128575897901) (作者 [@mcwangcn](https://x.com/mcwangcn))

**如果你想在不註冊的情況下，把 GLM-5.2 接入 Hermes 或其他 coding agent，可以用這個案例，因為這個共享服務會發放短時效 API key，整體設定相當輕量。**

mcwangcn 分享了一個免費的 GLM-5.2 API 服務，據稱不需要註冊或登入，就能直接從 Lobster、Hermes 或其他 coding agent 使用。貼文同時指出，每次生成的 API key 只會維持一小時，之後需要重新申請。這是一個很具體的反濫用限制，也意味著它更適合快速測試工作流，而不是長時間、無人值守的正式生產使用。

Type: Integration | Date: 2026-06-28

---

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

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI OpenCode 設定](https://x.com/RoundtableSpace/status/2070820686243959276) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想在不自備模型主機的情況下，透過 Cloudflare Workers AI 這條免費的 OpenAI 相容路線運行 GLM-5.2 做 coding agent，可以用這個案例。**

RoundtableSpace 表示，你可以先註冊一個免費的 Cloudflare account，複製 Account ID，建立 API token，再把 Cloudflare 當作 provider 加進 OpenCode，並指定模型 `@cf/zai-org/glm-5.2`。貼文還說，這條路線同樣適用於 OpenCode、Cursor、Aider、Hermes Agent、Claude Code 等其他 OpenAI 相容工具，是一條相當實用的 coding agent 託管接入捷徑。

類型: 教程 | 日期: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js 零設定瀏覽器客戶端](https://x.com/FareaNFts/status/2070848321212792945) (作者 [@FareaNFts](https://x.com/FareaNFts))

**如果你想在接觸 API key、帳單或後端設定之前，先用純瀏覽器原型測試 GLM-5.2，可以用這個案例。**

FareaNFts 表示，Puter.js 透過一個 CDN script tag 就能在客戶端暴露 GLM 系列模型，`z-ai/glm-5.2` 可以直接在瀏覽器程式碼裡呼叫，不需要伺服器，也不需要開發者側的計費設定。貼文把它定位成個人工具、vibe coding app 和輕量 agent 的快速原型路徑，同時也說明了代價：Puter 使用的是 user-pays 的瀏覽器模式，並不適合高吞吐的生產流量。

類型: 教程 | 日期: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 統一端點接入](https://x.com/FareaNFts/status/2070900056736379288) (作者 [@FareaNFts](https://x.com/FareaNFts))

**如果你想把 GLM-5.2 放進更大的多模型堆疊裡，可以用這個案例，因為貼文描述了一個帶 free trial credit 的單一 OpenAI 相容 SiliconFlow endpoint，同時覆蓋中文和西方模型。**

FareaNFts 表示，SiliconFlow 透過一個 OpenAI 相容 endpoint，同時提供 GLM-5.2、DeepSeek、Qwen、Llama 4、Hunyuan、Mistral、Yi、Gemma、Phi 等 200 多個模型。貼文還提到，註冊就送 1 美元 free credit、無需綁卡、部分模型持續免費、支援 spending limit，而且這套 key 可以直接塞進 Cursor、Claude Code、Aider 等工具裡。

類型: 整合 | 日期: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [HuggingChat 建站到 HF Space 部署](https://x.com/victormustar/status/2070190742991994967) (作者 [@victormustar](https://x.com/victormustar))

**如果你想在幾乎免費的 personal-site flow 裡試用 GLM-5.2，從 HuggingChat 搜集資料到部署到 Hugging Face Spaces，都可以參考這個案例。**

victormustar 表示，只要有 Hugging Face account，就有足夠的 free credits 可以在 HuggingChat 裡讓 GLM-5.2 幫你建網站，並由 Exa 補足關於使用者的背景 research。貼文還提到，最終生成的網站可以免費部署成 static Hugging Face Space，對於 personal site 實驗來說，是一條非常具體而且低成本的路線。

類型: 教程 | 日期: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 上線](https://x.com/digitalocean/status/2070177703911719301) (作者 [@digitalocean](https://x.com/digitalocean))

**如果你想透過 managed infrastructure 取得官方 provider access，而不自己托管 1M context 的模型，可以用這個案例接入 GLM-5.2。**

DigitalOcean 宣布在自家的 Inference Engine 上提供 GLM-5.1 與 GLM-5.2，並將它定位為適合長達 8 小時的 agentic coding workflow、擁有 1M-token context window 的模型。貼文也把這條路線描述成一種可直接接入既有 stack 的方案，具備 usage-based pricing 與 fully managed infrastructure。

類型: 整合 | 日期: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S 檔位](https://x.com/CommandCodeAI/status/2069891896881857016) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**如果你更在意長時程編碼任務的回應速度，而不只是最低入門價格，可以用這個案例接入更快的 GLM-5.2 檔位。**

Command Code 宣布上線 GLM-5.2 Fast，稱這是一個維持相同 frontier coding 定位、但速度提升到 120-250 tokens per second 的高吞吐版本。貼文也提到，這個檔位保留了 1M 上下文、tool use 與 reasoning，而且從 1 美元 Go plan 加 10 美元 usage credits 起就能使用。

類型: 整合 | 日期: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI Gateway Fast GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (作者 [@wafer_ai](https://x.com/wafer_ai))

**如果你需要 serverless 速度和明確的 token 定價，可以用這個案例透過 Vercel AI Gateway 接入 GLM-5.2 Fast。**

wafer_ai 表示，GLM-5.2 Fast 已經上線 Vercel AI Gateway，速度為 150-250 tokens per second，上下文視窗為 1M token，標價為每 1M token 輸入 3.00 美元、輸出 10.25 美元、快取 0.50 美元。對於優先考慮吞吐與閘道定價可預期性的團隊來說，這是一個很具體的託管接入訊號。

類型: 整合 | 日期: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定價與本地部署
<a id="case-191"></a>
### Case 191: [Hermes-Built LiteLLM Local Lab](https://x.com/ivanfioravanti/status/2074609005272375329) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想把 GLM-5.2 當作 coding agent 來搭一個本地 inference lab，可以看這個案例，因為原貼文說 Hermes Agent + GLM-5.2 把 LiteLLM、Postgres、Prometheus 和 Grafana 都接在了一套 M3 Ultra 環境上。**

貼文說，LiteLLM 已經在一台 M3 Ultra 上跑起來了，並把一條基於 DGX Spark 的 Qwen model 當作初始測試路由暴露出來。對這個 repo 更重要的是，作者明確說 Hermes Agent + GLM-5.2 完成了 LiteLLM、Postgres、Prometheus 和 Grafana 的搭建，所以這是一條很具體的本地實驗室整合案例，涵蓋 routing、持久化和 observability，而不只是泛泛稱讚。

類型: 整合 | 日期: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [Dual M5 Max Offline Droneship Sim](https://x.com/XavierLocalAI/status/2073938465121833452) (作者 [@XavierLocalAI](https://x.com/XavierLocalAI))

**如果你想估算一套完全離線的 Apple Silicon GLM-5.2 agent 到底能做什麼，可以看這個案例，因為 XavierLocalAI 報告了一個 753B 配置：在兩台 128GB M5 Max 上以 26 tok/s 編寫 droneship landing simulator。**

原貼文說，這套配置使用的是 GLM-5.2 753B build、約 222GB 磁碟占用的 Unsloth dynamic IQ2_M quant、透過 Thunderbolt 5 連起來、合計約 256GB pooled memory 的兩台 M5 Max，以及 llama.cpp RPC。這裡的結果不只是 throughput：模型當時正在完全離線地 live-coding 一個 Falcon 9 的 droneship landing simulator，所以它是一條很具體的本地部署與 privacy-first agent demo。

類型: 示範 | 日期: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x DGX Spark Production Harness](https://x.com/thatcofffeeguy/status/2074245620207058981) (作者 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**如果你想判斷 5 節點 DGX Spark 配置是否已經足夠支撐 production 級 GLM-5.2 工作，可以看這個案例，因為 thatcofffeeguy 報告了在 400K context 下單流約 13.9 tok/s，以及 3 條 lane 合計 19.9 tok/s 的 live harness 結果。**

貼文說，這是作者在多輪 experiment 後跑出的最佳配置，而且當天就在沒有 pruning 的情況下上線 production。它對應的 workload 也比純 lab test 更具體：這套 harness 已經拿來在約 30 分鐘內生成內容，並審查當天的 ERP data。所以它更像一條實用的 deployment checkpoint，而不只是硬體炫耀。

類型: 示範 | 日期: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [M3 Ultra ds4-eval Q4 Checkpoint](https://x.com/ivanfioravanti/status/2073742792044446194) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想用 ds4-eval 真正 benchmark 一台 Apple Silicon 單機上的 GLM-5.2，可以看這個案例，因為 ivanfioravanti 報告了一次 q4 運行：M3 Ultra 512GB 機器上約 16 tok/s，92 項裡過了 76 項，總時長 8 小時 53 分。**

ivanfioravanti 說，這次 q4 的 ds4-eval 運行是在一台 M3 Ultra 512GB 機器上完成的，後面還會把舊 branch 用 batch inference 再跑一遍。這樣一來，repo 裡此前那個以影片為主的 M3 案例就多了一個更硬的配套證據：這則貼文給出了 pass 數和總運行時長，而不只是 throughput 片段。

類型: 評測 | 日期: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [4x RTX PRO 6000 Build Guide](https://x.com/QingQ77/status/2073589933567094981) (作者 [@QingQ77](https://x.com/QingQ77))

**如果你想評估一套嚴肅的本地 GLM-5.2-594B 方案，可以看這個案例，因為 QingQ77 分享了一份完整的硬體與運維指南，核心是 4 張 RTX PRO 6000、透過 opencode 暴露的 API，以及給 agent 用的 sandbox VM。**

這份 guide 描述了一條更高預算的路線：用 4 張 RTX PRO 6000 和 384GB VRAM 跑 GLM-5.2-594B，同時配合二手 EPYC 與 DDR4。貼文還涵蓋了 PCIe Gen4 交換、BIOS 的 bifurcation 與 ASPM、`iommu=off`、110V 線路下每卡 350W 限制、透過 opencode 暴露的 Docker container，以及保護宿主機的 sandbox VM。

類型: 教學 | 日期: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [4x DGX Spark QuantTrio Run](https://x.com/Tech2Wild/status/2073637530960826787) (作者 [@Tech2Wild](https://x.com/Tech2Wild))

**如果你想估算 4 節點 DGX Spark 叢集跑 GLM-5.2 QuantTrio 的上限，可以看這個案例，因為 Tech2Wild 給出了 200K context、單流 30 tok/s，以及 6 並發下總計 60.5 tok/s 的結果。**

Tech2Wild 說，這次最終量測保留了全部 256 個 experts，並使用了 k=4 的 MTP speculative decoding。和此前偏規劃的 Spark thread 不同，這裡給出的是已經跑完的本地推理結果：單流 30 tok/s、6 個並發請求合計 60.5 tok/s，並把叢集目標 context 設在 200K。

類型: 示範 | 日期: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [Single M3 Ultra 4-Bit Video Run](https://x.com/ivanfioravanti/status/2073502277449486460) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想估算 GLM-5.2 在 Apple Silicon 單機上的可行性，可以看這個案例，因為 ivanfioravanti 展示了在一台 M3 Ultra 512GB 機器上以約 16 tok/s 跑 4-bit 版本，並拿它和約 17 tok/s 的 q2 ds4-eval 影片做比較。**

ivanfioravanti 發了一段影片，展示 GLM 5.2 4-bit 在一台 M3 Ultra 512GB 機器上以約每秒 16 token 運行，並補充說 ds4-eval 的影片使用的是約每秒 17 token 的 q2 build。作者把它定位成仍在進行中的本地測試，但它依然提供了一個具體的 Apple Silicon 單機 throughput checkpoint，能和 repo 裡既有的 multi-M3 以及 oMLX 本地部署案例互相參照。

類型: 演示 | 日期: 2026-07-04

<a id="case-173"></a>
### Case 173: [AMD MI355X 2626 Tok/s Node Serve](https://x.com/wafer_ai/status/2073155792182907085) (作者 [@wafer_ai](https://x.com/wafer_ai))

**如果你想估算 AMD 硬體上的高吞吐 GLM-5.2 推理能力，可以看這個案例，因為 wafer_ai 表示 MI355X 達到每節點 2626 tok/s、單流 213 tok/s，而且成本比 Blackwell 低超過 2 倍。**

wafer_ai 表示，工程團隊把 GLM 5.2 部署在 AMD MI355X 上後，每節點可達每秒 2626 token，single-stream 模式則為每秒 213 token。貼文把這個結果描述為大約達到 B200 吞吐的 80%，但成本卻低超過 2 倍，因此對評估 NVIDIA 之外 open-weight 推理經濟性的團隊來說，是一個具體的 deployment reference。

類型: 演示 | 日期: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel Gateway 287 Tok/s Serverless](https://x.com/wafer_ai/status/2072861749104288074) (作者 [@wafer_ai](https://x.com/wafer_ai))

**如果你想估算 GLM-5.2 經過 serverless gateway 時的真實用戶延遲，可以看這個案例，因為 wafer_ai 表示它的 GLM 5.2 Fast 路線不是只在 benchmark harness 中，而是在 Vercel AI Gateway 上跑到 287 tokens per second。**

wafer_ai 表示，它們的 GLM 5.2 Fast 路徑在 Vercel AI Gateway 上達到每秒 287 token，並將這視為 serverless 佈署下終端使用者真正會看到的數字。這讓它成為一個很好的橋梁，連接原始推理 benchmark 與更接近 production 的 hosted access，特別是當 gateway overhead 也會影響體驗時。

類型: 演示 | 日期: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [One-Click RTX PRO 6000 Deployment](https://x.com/XciD_/status/2073035324272328733) (作者 [@XciD_](https://x.com/XciD_))

**如果你想估算隔離式 hosted GLM-5.2 部署的最低門檻，可以看這個案例，因為 XciD_ 表示 GLM-5.2-NVFP4 現在可在 8x RTX PRO 6000 的 Inference Endpoints 上以每小時 22 美元 one-click 部署。**

XciD_ 表示，753B MoE 版本的 GLM-5.2-NVFP4 現已能在使用專屬 8x RTX PRO 6000 instance 的 Inference Endpoints 上 one-click 部署。貼文強調每小時 22 美元的可預期價格、zero setup，以及 full isolation，因此對不想自行維運整個堆疊的團隊來說，是一個具體的 hosted deployment reference。

類型: 整合 | 日期: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [Full 744B On 5x ASUS GX10s](https://x.com/thatcofffeeguy/status/2072525885077434743) (作者 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**如果你想估一個極端 home-lab GLM-5.2 部署的規模，可以看這個案例，因為作者說完整 744B 模型已經能在 5 台 ASUS GX10 上帶 full context 跑起來，而且已接到處理真實 workload 的 causal harness。**

thatcofffeeguy 說，完整 744B 的 GLM-5.2 現在已經能在五台 ASUS GX10 系統上帶 full context 運行，token rate 也比預期更好，整個 stack 已經接上 causal harness。貼文還沒公布精確 throughput 數字，但它已經是一個很具體的公開證據，說明這類本地叢集可以承載完整模型，而不只是縮減版。

類型: 演示 | 日期: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Agent Route Swap In China Stack](https://x.com/0xluffy_eth/status/2072548580183900430) (作者 [@0xluffy_eth](https://x.com/0xluffy_eth))

**如果你在乎的是成本壓力而不是絕對最高品質，想把 GLM-5.2 放進 mixed-model stack 的 agent 層，可以看這個案例，因為作者說把 Sonnet 換成 GLM-5.2 之後，這個 slot 的輸入成本降到五分之一，品質大約只掉了 3%。**

這條 thread 列出了 reasoning、code generation、agent calls、batch work、image、video 六個路由變更。對 agent 層來說，作者把 Sonnet 換成 GLM 5.2，並表示效能大約下降 3%，但輸入成本便宜了 5 倍。30 天總結則說，整體 AI 營運成本下降了 87%，而收入沒有變。

類型: 評測 | 日期: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B Local Hardware Floor](https://x.com/devjuninho/status/2072151237840007399) (作者 [@devjuninho](https://x.com/devjuninho))

**如果你想更現實地評估 GLM-5.2 的本地部署門檻，可以看這個案例，因為原帖說即便量化後，2bit 也大約要 239GB、4bit 大約要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比較實際的起步線。**

devjuninho 明確反對 open weights 就等於普通用戶本地能輕鬆跑 的說法。貼文裡說，GLM-5.2 大約是 744B 參數、其中約 40B 啟用，2bit 估算約 239GB、4bit 約 466GB，因此想真正把它本地跑起來，更需要伺服器級記憶體、充足 SSD 和耐心，而不是一台普通遊戲 PC。

類型: 限制 | 日期: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Local NVFP4 Rust Port At 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (作者 [@mov_axbx](https://x.com/mov_axbx))

**如果你想估算一套調校後的本地 GLM-5.2 部署在真實 coding 工作裡能做到什麼，可以用這個案例，因為作者回報了 140 tok/s 的 NVFP4 推理速度，以及幾分鐘內完成的 Python 到 Rust 全量移植。**

mov_axbx 回報說，一套運行在 OMP 上的本地 GLM-5.2 NVFP4 配置達到了每秒約 140 tokens。貼文還說，這個模型在大約 10 分鐘內把一個 Python 衛星定位服務移植到 Rust，接著又在幾分鐘內搭出一個 demo web app。

類型: 評測 | 日期: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 Agent 主導雙棧 Bring-Up](https://x.com/TheValueist/status/2071261052080148607) (作者 [@TheValueist](https://x.com/TheValueist))

**如果你想評估一套嚴肅的自託管 GLM-5.2 部署範圍，可以用這個案例，因為整個 thread 展示了分析 agent 在不到一天內，於裸機 B300 上同時跑起 vLLM 與 SGLang 的 NVFP4 推理。**

TheValueist 表示，一套 analyst-agent workflow 在裸機 NVIDIA B300 x2 叢集上，分別透過 vLLM 與 SGLang 成功部署了 GLM 5.2 NVFP4，並在 24 小時內把兩套堆疊都跑完了一整組 benchmark。貼文還指出，真正的限制因素不是純算力，而是 HBM 容量；當 KV cache 溢出時，DRAM 也會開始變得關鍵。對於正在評估本地推理經濟性與硬體瓶頸的團隊來說，這是一條非常具體的營運層面訊號。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 Ultra Prefill 加速](https://x.com/jundotkim/status/2071287585297887510) (作者 [@jundotkim](https://x.com/jundotkim))

**如果你想在最近的 kernel 更新後重新檢查 Apple Silicon 本地跑 GLM-5.2 的可行性，可以用這個案例，因為回報中的 M3 Ultra 512GB prefill 速度幾乎翻倍，而且快速測試裡沒有明顯品質崩塌。**

jundotkim 表示，oMLX 0.4.5.dev1 新增的自訂 MLX kernels，讓 GLM-5.2-oQ4 在 M3 Ultra 512GB 上的 32k prefill 從 87.7 tok/s 提升到 174.4 tok/s，增幅達 98.9%。貼文也同時說明，這條路徑目前仍屬實驗性，但在 needle-in-a-haystack 檢查與 Claude Code 風格 coding 測試裡，沒有觀察到明顯退化，因此它更像是一則可操作的本地推理進展更新，而不只是單純的 release note。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [註冊即送 2000 萬 Token 額度爆發](https://x.com/Bitbro4crypto/status/2071150218872283262) (作者 [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**如果你想評估直接註冊拿到的免費額度，是否足夠支撐一次真正的 GLM-5.2 試用，可以用這個案例，因為貼文聲稱新帳號可拿到 2000 萬免費 tokens、免綁卡，並提供完整 OpenAI 相容接入。**

Bitbro4crypto 表示，目前的 GLM 5.2 註冊流程會送出 2000 萬免費 tokens、120 個圖片與影片 credits、high 與 max thinking modes、1M context window，以及可直接塞進 Cursor 或 Claude Code 等工具的 OpenAI 相容 API。這可作為一個很具體的短期接入與定價訊號，但也應假設這類促銷額度隨時可能變動。

Type: Integration | Date: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark 本地 GLM 操作手冊](https://x.com/TraffAlex/status/2071020631072616698) (作者 [@TraffAlex](https://x.com/TraffAlex))

**如果你想判斷 DGX Spark 叢集是否是現實可行的本地 GLM-5.2 路線，可以用這個案例。整理出來的指南把具體硬體成本、叢集拓撲和 vLLM 命令都對應到了 1M context 的 GLM 目標上。**

TraffAlex 匯總了社群驗證過的經驗和 NVIDIA 官方資料，表示每台設備售價為 4,699 美元，其他模型用 2x Spark 叢集最合適，而 4x Sparks 可以在 1M-token context 下以每秒大約 20 tokens 的速度運行 GLM 5.2 NVFP4。貼文裡還給出了 CX7 網路配置、passwordless SSH、NCCL 檢查以及示例 vLLM Docker 命令，所以它更像一份可落地的本地 deployment playbook，而不是泛泛的硬體觀點。

類型: 教程 | 日期: 2026-06-27

---

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
### Case 64: [Basement Local Inference Speed](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (作者 [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

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

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 跑分](https://x.com/0xSero/status/2069871347010838586) (作者 [@0xSero](https://x.com/0xSero))

**如果你在評估高階本地工作站方案，可以用這個案例把四卡 GLM-5.2 配置放到高難終端 benchmark 裡衡量。**

0xSero 回報，GLM-5.2-REAP-NVFP4 在 Terminal Bench 2.0 上跑到了 69.1%，並把它描述為所有能塞進 4x RTX PRO 6000 的模型裡 terminal-bench 成績最高的一檔。對於要權衡量化開放權重部署與託管前沿終端能力的團隊來說，這是一個很具體的本地部署訊號。

類型: 評測 | 日期: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell 本地 Crackme 解題](https://x.com/CardilloSamuel/status/2069887782508753302) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想判斷嚴肅的本地 GLM-5.2 配置能否在沒有 debugger 的情況下完成長時逆向任務，可以用這個案例。**

CardilloSamuel 表示，一個運行在 2x RTX PRO 6000 Blackwell 與約 300GB RAM 上的本地 GLM 5.2 實例，透過 OpenCode 在大約 78 分鐘內、以約 14 tokens per second 的速度解出了一道 crackme 挑戰。貼文還說，這套 harness 沒有提供 debugger 或 MCP 存取權限，但模型依然會主動傾印記憶體位址、驗證假設，並遵循要求去解題，而不是直接 patch 二進位。

類型: 演示 | 日期: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、注意事項與安全訊號
<a id="case-205"></a>
### Case 205: [Static HTML Rewrite Executor Misses](https://x.com/petruknisme/status/2075092910182387759) (作者 [@petruknisme](https://x.com/petruknisme))

**如果你不想把 1:1 legacy rewrite 完全交給 GLM-5.2 當 executor，可以看這個案例，因為一個大型 static HTML 到 React/Vite 的遷移在 OpenCode Go 和 Cline 上仍掉了太多細節，讓作者更傾向把 GLM 當 planner 而不是 executor。**

作者描述了一個大型 static HTML 專案改寫成 React 與 Vite 的過程，即使已經消耗了不少 OpenCode Go 和 Cline 的使用量，最後仍漏掉了太多 1:1 遷移需要保留的細節。它給出的實務結論是：在高保真 legacy migration 裡，可以讓 GLM 留在 planning loop，但 execution review 必須嚴格很多。

類型: 限制 | 日期: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Composio 47-Task Agent Gaps](https://x.com/composio/status/2074908761970393265) (作者 [@composio](https://x.com/composio))

**如果你想看 GLM-5.2 在真實 SaaS agent 工作裡還會在哪裡出錯，可以看這個案例，因為 Composio 把它接到 17 個工具、47 個任務上後，只通過了 45 個，主要失誤點在完整性檢查和模糊 SLA 判斷。**

Composio 說，GLM-5.2 和 Fable 5 都以 agent 形式跑在 17 個真實 SaaS 產品上，包括 GitHub、LaunchDarkly 和 Zendesk。GLM-5.2 完成了 47 個任務中的 45 個，而 Fable 5 是 47 個全過。trace 複盤指出了兩個具體失效模式：在一個本應找到 130 個結果的 GitHub secret audit 上提早停下，以及在 Zendesk SLA breach 判斷上雖然輸出結構很好看，但分類仍然做錯。

類型: 評測 | 日期: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [Preliminary Cyber Research Parity](https://x.com/Irregular/status/2072682835798831168) (作者 [@Irregular](https://x.com/Irregular))

**如果你想衡量 GLM-5.2 在漏洞研究子任務上的能力，可以看這個案例，因為 Irregular 報告說，在一組範圍很窄的 cyber suite 上，它的早期內部評估可與 GPT-5.4 和 Opus 4.6 接近，同時也明確提醒 end-to-end 攻擊情境尚未測試。**

Irregular 說，在一組有限的內部漏洞研究任務中，GLM-5.2 在已測子集上的表現大致接近 GPT-5.4 和 Claude Opus 4.6。貼文同時補充，這組 suite 很窄，而且像 CyScenarioBench、FrontierCyber 這類 scenario-level benchmark 還沒有跑。它比較像是一個真實的早期 cyber 能力訊號，而不是完整 offensive-agent 對等的證明。

類型: 限制 | 日期: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter Spend-Cut Skill Rewrite](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (作者 [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**如果你想在切換 agent 模型前把遷移成本算清楚，可以看這個案例，因為某個基金團隊的 OpenRouter 試驗裡，GLM-5.2 的成本大約只有 Opus 的八分之一，但依然要重寫 skill、補 routing 邏輯，還得接受更慢、更弱一些的輸出。**

Rahul J Mathur 說，他們團隊的 agent 之前基本只跑在 Opus 模型上，年化開銷大約在 10 萬美元級別，後來在 6 月開啟了一次 OpenRouter 多模型試驗，目標是把支出壓低約 40%。按他的第一手觀察，GLM-5.2 比 Opus 4.8 更慢，也更容易在邊界條件或完整讀取 skill file 這類地方出錯，但從接收方視角看，輸出品質在成本只有約八分之一時仍然可以接受。同一個貼文還提醒，面向 Opus 和 GPT 寫的 skill 並不能直接平移，遷移過程需要更新 skill、重新建立使用習慣，並補上硬編碼的 routing 邏輯。

類型: 限制 | 日期: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA Verbosity And Reasoning Tradeoff](https://x.com/ArtificialAnlys/status/2072022576394821859) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想把 GLM-5.2 的 frontier 級 open-weight 智力表現和它的推理效率成本拆開看，可以用這個案例，因為 Artificial Analysis 一邊把它列為開源權重最強，一邊也指出它消耗了異常多的輸出 token。**

Artificial Analysis 表示，GLM-5.2 Max 為了跑完 Intelligence Index，大約用了 1.41 億輸出 tokens，其中 95% 是 reasoning tokens。這個數字高於 Opus 4.8 的 1.17 億和 GPT-5.5 的 7200 萬，但貼文依然把 GLM-5.2 視為最強 open-weight。

類型: 評測 | 日期: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR 狹義勝出提醒](https://x.com/leploutos/status/2071121981551047039) (作者 [@leploutos](https://x.com/leploutos))

**如果你想把真正的安全訊號和誇大的標題敘事分開來看，可以用這個案例，因為來源指出 GLM-5.2 只是在一個 IDOR benchmark 上贏過 Claude Code，並沒有直接對上 Mythos。**

leploutos 表示，網路上流傳的「GLM 等於 Mythos」這種解讀是錯的：Semgrep 的結果其實只是一個 IDOR detection benchmark，GLM-5.2 的 F1 分數是 39%，高於 Claude Code 各種配置的 28-37%，單個 bug 成本約 0.17 美元，大約只有前沿模型成本的六分之一。貼文也清楚標出對實務最重要的限制：這只是單一漏洞類型、單一資料集、單次執行，而且 benchmark 由供應商持有。因此，這應被視為一個狹義但真實的漏洞檢測訊號，而不是 GLM 已經追平 Anthropic 專用 cyber model 的證明。

Type: Limit | Date: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 推理效率差距](https://x.com/scaling01/status/2070961852008509918) (作者 [@scaling01](https://x.com/scaling01))

**如果你想先檢查 GLM-5.2 在高推理負載任務上的表現，再決定是否把編碼優勢外推到其他場景，可以用這個案例。貼文裡的 LisanBench 結果顯示它雖然比 GLM-5 好，但相較其他開源模型仍然不夠高效。**

scaling01 表示，GLM-5.2-high 在 LisanBench 上排第 29，得分 1834，而 GLM-5 的得分是 986.83。貼文還說，Kimi-K2.5 Thinking 用平均約 19K tokens 就能達到相近分數，而 GLM-5.2 大約要消耗 32K tokens，這說明它相比過去的 GLM 代際確實進步了，但在推理效率上仍然偏弱。

類型: 限制 | 日期: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench 領域錯配提醒](https://x.com/yuhasbeentaken/status/2070928066797351300) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想讓 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用這個案例，因為貼文把它較弱的 PrinzBench 分數和更強的軟體、工具使用 benchmark 做了對照。**

yuhasbeentaken 表示，GLM-5.2 在專注法律研究和困難 web search 的窄基準 PrinzBench 上只拿到 30/99，但在 SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0、MCP-Atlas 77.0、ProgramBench 63.7 等公開 benchmark 上表現更強。貼文把這種差異解釋為 domain fit 問題，而不是前後矛盾，並建議法律研究優先用更強的 proprietary model，coding 和 agentic execution 則繼續用 GLM-5.2。

類型: 限制 | 日期: 2026-06-27

---

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

<a id="case-126"></a>
### Case 126: [Rust 錯誤修復通過但回合數高 7 倍](https://x.com/BohuTANG/status/2069979942608425364) (作者 [@BohuTANG](https://x.com/BohuTANG))

**如果你想把 GLM-5.2 的 code quality 優勢，和目前的 agent harness overhead 分開來看，可以用這個案例。它能修好 bug，但會比 Opus 消耗得多得多。**

BohuTANG 用同一個 Rust bug，也就是 serde_json issue 979，在 evot、Claude Code、Pi 這 3 個 agents 上比較了 GLM-5.2 與 Opus 4.6。6 個 sessions 全部 pass，作者也表示 GLM 的 bug 理解與最終 code quality 都沒有問題；但 GLM 分別用了 38、43、61 個 turns，而 Opus 在 3 個 agents 上大約 18 個 turns、80 秒左右就結束。trace notes 把這個差距歸因於反覆處理 cargo 與環境、收斂性不佳，以及明顯更長的 self-verification loops。

類型: 評測 | 日期: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust 模型替換成本警示](https://x.com/ankrgyl/status/2069869387549446597) (作者 [@ankrgyl](https://x.com/ankrgyl))

**用這個案例避免想當然地認為，在真實 agentic coding workflow 裡把模型換成更便宜的選項後，品質還能維持不變。**

ankrgyl 表示，Braintrust 對一個從儲存庫 commit 和 bug 描述出發、再評估最終修復結果的工作流，比較了 Opus 4.8 與 GLM-5.2。在這種基礎替換實驗裡，GLM-5.2 的成本相近、執行時間更長、通過率更低，因此整體效率反而更差。

類型: 評測 | 日期: 2026-06-24

---


<a id="acknowledge"></a>
## 🙏 致謝

本倉庫來自公開分享 GLM-5.2 使用證據的創作者、開發者、benchmark 團隊、供應商與社群。

感謝這裡收錄的高訊號來源創作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)、[@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)、[@ScaleAILabs](https://x.com/ScaleAILabs)、[@wafer_ai](https://x.com/wafer_ai)、[@ankrgyl](https://x.com/ankrgyl)、[@vedovelli74](https://x.com/vedovelli74)、[@clairevo](https://x.com/clairevo)、[@AlicanKiraz0](https://x.com/AlicanKiraz0)、[@denizirgin](https://x.com/denizirgin)、[@Dracoshowumore](https://x.com/Dracoshowumore)、[@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar)、[@OkhayIea](https://x.com/OkhayIea)、[@MrAhmadAwais](https://x.com/MrAhmadAwais)、[@0G_labs](https://x.com/0G_labs)、[@SubhoGhosh02](https://x.com/SubhoGhosh02)、[@undefinedKi](https://x.com/undefinedKi)、[@alighodsi](https://x.com/alighodsi)、[@composio](https://x.com/composio)、[@pengsonal](https://x.com/pengsonal)、[@EpochAIResearch](https://x.com/EpochAIResearch)、[@stagedhappen](https://x.com/stagedhappen)。

最近新增的創作者：[@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), [@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)、[@TraffAlex](https://x.com/TraffAlex)、[@FareaNFts](https://x.com/FareaNFts)、[@xpasky](https://x.com/xpasky)。

*我們無法保證每個案例都已歸屬到最初原創者。如果需要修正，請聯絡我們，我們會更新。*

如果你有更多值得收錄的 GLM-5.2 使用案例，歡迎提交 issue 或 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
