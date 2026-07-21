<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/en.jpg" alt="GLM-5.2 高シグナルユースケース集 banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=badge&utm_campaign=awesome-glm-5.2-usecases&utm_content=top_badge)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=docs_link)

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

# GLM-5.2 高シグナルユースケース集

## 🍌 概要

GLM-5.2 の高シグナルなユースケース集へようこそ。

**公開デモやクリエイターコミュニティから、GLM-5.2 の実例、チュートリアル、統合、評価、価格シグナル、制約を収集しています。**

このローカライズ版 README は、具体的なワークフロー、公開ベンチマーク、実演デモ、統合、コスト、実用上の注意点を持つケースに焦点を当てています。

各ケースのタイトルは公開ソースへ、作者ハンドルは作者プロフィールへリンクしています。

[Evolink で GLM-5.2 を試す](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases&utm_content=introduction_cta)

## 📊 Overview

- **258 件の厳選 GLM-5.2 ケース**を、公開クリエイター、ベンチマークチーム、ツール開発者、プロバイダー、実利用者から収集しています。
- ベンチマークとフロンティア評価、コーディングエージェントと長文脈ワークフロー、実演デモとショーケースビルド、プロバイダ・ツール統合、コスト、価格、ローカル運用、制約、注意点、安全性シグナルを扱います。
- 各ケースには元ソース、作者クレジット、簡潔な活用ポイント、エビデンスタイプ、公開日を含めています。
- 実用ワークフロー、強みと限界の比較、プロバイダ経路、実際の検証例を探すために使ってください。

> [!NOTE]
> このコレクションは hype よりも具体的な証拠を重視します: 公開デモ、ベンチマーク方法、統合メモ、コストデータ、明示された caveat です。

> [!NOTE]
> ローカライズ版 README は英語版と同じケース順、リンク、anchor、帰属を維持します。追跡性を優先するため、ケースタイトルは原文に近い表記を残す場合があります。

<a id="quick-start"></a>
## ⚡ Quick Start

[EvoLink で GLM-5.2 を開く](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=model_link).

Evolink の OpenAI 互換 Chat Completions API から GLM-5.2 を使用できます。[API キーを取得](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) で API key を取得し、実行前に `EVOLINK_API_KEY` として設定してください。

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

GLM-5.2 API の完全なリファレンス: [GLM-5.2 API docs を開く](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run).

## 📑 メニュー

| セクション | ケース |
|---|---|
| [📏 ベンチマークとフロンティア評価](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207, 217, 223, 227, 235, 248, 250 |
| [💻 コーディングエージェントと長文脈ワークフロー](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194, 210-212, 228, 236-237, 243, 255, 257 |
| [🎮 実演デモとショーケースビルド](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202, 213, 218, 229 |
| [🔌 プロバイダ・ツール統合](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208, 214, 219-220, 224-225, 230-232, 238-239, 256, 258 |
| [💸 コスト、価格、ローカル運用](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209, 215, 221, 226, 233-234, 240-246, 249, 251, 253-254 |
| [🧭 制約、注意点、安全性シグナル](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205, 216, 222, 247, 252 |
| [関連リポジトリ](#related-repositories) | 検証済み API ルートと関連サーフェス |
| [🙏 謝辞](#acknowledge) | クレジットと修正ポリシー |

### [📏 ベンチマークとフロンティア評価](#benchmarks-frontier-evaluation)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 250: ToolEval FP16 Indexer 向上](#case-250) | このケースは、生の API baseline ではなく、fine-tune 済みローカル GLM-5.2 の tool use を benchmark したいときに使えます。volatilemarkts によると、753GB FP8 fine-tune と custom FP16 indexer により、SeraphimSerapis/tool-eval-bench が標準の GLM 5.2 API の 83 percent から 94 percent に上がったためです。 | Evaluation |
| [Case 248: Aikido 26-CVE ハーネス基準線](#case-248) | このケースは、chat demo ではなく実際の code-audit harness で GLM-5.2 を benchmark したいときに使えます。AikidoSecurity によると、26 件の既知 CVE を使った AI Code Analysis benchmark で、GLM-5.2 は pass@3 で 16 件を再発見し、max reasoning ではコスト約 1.3x でさらに 3 件増やしたためです。 | Evaluation |
| [Case 235: DiligenceBench 金融ハーネス上位](#case-235) | このケースは、公開株式リサーチ agent に対する GLM-5.2 の実力を評価したいときに使えます。karinanguyen によると、DiligenceBench では GLM 5.2 が上位に入り、この金融ハーネスが強いモデルをより高性能かつ低コストにできることを示したためです。 | Evaluation |
| [Case 227: Gargantua WebGL Raytracer 勝利](#case-227) | このケースは、物理寄りの単一ファイル browser build で GLM-5.2 を benchmark したいときに使えます。AlicanKiraz0 によると、GLM 5.2 Max は Gargantua geodesic raytracer 課題で、数値的正しさと real-time rendering discipline の両立によって比較対象を上回ったためです。 | Evaluation |
| [Case 223: Intelligence Index のトークン効率ギャップ](#case-223) | このケースは、長期的な benchmark workload 向けに GLM-5.2 の予算を見積もるときに使えます。Artificial Analysis によると、GLM-5.2 Max は Intelligence Index の 1 タスクあたり平均約 43K の output tokens を使い、Inkling は 25K、Kimi K2.6 と DeepSeek v4 Pro Max もそれより少なかったためです。 | Evaluation |
| [Case 217: EvalPlus レスキュールートが Fable 超え](#case-217) | このケースは、verifier 付きの二段モデル coding ルートを試したいときに使えます。gmi_cloud によると、最初に Opus 4.8 を走らせ、失敗時だけ GLM 5.2 FP8 を救援投入する構成で、凍結した EvalPlus 100 問のうち 94 問を解き、Fable 5 を 5 問上回りつつコストは約 47 パーセント低かったためです。 | 評価 |
| [Case 207: 安定した流体のブラウザ ベンチマーク](#case-207) | このケースは、algorithm-heavy な browser physics build で GLM-5.2 を比較したいときに使えます。AlicanKiraz0 が Stable Fluids の HTML benchmark を実行し、GLM 5.2 Max に 100 点中 88 点、コスト約 1.17 ドルを付け、Opus 4.8 と Fable 5 を上回りつつ GPT 5.6 Sol は下回ったためです。 | Evaluation |
| [Case 199: エポックオープンウェイト指数リード](#case-199) | このケースは、GLM-5.2 を長期的な capability curve の中で位置づけたいときに使えます。Epoch AI が Capabilities Index で推定 152 を与え、評価済み open-weight model の中で最高だとしているためです。 | Benchmark |
| [Case 196: Databricks 内部ハーネスの評価](#case-196) | このケースは、GLM-5.2 を大規模な private engineering codebase 上で benchmark したいときに使えます。Databricks によると、3,000 人超の engineer の仕事を含む内部評価で GLM 5.2 は非常に強く、harness の選び方だけでコストを約 2x 下げられるためです。 | Evaluation |
| [Case 190: ネイチャーベンチ無差別級準優勝](#case-190) | このケースは、GLM-5.2 を scientific-agent workflow で benchmark したいときに使えます。NatureBench が、6 つの scientific domain、90 task において GLM-5.2 が総合 2 位かつ open-weight 首位で debut したと述べているためです。 | Benchmark |
| [Case 189: ターミナルとベンチの 45 タスクのコストのトレードオフ](#case-189) | このケースは、同じ agent harness で GLM-5.2 と GPT-5.5 を比較したいときに使えます。45 件の Terminal-Bench で GLM-5.2 が 25 勝、GPT-5.5 が 29 勝となり、GLM は prompt caching 込みで約 40% 安かったためです。 | Evaluation |
| [Case 188: Harvey LAB-AA 法務エージェント ネクタイ](#case-188) | このケースは、GLM-5.2 を実際の法務エージェント業務で benchmark したいときに使えます。Harvey LAB-AA で GLM-5.2 Max が 24 の practice area、120 の private task で Claude Opus 4.8 と同率の 7.5% all-pass を出しているためです。 | Benchmark |
| [Case 184: AutomationBench-AA オープンウェイト リード](#case-184) | このケースは、GLM-5.2 を coding benchmark だけでなく business rule を守る SaaS automation で比較したいときに使えます。Artificial Analysis が AutomationBench-AA で GLM-5.2 Max を 27.8% と報告し、open weights では首位だと述べているためです。 | Evaluation |
| [Case 178: Three-Body Simulator ベンチマーク勝利](#case-178) | このケースは、数値物理を含むコーディングベンチマークで GLM-5.2 を比較したいときに使えます。AlicanKiraz0 がカオス的な三体シミュレータ課題を走らせ、GLM 5.2 Max に 100 点中 91 点の最高評価を付けたためです。 | Evaluation |
| [Case 167: GameDevBench 333-タスク オープンソース リード](#case-167) | このケースは、エージェント型のゲーム開発ベンチマークで GLM-5.2 を追うのに役立ちます。GameDevBench は 333 タスクまで拡張され、GLM-5.2 が視覚機能なしでも leaderboard 上で最強の open-source model だと述べています。 | Evaluation |
| [Case 175: カーソル ダブル ペンデュラム スコアカード](#case-175) | このケースは、制約付きの Cursor coding benchmark で GLM-5.2 を比較したいときに使えます。AlicanKiraz0 は HTML の double-pendulum simulator で 6 モデルを比較し、GLM 5.2 Max に 100 点中 88 点を付け、Fable と Sonnet には届かなかったものの、GPT-5.5、Kimi K2.7 Code、Composer を上回りました。 | Evaluation |
| [Case 162: VulcanBench 10 タスク 80% タイ](#case-162) | このケースは、cost と score の両方が重要な post-cutoff の実エンジニアリング課題で GLM-5.2 を比較するのに役立ちます。Morgan Linton によると、VulcanBench では GLM 5.2 High、Fable 5 Low、Sonnet 5 High が 10 repo で同じ 80 percent になり、GLM の cost は中間でした。 | Evaluation |
| [Case 159: SWE-再ベンチ 51.1 パーセント チェックポイント](#case-159) | このケースは、更新が続く SWE エージェント系リーダーボードで GLM-5.2 を追うのに向いています。最新の SWE rebench 投稿では 2.62 million tokens で 51.1 percent とされ、新しく加わった DeepSeek、MiMo、Qwen、Gemma より明確に上です。 | Evaluation |
| [Case 154: LaunchDarkly エッジケースで 40/41 で勝利](#case-154) | このケースは、チャット専用評価ではなく業務ツールを使うエージェント作業で GLM-5.2 を試すのに向いています。Composio によれば、GitHub、Jira、LaunchDarkly の 41 タスク中 40 を取り、保留承認のエッジケースを拾えたのは GLM だけでした。 | Evaluation |
| [Case 146: CyberBench 無差別級パッチ準優勝](#case-146) | GLM-5.2 を攻撃寄りの脆弱性発見とパッチ作成で測りたいならこの事例が役立ちます。CyberBench で 60 件の実在 OSS-Fuzz 脆弱性に対して総合 2 位になっているからです。 | Evaluation |
| [Case 1: 人工分析インテリジェンスインデックス](#case-1) | Artificial Analysis ポストを使用して、インテリジェンスとタスクあたりのコストに関して GLM-5.2 を他のオープンウェイトおよび独自のフロンティア モデルと比較します。 | Benchmark |
| [Case 2: コードアリーナフロントエンドランキング](#case-2) | このケースを使用して、アリーナ スタイルの比較によって判断される実際のフロントエンド コーディング タスクで GLM-5.2 を評価します。 | Benchmark |
| [Case 3: デザインアリーナ1位](#case-3) | このケースを使用して、GLM-5.2 がテキスト中心のコーディング ベンチマークだけではなく、デザインとコードのタスクを処理できるかどうかを判断します。 | Benchmark |
| [Case 4: FrontierSWEの結果](#case-4) | FrontierSWE の投稿を使用して、ソフトウェア エンジニアリング タスクに関して GLM-5.2 を GPT-5.5、Opus、および Fable スタイルのモデルと比較します。 | Benchmark |
| [Case 5: DeepSWE オープンソース リーダー](#case-5) | DeepSWE のケースを使用して、難しいソフトウェア エンジニアリングの評価タスク用の強力なオープン モデルとしての GLM-5.2 を理解します。 | Benchmark |
| [Case 6: ターミナルベンチが 80% 以上](#case-6) | 端末指向のコーディングおよびエージェント ワークフローについて GLM-5.2 を評価する場合は、このケースを使用してください。 | Benchmark |
| [Case 7: SWELancer と GPT-5.5 の比較](#case-7) | この SWELancer のケースを、タスクの成功、報酬、完了時間に関する GLM-5.2 と GPT-5.5 の具体的なマルチメトリクスの比較として使用します。 | Evaluation |
| [Case 8: BridgeBench パーフェクト スコア シグナル](#case-8) | このケースを使用して、リーダーボードをコーディングするだけではなく、根拠に基づいた複数ステップの推論に基づいて GLM-5.2 を検査します。 | Benchmark |
| [Case 9: BridgeBench 推論その 1](#case-9) | このケースを使用して、根拠のある推論タスクに関して GLM-5.2 をクローズド フロンティア モデルと比較します。 | Benchmark |
| [Case 10: KernelBench - ショートカットなしのハード](#case-10) | ベンチマークのゲインがショートカットではなく有効な実装動作によるものであるかどうかを確認する場合は、このケースを使用してください。 | Evaluation |
| [Case 11: ルーンスケープベンチの追い上げ](#case-11) | このケースは、ゲームのようなベンチマーク タスクにおける無重みモデルの進行状況を示す速い信号として使用します。 | Benchmark |
| [Case 12: BridgeBench の速度向上](#case-12) | このケースを使用して、インテリジェンスとともに速度が重要となる、レイテンシーに敏感なワークフローを評価します。 | Benchmark |
| [Case 60: KernelBench ハードおよびメガ GPU コーディング](#case-60) | このケースを使用して、KernelBench-Hard と KernelBench-Mega にわたる GPU カーネル コーディングで GLM-5.2 を評価します。オープン エージェント トレースにより結果が検査可能になります。 | Benchmark |
| [Case 70: DeepSWE Max-Effort オープンソース首位](#case-70) | 最大 effort 設定の DeepSWE で GLM-5.2 を追跡するためのケースです。公開リーダーボードでは open model 中 1 位、pass@1 は 44% と示されています。 | Benchmark |
| [Case 72: LLM Debate Benchmark 準優勝](#case-72) | コーディング以外でも GLM-5.2 を評価するためのケースです。敵対的な multi-turn debate で、max-reasoning variant が Claude 系に次ぐ 2 位となっています。 | Benchmark |
| [Case 76: AA-Omniscience hallucination rate](#case-76) | 不確実性の扱いを比較するためのケースです。公開された AA-Omniscience 結果では、GLM-5.2 の hallucination rate は複数の frontier model より低くなっています。 | Evaluation |
| [Case 90: GDPval-AA エージェント作業指数](#case-90) | コーディング専用のリーダーボードではなく、長期的な知識労働で GLM-5.2 を比較するためのケースです。 | Evaluation |
| [Case 94: ゲーム デベロッパー アリーナ 準優勝](#case-94) | ゲーム構築品質で GLM-5.2 を判断するためのケースです。Game Dev Arena で 2 位に入り、その順位ではオープンウェイト陣営の最上位になりました。 | Evaluation |
| [Case 120: PostTrainBench 信頼性首位](#case-120) | 見出しスコアだけでなく、84 タスクで failed run が 0 件だったという agent reliability も含めて GLM-5.2 Max を比較するためのケースです。 | Benchmark |
| [Case 121: Fireworks + Faros 211件リポジトリ課題評価](#case-121) | 公開 benchmark だけでなく private repo の実務 engineering task で GLM-5.2 を判断するためのケースです。公開値には score、speed、task あたりの cost が含まれています。 | Evaluation |
| [Case 110: AA-Briefcase タスク時間フロンティア](#case-110) | ベンチマークスコアだけでなく、1 タスクあたり時間も重要な長期知識労働で GLM-5.2 を比較するためのケースです。 | Benchmark |
| [Case 111: Code Arena Frontend 直接対決マージン](#case-111) | 単一の順位スクリーンショットではなく、ペアごとの直接対決結果から GLM-5.2 のフロントエンド優位を確認するためのケースです。 | Benchmark |
| [Case 113: SWE Atlas Codebase QnA 準優勝](#case-113) | 単一タスクの SWE リーダーボードだけでなく、Codebase QnA、テスト作成、リファクタリング全体で GLM-5.2 を追うためのケースです。 | Benchmark |

### [💻 コーディングエージェントと長文脈ワークフロー](#coding-agents-long-context-workflows)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 257: OpenCodex モデル切り替えワークフロー](#case-257) | このケースは、1 つの model に固定せず Codex 中心の coding loop の中で GLM-5.2 を切り替えて使いたいときに役立ちます。vista8 によると、OpenCodex では同じ環境のまま frontend design、backend work、ライブ X search に応じて GLM 5.2、Kimi K3、GPT-5.6 Sol、Grok 4.5 を切り替えられるためです。 | Integration |
| [Case 255: Hermes 11-Agent ハイブリッドラボ](#case-255) | このケースは、1 つの monolithic assistant ではなく、GLM-5.2 を含む役割ベースの multi-agent lab を組みたいときに役立ちます。MichaelGannotti によると、11-agent の Hermes 構成が DGX Spark、Ryzen workstation、cloud models 間で task を動的に振り分け、software、research、marketing、coordination を回しているためです。 | Integration |
| [Case 243: Hermes ハイブリッド API 同等運用](#case-243) | このケースは、自己ホストの GLM-5.2 coding agent を公式ルートと比較検証したいときに使えます。dangerm00se によると、4x RTX 6000 PCIe 上の Hermes と GLM-5.2 の hybrid は official API の 60 タスク中 59 件で一致し、3,149 tok/s の prefill、0.37 秒の warm TTFT、35.9 tok/s の decode を出したためです。 | Evaluation |
| [Case 237: LM Studio Bionic GLM エージェント](#case-237) | このケースは、ローカル優先の GLM-5.2 coding agent を評価したいときに使えます。chenzeling4 によると、LM Studio Bionic は GLM 5.2 にローカル document sandbox、inline code diff、rollback checkpoint、端末内 voice transcription を組み合わせているためです。 | Integration |
| [Case 236: Claude Code の Web 開発品質優位](#case-236) | このケースは、単純な完了速度ではなく初回生成時の Web 開発品質を比較したいときに使えます。Lumenix0 によると、Claude Code 上の GLM 5.2 は 3 つの実タスクで、Codex 上の GPT 5.5 を design quality と機能完成度で上回ったためです。 | Evaluation |
| [Case 168: Synthwave ハードスライス アンサンブル、$2.66](#case-168) | このケースは、GLM-5.2 を単独ではなく multi-model の coding ensemble に組み込んで試すのに向いています。TracNetwork によれば、GLM を含む Synthwave 構成は LiveCodeBench hard で 46.3 percent を約 2.66 ドルで出し、各 generator 単体を上回りました。 | Integration |
| [Case 228: OpenCode によるローカル agentic coding 基盤](#case-228) | このケースは、frontier サブスクに課金する前にローカル coding-agent stack を検証したいときに使えます。comma_ai によると、同社は Anthropic を内部スタックから外し、GLM 5.2 と OpenCode の組み合わせで agentic coding がより良く回るようになったためです。 | Demo |
| [Case 212: Dell Hub GLM Agent チュートリアル](#case-212) | このケースは、open-weight の学習ワークフロー向けに GLM-5.2 coding agent を立ち上げるときに使えます。juanjucm によれば、新しいガイドが Dell Enterprise Hub の GLM-5.2-FP8 カタログ追加と、そのモデルを中心にした agent のセットアップ手順をセットで示しているためです。 | Tutorial |
| [Case 211: 8xB200 Open-Weight レポートパイプライン](#case-211) | このケースは、GLM-5.2 をローカル寄りのレポート生成パイプラインで main writer に据えるときに役立ちます。TheZachMueller によれば、1 台の 8xB200 ノードを 4/4 に分割し、GLM 5.2 NVFP4 にレポート生成、Kimi K2.7 Code に retrieval を担当させることで、Claude API よりごく小さいコストで、より密度の高い 36 ページのレポートを出せたためです。 | Demo |
| [Case 210: Spettro の Liquid Glass マルチエージェント刷新](#case-210) | このケースは、multi-agent な web 改修の中で GLM-5.2 を調査負荷の高い frontend fixer として試したいときに役立ちます。spettrotoken によれば、Fable 5 と GPT-5.5 が失敗したあと、GLM 5.2 が統合済みの web scraping と data fetching ツールを使い、Firefox でも動く cross-browser な Liquid Glass 実装を出荷したためです。 | Demo |
| [Case 194: CuTeDSL カーネル スキル オープンソース](#case-194) | このケースは、GLM-5.2 を再利用可能な kernel-debugging skill の中で研究したいときに使えます。作者が CuTeDSL 向けの Hermes skill を open source 化し、kernel の debugging と writing で GLM-5.2 のコスト効率が特に良かったと述べているためです。 | Tutorial |
| [Case 180: Hermes SSDリカバリスキルループ](#case-180) | このケースは、修復志向の agent loop の中で GLM-5.2 を試したいときに使えます。ShankhadeepSho1 によると、Hermes と GLM 5.2 が故障した NAS SSD を診断し、問題を直したうえで、その修復方法を再利用可能な skill としてまとめたためです。 | Demo |
| [Case 174: ロールルーティングされた高耐久コーダー スタック](#case-174) | このケースは、役割ごとにルーティングする個人スタックで GLM-5.2 を重い coding 作業の担当に置くときに役立ちます。denizirgin は、Codex と OpenCode を 1 か月試した結果、月額 120 から 140 dollars 前後に抑えながら、より重い coding work を GLM 5.2 に回す運用に落ち着いたと述べています。 | Evaluation |
| [Case 155: Cotal 4 エージェント TUI ループ](#case-155) | このケースは、コーディングループを専門エージェントに分担させるのに使えます。著者は Opus のリードと GPT のレビュー役の下で GLM-5.2 ワーカーを 2 体使い、lazygit 風 TUI を 47 分で人手なしに仕上げました。 | Demo |
| [Case 153: レガシー移行のコスト削減パイロット](#case-153) | このケースは、レガシーアプリ刷新ループの中で GLM-5.2 を低コスト側の実行役として評価するのに使えます。8090 のパイロットでは、GLM と Software Factory の組み合わせが Opus 4.8 単体比で 16.4 倍安く、ただし約 3 倍遅いとされています。 | Evaluation |
| [Case 150: Mac Studio ブラウザ - ローカル ループの使用](#case-150) | 完全ローカルな GLM-5.2 スタックが consumer hardware 上で軽い browser agent 作業をこなせるか試したいならこの事例が役立ちます。作者は Mac Studio 上の llama.cpp と browser-use で Hugging Face の PII モデルを探しました。 | Demo |
| [Case 148: Gumloop エージェントスワップコスト削減](#case-148) | 既存の agent harness の中で単純なモデル差し替えを試したいならこの事例が役立ちます。Gumloop は GLM-5.2 へ移した後、品質低下をほぼ感じずに credit 消費を約 50% 下げたと言っているからです。 | Evaluation |
| [Case 13: 1 時間 42 分のリファクタリング ループ](#case-13) | このケースは、TDD、レビュー担当者のフィードバック、回帰チェックによる長時間にわたる自律的なフロントエンド リファクタリングのパターンとして使用してください。 | Demo |
| [Case 14: OpenCode のバグ修正と実装テスト](#case-14) | このケースを使用して、バグ修正と小規模な実装タスクのための OpenCode コーディング エージェントとして GLM-5.2 をテストします。 | Demo |
| [Case 15: OpenCode レトロ ビデオ ゲームのウォークスルー](#case-15) | このチュートリアルを使用して、単一のプロンプトから GLM-5.2 と OpenCode を使用して小規模なゲームを構築し、モデルが実装の詳細をどのように処理するかを検査します。 | Tutorial |
| [Case 16: HTML5 物理シミュレーション コンテスト](#case-16) | このケースを使用して、ライブラリを使用しない自己完結型 HTML5 物理シミュレーションで GLM-5.2 コードと Kim K2.7 コードを比較します。 | Evaluation |
| [Case 17: 個人サイトのUI UXの構築](#case-17) | このケースを使用して、GLM-5.2 に洗練された個人サイトを求め、複数のターンで UI/UX がどの程度改善されるかを検証します。 | Demo |
| [Case 18: AI 契約レビュー製品ビルド](#case-18) | このケースを使用して、PRD、時間予算、ステップ数、使用量割り当て、およびコード品質の比較を使用して製品構築タスクで GLM-5.2 を評価します。 | Evaluation |
| [Case 19: より大きな開発目標のための ZCode 目標機能](#case-19) | このケースを使用して、大規模なエージェント開発タスクのために GLM-5.2 がどのように ZCode 3.0 に統合されるかを理解してください。 | Integration |
| [Case 20: GLM-5.2 で構築された ZCode 用 Linux ラッパー](#case-20) | このケースは、コーディング エージェント環境に関するツールを支援する GLM-5.2 の例として使用してください。 | Demo |
| [Case 21: コンピュータ使用スキルのパッケージ化](#case-21) | このケースを使用して、オープンソースのコンピューター使用リポジトリを再利用可能なスキルに変えるためのヘルパーとして GLM-5.2 を検討してください。 | Demo |
| [Case 22: ZCode 3.0 エージェント開発環境のレビュー](#case-22) | このケースを使用して、単一のチャット セッションではなく完全なエージェント開発環境内で GLM-5.2 を評価します。 | Demo |
| [Case 62: ローカルサービスを備えた OpenCode ハーネス](#case-62) | このケースを使用して、Claude Opus と比較する前に、OpenCode ハーネス、ローカル サービング、およびツールを多用するコーディング ワークフローを使用して GLM-5.2 をテストします。 | Evaluation |
| [Case 65: Fast-RLM ロングコンテキスト命令インジェクション](#case-65) | このケースを使用して、指示を RLM システム プロンプトに移動することで、GLM-5.2 のロング コンテキストのカウントと REPL エージェントの動作を改善します。 | Integration |
| [Case 66: DeepAgents コード オープン ハーネス トライアル](#case-66) | このケースを使用して、オープン コーディング エージェント ハーネスで GLM-5.2 を試し、再現可能なエージェント シェルでモデルを比較します。 | Demo |
| [Case 77: 本番マーケティング agent stack のルーティング](#case-77) | 構造化、速度、self-hosting を重視する production agent workflow に GLM-5.2 を割り当てつつ、曖昧な判断はより強い closed model に任せるためのケースです。 | Evaluation |
| [Case 80: M3 ウルトラポケモンレッド ゴールラン](#case-80) | M3 Ultra 上での長時間ローカル coding agent 実行において、GLM-5.2 を評価するためのケースです。約半日かけて Pokemon Red を HTML で再現しようとした実例を追えます。 | Demo |
| [Case 91: Cline Repo バグ修正対決](#case-91) | 実際のリポジトリのバグ修正で GLM-5.2 と Opus 4.8 を比較するためのケースです。GLM はより多くのトークンを使いましたが、より安価でクリーンな最終パッチを出しました。 | Evaluation |
| [Case 102: OpenInspect FP8 バックグラウンド エージェント](#case-102) | ホスト型チャットではなく、GLM-5.2 を FP8 で回すセルフホストの background-agent stack を調べるためのケースです。 | Integration |
| [Case 145: OpenCode と Fireworks へのコスト削減移行](#case-145) | open-model harness への切り替えだけで十分か確かめたいならこの事例が役立ちます。作者は個人の coding と loop task を Fireworks 上の GLM-5.2 + OpenCode に移し、日常品質をほぼ保ったまま token コストが 3 分の 1 になったと言っているからです。 | Evaluation |
| [Case 143: Hermes MoA の GLM アグリゲーターワークフロー](#case-143) | 価値の高い agent の 1 ターンに追加のオーケストレーションをかける価値があるなら、この事例が役立ちます。Hermes Agent の Mixture of Agents 構成は、GLM-5.2 と他モデルを組み合わせ、小さな追加コストで目に見えて良い出力を出したからです。 | Integration |
| [Case 142: Cline の推論オン/オフによるハーネス差分](#case-142) | モデルの重みだけでなく harness 設計を見たいならこの事例が役立ちます。同じ GLM-5.2 が同じ coding task で、reasoning を有効にしただけで 57.3% から 68.5% に伸びたからです。 | Evaluation |
| [Case 136: カーソル + Fireworks 455M トークンのフィールド テスト](#case-136) | 高速な Fireworks 提供と 4.55 億 tokens の実運用を作者が報告しており、すぐに Opus や GPT-5.5 に戻る気がないとしているため、GLM-5.2 を Cursor の本格的な常用モデルとして判断するためのケースです。 | Evaluation |
| [Case 135: スキルポータビリティを備えた Devin デスクトップ ハーネス](#case-135) | Z.ai 自身の coding surface が不安定に感じられるときに、GLM-5.2 を Devin Desktop 内で試すためのケースです。作者は、より簡単な skill 移植、高速さ、そして hackability の高さを報告しています。 | Evaluation |
| [Case 127: Pi インライン GLM レビュアー](#case-127) | Pi スタイルの coding-agent loop に第 2 のレビュー担当を加えたいときに使うケースです。作者によれば、GLM-5.2 は Opus に turn ごとに助言でき、コスト増はおよそ 10% に収まるとのことです。 | Integration |
| [Case 122: AgentRouter による一発 Telegram Bot](#case-122) | 最低限動くだけのコードではなく、本番運用を意識した default を GLM-5.2 が one-shot の coding-agent build で自力推論できるか試すためのケースです。 | Demo |
| [Case 117: OpenCode Go リファクタリング初回成功](#case-117) | ベンチマーク主張だけに頼らず、OpenCode 内の中規模 Go リファクタリングで GLM-5.2 を評価するためのケースです。 | Evaluation |
| [Case 119: Claude Code + Cursor 3.36ドル常用実行](#case-119) | より自律的な coding work を open weights に移す前に、Claude Code と Cursor で日常利用モデルとしての GLM-5.2 を見極めるためのケースです。 | Evaluation |

### [🎮 実演デモとショーケースビルド](#hands-on-demos-showcase-builds)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 229: Hyperagent プロフィール・ポートフォリオ対決](#case-229) | このケースは、実際の browser-based agent タスクで GLM-5.2 を他の open model と比べたいときに使えます。arsh_goyal によると、GLM 5.2、DeepSeek V4、Kimi K2.6、Qwen 3.7 を Hyperagent 上で並列に走らせ、公開プロフィールから personal portfolio を作らせたためです。 | Demo |
| [Case 218: OpenCode によるポートフォリオと OS 再構築](#case-218) | このケースは、GLM-5.2 を野心的な OpenCode build で見極めたいときに使えます。MarkSShenouda によると、OpenCode Go と GLM-5.2 によって、portfolio site の再構築と、WASM または Qemu emulator で動く C / Assembly 製の本物の OS 開発が進んだからです。 | デモ |
| [Case 213: LlamaCoder v4 GLM 再構築](#case-213) | このケースは、GLM-5.2 の planning と design の強みを使って one-prompt app generation を試作するときに役立ちます。nutlope によれば、LlamaCoder v4 は GLM 5.2 を中心に再構築され、parsing と planning が改善され、現在は無料の open-source stack 上で WebAssembly renderer まで搭載しているためです。 | Demo |
| [Case 202: コマンドコードスペースシューター機能勝利](#case-202) | このケースは、one-shot の interactive UI build で GLM-5.2 を比べたいときに使えます。Command Code が同じ retro space-shooter prompt を Fable 5、GPT 5.5、GLM 5.2、DeepSeek V4 Pro に流し、features では GLM を最上位に置いたためです。 | Evaluation |
| [Case 200: ZCode ニンテンドー DS エミュレータ](#case-200) | このケースは、長時間にわたる local coding build を見たいときに使えます。作者が 4x RTX 6000 上の ZCode で GLM-5.2 を動かし、Nintendo DS emulator を C++ でゼロから作ることを目標にしたためです。 | Demo |
| [Case 192: コマンドコード Flappy Bird UX Split](#case-192) | このケースは、GLM-5.2 を軽い design-game task で比較したいときに使えます。作者が同じ Flappy Bird prompt を Command Code で流し、Fable 5 は GLM-5.2 の約 9 倍近い価格にもかかわらず UX で決定的優位を示さなかったと結論づけているためです。 | Evaluation |
| [Case 161: NVFP4 ルービック キューブ ワンショットを REAP](#case-161) | このケースは、単一プロンプトの対話型 build で GLM-5.2 を試すのに向いています。REAP-NVFP4 の demo では、1 回の prompt だけで 3D Rubiks Cube、実際の scramble、live state、solve button まで生成したと述べています。 | Demo |
| [Case 158: OMP リレー iPhone クライアント](#case-158) | このケースは、ローカル GLM-5.2 エージェントを素早くモバイル面に載せたいときに使えます。著者によれば、Codex の build-ios-app plugin が、すでに GLM-5.2 と Cloudflare トンネルを使う OMP relay 向けに、数時間で整った iPhone クライアントを作りました。 | Demo |
| [Case 144: オープンソースの DevRel リサーチエージェント](#case-144) | GLM-5.2 を汎用チャットではなく縦型の調査アシスタントに変えたいならこの事例が役立ちます。作者は、製品とオーディエンスの入力を根拠付きのコンテンツ候補とアウトラインに変えるオープンソース DevRel エージェントを作ったからです。 | Demo |
| [Case 123: Recast 6 バリエーションの LP 反復ループ](#case-123) | まず複数の GLM-5.2 案を作ってから最良案を coding agent に引き継ぎ、低コストで landing page を試作するためのケースです。 | Tutorial |
| [Case 23: プレイ可能なバックルーム ワンショット](#case-23) | このケースを使用して、GLM-5.2 と Opus 4.8 の間で同じプロンプトのゲーム構築の出力、ランタイム、コストを比較します。 | Demo |
| [Case 24: 結果がまちまちの 3 つの実際のビルド](#case-24) | このケースは、注意深いデモ セットとして使用してください。実稼働ゲームやビデオ タスクのモデルを信頼する前に、複数の実際のビルドをテストしてください。 | Evaluation |
| [Case 25: ZCode でのスーパー マリオ クローン](#case-25) | このケースを使用して、いくつかの修正と機能のパスにわたって GLM-5.2 と ZCode を使用した反復的なゲーム構築を評価します。 | Demo |
| [Case 26: 月着陸船コンテスト](#case-26) | このケースを使用して、インタラクティブなゲーム スタイルのタスクで GLM-5.2、MiniMax M3、および Kim K2.7 コードを比較します。 | Evaluation |
| [Case 27: ワンプロンプトのデザインアリーナの作成](#case-27) | このケースを使用して、GLM-5.2 がアリーナ コンテキスト内の単一のデザイン プロンプトから何を生成できるかを検査します。 | Demo |
| [Case 28: 研究論文のワークフローを理解する](#case-28) | このケースを使用して、状況に応じた質問や論文間の参照を含む論文読書ワークフローに GLM-5.2 を適用します。 | Integration |
| [Case 29: 制約された詩の比較](#case-29) | GLM-5.2 を寓話スタイルのモデルと比較する場合は、このケースを使用して、正確性とクリエイティブの品質を区別します。 | Evaluation |
| [Case 30: デザインセンスの例](#case-30) | このケースを軽量のビジュアル デザイン シグナルとして使用し、独自のプロンプトと UI レビューで検証します。 | Demo |
| [Case 71: Temple Run 風ボクセルゲームのワンショット生成](#case-71) | 単一プロンプトのゲーム生成で GLM-5.2 を stress-test し、視覚的にリッチなビルドで何が追加修正を要するかを確認するためのケースです。 | Demo |
| [Case 78: OpenCode Go ワンショット実例セット](#case-78) | より open-ended な agent loop に投入する前に、OpenCode Go 内の quick one-shot build で GLM-5.2 を benchmark するためのケースです。 | Demo |
| [Case 81: スペースインベーダーのワンプロンプトビルド](#case-81) | 単一プロンプトのゲーム生成で GLM-5.2 を試し、その後の数回の追加入力で asset 差し替えや軽い polish がどう進むかを見るためのケースです。 | Demo |
| [Case 82: OpenCode Recovery Lab ワンショット](#case-82) | 対話的な agent failure simulation を素早く試作するためのケースです。作者は約 3.50 ドルで動く recovery lab を one-shot で作れたと報告しています。 | Demo |
| [Case 92: オープンデザイン参照 URL 再構築](#case-92) | 参照ベースの Web 再現で GLM-5.2 を試すためのケースです。1 つのプロンプトと元 URL だけで、ほぼピクセルレベルの忠実さでサイトを再現しました。 | Demo |
| [Case 99: トレーダーデスクのコスト品質テスト](#case-99) | フルスタック UI 構築で GLM-5.2 を比較するためのケースです。最も洗練された取引デスク出力にかなり近づきながら、コストはそのごく一部に収まりました。 | Evaluation |
| [Case 100: クロードの拒否後のラッダイト・ゲーム](#case-100) | クローズドモデルが拒否したゲーム案を GLM-5.2 で代替試作し、実際に動く出力を自分で検証するためのケースです。 | Demo |

### [🔌 プロバイダ・ツール統合](#provider-tool-integrations)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 258: Orbit Provider 50% GLM アクセス](#case-258) | このケースは、個別の provider credentials を管理せずに Orbit 内で GLM-5.2 を試したいときに役立ちます。Orbit Editor v0.4.0 によると、新しい Orbit Provider が editor 内で GLM-5.2 を直接提供し、50 percent off で開始されたためです。 | Integration |
| [Case 256: pen.dev 並列デザイン評価](#case-256) | このケースは、1 つのローカル workflow 内で GLM-5.2 を design-oriented な競合と比較したいときに役立ちます。tomkrcha によると、pen.dev は ChatGPT、Claude、Cursor Composer、OpenCode Go、Kimi、Grok、Gemini、Qwen などと並列に GLM 5.2 を desktop codebase 上の design task へ流せるためです。 | Integration |
| [Case 239: TokenRouter 無料 GLM API 提供期間](#case-239) | このケースは、短期間だけ無料の GLM-5.2 API ルートを確保したいときに使えます。meliasiih によると、TokenRouter は 2026-07-25 まで、簡単な signup、API key 発行フロー、公開 base URL 付きで無料アクセスを提供しているためです。 | Tutorial |
| [Case 238: Agentuity Wafer GLM ゲートウェイ](#case-238) | このケースは、Agentuity gateway stack に GLM-5.2 を追加したいときに使えます。wafer_ai によると、この serverless ルートは Agentuity 上で GLM 5.2 を regular / Fast の両 tier で提供し、約 100 から 250 tok/s と 1M context を出しているためです。 | Integration |
| [Case 232: Macroscope Check Run GLM エージェント](#case-232) | このケースは、PR review agent のコストを下げつつ check-run workflow を維持したいときに使えます。kayvz によると、Macroscope の Check Run Agents は通常の `.md` ベース repo config から GLM 5.2 を選べるようになったためです。 | Integration |
| [Case 231: Aster の 281 TPS research-agent API](#case-231) | このケースは、高速な hosted GLM-5.2 endpoint を benchmark したいときに使えます。asterailabs によると、Aster Inference は research-agent 最適化由来の API で GLM 5.2 を 281 tokens per second で提供しているためです。 | Integration |
| [Case 230: TrueFoundry 向けネイティブ Wafer GLM ルート](#case-230) | このケースは、既存の TrueFoundry AI Gateway stack に GLM-5.2 を差し込みたいときに使えます。wafer_ai によると、native provider integration は GLM 5.2 と GLM 5.2 Fast から始まり、残りの gateway stack を変えずに使えるためです。 | Integration |
| [Case 170: NVIDIA 無料 API プラグアンドプレイ アクセス](#case-170) | このケースは、無償の hosted endpoint 経由で GLM-5.2 を素早く試すのに役立ちます。hqmank は NVIDIA が OpenAI 互換 API ルートを公開し、plug-and-play の差し替えとして動いたと確認しています。 | Integration |
| [Case 169: 無料の Workers AI コーディング エージェント ルート](#case-169) | このケースは、coding agent 向けに無料の GLM-5.2 ルートを立ち上げるためのものです。チュートリアルでは Workers AI を Claude Code、OpenCode、Cursor、Aider に、OpenAI 互換の `cf/zai-org/glm-5.2` endpoint 経由で接続しています。 | Tutorial |
| [Case 220: OpenMed の de-id 臨床エージェント](#case-220) | このケースは、GLM-5.2 を privacy-preserving な clinical agent flow の中に置きたいときに使えます。MaziyarPanahi によると、OpenMed が識別子をローカルで除去し、Gemma 4 が構造化を担当したあと、GLM 5.2 が症例全体を計画し、ツールを呼び、disposition まで書いたためです。 | 統合 |
| [Case 219: Katana の USDC GLM アクセスルート](#case-219) | このケースは、wallet ネイティブな pay-per-request ルートで GLM-5.2 を公開したいときに使えます。imgn_ai によると、Katana は Base 上の x402 を通じて、アカウント不要・USDC 決済・公開 llms.txt 付きで GLM-5.2 を提供しているためです。 | 統合 |
| [Case 214: Databricks AI Gateway GLM ルート](#case-214) | このケースは、agent tooling 内で GLM-5.2 への高速な managed access path を試すときに使えます。QCXINT_ によれば、Databricks AI Gateway が組織固有の base URL と token flow を発行し、非常に高速で 1M context に見える GLM 5.2 ルートを exposed した一方、backend identity はまだ未確認のままだからです。 | Integration |
| [Case 208: オープン分子ビューア エージェント スタック](#case-208) | このケースは、GLM-5.2 を open な scientific inspection workflow に組み込みたいときに使えます。MaziyarPanahi が Hugging Face Inference Providers 経由の GLM-5.2 を、llama.cpp 上の Qwen3-VL、Mol*、PydanticAI と組み合わせ、1 つの prompt で EGFR と erlotinib の構造を render して critique したためです。 | Integration |
| [Case 204: Perplexity Advisor WANDR コスト ベースライン](#case-204) | このケースは、routing された computer-use harness の中で GLM-5.2 の economics を見積もりたいときに使えます。Perplexity が GLM 5.2 plus advisor setup で WANDR 2.1x、Opus 6.1x と述べ、benchmark 全体でもほぼ半額だとしているためです。 | Evaluation |
| [Case 203: 同僚のオープンアーティファクトルーティング](#case-203) | このケースは、GLM-5.2 を enterprise artifact workflow に入れたいときに使えます。Coworker は Open Artifacts で docs、decks、PDF、spreadsheets、dashboards、apps を作れ、optimized router で token 使用量を約 5x 減らしつつ US-hosted GLM 5.2 を提供すると述べています。 | Integration |
| [Case 201: DotCode コンテキストのアップロード ワークフロー](#case-201) | このケースは、private coding sandbox の中で GLM-5.2 により豊かな project context を与えたいときに使えます。DotCode が GLM 5.2 対応に加えて、screenshot、image、CSV、PDF、source file、zip の upload を同じ filesystem-and-terminal workflow に流せるようにしたためです。 | Integration |
| [Case 221: SGLang TopK-V2 による B300 agentic serving](#case-221) | このケースは、long-context agent workload における本番 GLM-5.2 serving を benchmark したいときに使えます。lmsysorg によると、SGLang は 8xB300・batch size 1 でユーザー当たり 500 tok/s 超を達成しつつ、single-user interactivity を 18 から 34 パーセント改善したためです。 | 評価 |
| [Case 215: llm-d H200 Prefix-Cache ルート](#case-215) | このケースは、H200 上で GLM-5.2 の hosted serving economics を benchmark するときに使えます。RedHat_AI によれば、llm-d の Wide EP と prefix-cache routing によって、700B 超の GLM-5.2 ルートで 90 percent 超の cache reuse、3 秒未満の TTFT、100 万 output tokens あたり約 2 dollars を実現したためです。 | Integration |
| [Case 209: Colibri 25GB RAM スパース ストリーミング](#case-209) | このケースは、ローカル GLM-5.2 実験の新しい下限を把握したいときに使えます。techNmak が、Colibrì は NVMe から expert を streaming することで約 25GB RAM で 744B MoE を動かせる一方、最小構成では 0.05 から 0.1 tok/s 程度に留まると詳述しているためです。 | Demo |
| [Case 206: SGLang NVFP4 プロダクション スループット](#case-206) | このケースは、GLM-5.2 NVFP4 向けの本番 SGLang serving を見積もるときに使えます。公式の SGLang v0.5.15 release が、batch size 1 で 8x B300 なら user あたり 500+ tok/s、4x GB300 なら 450 tok/s に達したと述べているためです。 | Evaluation |
| [Case 198: Dahl 100M 無料 GLM エンドポイント](#case-198) | このケースは、クレジットカード不要の OpenAI-compatible route で GLM-5.2 を試したいときに使えます。Dahl Inference が GLM 5.2 FP8 向けに 100M free token を出し、key の作成方法と `/v1/chat/completions` の呼び方を示しているためです。 | Tutorial |
| [Case 195: NVIDIA 無料エンドポイント GLM セットアップ](#case-195) | このケースは、GLM-5.2 を self-hosting なしで coding tool に入れて試したいときに使えます。source が、無料 NVIDIA endpoint の流れで GLM-5.2 の API key を Claude Code、Cursor、Cline に入れる手順を示しているためです。 | Tutorial |
| [Case 193: 0G TeeML プライベート推論ルート](#case-193) | このケースは、GLM-5.2 を privacy-first な provider path に流したいときに使えます。0G が、GLM 5.2 は TeeML 上で TEE enclave の中に prompt を閉じ込めたまま動き、価格も公式ルートより低いと述べているためです。 | Integration |
| [Case 185: DuckDB Flock の Open-SQL PR](#case-185) | このケースは、GLM-5.2 を完全に open なローカル SQL analysis に持ち込みたいときに使えます。lhoestq によると、duckdb と flock の PR で GLM-5.2 が 100% open-source の data stack に入るためです。 | Integration |
| [Case 179: ワンキー 26 モデル API アクセス](#case-179) | このケースは、単一の OpenAI 互換プロバイダ経由で GLM-5.2 を試したいときに使えます。Alan_Earn によると、1 本の API key で GLM-5.2 を含む 26 モデルにアクセスでき、開始時に 26 ドル分のクレジットも付くためです。 | Tutorial |
| [Case 176: NVIDIA NIM OpenCode 思考のセットアップ](#case-176) | このケースは、thinking を明示的に有効にしたゼロコスト経路として NVIDIA の無料 NIM endpoint 経由で GLM-5.2 を OpenCode に接続したいときに使えます。Dracoshowumore は API key の取得手順、base URL、そして tool layer が function calls を引き受ける一方で GLM を enable_thinking=true で動かす OpenCode 設定を共有しています。 | Tutorial |
| [Case 165: モバイル エージェント コントロールを使用した ZCode の起動](#case-165) | このケースは、ZCode を GLM-5.2 の公式 coding surface として評価するのに役立ちます。launch report では、この無料の agentic IDE が Windows、macOS、Linux で動き、Telegram、WeChat、Feishu から project progress を確認できるとされています。 | Integration |
| [Case 160: OpenWiki 自動保守エージェント ドキュメント](#case-160) | このケースは、agent が読めるドキュメントを自動で最新化したいときに役立ちます。LangChain によると、OpenWiki はコード変更に合わせて repo docs を再生成・維持し、GLM 5.2 のような open model で動きます。 | Integration |
| [Case 152: FireConnect を介したファウンドリ PTU](#case-152) | このケースを使えば、エージェント用クライアントを書き直さずに企業向け Foundry 予算で GLM-5.2 を流せます。Fireworks によれば、FireConnect が Microsoft Foundry の PTU を Codex、OpenCode、Pi のフローにつなぐからです。 | Integration |
| [Case 147: Braintrust GLM 評価ワークベンチ](#case-147) | GLM-5.2 と Opus を同じ eval スタックで比べたいならこの事例が役立ちます。Braintrust と Baseten が、long-context の精度とコスト差を具体例つきで公開したからです。 | Integration |
| [Case 141: ClinePass のオープンウェイト定額購読](#case-141) | 複数のオープンウェイト coding model を 1 つの agent harness にまとめたいならこの事例が役立ちます。ClinePass は GLM-5.2 と関連モデルを、個別の provider key や請求管理ではなく月額固定で束ねているからです。 | Integration |
| [Case 137: コーディングエージェント向けの無料のGLM APIサービス](#case-137) | 登録なしで Hermes や他の coding agent で GLM-5.2 を試すためのケースです。共有サービスは短時間有効な API key を発行し、セットアップを軽量に保ちます。 | Integration |
| [Case 31: OpenCode Go の利用可能性](#case-31) | このケースを使用して、テキスト、1M コンテキスト、GLM-5.1 のような価格設定を使用して OpenCode Go ワークフロー内で GLM-5.2 の可用性を追跡します。 | Integration |
| [Case 32: Ollama クラウドの可用性](#case-32) | このケースを使用して、アクセス可能なオープンソースのコーディング モデル実験のために GLM-5.2 を Ollama Cloud にルーティングします。 | Integration |
| [Case 33: OpenRouter One API 呼び出しアクセス](#case-33) | プロバイダー ルーティングまたはマルチモデル スタックを比較する場合は、OpenRouter 経由で GLM-5.2 にアクセスする場合にこのケースを使用します。 | Integration |
| [Case 34: vLLM デイゼロ サポート](#case-34) | このケースを使用して、デイゼロ サポートを備えた vLLM を介して GLM-5.2 をセルフホストまたは提供します。 | Integration |
| [Case 35: Baseten 経由の Notion の可用性](#case-35) | このケースを使用して、Notion ワークフロー内で利用可能なオープンウェイト モデルとして GLM-5.2 を識別します。 | Integration |
| [Case 36: 花火のデイゼロの提供](#case-36) | このケースを使用して、ホスト型インフラストラクチャを必要とする GLM-5.2 ワークロードのサービス提供ルートとして Fireworks を評価します。 | Integration |
| [Case 37: Google Cloud モデル ガーデン リンク](#case-37) | このケースを使用して、Google Cloud 指向のデプロイメントおよびエージェント プラットフォームのコンテキストで GLM-5.2 を見つけます。 | Integration |
| [Case 38: ヴェニス プライバシー モード](#case-38) | プライバシー モード、TEE、またはエンドツーエンド暗号化が GLM-5.2 を試行する際の決定要因となる場合は、このケースを使用してください。 | Integration |
| [Case 39: コマンドコードの利用可能性](#case-39) | このケースを使用して、低コストのエントリー プランとロング コンテキスト コーディング機能を備えたコマンド コードで GLM-5.2 を試してください。 | Integration |
| [Case 40: ヌースポータルのヘルメスエージェント](#case-40) | このケースを使用して、Nous Portal および OpenRouter を介して GLM-5.2 を Hermes Agent ワークフローに接続します。 | Integration |
| [Case 41: io.net Day-Zero 立ち上げパートナー](#case-41) | 753B パラメータのロングコンテキスト モデルのコンピューティング支援型サービスを評価する場合は、このケースを使用してください。 | Integration |
| [Case 42: モジュラークラウドデイゼロサービス](#case-42) | このケースを使用して、プロバイダー規模でサービスを提供するロングコンテキスト GLM-5.2 のモジュラー クラウドを検討してください。 | Integration |
| [Case 61: OpenRouter によるカーソルのセットアップ](#case-61) | このケースを使用して、低コストのオープン モデル コーディング ワークフローのために OpenRouter を介して Cursor で GLM-5.2 を構成します。 | Tutorial |
| [Case 63: ビジュアルデザインのためのAmp Agentic Eyes](#case-63) | テキストのみのモデルでデザイン タスクのビジュアル レビュー サポートが必要な場合は、このケースを使用して GLM-5.2 と Amp カスタム エージェントを組み合わせます。 | Integration |
| [Case 69: Baseten による 100 万コンテキストの提供の高速化](#case-69) | Factory Droid、OpenCode、およびコーディング ハーネスでロング コンテキストの処理速度が重要な場合は、このケースを使用して GLM-5.2 を Baseten 経由でルーティングします。 | Integration |
| [Case 74: Web デザイン向け Browser Use QA subagents](#case-74) | text-only model に視覚確認が必要なとき、GLM-5.2 を Browser Use v2 の multimodal QA subagents と組み合わせ、反復的な website 修正に使うためのケースです。 | Integration |
| [Case 79: ZCode 公式 IDE の daily free tokens](#case-79) | 大きな daily token allowance と Cursor 風 workflow を備えた無料の公式 coding IDE として、ZCode 経由で GLM-5.2 にアクセスするためのケースです。 | Tutorial |
| [Case 83: Fireworks によるカーソルのセットアップ](#case-83) | Fireworks 経由で GLM-5.2 を Cursor に最小構成で接続し、独自クライアントコードなしで試すためのケースです。 | Tutorial |
| [Case 84: VulcanBench ZAI プロバイダーのサポート](#case-84) | 専用の ZAI provider 対応と API key 導線を備えたオープン benchmark harness で GLM-5.2 を走らせるためのケースです。 | Integration |
| [Case 85: OpenCode High/Max 推論のバリアント](#case-85) | OpenCode 内で GLM-5.2 の High / Max reasoning variant にアクセスしつつ、より安定した step-limit 処理も取り込むためのケースです。 | Integration |
| [Case 86: Z.ai コーディングエンドポイントの選択](#case-86) | GLM-5.2 の coding plan トラフィックを、汎用 API ではなく coding 最適化済みの Z.ai endpoint に向けるためのケースです。 | Tutorial |
| [Case 87: ZenMux の無料 GLM-5.2 API セットアップ](#case-87) | 無料の GLM-5.2 API key と base URL を取得し、Claude、Cursor、Hermes などに差し込むためのケースです。 | Tutorial |
| [Case 93: 番号コード GLM デフォルト](#case-93) | 標準エンドポイントと 1M コンテキスト用エンドポイントを分け、デフォルトモデル対応も備えた ncode と Noumena 系エージェント環境に GLM-5.2 を組み込むためのケースです。 | Integration |
| [Case 95: Baseten 経由のクロード コード](#case-95) | Baseten のキー、カスタム base URL、`~/.claude/settings.json` のモデル再マッピングを使って Claude Code 内で GLM-5.2 を動かすためのケースです。 | Tutorial |
| [Case 96: Deepsec Pi エージェントのデフォルト](#case-96) | セキュリティハーネス内で GLM-5.2 を試すためのケースです。`deepsec` は Pi agent のデフォルトモデルに採用し、競争力のある eval 結果を報告しました。 | Integration |
| [Case 101: Baseten + Droid ハーネスのクイックスタート](#case-101) | Baseten と Droid harness 経由で GLM-5.2 を素早く動かし、他の IDE にも流用できる短いセットアップ手順を得るためのケースです。 | Tutorial |
| [Case 104: OpenAI 互換の GLM API ワークフロー](#case-104) | reasoning control、tool calling、長文脈 retrieval、cost tracking を備えた OpenAI 互換 GLM-5.2 クライアントを Python で組むためのケースです。 | Tutorial |
| [Case 105: Perplexity Agent API 検索サンドボックス](#case-105) | search 対応の sandboxed agent を単一 API call で使いたいとき、Perplexity Agent API に GLM-5.2 を接続するためのケースです。 | Integration |
| [Case 109: Baseten の 280 TPS GLM API](#case-109) | プロバイダー遅延が重要なとき、Baseten が主張する GLM-5.2 の高速 serving を確認するためのケースです。sub-second の first-token time と高い decoding throughput が示されています。 | Integration |
| [Case 124: HuggingChat で作るサイトから HF Space 配置まで](#case-124) | HuggingChat での下調べから Hugging Face Spaces への static deploy まで、ほぼ無料の personal-site flow で GLM-5.2 を試すためのケースです。 | Tutorial |
| [Case 125: DigitalOcean Inference Engine 提供開始](#case-125) | 1M context model を自前でホストせずに、official provider access を managed infrastructure 経由で使いたいときのケースです。 | Integration |
| [Case 128: Cloudflare Workers AI での OpenCode セットアップ](#case-128) | 独自のモデルホストを用意せず、coding agent 向けの無料の OpenAI 互換ルートとして Cloudflare Workers AI 経由で GLM-5.2 を動かしたいときに使うケースです。 | Tutorial |
| [Case 129: Puter.js ノーセットアップのブラウザクライアント](#case-129) | API key、課金、バックエンド設定に触れる前に、ブラウザだけの試作で GLM-5.2 を試したいときに使うケースです。 | Tutorial |
| [Case 130: SiliconFlow 統合エンドポイントアクセス](#case-130) | 中国系と西洋系のモデルを free trial credit 付きの単一 OpenAI 互換 SiliconFlow endpoint にまとめて扱えると投稿が説明しているため、GLM-5.2 をより広い multi-model stack に組み込みたいときに使うケースです。 | Integration |
| [Case 115: Command Code Fast 120-250 Tok/S ティア](#case-115) | 最安の入口価格だけでなく、長期コーディング速度を重視するときに Command Code の高速な GLM-5.2 tier にアクセスするためのケースです。 | Integration |
| [Case 116: Vercel AI ゲートウェイ高速 GLM-5.2 API](#case-116) | サーバレス速度と明示的なトークン価格が必要なときに、Vercel AI Gateway 経由で GLM-5.2 Fast を使うためのケースです。 | Integration |

### [💸 コスト、価格、ローカル運用](#cost-pricing-local-deployment)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 254: 8x GB10 860K スパースサービング](#case-254) | このケースは、GB10 級 cluster 上で長文脈のローカル GLM-5.2 serving を benchmark したいときに役立ちます。light_foundry によると、sparse indexer と Int4-Int8Mix weights を使った 8x GB10 stack が、4K depth で 1,101 tok/s prefill、最大 860K tokens の serving、845K context での needle recovery を達成したためです。 | Evaluation |
| [Case 253: ハイブリッド 3/4/8-Bit ローカルトレードオフ](#case-253) | このケースは、BF16 に戻す前に強く量子化したローカル GLM-5.2 route の規模感を見積もりたいときに役立ちます。0xSero によると、hybrid 3/4/8-bit build でも Terminal-Bench 2.1 で 70.8 percent、GPQA Diamond で 88.89 percent、4x RTX 6000s で約 82 tok/s、task あたり約 0.22 cents を記録したためです。 | Evaluation |
| [Case 251: Ollama Pro の高負荷 GLM 予算](#case-251) | このケースは、定価ではなく heavy-task quota で flat-rate の GLM-5.2 subscription を見積もりたいときに使えます。iamcheyan によると、OpenCode Go の weekly quota では重い GLM-5.2 task を約 5 件しか処理できなかった一方、Ollama Pro の weekly pool ではおよそ 3 日分の継続的な GLM 作業をこなせたためです。 | Limit |
| [Case 249: Alibaba 統合トークンプラン](#case-249) | このケースは、provider ごとの残高ではなく、複数モデル向けの monthly access を比較したいときに使えます。Alibaba Cloud によると、Token Plan for Individuals は text、image、video tools にまたがる統合 credits を共有し、GLM-5.2 を対象の frontier text models に含めつつ、coupon 適用後の初月料金は 4 US dollars から始まるためです。 | Integration |
| [Case 246: 8x DGX Spark 400K クラスタ](#case-246) | このケースは、机上の GLM-5.2 cluster が hosted API 支出を置き換えられる境目を判断したいときに使えます。thelichhh によると、8 台の DGX Spark を 1TB unified memory の 1 台として束ね、全ノードに GLM-5.2 を載せて 400K context で動かしたためです。 | Demo |
| [Case 245: Pulsar CPU Expert Lane](#case-245) | このケースは、低 VRAM の GLM-5.2 local stack を試したいときに使えます。Giannisanii によると、Pulsar の CPU expert lane により、2 枚の 16GB GeForce と 1 台の NVMe、32GB RAM で GLM-5.2 744B の throughput が 1.6 tok/s から最大 2.8 tok/s まで上がったためです。 | Demo |
| [Case 244: Peezy Go 3K GLM 枠](#case-244) | このケースは、token 単価ではなく request cap で flat-rate の GLM-5.2 coding access を比較したいときに使えます。SerPepeXBT によると、Peezy Go plan は limit をリセットし、GLM 5.2 を 5 時間ごとに最大 3,000 requests まで使え、月額 10 dollar を維持しつつ初月は 5 dollar になったためです。 | Integration |
| [Case 242: ZenMux 249M Token Receipt](#case-242) | このケースは、定価ではなく実際の receipt で GLM-5.2 の経済性を確かめたいときに使えます。AstridWiegner によると、1 件の ZenMux Token Receipt には 2.49 億超の処理 tokens、元の料金 105.81 dollars、最終合計 0 dollars が記録されていたためです。 | Evaluation |
| [Case 241: Zro Pro 300M GLM トライアル](#case-241) | このケースは、予算を抑えて private hosted な GLM-5.2 agent 作業を試したいときに使えます。AndarkFomo によると、Zro Pro の promo により OpenAI-compatible access、EU infra、zero-retention 方針付きで、約 1 dollar でおよそ 300M GLM-5.2 tokens を使えるためです。 | Tutorial |
| [Case 240: DGX Station 256K デスクトップ推論](#case-240) | このケースは、デスクトップ級の GLM-5.2 配備規模を見積もりたいときに使えます。TheAhmadOsman によると、DGX Station 上の GLM 5.2 NVFP4 は 256K context で約 3,000 tok/s の prefill と 32 tok/s の decode を出したためです。 | Demo |
| [Case 234: Jatevo 割引 GLM アクセス](#case-234) | このケースは、公開価格付きの hosted GLM-5.2 アクセス経路をすぐに押さえたいときに使えます。JatevoId によると、GLM 5.2 は platform 上で input $1.40 / 1M、output $4.40 / 1M で提供され、対象 JTVO holder には 50% 割引があるためです。 | Integration |
| [Case 233: MI325x で 0.1 セント未満の GLM serving](#case-233) | このケースは、AMD hardware 上で self-hosted GLM-5.2 inference の予算を見積もりたいときに使えます。picocreator によると、4xMI325x 構成で GLM 5.2 を 1,482 tok/s、100 万 tokens あたり 0.10 ドル未満で提供できたためです。 | Demo |
| [Case 191: Hermes が構築した LiteLLM ローカル ラボ](#case-191) | このケースは、GLM-5.2 を coding agent として使いながら local inference lab を立ち上げたいときに使えます。source では Hermes Agent と GLM-5.2 が M3 Ultra 上で LiteLLM、Postgres、Prometheus、Grafana を組んだと述べているためです。 | Integration |
| [Case 187: デュアル M5 Max オフライン ドローンシップ シム](#case-187) | このケースは、完全 offline の Apple Silicon 上で GLM-5.2 agent がどこまでできるかを見積もりたいときに使えます。XavierLocalAI が、2 台の 128GB M5 Max を使って 753B 構成で droneship-landing simulator を 26 tok/s で書いていると報告しているためです。 | Demo |
| [Case 186: 5x DGX Spark プロダクション ハーネス](#case-186) | このケースは、5 ノードの DGX Spark 構成が production の GLM-5.2 workload に足りるかを見たいときに使えます。thatcofffeeguy が、400K context で single-stream 約 13.9 tok/s、3 lane 合計で 19.9 tok/s を live harness で報告しているためです。 | Demo |
| [Case 183: M3 ウルトラ ds4-eval Q4 チェックポイント](#case-183) | このケースは、Apple Silicon の単機 GLM-5.2 構成を ds4-eval で benchmark したいときに使えます。ivanfioravanti が、M3 Ultra 512GB マシンで q4 実行を約 16 tok/s、92 件中 76 件通過、所要 8 時間 53 分と報告しているためです。 | Evaluation |
| [Case 182: 4x RTX PRO 6000 ビルド ガイド](#case-182) | このケースは、本気のローカル GLM-5.2-594B 構成を見積もるときに使えます。QingQ77 が、4 枚の RTX PRO 6000、opencode 経由で公開する API、そして agent 作業用の sandbox VM を中心にしたハードウェアと運用の完全ガイドを共有しているためです。 | Tutorial |
| [Case 181: 4x DGX Spark QuantTrio ラン](#case-181) | このケースは、4 ノードの DGX Spark クラスタで GLM-5.2 QuantTrio がどこまで出るか見積もりたいときに使えます。Tech2Wild が 200K context、単一ストリームで 30 tok/s、6 並列で合計 60.5 tok/s を報告しているためです。 | Demo |
| [Case 177: シングル M3 Ultra 4 ビット ビデオ実行](#case-177) | このケースは、Apple Silicon の単体マシンで GLM-5.2 がどこまで実用になるかを見積もるのに役立ちます。ivanfioravanti は 1 台の M3 Ultra 512GB で 4-bit 実行を約 16 tok/s で示し、q2 の ds4-eval 動画がおよそ 17 tok/s であることと比較しています。 | Demo |
| [Case 173: AMD MI355X 2626 Tok/s ノード サーブ](#case-173) | このケースは、AMD hardware 上での高スループットな GLM-5.2 inference を見積もるのに役立ちます。wafer_ai によれば、MI355X は 1 ノードあたり 2626 tok/s、single-stream で 213 tok/s に達し、Blackwell より 2 倍以上低コストでした。 | Demo |
| [Case 172: Vercel Gateway 287 Tok/s サーバーレス](#case-172) | このケースは、serverless gateway 経由での実ユーザー向け GLM-5.2 レイテンシを見積もるのに役立ちます。wafer_ai は、GLM 5.2 Fast ルートが benchmark harness ではなく Vercel AI Gateway 上で 287 tokens per second に達したと述べています。 | Demo |
| [Case 171: ワンクリック RTX PRO 6000 導入](#case-171) | このケースは、隔離された hosted GLM-5.2 deployment の下限コスト感をつかむのに役立ちます。XciD_ によれば、GLM-5.2-NVFP4 は 8x RTX PRO 6000 上の Inference Endpoints で 1 クリック、1 時間 22 ドルで展開できます。 | Integration |
| [Case 166: 5x ASUS GX10 上のフル 744B](#case-166) | このケースは、極端な home-lab GLM-5.2 deployment を見積もるためのものです。著者によると、744B の full model が 5 台の ASUS GX10 上で full context 付きで動作し、real workloads 向けの causal harness にもすでに接続されています。 | Demo |
| [Case 164: 中国スタックでのエージェント ルート スワップ](#case-164) | このケースは、最高品質よりコスト圧力が重要なときに、mixed-model stack の agent layer へ GLM-5.2 を routing する参考になります。著者によれば、Sonnet を GLM-5.2 に置き換えると、その slot の input cost は 5 倍安くなり、品質低下は約 3 percent でした。 | Evaluation |
| [Case 156: 744B ローカル ハードウェア フロア](#case-156) | このケースを使えば、GLM-5.2 のローカル計画を現実的に見積もれます。情報源によれば、量子化しても 2bit で約 239GB、4bit で約 466GB あり、RAM や VRAM は 256GB 超が実用ラインになるからです。 | Limit |
| [Case 151: ローカル NVFP4 Rust ポート (140 Tok/s)](#case-151) | 調整済みローカル GLM-5.2 配置が実際の coding 作業で何をできるか見積もりたいならこの事例が役立ちます。作者は NVFP4 で 140 tok/s と、Python から Rust への全面移植を数分で終えたと報告しています。 | Evaluation |
| [Case 140: B300 x2 エージェント主導のデュアルスタック起動](#case-140) | 本格的なセルフホスト型 GLM-5.2 deployment の規模感を見積もるためのケースです。スレッドでは、分析 agent がベアメタル B300 上で vLLM と SGLang の両方に NVFP4 推論を 1 日未満で立ち上げています。 | Evaluation |
| [Case 139: oMLX M3 ウルトラ プレフィルのスピードアップ](#case-139) | 最近の kernel work 後に Apple silicon でのローカル運用可能性を再確認するためのケースです。M3 Ultra 512GB での GLM-5.2 prefill speed が、簡単なテストで品質を大きく落とさずほぼ倍増したと報告されています。 | Evaluation |
| [Case 138: 20M トークンのサインアップ クレジット バースト](#case-138) | 直接 signup でも実用的な GLM-5.2 試用ができるかを判断するためのケースです。投稿では、新規アカウントに 2000 万 free tokens、カード不要、完全な OpenAI 互換 access が付くとされています。 | Integration |
| [Case 131: 4x DGX Spark ローカル GLM 運用ガイド](#case-131) | DGX Spark クラスタが現実的なローカル GLM-5.2 の道筋かどうかを見極めるためのケースです。収集されたガイドは、具体的なハードウェア費用、クラスタ構成、vLLM コマンドを 1M context の GLM 目標に結び付けています。 | Tutorial |
| [Case 43: 出力トークンコストの比較](#case-43) | このケースを使用して、GLM-5.2 出力トークンの経済性を Opus、Fable、および GPT-5.5 スタイルのモデルと比較します。 | Evaluation |
| [Case 44: ローカルのニアフロンティアハードウェアの ROI](#case-44) | このケースを使用して、セルフホスティング GLM-5.2 のようなモデルがエージェントのヘビー ユーザーのハードウェア コストを返済できるかどうかを検討してください。 | Evaluation |
| [Case 45: 2 つの Mac スタジオ上の MLX](#case-45) | このケースを使用して、Apple ハードウェアおよび MLX 指向のセットアップ上で実行されるローカル GLM-5.2 を調べます。 | Demo |
| [Case 46: H100 月次ローカル展開請求](#case-46) | このケースは、サブスクリプションとセルフホスティングのどちらかを選択する前に、ローカル展開の前提条件を確認するためのコスト比較プロンプトとして使用します。 | Evaluation |
| [Case 47: 毎日のクレジットとクロードの交換請求](#case-47) | このケースを使用して、GLM-5.2 に関する無料クレジットと代替エージェントの物語を検証し、マーケティング上の主張と検証済みのワークロード適合性を区別します。 | Evaluation |
| [Case 48: 無料の ZCode トークン ウィンドウ](#case-48) | このケースを使用して、有料プロバイダーまたはローカル展開にコミットする前に、無料の ZCode 許容量を通じて GLM-5.2 をテストします。 | Integration |
| [Case 49: ZenMux 無料週間オファー](#case-49) | このケースを使用して、GLM-5.2 テスト用のタイムボックス化されたフリーアクセス ウィンドウを見つけます。 | Integration |
| [Case 50: crofAIのトークンごとの価格設定](#case-50) | このケースを使用して、ルートを選択する前に GLM-5.2 のサードパーティ プロバイダーの価格を比較します。 | Integration |
| [Case 51: API価格マージンの比較](#case-51) | GLM-5.2 を他のフロンティア ラボやオープン モデルと比較するときは、このケースを市場価格の批評として使用してください。 | Evaluation |
| [Case 64: 地下室のローカル推論速度](#case-64) | このケースを使用して、オフライン コーディングのセットアップを計画する前に、大容量メモリの Apple ハードウェアでのローカル GLM-5.2 推論スループットを見積もります。 | Demo |
| [Case 68: Unsloth の量子化されたローカル展開](#case-68) | このケースは、完全なモデルの重みが通常のローカル ハードウェアにとって大きすぎる場合に、量子化された GLM-5.2 デプロイメント パスを評価するために使用します。 | Tutorial |
| [Case 88: 2 つの M3 Ultra MLX 分散実行](#case-88) | より大きな Apple Silicon 構成を組む前に、2 台の M3 Ultra で分散 MLX 実行した GLM-5.2 8-bit serving の実態を見積もるためのケースです。 | Demo |
| [Case 89: ZCode乗数は9月まで削減](#case-89) | peak / off-peak の multiplier 引き下げ期間を使って、GLM-5.2 の plan credits を引き延ばすためのケースです。 | Integration |
| [Case 97: RTX PRO 6000 のローカル スループット](#case-97) | ハイエンドなローカル GLM-5.2 ワークステーションを見積もるためのケースです。Blackwell 2 枚のデスクトップで、4-bit 量子化ビルドの二桁デコード速度を維持しました。 | Demo |
| [Case 98: Mac Studio API ROI リアリティチェック](#case-98) | ローカル GLM-5.2 推論のために Mac Studio を買う意味があるかを現実的に確認するためのケースです。投稿された回収計算では、多くの利用者にとって API やプラン利用の方が有利です。 | Evaluation |
| [Case 106: LiteLLM ローカル停止保存](#case-106) | ホスト型 frontier API が停止や上限到達を起こしても、LiteLLM 経由でローカル GLM-5.2 に切り替えて納品を前に進めるためのケースです。 | Demo |
| [Case 107: 個人とチームのローカル ROI](#case-107) | ローカル GLM-5.2 デプロイが個人に見合うのか、より大きな開発チーム向きなのかを判断するためのケースです。 | Evaluation |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 実行](#case-112) | 高性能ワークステーションを組む前に、4 GPU のローカル GLM-5.2 構成を厳しい terminal benchmark に照らして見積もるためのケースです。 | Evaluation |
| [Case 118: 2x RTX PRO 6000 Blackwell でのローカル Crackme 解読](#case-118) | デバッガなしでも、本格的なローカル GLM-5.2 構成が長時間のリバースエンジニアリング課題を完了できるかを判断するためのケースです。 | Demo |

### [🧭 制約、注意点、安全性シグナル](#limits-caveats-safety-signals)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 247: ZCode デフォルト RCE 修正](#case-247) | このケースは、GLM-5.2 coding agent の sandboxing をより厳格にすべき根拠として使えます。weezerOSINT によると、1 回の prompt だけで ZCode が repo 内コードを default で full RCE 実行し、この問題は報告されて version 3.3.6 で修正されたためです。 | Limit |
| [Case 222: 本番向け GLM ガードレール警告](#case-222) | このケースは、GLM-5.2 coding agent の guardrail をより厳しくすべき根拠として使えます。mitsuhiko によると、このモデルは force-push、無断の Pulumi 変更、production database への接触に積極的だったためです。 | 制限 |
| [Case 216: KV-Cache Debugger エッジケース見落とし](#case-216) | このケースは、GLM-5.2 を clean-pass の benchmark 数字だけでなく、矛盾入力の扱いで試したいときに役立ちます。cyrilXBT によれば、KV-cache debugger の正面比較で、GLM は clean config では他モデルと同等だった一方、1 つの bad variable を見落とし、警告なしで 2.667x 間違った preset を出したためです。 | Evaluation |
| [Case 205: 静的 HTML Rewrite Executor が失敗する](#case-205) | このケースは、1:1 の legacy rewrite を GLM-5.2 に executor として丸ごと任せないために使えます。大きな static HTML から React/Vite への移行で OpenCode Go と Cline を使っても detail がかなり落ち、author が GLM を executor より planner 寄りに見るようになったためです。 | Limit |
| [Case 197: Composio 47 とタスク エージェントのギャップ](#case-197) | このケースは、GLM-5.2 が live SaaS-agent work でどこでまだ崩れるかを理解したいときに使えます。Composio が 17 の tool、47 task につなぎ、45 件は通した一方で、completeness check と曖昧な SLA judgment で失敗したためです。 | Evaluation |
| [Case 163: 予備的なサイバーリサーチパリティ](#case-163) | このケースは、vulnerability research の部分タスクで GLM-5.2 を測るためのものです。Irregular は、狭い cyber suite で GPT-5.4 と Opus 4.6 に近い初期内部評価を報告しつつ、end-to-end の attack scenario はまだ未検証だと明言しています。 | Limit |
| [Case 157: OpenRouter 支出削減スキルの書き換え](#case-157) | このケースは、エージェントモデルを入れ替える前に移行コストを見積もるのに役立ちます。あるファンドの OpenRouter 試行では GLM-5.2 が Opus の約 8 分の 1 のコストでしたが、skill の書き換え、routing ロジック、そして遅く弱い出力を受け入れる前提が必要でした。 | Limit |
| [Case 149: AA の冗長性と推論のトレードオフ](#case-149) | GLM-5.2 の frontier 級 open-weight 性能と reasoning 効率コストを切り分けたいならこの事例が役立ちます。Artificial Analysis が、open-weight 首位でありながら出力 token 消費が極端に大きいことも示しているからです。 | Evaluation |
| [Case 134: Semgrep IDOR Narrow-Win の警告](#case-134) | ソースによれば GLM-5.2 は 1 つの IDOR benchmark で Claude Code を上回った一方、Mythos 自体とは比較されていないため、実際の security signal と見出し先行の誇張を切り分けるためのケースです。 | Limit |
| [Case 132: LisanBench 推論効率ギャップ](#case-132) | reasoning 負荷の高い workload で GLM-5.2 を確認したいときに使うケースです。投稿された LisanBench 結果では GLM-5 より改善していますが、他の open model と比べるとまだ効率が低いことが示されています。 | Limit |
| [Case 133: PrinzBench ドメイン不一致の注意点](#case-133) | 弱い PrinzBench スコアと、はるかに強い software・tool-use benchmark を投稿が対比しているため、GLM-5.2 を法務調査ではなく coding と agent execution に集中させるためのケースです。 | Limit |
| [Case 52: ビジョンなしの警告](#case-52) | この場合は、GLM-5.2 がネイティブ ビジョン機能を必要とするワークフローにはあまり役に立たない可能性があることを覚えておいてください。 | Limit |
| [Case 53: 現実世界のエージェントギャップに関する警告](#case-53) | このケースを使用して、GLM-5.2 がデプロイされたすべてのエージェント タスクで最適な独自モデルに一致することを証明するベンチマークの勝利を読みすぎないようにします。 | Limit |
| [Case 54: 安全ガードレールに関する懸念](#case-54) | このケースは、機密性の高いドメインに GLM-5.2 を展開する前に安全性評価を実行するためのリマインダーとして使用してください。 | Limit |
| [Case 55: ベンチマーク方法論の批評](#case-55) | このケースを使用して、ヘッドラインの結果が GLM-5.2 を支持する場合でも、ベンチマーク手法に疑問を持ちます。 | Limit |
| [Case 56: ピーク時の遅延の懸念](#case-56) | このケースは、コーディング プランを切り替える前、またはクロード コード スタイルのワークフローを GLM-5.2 にルーティングする前に、プロバイダーの遅延をテストするために使用します。 | Limit |
| [Case 57: FutureSim の非改善結果](#case-57) | このケースを使用して、広範囲に展開する前に、コーディングの利点が非コーディング ドメインに一般化するかどうかを確認します。 | Limit |
| [Case 58: 立ち上げ準備の批評](#case-58) | このケースを使用して、モデルの機能を起動の実行、ドキュメント、API の準備から分離します。 | Limit |
| [Case 59: コーディングプランの値上げ](#case-59) | GLM-5.2 を低コストの代替品として推奨する前に、このケースを使用してプランの価格を確認してください。 | Limit |
| [Case 67: 短い並列作業と長いエージェント実行](#case-67) | このケースを使用して、GLM-5.2 を短期間のコーディング タスクにルーティングしながら、より深い数時間にわたるエージェント実行用に強力なモデルを確保します。 | Limit |
| [Case 73: コード検閲とバイアスのチェック](#case-73) | コードと政治的バイアス検証の実用的な safety signal として使うためのケースであり、広範な alignment 上の懸念が解決済みだと示すものではありません。 | Limit |
| [Case 75: 高難度推論での課金 failure](#case-75) | hard reasoning workload に対して GLM-5.2 を慎重に試すためのケースです。公開報告では長い実行時間、低い完了率、予想外に高い課金出力量が示されています。 | Limit |
| [Case 103: HalluHard マルチターン幻覚信号](#case-103) | 他のベンチマーク成績を信頼しすぎる前に、幻覚に敏感なマルチターンタスクで GLM-5.2 を検証するためのケースです。 | Limit |
| [Case 108: オープンウェイトセキュリティ緊急警告](#case-108) | 安全計画のシグナルとして、open-weight の GLM-5.2 が offensive security agents の運用摩擦を下げる点を確認するためのケースです。 | Limit |
| [Case 126: Rust バグは通るがターン数は 7 倍](#case-126) | GLM-5.2 の code quality の強みと、現時点の agent harness overhead を切り分けて考えるためのケースです。bug 自体は通せても Opus より大幅に多くの turns を消費します。 | Evaluation |
| [Case 114: Braintrust モデル差し替えコストの注意点](#case-114) | 実際の agentic coding workflow で、安価なモデルへの差し替えが品質を保つと安易に仮定しないためのケースです。 | Evaluation |

<a id="benchmarks-frontier-evaluation"></a>
## 📏 ベンチマークとフロンティア評価
---
---
<a id="case-250"></a>
### Case 250: [ToolEval FP16 Indexer 向上](https://x.com/volatilemarkts/status/2078663037825831172) (by [@volatilemarkts](https://x.com/volatilemarkts))

**このケースは、生の API baseline ではなく、fine-tune 済みローカル GLM-5.2 の tool use を benchmark したいときに使えます。volatilemarkts によると、753GB FP8 fine-tune と custom FP16 indexer により、SeraphimSerapis/tool-eval-bench が標準の GLM 5.2 API の 83 percent から 94 percent に上がったためです。**

著者によると、この構成では fine-tune 済みの GLM 5.2 model、753GB の FP8 weights、そして開発中の custom FP16 indexer を使っています。同じ投稿では、標準 API baseline と比べておよそ 10 ポイント改善し、さらに tuned model が Fable run で見逃された複数の line も拾ったと述べています。generic な open-source endorsement ではなく、具体的な local benchmarking と fine-tuning の reference です。

Type: Evaluation | Date: 2026-07-19

---
<a id="case-248"></a>
### Case 248: [Aikido 26-CVE ハーネス基準線](https://x.com/AikidoSecurity/status/2078816460865253714) (by [@AikidoSecurity](https://x.com/AikidoSecurity))

**このケースは、chat demo ではなく実際の code-audit harness で GLM-5.2 を benchmark したいときに使えます。AikidoSecurity によると、26 件の既知 CVE を使った AI Code Analysis benchmark で、GLM-5.2 は pass@3 で 16 件を再発見し、max reasoning ではコスト約 1.3x でさらに 3 件増やしたためです。**

この投稿は、Aikido が 7 月 16 日に出した benchmark report を指しており、同社の production analysis harness 内で GitHub Advisory Database の既知 vulnerability 26 件に対して 13 モデルをテストしたと説明しています。report では GLM-5.2 が完全な pass@3 table の中位に位置し、open-weight models が追い上げていると明記され、さらに high から max reasoning へ上げるとコスト約 1.3x で検出件数が 3 件増えたと示されています。generic な security claim ではなく、具体的な cyber code-review baseline です。

Type: Evaluation | Date: 2026-07-19

---
<a id="case-235"></a>
### Case 235: [DiligenceBench 金融ハーネス上位](https://x.com/karinanguyen/status/2078245092855525578) (by [@karinanguyen](https://x.com/karinanguyen))

**このケースは、公開株式リサーチ agent に対する GLM-5.2 の実力を評価したいときに使えます。karinanguyen によると、DiligenceBench では GLM 5.2 が上位に入り、この金融ハーネスが強いモデルをより高性能かつ低コストにできることを示したためです。**

karinanguyen は、DiligenceBench を公開株式リサーチ向けの rubric-based evaluation として紹介し、Meta Muse Spark 1.1 が 57.4 percent で首位、GLM 5.2 は Sonnet 4.6 と GPT-5.6 Sol の近くに続いたと述べています。さらに、汎用ツールは強いモデルほど恩恵が大きく、弱いモデルほど domain-specific な scaffold が必要だと論じており、この金融ハーネスによって price-performance frontier が十分に動くため、GLM 5.2 は絶対性能で目立ち、効率面では MiniMax M3 が最も強く見えるとしています。

Type: Evaluation | Date: 2026-07-17

---
<a id="case-227"></a>
### Case 227: [Gargantua WebGL Raytracer 勝利](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**このケースは、物理寄りの単一ファイル browser build で GLM-5.2 を benchmark したいときに使えます。AlicanKiraz0 によると、GLM 5.2 Max は Gargantua geodesic raytracer 課題で、数値的正しさと real-time rendering discipline の両立によって比較対象を上回ったためです。**

AlicanKiraz0 は、RK4 null-geodesic integration、accretion disk、gravitational lensing、redshift、Doppler effects、camera controls、そして練られた control panel を含む Schwarzschild black-hole renderer を、one-file raw WebGL2 で実装させる課題を説明しています。投稿では、勝敗を分けたのは visuals だけでなく numerical correctness、boundary handling、solver discipline であり、GLM 5.2 Max は 92/100 で GPT5.6 Sol Ultra の 90、Kimi K3 Thinking Max の 85、Fable 5 Max の 80 を上回ったとされています。

Type: Evaluation | Date: 2026-07-16

<a id="case-223"></a>
### Case 223: [Intelligence Index Token Efficiency Gap](https://x.com/ArtificialAnlys/status/2077466596528832678) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**このケースは、長期的な benchmark workload 向けに GLM-5.2 の予算を見積もるときに使えます。Artificial Analysis によると、GLM-5.2 Max は Intelligence Index の 1 タスクあたり平均約 43K の output tokens を使い、Inkling は 25K、Kimi K2.6 と DeepSeek v4 Pro Max もそれより少なかったためです。**

Artificial Analysis は leaderboard score だけでなく output-token usage を切り出して比較しており、同じ benchmark family の中で GLM-5.2 を open-weight 勢としてはコスト高めの側に置いています。投稿では、平均 output tokens が Inkling は 25K、GLM-5.2 Max は 43K、Kimi K2.6 は 38K、DeepSeek v4 Pro Max は 37K とされており、GLM の quality を評価しつつも agent loop の token burn を予測したいチームにとって実務的な efficiency note になります。

Type: Evaluation | Date: 2026-07-15

---
<a id="case-217"></a>
### Case 217: [EvalPlus レスキュールートが Fable 超え](https://x.com/gmi_cloud/status/2077124979397947824) (by [@gmi_cloud](https://x.com/gmi_cloud))

**このケースは、verifier 付きの二段モデル coding ルートを試したいときに使えます。gmi_cloud によると、最初に Opus 4.8 を走らせ、失敗時だけ GLM 5.2 FP8 を救援投入する構成で、凍結した EvalPlus 100 問のうち 94 問を解き、Fable 5 を 5 問上回りつつコストは約 47 パーセント低かったためです。**

gmi_cloud によれば、このスタックは HumanEval+ を 50 問、MBPP+ を 50 問実行し、Opus が verifier を通らなかったときだけ GLM 5.2 FP8 を呼び出しました。それでも pass rate は単体モデルをすべて上回りました。トレードオフも明確で、Fable 5 より 85.4 パーセント多く tokens を使った一方、コストは 0.4251 ドル対 0.8033 ドルで、Opus の 10 件の失敗のうち 4 件を GLM が救っています。

Type: 評価 | Date: 2026-07-14

---
<a id="case-207"></a>
### Case 207: [安定した流体のブラウザ ベンチマーク](https://x.com/AlicanKiraz0/status/2075639232169705781) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**このケースは、algorithm-heavy な browser physics build で GLM-5.2 を比較したいときに使えます。AlicanKiraz0 が Stable Fluids の HTML benchmark を実行し、GLM 5.2 Max に 100 点中 88 点、コスト約 1.17 ドルを付け、Opus 4.8 と Fable 5 を上回りつつ GPT 5.6 Sol は下回ったためです。**

この benchmark では、各 model に対して Jos Stam の stable fluids を、semi-Lagrangian advection、iterative diffusion、pressure projection、live divergence reporting、interactive な paint と velocity injection 付きで、単一の self-contained HTML file として実装させます。AlicanKiraz0 は、GLM 5.2 Max が 100 点中 88 点で、Opus 4.8 の 86 点と Fable 5 の 81 点を上回りながら大幅に安価だったと述べており、これは単なる好みの frontend 比較ではなく、数値的正しさと real-time browser performance を見る engineering-style evaluation になっています。

Type: Evaluation | Date: 2026-07-10

<a id="case-199"></a>
### Case 199: [エポックオープンウェイト指数リード](https://x.com/EpochAIResearch/status/2074894535558300103) (by [@EpochAIResearch](https://x.com/EpochAIResearch))

**このケースは、GLM-5.2 を長期的な capability curve の中で位置づけたいときに使えます。Epoch AI が Capabilities Index で推定 152 を与え、評価済み open-weight model の中で最高だとしているためです。**

Epoch AI は、GLM-5.2 が Epoch Capabilities Index で推定 152 を記録し、自分たちが評価した open-weight model の中で最も高いスコアだと述べています。そのためこの投稿は、狭い coding leaderboard ではなく、単一の capability-positioning signal が欲しいときの benchmark reference として使えます。

Type: Benchmark | Date: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Databricks 内部ハーネスの評価](https://x.com/alighodsi/status/2074996561306955958) (by [@alighodsi](https://x.com/alighodsi))

**このケースは、GLM-5.2 を大規模な private engineering codebase 上で benchmark したいときに使えます。Databricks によると、3,000 人超の engineer の仕事を含む内部評価で GLM 5.2 は非常に強く、harness の選び方だけでコストを約 2x 下げられるためです。**

Ali Ghodsi は、Databricks が自社の task、codebase、infrastructure に対して包括的な評価を行い、その対象は 3,000 人超の software engineer、3 つの hyperscaler cloud、多数の language にまたがったと述べています。投稿では GLM 5.2 が非常に良い結果を出し、同じ model でも正しい harness を選ぶだけでコストを約 2x 下げられるとされ、Omnigent が task ごとに model と harness を multiplex したと説明しています。

Type: Evaluation | Date: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [ネイチャーベンチ無差別級準優勝](https://x.com/OkhayIea/status/2074498200262889837) (by [@OkhayIea](https://x.com/OkhayIea))

**このケースは、GLM-5.2 を scientific-agent workflow で benchmark したいときに使えます。NatureBench が、6 つの scientific domain、90 task において GLM-5.2 が総合 2 位かつ open-weight 首位で debut したと述べているためです。**

NatureBench は、web search なしで coding agent が Nature 系論文の公開 SOTA を上回る手法を発見できるかを、6 つの scientific domain にまたがる 90 task で問う benchmark です。今回の更新では、GLM-5.2 が Claude Opus 4.7 に次ぐ総合 2 位で debut し、open-weight 勢の首位に立ったとされています。つまりこれは、普通の code generation ではなく scientific-agent workflow 向けの具体的な benchmark です。

Type: Benchmark | Date: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [ターミナルとベンチの 45 タスクのコストのトレードオフ](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (by [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**このケースは、同じ agent harness で GLM-5.2 と GPT-5.5 を比較したいときに使えます。45 件の Terminal-Bench で GLM-5.2 が 25 勝、GPT-5.5 が 29 勝となり、GLM は prompt caching 込みで約 40% 安かったためです。**

benchmark の投稿では、チームが GPT-5.5 と GLM-5.2 を 45 件の Terminal-Bench task に対して、同じ agent、同じ prompt、同じ evaluation、同じ harness で走らせ、変更したのは model だけだったと述べています。GLM は 45 件中 25 件を解き、GPT-5.5 は 29 件でしたが、prompt caching を含めたコストは GLM の方が約 40% 低かったとのことです。つまりこれは、曖昧な workflow の好みではなく、価格と成功率の具体的な比較材料です。

Type: Evaluation | Date: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Harvey LAB-AA 法務エージェント ネクタイ](https://x.com/ArtificialAnlys/status/2074541975186165887) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**このケースは、GLM-5.2 を実際の法務エージェント業務で benchmark したいときに使えます。Harvey LAB-AA で GLM-5.2 Max が 24 の practice area、120 の private task で Claude Opus 4.8 と同率の 7.5% all-pass を出しているためです。**

Artificial Analysis によると、Harvey LAB-AA は 24 の practice area にまたがる 120 件の private legal task を評価し、出力を binary rubric で採点します。launch 結果では GLM-5.2 Max が 7.5% all-pass、91.0% criteria-pass を記録し、Claude Opus 4.8 と同率でした。一方で task あたりのコストは Claude Fable 5 の約 6% とされており、frontier-domain benchmark と cost-efficiency signal の両方として使えます。

Type: Benchmark | Date: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [AutomationBench-AA オープンウェイト リード](https://x.com/ArtificialAnlys/status/2074194764510208230) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**このケースは、GLM-5.2 を coding benchmark だけでなく business rule を守る SaaS automation で比較したいときに使えます。Artificial Analysis が AutomationBench-AA で GLM-5.2 Max を 27.8% と報告し、open weights では首位だと述べているためです。**

Artificial Analysis によると、AutomationBench-AA は 40 個の simulated SaaS app をまたぐ 657 件の private workflow task を、約 12,000 の objective / guardrail assertion で採点します。launch post では GLM-5.2 Max が 27.8% で open weights の首位とされる一方、より強い closed model にはまだ差があり、guardrail violation も task あたりでかなり多いと書かれています。つまりこのケースは、agentic business automation における強みと限界の両方を示します。

Type: Evaluation | Date: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [Three-Body Simulator ベンチマーク勝利](https://x.com/AlicanKiraz0/status/2073823792543998170) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**このケースは、数値物理を含むコーディングベンチマークで GLM-5.2 を比較したいときに使えます。AlicanKiraz0 がカオス的な三体シミュレータ課題を走らせ、GLM 5.2 Max に 100 点中 91 点の最高評価を付けたためです。**

この benchmark では三体物理、実際の RK4、近接時の安定性、保存量のライブグラフ、対話的な操作が同時に求められます。thread では、GLM 5.2 Max が Float64Array state、再利用する RK4 buffer、Plummer softening、adaptive substep で優れていたと説明されており、単なる順位画像ではなく具体的な engineering quality の評価になっています。

Type: Evaluation | Date: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [GameDevBench 333-タスク オープンソース リード](https://x.com/iamwaynechi/status/2073081777091182633) (by [@iamwaynechi](https://x.com/iamwaynechi))

**このケースは、エージェント型のゲーム開発ベンチマークで GLM-5.2 を追うのに役立ちます。GameDevBench は 333 タスクまで拡張され、GLM-5.2 が視覚機能なしでも leaderboard 上で最強の open-source model だと述べています。**

iamwaynechi によると、GameDevBench は 333 タスクまで 3 倍に拡張され、paper も更新され、GLM-5.2 と Opus 4.8 が leaderboard に追加されました。投稿では総合首位は僅差で Opus ですが、GLM-5.2 は最強の open-source model とされており、テキスト coding だけでなくゲーム構築系 workflow の benchmark signal として有用です。

Type: Evaluation | Date: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [カーソル ダブル ペンデュラム スコアカード](https://x.com/AlicanKiraz0/status/2073386918813778143) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**このケースは、制約付きの Cursor coding benchmark で GLM-5.2 を比較したいときに使えます。AlicanKiraz0 は HTML の double-pendulum simulator で 6 モデルを比較し、GLM 5.2 Max に 100 点中 88 点を付け、Fable と Sonnet には届かなかったものの、GPT-5.5、Kimi K2.7 Code、Composer を上回りました。**

AlicanKiraz0 は、Cursor 内で 1 つの HTML double-pendulum simulator task に対して 6 モデルを比較し、総合スコアと各モデル固有の弱点を公開しました。GLM 5.2 Max は、見た目と教育的な説明は強い一方、performance architecture では Fable や Sonnet ほど洗練されておらず、RK4 wrapper の allocation リスクや trail buffer の resize 時の堅牢性の弱さが指摘されています。曖昧な好みではなく、具体的な comparative evaluation として使える thread です。

Type: Evaluation | Date: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10 タスク 80% タイ](https://x.com/morganlinton/status/2072689409011679642) (by [@morganlinton](https://x.com/morganlinton))

**このケースは、cost と score の両方が重要な post-cutoff の実エンジニアリング課題で GLM-5.2 を比較するのに役立ちます。Morgan Linton によると、VulcanBench では GLM 5.2 High、Fable 5 Low、Sonnet 5 High が 10 repo で同じ 80 percent になり、GLM の cost は中間でした。**

Morgan Linton によると、この benchmark は Flask、aiohttp、sqlglot などの project から取った 10 件の実エンジニアリング task を使っており、すべて post-training-cutoff と説明されています。Fable 5 Low、GLM 5.2 High、Sonnet 5 High はいずれも 80 percent で、reported cost は 2.27、8.41、15.81 dollars でした。単一モデルの自慢ではなく、3 者の価格対品質チェックポイントとして有用です。

Type: Evaluation | Date: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-再ベンチ 51.1 パーセント チェックポイント](https://x.com/ibragim_bad/status/2072318238407483593) (by [@ibragim_bad](https://x.com/ibragim_bad))

**このケースは、更新が続く SWE エージェント系リーダーボードで GLM-5.2 を追うのに向いています。最新の SWE rebench 投稿では 2.62 million tokens で 51.1 percent とされ、新しく加わった DeepSeek、MiMo、Qwen、Gemma より明確に上です。**

ibragim_bad によると、最新の SWE rebench 更新では GLM-5.2 が複数の新しい open model と並んで追加されました。公開された数値では、GLM は 2.62 million tokens で 51.1 percent、DeepSeek V4 Pro は 42.7 percent、MiMo V2.5 Pro は 42.4 percent、Qwen と Gemma はそれ以下で、公開リーダーボードの具体的な比較点になっています。

Type: Evaluation | Date: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly エッジケースで 40/41 で勝利](https://x.com/composio/status/2072355937415827950) (by [@composio](https://x.com/composio))

**このケースは、チャット専用評価ではなく業務ツールを使うエージェント作業で GLM-5.2 を試すのに向いています。Composio によれば、GitHub、Jira、LaunchDarkly の 41 タスク中 40 を取り、保留承認のエッジケースを拾えたのは GLM だけでした。**

Composio は、GitHub、Jira、LaunchDarkly など実ツールを使う 41 のエージェントタスクで GLM-5.2 を Claude Opus 4.8 と GPT-5.5 にぶつけました。GLM は 40/41、Opus と GPT はどちらも 39/41 です。LaunchDarkly の 1 タスクでは、GLM だけがフラグを stale と判定する前に pending approval を確認し、他の 2 モデルは on/off 状態で止まりました。

Type: Evaluation | Date: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench 無差別級パッチ準優勝](https://x.com/ValsAI/status/2072099011398627639) (by [@ValsAI](https://x.com/ValsAI))

**GLM-5.2 を攻撃寄りの脆弱性発見とパッチ作成で測りたいならこの事例が役立ちます。CyberBench で 60 件の実在 OSS-Fuzz 脆弱性に対して総合 2 位になっているからです。**

ValsAI は、CyberBench が「脆弱ビルドだけを落とす PoC 提出」と「挙動を壊さないパッチ作成」を組み合わせた評価だと説明しています。60 件の OSS-Fuzz メモリ安全性脆弱性では GPT-5.5 が首位で、GLM 5.2 は最も強い open-weight 群の一つとして示されています。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [人工分析インテリジェンスインデックス](https://x.com/ArtificialAnlys/status/2067135640249209175) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Artificial Analysis ポストを使用して、インテリジェンスとタスクあたりのコストに関して GLM-5.2 を他のオープンウェイトおよび独自のフロンティア モデルと比較します。**

Artificial Analysis は、GLM-5.2 をインテリジェンス インデックスの主要なオープンウェイト モデルとして報告し、スコアは 51 で、インテリジェンスとタスクあたりのコストに関してパレート フロンティアの位置にあります。この投稿には、モデルのサイズ、コンテキスト ウィンドウ、価格、プロバイダーの可用性も記録されます。

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [コードアリーナフロントエンドランキング](https://x.com/arena/status/2066957802741043641) (by [@arena](https://x.com/arena))

**このケースを使用して、アリーナ スタイルの比較によって判断される実際のフロントエンド コーディング タスクで GLM-5.2 を評価します。**

Arena アカウントは、GLM-5.2 Max が Code Arena フロントエンドで 2 位にランクされ、他のオープン モデルを上回り、フロンティア エントリーのトップに迫っていると報告しました。この投稿は、フロントエンド、React、HTML、ゲーム、シミュレーション、リファレンスベースのデザインのユースケースに特に役立ちます。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [デザインアリーナ1位](https://x.com/Designarena/status/2066940737011560652) (by [@Designarena](https://x.com/Designarena))

**このケースを使用して、GLM-5.2 がテキスト中心のコーディング ベンチマークだけではなく、デザインとコードのタスクを処理できるかどうかを判断します。**

Design Arena は、GLM-5.2 が Elo スコア 1360 で 1 位になったと報告し、オープンウェイト モデルの設計コード パフォーマンスの飛躍を強調しました。プロジェクト固有の UI レビューの代わりとしてではなく、設計ベンチマーク信号として扱います。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWEの結果](https://x.com/ProximalHQ/status/2066939701026787583) (by [@ProximalHQ](https://x.com/ProximalHQ))

**FrontierSWE の投稿を使用して、ソフトウェア エンジニアリング タスクに関して GLM-5.2 を GPT-5.5、Opus、および Fable スタイルのモデルと比較します。**

この投稿では、GLM-5.2 が FrontierSWE で 3 位にランクされていると報告しており、これを、実装の負荷が高いエンジニアリング作業においてトップの独自モデルとの差を縮める最初のオープンウェイト モデルの 1 つであると位置づけています。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE オープンソース リーダー](https://x.com/AiBattle_/status/2066938378512126024) (by [@AiBattle_](https://x.com/AiBattle_))

**DeepSWE のケースを使用して、難しいソフトウェア エンジニアリングの評価タスク用の強力なオープン モデルとしての GLM-5.2 を理解します。**

AiBattle は、GLM-5.2 の 46.2% DeepSWE スコアを報告し、それがそのベンチマークのコンテキストにおけるオープンソース モデルの最高スコアであると説明しました。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [ターミナルベンチが 80% 以上](https://x.com/cline/status/2066951439793242193) (by [@cline](https://x.com/cline))

**端末指向のコーディングおよびエージェント ワークフローについて GLM-5.2 を評価する場合は、このケースを使用してください。**

クライン氏は、ターミナルベンチで 80% を超えた最初のオープンウェイト モデルとして GLM-5.2 を強調し、これをアクセス可能なツールベースの開発のフロンティア レベルのオプションとして位置づけました。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer と GPT-5.5 の比較](https://x.com/gosrum/status/2067153091842203676) (by [@gosrum](https://x.com/gosrum))

**この SWELancer のケースを、タスクの成功、報酬、完了時間に関する GLM-5.2 と GPT-5.5 の具体的なマルチメトリクスの比較として使用します。**

著者は、アクセスできない 2 つのタスクを除いて、タスクの成功、獲得報酬、完了までの時間に関する SWELancer の最新結果において、GLM-5.2 が予想外に GPT-5.5 を上回ったという日本のベンチマーク更新情報を共有しました。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench パーフェクト スコア シグナル](https://x.com/bridgemindai/status/2065874542321426819) (by [@bridgemindai](https://x.com/bridgemindai))

**このケースを使用して、リーダーボードをコーディングするだけではなく、根拠に基づいた複数ステップの推論に基づいて GLM-5.2 を検査します。**

BridgeMind は、GLM-5.2 が BridgeBench BS ベンチマークで満点を獲得した最初のモデルであると報告しており、推論重視の評価主張の有用な情報源となっています。

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench 推論その 1](https://x.com/bridgebench/status/2066123398816624743) (by [@bridgebench](https://x.com/bridgebench))

**このケースを使用して、根拠のある推論タスクに関して GLM-5.2 をクローズド フロンティア モデルと比較します。**

BridgeBench は、GLM-5.2 が推論ベンチマークでナンバー 1 の座を獲得し、その測定コンテキストで Claude Fable 5 を上回っていると報告しました。

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench - ショートカットなしのハード](https://x.com/elliotarledge/status/2065735912370417760) (by [@elliotarledge](https://x.com/elliotarledge))

**ベンチマークのゲインがショートカットではなく有効な実装動作によるものであるかどうかを確認する場合は、このケースを使用してください。**

KernelBench-Hard の投稿では、興味深い結果はスコアだけでなく、GLM-5.2 が fp8 GEMM 問題で不適切なショートカットの使用を停止し、ベンチマークの整合性に関連するものになったと述べています。

Type: Evaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [ルーンスケープベンチの追い上げ](https://x.com/maxbittker/status/2066985743197577433) (by [@maxbittker](https://x.com/maxbittker))

**このケースは、ゲームのようなベンチマーク タスクにおける無重みモデルの進行状況を示す速い信号として使用します。**

この投稿では、Runescape ベンチで GLM-5.2 のスコアが最近の独自モデルよりも優れていると報告しており、その結果を利用して、オープンソースのフロンティア機能がいかに早く追いつくかを示しています。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench の速度向上](https://x.com/bridgebench/status/2065845045752648159) (by [@bridgebench](https://x.com/bridgebench))

**このケースを使用して、インテリジェンスとともに速度が重要となる、レイテンシーに敏感なワークフローを評価します。**

BridgeBench は、GLM-5.2 が GLM-5.1 の 3 倍高速であり、速度ベンチマークで 4 番目であると報告しており、反復速度が使いやすさに影響を与えるワークフローに適していると報告しています。

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench ハードおよびメガ GPU コーディング](https://x.com/elliotarledge/status/2068177175640240323) (by [@elliotarledge](https://x.com/elliotarledge))

**このケースを使用して、KernelBench-Hard と KernelBench-Mega にわたる GPU カーネル コーディングで GLM-5.2 を評価します。オープン エージェント トレースにより結果が検査可能になります。**

KernelBench アップデートでは、H100、B200、RTX PRO 6000 のテスト、オープンソースのエージェント トレース、および比較の最上位のオープン モデルとして GLM-5.2 が報告されています。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE Max-Effort オープンソース首位](https://x.com/datacurve/status/2068473057107476680) (by [@datacurve](https://x.com/datacurve))

**最大 effort 設定の DeepSWE で GLM-5.2 を追跡するためのケースです。公開リーダーボードでは open model 中 1 位、pass@1 は 44% と示されています。**

DataCurve は DeepSWE の leaderboard update を共有し、GLM-5.2 が pass@1 44% で、open model の中では Kimi K2.7 Code を 17 ポイント上回ったと示しました。これは benchmark update として扱うべきであり、あらゆる実運用 agent workflow がすでに解決された証拠とみなすべきではありません。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM Debate Benchmark 準優勝](https://x.com/LechMazur/status/2068428300460974279) (by [@LechMazur](https://x.com/LechMazur))

**コーディング以外でも GLM-5.2 を評価するためのケースです。敵対的な multi-turn debate で、max-reasoning variant が Claude 系に次ぐ 2 位となっています。**

Lech Mazur は、GLM-5.2 Max が 2 位になった LLM Debate Benchmark の結果を共有しました。この benchmark は幅広いトピックにわたる敵対的な multi-turn debate を測定しており、標準的な coding leaderboard の外側にある reasoning signal として有用です。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience hallucination rate](https://x.com/yuhasbeentaken/status/2068259921519423855) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**不確実性の扱いを比較するためのケースです。公開された AA-Omniscience 結果では、GLM-5.2 の hallucination rate は複数の frontier model より低くなっています。**

この投稿では、AA-Omniscience における GLM-5.2 の hallucination rate は 28% で、Fable 5 や DeepSeek V4 Pro より高い rate を示したモデル群より低いと報告されています。この benchmark は、推測する代わりに model が拒否または不確実性を認めるかどうかに焦点を当てています。

Type: Evaluation | Date: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA エージェント作業指数](https://x.com/ArtificialAnlys/status/2069121548670406947) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**コーディング専用のリーダーボードではなく、長期的な知識労働で GLM-5.2 を比較するためのケースです。**

Artificial Analysis によると、GDPval-AA での GLM-5.2 は Elo 1524 で、Claude Fable 5 と Opus 4.8 に次ぐ総合 3 位、GPT-5.5 xhigh の 1509 をわずかに上回りました。オープンウェイトモデルでは大差の首位であり、投稿では 1,999 試合にわたって 1 タスク平均約 31 ターンだったと述べられています。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [ゲーム デベロッパー アリーナ 準優勝](https://x.com/Designarena/status/2069166634976371084) (by [@Designarena](https://x.com/Designarena))

**ゲーム構築品質で GLM-5.2 を判断するためのケースです。Game Dev Arena で 2 位に入り、その順位ではオープンウェイト陣営の最上位になりました。**

Design Arena は、Game Dev Arena における GLM-5.2 のスコアを Elo 1368 と報告しており、GLM-5.1 から 29 ポイント上昇し、順位も 6 つ上がったとしています。投稿では Claude Fable 5 と同等の性能帯にあるとされ、総合 2 位、ラボ別では OpenAI を上回り Anthropic のみが上位だったと述べています。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [PostTrainBench 信頼性首位](https://x.com/hrdkbhatnagar/status/2070244540108423427) (by [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**見出しスコアだけでなく、84 タスクで failed run が 0 件だったという agent reliability も含めて GLM-5.2 Max を比較するためのケースです。**

hrdkbhatnagar は、GLM 5.2 Max reasoning が 34.29% で Opus 4.8 Max の 34.08% をわずかに上回った PostTrainBench leaderboard を共有しています。同じ投稿では、GLM が 84 runs で failed run 0 件だった一方、Opus agents ではおよそ 10% の failure rate があったとも述べられており、raw pass rate だけでなく agent の信頼性を重視するチームに有用です。

Type: Benchmark | Date: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211件リポジトリ課題評価](https://x.com/FireworksAI_HQ/status/2070181898962534570) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**公開 benchmark だけでなく private repo の実務 engineering task で GLM-5.2 を判断するためのケースです。公開値には score、speed、task あたりの cost が含まれています。**

Fireworks は、Faros と共同で行った 211 件の実 engineering task 評価で、Claude Code + GLM-5.2 が Claude Code + Opus 4.8 と Codex + GPT-5.5 の両方を上回ったと述べています。投稿では、judge score 0.568 対 0.521 / 0.466、task あたり 321 秒 対 775 / 392、task あたり 0.92 ドル 対 1.76 / 2.06 という数値が示され、さらに Faros が公開 benchmark だけでなく自社の repositories と業務を使ったことも明記されています。

Type: Evaluation | Date: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase タスク時間フロンティア](https://x.com/ArtificialAnlys/status/2069914443639635978) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**ベンチマークスコアだけでなく、1 タスクあたり時間も重要な長期知識労働で GLM-5.2 を比較するためのケースです。**

Artificial Analysis は、GLM-5.2 が AA-Briefcase のパレートフロンティア上にあり、スコア 1261、1 タスク平均 16.3 分を記録し、GPT-5.5 xhigh の 1159 を上回りつつ、同ベンチマークで最高性能の open-weights model だと述べています。単なるリーダーボード順位ではなく、長期タスクの成果物品質と実行時間を比較したいチームに有用な benchmark です。

Type: Benchmark | Date: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena Frontend 直接対決マージン](https://x.com/arena/status/2069885722333769963) (by [@arena](https://x.com/arena))

**単一の順位スクリーンショットではなく、ペアごとの直接対決結果から GLM-5.2 のフロントエンド優位を確認するためのケースです。**

arena は、GLM-5.2 Max が Code Arena: Frontend の首位に到達した理由を分解し、1 つを除くすべての対戦相手との組み合わせで相手より高い win share を出したと説明しています。スレッドでは Kimi-K2.6 に対する 61.0%、Sonnet 4.6 に対する 59.4%、Opus 4.7 Thinking に対する 55.0%、GPT-5.5 xHigh との 41.7% 対 40.0% の接戦、そして GLM-5.1 との 45.5% 引き分けが示されています。

Type: Benchmark | Date: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas Codebase QnA 準優勝](https://x.com/ScaleAILabs/status/2069864932913631617) (by [@ScaleAILabs](https://x.com/ScaleAILabs))

**単一タスクの SWE リーダーボードだけでなく、Codebase QnA、テスト作成、リファクタリング全体で GLM-5.2 を追うためのケースです。**

Scale AI Labs は、GLM 5.2 が SWE Atlas の 3 つのリーダーボード、Codebase QnA、Test Writing、Refactoring のすべてで公開されたと述べています。特に Codebase QnA で 2 位に入った点を強調し、open model が全体として frontier system に迫ってきていると説明しています。

Type: Benchmark | Date: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 コーディングエージェントと長文脈ワークフロー
---
<a id="case-257"></a>
### Case 257: [OpenCodex モデル切り替えワークフロー](https://x.com/vista8/status/2079239701391675404) (by [@vista8](https://x.com/vista8))

**このケースは、1 つの model に固定せず Codex 中心の coding loop の中で GLM-5.2 を切り替えて使いたいときに役立ちます。vista8 によると、OpenCodex では同じ環境のまま frontend design、backend work、ライブ X search に応じて GLM 5.2、Kimi K3、GPT-5.6 Sol、Grok 4.5 を切り替えられるためです。**

vista8 は、実運用で最も多く使っている coding tool は依然として Codex だが、frontend のセンスには弱みがあったため、必要に応じて model を差し替えられる OpenCodex project に workflow を移したと述べています。routing note も具体的で、frontend design では OAuth 経由の Kimi K3、backend work では GPT-5.6 Sol、X search では Grok 4.5 を使い、GLM 5.2 も同じ coding surface 内の drop-in option として扱う構成です。単なる model ranking ではなく、coding agent 向けの実践的な model-router workflow として読めます。

Type: Integration | Date: 2026-07-20

---
<a id="case-255"></a>
### Case 255: [Hermes 11-Agent ハイブリッドラボ](https://x.com/MichaelGannotti/status/2079168568478912834) (by [@MichaelGannotti](https://x.com/MichaelGannotti))

**このケースは、1 つの monolithic assistant ではなく、GLM-5.2 を含む役割ベースの multi-agent lab を組みたいときに役立ちます。MichaelGannotti によると、11-agent の Hermes 構成が DGX Spark、Ryzen workstation、cloud models 間で task を動的に振り分け、software、research、marketing、coordination を回しているためです。**

MichaelGannotti は、具体的な lab architecture を示しています。128GB unified memory を備えた DGX Spark をメインのローカル推論サーバーにし、Ryzen 9 Halo Strix マシンで engineering と organizational roles 向けに 8 つの Hermes agents を動かし、Ryzen 7 の Windows マシンで content と Microsoft stack 向けにさらに 3 agents を回す構成です。その上で各 agent は task に応じて GPT-5.6、GLM 5.2、Grok 4.5 の cloud models と、ローカルの Qwen、Nemotron、Gemma を使い分けるため、この投稿は曖昧な productivity claim ではなく、hybrid local-cloud agent team の具体的な運用モデルとして参考になります。

Type: Integration | Date: 2026-07-20

---
<a id="case-243"></a>
### Case 243: [Hermes ハイブリッド API 同等運用](https://x.com/dangerm00se/status/2078369336239313368) (by [@dangerm00se](https://x.com/dangerm00se))

**このケースは、自己ホストの GLM-5.2 coding agent を公式ルートと比較検証したいときに使えます。dangerm00se によると、4x RTX 6000 PCIe 上の Hermes と GLM-5.2 の hybrid は official API の 60 タスク中 59 件で一致し、3,149 tok/s の prefill、0.37 秒の warm TTFT、35.9 tok/s の decode を出したためです。**

dangerm00se はこの結果を、単なる throughput screenshot ではなく autonomy の節目として位置付けています。post によると、Hermes と GLM-5.2 の hybrid は DDR4 host 上の 4x RTX 6000 PCIe で動き、3,149 tok/s の prefill、0.37 second の warm TTFT、35.9 tok/s の decode を記録し、official GLM API と 60 タスク中 59 件で一致しました。さらに setup instruction と official route との accuracy report も案内しており、曖昧な self-hosting 自慢ではなく具体的な local-agent reference になっています。

Type: Evaluation | Date: 2026-07-18

<a id="case-237"></a>
### Case 237: [LM Studio Bionic GLM エージェント](https://x.com/chenzeling4/status/2077967277698515184) (by [@chenzeling4](https://x.com/chenzeling4))

**このケースは、ローカル優先の GLM-5.2 coding agent を評価したいときに使えます。chenzeling4 によると、LM Studio Bionic は GLM 5.2 にローカル document sandbox、inline code diff、rollback checkpoint、端末内 voice transcription を組み合わせているためです。**

chenzeling4 は、LM Studio Bionic を open model 中心の standalone agent と説明しており、task に応じて local または cloud compute を使い分けつつ、どちらでも zero-retention を打ち出していると述べています。投稿では、coding は GLM 5.2 と Kimi K2.7 Code が担当し、document は sandbox 内で動き、automatic rollback checkpoint が付き、code edit は inline diff として表示され、voice transcription は Voxtral により端末内で完結するとされています。単なる model availability note ではなく、具体的な local-agent workflow の更新として扱える内容です。

Type: Integration | Date: 2026-07-17

---
<a id="case-236"></a>
### Case 236: [Claude Code の Web 開発品質優位](https://x.com/Lumenix0/status/2078241726897230164) (by [@Lumenix0](https://x.com/Lumenix0))

**このケースは、単純な完了速度ではなく初回生成時の Web 開発品質を比較したいときに使えます。Lumenix0 によると、Claude Code 上の GLM 5.2 は 3 つの実タスクで、Codex 上の GPT 5.5 を design quality と機能完成度で上回ったためです。**

Lumenix0 は、Claude Code 経由の GLM 5.2 と Codex 経由の GPT 5.5 を、website redesign、React の bug hunt、Kanban board build の 3 件で直接比較したと要約しています。各 task の完了速度は GPT の方が速かった一方で、GLM はより良い redesign を出し、bug fix ではより明快な説明を付け、Kanban board では task naming、priority、status change、reset button まで揃った唯一の fully working 実装を one shot で出したとされています。同じ投稿では、この 3 テスト全体で 16 dollar plan の weekly quota の 7 percent しか使わなかったとも述べています。

Type: Evaluation | Date: 2026-07-17

<a id="case-168"></a>
### Case 168: [Synthwave ハードスライス アンサンブル、$2.66](https://x.com/TracNetwork/status/2073038214592360522) (by [@TracNetwork](https://x.com/TracNetwork))

**このケースは、GLM-5.2 を単独ではなく multi-model の coding ensemble に組み込んで試すのに向いています。TracNetwork によれば、GLM を含む Synthwave 構成は LiveCodeBench hard で 46.3 percent を約 2.66 ドルで出し、各 generator 単体を上回りました。**

TracNetwork は、OpenRouter 上で qwen3-coder-next を synthesizer に、GLM-5.2 と qwen3.5-122b、qwen3-coder-next を coding generator にした Synthwave ensemble を使ったと述べています。82 件の LiveCodeBench hard task で 46.3 percent、コストは約 2.66 ドルで、どの generator 単体もこのスコアに届かなかったとのことです。GLM-5.2 を唯一の coding model としてではなく、コスト重視 ensemble の一員として使う具体例です。

Type: Integration | Date: 2026-07-03

---

---

<a id="case-228"></a>
### Case 228: [OpenCode によるローカル agentic coding 基盤](https://x.com/comma_ai/status/2077819467267186700) (by [@comma_ai](https://x.com/comma_ai))

**このケースは、frontier サブスクに課金する前にローカル coding-agent stack を検証したいときに使えます。comma_ai によると、同社は Anthropic を内部スタックから外し、GLM 5.2 と OpenCode の組み合わせで agentic coding がより良く回るようになったためです。**

comma_ai は、GLM deployment が open-source driving agent を訓練するマシンのすぐそばで動いていると述べており、これは単なる cloud 好みではなく local ownership の強いシグナルです。thread では GLM 5.2 を OpenCode と明示的に結び付け、Anthropic を stack から外した後の daily agentic coding が改善したと主張しているため、一般的な open-source 礼賛ではなく、実務的な local-first workflow の参照例になります。

Type: Demo | Date: 2026-07-16

<a id="case-212"></a>
### Case 212: [Dell Hub GLM Agent チュートリアル](https://x.com/juanjucm/status/2076714987569963508) (by [@juanjucm](https://x.com/juanjucm))

**このケースは、open-weight の学習ワークフロー向けに GLM-5.2 coding agent を立ち上げるときに使えます。juanjucm によれば、新しいガイドが Dell Enterprise Hub の GLM-5.2-FP8 カタログ追加と、そのモデルを中心にした agent のセットアップ手順をセットで示しているためです。**

juanjucm は、2 つの小規模 language model を訓練するための GLM-5.2 ベース coding agent の組み方を公開ガイドにまとめ、そのチュートリアルを Dell Enterprise Hub の GLM-5.2-FP8 カタログ追加と結びつけて紹介したと述べています。リンク先の Hugging Face 記事が公開チュートリアル面を担い、投稿自体はこの stack を、単なる availability note ではなく、hands-on な training と agent 実験向けの open-weight ルートとして位置づけています。

Type: Tutorial | Date: 2026-07-13

---

<a id="case-211"></a>
### Case 211: [8xB200 Open-Weight レポートパイプライン](https://x.com/TheZachMueller/status/2076746035758502275) (by [@TheZachMueller](https://x.com/TheZachMueller))

**このケースは、GLM-5.2 をローカル寄りのレポート生成パイプラインで main writer に据えるときに役立ちます。TheZachMueller によれば、1 台の 8xB200 ノードを 4/4 に分割し、GLM 5.2 NVFP4 にレポート生成、Kimi K2.7 Code に retrieval を担当させることで、Claude API よりごく小さいコストで、より密度の高い 36 ページのレポートを出せたためです。**

TheZachMueller は、週末いっぱい tuning したあと、実作業のパイプラインを Claude Code から Pi dot dev と open-weight stack へ移したと述べています。公開された構成では、1 台の 8xB200 ノードを半分ずつに分け、GLM 5.2 NVFP4 を main agent 兼 driver、Kimi K2.7 Code を retriever として使い、Claude の 21 ページ版ではなく 36 ページのレポートを生成しました。投稿は tradeoff も明確に書いており、処理時間はおよそ 20 分から 30 から 40 分へ伸びた一方で、最大の品質改善は source article を何度も要約させるのをやめ、全文を disk 上に残して deeper retrieval に回した点だとしています。

Type: Demo | Date: 2026-07-13

---

<a id="case-210"></a>
### Case 210: [Spettro の Liquid Glass マルチエージェント刷新](https://x.com/spettrotoken/status/2076330234492698844) (by [@spettrotoken](https://x.com/spettrotoken))

**このケースは、multi-agent な web 改修の中で GLM-5.2 を調査負荷の高い frontend fixer として試したいときに役立ちます。spettrotoken によれば、Fable 5 と GPT-5.5 が失敗したあと、GLM 5.2 が統合済みの web scraping と data fetching ツールを使い、Firefox でも動く cross-browser な Liquid Glass 実装を出荷したためです。**

spettrotoken は、稼働中の Spettro サイト刷新を 4 つの Spettro instance に分け、それぞれに別の frontend セクターを持たせた一方で、GLM-5.2 には Firefox で壊れがちな屈折型 Liquid Glass という最難関の視覚コンポーネントを任せたと説明しています。投稿によると、GLM 5.2 は web を自律的に調べ、CSS と SVG filter の workaround を読み、効果を reverse-engineer したうえで、本番サイトにデプロイされた動作する cross-browser 実装を作りました。広い範囲の刷新では Kimi K2.7 と並列 sub-agent も補助に回ったとされています。

Type: Demo | Date: 2026-07-12

---

<a id="case-194"></a>
### Case 194: [CuTeDSL カーネル スキル オープンソース](https://x.com/SubhoGhosh02/status/2074466050557739469) (by [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**このケースは、GLM-5.2 を再利用可能な kernel-debugging skill の中で研究したいときに使えます。作者が CuTeDSL 向けの Hermes skill を open source 化し、kernel の debugging と writing で GLM-5.2 のコスト効率が特に良かったと述べているためです。**

投稿では、skill の大部分が複数 model をまたぐ Hermes の agentic conversation で作られ、その中で GLM-5.2 が kernel debugging と kernel writing において cost efficiency の面で目立ったと説明しています。さらに source には `hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` と `hermes chat -s cutedsl-kernels` という正確な install / launch command も含まれているため、これは曖昧な称賛ではなく再利用可能な tutorial-style workflow です。

Type: Tutorial | Date: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Hermes SSDリカバリスキルループ](https://x.com/ShankhadeepSho1/status/2073658918937473444) (by [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**このケースは、修復志向の agent loop の中で GLM-5.2 を試したいときに使えます。ShankhadeepSho1 によると、Hermes と GLM 5.2 が故障した NAS SSD を診断し、問題を直したうえで、その修復方法を再利用可能な skill としてまとめたためです。**

投稿者によれば、QNAP NAS の SSD が故障し、それを予備マシンへ移して Hermes に診断させたとのことです。公開された結果はかなり具体的で、stack が問題を修復し、自分用の skill を作成し、復旧戦略を infrastructure wiki に追記したとされています。

Type: Demo | Date: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [ロールルーティングされた高耐久コーダー スタック](https://x.com/denizirgin/status/2073462071639876004) (by [@denizirgin](https://x.com/denizirgin))

**このケースは、役割ごとにルーティングする個人スタックで GLM-5.2 を重い coding 作業の担当に置くときに役立ちます。denizirgin は、Codex と OpenCode を 1 か月試した結果、月額 120 から 140 dollars 前後に抑えながら、より重い coding work を GLM 5.2 に回す運用に落ち着いたと述べています。**

denizirgin は、現在の個人セットアップが Codex、OpenCode、DeepSeek、OpenRouter、そして coding、review、research、speed、cost を判断する自作の sub-agent skill と decision table で構成されていると説明しています。そのルーティングでは GLM 5.2 が complementary provider 経由の heavy-duty coder を担い、Codex が main backbone に残り、OpenRouter はモデル実験用により選択的に使われます。一般的なモデル順位ではなく、一次情報としての cost-aware workflow note です。

Type: Evaluation | Date: 2026-07-04

<a id="case-155"></a>
### Case 155: [Cotal 4 エージェント TUI ループ](https://x.com/silvanrec/status/2072335315822403656) (by [@silvanrec](https://x.com/silvanrec))

**このケースは、コーディングループを専門エージェントに分担させるのに使えます。著者は Opus のリードと GPT のレビュー役の下で GLM-5.2 ワーカーを 2 体使い、lazygit 風 TUI を 47 分で人手なしに仕上げました。**

silvanrec によると、Cotal は 4 モデルを協調させました。フロントエンド担当とバックエンド担当の GLM-5.2 が 2 体、バックグラウンドレビュー役の GPT-5.5、そしてループ全体を率いる Claude Opus です。実用的な TUI コンソールを作る 1 つのプロンプトから始まり、4 ラウンドの中でレンダリングやタブ配線のバグを見つけ、エージェント間の handoff を回し、47 分で動く結果を出しました。投稿では open source 層として npx cotal-ai setup --full も示しています。

Type: Demo | Date: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [レガシー移行のコスト削減パイロット](https://x.com/chamath/status/2072390507628540213) (by [@chamath](https://x.com/chamath))

**このケースは、レガシーアプリ刷新ループの中で GLM-5.2 を低コスト側の実行役として評価するのに使えます。8090 のパイロットでは、GLM と Software Factory の組み合わせが Opus 4.8 単体比で 16.4 倍安く、ただし約 3 倍遅いとされています。**

Chamath は PHP から Next.js への初期モダナイズ実験を共有しています。8090 の Software Factory を載せた Opus 4.8 は Opus 単体より 1.4 倍安く 1.5 倍速く、一方で同じファクトリーに GLM 5.2 を組み合わせると Opus 単体比で 16.4 倍安くなる代わりに約 3 倍遅くなったとされています。投稿では n=1 の方向性確認にすぎず、10 から 15 件の実案件で再検証すべきだと明言しています。

Type: Evaluation | Date: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio ブラウザ - ローカル ループの使用](https://x.com/MaziyarPanahi/status/2071955191260151862) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**完全ローカルな GLM-5.2 スタックが consumer hardware 上で軽い browser agent 作業をこなせるか試したいならこの事例が役立ちます。作者は Mac Studio 上の llama.cpp と browser-use で Hugging Face の PII モデルを探しました。**

MaziyarPanahi は、Mac Studio 上で llama.cpp により GLM-5.2 をローカル実行し、その上に browser-use の agent loop を載せたと述べています。公開例では Hugging Face を操作して `privacy-filter-nemotron` を見つけています。

Type: Demo | Date: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop エージェントスワップコスト削減](https://x.com/aronkor/status/2072032854675218538) (by [@aronkor](https://x.com/aronkor))

**既存の agent harness の中で単純なモデル差し替えを試したいならこの事例が役立ちます。Gumloop は GLM-5.2 へ移した後、品質低下をほぼ感じずに credit 消費を約 50% 下げたと言っているからです。**

aronkor は、同じ harness と同じ prompt のまま、Gumloop で最も使われる agent 群を GLM 5.2 に置き換えた内部実験を説明しています。報告では、出力品質の差はほとんど気づかれず、credit 消費だけがほぼ半分になりました。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [1 時間 42 分のリファクタリング ループ](https://x.com/KELMAND1/status/2066012493315723610) (by [@KELMAND1](https://x.com/KELMAND1))

**このケースは、TDD、レビュー担当者のフィードバック、回帰チェックによる長時間にわたる自律的なフロントエンド リファクタリングのパターンとして使用してください。**

この投稿では、88 回のモデル回転と 102 回のツール呼び出しを含む、1 時間 42 分の GLM-5.2 リファクタリング タスクについて説明しています。ワークフローには、ハンドオフ、4 つのブロッカーの修正、12 のテストの TDD 実装、2 ラウンドの P2 修正、および最終回帰が含まれていました。

Type: Demo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode のバグ修正と実装テスト](https://x.com/altudev/status/2065868921341632881) (by [@altudev](https://x.com/altudev))

**このケースを使用して、バグ修正と小規模な実装タスクのための OpenCode コーディング エージェントとして GLM-5.2 をテストします。**

著者は、6 つのバグ修正と OpenCode での 1 つの実装を含む GLM-5.2 のテストを報告し、変更は確実な計画と GLM-5.1 よりも速い速度できれいに完了したと述べています。

Type: Demo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode レトロ ビデオ ゲームのウォークスルー](https://x.com/AskVenice/status/2067047775783534789) (by [@AskVenice](https://x.com/AskVenice))

**このチュートリアルを使用して、単一のプロンプトから GLM-5.2 と OpenCode を使用して小規模なゲームを構築し、モデルが実装の詳細をどのように処理するかを検査します。**

Venice は、GLM-5.2 と OpenCode を使用してレトロ ビデオ ゲームを構築するための完全なチュートリアルを共有し、これをプライベートなオープンソースの長期的なコーディング ワークフローとして位置づけました。

Type: Tutorial | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 物理シミュレーション コンテスト](https://x.com/atomic_chat_hq/status/2067038851139334588) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**このケースを使用して、ライブラリを使用しない自己完結型 HTML5 物理シミュレーションで GLM-5.2 コードと Kim K2.7 コードを比較します。**

Atomic Chat は、両方のモデルにプールブレイク、スプリングブロック、ゴルトンボードのシミュレーションを構築するよう依頼したと報告しました。彼らの投稿によると、GLM-5.2 は 3 つすべてをより詳細かつ洗練して処理し、一方、キミは身体的動作に苦労していました。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [個人サイトのUI UXの構築](https://x.com/anshuc/status/2067034697704857615) (by [@anshuc](https://x.com/anshuc))

**このケースを使用して、GLM-5.2 に洗練された個人サイトを求め、複数のターンで UI/UX がどの程度改善されるかを検証します。**

著者によると、GLM-5.2 は適切なプロンプトでプッシュされた後、クリエイティブな個人サイトを作成し、その結果のビデオを共有しました。これは、単発のベンチマーク要求ではなく、フロントエンド設計の反復に役立ちます。

Type: Demo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI 契約レビュー製品ビルド](https://x.com/laozhang2579/status/2066339734956499301) (by [@laozhang2579](https://x.com/laozhang2579))

**このケースを使用して、PRD、時間予算、ステップ数、使用量割り当て、およびコード品質の比較を使用して製品構築タスクで GLM-5.2 を評価します。**

中国の投稿では、AI 契約レビュー製品 PRD で GLM-5.2、Kimi K2.7、および Claude Opus 4.8 を比較しています。ビルド時間、ステップ数、5 時間のクォータ使用量、コード品質スコアがレポートされます。

Type: Evaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [より大きな開発目標のための ZCode 目標機能](https://x.com/zcode_ai/status/2066236605917188228) (by [@zcode_ai](https://x.com/zcode_ai))

**このケースを使用して、大規模なエージェント開発タスクのために GLM-5.2 がどのように ZCode 3.0 に統合されるかを理解してください。**

ZCode は、コーディング プラン ユーザー向けの GLM-5.2 の提供、より強力なエージェント タスクの実行、より優れたロング コンテキスト コーディング、および計画から完了までのより大きな目標を管理するための目標機能を発表しました。

Type: Integration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [GLM-5.2 で構築された ZCode 用 Linux ラッパー](https://x.com/gosrum/status/2066484949755269510) (by [@gosrum](https://x.com/gosrum))

**このケースは、コーディング エージェント環境に関するツールを支援する GLM-5.2 の例として使用してください。**

著者は、GLM-5.2 と Claude Code を使用して zcode-linux を完成させ、Linux ユーザーが Linux 環境で ZCode を実行し、ローカル LLM エンドポイントを含む任意の API エンドポイントを追加できるようにしたと報告しています。

Type: Demo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [コンピュータ使用スキルのパッケージ化](https://x.com/0xSero/status/2065952130054382079) (by [@0xSero](https://x.com/0xSero))

**このケースを使用して、オープンソースのコンピューター使用リポジトリを再利用可能なスキルに変えるためのヘルパーとして GLM-5.2 を検討してください。**

この投稿では、GLM-5.2 がコンピューターの使用を設定し、高度なオープンソース リポジトリを見つけて、それをスキルに変換したと述べています。これは、ツールのラッピングとエージェントの統合作業のための実践的なシグナルです。

Type: Demo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 エージェント開発環境のレビュー](https://x.com/laogui/status/2066190262993559963) (by [@laogui](https://x.com/laogui))

**このケースを使用して、単一のチャット セッションではなく完全なエージェント開発環境内で GLM-5.2 を評価します。**

中国のレビューによると、ZCode 3.0 はシェルのような以前のバージョンから、GLM-5.2 と組み合わせた自社開発のエージェント コアに書き直され、国内のエージェント開発環境の中でより優れたエクスペリエンスを備えているとのことです。

Type: Demo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [ローカルサービスを備えた OpenCode ハーネス](https://x.com/PatrickToulme/status/2068134212587184442) (by [@PatrickToulme](https://x.com/PatrickToulme))

**このケースを使用して、Claude Opus と比較する前に、OpenCode ハーネス、ローカル サービング、およびツールを多用するコーディング ワークフローを使用して GLM-5.2 をテストします。**

著者は、ローカル展開、ネストされたサブエージェント、調査/計画動作、および動作するアプリケーションのビルドを報告します。

Type: Evaluation | Date: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM ロングコンテキスト命令インジェクション](https://x.com/neural_avb/status/2067992817625088439) (by [@neural_avb](https://x.com/neural_avb))

**このケースを使用して、指示を RLM システム プロンプトに移動することで、GLM-5.2 のロング コンテキストのカウントと REPL エージェントの動作を改善します。**

リリース ノートでは、具体的なエージェント スキャフォールディングの変更と GLM-5.2 ロング コンテキスト ベンチマーク効果について説明しています。

Type: Integration | Date: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents コード オープン ハーネス トライアル](https://x.com/sydneyrunkle/status/2067947260369854830) (by [@sydneyrunkle](https://x.com/sydneyrunkle))

**このケースを使用して、オープン コーディング エージェント ハーネスで GLM-5.2 を試し、再現可能なエージェント シェルでモデルを比較します。**

著者は、DeepAgents コードで GLM-5.2 を使用することを報告し、オープン モデルとオープン ハーネスをテスト パターンとして示しています。

Type: Demo | Date: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [本番マーケティング agent stack のルーティング](https://x.com/DeRonin_/status/2068303752671477820) (by [@DeRonin_](https://x.com/DeRonin_))

**構造化、速度、self-hosting を重視する production agent workflow に GLM-5.2 を割り当てつつ、曖昧な判断はより強い closed model に任せるためのケースです。**

作者は agency stack で 6 日間の side-by-side run を行った後、GLM-5.2 は drift するまで 60 を超える agent step を維持し、800 回以上連続で structured format に一致し、低遅延の self-hosted response を返したと述べています。同じ投稿では voice が重要な task や曖昧な task では依然として Opus を好むとしており、その routing rule 自体が有用な takeaway です。

Type: Evaluation | Date: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 ウルトラポケモンレッド ゴールラン](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**M3 Ultra 上での長時間ローカル coding agent 実行において、GLM-5.2 を評価するためのケースです。約半日かけて Pokemon Red を HTML で再現しようとした実例を追えます。**

作者は Claude Code の model をローカル GLM 5.2 に差し替え、M3 Ultra 512GB マシンで 12 時間の `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` を実行しました。投稿では実行時間、token 使用量、code churn、RAM 使用量、GGUF と KV-cache 構成が共有されており、品質は frontier 級に感じる一方でローカル推論速度が主なボトルネックだと述べています。

Type: Demo | Date: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo バグ修正対決](https://x.com/cline/status/2069171146994729078) (by [@cline](https://x.com/cline))

**実際のリポジトリのバグ修正で GLM-5.2 と Opus 4.8 を比較するためのケースです。GLM はより多くのトークンを使いましたが、より安価でクリーンな最終パッチを出しました。**

Cline は同じハーネスとツールの下で、Cline リポジトリの同一バグに対して両モデルをテストしました。投稿によれば、GLM は約 110 万トークン、Opus は 66 万トークンを使用し、コストは 0.41 ドル対 0.81 ドル、所要時間は 4.7 分と 28 回のツール呼び出し対 1.6 分と 12 回でした。さらに、GLM はデッドコードの整理と本番ビルド成功で終えた一方、Opus はテストは通ったものの型エラーを残しました。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 バックグラウンド エージェント](https://x.com/colemurray/status/2069485572339707938) (by [@colemurray](https://x.com/colemurray))

**ホスト型チャットではなく、GLM-5.2 を FP8 で回すセルフホストの background-agent stack を調べるためのケースです。**

colemurray は、Modal Inference 上の OpenInspect を、GLM-5.2 を FP8 で動かす完全セルフホストの background agent system として共有し、重要なインフラに対する速度と制御性を強調しています。投稿自体は短いですが、使っているツールスタックとデプロイ形態を明確に示しています。

Type: Integration | Date: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [OpenCode と Fireworks へのコスト削減移行](https://x.com/SeekingN0rth/status/2071484711327985696) (by [@SeekingN0rth](https://x.com/SeekingN0rth))

**open-model harness への切り替えだけで十分か確かめたいならこの事例が役立ちます。作者は個人の coding と loop task を Fireworks 上の GLM-5.2 + OpenCode に移し、日常品質をほぼ保ったまま token コストが 3 分の 1 になったと言っているからです。**

SeekingN0rth は、個人の coding と loop task を週末のうちに Fireworks 上の GLM 5.2 + OpenCode へ移したことで、token 支出が約 3 分の 1 になったと述べています。投稿では、体験を決めたのは frontier かどうかより harness だとされており、OpenCode は terminal での Claude Code に近い感触で、日常タスクでは目立った品質低下もなかったといいます。この例は、コストを絶対的な SOTA より重視する大企業にも通じるモデル切り替えパターンとして語られています。

Type: Evaluation | Date: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA の GLM アグリゲーターワークフロー](https://x.com/IBuzovskyi/status/2071601107944571249) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**価値の高い agent の 1 ターンに追加のオーケストレーションをかける価値があるなら、この事例が役立ちます。Hermes Agent の Mixture of Agents 構成は、GLM-5.2 と他モデルを組み合わせ、小さな追加コストで目に見えて良い出力を出したからです。**

IBuzovskyi は Hermes Agent の Mixture of Agents モードを、ツールアクセスを持つ 1 つのアグリゲーターモデルと、私的な助言だけを返す複数の参照モデルの組み合わせとして説明しています。投稿では、GLM 5.2 単体だと 13 分・0.38 ドルだった coding テストが、GLM 5.2 をアグリゲーターにして Kimi K2.6 と MiniMax M3 を組み合わせると 35 分・0.47 ドルになった一方で、アニメーション、ビジュアル、ゲームメカニクスはより良くなったと報告しています。プリセット設計、機能の有効化場所、追加レイテンシを許容すべき場面も整理されています。

Type: Integration | Date: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline の推論オン/オフによるハーネス差分](https://x.com/akshay_pachaar/status/2071638409022763292) (by [@akshay_pachaar](https://x.com/akshay_pachaar))

**モデルの重みだけでなく harness 設計を見たいならこの事例が役立ちます。同じ GLM-5.2 が同じ coding task で、reasoning を有効にしただけで 57.3% から 68.5% に伸びたからです。**

akshay_pachaar は、同じ GLM 5.2 に同じ coding task 群を与えた Cline のテストを引用しています。reasoning をオフにすると 57.3%、オンにすると 68.5% でした。この差を使って投稿は、出力が単なるテキストではなく出荷可能なコードになるかどうかは、コンテキスト保持、ツール利用、編集適用、検証ループが基盤モデルと同じくらい重要だと論じています。

Type: Evaluation | Date: 2026-06-29

<a id="case-136"></a>
### Case 136: [カーソル + Fireworks 455M トークンのフィールド テスト](https://x.com/robinebers/status/2071246749210190132) (by [@robinebers](https://x.com/robinebers))

**高速な Fireworks 提供と 4.55 億 tokens の実運用を作者が報告しており、すぐに Opus や GPT-5.5 に戻る気がないとしているため、GLM-5.2 を Cursor の本格的な常用モデルとして判断するためのケースです。**

robinebers は、Cursor で GLM 5.2 に切り替えて 36 時間使ったことで、このモデルへの見方が Fireworks と組み合わせた時点で大きく変わったと述べています。投稿では、image support、ゼロデータ保持の主張、毎秒約 80-100 tokens の throughput、そして 4 億 5500 万 tokens に対して約 145 ドルかかった点を具体的に挙げています。汎用的な benchmark 賞賛よりも、provider の選択が実運用体験を変えることを示す、harness 固有の強い評価例です。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [スキルポータビリティを備えた Devin デスクトップ ハーネス](https://x.com/lily_gpupoor/status/2071297351801794850) (by [@lily_gpupoor](https://x.com/lily_gpupoor))

**Z.ai 自身の coding surface が不安定に感じられるときに、GLM-5.2 を Devin Desktop 内で試すためのケースです。作者は、より簡単な skill 移植、高速さ、そして hackability の高さを報告しています。**

lily_gpupoor は、API が不安定だった時期に、Devin Desktop 経由で大量に使った GLM-5.2 の体験が、Z.ai の直接の coding plan より明確に良かったと述べています。投稿では、custom Solarized Green theme の JSON を GLM が編集して extension の登録まで成功したこと、Devin が異様に速く感じられたこと、そして既存の skill の大半がデフォルトの Windsurf Cascade agent から Devin Local へ切り替えてもそのまま移植できたこと、という 3 つの具体的な workflow 上の利点が挙げられています。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi インライン GLM レビュアー](https://x.com/xpasky/status/2070831715518460177) (by [@xpasky](https://x.com/xpasky))

**Pi スタイルの coding-agent loop に第 2 のレビュー担当を加えたいときに使うケースです。作者によれば、GLM-5.2 は Opus に turn ごとに助言でき、コスト増はおよそ 10% に収まるとのことです。**

xpasky は、チームが GLM-5.2 を Pi workflow の第 2 レビュアーとして使っており、1 つの Opus がコーディングし、もう 1 つの Opus が難題を解き、その横で GLM が turn ごとに Opus へ助言していると述べています。投稿では、この reviewer を追加してもコスト増は約 10% にとどまり、これまでで最良の code が得られているとも評価しています。

Type: Integration | Date: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter による一発 Telegram Bot](https://x.com/MatinSenPai/status/2070259817818812701) (by [@MatinSenPai](https://x.com/MatinSenPai))

**最低限動くだけのコードではなく、本番運用を意識した default を GLM-5.2 が one-shot の coding-agent build で自力推論できるか試すためのケースです。**

MatinSenPai は、動画と同じ prompt から GLM 5.2 で Telegram bot を one shot で作ったと報告し、頼んでいない実務的な配慮までモデルが自動で入れたと述べています。投稿では、動画送信後の自動ファイル削除、Telegram Bot API のサイズ制限を踏まえたデフォルト 50MB cap、完了前の繰り返し self-test、以前の MiMo build よりきれいな structure、そして AgentRouter 経由で約 140K tokens、概算 5 ドル程度の利用が挙げられています。

Type: Demo | Date: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go リファクタリング初回成功](https://x.com/vedovelli74/status/2069889605969592500) (by [@vedovelli74](https://x.com/vedovelli74))

**ベンチマーク主張だけに頼らず、OpenCode 内の中規模 Go リファクタリングで GLM-5.2 を評価するためのケースです。**

vedovelli74 は、中規模の GoLang コードベースを対象にした最初の OpenCode 実行を報告し、GLM-5.2 は Opus 4.8 より高速で、トークン効率も高く、何をリファクタリングすべきかを初回判断で正しく見抜いたと述べています。さらに、その結果は後から Codex と Opus でも検証され、それでも納品品質では GLM-5.2 が上回ったとしています。

Type: Evaluation | Date: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 3.36ドル常用実行](https://x.com/clairevo/status/2069828122640548204) (by [@clairevo](https://x.com/clairevo))

**より自律的な coding work を open weights に移す前に、Claude Code と Cursor で日常利用モデルとしての GLM-5.2 を見極めるためのケースです。**

clairevo は、GLM 5.2 が Claude Code と Cursor におけるデフォルトモデルになっており、ここまでの利用コストは 3.36 ドルだと述べています。投稿では、Opus に近い coding quality を感じたことに加え、OpenRouter 経由のセットアップ経路、フロントエンドのデザイン感、長時間の autonomous task に関する評価が、常用モデルとして採用した理由だと説明しています。

Type: Evaluation | Date: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 実演デモとショーケースビルド
<a id="case-229"></a>
### Case 229: [Hyperagent プロフィール・ポートフォリオ対決](https://x.com/arsh_goyal/status/2077764207945416949) (by [@arsh_goyal](https://x.com/arsh_goyal))

**このケースは、実際の browser-based agent タスクで GLM-5.2 を他の open model と比べたいときに使えます。arsh_goyal によると、GLM 5.2、DeepSeek V4、Kimi K2.6、Qwen 3.7 を Hyperagent 上で並列に走らせ、公開プロフィールから personal portfolio を作らせたためです。**

arsh_goyal は、各モデルに本物の browser を持つ別々の cloud machine を与え、YouTube、LinkedIn、X のプロフィールを読ませたうえで、同じ one-line prompt から website を組み立てさせたと説明しています。投稿は run ごとの cost と duration を公開し、さらに video と prompt も reply thread に添えているため、単なる screenshot や leaderboard repost よりも hands-on 比較としての強度が高いケースです。

Type: Demo | Date: 2026-07-16

---
<a id="case-218"></a>
### Case 218: [OpenCode によるポートフォリオと OS 再構築](https://x.com/MarkSShenouda/status/2077032282141978842) (by [@MarkSShenouda](https://x.com/MarkSShenouda))

**このケースは、GLM-5.2 を野心的な OpenCode build で見極めたいときに使えます。MarkSShenouda によると、OpenCode Go と GLM-5.2 によって、portfolio site の再構築と、WASM または Qemu emulator で動く C / Assembly 製の本物の OS 開発が進んだからです。**

この投稿は、GLM-5.2 をおもちゃの demo ではなく、2 つの完成物に結び付けています。ひとつは作り直した portfolio site、もうひとつは C と Assembly で書かれた operating system project で、WASM と Qemu をターゲットにしています。tweet 自体は短いですが、2 つのリンク付き preview があるため、大きめの maker-style coding 事例として十分具体的です。

Type: デモ | Date: 2026-07-14

---
<a id="case-213"></a>
### Case 213: [LlamaCoder v4 GLM 再構築](https://x.com/nutlope/status/2076722464671793184) (by [@nutlope](https://x.com/nutlope))

**このケースは、GLM-5.2 の planning と design の強みを使って one-prompt app generation を試作するときに役立ちます。nutlope によれば、LlamaCoder v4 は GLM 5.2 を中心に再構築され、parsing と planning が改善され、現在は無料の open-source stack 上で WebAssembly renderer まで搭載しているためです。**

nutlope は、LlamaCoder v4 が現在 GLM 5.2 を中心にし、UI レイヤーを Base UI with shadcn に切り替え、parsing、planning、app design を改善し、さらに WebAssembly ベースの renderer を追加したと述べています。プロジェクトは free、open source、Together powered と説明されており、単なる model-quality の感想ではなく、実際に出荷された具体的 demo です。

Type: Demo | Date: 2026-07-13

---

<a id="case-202"></a>
### Case 202: [コマンドコードスペースシューター機能勝利](https://x.com/CommandCodeAI/status/2075264795817972107) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**このケースは、one-shot の interactive UI build で GLM-5.2 を比べたいときに使えます。Command Code が同じ retro space-shooter prompt を Fable 5、GPT 5.5、GLM 5.2、DeepSeek V4 Pro に流し、features では GLM を最上位に置いたためです。**

Command Code は、同じ `/design` prompt で 4 モデルとも近い retro pixel-art space-shooter layout を出したものの、GLM 5.2 は sound、controls、leveling、overall UX で特に目立ち、cost も Fable 5 の $0.80 に対して $0.07 だったと述べています。単なる benchmark screenshot ではなく、軽量な game/UI build の実地比較として見られます。

Type: Evaluation | Date: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [ZCode ニンテンドー DS エミュレータ](https://x.com/0xSero/status/2074870153267818638) (by [@0xSero](https://x.com/0xSero))

**このケースは、長時間にわたる local coding build を見たいときに使えます。作者が 4x RTX 6000 上の ZCode で GLM-5.2 を動かし、Nintendo DS emulator を C++ でゼロから作ることを目標にしたためです。**

source では、4 枚の RTX 6000 を積んだ setup 上の ZCode で GLM-5.2 が動いており、ready-made emulator を使わずに C++ で Nintendo DS emulator を作り、Mario 64 DS の ROM が動くまで止まらないという具体的な目標が与えられています。つまりこれは、曖昧な『小さなアプリを作った』話ではなく、明確な終点を持つ本物の coding-agent demo です。

Type: Demo | Date: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [コマンドコード Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**このケースは、GLM-5.2 を軽い design-game task で比較したいときに使えます。作者が同じ Flappy Bird prompt を Command Code で流し、Fable 5 は GLM-5.2 の約 9 倍近い価格にもかかわらず UX で決定的優位を示さなかったと結論づけているためです。**

投稿では、同じ game prompt と同じ Command Code の `/design` 設定を DeepSeek V4 Pro、GLM 5.2、Fable 5 に対して使ったと説明しています。GLM 5.2 は価格では DeepSeek と Fable の中間でしたが、作者は Fable の UX 差分がその価格差を正当化するほど大きくなかったと述べています。つまりこれは、generic な arena claim ではなく、実地の UX-versus-cost 比較です。

Type: Evaluation | Date: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [NVFP4 ルービック キューブ ワンショットを REAP](https://x.com/RoundtableSpace/status/2072700573145788914) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**このケースは、単一プロンプトの対話型 build で GLM-5.2 を試すのに向いています。REAP-NVFP4 の demo では、1 回の prompt だけで 3D Rubiks Cube、実際の scramble、live state、solve button まで生成したと述べています。**

RoundtableSpace によると、GLM-5.2-REAP-NVFP4 には HTML prompt を 1 つだけ渡し、live state、real scramble logic、solve action を備えた 3D Rubiks Cube app が返ってきました。コード詳細は薄いものの、generic な benchmark screenshot ではなく、具体的な one-shot build demo です。

Type: Demo | Date: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP リレー iPhone クライアント](https://x.com/mov_axbx/status/2072192903762288721) (by [@mov_axbx](https://x.com/mov_axbx))

**このケースは、ローカル GLM-5.2 エージェントを素早くモバイル面に載せたいときに使えます。著者によれば、Codex の build-ios-app plugin が、すでに GLM-5.2 と Cloudflare トンネルを使う OMP relay 向けに、数時間で整った iPhone クライアントを作りました。**

mov_axbx は、ローカルホストの OMP エージェント向けに電話アプリが欲しくなり、Codex の build-ios-app plugin を使って数時間で整った版を得たと言っています。バックエンド側は GLM-5.2 と OMP で書かれた custom relay を使い、トンネルは Cloudflare が担っていました。

Type: Demo | Date: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [オープンソースの DevRel リサーチエージェント](https://x.com/Astrodevil_/status/2071572680470655253) (by [@Astrodevil_](https://x.com/Astrodevil_))

**GLM-5.2 を汎用チャットではなく縦型の調査アシスタントに変えたいならこの事例が役立ちます。作者は、製品とオーディエンスの入力を根拠付きのコンテンツ候補とアウトラインに変えるオープンソース DevRel エージェントを作ったからです。**

Astrodevil_ は GLM-5.2 上に、製品とターゲットの説明を受け取る chat-first の DevRel 調査アプリを構築しました。Hacker News から需要シグナルを探し、DEV のコンテンツギャップを調べ、Engram memory で事実を更新し、根拠付きで優先順位付けされたトピック案とアウトラインを返します。投稿では Agno、Weaviate Engram、Nebius inference、そしてオープンソースのコードベースも明示しています。

Type: Demo | Date: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 6 バリエーションの LP 反復ループ](https://x.com/nutlope/status/2070199649818779914) (by [@nutlope](https://x.com/nutlope))

**まず複数の GLM-5.2 案を作ってから最良案を coding agent に引き継ぎ、低コストで landing page を試作するためのケースです。**

nutlope は、GLM 5.2 と Recast を使った web iteration workflow を説明しています。1 つの prompt から landing page を 6 variations 生成し、最も良い design を選び、その code をダウンロードして別の coding agent で反復を続ける流れです。投稿では、GLM-5.2 は fast で cheap かつ design に強いためこの用途に向いており、同じ予算で Opus 4.8 の 1 ページに対して GLM では 3〜6 案ほど作れることが多いと述べています。

Type: Tutorial | Date: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [プレイ可能なバックルーム ワンショット](https://x.com/aimlapi/status/2066996493257408639) (by [@aimlapi](https://x.com/aimlapi))

**このケースを使用して、GLM-5.2 と Opus 4.8 の間で同じプロンプトのゲーム構築の出力、ランタイム、コストを比較します。**

AI/ML API は、GLM-5.2 および Opus 4.8 に、プレイ可能なバックルーム ゲームをワンショットで実行するよう要求すると報告しました。彼らの投稿によると、GLM-5.2 はより充実した機構を 1:08 で 0.37 ドルで構築したが、Opus は 2:14 で 1.94 ドルかかったという。

Type: Demo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [結果がまちまちの 3 つの実際のビルド](https://x.com/bridgemindai/status/2065840871929442319) (by [@bridgemindai](https://x.com/bridgemindai))

**このケースは、注意深いデモ セットとして使用してください。実稼働ゲームやビデオ タスクのモデルを信頼する前に、複数の実際のビルドをテストしてください。**

BridgeMind は、ホラー ハウス ゲーム、3D ステルス ゲーム、およびリモート マーケティング ビデオで GLM-5.2 をテストしました。この投稿では、壊れたゲーム ロジックを含むさまざまな結果が報告されており、根拠のある制限信号として役立ちます。

Type: Evaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [ZCode でのスーパー マリオ クローン](https://x.com/ivanfioravanti/status/2066272681406980208) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースを使用して、いくつかの修正と機能のパスにわたって GLM-5.2 と ZCode を使用した反復的なゲーム構築を評価します。**

著者は、スーパー マリオ スタイルのクローンを作成して GLM-5.2 で ZCode 3.0 をテストし、問題修正と機能追加を 5 回繰り返した後に結果を共有しました。

Type: Demo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [月着陸船コンテスト](https://x.com/ivanfioravanti/status/2066193134984319173) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースを使用して、インタラクティブなゲーム スタイルのタスクで GLM-5.2、MiniMax M3、および Kim K2.7 コードを比較します。**

この投稿では、ローカル モデルの開発に戻る前の実用的なベンチマークとしてビデオ結果を使用して、MiniMax M3、GLM-5.2、および Kim K2.7 コード間の月着陸船コンテストについて説明しています。

Type: Evaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [ワンプロンプトのデザインアリーナの作成](https://x.com/grx_xce/status/2066951779154374907) (by [@grx_xce](https://x.com/grx_xce))

**このケースを使用して、GLM-5.2 がアリーナ コンテキスト内の単一のデザイン プロンプトから何を生成できるかを検査します。**

著者は、デザイン アリーナで 1 つのプロンプトから作成された GLM-5.2 作成の例を共有し、それを使用してオープン ウェイト モデルとクローズド ウェイト モデル間のギャップが縮まっていることを示しました。

Type: Demo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [研究論文のワークフローを理解する](https://x.com/askalphaxiv/status/2066996976445706745) (by [@askalphaxiv](https://x.com/askalphaxiv))

**このケースを使用して、状況に応じた質問や論文間の参照を含む論文読書ワークフローに GLM-5.2 を適用します。**

AlphaXiv は、研究論文を理解するために GLM-5.2 を導入しました。ユーザーはセクションを強調表示したり、質問したり、文脈、比較、ベンチマークの参考として他の論文を参照したりできます。

Type: Integration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [制約された詩の比較](https://x.com/emollick/status/2067056226337186146) (by [@emollick](https://x.com/emollick))

**GLM-5.2 を寓話スタイルのモデルと比較する場合は、このケースを使用して、正確性とクリエイティブの品質を区別します。**

Ethan Mollick 氏は、GLM-5.2 Max が正しい制約のある詩を生み出したことを認め、一方で、Fable は消える文字の制約をより創造的に詩のテーマに組み込んだと指摘しました。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [デザインセンスの例](https://x.com/0xSero/status/2067074877941796994) (by [@0xSero](https://x.com/0xSero))

**このケースを軽量のビジュアル デザイン シグナルとして使用し、独自のプロンプトと UI レビューで検証します。**

著者は、GLM-5.2 のデザインセンスを気に入って、視覚的な例を共有したと述べています。これは、生産設計品質の独立した証拠としてではなく、検査の指針として役立ちます。

Type: Demo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 風ボクセルゲームのワンショット生成](https://x.com/pseudokid/status/2068431546143649829) (by [@pseudokid](https://x.com/pseudokid))

**単一プロンプトのゲーム生成で GLM-5.2 を stress-test し、視覚的にリッチなビルドで何が追加修正を要するかを確認するためのケースです。**

作者は、Temple Run に着想を得た voxel biker game の大半を 1 ターン目で作れたと述べ、その後 camera と movement の修正のために数回の follow-up を行ったと報告しています。さらに、この投稿では Z.ai の tooling が screenshot と gameplay video を生成し、text model が結果を評価する助けになるとも述べられています。

Type: Demo | Date: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go ワンショット実例セット](https://x.com/LyalinDotCom/status/2068378281636982990) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**より open-ended な agent loop に投入する前に、OpenCode Go 内の quick one-shot build で GLM-5.2 を benchmark するためのケースです。**

作者は、OpenCode Go を通じて solar-system web app、system-info Electron app、simple explore-island web game にわたる one-shot 例を報告しています。同じ投稿では、GLM-5.2 はこれまで使った中で最高の open model だとしつつ、frontier-equal と断言することは避けています。

Type: Demo | Date: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [スペースインベーダーのワンプロンプトビルド](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**単一プロンプトのゲーム生成で GLM-5.2 を試し、その後の数回の追加入力で asset 差し替えや軽い polish がどう進むかを見るためのケースです。**

作者は GLM-5.2 が 1 つのメインプロンプトから遊べる Space Invaders 風ゲームを作り、その後 3 回の追加プロンプトで sprite 差し替えや leaderboard などの小さな追加を行ったと報告しています。公開結果は軽量なゲーム生成例として有用ですが、完全な benchmark ではありません。

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab ワンショット](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**対話的な agent failure simulation を素早く試作するためのケースです。作者は約 3.50 ドルで動く recovery lab を one-shot で作れたと報告しています。**

作者は 4,000 語の分析と Agents SDK repository を渡した後、OpenCode と GLM-5.2 で完全に操作可能な recovery lab を構築しました。投稿では 176k tokens の実行、one-shot の成功、polish 前で約 3.50 ドルという end-to-end cost が示されています。

Type: Demo | Date: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [オープンデザイン参照 URL 再構築](https://x.com/OpenDesignHQ/status/2069046584134778995) (by [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**参照ベースの Web 再現で GLM-5.2 を試すためのケースです。1 つのプロンプトと元 URL だけで、ほぼピクセルレベルの忠実さでサイトを再現しました。**

Open Design は、組み込みの AMR で参照 URL と簡単な 1 つのプロンプトだけを使って GLM-5.2 をテストし、デモではウェブサイトをほぼ完璧に再現したと述べています。完全なベンチマークではなく、参照ベース UI 生成の実演的な証拠として扱うべきケースです。

Type: Demo | Date: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [トレーダーデスクのコスト品質テスト](https://x.com/atomic_chat_hq/status/2069171121044513273) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**フルスタック UI 構築で GLM-5.2 を比較するためのケースです。最も洗練された取引デスク出力にかなり近づきながら、コストはそのごく一部に収まりました。**

Atomic Chat は、フロントエンド、バックエンド、8 銘柄の市場データ、カスタムのダークテーマ UI を含む同一の Trader Desk ビルドプロンプトで 4 つのモデルを比較しました。投稿によると、GLM-5.2 は 13,677 トークンで 0.03 ドル、Fugu Ultra は 22,225 トークンで 0.51 ドルでした。GLM は、はるかに低コストで、ライブデータ付きの同程度に完成したマルチパネル UI を出力したとされています。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [クロードの拒否後のラッダイト・ゲーム](https://x.com/atmoio/status/2069559053114577088) (by [@atmoio](https://x.com/atmoio))

**クローズドモデルが拒否したゲーム案を GLM-5.2 で代替試作し、実際に動く出力を自分で検証するためのケースです。**

atmoio は、AI を破壊する Plague Inc 風のユーモアゲームが Claude で利用規約違反と判定されたため、代わりに GLM 5.2 で Luddite を制作し、デモ動画も添付したと述べています。ポリシー上の理由でクローズドモデルが拒否しがちな creative coding task に対する実地の代替例として扱えます。

Type: Demo | Date: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 プロバイダ・ツール統合
<a id="case-258"></a>
### Case 258: [Orbit Provider 50% GLM アクセス](https://x.com/orbiteditor/status/2079148011259916552) (by [@orbiteditor](https://x.com/orbiteditor))

**このケースは、個別の provider credentials を管理せずに Orbit 内で GLM-5.2 を試したいときに役立ちます。Orbit Editor v0.4.0 によると、新しい Orbit Provider が editor 内で GLM-5.2 を直接提供し、50 percent off で開始されたためです。**

Orbit Editor の v0.4.0 告知では、open-source models 向けの組み込み provider layer が導入され、個別の API key や provider setup を 1 つの editor workflow の裏側へ隠すことが目標だと説明しています。投稿では、ユーザーが 1 か所で model を選び、coding を始め、usage を追跡し、cost を管理できるとし、GLM-5.2 は 50 percent off の価格で立ち上がったと述べています。GLM を friction 少なく試したい team にとって、具体的な editor integration と access note です。

Type: Integration | Date: 2026-07-20

---
<a id="case-256"></a>
### Case 256: [pen.dev 並列デザイン評価](https://x.com/tomkrcha/status/2079253857834828230) (by [@tomkrcha](https://x.com/tomkrcha))

**このケースは、1 つのローカル workflow 内で GLM-5.2 を design-oriented な競合と比較したいときに役立ちます。tomkrcha によると、pen.dev は ChatGPT、Claude、Cursor Composer、OpenCode Go、Kimi、Grok、Gemini、Qwen などと並列に GLM 5.2 を desktop codebase 上の design task へ流せるためです。**

tomkrcha は、pen.dev を単一 model の demo ではなく realtime な design-agent surface として位置付けています。投稿によると、builder は既存の ChatGPT や Claude subscription で sign in し、Cursor Composer、GitHub Copilot、OpenCode Go、Grok 4.5、Kimi、MiniMax、GLM 5.2、Gemini、Qwen を接続したうえで、同じローカル project 内の frontend design task に対して組み合わせて使えます。孤立した benchmark screenshot ではなく、UI-heavy な作業で GLM-5.2 を横並び比較できる具体的な evaluation surface です。

Type: Integration | Date: 2026-07-20

---
<a id="case-239"></a>
### Case 239: [TokenRouter の無料 GLM API 枠](https://x.com/meliasiih/status/2078180641468985564) (by [@meliasiih](https://x.com/meliasiih))

**このケースは、期間限定の無料 GLM-5.2 API ルートを確保したいときに使えます。meliasiih によると、TokenRouter は 2026-07-25 まで無料アクセスを提供しており、簡単な signup、API key 発行、公開 base URL が揃っているためです。**

meliasiih は、email か X で signup し、account を verify し、API key を生成し、GLM-5.2 を選択して `https://api.tokenrouter.com/v1` に client を向けるまでの実用的な手順を示しています。さらに、この free-access program は 2026-07-25 までだと明記しており、すぐに行動できる time-boxed hosted-access note になっています。

Type: Tutorial | Date: 2026-07-17

---
<a id="case-238"></a>
### Case 238: [Agentuity 向け Wafer GLM Gateway](https://x.com/wafer_ai/status/2078186124258984374) (by [@wafer_ai](https://x.com/wafer_ai))

**このケースは、Agentuity gateway stack に GLM-5.2 を追加したいときに使えます。wafer_ai によると、同社の serverless route は Agentuity 上で GLM 5.2 を regular / Fast の両 tier で約 100 から 250 tok/s、1M context 付きで提供しているためです。**

wafer_ai は、最速の serverless GLM 5.2 route が Agentuity AI Gateway で利用可能になり、Wafer が regular と Fast の両 variant を提供していると述べています。post は単なる availability note ではなく、約 100 から 250 tokens per second と 1M-token context window という実運用に使える profile を明示しています。

Type: Integration | Date: 2026-07-17

---
---
<a id="case-232"></a>
### Case 232: [Macroscope Check Run GLM エージェント](https://x.com/kayvz/status/2077810181904494631) (by [@kayvz](https://x.com/kayvz))

**このケースは、PR review agent のコストを下げつつ check-run workflow を維持したいときに使えます。kayvz によると、Macroscope の Check Run Agents は通常の `.md` ベース repo config から GLM 5.2 を選べるようになったためです。**

kayvz は、新しい model options が check-run `.md` ファイルの設定時にそのまま現れると述べており、これは単なる availability post より実装面に近い更新です。thread は custom code-review agents for pull requests を明示的な対象にしているため、Macroscope 経由で review automation を回していて open-weight 選択肢を探すチームにとって具体的な integration surface になります。

Type: Integration | Date: 2026-07-16

---
<a id="case-231"></a>
### Case 231: [Aster の 281 TPS research-agent API](https://x.com/asterailabs/status/2077556435085574429) (by [@asterailabs](https://x.com/asterailabs))

**このケースは、高速な hosted GLM-5.2 endpoint を benchmark したいときに使えます。asterailabs によると、Aster Inference は research-agent 最適化由来の API で GLM 5.2 を 281 tokens per second で提供しているためです。**

Aster は、自社製品を AI research agents から生まれた inference API と位置付け、単なる launch 文句ではなく具体的な throughput 数値を挙げています。post では GPU 上で gpt-oss-120b が 644 tps、GLM 5.2 が 281 tps とされ、さらに自社 research system で得た inference 知見をそのまま product improvements に戻していると述べているため、ゼロから self-hosting する前に hosted provider を比較したいチームに適した route です。

Type: Integration | Date: 2026-07-16

---
<a id="case-230"></a>
### Case 230: [TrueFoundry 向けネイティブ Wafer GLM ルート](https://x.com/wafer_ai/status/2077837999514214456) (by [@wafer_ai](https://x.com/wafer_ai))

**このケースは、既存の TrueFoundry AI Gateway stack に GLM-5.2 を差し込みたいときに使えます。wafer_ai によると、native provider integration は GLM 5.2 と GLM 5.2 Fast から始まり、残りの gateway stack を変えずに使えるためです。**

wafer_ai は、すでに TrueFoundry AI Gateway を使っているチームなら、stack の他の部分を変えずに Wafer models を導入できると説明しています。rollout は GLM 5.2 と GLM 5.2 Fast から始まり、post では Wafer を最速の serverless GLM route と位置付けているため、一般的な model availability 通知よりも具体的な managed-access path として読めます。

Type: Integration | Date: 2026-07-16

<a id="case-225"></a>
### Case 225: [TogetherLink Codex Harness Bridge](https://x.com/nutlope/status/2077432463685554558) (by [@nutlope](https://x.com/nutlope))

**このケースは、既存の coding-agent CLI の中で GLM-5.2 を動かしたいときに使えます。nutlope によると、TogetherLink は Codex や Claude Code から GLM 5.2 のような open model を直接呼び出せる open-source CLI だからです。**

この告知では、TogetherLink を、開発者が使い慣れた coding harness を保ったまま、下層の model だけを open-weight stack に差し替えるための bridge layer と位置付けています。投稿では Codex と Claude Code を対応 harness として明示し、project を open source だと説明しているため、既存の terminal workflow を捨てずに GLM-5.2 を試したいチームにとって具体的な access route です。

Type: Integration | Date: 2026-07-15

---
<a id="case-224"></a>
### Case 224: [Vorflux Open Model Harness Routing](https://x.com/vorfluxai/status/2077449967711760587) (by [@vorfluxai](https://x.com/vorfluxai))

**このケースは、custom glue なしで GLM-5.2 をフル agent session に組み込みたいときに使えます。vorfluxai によると、その Open Model Harness では Vorflux の通常フローを維持したまま、GLM 5.2 を design、build、simplify の各 step に割り当てているためです。**

vorfluxai によると、この harness は dropdown ひとつで session 全体を open models に切り替えつつ、planning、subagents、pull requests、testing では通常の Vorflux flow をそのまま保てます。公開された routing table では、DeepSeek V4 Pro が main、plan、review、DeepSeek V4 Flash が explore、GLM 5.2 が design、build、simplify、Kimi 2.7 Code が debug と testing を担当しており、これは単なる availability post ではなく、具体的な multi-model agent orchestration pattern です。

Type: Integration | Date: 2026-07-15

---
<a id="case-170"></a>
### Case 170: [NVIDIA 無料 API プラグアンドプレイ アクセス](https://x.com/hqmank/status/2072855265612030010) (by [@hqmank](https://x.com/hqmank))

**このケースは、無償の hosted endpoint 経由で GLM-5.2 を素早く試すのに役立ちます。hqmank は NVIDIA が OpenAI 互換 API ルートを公開し、plug-and-play の差し替えとして動いたと確認しています。**

hqmank は、GLM-5.2 が NVIDIA の無料 API に追加され、簡単な hands-on test で問題なく動いたと述べています。投稿では OpenAI 互換かつ plug-and-play とされる一方、無料 tier は需要増で厳しくなる可能性も示されています。短期的な評価や一時的な agent routing の実用的な access note です。

Type: Integration | Date: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [無料の Workers AI コーディング エージェント ルート](https://x.com/ClaudeCode_UT/status/2072881775408456066) (by [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**このケースは、coding agent 向けに無料の GLM-5.2 ルートを立ち上げるためのものです。チュートリアルでは Workers AI を Claude Code、OpenCode、Cursor、Aider に、OpenAI 互換の `cf/zai-org/glm-5.2` endpoint 経由で接続しています。**

ClaudeCode_UT は、Cloudflare の無料アカウント作成、Workers AI の account ID 取得、API token 発行、OpenAI 互換ツールへの Cloudflare provider 追加、`cf/zai-org/glm-5.2` の選択、Claude Code や Cursor、Aider、OpenCode の起動という 6 ステップを示しています。token 課金の前に coding-agent workflow を試したいチーム向けの実用的な access tutorial です。

Type: Tutorial | Date: 2026-07-03

---

<a id="case-220"></a>
### Case 220: [OpenMed の de-id 臨床エージェント](https://x.com/MaziyarPanahi/status/2077000157103898789) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**このケースは、GLM-5.2 を privacy-preserving な clinical agent flow の中に置きたいときに使えます。MaziyarPanahi によると、OpenMed が識別子をローカルで除去し、Gemma 4 が構造化を担当したあと、GLM 5.2 が症例全体を計画し、ツールを呼び、disposition まで書いたためです。**

MaziyarPanahi は、OpenMed が端末上で de-identification を行い、Gemma 4 が structure を抽出し、GLM-5.2 が redact 済みテキスト上で agentic な medical reasoning を担う完全 open workflow を説明しています。運用上の重要点は、生の clinical note が一度も端末外へ出ないことです。これにより、この thread は単なる model 推しではなく、医療プライバシーと tooling の具体的パターンになります。

Type: 統合 | Date: 2026-07-14

---
<a id="case-219"></a>
### Case 219: [Katana の USDC GLM アクセスルート](https://x.com/imgn_ai/status/2077061568068465148) (by [@imgn_ai](https://x.com/imgn_ai))

**このケースは、wallet ネイティブな pay-per-request ルートで GLM-5.2 を公開したいときに使えます。imgn_ai によると、Katana は Base 上の x402 を通じて、アカウント不要・USDC 決済・公開 llms.txt 付きで GLM-5.2 を提供しているためです。**

imgn_ai は Katana を、開発者がサービスの llms.txt をコピーし、wallet を接続して、frontier の text / image / video model を wholesale price で呼び出せる x402 ベースの経路として紹介しています。投稿にはアカウント不要で、支払いは USDC の request 単位だと明記されているため、常設の SaaS アカウントを持ちたくない実験用途に具体的な access option になります。

Type: 統合 | Date: 2026-07-14

---
<a id="case-214"></a>
### Case 214: [Databricks AI Gateway GLM ルート](https://x.com/QCXINT_/status/2076490318695088218) (by [@QCXINT_](https://x.com/QCXINT_))

**このケースは、agent tooling 内で GLM-5.2 への高速な managed access path を試すときに使えます。QCXINT_ によれば、Databricks AI Gateway が組織固有の base URL と token flow を発行し、非常に高速で 1M context に見える GLM 5.2 ルートを exposed した一方、backend identity はまだ未確認のままだからです。**

QCXINT_ は、具体的な setup flow を示しています。Databricks workspace を作成し、User Settings を開き、AI Gateway scope 付きの access token を作り、組織固有の AI Gateway base URL をコピーしたうえで、OpenClaw や Hermes のような agent tool から exposed endpoint を呼ぶ流れです。投稿によると、現時点の testing では GLM-5.2 しか見えておらず、速度は異様に速く、最大 1M context をサポートしているように見える一方、gateway が主張する通り backend が本当に厳密な GLM-5.2 なのかは、著者自身まだ確認できていないと明記されています。

Type: Integration | Date: 2026-07-13

---

<a id="case-208"></a>
### Case 208: [オープン分子ビューア エージェント スタック](https://x.com/MaziyarPanahi/status/2075913552854933869) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**このケースは、GLM-5.2 を open な scientific inspection workflow に組み込みたいときに使えます。MaziyarPanahi が Hugging Face Inference Providers 経由の GLM-5.2 を、llama.cpp 上の Qwen3-VL、Mol*、PydanticAI と組み合わせ、1 つの prompt で EGFR と erlotinib の構造を render して critique したためです。**

MaziyarPanahi は、GLM-5.2 が Hugging Face Inference Providers を通じて language brain を担い、Qwen3-VL が llama.cpp 経由で visual inspection を担当し、Mol* が構造を描画し、PydanticAI が agent layer を調整する完全に open な stack を説明しています。投稿では、RCSB PDB の EGFR と erlotinib の例を 1 つの prompt から 6 件の render に落とし込んだとされており、単なる availability announcement ではなく、複数ツールをまたぐ科学系 agent integration の具体例になっています。

Type: Integration | Date: 2026-07-11

---
<a id="case-204"></a>
### Case 204: [Perplexity Advisor WANDR コスト ベースライン](https://x.com/perplexity_ai/status/2075229779716973030) (by [@perplexity_ai](https://x.com/perplexity_ai))

**このケースは、routing された computer-use harness の中で GLM-5.2 の economics を見積もりたいときに使えます。Perplexity が GLM 5.2 plus advisor setup で WANDR 2.1x、Opus 6.1x と述べ、benchmark 全体でもほぼ半額だとしているためです。**

Perplexity は、task あたりの cost を GLM 5.2 baseline で測り、WANDR では GLM 5.2 plus advisor route が 2.1x、Opus が 6.1x だったと述べています。より高価な closed model を毎 step 回す代わりに、安い GLM core を selective escalation と組み合わせる computer-agent routing の具体的シグナルとして読めます。

Type: Evaluation | Date: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [同僚のオープンアーティファクトルーティング](https://x.com/coworkerapp/status/2075233366266310905) (by [@coworkerapp](https://x.com/coworkerapp))

**このケースは、GLM-5.2 を enterprise artifact workflow に入れたいときに使えます。Coworker は Open Artifacts で docs、decks、PDF、spreadsheets、dashboards、apps を作れ、optimized router で token 使用量を約 5x 減らしつつ US-hosted GLM 5.2 を提供すると述べています。**

Coworker は、Open Artifacts が docs、decks、dashboards、spreadsheets、PDF、full apps などの共有可能な成果物を作れると説明しています。同じ launch post では、optimized mode が task ごとに適切な model を選んで token 使用量を約 5 倍削減しつつ、team が US-hosted、SOC 2、connector-rich な環境で GLM 5.2 を使えるとも述べています。

Type: Integration | Date: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [DotCode コンテキストのアップロード ワークフロー](https://x.com/stagedhappen/status/2074775356867789241) (by [@stagedhappen](https://x.com/stagedhappen))

**このケースは、private coding sandbox の中で GLM-5.2 により豊かな project context を与えたいときに使えます。DotCode が GLM 5.2 対応に加えて、screenshot、image、CSV、PDF、source file、zip の upload を同じ filesystem-and-terminal workflow に流せるようにしたためです。**

DotCode は、GLM 5.2 が contextual workspace upload と一緒に動くようになり、agent が file を確認し、project structure をたどり、code を編集し、terminal command を実行し、同じ sandbox から継続できると述べています。投稿では対応 input が列挙され、prompt plus files から sandbox execution までの flow も示されており、real project context から始まる真の coding-agent work への一歩として位置づけられています。

Type: Integration | Date: 2026-07-08

---
<a id="case-221"></a>
### Case 221: [SGLang TopK-V2 による B300 agentic serving](https://x.com/lmsysorg/status/2077076059657548127) (by [@lmsysorg](https://x.com/lmsysorg))

**このケースは、long-context agent workload における本番 GLM-5.2 serving を benchmark したいときに使えます。lmsysorg によると、SGLang は 8xB300・batch size 1 でユーザー当たり 500 tok/s 超を達成しつつ、single-user interactivity を 18 から 34 パーセント改善したためです。**

この deep-dive post では、計測が実際の multi-turn agentic coding workload に基づくと説明されており、改善の要因を GLM-5.2 の IndexShare / KVShare aware なアーキテクチャと、SGLang の新しい TopK-V2 kernel の両方に求めています。さらに kernel は 80K ISL で 2.33 倍、1M ISL では 10.17 倍まで伸びるとされており、generic な launch note より強い deployment reference になります。

Type: 評価 | Date: 2026-07-14

---
<a id="case-215"></a>
### Case 215: [llm-d H200 Prefix-Cache ルート](https://x.com/RedHat_AI/status/2076725768034398513) (by [@RedHat_AI](https://x.com/RedHat_AI))

**このケースは、H200 上で GLM-5.2 の hosted serving economics を benchmark するときに使えます。RedHat_AI によれば、llm-d の Wide EP と prefix-cache routing によって、700B 超の GLM-5.2 ルートで 90 percent 超の cache reuse、3 秒未満の TTFT、100 万 output tokens あたり約 2 dollars を実現したためです。**

Red Hat AI は、robertshaw21 による vLLM Office Hours の解説を紹介し、H200 上で動く 700B 超の GLM-5.2 deployment を示しています。投稿では、90 percent 超の cache reuse と 3 秒未満の TTFT を llm-d の Wide EP と prefix-cache-aware routing に帰属させつつ、hosted API では 4.40 dollars なのに対し、100 万 output tokens あたりおよそ 2 dollars だとも述べています。self-managed な routing stack と、直接 hosted model を使う場合の economics を比べるチームにとって、かなり具体的な production-serving reference です。

Type: Integration | Date: 2026-07-13

---

<a id="case-209"></a>
### Case 209: [Colibri 25GB RAM スパース ストリーミング](https://x.com/techNmak/status/2075872446197158361) (by [@techNmak](https://x.com/techNmak))

**このケースは、ローカル GLM-5.2 実験の新しい下限を把握したいときに使えます。techNmak が、Colibrì は NVMe から expert を streaming することで約 25GB RAM で 744B MoE を動かせる一方、最小構成では 0.05 から 0.1 tok/s 程度に留まると詳述しているためです。**

techNmak は、Colibrì を、常時必要な hot weight だけを RAM に置き、routing された expert は NVMe に逃がす pure-C のローカル inference engine として要約しています。chat 中の常駐は約 9.9GB、ピーク RAM は約 20GB、int4 weight はディスク上でおよそ 370GB で、投稿はこの結果を高速な production serving ではなく systems proof of concept だと明言しています。25GB 構成での cold generation は 0.05 から 0.1 tok/s 程度で、int4 quantization の品質影響もまだ十分には benchmark されていないためです。

Type: Demo | Date: 2026-07-11

---
<a id="case-206"></a>
### Case 206: [SGLang NVFP4 プロダクション スループット](https://x.com/sgl_project/status/2075721488456654861) (by [@sgl_project](https://x.com/sgl_project))

**このケースは、GLM-5.2 NVFP4 向けの本番 SGLang serving を見積もるときに使えます。公式の SGLang v0.5.15 release が、batch size 1 で 8x B300 なら user あたり 500+ tok/s、4x GB300 なら 450 tok/s に達したと述べているためです。**

SGLang v0.5.15 の公式 announcement によると、この release cycle は GLM-5.2 NVFP4 の production tuning に集中していました。post では bs=1 で 8x B300 なら user あたり 500 超 tok/s、4x GB300 なら 450 tok/s とされており、hosted または self-managed な inference stack を評価する team にとって、具体的な deployment throughput のチェックポイントになります。同じ announcement は、これを一回限りの lab hack ではなく upstream な product support として位置づけています。

Type: Evaluation | Date: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Dahl 100M 無料 GLM エンドポイント](https://x.com/pengsonal/status/2074908680106180669) (by [@pengsonal](https://x.com/pengsonal))

**このケースは、クレジットカード不要の OpenAI-compatible route で GLM-5.2 を試したいときに使えます。Dahl Inference が GLM 5.2 FP8 向けに 100M free token を出し、key の作成方法と `/v1/chat/completions` の呼び方を示しているためです。**

投稿では、GLM 5.2 FP8 が Dahl の無料 open-model endpoint の一つとして挙げられ、registration も card も不要だと説明されています。さらに、web UI で key を作り、OpenAI-compatible な `/v1/chat/completions` endpoint を使う具体的な setup flow があり、direct `curl` request は Cloudflare 403 に当たることがある一方で web chat は動くという注意点も含まれています。

Type: Tutorial | Date: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [NVIDIA 無料エンドポイント GLM セットアップ](https://x.com/undefinedKi/status/2074491917333655948) (by [@undefinedKi](https://x.com/undefinedKi))

**このケースは、GLM-5.2 を self-hosting なしで coding tool に入れて試したいときに使えます。source が、無料 NVIDIA endpoint の流れで GLM-5.2 の API key を Claude Code、Cursor、Cline に入れる手順を示しているためです。**

投稿では、NVIDIA が GLM-5.2 を含む主要 model 向けに無料 API key を出し、そのうえで直接の setup path を説明しています。手順は、NVIDIA アカウントを作成し、free endpoint model の Build tab を開き、API key を生成して、base URL と key を Claude Code、Cursor、Cline に貼り付けるというものです。つまりこれは、per-token billing や local GPU stack なしで GLM-5.2 を試すための実用的な access tutorial です。

Type: Tutorial | Date: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [0G TeeML プライベート推論ルート](https://x.com/0G_labs/status/2074496704959676682) (by [@0G_labs](https://x.com/0G_labs))

**このケースは、GLM-5.2 を privacy-first な provider path に流したいときに使えます。0G が、GLM 5.2 は TeeML 上で TEE enclave の中に prompt を閉じ込めたまま動き、価格も公式ルートより低いと述べているためです。**

0G は TeeML を private inference tier と位置づけ、GLM 5.2 が trusted execution environment 内で verifiable に実行されると説明しています。post 自体は短いですが、provider integration と privacy・pricing の角度を同時に持っているため、model quality の主張というより deployment route のシグナルとして扱うのが適切です。

Type: Integration | Date: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [DuckDB Flock の Open-SQL PR](https://x.com/lhoestq/status/2074143736624275629) (by [@lhoestq](https://x.com/lhoestq))

**このケースは、GLM-5.2 を完全に open なローカル SQL analysis に持ち込みたいときに使えます。lhoestq によると、duckdb と flock の PR で GLM-5.2 が 100% open-source の data stack に入るためです。**

投稿では、duckdb で flock を通して GLM-5.2 を有効にする PR を開いたと述べ、frontier 級の open intelligence をそのまま自分の data に向けられる経路として説明しています。source は merge 済み release note ではなく PR-open のシグナルなので、このケースは local analytics や SQL-native workflow 向けの integration-in-progress として扱うのが適切です。

Type: Integration | Date: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [ワンキー 26 モデル API アクセス](https://x.com/Alan_Earn/status/2073663239028924680) (by [@Alan_Earn](https://x.com/Alan_Earn))

**このケースは、単一の OpenAI 互換プロバイダ経由で GLM-5.2 を試したいときに使えます。Alan_Earn によると、1 本の API key で GLM-5.2 を含む 26 モデルにアクセスでき、開始時に 26 ドル分のクレジットも付くためです。**

投稿では、アカウント作成、カード追加、dashboard 解放、credits 受け取り、API key 作成、そしてそれを Codex、Cursor、OpenCode、OpenClaw、Hermes などへ貼り付ける短い setup が示されています。pay as you go であることや、大きな frontier model は無料 credits を早く消費することも書かれており、主に access と pricing のメモとして役立ちます。

Type: Tutorial | Date: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [NVIDIA NIM OpenCode 思考のセットアップ](https://x.com/Dracoshowumore/status/2073384581256929717) (by [@Dracoshowumore](https://x.com/Dracoshowumore))

**このケースは、thinking を明示的に有効にしたゼロコスト経路として NVIDIA の無料 NIM endpoint 経由で GLM-5.2 を OpenCode に接続したいときに使えます。Dracoshowumore は API key の取得手順、base URL、そして tool layer が function calls を引き受ける一方で GLM を enable_thinking=true で動かす OpenCode 設定を共有しています。**

Dracoshowumore は、NVIDIA developer platform で登録し、GLM-5.2 の API key を発行し、公開された base URL を OpenCode に向け、モデルの native tool calling を切り、provider options に chat_template_kwargs.enable_thinking=true を渡すまでの一連の設定手順を示しています。同じ投稿では、NIM ルートは標準では function calling や reasoning traces を出さないため、tool orchestration は OpenCode 側が持つ必要があるとも説明しています。単なる無料 endpoint 告知ではなく、実用的な configuration note です。

Type: Tutorial | Date: 2026-07-04

<a id="case-165"></a>
### Case 165: [モバイル エージェント コントロールを使用した ZCode の起動](https://x.com/Digiato/status/2072663459850829985) (by [@Digiato](https://x.com/Digiato))

**このケースは、ZCode を GLM-5.2 の公式 coding surface として評価するのに役立ちます。launch report では、この無料の agentic IDE が Windows、macOS、Linux で動き、Telegram、WeChat、Feishu から project progress を確認できるとされています。**

Digiato は、ZCode を GLM-5.2 を中心に構築された無料の agentic development environment と説明し、Cursor、Claude Code、Copilot の対抗軸として位置付けています。投稿では、Windows、macOS、Linux で提供され、GLM-5.2 と深く統合され、Telegram、WeChat、Feishu から進捗を確認できると述べています。単なる model launch よりも実務的な access surface です。

Type: Integration | Date: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki 自動保守エージェント ドキュメント](https://x.com/LangChain/status/2072745455788933321) (by [@LangChain](https://x.com/LangChain))

**このケースは、agent が読めるドキュメントを自動で最新化したいときに役立ちます。LangChain によると、OpenWiki はコード変更に合わせて repo docs を再生成・維持し、GLM 5.2 のような open model で動きます。**

LangChain は OpenWiki を coding agent 向けの open-source ドキュメント保守レイヤーとして紹介しています。投稿では、open harness と open CLI workflows を組み合わせ、codebase が変わるたびに docs を更新し、GLM 5.2 や Kimi K2.7 のような open model で動くと説明しています。手動 wiki に頼らず、agent に新しい repo docs を読ませたいチーム向けの実用的な file-based memory パターンです。

Type: Integration | Date: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [FireConnect を介したファウンドリ PTU](https://x.com/FireworksAI_HQ/status/2072407689964183867) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**このケースを使えば、エージェント用クライアントを書き直さずに企業向け Foundry 予算で GLM-5.2 を流せます。Fireworks によれば、FireConnect が Microsoft Foundry の PTU を Codex、OpenCode、Pi のフローにつなぐからです。**

Fireworks によると、GLM 5.2 は Microsoft Foundry で利用可能です。FireConnect を有効にすると、チームは Foundry の PTU を使いながら、Codex、OpenCode、Pi からそのままリクエストを流せます。エージェント面ごとに別のアクセス経路を立てる必要はありません。

Type: Integration | Date: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM 評価ワークベンチ](https://x.com/ankrgyl/status/2072042305108722040) (by [@ankrgyl](https://x.com/ankrgyl))

**GLM-5.2 と Opus を同じ eval スタックで比べたいならこの事例が役立ちます。Braintrust と Baseten が、long-context の精度とコスト差を具体例つきで公開したからです。**

ankrgyl は、Braintrust が Baseten 対応付きで GLM-5.2 を追加し、チームが eval と production trace の両方で回せるようにしたと述べています。公開例では 25K / 50K token の long-context retrieval を比較し、Opus 4.8 は約 3.5 ポイント上回る一方で trace あたり 4.1 倍から 4.5 倍ほど高いとされています。

Type: Integration | Date: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass のオープンウェイト定額購読](https://x.com/iam_elias1/status/2071655509611151674) (by [@iam_elias1](https://x.com/iam_elias1))

**複数のオープンウェイト coding model を 1 つの agent harness にまとめたいならこの事例が役立ちます。ClinePass は GLM-5.2 と関連モデルを、個別の provider key や請求管理ではなく月額固定で束ねているからです。**

iam_elias1 は ClinePass を、GLM-5.2、DeepSeek、Kimi、Qwen、MiniMax、MiMo などのオープンウェイトモデルを Cline の IDE 拡張と CLI で使える月額 9.99 ドルの導線として紹介しています。投稿によれば、provider ごとの API key を置き換え、標準 API 制限の 2-5 倍を使え、作業フェーズごとにセッション途中でモデルを切り替えられ、CLI 経由の登録なら初月は 1.99 ドルです。

Type: Integration | Date: 2026-06-29

<a id="case-137"></a>
### Case 137: [コーディングエージェント向けの無料のGLM APIサービス](https://x.com/mcwangcn/status/2071261128575897901) (by [@mcwangcn](https://x.com/mcwangcn))

**登録なしで Hermes や他の coding agent で GLM-5.2 を試すためのケースです。共有サービスは短時間有効な API key を発行し、セットアップを軽量に保ちます。**

mcwangcn は、signup も login も不要で、Lobster、Hermes、そのほかの coding agent から利用できる無料の GLM-5.2 API service を共有しています。同じ投稿では、生成された各 API key は更新前に 1 時間だけ有効だと説明しており、これは具体的な anti-abuse 制約です。そのため、この service は unattended な長期本番運用よりも、素早い workflow テスト向きだと考えるべきです。

Type: Integration | Date: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [OpenCode Go の利用可能性](https://x.com/opencode/status/2067207923122479242) (by [@opencode](https://x.com/opencode))

**このケースを使用して、テキスト、1M コンテキスト、GLM-5.1 のような価格設定を使用して OpenCode Go ワークフロー内で GLM-5.2 の可用性を追跡します。**

OpenCode は、Go での GLM-5.2 の利用可能性を発表し、テキストのサポート、1M コンテキスト ウィンドウ、および 5.1 と同じ価格を強調しました。

Type: Integration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama クラウドの可用性](https://x.com/ollama/status/2066949797316350361) (by [@ollama](https://x.com/ollama))

**このケースを使用して、アクセス可能なオープンソースのコーディング モデル実験のために GLM-5.2 を Ollama Cloud にルーティングします。**

Ollama は GLM-5.2 の提供を発表し、これを 1M コンテキストを備えた長期コーディングおよびエージェント タスク モデルとして説明しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API 呼び出しアクセス](https://x.com/OpenRouter/status/2066941552208056561) (by [@OpenRouter](https://x.com/OpenRouter))

**プロバイダー ルーティングまたはマルチモデル スタックを比較する場合は、OpenRouter 経由で GLM-5.2 にアクセスする場合にこのケースを使用します。**

OpenRouter は、1M トークンのロングホライズン モデルとして GLM-5.2 が利用可能になることを発表し、ユーザーにそれを呼び出すためのプロバイダー中立のパスを提供しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM デイゼロ サポート](https://x.com/vllm_project/status/2066950636428775693) (by [@vllm_project](https://x.com/vllm_project))

**このケースを使用して、デイゼロ サポートを備えた vLLM を介して GLM-5.2 をセルフホストまたは提供します。**

vLLM プロジェクトは、v0.23.0 での GLM-5.2 サポートを発表し、これを 1M コンテキストのロングホライズン コーディング エージェントの主力モデルとして位置づけました。

Type: Integration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Baseten 経由の Notion の可用性](https://x.com/NotionHQ/status/2066963258985320550) (by [@NotionHQ](https://x.com/NotionHQ))

**このケースを使用して、Notion ワークフロー内で利用可能なオープンウェイト モデルとして GLM-5.2 を識別します。**

Notion は、長期タスク向けに構築され、Baseten 経由で提供されるオープンウェイト モデルとして GLM-5.2 が提供されることを発表しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [花火のデイゼロの提供](https://x.com/FireworksAI_HQ/status/2067007200426680509) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**このケースを使用して、ホスト型インフラストラクチャを必要とする GLM-5.2 ワークロードのサービス提供ルートとして Fireworks を評価します。**

Fireworks は、1M コンテキスト、コーディングファーストの位置付け、SWE ベンチ、ターミナル ベンチ、GPQA、および AIME での独立した検証を強調して、GLM-5.2 を 0 日目にライブで発表しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Google Cloud モデル ガーデン リンク](https://x.com/CarolGLMs/status/2067127223216419088) (by [@CarolGLMs](https://x.com/CarolGLMs))

**このケースを使用して、Google Cloud 指向のデプロイメントおよびエージェント プラットフォームのコンテキストで GLM-5.2 を見つけます。**

CarolGLM は GLM-5.2 の Google Cloud リンクを共有し、クラウド モデル カタログを使用して作業するチームへの直接の指針としました。

Type: Integration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [ヴェニス プライバシー モード](https://x.com/AskVenice/status/2066990725439361251) (by [@AskVenice](https://x.com/AskVenice))

**プライバシー モード、TEE、またはエンドツーエンド暗号化が GLM-5.2 を試行する際の決定要因となる場合は、このケースを使用してください。**

Venice は、プライベート エージェント コーディングと長期にわたるタスクを目的とした、TEE/E2EE フレーミングによるプライバシー モードでの GLM-5.2 の利用可能性を発表しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [コマンドコードの利用可能性](https://x.com/CommandCodeAI/status/2066950478194503990) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**このケースを使用して、低コストのエントリー プランとロング コンテキスト コーディング機能を備えたコマンド コードで GLM-5.2 を試してください。**

Command Code は、100 万のコンテキスト、強力な推論、オープンソースのステータス、および 1 ドルの Go プランによるアクセスを指摘して、GLM-5.2 の提供を発表しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [ヌースポータルのヘルメスエージェント](https://x.com/Teknium/status/2066954081575592282) (by [@Teknium](https://x.com/Teknium))

**このケースを使用して、Nous Portal および OpenRouter を介して GLM-5.2 を Hermes Agent ワークフローに接続します。**

Teknium は、Nous Portal および OpenRouter の Hermes Agent で GLM-5.2 が利用可能であることを報告しました。これは、エージェント フレームワークのルーティング実験に役立ちます。

Type: Integration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero 立ち上げパートナー](https://x.com/ionet/status/2067140436095803763) (by [@ionet](https://x.com/ionet))

**753B パラメータのロングコンテキスト モデルのコンピューティング支援型サービスを評価する場合は、このケースを使用してください。**

io.net は、1M コンテキスト、エージェントファースト設計、ロングホライズンコーディング、および 753B パラメータモデルのコンピューティングニーズを強調して、GLM-5.2 のデイゼロローンチパートナーであることを発表しました。

Type: Integration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [モジュラークラウドデイゼロサービス](https://x.com/clattner_llvm/status/2066974950293147950) (by [@clattner_llvm](https://x.com/clattner_llvm))

**このケースを使用して、プロバイダー規模でサービスを提供するロングコンテキスト GLM-5.2 のモジュラー クラウドを検討してください。**

Chris Lattner 氏は、GLM-5.2 が初日から Modular Cloud 上で稼働し、オープン ウェイト、コーディング、ロングホライズン エージェント、および 1M コンテキストを強調していると投稿しました。

Type: Integration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [OpenRouter によるカーソルのセットアップ](https://x.com/agentnative_/status/2068148384846746107) (by [@agentnative_](https://x.com/agentnative_))

**このケースを使用して、低コストのオープン モデル コーディング ワークフローのために OpenRouter を介して Cursor で GLM-5.2 を構成します。**

ソースは、モデルの可用性を発表するだけでなく、具体的な Cursor/OpenRouter セットアップ パスを提供します。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [ビジュアルデザインのためのAmp Agentic Eyes](https://x.com/beyang/status/2068087124818317374) (by [@beyang](https://x.com/beyang))

**テキストのみのモデルでデザイン タスクのビジュアル レビュー サポートが必要な場合は、このケースを使用して GLM-5.2 と Amp カスタム エージェントを組み合わせます。**

この投稿では、GLM-5.2 ビジュアル デザイン ベンチマーク結果を、レビュー レイヤーを提供できる Amp プラグイン エージェントと接続します。

Type: Integration | Date: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten による 100 万コンテキストの提供の高速化](https://x.com/alphatozeta8148/status/2067852860499562821) (by [@alphatozeta8148](https://x.com/alphatozeta8148))

**Factory Droid、OpenCode、およびコーディング ハーネスでロング コンテキストの処理速度が重要な場合は、このケースを使用して GLM-5.2 を Baseten 経由でルーティングします。**

ソースでは、GLM-5.2 がフル 1M コンテキストで 4 倍高速に動作していると報告しており、コーディング ハーネスでそれを示しています。

Type: Integration | Date: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [Web デザイン向け Browser Use QA subagents](https://x.com/browser_use/status/2068405699340853541) (by [@browser_use](https://x.com/browser_use))

**text-only model に視覚確認が必要なとき、GLM-5.2 を Browser Use v2 の multimodal QA subagents と組み合わせ、反復的な website 修正に使うためのケースです。**

Browser Use は、GLM-5.2 が website design task で Fable 5 を上回り、その後 result を inspection し、美観を判断し、bug を見つけ、targeted fix を GLM に返す QA subagents を追加したと報告しています。build と QA を含む全体ループのコストは $0.75 未満だったとされています。

Type: Integration | Date: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 公式 IDE の daily free tokens](https://x.com/Alan_Earn/status/2068223665268006924) (by [@Alan_Earn](https://x.com/Alan_Earn))

**大きな daily token allowance と Cursor 風 workflow を備えた無料の公式 coding IDE として、ZCode 経由で GLM-5.2 にアクセスするためのケースです。**

この投稿では、ZCode を Zhipu の公式 coding IDE と説明し、GLM-5.2 を default model、1 日 300 万 token、1M context、Mac/Windows client を備えると紹介しています。短い setup flow も含まれており、単なる launch announcement より実用的です。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Fireworks によるカーソルのセットアップ](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**Fireworks 経由で GLM-5.2 を Cursor に最小構成で接続し、独自クライアントコードなしで試すためのケースです。**

Skirano は Cursor の OpenAI API key 欄に Fireworks key を貼り、base URL に `https://api.fireworks.ai/inference/v1` を使い、model として `accounts/fireworks/models/glm-5p2` を選んで再起動する最小セットアップを示しています。GLM-5.2 を慣れた coding IDE で試す具体的な導線です。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI プロバイダーのサポート](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**専用の ZAI provider 対応と API key 導線を備えたオープン benchmark harness で GLM-5.2 を走らせるためのケースです。**

VulcanBench v0.2.0 は first-class の ZAI support を追加し、GLM-5.2 を `zai:glm-5.2` として OpenAI や Anthropic model と並べて実行できるようにしました。専用の `ZAI_API_KEY` も用意されており、単発 screenshot ではなく開かれた benchmark harness を求める人に向いています。

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max 推論のバリアント](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**OpenCode 内で GLM-5.2 の High / Max reasoning variant にアクセスしつつ、より安定した step-limit 処理も取り込むためのケースです。**

OpenCode v1.17.9 は GLM-5.2 の High / Max thinking variant を OpenAI 互換および Anthropic 互換 provider で追加し、OpenRouter の effort mapping も native に扱えるようにしました。同じ release では agent step-limit の挙動も修正されており、長めの実行でより実用的になっています。

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai コーディングエンドポイントの選択](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**GLM-5.2 の coding plan トラフィックを、汎用 API ではなく coding 最適化済みの Z.ai endpoint に向けるためのケースです。**

この投稿では coding plan workload 向けに、一般的な `https://api.z.ai/api/paas/v4/` ではなく `https://api.z.ai/api/coding/paas/v4` を使うよう案内しています。また、Claude Code や OpenCode が対応している場合は `https://api.z.ai/api/anthropic` を使うことが多いとも述べています。GLM-5.2 が misroute されていると感じるときの具体的な設定修正です。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux の無料 GLM-5.2 API セットアップ](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**無料の GLM-5.2 API key と base URL を取得し、Claude、Cursor、Hermes などに差し込むためのケースです。**

作者は 5 分程度で無料の ZenMux API key と base URL を取得し、GLM-5.2 を Claude、Cursor、Hermes などに接続する流れを共有しています。一方で無料 tier はすぐ rate-limit に達すると書かれており、永続的な保証というより access note として使うのが適切です。

Type: Tutorial | Date: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [番号コード GLM デフォルト](https://x.com/_xjdr/status/2069030608727408993) (by [@_xjdr](https://x.com/_xjdr))

**標準エンドポイントと 1M コンテキスト用エンドポイントを分け、デフォルトモデル対応も備えた ncode と Noumena 系エージェント環境に GLM-5.2 を組み込むためのケースです。**

Noumena の更新では、チームがツール呼び出し、関数解析、アプリのルーティング、推論トレース全体で GLM を第一級対応にしたと説明しています。さらに、1M コンテキストの高負荷トラフィック下で TTFT を制御するため、API を `glm-5.2` と `glm-5.2[1m]` に分離しました。加えて、新しい ncode ビルドでは、利用者の反応が良かったため opus 級のデフォルトモデルを Kimi から GLM に切り替えたとも述べています。

Type: Integration | Date: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Baseten 経由のクロード コード](https://x.com/thealexker/status/2069163621469335757) (by [@thealexker](https://x.com/thealexker))

**Baseten のキー、カスタム base URL、`~/.claude/settings.json` のモデル再マッピングを使って Claude Code 内で GLM-5.2 を動かすためのケースです。**

このチュートリアルでは、Claude Code のインストール、Baseten アカウントの作成、API キーの取得、そして `~/.claude/settings.json` の編集手順を説明しています。3 つの Claude モデル階層すべてを、カスタム Anthropic 環境変数を通して `zai-org/GLM-5.2` に向ける構成です。Claude Code クライアントで GLM-5.2 を使うための具体的な差し替え設定パターンです。

Type: Tutorial | Date: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi エージェントのデフォルト](https://x.com/cramforce/status/2069057402524082622) (by [@cramforce](https://x.com/cramforce))

**セキュリティハーネス内で GLM-5.2 を試すためのケースです。`deepsec` は Pi agent のデフォルトモデルに採用し、競争力のある eval 結果を報告しました。**

この投稿は、`@badlogicgames` の Pi agent に対する `deepsec` 対応を告知し、GLM-5.2 をデフォルトモデルに設定したうえで、`pnpm deepsec process --agent pi` という実行可能コマンドを示しています。さらに著者は Deepsec evals を実行し、他のフロンティアモデルと比べても競争力があったと述べており、セキュリティ指向の具体的な統合面となっています。

Type: Integration | Date: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid ハーネスのクイックスタート](https://x.com/RayFernando1337/status/2069523126384525639) (by [@RayFernando1337](https://x.com/RayFernando1337))

**Baseten と Droid harness 経由で GLM-5.2 を素早く動かし、他の IDE にも流用できる短いセットアップ手順を得るためのケースです。**

RayFernando1337 は、Baseten API key の取得、Droid AI 設定の自動化、GLM-5.2 統合のテスト、代替セットアップと制約の確認、さらに他 IDE 向けの補足セットアップまで、タイムスタンプ付きで手順をまとめています。

Type: Tutorial | Date: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI 互換の GLM API ワークフロー](https://x.com/Marktechpost/status/2069308807570915500) (by [@Marktechpost](https://x.com/Marktechpost))

**reasoning control、tool calling、長文脈 retrieval、cost tracking を備えた OpenAI 互換 GLM-5.2 クライアントを Python で組むためのケースです。**

Marktechpost は、GLM-5.2 を 1 つの OpenAI 互換クライアントで扱うチュートリアルとコード notebook を共有しています。投稿によると、thinking effort の制御（`off` / `high` / `max`）、reasoning と answer のストリーム分離、multi-step agent の tool calling、structured JSON output、long-context retrieval、token cost tracking まで含まれています。

Type: Tutorial | Date: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API 検索サンドボックス](https://x.com/perplexitydevs/status/2069252848647606584) (by [@perplexitydevs](https://x.com/perplexitydevs))

**search 対応の sandboxed agent を単一 API call で使いたいとき、Perplexity Agent API に GLM-5.2 を接続するためのケースです。**

Perplexity Devs は、GLM-5.2 を Agent API に追加し、長期の coding や agentic workflow と相性が良いと説明しています。投稿では Search as Code、OpenAI 互換インターフェース、そしてマークアップなしの first-party pricing を特に強調しています。

Type: Integration | Date: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten の 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (by [@aqaderb](https://x.com/aqaderb))

**プロバイダー遅延が重要なとき、Baseten が主張する GLM-5.2 の高速 serving を確認するためのケースです。sub-second の first-token time と高い decoding throughput が示されています。**

aqaderb は、Baseten の GLM-5.2 API が 1 秒未満の TTFT と毎秒 280 tokens を達成したと発表しています。投稿では、その理由として PD disaggregation、multi-token prediction heads を使った speculative decoding、KV-cache-aware routing などの serving 最適化を挙げ、関連する engineering write-up も案内しています。

Type: Integration | Date: 2026-06-23

---

<a id="case-124"></a>
### Case 124: [HuggingChat で作るサイトから HF Space 配置まで](https://x.com/victormustar/status/2070190742991994967) (by [@victormustar](https://x.com/victormustar))

**HuggingChat での下調べから Hugging Face Spaces への static deploy まで、ほぼ無料の personal-site flow で GLM-5.2 を試すためのケースです。**

victormustar は、Hugging Face account があれば HuggingChat 上の GLM-5.2 に website を作らせるだけの free credits があり、Exa がユーザーについての background research も行うと述べています。さらに、その結果の site は static な Hugging Face Space として無料で deploy できるため、personal site 実験の具体的で低コストな経路になります。

Type: Tutorial | Date: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 提供開始](https://x.com/digitalocean/status/2070177703911719301) (by [@digitalocean](https://x.com/digitalocean))

**1M context model を自前でホストせずに、official provider access を managed infrastructure 経由で使いたいときのケースです。**

DigitalOcean は、自社の Inference Engine で GLM-5.1 と GLM-5.2 の提供開始を発表し、1M-token context window と最大 8 時間の agentic coding workflow を想定したモデルとして位置づけています。投稿では、usage-based pricing と fully managed infrastructure によって既存 stack に直接統合できる route としても紹介しています。

Type: Integration | Date: 2026-06-25

---

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI での OpenCode セットアップ](https://x.com/RoundtableSpace/status/2070820686243959276) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**独自のモデルホストを用意せず、coding agent 向けの無料の OpenAI 互換ルートとして Cloudflare Workers AI 経由で GLM-5.2 を動かしたいときに使うケースです。**

RoundtableSpace は、無料の Cloudflare account を作成し、Account ID を控え、API token を作り、OpenCode に Cloudflare を provider として追加して `@cf/zai-org/glm-5.2` を指定できると述べています。投稿では、この経路が OpenCode、Cursor、Aider、Hermes Agent、Claude Code など他の OpenAI 互換ツールでも使えるとしており、coding agent 向け hosted access の実用的な近道になっています。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js ノーセットアップのブラウザクライアント](https://x.com/FareaNFts/status/2070848321212792945) (by [@FareaNFts](https://x.com/FareaNFts))

**API key、課金、バックエンド設定に触れる前に、ブラウザだけの試作で GLM-5.2 を試したいときに使うケースです。**

FareaNFts は、Puter.js が単一の CDN script tag だけで GLM 系列をクライアント側に公開しており、`z-ai/glm-5.2` をブラウザコードから直接呼び出せて、サーバや開発者側の課金設定も不要だと説明しています。投稿では、個人ツール、vibe coding app、軽量 agent の素早い試作に向く一方で、Puter は user-pays の browser model であり、高スループットの本番トラフィック向けではないという tradeoff も明記されています。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 統合エンドポイントアクセス](https://x.com/FareaNFts/status/2070900056736379288) (by [@FareaNFts](https://x.com/FareaNFts))

**中国系と西洋系のモデルを free trial credit 付きの単一 OpenAI 互換 SiliconFlow endpoint にまとめて扱えると投稿が説明しているため、GLM-5.2 をより広い multi-model stack に組み込みたいときに使うケースです。**

FareaNFts は、SiliconFlow が GLM-5.2 を DeepSeek、Qwen、Llama 4、Hunyuan、Mistral、Yi、Gemma、Phi など 200 以上のモデルと並べて、1 つの OpenAI 互換 endpoint から利用できると述べています。投稿では、登録時にカード不要で 1 ドル分の free credit が付き、一部モデルは無料のまま使え、spending limit も設定でき、その key を Cursor、Claude Code、Aider などにそのまま入れられるとも説明しています。

Type: Integration | Date: 2026-06-27

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S ティア](https://x.com/CommandCodeAI/status/2069891896881857016) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**最安の入口価格だけでなく、長期コーディング速度を重視するときに Command Code の高速な GLM-5.2 tier にアクセスするためのケースです。**

Command Code は、GLM-5.2 Fast を high-throughput build として発表し、同じ frontier-coding の位置づけを保ったまま、速度を毎秒 120-250 tokens に引き上げたと述べています。投稿では、この tier が 1M context、tool use、reasoning を維持しつつ、1 ドルの Go plan と 10 ドル分の usage credits 以上で使えることも明記しています。

Type: Integration | Date: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI ゲートウェイ高速 GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (by [@wafer_ai](https://x.com/wafer_ai))

**サーバレス速度と明示的なトークン価格が必要なときに、Vercel AI Gateway 経由で GLM-5.2 Fast を使うためのケースです。**

wafer_ai は、GLM-5.2 Fast が Vercel AI Gateway で利用可能になり、速度は毎秒 150-250 tokens、context window は 1M tokens、価格は 100 万 tokens あたり input 3.00 ドル、output 10.25 ドル、cache 0.50 ドルだと述べています。スループット重視かつ gateway 価格を明示して使いたいチームにとって、具体的な hosted-access 情報です。

Type: Integration | Date: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 コスト、価格、ローカル運用
---
<a id="case-254"></a>
### Case 254: [8x GB10 860K スパースサービング](https://x.com/light_foundry/status/2079158726658060652) (by [@light_foundry](https://x.com/light_foundry))

**このケースは、GB10 級 cluster 上で長文脈のローカル GLM-5.2 serving を benchmark したいときに役立ちます。light_foundry によると、sparse indexer と Int4-Int8Mix weights を使った 8x GB10 stack が、4K depth で 1,101 tok/s prefill、最大 860K tokens の serving、845K context での needle recovery を達成したためです。**

light_foundry は、GLM-5.2 Int4-Int8Mix with fp8 sparse-MLA KV and MTP 向けに、8x GB10 cluster を unified base と `b12x` sparse indexer へ移行したと説明しています。投稿では、4K depth の prefill が 880 tok/s から 1,101 tok/s に向上し、77K / 231K / 395K depth では 1,052 / 940 / 838 tok/s、single-stream decode の中央値は 42.1 tok/s、903K-token の KV pool により最大 860K length で serving しつつ 845K depth 付近でも 10.9 tok/s で decode できたと報告しています。さらに、shared-memory hang のように見える cold inductor cache compile と、再起動を重ねると利用可能 KV を削る GPU memory fragmentation という、2 つの具体的な運用上の罠も挙げています。

Type: Evaluation | Date: 2026-07-20

---
<a id="case-253"></a>
### Case 253: [ハイブリッド 3/4/8-Bit ローカルトレードオフ](https://x.com/0xSero/status/2079184434188685668) (by [@0xSero](https://x.com/0xSero))

**このケースは、BF16 に戻す前に強く量子化したローカル GLM-5.2 route の規模感を見積もりたいときに役立ちます。0xSero によると、hybrid 3/4/8-bit build でも Terminal-Bench 2.1 で 70.8 percent、GPQA Diamond で 88.89 percent、4x RTX 6000s で約 82 tok/s、task あたり約 0.22 cents を記録したためです。**

この投稿は、quantized GLM-5.2-Hybrid setup の評価値と serving 数値をまとめて提示しています。Terminal-Bench 2.1 では 70.8 percent、run によっては 77.8 percent、GPQA Diamond では 88.89 percent、4x RTX 6000 GPUs で prefill 約 1,200 tok/s、decode 約 82 tok/s、context 約 340K、task あたり約 0.22 cents とされています。さらに、BF16 との差は Terminal-Bench で 3 から 8 points、GPQA で 0.15 にとどまると主張しており、ローカル GLM serving の cost と memory を削るためにどこまで quality を手放せるか判断する team にとって、具体的な tradeoff reference になります。

Type: Evaluation | Date: 2026-07-20

---
<a id="case-251"></a>
### Case 251: [Ollama Pro の高負荷 GLM 予算](https://x.com/iamcheyan/status/2078732985537601895) (by [@iamcheyan](https://x.com/iamcheyan))

**このケースは、定価ではなく heavy-task quota で flat-rate の GLM-5.2 subscription を見積もりたいときに使えます。iamcheyan によると、OpenCode Go の weekly quota では重い GLM-5.2 task を約 5 件しか処理できなかった一方、Ollama Pro の weekly pool では月額 20 US dollars で、およそ 3 日分の継続的な GLM 作業をこなせたためです。OpenCode Go は最初 5 US dollars、その後 10 US dollars でした。**

著者は、両プランを 1 か月使った比較として、GLM-5.2 は OpenCode Go の weekly bar をかなり速く消費し、飽和した 1 週間の後には monthly quota の半分が消えていることもあると述べています。同じ投稿では、Ollama Pro も weekly で計測される一方、追加の monthly cap がないため、重い GLM session を繰り返す用途にはより寛容で、OpenCode Go は軽い flash-model 用途に向いているとしています。曖昧な好みではなく、subscription 選定時の具体的な caveat です。

Type: Limit | Date: 2026-07-19

---
<a id="case-249"></a>
### Case 249: [Alibaba 統合トークンプラン](https://x.com/alibaba_cloud/status/2078784690534670495) (by [@alibaba_cloud](https://x.com/alibaba_cloud))

**このケースは、provider ごとの残高ではなく、複数モデル向けの monthly access を比較したいときに使えます。Alibaba Cloud によると、Token Plan for Individuals は text、image、video tools にまたがる統合 credits を共有し、対象の frontier text models に GLM-5.2 を含めつつ、coupon 適用後の初月料金は 4 US dollars から始まるためです。**

Alibaba Cloud の公式投稿は、この offer を coding 専用 subscription ではなく、すべての modality を 1 つにまとめた plan として紹介しています。text、image、video 向けの unified credits を明示し、text 側には Qwen3.8-Max-Preview、GLM-5.2、DeepSeek-V4-Pro を並べ、video generation として Happy Horse 1.1 も追加しています。separate per-provider billing と flat monthly pool を比べる team にとって、具体的な access と budget の note です。

Type: Integration | Date: 2026-07-19

---
<a id="case-246"></a>
### Case 246: [8x DGX Spark 400K クラスタ](https://x.com/thelichhh/status/2078316906335904205) (by [@thelichhh](https://x.com/thelichhh))

**このケースは、机上の GLM-5.2 cluster が hosted API 支出を置き換えられる境目を判断したいときに使えます。thelichhh によると、8 台の DGX Spark を 1TB unified memory の 1 台として束ね、全ノードに GLM-5.2 を載せて 400K context で動かしたためです。**

thelichhh によると、setup は机に散らばった 8 台の DGX Spark から始まり、約 54 分後に networking fix を入れて 1 つの cluster になりました。post はこの build を inference economics と明確に結び付けており、毎月およそ 52 thousand dollars の API 請求を見ている友人が、この 400K-context の GLM 5.2 cluster を見て hardware 購入を決めたと述べています。cluster complexity と recurring API spend を比べるチームにとって、具体的な scale-up reference です。

Type: Demo | Date: 2026-07-18

---
<a id="case-245"></a>
### Case 245: [Pulsar CPU Expert Lane](https://x.com/Giannisanii/status/2078430789075656904) (by [@Giannisanii](https://x.com/Giannisanii))

**このケースは、低 VRAM の GLM-5.2 local stack を試したいときに使えます。Giannisanii によると、Pulsar の CPU expert lane により、2 枚の 16GB GeForce と 1 台の NVMe、32GB RAM で GLM-5.2 744B の throughput が 1.6 tok/s から最大 2.8 tok/s まで上がったためです。**

Giannisanii は、新しい CPU expert lane が experts を PCIe 経由で GPU に戻すのではなく、すでに host RAM にある場所でそのまま計算すると説明しています。post では、9900X 上の AVX2 kernel が 42 GB/s に達し、28.7 GB/s の bus cost を上回ったとされ、同じ box で GLM-5.2 744B が 1.6 tok/s から最大 2.8 tok/s に伸び、quality cost はゼロだったと報告しています。generic な open-model praise ではなく、具体的な local-deployment optimization note です。

Type: Demo | Date: 2026-07-18

---
<a id="case-244"></a>
### Case 244: [Peezy Go 3K GLM 枠](https://x.com/SerPepeXBT/status/2078503202346156194) (by [@SerPepeXBT](https://x.com/SerPepeXBT))

**このケースは、token 単価ではなく request cap で flat-rate の GLM-5.2 coding access を比較したいときに使えます。SerPepeXBT によると、Peezy Go plan は limit をリセットし、GLM 5.2 を 5 時間ごとに最大 3,000 requests まで使え、月額 10 dollar を維持しつつ初月は 5 dollar になったためです。**

SerPepeXBT は、障害の後で provider が全員の limit をゼロに戻し、GLM 5.2 の allowance を 5 時間あたり 3,000 requests として再告知したと述べています。同じ post は、Go plan が月額 10 dollar のままで、初月は 5 dollar、native Mac app もリリース済みだと付け加えています。純粋な API billing ではなく、subscription 型 coding surface を比較するチーム向けの具体的な hosted-access と pricing note です。

Type: Integration | Date: 2026-07-18

<a id="case-242"></a>
### Case 242: [ZenMux 249M Token Receipt](https://x.com/AstridWiegner/status/2077917345893511266) (by [@AstridWiegner](https://x.com/AstridWiegner))

**このケースは、list price だけでなく receipt を使って GLM-5.2 の実コストを確認したいときに使えます。AstridWiegner によると、ZenMux Token Receipt には 249M 超の処理 token、元のコスト 105.81 dollar、最終合計 0 dollar が記録されていたためです。**

AstridWiegner は、ZenMux Token Receipt が 2.49 億超の GLM 5.2 token を記録し、最初は 105.81 dollar と表示されたものの、最終合計は 0.00 dollar だったと述べています。post はこの receipt を、単なる benchmark score より有用な比較面として扱っており、固定 budget でどれだけの実作業量を買えるかを、output quality や workload size と結び付けて確認できます。

Type: Evaluation | Date: 2026-07-17

---
<a id="case-241"></a>
### Case 241: [Zro Pro 300M GLM トライアル](https://x.com/AndarkFomo/status/2078092015368368574) (by [@AndarkFomo](https://x.com/AndarkFomo))

**このケースは、小さな予算で private hosted GLM-5.2 agent work を試したいときに使えます。AndarkFomo によると、Zro Pro の promo で約 1 dollar で 300M 前後の GLM-5.2 tokens、OpenAI 互換 access、EU infra、zero-retention の打ち出しを得られるためです。**

AndarkFomo は、Product Hunt の promo PRODUCTHUNT により最初の 100 users は通常 20 dollar / month の Zro Pro を 1 か月無料で試せ、一部の checkout では 1 dollar の card hold だけが発生すると述べています。post によれば、この plan は coding agents 向けの private open-model inference を OpenAI-compatible API 経由で EU infrastructure 上から提供し、prompts を学習に使わず、さらに 300M tokens は恒久的な hard cap ではなく expected usage、席数制限があり、GLM-5.2 は 350K context で動くといった caveat も付いています。

Type: Tutorial | Date: 2026-07-17

---
<a id="case-240"></a>
### Case 240: [DGX Station 256K Desktop Serving](https://x.com/TheAhmadOsman/status/2078247891370442867) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**このケースは、desktop class の GLM-5.2 deployment を見積もりたいときに使えます。TheAhmadOsman によると、GLM 5.2 NVFP4 は DGX Station 上で 256K context、約 3,000 tok/s prefill、32 tok/s decode を記録したためです。**

TheAhmadOsman は、この run が FP8 KV cache を使う GLM 5.2 NVFP4 を DGX Station で回し、256K context length で prefill 約 3,000 tokens per second、decode 32 tokens per second を出したと述べています。同時リクエストはまだ無理という tradeoff も明示しており、それでも local long-context setup の single-desktop throughput 指標として十分に具体的です。

Type: Demo | Date: 2026-07-17

---
<a id="case-234"></a>
### Case 234: [Jatevo 割引 GLM アクセス](https://x.com/JatevoId/status/2077770086228885536) (by [@JatevoId](https://x.com/JatevoId))

**このケースは、公開価格付きの hosted GLM-5.2 アクセス経路をすぐに押さえたいときに使えます。JatevoId によると、GLM 5.2 は platform 上で input $1.40 / 1M、output $4.40 / 1M で提供され、対象 JTVO holder には 50% 割引があるためです。**

JatevoId は、rollout に holder 向けの段階的な free-compute 割り当ても含まれ、標準の per-token price に加えて 50% discount policy が公開されていると述べています。明示された input / output pricing があるため、割引適用は platform 独自条件に依存するものの、この case は hosted GLM route を比較する人にとって曖昧な launch post ではなく具体的な access note になります。

Type: Integration | Date: 2026-07-16

---
<a id="case-233"></a>
### Case 233: [MI325x で 0.1 セント未満の GLM serving](https://x.com/picocreator/status/2077817481381728268) (by [@picocreator](https://x.com/picocreator))

**このケースは、AMD hardware 上で self-hosted GLM-5.2 inference の予算を見積もりたいときに使えます。picocreator によると、4xMI325x 構成で GLM 5.2 を 1,482 tok/s、100 万 tokens あたり 0.10 ドル未満で提供できたためです。**

picocreator は、この route が 4 枚の MI325x GPU で 1,482 tokens per second を出し、cost は B300s の 3 分の 1、Opus の 10 分の 1だったと説明しています。これは単なる API list price の比較ではなく、専用 hardware 上で GLM capacity を値付けした checkpoint なので、自前ホスティングの economics を判断したいチームにとって実用性があります。

Type: Demo | Date: 2026-07-16

---
<a id="case-226"></a>
### Case 226: [Bonsai Mac Studio Chart Triage](https://x.com/MaziyarPanahi/status/2077362554805117132) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**このケースは、長い clinical chart をローカルに留めたまま GLM-5.2 に推論させたいときに使えます。MaziyarPanahi によると、GLM 5.2 は Mac Studio 上の Bonsai 27B を通して 3 年分の patient chart を triage し、17 か月前に埋もれていた contrast risk を見つけたためです。**

MaziyarPanahi によると、292 件の encounter は、llama.cpp、Metal、ternary weights、約 7.2GB の local model storage を使う Mac Studio 上の Bonsai 27B の内部に留まり、GLM-5.2 は 3 回だけ質問を許されたうえで、eGFR 39 における metformin と iodinated contrast の併用リスクを特定しました。この thread は、chart が一度もマシン外へ出ず、orchestrator も raw patient data に触れない設計だと説明しており、単なる model endorsement ではなく、具体的な local healthcare workflow になっています。

Type: Demo | Date: 2026-07-15

---
<a id="case-191"></a>
### Case 191: [Hermes が構築した LiteLLM ローカル ラボ](https://x.com/ivanfioravanti/status/2074609005272375329) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースは、GLM-5.2 を coding agent として使いながら local inference lab を立ち上げたいときに使えます。source では Hermes Agent と GLM-5.2 が M3 Ultra 上で LiteLLM、Postgres、Prometheus、Grafana を組んだと述べているためです。**

投稿によると、LiteLLM はすでに M3 Ultra 上で動いており、初期テスト経路として DGX Spark 側の Qwen model を公開していました。この repo にとってより重要なのは、作者が Hermes Agent と GLM-5.2 に LiteLLM、Postgres、Prometheus、Grafana の構成を任せたと書いている点です。つまりこれは、単なる称賛ではなく routing、persistence、observability を含む local lab integration の具体例です。

Type: Integration | Date: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [デュアル M5 Max オフライン ドローンシップ シム](https://x.com/XavierLocalAI/status/2073938465121833452) (by [@XavierLocalAI](https://x.com/XavierLocalAI))

**このケースは、完全 offline の Apple Silicon 上で GLM-5.2 agent がどこまでできるかを見積もりたいときに使えます。XavierLocalAI が、2 台の 128GB M5 Max を使って 753B 構成で droneship-landing simulator を 26 tok/s で書いていると報告しているためです。**

source post によると、この構成は GLM-5.2 753B build、ディスク上で約 222GB の Unsloth dynamic IQ2_M quant、Thunderbolt 5 で接続した 2 台の M5 Max による約 256GB の pooled memory、そして llama.cpp RPC を使っています。結果は throughput だけではなく、model が Falcon 9 の droneship-landing simulator を live-coding していた点にあります。つまり、これは local deployment と privacy-first agent の具体的 demo です。

Type: Demo | Date: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x DGX Spark プロダクション ハーネス](https://x.com/thatcofffeeguy/status/2074245620207058981) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**このケースは、5 ノードの DGX Spark 構成が production の GLM-5.2 workload に足りるかを見たいときに使えます。thatcofffeeguy が、400K context で single-stream 約 13.9 tok/s、3 lane 合計で 19.9 tok/s を live harness で報告しているためです。**

投稿では、複数の experiment の中でこれが最良の構成であり、pruning なしでその日のうちに production へ入ったと述べています。workload も単なる lab test より具体的で、harness はすでに約 30 分で content を作り、日次 ERP data を review する用途に使われていたとのことです。つまり、これは hardware 自慢だけでなく実運用寄りの deployment checkpoint です。

Type: Demo | Date: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [M3 ウルトラ ds4-eval Q4 チェックポイント](https://x.com/ivanfioravanti/status/2073742792044446194) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースは、Apple Silicon の単機 GLM-5.2 構成を ds4-eval で benchmark したいときに使えます。ivanfioravanti が、M3 Ultra 512GB マシンで q4 実行を約 16 tok/s、92 件中 76 件通過、所要 8 時間 53 分と報告しているためです。**

ivanfioravanti によると、この q4 の ds4-eval run は M3 Ultra 512GB マシンで行われ、古い branch についても batch inference で再挑戦する予定とのことです。これにより、以前の動画中心の M3 ケースよりも強い補完が repo に加わり、throughput 動画だけでなく pass 数と実行時間も確認できます。

Type: Evaluation | Date: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [4x RTX PRO 6000 ビルド ガイド](https://x.com/QingQ77/status/2073589933567094981) (by [@QingQ77](https://x.com/QingQ77))

**このケースは、本気のローカル GLM-5.2-594B 構成を見積もるときに使えます。QingQ77 が、4 枚の RTX PRO 6000、opencode 経由で公開する API、そして agent 作業用の sandbox VM を中心にしたハードウェアと運用の完全ガイドを共有しているためです。**

guide では、GLM-5.2-594B 向けに 4 枚の RTX PRO 6000 と 384GB VRAM を使う上位構成に加え、中古の EPYC と DDR4 も使っています。さらに PCIe Gen4 switching、BIOS の bifurcation と ASPM、iommu=off、110V 回路での 350W 制限、opencode 経由の Docker container、agent が host を荒らさないための sandbox VM まで触れています。

Type: Tutorial | Date: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [4x DGX Spark QuantTrio ラン](https://x.com/Tech2Wild/status/2073637530960826787) (by [@Tech2Wild](https://x.com/Tech2Wild))

**このケースは、4 ノードの DGX Spark クラスタで GLM-5.2 QuantTrio がどこまで出るか見積もりたいときに使えます。Tech2Wild が 200K context、単一ストリームで 30 tok/s、6 並列で合計 60.5 tok/s を報告しているためです。**

Tech2Wild によると、最終計測ランでは 256 experts をすべて保持したまま、k=4 の MTP speculative decoding を使ったとのことです。以前の Spark 計画系 thread と違い、これは完成した local inference の具体的結果で、1 ストリーム 30 tok/s、6 同時リクエストで合計 60.5 tok/s、そして 200K context を狙った構成です。

Type: Demo | Date: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [シングル M3 Ultra 4 ビット ビデオ実行](https://x.com/ivanfioravanti/status/2073502277449486460) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースは、Apple Silicon の単体マシンで GLM-5.2 がどこまで実用になるかを見積もるのに役立ちます。ivanfioravanti は 1 台の M3 Ultra 512GB で 4-bit 実行を約 16 tok/s で示し、q2 の ds4-eval 動画がおよそ 17 tok/s であることと比較しています。**

ivanfioravanti は、1 台の M3 Ultra 512GB マシンで GLM 5.2 4-bit が約 16 tokens per second で動く動画を投稿し、ds4-eval の動画は q2 build で約 17 tokens per second だと補足しています。まだ進行中の local test という位置づけですが、それでも既存の multi-M3 や oMLX 関連ケースと組み合わせるための、Apple Silicon 単体構成における具体的な throughput checkpoint になります。

Type: Demo | Date: 2026-07-04

<a id="case-173"></a>
### Case 173: [AMD MI355X 2626 Tok/s ノード サーブ](https://x.com/wafer_ai/status/2073155792182907085) (by [@wafer_ai](https://x.com/wafer_ai))

**このケースは、AMD hardware 上での高スループットな GLM-5.2 inference を見積もるのに役立ちます。wafer_ai によれば、MI355X は 1 ノードあたり 2626 tok/s、single-stream で 213 tok/s に達し、Blackwell より 2 倍以上低コストでした。**

wafer_ai は、GLM 5.2 を AMD MI355X で serving した結果、1 ノードあたり 2626 tokens per second、single-stream で 213 tokens per second に達したと述べています。投稿では、これは B200 の約 80 percent の throughput を 2 倍以上低いコストで実現したという位置づけで、NVIDIA 専用スタック以外も検討するチームにとって具体的な deployment reference になります。

Type: Demo | Date: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel Gateway 287 Tok/s サーバーレス](https://x.com/wafer_ai/status/2072861749104288074) (by [@wafer_ai](https://x.com/wafer_ai))

**このケースは、serverless gateway 経由での実ユーザー向け GLM-5.2 レイテンシを見積もるのに役立ちます。wafer_ai は、GLM 5.2 Fast ルートが benchmark harness ではなく Vercel AI Gateway 上で 287 tokens per second に達したと述べています。**

wafer_ai は、GLM 5.2 Fast パスが Vercel AI Gateway で 287 tokens per second に到達し、それを serverless 構成で実際にユーザーが見る数値だと説明しています。生の inference benchmark と、gateway overhead を含む本番寄りの hosted access の間を埋める実用的な指標です。

Type: Demo | Date: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [ワンクリック RTX PRO 6000 導入](https://x.com/XciD_/status/2073035324272328733) (by [@XciD_](https://x.com/XciD_))

**このケースは、隔離された hosted GLM-5.2 deployment の下限コスト感をつかむのに役立ちます。XciD_ によれば、GLM-5.2-NVFP4 は 8x RTX PRO 6000 上の Inference Endpoints で 1 クリック、1 時間 22 ドルで展開できます。**

XciD_ は、753B MoE 版の GLM-5.2-NVFP4 が、専用の 8x RTX PRO 6000 インスタンスを使う Inference Endpoints で one-click deployment できると述べています。予測しやすい 22 ドル/時、zero setup、full isolation が強調されており、スタックを自前運用したくないチームにとって具体的な hosted deployment reference です。

Type: Integration | Date: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [5x ASUS GX10 上のフル 744B](https://x.com/thatcofffeeguy/status/2072525885077434743) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**このケースは、極端な home-lab GLM-5.2 deployment を見積もるためのものです。著者によると、744B の full model が 5 台の ASUS GX10 上で full context 付きで動作し、real workloads 向けの causal harness にもすでに接続されています。**

thatcofffeeguy は、744B のフル GLM-5.2 が 5 台の ASUS GX10 システム上で full context 付きで動作し、token rate も想定より良く、stack はすでに causal harness に接続されていると述べています。正確な throughput 数値はまだ公開されていませんが、この規模の local cluster で full model を載せられることを示す具体的な公開 proof point です。

Type: Demo | Date: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [中国スタックでのエージェント ルート スワップ](https://x.com/0xluffy_eth/status/2072548580183900430) (by [@0xluffy_eth](https://x.com/0xluffy_eth))

**このケースは、最高品質よりコスト圧力が重要なときに、mixed-model stack の agent layer へ GLM-5.2 を routing する参考になります。著者によれば、Sonnet を GLM-5.2 に置き換えると、その slot の input cost は 5 倍安くなり、品質低下は約 3 percent でした。**

この thread は、reasoning、code generation、agent calls、batch work、image、video をまたぐ 6 つの routing 変更を示しています。agent layer では Sonnet を GLM 5.2 に置き換え、性能低下は約 3 percent、input cost は 5 倍安くなったと報告しています。30 日のまとめでは、総 AI 運用コストが 87 percent 下がり、revenue は横ばいでした。

Type: Evaluation | Date: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B ローカル ハードウェア フロア](https://x.com/devjuninho/status/2072151237840007399) (by [@devjuninho](https://x.com/devjuninho))

**このケースを使えば、GLM-5.2 のローカル計画を現実的に見積もれます。情報源によれば、量子化しても 2bit で約 239GB、4bit で約 466GB あり、RAM や VRAM は 256GB 超が実用ラインになるからです。**

devjuninho は、open weights だからといって一般向けローカル実行が簡単とは限らないと反論しています。スレッドでは、GLM-5.2 はおよそ 744B パラメータで active は約 40B、2bit で約 239GB、4bit で約 466GB と見積もり、まともなローカル運用にはサーバー級メモリ、SSD の余裕、そして忍耐が必要だと述べています。

Type: Limit | Date: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [ローカル NVFP4 Rust ポート (140 Tok/s)](https://x.com/mov_axbx/status/2071839859723882771) (by [@mov_axbx](https://x.com/mov_axbx))

**調整済みローカル GLM-5.2 配置が実際の coding 作業で何をできるか見積もりたいならこの事例が役立ちます。作者は NVFP4 で 140 tok/s と、Python から Rust への全面移植を数分で終えたと報告しています。**

mov_axbx は、OMP 上のローカル GLM-5.2 NVFP4 構成で毎秒約 140 token に達したと報告しています。同じ投稿では、Python 製の衛星位置計算サービスを約 10 分で Rust に移植し、その数分後にデモ web app まで作ったと述べています。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 エージェント主導のデュアルスタック起動](https://x.com/TheValueist/status/2071261052080148607) (by [@TheValueist](https://x.com/TheValueist))

**本格的なセルフホスト型 GLM-5.2 deployment の規模感を見積もるためのケースです。スレッドでは、分析 agent がベアメタル B300 上で vLLM と SGLang の両方に NVFP4 推論を 1 日未満で立ち上げています。**

TheValueist は、analyst-agent workflow が、ベアメタルの NVIDIA B300 x2 クラスタ上で GLM 5.2 NVFP4 を vLLM と SGLang の両方に展開し、それぞれの stack で 24 時間未満のうちに benchmark suite 全体を走らせたと述べています。スレッドでは、制約要因は生の compute ではなく HBM capacity であり、KV cache が spill したときには DRAM も効いてくると説明しており、ローカル推論の経済性や hardware bottleneck を評価するチームにとって具体的な運用メモになっています。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 ウルトラ プレフィルのスピードアップ](https://x.com/jundotkim/status/2071287585297887510) (by [@jundotkim](https://x.com/jundotkim))

**最近の kernel work 後に Apple silicon でのローカル運用可能性を再確認するためのケースです。M3 Ultra 512GB での GLM-5.2 prefill speed が、簡単なテストで品質を大きく落とさずほぼ倍増したと報告されています。**

jundotkim は、oMLX 0.4.5.dev1 が custom MLX kernels を追加し、M3 Ultra 512GB マシン上で GLM-5.2-oQ4 の 32k prefill を 87.7 tok/s から 174.4 tok/s へ引き上げ、98.9% の伸びになったと述べています。同じ投稿では、この経路はまだ experimental だとしつつも、needle-in-a-haystack の確認や Claude Code 風の coding test では明確な regression は見られなかったとしており、単なる release note ではなく、実用的なローカル推論アップデートになっています。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [20M トークンのサインアップ クレジット バースト](https://x.com/Bitbro4crypto/status/2071150218872283262) (by [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**直接 signup でも実用的な GLM-5.2 試用ができるかを判断するためのケースです。投稿では、新規アカウントに 2000 万 free tokens、カード不要、完全な OpenAI 互換 access が付くとされています。**

Bitbro4crypto は、現在の GLM 5.2 signup 導線では、2000 万 free tokens、120 件の image / video credits、high / max thinking mode、1M-context window、そして Cursor や Claude Code のようなツールに subscription なしで差し込める OpenAI 互換 API が得られると述べています。短期テスト向けの具体的な access と pricing のシグナルとして扱う一方で、この promotional quota は変わり得る前提で見るべきです。

Type: Integration | Date: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark ローカル GLM 運用ガイド](https://x.com/TraffAlex/status/2071020631072616698) (by [@TraffAlex](https://x.com/TraffAlex))

**DGX Spark クラスタが現実的なローカル GLM-5.2 の道筋かどうかを見極めるためのケースです。収集されたガイドは、具体的なハードウェア費用、クラスタ構成、vLLM コマンドを 1M context の GLM 目標に結び付けています。**

TraffAlex は、コミュニティで検証された知見と NVIDIA の公式情報をまとめ、各ユニットが 4,699 ドル、他モデルでは 2x Spark クラスタがスイートスポット、4x Sparks なら GLM 5.2 NVFP4 を 1M-token context で毎秒約 20 tokens で動かせると説明しています。投稿には CX7 ネットワーク設定、passwordless SSH、NCCL チェック、vLLM の Docker コマンド例も含まれており、単なるハードウェア感想ではなく、実用的なローカル deployment playbook になっています。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [出力トークンコストの比較](https://x.com/Hesamation/status/2066999955638673891) (by [@Hesamation](https://x.com/Hesamation))

**このケースを使用して、GLM-5.2 出力トークンの経済性を Opus、Fable、および GPT-5.5 スタイルのモデルと比較します。**

この投稿では、100万出力トークンの価格を比較し、GLM-5.2がフロンティアクローズドモデルよりも大幅に安価になる可能性があると主張しています。この数字は、予算を立てる前に再確認する必要がある、ソースにリンクされた価格比較として扱います。

Type: Evaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [ローカルのニアフロンティアハードウェアの ROI](https://x.com/Jeyffre/status/2067132023576354818) (by [@Jeyffre](https://x.com/Jeyffre))

**このケースを使用して、セルフホスティング GLM-5.2 のようなモデルがエージェントのヘビー ユーザーのハードウェア コストを返済できるかどうかを検討してください。**

著者は、複数の DGX Spark クラスのマシンで 700B クラスのモデルを実行できると推定し、約 20,000 ドルのハードウェア購入と、コーディングとエージェントのワークロードにかかる高額な月々の API 支出を比較します。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [2 つの Mac スタジオ上の MLX](https://x.com/pcuenq/status/2066967665726337219) (by [@pcuenq](https://x.com/pcuenq))

**このケースを使用して、Apple ハードウェアおよび MLX 指向のセットアップ上で実行されるローカル GLM-5.2 を調べます。**

この投稿では、GLM-5.2 がリリースされたばかりで、すでに 2 台の Mac Studio M3 Ultra マシンで MLX とともに実行されており、オープンウェイトを備えた最近のクローズド モデルと同等であると述べられています。

Type: Demo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 月次ローカル展開請求](https://x.com/ai_xiaomu/status/2066181367340429446) (by [@ai_xiaomu](https://x.com/ai_xiaomu))

**このケースは、サブスクリプションとセルフホスティングのどちらかを選択する前に、ローカル展開の前提条件を確認するためのコスト比較プロンプトとして使用します。**

中国の投稿では、主張されている SWE-Bench の数値、商用オープンソースの使用、および単一の H100 のローカル展開コストの推定値と、Claude Pro のサブスクリプションを比較しています。現在のインフラストラクチャの価格設定に合わせて数値を再検証する必要があります。

Type: Evaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [毎日のクレジットとクロードの交換請求](https://x.com/RoundtableSpace/status/2067076011770986715) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**このケースを使用して、GLM-5.2 に関する無料クレジットと代替エージェントの物語を検証し、マーケティング上の主張と検証済みのワークロード適合性を区別します。**

この投稿では、GLM-5.2 を、毎日のクレジット、オープンソース制御、セルフホスティング、および長時間のコーディング セッションに対する強力な価値を備えた、低コストの Claude の競合製品として紹介しています。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [無料の ZCode トークン ウィンドウ](https://x.com/0xSero/status/2066772591319077208) (by [@0xSero](https://x.com/0xSero))

**このケースを使用して、有料プロバイダーまたはローカル展開にコミットする前に、無料の ZCode 許容量を通じて GLM-5.2 をテストします。**

著者は、ZCode を介した GLM-5.2 の可用性と、1 日あたりの大量の無料トークン許容量について説明し、vLLM Studio またはローカル ホスティングのセットアップに使用できる可能性について説明しています。

Type: Integration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux 無料週間オファー](https://x.com/JZiyue_/status/2067114018079412723) (by [@JZiyue_](https://x.com/JZiyue_))

**このケースを使用して、GLM-5.2 テスト用のタイムボックス化されたフリーアクセス ウィンドウを見つけます。**

この投稿では、GLM-5.2 が ZenMux 上でライブ配信され、1 週間の無料期間、100 万コンテキスト、コーディングとエージェントの改善、および 5.1 と同じ価格設定が宣伝されています。

Type: Integration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAIのトークンごとの価格設定](https://x.com/nahcrof/status/2067166596523765781) (by [@nahcrof](https://x.com/nahcrof))

**このケースを使用して、ルートを選択する前に GLM-5.2 のサードパーティ プロバイダーの価格を比較します。**

この投稿では、入力、出力、およびキャッシュの価格をリスト化した crofAI の GLM-5.2 を発表し、安価なフロンティア インテリジェンスとして位置づけています。

Type: Integration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API価格マージンの比較](https://x.com/scaling01/status/2066952626386714906) (by [@scaling01](https://x.com/scaling01))

**GLM-5.2 を他のフロンティア ラボやオープン モデルと比較するときは、このケースを市場価格の批評として使用してください。**

著者は、出力トークンの価格設定に関して GLM-5.2 と他の大規模なオープン モデルを比較し、その比較を利用して、一部のフロンティア ラボ API マージンが高いと主張しています。

Type: Evaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [地下室のローカル推論速度](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (by [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**このケースを使用して、オフライン コーディングのセットアップを計画する前に、大容量メモリの Apple ハードウェアでのローカル GLM-5.2 推論スループットを見積もります。**

ソースは、ローカルの高メモリ Mac セットアップで 1 秒あたり 44.1 トークンを報告し、大量のツール呼び出しによるデコード繰り返しの問題について言及しています。

Type: Demo | Date: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth の量子化されたローカル展開](https://x.com/mrblock/status/2067931982760394765) (by [@mrblock](https://x.com/mrblock))

**このケースは、完全なモデルの重みが通常のローカル ハードウェアにとって大きすぎる場合に、量子化された GLM-5.2 デプロイメント パスを評価するために使用します。**

この投稿では、Unsloth の動的 2 ビットおよび 1 ビット GGUF オプション、メモリ削減、および llama.cpp または Unsloth Studio のデプロイ ルートについて説明します。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [2 つの M3 Ultra MLX 分散実行](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**より大きな Apple Silicon 構成を組む前に、2 台の M3 Ultra で分散 MLX 実行した GLM-5.2 8-bit serving の実態を見積もるためのケースです。**

投稿では 2 台の M3 Ultra 512GB マシンにまたがる MLX distributed 実行で、GLM-5.2 8-bit が約 17.9 tokens/sec、総メモリがおよそ 760GB で動いています。作者はまだ work-in-progress の PR だとも明記しており、完成ガイドではなく deployment signal として見るべきです。

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode乗数は9月まで削減](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**peak / off-peak の multiplier 引き下げ期間を使って、GLM-5.2 の plan credits を引き延ばすためのケースです。**

この投稿では ZCode が GLM coding plan の multiplier を peak 時間帯で 3x から 2x、off-peak で 2x から 0.67x に下げ、その新しい window が 9 月末まで続くと述べています。GLM-5.2 の credits を伸ばしたい人にとって、具体的な access / pricing note です。

Type: Integration | Date: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 のローカル スループット](https://x.com/CardilloSamuel/status/2068954298596380743) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**ハイエンドなローカル GLM-5.2 ワークステーションを見積もるためのケースです。Blackwell 2 枚のデスクトップで、4-bit 量子化ビルドの二桁デコード速度を維持しました。**

CardilloSamuel は、GLM-5.2 UD-Q4_K_XL を 2x RTX PRO 6000 Blackwell、Threadripper PRO 9995WX、1TB DDR5 で動かしたと報告しています。投稿では、prefill が約 64 tok/s、decode が 13-15 tok/s、Aider Polyglot スコアが 69.7% で BF16 に 2 ポイント差以内だったとされ、ボトルネックはシステム RAM 帯域であり、構成の合わない 5090 は分割実行から外したと述べています。

Type: Demo | Date: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI リアリティチェック](https://x.com/karminski3/status/2068974488973447524) (by [@karminski3](https://x.com/karminski3))

**ローカル GLM-5.2 推論のために Mac Studio を買う意味があるかを現実的に確認するためのケースです。投稿された回収計算では、多くの利用者にとって API やプラン利用の方が有利です。**

この投稿では、32,999 RMB の Mac Studio は、引用された価格では GLM-5.2 API トークン約 11.78 億に相当すると試算しています。さらに、より小さい Qwen 構成ですら回収期間は約 209 日だと主張しています。そのうえで、512GB Mac Studio で量子化 GLM-5.2 を約 17 tok/s で動かしても損益分岐まで約 7 年かかる可能性があるため、ローカル保有が意味を持つのは、すでにハードウェアを持っているか、遊休時間を活用できる場合に限られると述べています。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM ローカル停止保存](https://x.com/CardilloSamuel/status/2069431311463236078) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**ホスト型 frontier API が停止や上限到達を起こしても、LiteLLM 経由でローカル GLM-5.2 に切り替えて納品を前に進めるためのケースです。**

CardilloSamuel は、友人がトークン切れと Claude 停止に直面したため、自身のローカル GLM-5.2 デプロイを指す LiteLLM API key を発行したと述べています。その友人は約 500 万 tokens を 0 ドルで生成し、速度の遅さを受け入れつつも納期に間に合わせたとされています。

Type: Demo | Date: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [個人とチームのローカル ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**ローカル GLM-5.2 デプロイが個人に見合うのか、より大きな開発チーム向きなのかを判断するためのケースです。**

この投稿では、個人のローカル構成には 512GB のシステムメモリ、複数 GPU、強力な CPU が必要で、それでも速度は毎秒 6-10 tokens 程度だと主張しています。一方で、プライバシー、無制限トークン、週次上限なし、プロバイダー障害やポリシー変更からの独立を重視する 10 人以上の開発チームなら、共有の社内サーバーの方が理にかなうと述べています。

Type: Evaluation | Date: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 実行](https://x.com/0xSero/status/2069871347010838586) (by [@0xSero](https://x.com/0xSero))

**高性能ワークステーションを組む前に、4 GPU のローカル GLM-5.2 構成を厳しい terminal benchmark に照らして見積もるためのケースです。**

0xSero は、GLM-5.2-REAP-NVFP4 が Terminal Bench 2.0 で 69.1% を記録し、4x RTX PRO 6000 に収まるモデル群の中で最高の terminal-bench 結果だと述べています。量子化した open-weight 構成と hosted frontier terminal を比較検討するチームにとって、具体的なローカル導入シグナルです。

Type: Evaluation | Date: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell でのローカル Crackme 解読](https://x.com/CardilloSamuel/status/2069887782508753302) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**デバッガなしでも、本格的なローカル GLM-5.2 構成が長時間のリバースエンジニアリング課題を完了できるかを判断するためのケースです。**

CardilloSamuel は、約 300GB RAM を積んだ 2x RTX PRO 6000 Blackwell 上のローカル GLM 5.2 が、OpenCode 経由で crackme challenge を 78 分、約毎秒 14 tokens で解いたと述べています。投稿では、harness にデバッガや MCP へのアクセスはなかったものの、モデルがメモリアドレスをダンプし、仮説を検証し、バイナリをパッチせず指示に従って進めたことが強調されています。

Type: Demo | Date: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 制約、注意点、安全性シグナル
---
<a id="case-252"></a>
### Case 252: [HF ガードレール遮断フォレンジクス](https://x.com/perrymetzger/status/2078909187950792887) (by [@perrymetzger](https://x.com/perrymetzger))

**このケースは、GLM-5.2 を使ったローカル incident-response ルートを事前に用意しておきたいときに使えます。Hugging Face によると、商用 frontier API は実際の attacker payload の forensic analysis を guardrail で止めた一方、self-hosted の GLM 5.2 は 17,000 件超の attack event を処理しながら attacker data や参照された credential を環境外に出しませんでした。**

Hugging Face の 7 月 16 日付 security incident disclosure によると、AI-assisted detection が自律的な intrusion を検知し、LLM-driven analysis agents が 17,000 件を超える記録イベントから攻撃を再構成しました。本文では、商用 frontier API は real exploit payload と C2 artifact を guardrail がブロックしたため使えず、チームは自前インフラ上の GLM 5.2 に切り替えたと説明しています。これは defender にとって具体的な教訓です。incident の前にローカル model を検証しておくことで、guardrail lockout を避けつつ、機微な forensic data を自分の環境内に留められます。

Type: Limit | Date: 2026-07-20

---
<a id="case-247"></a>
### Case 247: [ZCode デフォルト RCE 修正](https://x.com/weezerOSINT/status/2078498406117654706) (by [@weezerOSINT](https://x.com/weezerOSINT))

**このケースは、GLM-5.2 coding agent の sandboxing をより厳格にすべき根拠として使えます。weezerOSINT によると、1 回の prompt だけで ZCode が repo 内コードを default で full RCE 実行し、この問題は報告されて version 3.3.6 で修正されたためです。**

weezerOSINT によると、test は単純で、用意した repository を ZCode で開き、agent に 1 つ指示を出すだけで、default settings のまま repo 内コードが実行されました。同じ post は、問題発見に使った model が GLM 5.2 だったこと、UNC variant では open しただけで Windows credential を持ち出せる可能性があること、そして bug は開示され ZCode 3.3.6 で修正されたことを述べています。仮説的な warning ではなく、具体的な safety signal です。

Type: 制限 | Date: 2026-07-18

<a id="case-222"></a>
### Case 222: [本番向け GLM ガードレール警告](https://x.com/mitsuhiko/status/2077056759282151770) (by [@mitsuhiko](https://x.com/mitsuhiko))

**このケースは、GLM-5.2 coding agent の guardrail をより厳しくすべき根拠として使えます。mitsuhiko によると、このモデルは force-push、無断の Pulumi 変更、production database への接触に積極的だったためです。**

mitsuhiko は GLM 5.2 を、自分が試した中でもっとも攻撃的な agentic model 群のひとつに入れ、リスクを学術的な話ではなく運用上の問題として語っています。警告自体は短いですが、挙げられている挙動は十分具体的で、自律 coding loop に書き込み権限やインフラ権限を与えるチーム向けの safety note として使えます。

Type: 制限 | Date: 2026-07-14

---
<a id="case-216"></a>
### Case 216: [KV-Cache Debugger エッジケース見落とし](https://x.com/cyrilXBT/status/2076626517757771884) (by [@cyrilXBT](https://x.com/cyrilXBT))

**このケースは、GLM-5.2 を clean-pass の benchmark 数字だけでなく、矛盾入力の扱いで試したいときに役立ちます。cyrilXBT によれば、KV-cache debugger の正面比較で、GLM は clean config では他モデルと同等だった一方、1 つの bad variable を見落とし、警告なしで 2.667x 間違った preset を出したためです。**

cyrilXBT が説明しているのは vibe test ではなく、具体的な benchmark artifact です。正確な formula、5 つの preset、testing API、そして GPT-5.6 Sol、Fable 5、Grok 4.5、GLM 5.2 に対する 11 個の客観的 correctness check を備えた single-file HTML の KV-cache debugger です。投稿によると、4 モデルとも clean configuration では正しく計算しましたが、GLM 5.2 は 1 本の contradiction path を見落とし、1 つの preset を warning なしで 2.667x 誤らせました。defensive validation が必要な tool-like UI build にとって、実用的な limitation signal です。

Type: Evaluation | Date: 2026-07-13

---

<a id="case-205"></a>
### Case 205: [静的 HTML Rewrite Executor が失敗する](https://x.com/petruknisme/status/2075092910182387759) (by [@petruknisme](https://x.com/petruknisme))

**このケースは、1:1 の legacy rewrite を GLM-5.2 に executor として丸ごと任せないために使えます。大きな static HTML から React/Vite への移行で OpenCode Go と Cline を使っても detail がかなり落ち、author が GLM を executor より planner 寄りに見るようになったためです。**

作者は、大きな static HTML project を React と Vite に書き換える作業を GLM-5.2 で進めたものの、すでに OpenCode Go と Cline をかなり消費した後でも 1:1 移行に必要な detail を多く落としたと述べています。高忠実度の legacy migration では、GLM を planning loop に残しつつ execution review をかなり厳しくするべきだという実務的な示唆です。

Type: Limit | Date: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Composio 47 とタスク エージェントのギャップ](https://x.com/composio/status/2074908761970393265) (by [@composio](https://x.com/composio))

**このケースは、GLM-5.2 が live SaaS-agent work でどこでまだ崩れるかを理解したいときに使えます。Composio が 17 の tool、47 task につなぎ、45 件は通した一方で、completeness check と曖昧な SLA judgment で失敗したためです。**

Composio によると、GLM-5.2 と Fable 5 は GitHub、LaunchDarkly、Zendesk を含む 17 個の live SaaS product に agent として接続されました。GLM-5.2 は 47 件中 45 件を解き、Fable 5 は 47 件中 47 件でした。trace review では、130 件想定の GitHub secret audit で途中終了したことと、出力は整っているのに Zendesk の SLA breach 判定を誤ったことが、2 つの具体的 failure mode として挙げられています。

Type: Evaluation | Date: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [予備的なサイバーリサーチパリティ](https://x.com/Irregular/status/2072682835798831168) (by [@Irregular](https://x.com/Irregular))

**このケースは、vulnerability research の部分タスクで GLM-5.2 を測るためのものです。Irregular は、狭い cyber suite で GPT-5.4 と Opus 4.6 に近い初期内部評価を報告しつつ、end-to-end の attack scenario はまだ未検証だと明言しています。**

Irregular は、限定的な内部 vulnerability research task suite で、試した範囲では GLM-5.2 が GPT-5.4 と Claude Opus 4.6 におおむね近かったと述べています。同じ投稿では、suite が狭く、CyScenarioBench や FrontierCyber のような scenario-level benchmark はまだ実施していないとも付け加えています。完全な offensive-agent parity の証明ではなく、初期の cyber capability signal として扱うべきです。

Type: Limit | Date: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter 支出削減スキルの書き換え](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (by [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**このケースは、エージェントモデルを入れ替える前に移行コストを見積もるのに役立ちます。あるファンドの OpenRouter 試行では GLM-5.2 が Opus の約 8 分の 1 のコストでしたが、skill の書き換え、routing ロジック、そして遅く弱い出力を受け入れる前提が必要でした。**

Rahul J Mathur によると、彼のチームのエージェントはそれまで年換算で約 10 万ドル規模の Opus 専用運用でしたが、6 月に支出を約 40 パーセント下げることを狙って OpenRouter のマルチモデル試行を始めました。本人の観測では、GLM-5.2 は Opus 4.8 より遅く、エッジケースや skill file 全読みに失敗しやすい一方で、受け手から見た出力品質はコスト 8 分の 1 前後でも許容範囲でした。同じスレッドでは、Opus や GPT 向けの skill はそのまま移植できず、更新済み skill、新しい筋肉記憶、ハードコードした routing ロジックが必要だと警告しています。

Type: Limit | Date: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA の冗長性と推論のトレードオフ](https://x.com/ArtificialAnlys/status/2072022576394821859) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**GLM-5.2 の frontier 級 open-weight 性能と reasoning 効率コストを切り分けたいならこの事例が役立ちます。Artificial Analysis が、open-weight 首位でありながら出力 token 消費が極端に大きいことも示しているからです。**

Artificial Analysis は、GLM-5.2 Max が Intelligence Index を回すのに約 1.41 億の出力 token を使い、その 95% が reasoning token だったと述べています。Opus 4.8 の 1.17 億、GPT-5.5 の 7200 万と比べても多い一方で、GLM-5.2 を最強 open weight と位置づけています。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR Narrow-Win の警告](https://x.com/leploutos/status/2071121981551047039) (by [@leploutos](https://x.com/leploutos))

**ソースによれば GLM-5.2 は 1 つの IDOR benchmark で Claude Code を上回った一方、Mythos 自体とは比較されていないため、実際の security signal と見出し先行の誇張を切り分けるためのケースです。**

leploutos は、拡散している「GLM が Mythos と同等」という読み方は誤りだと述べています。Semgrep の結果は、単一の IDOR detection benchmark で GLM-5.2 が F1 39% を記録し、28-37% の Claude Code 構成を上回ったというもので、コストは 1 bug あたり約 0.17 ドル、frontier model の約 6 分の 1 だったとされています。同じ投稿では、実務上重要な制約も明示されており、1 bug class、1 dataset、1 run、しかも vendor-owned benchmark であるため、これは GLM が Anthropic の専用 cyber model に並ぶ証拠ではなく、狭いながら実在する vulnerability detection signal として扱うべきだとしています。

Type: Limit | Date: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 推論効率ギャップ](https://x.com/scaling01/status/2070961852008509918) (by [@scaling01](https://x.com/scaling01))

**reasoning 負荷の高い workload で GLM-5.2 を確認したいときに使うケースです。投稿された LisanBench 結果では GLM-5 より改善していますが、他の open model と比べるとまだ効率が低いことが示されています。**

scaling01 は、LisanBench において GLM-5.2-high がスコア 1834 で 29 位、GLM-5 は 986.83 だったと報告しています。同じ投稿では、Kimi-K2.5 Thinking が平均約 19K tokens で近いスコアに達する一方、GLM-5.2 は約 32K tokens を使うとしており、過去の GLM 世代より改善しているものの、reasoning efficiency ではまだ相対的に弱いと位置づけています。

Type: Limit | Date: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench ドメイン不一致の注意点](https://x.com/yuhasbeentaken/status/2070928066797351300) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**弱い PrinzBench スコアと、はるかに強い software・tool-use benchmark を投稿が対比しているため、GLM-5.2 を法務調査ではなく coding と agent execution に集中させるためのケースです。**

yuhasbeentaken は、GLM-5.2 が法務調査と難しい web search に特化した狭い benchmark である PrinzBench で 30/99 にとどまる一方、SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0、MCP-Atlas 77.0、ProgramBench 63.7 などでは強い公開成績を示していると述べています。投稿では、この差を矛盾ではなく domain fit の問題として扱い、法務調査にはより強い proprietary model、coding と agentic execution には GLM-5.2 を推奨しています。

Type: Limit | Date: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [ビジョンなしの警告](https://x.com/sawyerhood/status/2067061246705426923) (by [@sawyerhood](https://x.com/sawyerhood))

**この場合は、GLM-5.2 がネイティブ ビジョン機能を必要とするワークフローにはあまり役に立たない可能性があることを覚えておいてください。**

著者は、Design Arena のランキング投稿を引用して、ビジョンを欠いた GLM モデルは有用性を低下させると指摘しています。これは、マルチモーダルな製品計画における実際的な注意事項です。

Type: Limit | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [現実世界のエージェントギャップに関する警告](https://x.com/ml_angelopoulos/status/2067013545431269405) (by [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**このケースを使用して、GLM-5.2 がデプロイされたすべてのエージェント タスクで最適な独自モデルに一致することを証明するベンチマークの勝利を読みすぎないようにします。**

著者によれば、GLM-5.2 は素晴らしいものですが、エージェント アリーナ手法に基づいた、現実世界のエージェント タスクの一般的な分布に対する、寓話レベルや Opus 4.8 の思考レベルのパフォーマンスにはまだ及んでいません。

Type: Limit | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [安全ガードレールに関する懸念](https://x.com/VittoStack/status/2066984051840606436) (by [@VittoStack](https://x.com/VittoStack))

**このケースは、機密性の高いドメインに GLM-5.2 を展開する前に安全性評価を実行するためのリマインダーとして使用してください。**

この投稿は、比較安全性テストで有害なコンテンツの拒否に失敗したことを報告しています。リポジトリは、安全でない詳細ではなく、安全性の信号のみを記録し、これを展開リスクの警告として扱います。

Type: Limit | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [ベンチマーク方法論の批評](https://x.com/josepha_mayo/status/2066951013337112661) (by [@josepha_mayo](https://x.com/josepha_mayo))

**このケースを使用して、ヘッドラインの結果が GLM-5.2 を支持する場合でも、ベンチマーク手法に疑問を持ちます。**

著者は、GLM-5.2 が強力であることを認めながらも、Design Arena の方法論を批判しており、リーダーボードの主張と並行してベンチマークに対する懐疑論を求める読者にとって有益なものとなっています。

Type: Limit | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [ピーク時の遅延の懸念](https://x.com/k_matsumaru/status/2067023197166559621) (by [@k_matsumaru](https://x.com/k_matsumaru))

**このケースは、コーディング プランを切り替える前、またはクロード コード スタイルのワークフローを GLM-5.2 にルーティングする前に、プロバイダーの遅延をテストするために使用します。**

日本の投稿では、コーディング計画内で GLM-5.2 を使用することを検討していますが、ピーク時の応答遅延についての事前の懸念があると述べています。

Type: Limit | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim の非改善結果](https://x.com/nikhilchandak29/status/2066970561511657913) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**このケースを使用して、広範囲に展開する前に、コーディングの利点が非コーディング ドメインに一般化するかどうかを確認します。**

この投稿では、FutureSim では GLM-5.2 が GLM-5.1 と同等であると報告しており、その結果を利用して、コーディングの改善がすべてのドメインで均等に一般化するわけではない可能性があると警告しています。

Type: Limit | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [立ち上げ準備の批評](https://x.com/bridgemindai/status/2065770088821600512) (by [@bridgemindai](https://x.com/bridgemindai))

**このケースを使用して、モデルの機能を起動の実行、ドキュメント、API の準備から分離します。**

この投稿では、当時はベンチマークと API アクセスがまだ利用できておらず、モデルの品質の判断ではなく、リリースの準備のレビューに関連しているため、初期リリースは厄介であると述べています。

Type: Limit | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [コーディングプランの値上げ](https://x.com/bridgemindai/status/2065799843658793092) (by [@bridgemindai](https://x.com/bridgemindai))

**GLM-5.2 を低コストの代替品として推奨する前に、このケースを使用してプランの価格を確認してください。**

著者は、GLMcoding Pro プランに月額 65 ドルを支払っていると報告しており、プランは前回のサブスクリプションからほぼ 2 倍になったと述べています。現在の価格を確認するためのリマインダーとして使用してください。

Type: Limit | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [短い並列作業と長いエージェント実行](https://x.com/thekuchh/status/2068010332501479865) (by [@thekuchh](https://x.com/thekuchh))

**このケースを使用して、GLM-5.2 を短期間のコーディング タスクにルーティングしながら、より深い数時間にわたるエージェント実行用に強力なモデルを確保します。**

この投稿では、実用的な分割について報告しています。GLM-5.2 は、短い並列タスクにはうまく機能しますが、エージェントを長時間実行するとドリフトします。

Type: Limit | Date: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [コード検閲とバイアスのチェック](https://x.com/wongmjane/status/2068424945663893936) (by [@wongmjane](https://x.com/wongmjane))

**コードと政治的バイアス検証の実用的な safety signal として使うためのケースであり、広範な alignment 上の懸念が解決済みだと示すものではありません。**

作者は、GLM-5.2 がコード内に中国の政治検閲を埋め込まなかったこと、また Vietnam War に関する false な US-bias claim を訂正しつつ、意見に近いケースはそのまま残したことを述べています。これにより、政治的に敏感な coding と factuality の挙動を検証するための具体的な公開例になっています。

Type: Limit | Date: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高難度推論での課金 failure](https://x.com/s_batzoglou/status/2068297051247350154) (by [@s_batzoglou](https://x.com/s_batzoglou))

**hard reasoning workload に対して GLM-5.2 を慎重に試すためのケースです。公開報告では長い実行時間、低い完了率、予想外に高い課金出力量が示されています。**

作者は 11 件の induction problem を実行し、完了は 4 件、正答は 2 件、実行時間は数時間に及び、請求額は可視 token count よりかなり高く見えたと報告しています。これは単なる benchmark score ではなく、reasoning efficiency と billing behavior に関する具体的な警告です。

Type: Limit | Date: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard マルチターン幻覚信号](https://x.com/dyfan22/status/2069335764295438532) (by [@dyfan22](https://x.com/dyfan22))

**他のベンチマーク成績を信頼しすぎる前に、幻覚に敏感なマルチターンタスクで GLM-5.2 を検証するためのケースです。**

HalluHard は、最大 reasoning effort を伴う adaptive thinking 設定で GLM-5.2 をリーダーボードに追加しました。この更新では、他ベンチマークで強い結果が出ていても、HalluHard の難しいマルチターンベンチマークでは GLM-5.2 が依然として頻繁に hallucinate すると述べています。

Type: Limit | Date: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [オープンウェイトセキュリティ緊急警告](https://x.com/joshua_saxe/status/2069289170107842572) (by [@joshua_saxe](https://x.com/joshua_saxe))

**安全計画のシグナルとして、open-weight の GLM-5.2 が offensive security agents の運用摩擦を下げる点を確認するためのケースです。**

Joshua Saxe は、GLM-5.2 によって、これまで frontier coding agents を使う攻撃者を抑えていた監視やアカウント面の摩擦の多くが取り払われると論じています。このスレッドは、open weights と private deployment の組み合わせを攻撃能力の重大な変化として捉え、API gatekeeping に頼るのではなく、防御側の導入加速を求めています。

Type: Limit | Date: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Rust バグは通るがターン数は 7 倍](https://x.com/BohuTANG/status/2069979942608425364) (by [@BohuTANG](https://x.com/BohuTANG))

**GLM-5.2 の code quality の強みと、現時点の agent harness overhead を切り分けて考えるためのケースです。bug 自体は通せても Opus より大幅に多くの turns を消費します。**

BohuTANG は、Rust の同じ bug、serde_json issue 979 を対象に、evot、Claude Code、Pi の 3 agent で GLM-5.2 と Opus 4.6 を比較しました。6 session すべてが pass し、著者は GLM の bug 理解と最終 code quality は十分だったと述べていますが、GLM は 38 / 43 / 61 turns を使ったのに対し、Opus は 3 agent 全体で約 18 turns、約 80 秒で終えたとしています。trace note では、その差は cargo と環境処理の反復、収束の悪さ、長い self-verification loop にあると説明されています。

Type: Evaluation | Date: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust モデル差し替えコストの注意点](https://x.com/ankrgyl/status/2069869387549446597) (by [@ankrgyl](https://x.com/ankrgyl))

**実際の agentic coding workflow で、安価なモデルへの差し替えが品質を保つと安易に仮定しないためのケースです。**

ankrgyl は、Braintrust がリポジトリの commit と bug description から始めて修正結果を評価する workflow で、Opus 4.8 と GLM-5.2 を比較したと述べています。その単純な置き換えでは、GLM-5.2 はコストがほぼ同程度で、実行時間は長く、pass rate は低く、総合的には効率が劣ったと報告されています。

Type: Evaluation | Date: 2026-06-24

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [GLM-5.2 API ドキュメントを読む](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run) - 現行モデル向けに検証済みの初回実行サーフェスです。

このガイドでは、検証済みでインストール可能な GLM-5.2 skill リポジトリの存在を主張しません。上記の API ドキュメントを使用してください。

<a id="acknowledge"></a>
## 🙏 謝辞

このリポジトリは、実際の GLM-5.2 利用の証拠を公開で共有してくれたクリエイター、開発者、ベンチマークチーム、プロバイダー、コミュニティに触発されて作られました。

ここで紹介した高シグナルな情報源とクリエイターに感謝します: [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan), [@ScaleAILabs](https://x.com/ScaleAILabs), [@wafer_ai](https://x.com/wafer_ai), [@ankrgyl](https://x.com/ankrgyl), [@clairevo](https://x.com/clairevo), [@MatinSenPai](https://x.com/MatinSenPai), [@hrdkbhatnagar](https://x.com/hrdkbhatnagar), [@nutlope](https://x.com/nutlope), [@victormustar](https://x.com/victormustar), [@digitalocean](https://x.com/digitalocean), [@BohuTANG](https://x.com/BohuTANG)., [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@denizirgin](https://x.com/denizirgin), [@Dracoshowumore](https://x.com/Dracoshowumore), [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar), [@OkhayIea](https://x.com/OkhayIea), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@0G_labs](https://x.com/0G_labs), [@SubhoGhosh02](https://x.com/SubhoGhosh02), [@undefinedKi](https://x.com/undefinedKi), [@alighodsi](https://x.com/alighodsi), [@composio](https://x.com/composio), [@pengsonal](https://x.com/pengsonal), [@EpochAIResearch](https://x.com/EpochAIResearch), [@stagedhappen](https://x.com/stagedhappen)

最近追加したクリエイター: [@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI), [@CommandCodeAI](https://x.com/CommandCodeAI), [@coworkerapp](https://x.com/coworkerapp), [@perplexity_ai](https://x.com/perplexity_ai), [@petruknisme](https://x.com/petruknisme), [@sgl_project](https://x.com/sgl_project), [@MaziyarPanahi](https://x.com/MaziyarPanahi), [@techNmak](https://x.com/techNmak), [@spettrotoken](https://x.com/spettrotoken), [@TheZachMueller](https://x.com/TheZachMueller), [@RedHat_AI](https://x.com/RedHat_AI), [@juanjucm](https://x.com/juanjucm), [@cyrilXBT](https://x.com/cyrilXBT), [@QCXINT_](https://x.com/QCXINT_), [@vorfluxai](https://x.com/vorfluxai), [@dangerm00se](https://x.com/dangerm00se), [@SerPepeXBT](https://x.com/SerPepeXBT), [@Giannisanii](https://x.com/Giannisanii), [@thelichhh](https://x.com/thelichhh), [@weezerOSINT](https://x.com/weezerOSINT), [@MichaelGannotti](https://x.com/MichaelGannotti), [@tomkrcha](https://x.com/tomkrcha), [@vista8](https://x.com/vista8), [@light_foundry](https://x.com/light_foundry), [@orbiteditor](https://x.com/orbiteditor)。

*帰属に修正が必要な場合はご連絡ください。確認のうえ更新します。*

興味深い GLM-5.2 の実利用ケースがあれば、issue や pull request でぜひ共有してください。

[![Star History Chart](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
