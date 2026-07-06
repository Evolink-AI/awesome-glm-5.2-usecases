<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="GLM-5.2 高シグナルユースケース集 banner" width="760"></a>

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

# GLM-5.2 高シグナルユースケース集

## 🍌 概要

GLM-5.2 の高シグナルなユースケース集へようこそ。

**公開デモやクリエイターコミュニティから、GLM-5.2 の実例、チュートリアル、統合、評価、価格シグナル、制約を収集しています。**

このローカライズ版 README は、具体的なワークフロー、公開ベンチマーク、実演デモ、統合、コスト、実用上の注意点を持つケースに焦点を当てています。

各ケースのタイトルは公開ソースへ、作者ハンドルは作者プロフィールへリンクしています。

[Evolink で GLM-5.2 を試す](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 Overview

- **166 件の厳選 GLM-5.2 ケース**を、公開クリエイター、ベンチマークチーム、ツール開発者、プロバイダー、実利用者から収集しています。
- ベンチマークとフロンティア評価、コーディングエージェントと長文脈ワークフロー、実演デモとショーケースビルド、プロバイダ・ツール統合、コスト、価格、ローカル運用、制約、注意点、安全性シグナルを扱います。
- 各ケースには元ソース、作者クレジット、簡潔な活用ポイント、エビデンスタイプ、公開日を含めています。
- 実用ワークフロー、強みと限界の比較、プロバイダ経路、実際の検証例を探すために使ってください。

> [!NOTE]
> このコレクションは hype よりも具体的な証拠を重視します: 公開デモ、ベンチマーク方法、統合メモ、コストデータ、明示された caveat です。

> [!NOTE]
> ローカライズ版 README は英語版と同じケース順、リンク、anchor、帰属を維持します。追跡性を優先するため、ケースタイトルは原文に近い表記を残す場合があります。

<a id="quick-start"></a>
## ⚡ Quick Start

Evolink の OpenAI 互換 Chat Completions API から GLM-5.2 を使用できます。[Evolink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) で API key を取得し、実行前に `EVOLINK_API_KEY` として設定してください。

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

GLM-5.2 API の完全なリファレンス: [GLM-5.2 API docs を開く](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases).

## 📑 メニュー

| セクション | ケース |
|---|---|
| [📏 ベンチマークとフロンティア評価](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162 |
| [💻 コーディングエージェントと長文脈ワークフロー](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155 |
| [🎮 実演デモとショーケースビルド](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161 |
| [🔌 プロバイダ・ツール統合](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165 |
| [💸 コスト、価格、ローカル運用](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166 |
| [🧭 制約、注意点、安全性シグナル](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163 |
| [🙏 謝辞](#acknowledge) | クレジットと修正ポリシー |

### [📏 ベンチマークとフロンティア評価](#benchmarks-frontier-evaluation)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 162: VulcanBench 10-Task 80 Percent Tie](#case-162) | このケースは、cost と score の両方が重要な post-cutoff の実エンジニアリング課題で GLM-5.2 を比較するのに役立ちます。Morgan Linton によると、VulcanBench では GLM 5.2 High、Fable 5 Low、Sonnet 5 High が 10 repo で同じ 80 percent になり、GLM の cost は中間でした。 | 評価 |
| [Case 159: SWE-Rebench 51.1 Percent Checkpoint](#case-159) | このケースは、更新が続く SWE エージェント系リーダーボードで GLM-5.2 を追うのに向いています。最新の SWE rebench 投稿では 2.62 million tokens で 51.1 percent とされ、新しく加わった DeepSeek、MiMo、Qwen、Gemma より明確に上です。 | 評価 |
| [Case 154: LaunchDarkly Edge-Case Win At 40/41](#case-154) | このケースは、チャット専用評価ではなく業務ツールを使うエージェント作業で GLM-5.2 を試すのに向いています。Composio によれば、GitHub、Jira、LaunchDarkly の 41 タスク中 40 を取り、保留承認のエッジケースを拾えたのは GLM だけでした。 | 評価 |
| [Case 110: AA-Briefcase タスク時間フロンティア](#case-110) | ベンチマークスコアだけでなく、1 タスクあたり時間も重要な長期知識労働で GLM-5.2 を比較するためのケースです。 | ベンチマーク |
| [Case 111: Code Arena Frontend 直接対決マージン](#case-111) | 単一の順位スクリーンショットではなく、ペアごとの直接対決結果から GLM-5.2 のフロントエンド優位を確認するためのケースです。 | ベンチマーク |
| [Case 113: SWE Atlas Codebase QnA 準優勝](#case-113) | 単一タスクの SWE リーダーボードだけでなく、Codebase QnA、テスト作成、リファクタリング全体で GLM-5.2 を追うためのケースです。 | ベンチマーク |
| [Artificial Analysis Intelligence Index](#case-1) | Artificial Analysis ポストを使用して、インテリジェンスとタスクあたりのコストに関して GLM-5.2 を他のオープンウェイトおよび独自のフロンティア モデルと比較します。 | ベンチマーク |
| [Code Arena Frontend Ranking](#case-2) | このケースを使用して、アリーナ スタイルの比較によって判断される実際のフロントエンド コーディング タスクで GLM-5.2 を評価します。 | ベンチマーク |
| [Design Arena First Place](#case-3) | このケースを使用して、GLM-5.2 がテキスト中心のコーディング ベンチマークだけではなく、デザインとコードのタスクを処理できるかどうかを判断します。 | ベンチマーク |
| [FrontierSWE Result](#case-4) | FrontierSWE の投稿を使用して、ソフトウェア エンジニアリング タスクに関して GLM-5.2 を GPT-5.5、Opus、および Fable スタイルのモデルと比較します。 | ベンチマーク |
| [DeepSWE Open-Source Lead](#case-5) | DeepSWE のケースを使用して、難しいソフトウェア エンジニアリングの評価タスク用の強力なオープン モデルとしての GLM-5.2 を理解します。 | ベンチマーク |
| [Terminal-Bench Over 80 Percent](#case-6) | 端末指向のコーディングおよびエージェント ワークフローについて GLM-5.2 を評価する場合は、このケースを使用してください。 | ベンチマーク |
| [SWELancer と GPT-5.5 の比較](#case-7) | この SWELancer のケースを、タスクの成功、報酬、完了時間に関する GLM-5.2 と GPT-5.5 の具体的なマルチメトリクスの比較として使用します。 | 評価 |
| [BridgeBench Perfect Score Signal](#case-8) | このケースを使用して、リーダーボードをコーディングするだけではなく、根拠に基づいた複数ステップの推論に基づいて GLM-5.2 を検査します。 | ベンチマーク |
| [BridgeBench Reasoning Number One](#case-9) | このケースを使用して、根拠のある推論タスクに関して GLM-5.2 をクローズド フロンティア モデルと比較します。 | ベンチマーク |
| [KernelBench-Hard Without Shortcutting](#case-10) | ベンチマークのゲインがショートカットではなく有効な実装動作によるものであるかどうかを確認する場合は、このケースを使用してください。 | 評価 |
| [Runescape Bench Catch-Up](#case-11) | このケースは、ゲームのようなベンチマーク タスクにおける無重みモデルの進行状況を示す速い信号として使用します。 | ベンチマーク |
| [BridgeBench Speed Improvement](#case-12) | このケースを使用して、インテリジェンスとともに速度が重要となる、レイテンシーに敏感なワークフローを評価します。 | ベンチマーク |
| [KernelBench ハードおよびメガ GPU コーディング](#case-60) | このケースを使用して、KernelBench-Hard と KernelBench-Mega にわたる GPU カーネル コーディングで GLM-5.2 を評価します。オープン エージェント トレースにより結果が検査可能になります。 | ベンチマーク |
| [DeepSWE Max-Effort オープンソース首位](#case-70) | 最大 effort 設定の DeepSWE で GLM-5.2 を追跡するためのケースです。公開リーダーボードでは open model 中 1 位、pass@1 は 44% と示されています。 | ベンチマーク |
| [LLM Debate Benchmark 準優勝](#case-72) | コーディング以外でも GLM-5.2 を評価するためのケースです。敵対的な multi-turn debate で、max-reasoning variant が Claude 系に次ぐ 2 位となっています。 | ベンチマーク |
| [AA-Omniscience hallucination rate](#case-76) | 不確実性の扱いを比較するためのケースです。公開された AA-Omniscience 結果では、GLM-5.2 の hallucination rate は複数の frontier model より低くなっています。 | 評価 |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | コーディング専用のリーダーボードではなく、長期的な知識労働で GLM-5.2 を比較するためのケースです。 | 評価 |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | ゲーム構築品質で GLM-5.2 を判断するためのケースです。Game Dev Arena で 2 位に入り、その順位ではオープンウェイト陣営の最上位になりました。 | 評価 |

### [💻 コーディングエージェントと長文脈ワークフロー](#coding-agents-long-context-workflows)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 155: Cotal Four-Agent TUI Loop](#case-155) | このケースは、コーディングループを専門エージェントに分担させるのに使えます。著者は Opus のリードと GPT のレビュー役の下で GLM-5.2 ワーカーを 2 体使い、lazygit 風 TUI を 47 分で人手なしに仕上げました。 | デモ |
| [Case 153: Legacy Migration Cost-Cut Pilot](#case-153) | このケースは、レガシーアプリ刷新ループの中で GLM-5.2 を低コスト側の実行役として評価するのに使えます。8090 のパイロットでは、GLM と Software Factory の組み合わせが Opus 4.8 単体比で 16.4 倍安く、ただし約 3 倍遅いとされています。 | 評価 |
| [Case 145: OpenCode と Fireworks へのコスト削減移行](#case-145) | open-model harness への切り替えだけで十分か確かめたいならこの事例が役立ちます。作者は個人の coding と loop task を Fireworks 上の GLM-5.2 + OpenCode に移し、日常品質をほぼ保ったまま token コストが 3 分の 1 になったと言っているからです。 | 評価 |
| [Case 143: Hermes MoA の GLM アグリゲーターワークフロー](#case-143) | 価値の高い agent の 1 ターンに追加のオーケストレーションをかける価値があるなら、この事例が役立ちます。Hermes Agent の Mixture of Agents 構成は、GLM-5.2 と他モデルを組み合わせ、小さな追加コストで目に見えて良い出力を出したからです。 | 統合 |
| [Case 142: Cline の推論オン/オフによるハーネス差分](#case-142) | モデルの重みだけでなく harness 設計を見たいならこの事例が役立ちます。同じ GLM-5.2 が同じ coding task で、reasoning を有効にしただけで 57.3% から 68.5% に伸びたからです。 | 評価 |
| [Case 136: Cursor + Fireworks 455M-Token Field Test](#case-136) | 高速な Fireworks 提供と 4.55 億 tokens の実運用を作者が報告しており、すぐに Opus や GPT-5.5 に戻る気がないとしているため、GLM-5.2 を Cursor の本格的な常用モデルとして判断するためのケースです。 | 評価 |
| [Case 135: Devin Desktop Harness With Skill Portability](#case-135) | Z.ai 自身の coding surface が不安定に感じられるときに、GLM-5.2 を Devin Desktop 内で試すためのケースです。作者は、より簡単な skill 移植、高速さ、そして hackability の高さを報告しています。 | 評価 |
| [Case 127: Pi インライン GLM レビュアー](#case-127) | Pi スタイルの coding-agent loop に第 2 のレビュー担当を加えたいときに使うケースです。作者によれば、GLM-5.2 は Opus に turn ごとに助言でき、コスト増はおよそ 10% に収まるとのことです。 | 統合 |
| [Case 122: AgentRouter による一発 Telegram Bot](#case-122) | 最低限動くだけのコードではなく、本番運用を意識した default を GLM-5.2 が one-shot の coding-agent build で自力推論できるか試すためのケースです。 | デモ |
| [Case 117: OpenCode Go リファクタリング初回成功](#case-117) | ベンチマーク主張だけに頼らず、OpenCode 内の中規模 Go リファクタリングで GLM-5.2 を評価するためのケースです。 | 評価 |
| [Case 119: Claude Code + Cursor 3.36ドル常用実行](#case-119) | より自律的な coding work を open weights に移す前に、Claude Code と Cursor で日常利用モデルとしての GLM-5.2 を見極めるためのケースです。 | 評価 |
| [One Hour Forty Two Minute Refactor Loop](#case-13) | このケースは、TDD、レビュー担当者のフィードバック、回帰チェックによる長時間にわたる自律的なフロントエンド リファクタリングのパターンとして使用してください。 | デモ |
| [OpenCode Bug Fix And Implementation Test](#case-14) | このケースを使用して、バグ修正と小規模な実装タスクのための OpenCode コーディング エージェントとして GLM-5.2 をテストします。 | デモ |
| [OpenCode Retro Video Game Walkthrough](#case-15) | このチュートリアルを使用して、単一のプロンプトから GLM-5.2 と OpenCode を使用して小規模なゲームを構築し、モデルが実装の詳細をどのように処理するかを検査します。 | チュートリアル |
| [HTML5 Physics Simulations Contest](#case-16) | このケースを使用して、ライブラリを使用しない自己完結型 HTML5 物理シミュレーションで GLM-5.2 コードと Kim K2.7 コードを比較します。 | 評価 |
| [Personal Site UI UX Build](#case-17) | このケースを使用して、GLM-5.2 に洗練された個人サイトを求め、複数のターンで UI/UX がどの程度改善されるかを検証します。 | デモ |
| [AI Contract Review Product Build](#case-18) | このケースを使用して、PRD、時間予算、ステップ数、使用量割り当て、およびコード品質の比較を使用して製品構築タスクで GLM-5.2 を評価します。 | 評価 |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | このケースを使用して、大規模なエージェント開発タスクのために GLM-5.2 がどのように ZCode 3.0 に統合されるかを理解してください。 | 統合 |
| [GLM-5.2 で構築された ZCode 用 Linux ラッパー](#case-20) | このケースは、コーディング エージェント環境に関するツールを支援する GLM-5.2 の例として使用してください。 | デモ |
| [Computer Use Skill Packaging](#case-21) | このケースを使用して、オープンソースのコンピューター使用リポジトリを再利用可能なスキルに変えるためのヘルパーとして GLM-5.2 を検討してください。 | デモ |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | このケースを使用して、単一のチャット セッションではなく完全なエージェント開発環境内で GLM-5.2 を評価します。 | デモ |
| [ローカルサービスを備えた OpenCode ハーネス](#case-62) | このケースを使用して、Claude Opus と比較する前に、OpenCode ハーネス、ローカル サービング、およびツールを多用するコーディング ワークフローを使用して GLM-5.2 をテストします。 | 評価 |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | このケースを使用して、指示を RLM システム プロンプトに移動することで、GLM-5.2 のロング コンテキストのカウントと REPL エージェントの動作を改善します。 | 統合 |
| [DeepAgents Code Open Harness Trial](#case-66) | このケースを使用して、オープン コーディング エージェント ハーネスで GLM-5.2 を試し、再現可能なエージェント シェルでモデルを比較します。 | デモ |
| [本番マーケティング agent stack のルーティング](#case-77) | 構造化、速度、self-hosting を重視する production agent workflow に GLM-5.2 を割り当てつつ、曖昧な判断はより強い closed model に任せるためのケースです。 | 評価 |
| [M3 Ultra Pokemon Red Goal Run](#case-80) | M3 Ultra 上での長時間ローカル coding agent 実行において、GLM-5.2 を評価するためのケースです。約半日かけて Pokemon Red を HTML で再現しようとした実例を追えます。 | デモ |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | 実際のリポジトリのバグ修正で GLM-5.2 と Opus 4.8 を比較するためのケースです。GLM はより多くのトークンを使いましたが、より安価でクリーンな最終パッチを出しました。 | 評価 |
| [Case 102: OpenInspect FP8 Background Agent](#case-102) | ホスト型チャットではなく、GLM-5.2 を FP8 で回すセルフホストの background-agent stack を調べるためのケースです。 | 統合 |

### [🎮 実演デモとショーケースビルド](#hands-on-demos-showcase-builds)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 161: REAP NVFP4 Rubiks Cube One-Shot](#case-161) | このケースは、単一プロンプトの対話型 build で GLM-5.2 を試すのに向いています。REAP-NVFP4 の demo では、1 回の prompt だけで 3D Rubiks Cube、実際の scramble、live state、solve button まで生成したと述べています。 | デモ |
| [Case 158: OMP Relay iPhone Client](#case-158) | このケースは、ローカル GLM-5.2 エージェントを素早くモバイル面に載せたいときに使えます。著者によれば、Codex の build-ios-app plugin が、すでに GLM-5.2 と Cloudflare トンネルを使う OMP relay 向けに、数時間で整った iPhone クライアントを作りました。 | デモ |
| [Case 144: オープンソースの DevRel リサーチエージェント](#case-144) | GLM-5.2 を汎用チャットではなく縦型の調査アシスタントに変えたいならこの事例が役立ちます。作者は、製品とオーディエンスの入力を根拠付きのコンテンツ候補とアウトラインに変えるオープンソース DevRel エージェントを作ったからです。 | デモ |
| [Case 123: Recast 6 バリエーションの LP 反復ループ](#case-123) | まず複数の GLM-5.2 案を作ってから最良案を coding agent に引き継ぎ、低コストで landing page を試作するためのケースです。 | チュートリアル |
| [Playable Backrooms One-Shot](#case-23) | このケースを使用して、GLM-5.2 と Opus 4.8 の間で同じプロンプトのゲーム構築の出力、ランタイム、コストを比較します。 | デモ |
| [結果がまちまちの 3 つの実際のビルド](#case-24) | このケースは、注意深いデモ セットとして使用してください。実稼働ゲームやビデオ タスクのモデルを信頼する前に、複数の実際のビルドをテストしてください。 | 評価 |
| [Super Mario Clone In ZCode](#case-25) | このケースを使用して、いくつかの修正と機能のパスにわたって GLM-5.2 と ZCode を使用した反復的なゲーム構築を評価します。 | デモ |
| [Lunar Lander Contest](#case-26) | このケースを使用して、インタラクティブなゲーム スタイルのタスクで GLM-5.2、MiniMax M3、および Kim K2.7 コードを比較します。 | 評価 |
| [One-Prompt Design Arena Creation](#case-27) | このケースを使用して、GLM-5.2 がアリーナ コンテキスト内の単一のデザイン プロンプトから何を生成できるかを検査します。 | デモ |
| [研究論文のワークフローを理解する](#case-28) | このケースを使用して、状況に応じた質問や論文間の参照を含む論文読書ワークフローに GLM-5.2 を適用します。 | 統合 |
| [Constrained Poem Comparison](#case-29) | GLM-5.2 を寓話スタイルのモデルと比較する場合は、このケースを使用して、正確性とクリエイティブの品質を区別します。 | 評価 |
| [Design Sense Example](#case-30) | このケースを軽量のビジュアル デザイン シグナルとして使用し、独自のプロンプトと UI レビューで検証します。 | デモ |
| [Temple Run 風ボクセルゲームのワンショット生成](#case-71) | 単一プロンプトのゲーム生成で GLM-5.2 を stress-test し、視覚的にリッチなビルドで何が追加修正を要するかを確認するためのケースです。 | デモ |
| [OpenCode Go ワンショット実例セット](#case-78) | より open-ended な agent loop に投入する前に、OpenCode Go 内の quick one-shot build で GLM-5.2 を benchmark するためのケースです。 | デモ |
| [Space Invaders One-Prompt Build](#case-81) | 単一プロンプトのゲーム生成で GLM-5.2 を試し、その後の数回の追加入力で asset 差し替えや軽い polish がどう進むかを見るためのケースです。 | デモ |
| [OpenCode Recovery Lab One-Shot](#case-82) | 対話的な agent failure simulation を素早く試作するためのケースです。作者は約 3.50 ドルで動く recovery lab を one-shot で作れたと報告しています。 | デモ |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | 参照ベースの Web 再現で GLM-5.2 を試すためのケースです。1 つのプロンプトと元 URL だけで、ほぼピクセルレベルの忠実さでサイトを再現しました。 | デモ |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | フルスタック UI 構築で GLM-5.2 を比較するためのケースです。最も洗練された取引デスク出力にかなり近づきながら、コストはそのごく一部に収まりました。 | 評価 |
| [Case 100: Luddite Game After Claude Refusal](#case-100) | クローズドモデルが拒否したゲーム案を GLM-5.2 で代替試作し、実際に動く出力を自分で検証するためのケースです。 | デモ |

### [🔌 プロバイダ・ツール統合](#provider-tool-integrations)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 165: ZCode Launch With Mobile Agent Control](#case-165) | このケースは、ZCode を GLM-5.2 の公式 coding surface として評価するのに役立ちます。launch report では、この無料の agentic IDE が Windows、macOS、Linux で動き、Telegram、WeChat、Feishu から project progress を確認できるとされています。 | 統合 |
| [Case 160: OpenWiki Auto-Maintained Agent Docs](#case-160) | このケースは、agent が読めるドキュメントを自動で最新化したいときに役立ちます。LangChain によると、OpenWiki はコード変更に合わせて repo docs を再生成・維持し、GLM 5.2 のような open model で動きます。 | 統合 |
| [Case 152: Foundry PTUs Through FireConnect](#case-152) | このケースを使えば、エージェント用クライアントを書き直さずに企業向け Foundry 予算で GLM-5.2 を流せます。Fireworks によれば、FireConnect が Microsoft Foundry の PTU を Codex、OpenCode、Pi のフローにつなぐからです。 | 統合 |
| [Case 141: ClinePass のオープンウェイト定額購読](#case-141) | 複数のオープンウェイト coding model を 1 つの agent harness にまとめたいならこの事例が役立ちます。ClinePass は GLM-5.2 と関連モデルを、個別の provider key や請求管理ではなく月額固定で束ねているからです。 | 統合 |
| [Case 137: Free GLM API Service For Coding Agents](#case-137) | 登録なしで Hermes や他の coding agent で GLM-5.2 を試すためのケースです。共有サービスは短時間有効な API key を発行し、セットアップを軽量に保ちます。 | 統合 |
| [Case 128: Cloudflare Workers AI での OpenCode セットアップ](#case-128) | 独自のモデルホストを用意せず、coding agent 向けの無料の OpenAI 互換ルートとして Cloudflare Workers AI 経由で GLM-5.2 を動かしたいときに使うケースです。 | チュートリアル |
| [Case 129: Puter.js ノーセットアップのブラウザクライアント](#case-129) | API key、課金、バックエンド設定に触れる前に、ブラウザだけの試作で GLM-5.2 を試したいときに使うケースです。 | チュートリアル |
| [Case 130: SiliconFlow 統合エンドポイントアクセス](#case-130) | 中国系と西洋系のモデルを free trial credit 付きの単一 OpenAI 互換 SiliconFlow endpoint にまとめて扱えると投稿が説明しているため、GLM-5.2 をより広い multi-model stack に組み込みたいときに使うケースです。 | 統合 |
| [Case 124: HuggingChat で作るサイトから HF Space 配置まで](#case-124) | HuggingChat での調査から Hugging Face Spaces への静的配置まで、ほぼ無料の個人サイト workflow で GLM-5.2 を試したいときに使うケースです。 | チュートリアル |
| [Case 125: DigitalOcean Inference Engine 提供開始](#case-125) | 1M context モデルを自分でホストせずに、公式な provider access を managed infrastructure 経由で使いたいときに GLM-5.2 をルーティングするためのケースです。 | 統合 |
| [Case 115: Command Code Fast 120-250 Tok/S ティア](#case-115) | 最安の入口価格だけでなく、長期コーディング速度を重視するときに Command Code の高速な GLM-5.2 tier にアクセスするためのケースです。 | 統合 |
| [Case 116: Vercel AI Gateway Fast GLM-5.2 API](#case-116) | サーバレス速度と明示的なトークン価格が必要なときに、Vercel AI Gateway 経由で GLM-5.2 Fast を使うためのケースです。 | 統合 |
| [OpenCode Go Availability](#case-31) | このケースを使用して、テキスト、1M コンテキスト、GLM-5.1 のような価格設定を使用して OpenCode Go ワークフロー内で GLM-5.2 の可用性を追跡します。 | 統合 |
| [Ollama Cloud Availability](#case-32) | このケースを使用して、アクセス可能なオープンソースのコーディング モデル実験のために GLM-5.2 を Ollama Cloud にルーティングします。 | 統合 |
| [OpenRouter One API Call Access](#case-33) | プロバイダー ルーティングまたはマルチモデル スタックを比較する場合は、OpenRouter 経由で GLM-5.2 にアクセスする場合にこのケースを使用します。 | 統合 |
| [vLLM Day-Zero Support](#case-34) | このケースを使用して、デイゼロ サポートを備えた vLLM を介して GLM-5.2 をセルフホストまたは提供します。 | 統合 |
| [Notion Availability Via Baseten](#case-35) | このケースを使用して、Notion ワークフロー内で利用可能なオープンウェイト モデルとして GLM-5.2 を識別します。 | 統合 |
| [Fireworks Day-Zero Serving](#case-36) | このケースを使用して、ホスト型インフラストラクチャを必要とする GLM-5.2 ワークロードのサービス提供ルートとして Fireworks を評価します。 | 統合 |
| [Google Cloud モデル ガーデン リンク](#case-37) | このケースを使用して、Google Cloud 指向のデプロイメントおよびエージェント プラットフォームのコンテキストで GLM-5.2 を見つけます。 | 統合 |
| [Venice Privacy Mode](#case-38) | プライバシー モード、TEE、またはエンドツーエンド暗号化が GLM-5.2 を試行する際の決定要因となる場合は、このケースを使用してください。 | 統合 |
| [Command Code Availability](#case-39) | このケースを使用して、低コストのエントリー プランとロング コンテキスト コーディング機能を備えたコマンド コードで GLM-5.2 を試してください。 | 統合 |
| [ヌースポータルのヘルメスエージェント](#case-40) | このケースを使用して、Nous Portal および OpenRouter を介して GLM-5.2 を Hermes Agent ワークフローに接続します。 | 統合 |
| [io.net Day-Zero Launch Partner](#case-41) | 753B パラメータのロングコンテキスト モデルのコンピューティング支援型サービスを評価する場合は、このケースを使用してください。 | 統合 |
| [Modular Cloud Day-Zero Serving](#case-42) | このケースを使用して、プロバイダー規模でサービスを提供するロングコンテキスト GLM-5.2 のモジュラー クラウドを検討してください。 | 統合 |
| [Cursor Setup Through OpenRouter](#case-61) | このケースを使用して、低コストのオープン モデル コーディング ワークフローのために OpenRouter を介して Cursor で GLM-5.2 を構成します。 | チュートリアル |
| [Amp Agentic Eyes For Visual Design](#case-63) | テキストのみのモデルでデザイン タスクのビジュアル レビュー サポートが必要な場合は、このケースを使用して GLM-5.2 と Amp カスタム エージェントを組み合わせます。 | 統合 |
| [Baseten Faster One-Million-Context Serving](#case-69) | Factory Droid、OpenCode、およびコーディング ハーネスでロング コンテキストの処理速度が重要な場合は、このケースを使用して GLM-5.2 を Baseten 経由でルーティングします。 | 統合 |
| [Web デザイン向け Browser Use QA subagents](#case-74) | text-only model に視覚確認が必要なとき、GLM-5.2 を Browser Use v2 の multimodal QA subagents と組み合わせ、反復的な website 修正に使うためのケースです。 | 統合 |
| [ZCode 公式 IDE の daily free tokens](#case-79) | 大きな daily token allowance と Cursor 風 workflow を備えた無料の公式 coding IDE として、ZCode 経由で GLM-5.2 にアクセスするためのケースです。 | チュートリアル |
| [Cursor Setup Through Fireworks](#case-83) | Fireworks 経由で GLM-5.2 を Cursor に最小構成で接続し、独自クライアントコードなしで試すためのケースです。 | チュートリアル |
| [VulcanBench ZAI Provider Support](#case-84) | 専用の ZAI provider 対応と API key 導線を備えたオープン benchmark harness で GLM-5.2 を走らせるためのケースです。 | 統合 |
| [OpenCode High/Max Reasoning Variants](#case-85) | OpenCode 内で GLM-5.2 の High / Max reasoning variant にアクセスしつつ、より安定した step-limit 処理も取り込むためのケースです。 | 統合 |
| [Z.ai Coding Endpoint Selection](#case-86) | GLM-5.2 の coding plan トラフィックを、汎用 API ではなく coding 最適化済みの Z.ai endpoint に向けるためのケースです。 | チュートリアル |
| [ZenMux Free GLM-5.2 API Setup](#case-87) | 無料の GLM-5.2 API key と base URL を取得し、Claude、Cursor、Hermes などに差し込むためのケースです。 | チュートリアル |
| [Case 93: Noumena ncode GLM Default](#case-93) | 標準エンドポイントと 1M コンテキスト用エンドポイントを分け、デフォルトモデル対応も備えた ncode と Noumena 系エージェント環境に GLM-5.2 を組み込むためのケースです。 | 統合 |
| [Case 95: Claude Code Through Baseten](#case-95) | Baseten のキー、カスタム base URL、`~/.claude/settings.json` のモデル再マッピングを使って Claude Code 内で GLM-5.2 を動かすためのケースです。 | チュートリアル |
| [Case 96: Deepsec Pi Agent Default](#case-96) | セキュリティハーネス内で GLM-5.2 を試すためのケースです。`deepsec` は Pi agent のデフォルトモデルに採用し、競争力のある eval 結果を報告しました。 | 統合 |
| [Case 101: Baseten + Droid Harness Quickstart](#case-101) | Baseten と Droid harness 経由で GLM-5.2 を素早く動かし、他の IDE にも流用できる短いセットアップ手順を得るためのケースです。 | チュートリアル |
| [Case 104: OpenAI-Compatible GLM API Workflow](#case-104) | reasoning control、tool calling、長文脈 retrieval、cost tracking を備えた OpenAI 互換 GLM-5.2 クライアントを Python で組むためのケースです。 | チュートリアル |
| [Case 105: Perplexity Agent API Search Sandbox](#case-105) | search 対応の sandboxed agent を単一 API call で使いたいとき、Perplexity Agent API に GLM-5.2 を接続するためのケースです。 | 統合 |
| [Case 109: Baseten 280 TPS GLM API](#case-109) | プロバイダー遅延が重要なとき、Baseten が主張する GLM-5.2 の高速 serving を確認するためのケースです。 | 統合 |

### [💸 コスト、価格、ローカル運用](#cost-pricing-local-deployment)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 166: Full 744B On 5x ASUS GX10s](#case-166) | このケースは、極端な home-lab GLM-5.2 deployment を見積もるためのものです。著者によると、744B の full model が 5 台の ASUS GX10 上で full context 付きで動作し、real workloads 向けの causal harness にもすでに接続されています。 | デモ |
| [Case 164: Agent Route Swap In China Stack](#case-164) | このケースは、最高品質よりコスト圧力が重要なときに、mixed-model stack の agent layer へ GLM-5.2 を routing する参考になります。著者によれば、Sonnet を GLM-5.2 に置き換えると、その slot の input cost は 5 倍安くなり、品質低下は約 3 percent でした。 | 評価 |
| [Case 156: 744B Local Hardware Floor](#case-156) | このケースを使えば、GLM-5.2 のローカル計画を現実的に見積もれます。情報源によれば、量子化しても 2bit で約 239GB、4bit で約 466GB あり、RAM や VRAM は 256GB 超が実用ラインになるからです。 | 制限 |
| [Case 140: B300 x2 Agent-Led Dual-Stack Bring-Up](#case-140) | 本格的なセルフホスト型 GLM-5.2 deployment の規模感を見積もるためのケースです。スレッドでは、分析 agent がベアメタル B300 上で vLLM と SGLang の両方に NVFP4 推論を 1 日未満で立ち上げています。 | 評価 |
| [Case 139: oMLX M3 Ultra Prefill Speedup](#case-139) | 最近の kernel work 後に Apple silicon でのローカル運用可能性を再確認するためのケースです。M3 Ultra 512GB での GLM-5.2 prefill speed が、簡単なテストで品質を大きく落とさずほぼ倍増したと報告されています。 | 評価 |
| [Case 138: 20M Token Signup Credit Burst](#case-138) | 直接 signup でも実用的な GLM-5.2 試用ができるかを判断するためのケースです。投稿では、新規アカウントに 2000 万 free tokens、カード不要、完全な OpenAI 互換 access が付くとされています。 | 統合 |
| [Case 131: 4x DGX Spark ローカル GLM 運用ガイド](#case-131) | DGX Spark クラスタが現実的なローカル GLM-5.2 の道筋かどうかを見極めるためのケースです。収集されたガイドは、具体的なハードウェア費用、クラスタ構成、vLLM コマンドを 1M context の GLM 目標に結び付けています。 | チュートリアル |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 実行](#case-112) | 高性能ワークステーションを組む前に、4 GPU のローカル GLM-5.2 構成を厳しい terminal benchmark に照らして見積もるためのケースです。 | 評価 |
| [Case 118: 2x RTX PRO 6000 Blackwell でのローカル Crackme 解読](#case-118) | デバッガなしでも、本格的なローカル GLM-5.2 構成が長時間のリバースエンジニアリング課題を完了できるかを判断するためのケースです。 | デモ |
| [Output Token Cost Comparison](#case-43) | このケースを使用して、GLM-5.2 出力トークンの経済性を Opus、Fable、および GPT-5.5 スタイルのモデルと比較します。 | 評価 |
| [Local Near-Frontier Hardware ROI](#case-44) | このケースを使用して、セルフホスティング GLM-5.2 のようなモデルがエージェントのヘビー ユーザーのハードウェア コストを返済できるかどうかを検討してください。 | 評価 |
| [MLX On Two Mac Studios](#case-45) | このケースを使用して、Apple ハードウェアおよび MLX 指向のセットアップ上で実行されるローカル GLM-5.2 を調べます。 | デモ |
| [H100 Monthly Local Deployment Claim](#case-46) | このケースは、サブスクリプションとセルフホスティングのどちらかを選択する前に、ローカル展開の前提条件を確認するためのコスト比較プロンプトとして使用します。 | 評価 |
| [Daily Credits And Claude Replacement Claim](#case-47) | このケースを使用して、GLM-5.2 に関する無料クレジットと代替エージェントの物語を検証し、マーケティング上の主張と検証済みのワークロード適合性を区別します。 | 評価 |
| [Free ZCode Token Window](#case-48) | このケースを使用して、有料プロバイダーまたはローカル展開にコミットする前に、無料の ZCode 許容量を通じて GLM-5.2 をテストします。 | 統合 |
| [ZenMux Free Week Offer](#case-49) | このケースを使用して、GLM-5.2 テスト用のタイムボックス化されたフリーアクセス ウィンドウを見つけます。 | 統合 |
| [crofAIのトークンごとの価格設定](#case-50) | このケースを使用して、ルートを選択する前に GLM-5.2 のサードパーティ プロバイダーの価格を比較します。 | 統合 |
| [API Price Margin Comparison](#case-51) | GLM-5.2 を他のフロンティア ラボやオープン モデルと比較するときは、このケースを市場価格の批評として使用してください。 | 評価 |
| [Basement Local Inference Speed](#case-64) | このケースを使用して、オフライン コーディングのセットアップを計画する前に、大容量メモリの Apple ハードウェアでのローカル GLM-5.2 推論スループットを見積もります。 | デモ |
| [Unsloth Quantized Local Deployment](#case-68) | このケースは、完全なモデルの重みが通常のローカル ハードウェアにとって大きすぎる場合に、量子化された GLM-5.2 デプロイメント パスを評価するために使用します。 | チュートリアル |
| [Two M3 Ultra MLX Distributed Run](#case-88) | より大きな Apple Silicon 構成を組む前に、2 台の M3 Ultra で分散 MLX 実行した GLM-5.2 8-bit serving の実態を見積もるためのケースです。 | デモ |
| [ZCode Multiplier Cut Through September](#case-89) | peak / off-peak の multiplier 引き下げ期間を使って、GLM-5.2 の plan credits を引き延ばすためのケースです。 | 統合 |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | ハイエンドなローカル GLM-5.2 ワークステーションを見積もるためのケースです。Blackwell 2 枚のデスクトップで、4-bit 量子化ビルドの二桁デコード速度を維持しました。 | デモ |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | ローカル GLM-5.2 推論のために Mac Studio を買う意味があるかを現実的に確認するためのケースです。投稿された回収計算では、多くの利用者にとって API やプラン利用の方が有利です。 | 評価 |
| [Case 106: LiteLLM Local Outage Save](#case-106) | ホスト型 frontier API が停止や上限到達を起こしても、LiteLLM 経由でローカル GLM-5.2 に切り替えて納品を前に進めるためのケースです。 | デモ |
| [Case 107: Individual Versus Team Local ROI](#case-107) | ローカル GLM-5.2 デプロイが個人に見合うのか、より大きな開発チーム向きなのかを判断するためのケースです。 | 評価 |

### [🧭 制約、注意点、安全性シグナル](#limits-caveats-safety-signals)

| ケース | 注目点 | タイプ |
|---|---|---|
| [Case 163: Preliminary Cyber Research Parity](#case-163) | このケースは、vulnerability research の部分タスクで GLM-5.2 を測るためのものです。Irregular は、狭い cyber suite で GPT-5.4 と Opus 4.6 に近い初期内部評価を報告しつつ、end-to-end の attack scenario はまだ未検証だと明言しています。 | 制約 |
| [Case 157: OpenRouter Spend-Cut Skill Rewrite](#case-157) | このケースは、エージェントモデルを入れ替える前に移行コストを見積もるのに役立ちます。あるファンドの OpenRouter 試行では GLM-5.2 が Opus の約 8 分の 1 のコストでしたが、skill の書き換え、routing ロジック、そして遅く弱い出力を受け入れる前提が必要でした。 | 制限 |
| [Case 134: Semgrep IDOR Narrow-Win Caveat](#case-134) | ソースによれば GLM-5.2 は 1 つの IDOR benchmark で Claude Code を上回った一方、Mythos 自体とは比較されていないため、実際の security signal と見出し先行の誇張を切り分けるためのケースです。 | 制限 |
| [Case 132: LisanBench 推論効率ギャップ](#case-132) | reasoning 負荷の高い workload で GLM-5.2 を確認したいときに使うケースです。投稿された LisanBench 結果では GLM-5 より改善していますが、他の open model と比べるとまだ効率が低いことが示されています。 | 制限 |
| [Case 133: PrinzBench ドメイン不一致の注意点](#case-133) | 弱い PrinzBench スコアと、はるかに強い software・tool-use benchmark を投稿が対比しているため、GLM-5.2 を法務調査ではなく coding と agent execution に集中させるためのケースです。 | 制限 |
| [Case 126: Rust バグは通るがターン数は 7 倍](#case-126) | GLM-5.2 はバグ自体は通せても、Opus よりはるかに多くのターンを消費しうるため、コード品質の強みと現時点の agent harness overhead を切り分けるためのケースです。 | 評価 |
| [Case 114: Braintrust モデル差し替えコストの注意点](#case-114) | 実際の agentic coding workflow で、安価なモデルへの差し替えが品質を保つと安易に仮定しないためのケースです。 | 評価 |
| [No Vision Caveat](#case-52) | この場合は、GLM-5.2 がネイティブ ビジョン機能を必要とするワークフローにはあまり役に立たない可能性があることを覚えておいてください。 | 制限 |
| [現実世界のエージェントギャップに関する警告](#case-53) | このケースを使用して、GLM-5.2 がデプロイされたすべてのエージェント タスクで最適な独自モデルに一致することを証明するベンチマークの勝利を読みすぎないようにします。 | 制限 |
| [Safety Guardrail Concern](#case-54) | このケースは、機密性の高いドメインに GLM-5.2 を展開する前に安全性評価を実行するためのリマインダーとして使用してください。 | 制限 |
| [ベンチマーク方法論の批評](#case-55) | このケースを使用して、ヘッドラインの結果が GLM-5.2 を支持する場合でも、ベンチマーク手法に疑問を持ちます。 | 制限 |
| [Peak-Time Latency Concern](#case-56) | このケースは、コーディング プランを切り替える前、またはクロード コード スタイルのワークフローを GLM-5.2 にルーティングする前に、プロバイダーの遅延をテストするために使用します。 | 制限 |
| [FutureSim Non-Improvement Result](#case-57) | このケースを使用して、広範囲に展開する前に、コーディングの利点が非コーディング ドメインに一般化するかどうかを確認します。 | 制限 |
| [Launch Readiness Critique](#case-58) | このケースを使用して、モデルの機能を起動の実行、ドキュメント、API の準備から分離します。 | 制限 |
| [コーディングプランの値上げ](#case-59) | GLM-5.2 を低コストの代替品として推奨する前に、このケースを使用してプランの価格を確認してください。 | 制限 |
| [短い並列作業と長いエージェント実行](#case-67) | このケースを使用して、GLM-5.2 を短期間のコーディング タスクにルーティングしながら、より深い数時間にわたるエージェント実行用に強力なモデルを確保します。 | 制限 |
| [コード検閲とバイアスのチェック](#case-73) | コードと政治的バイアス検証の実用的な safety signal として使うためのケースであり、広範な alignment 上の懸念が解決済みだと示すものではありません。 | 制限 |
| [高難度推論での課金 failure](#case-75) | hard reasoning workload に対して GLM-5.2 を慎重に試すためのケースです。公開報告では長い実行時間、低い完了率、予想外に高い課金出力量が示されています。 | 制限 |
| [Case 103: HalluHard Multiturn Hallucination Signal](#case-103) | 他のベンチマーク成績を信頼しすぎる前に、幻覚に敏感なマルチターンタスクで GLM-5.2 を検証するためのケースです。 | 制限 |
| [Case 108: Open-Weight Security Emergency Warning](#case-108) | 安全計画のシグナルとして、open-weight の GLM-5.2 が offensive security agents の運用摩擦を下げる点を確認するためのケースです。 | 制限 |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 ベンチマークとフロンティア評価
<a id="case-162"></a>
### Case 162: [VulcanBench 10-Task 80 Percent Tie](https://x.com/morganlinton/status/2072689409011679642) (作者 [@morganlinton](https://x.com/morganlinton))

**このケースは、cost と score の両方が重要な post-cutoff の実エンジニアリング課題で GLM-5.2 を比較するのに役立ちます。Morgan Linton によると、VulcanBench では GLM 5.2 High、Fable 5 Low、Sonnet 5 High が 10 repo で同じ 80 percent になり、GLM の cost は中間でした。**

Morgan Linton によると、この benchmark は Flask、aiohttp、sqlglot などの project から取った 10 件の実エンジニアリング task を使っており、すべて post-training-cutoff と説明されています。Fable 5 Low、GLM 5.2 High、Sonnet 5 High はいずれも 80 percent で、reported cost は 2.27、8.41、15.81 dollars でした。単一モデルの自慢ではなく、3 者の価格対品質チェックポイントとして有用です。

タイプ: 評価 | 日付: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-Rebench 51.1 Percent Checkpoint](https://x.com/ibragim_bad/status/2072318238407483593) (作者 [@ibragim_bad](https://x.com/ibragim_bad))

**このケースは、更新が続く SWE エージェント系リーダーボードで GLM-5.2 を追うのに向いています。最新の SWE rebench 投稿では 2.62 million tokens で 51.1 percent とされ、新しく加わった DeepSeek、MiMo、Qwen、Gemma より明確に上です。**

ibragim_bad によると、最新の SWE rebench 更新では GLM-5.2 が複数の新しい open model と並んで追加されました。公開された数値では、GLM は 2.62 million tokens で 51.1 percent、DeepSeek V4 Pro は 42.7 percent、MiMo V2.5 Pro は 42.4 percent、Qwen と Gemma はそれ以下で、公開リーダーボードの具体的な比較点になっています。

タイプ: 評価 | 日付: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case Win At 40/41](https://x.com/composio/status/2072355937415827950) (作者 [@composio](https://x.com/composio))

**このケースは、チャット専用評価ではなく業務ツールを使うエージェント作業で GLM-5.2 を試すのに向いています。Composio によれば、GitHub、Jira、LaunchDarkly の 41 タスク中 40 を取り、保留承認のエッジケースを拾えたのは GLM だけでした。**

Composio は、GitHub、Jira、LaunchDarkly など実ツールを使う 41 のエージェントタスクで GLM-5.2 を Claude Opus 4.8 と GPT-5.5 にぶつけました。GLM は 40/41、Opus と GPT はどちらも 39/41 です。LaunchDarkly の 1 タスクでは、GLM だけがフラグを stale と判定する前に pending approval を確認し、他の 2 モデルは on/off 状態で止まりました。

タイプ: 評価 | 日付: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench Open-Weight Patch Runner-Up](https://x.com/ValsAI/status/2072099011398627639) (作者 [@ValsAI](https://x.com/ValsAI))

**GLM-5.2 を攻撃寄りの脆弱性発見とパッチ作成で測りたいならこの事例が役立ちます。CyberBench で 60 件の実在 OSS-Fuzz 脆弱性に対して総合 2 位になっているからです。**

ValsAI は、CyberBench が「脆弱ビルドだけを落とす PoC 提出」と「挙動を壊さないパッチ作成」を組み合わせた評価だと説明しています。60 件の OSS-Fuzz メモリ安全性脆弱性では GPT-5.5 が首位で、GLM 5.2 は最も強い open-weight 群の一つとして示されています。

タイプ: 評価 | 日付: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Artificial Analysis ポストを使用して、インテリジェンスとタスクあたりのコストに関して GLM-5.2 を他のオープンウェイトおよび独自のフロンティア モデルと比較します。**

Artificial Analysis は、GLM-5.2 をインテリジェンス インデックスの主要なオープンウェイト モデルとして報告し、スコアは 51 で、インテリジェンスとタスクあたりのコストに関してパレート フロンティアの位置にあります。この投稿には、モデルのサイズ、コンテキスト ウィンドウ、価格、プロバイダーの可用性も記録されます。

タイプ: ベンチマーク | 日付: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (作者 [@arena](https://x.com/arena))

**このケースを使用して、アリーナ スタイルの比較によって判断される実際のフロントエンド コーディング タスクで GLM-5.2 を評価します。**

Arena アカウントは、GLM-5.2 Max が Code Arena フロントエンドで 2 位にランクされ、他のオープン モデルを上回り、フロンティア エントリーのトップに迫っていると報告しました。この投稿は、フロントエンド、React、HTML、ゲーム、シミュレーション、リファレンスベースのデザインのユースケースに特に役立ちます。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (作者 [@Designarena](https://x.com/Designarena))

**このケースを使用して、GLM-5.2 がテキスト中心のコーディング ベンチマークだけではなく、デザインとコードのタスクを処理できるかどうかを判断します。**

Design Arena は、GLM-5.2 が Elo スコア 1360 で 1 位になったと報告し、オープンウェイト モデルの設計コード パフォーマンスの飛躍を強調しました。プロジェクト固有の UI レビューの代わりとしてではなく、設計ベンチマーク信号として扱います。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (作者 [@ProximalHQ](https://x.com/ProximalHQ))

**FrontierSWE の投稿を使用して、ソフトウェア エンジニアリング タスクに関して GLM-5.2 を GPT-5.5、Opus、および Fable スタイルのモデルと比較します。**

この投稿では、GLM-5.2 が FrontierSWE で 3 位にランクされていると報告しており、これを、実装の負荷が高いエンジニアリング作業においてトップの独自モデルとの差を縮める最初のオープンウェイト モデルの 1 つであると位置づけています。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (作者 [@AiBattle_](https://x.com/AiBattle_))

**DeepSWE のケースを使用して、難しいソフトウェア エンジニアリングの評価タスク用の強力なオープン モデルとしての GLM-5.2 を理解します。**

AiBattle は、GLM-5.2 の 46.2% DeepSWE スコアを報告し、それがそのベンチマークのコンテキストにおけるオープンソース モデルの最高スコアであると説明しました。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (作者 [@cline](https://x.com/cline))

**端末指向のコーディングおよびエージェント ワークフローについて GLM-5.2 を評価する場合は、このケースを使用してください。**

クライン氏は、ターミナルベンチで 80% を超えた最初のオープンウェイト モデルとして GLM-5.2 を強調し、これをアクセス可能なツールベースの開発のフロンティア レベルのオプションとして位置づけました。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer と GPT-5.5 の比較](https://x.com/gosrum/status/2067153091842203676) (作者 [@gosrum](https://x.com/gosrum))

**この SWELancer のケースを、タスクの成功、報酬、完了時間に関する GLM-5.2 と GPT-5.5 の具体的なマルチメトリクスの比較として使用します。**

著者は、アクセスできない 2 つのタスクを除いて、タスクの成功、獲得報酬、完了までの時間に関する SWELancer の最新結果において、GLM-5.2 が予想外に GPT-5.5 を上回ったという日本のベンチマーク更新情報を共有しました。

タイプ: 評価 | 日付: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (作者 [@bridgemindai](https://x.com/bridgemindai))

**このケースを使用して、リーダーボードをコーディングするだけではなく、根拠に基づいた複数ステップの推論に基づいて GLM-5.2 を検査します。**

BridgeMind は、GLM-5.2 が BridgeBench BS ベンチマークで満点を獲得した最初のモデルであると報告しており、推論重視の評価主張の有用な情報源となっています。

タイプ: ベンチマーク | 日付: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (作者 [@bridgebench](https://x.com/bridgebench))

**このケースを使用して、根拠のある推論タスクに関して GLM-5.2 をクローズド フロンティア モデルと比較します。**

BridgeBench は、GLM-5.2 が推論ベンチマークでナンバー 1 の座を獲得し、その測定コンテキストで Claude Fable 5 を上回っていると報告しました。

タイプ: ベンチマーク | 日付: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (作者 [@elliotarledge](https://x.com/elliotarledge))

**ベンチマークのゲインがショートカットではなく有効な実装動作によるものであるかどうかを確認する場合は、このケースを使用してください。**

KernelBench-Hard の投稿では、興味深い結果はスコアだけでなく、GLM-5.2 が fp8 GEMM 問題で不適切なショートカットの使用を停止し、ベンチマークの整合性に関連するものになったと述べています。

タイプ: 評価 | 日付: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (作者 [@maxbittker](https://x.com/maxbittker))

**このケースは、ゲームのようなベンチマーク タスクにおける無重みモデルの進行状況を示す速い信号として使用します。**

この投稿では、Runescape ベンチで GLM-5.2 のスコアが最近の独自モデルよりも優れていると報告しており、その結果を利用して、オープンソースのフロンティア機能がいかに早く追いつくかを示しています。

タイプ: ベンチマーク | 日付: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (作者 [@bridgebench](https://x.com/bridgebench))

**このケースを使用して、インテリジェンスとともに速度が重要となる、レイテンシーに敏感なワークフローを評価します。**

BridgeBench は、GLM-5.2 が GLM-5.1 の 3 倍高速であり、速度ベンチマークで 4 番目であると報告しており、反復速度が使いやすさに影響を与えるワークフローに適していると報告しています。

タイプ: ベンチマーク | 日付: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench ハードおよびメガ GPU コーディング](https://x.com/elliotarledge/status/2068177175640240323) (作者 [@elliotarledge](https://x.com/elliotarledge))

**このケースを使用して、KernelBench-Hard と KernelBench-Mega にわたる GPU カーネル コーディングで GLM-5.2 を評価します。オープン エージェント トレースにより結果が検査可能になります。**

KernelBench アップデートでは、H100、B200、RTX PRO 6000 のテスト、オープンソースのエージェント トレース、および比較の最上位のオープン モデルとして GLM-5.2 が報告されています。

タイプ: ベンチマーク | 日付: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE Max-Effort オープンソース首位](https://x.com/datacurve/status/2068473057107476680) (作者 [@datacurve](https://x.com/datacurve))

**最大 effort 設定の DeepSWE で GLM-5.2 を追跡するためのケースです。公開リーダーボードでは open model 中 1 位、pass@1 は 44% と示されています。**

DataCurve は DeepSWE の leaderboard update を共有し、GLM-5.2 が pass@1 44% で、open model の中では Kimi K2.7 Code を 17 ポイント上回ったと示しました。これは benchmark update として扱うべきであり、あらゆる実運用 agent workflow がすでに解決された証拠とみなすべきではありません。

タイプ: ベンチマーク | 日付: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM Debate Benchmark 準優勝](https://x.com/LechMazur/status/2068428300460974279) (作者 [@LechMazur](https://x.com/LechMazur))

**コーディング以外でも GLM-5.2 を評価するためのケースです。敵対的な multi-turn debate で、max-reasoning variant が Claude 系に次ぐ 2 位となっています。**

Lech Mazur は、GLM-5.2 Max が 2 位になった LLM Debate Benchmark の結果を共有しました。この benchmark は幅広いトピックにわたる敵対的な multi-turn debate を測定しており、標準的な coding leaderboard の外側にある reasoning signal として有用です。

タイプ: ベンチマーク | 日付: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience hallucination rate](https://x.com/yuhasbeentaken/status/2068259921519423855) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**不確実性の扱いを比較するためのケースです。公開された AA-Omniscience 結果では、GLM-5.2 の hallucination rate は複数の frontier model より低くなっています。**

この投稿では、AA-Omniscience における GLM-5.2 の hallucination rate は 28% で、Fable 5 や DeepSeek V4 Pro より高い rate を示したモデル群より低いと報告されています。この benchmark は、推測する代わりに model が拒否または不確実性を認めるかどうかに焦点を当てています。

タイプ: 評価 | 日付: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**コーディング専用のリーダーボードではなく、長期的な知識労働で GLM-5.2 を比較するためのケースです。**

Artificial Analysis によると、GDPval-AA での GLM-5.2 は Elo 1524 で、Claude Fable 5 と Opus 4.8 に次ぐ総合 3 位、GPT-5.5 xhigh の 1509 をわずかに上回りました。オープンウェイトモデルでは大差の首位であり、投稿では 1,999 試合にわたって 1 タスク平均約 31 ターンだったと述べられています。

タイプ: 評価 | 日付: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (作者 [@Designarena](https://x.com/Designarena))

**ゲーム構築品質で GLM-5.2 を判断するためのケースです。Game Dev Arena で 2 位に入り、その順位ではオープンウェイト陣営の最上位になりました。**

Design Arena は、Game Dev Arena における GLM-5.2 のスコアを Elo 1368 と報告しており、GLM-5.1 から 29 ポイント上昇し、順位も 6 つ上がったとしています。投稿では Claude Fable 5 と同等の性能帯にあるとされ、総合 2 位、ラボ別では OpenAI を上回り Anthropic のみが上位だったと述べています。

タイプ: 評価 | 日付: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [PostTrainBench 信頼性首位](https://x.com/hrdkbhatnagar/status/2070244540108423427) (作者 [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**見出しスコアだけでなく、84 タスクで failed run が 0 件だったという agent reliability も含めて GLM-5.2 Max を比較するためのケースです。**

hrdkbhatnagar は、GLM 5.2 Max reasoning が 34.29% で Opus 4.8 Max の 34.08% をわずかに上回った PostTrainBench leaderboard を共有しています。同じ投稿では、GLM が 84 runs で failed run 0 件だった一方、Opus agents ではおよそ 10% の failure rate があったとも述べられており、raw pass rate だけでなく agent の信頼性を重視するチームに有用です。

タイプ: ベンチマーク | 日付: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211件リポジトリ課題評価](https://x.com/FireworksAI_HQ/status/2070181898962534570) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**公開 benchmark だけでなく private repo の実務 engineering task で GLM-5.2 を判断するためのケースです。公開値には score、speed、task あたりの cost が含まれています。**

Fireworks は、Faros と共同で行った 211 件の実 engineering task 評価で、Claude Code + GLM-5.2 が Claude Code + Opus 4.8 と Codex + GPT-5.5 の両方を上回ったと述べています。投稿では、judge score 0.568 対 0.521 / 0.466、task あたり 321 秒 対 775 / 392、task あたり 0.92 ドル 対 1.76 / 2.06 という数値が示され、さらに Faros が公開 benchmark だけでなく自社の repositories と業務を使ったことも明記されています。

タイプ: 評価 | 日付: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase タスク時間フロンティア](https://x.com/ArtificialAnlys/status/2069914443639635978) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**ベンチマークスコアだけでなく、1 タスクあたり時間も重要な長期知識労働で GLM-5.2 を比較するためのケースです。**

Artificial Analysis は、GLM-5.2 が AA-Briefcase のパレートフロンティア上にあり、スコア 1261、1 タスク平均 16.3 分を記録し、GPT-5.5 xhigh の 1159 を上回りつつ、同ベンチマークで最高性能の open-weights model だと述べています。単なるリーダーボード順位ではなく、長期タスクの成果物品質と実行時間を比較したいチームに有用な benchmark です。

タイプ: ベンチマーク | 日付: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena Frontend 直接対決マージン](https://x.com/arena/status/2069885722333769963) (作者 [@arena](https://x.com/arena))

**単一の順位スクリーンショットではなく、ペアごとの直接対決結果から GLM-5.2 のフロントエンド優位を確認するためのケースです。**

arena は、GLM-5.2 Max が Code Arena: Frontend の首位に到達した理由を分解し、1 つを除くすべての対戦相手との組み合わせで相手より高い win share を出したと説明しています。スレッドでは Kimi-K2.6 に対する 61.0%、Sonnet 4.6 に対する 59.4%、Opus 4.7 Thinking に対する 55.0%、GPT-5.5 xHigh との 41.7% 対 40.0% の接戦、そして GLM-5.1 との 45.5% 引き分けが示されています。

タイプ: ベンチマーク | 日付: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas Codebase QnA 準優勝](https://x.com/ScaleAILabs/status/2069864932913631617) (作者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**単一タスクの SWE リーダーボードだけでなく、Codebase QnA、テスト作成、リファクタリング全体で GLM-5.2 を追うためのケースです。**

Scale AI Labs は、GLM 5.2 が SWE Atlas の 3 つのリーダーボード、Codebase QnA、Test Writing、Refactoring のすべてで公開されたと述べています。特に Codebase QnA で 2 位に入った点を強調し、open model が全体として frontier system に迫ってきていると説明しています。

タイプ: ベンチマーク | 日付: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 コーディングエージェントと長文脈ワークフロー
<a id="case-155"></a>
### Case 155: [Cotal Four-Agent TUI Loop](https://x.com/silvanrec/status/2072335315822403656) (作者 [@silvanrec](https://x.com/silvanrec))

**このケースは、コーディングループを専門エージェントに分担させるのに使えます。著者は Opus のリードと GPT のレビュー役の下で GLM-5.2 ワーカーを 2 体使い、lazygit 風 TUI を 47 分で人手なしに仕上げました。**

silvanrec によると、Cotal は 4 モデルを協調させました。フロントエンド担当とバックエンド担当の GLM-5.2 が 2 体、バックグラウンドレビュー役の GPT-5.5、そしてループ全体を率いる Claude Opus です。実用的な TUI コンソールを作る 1 つのプロンプトから始まり、4 ラウンドの中でレンダリングやタブ配線のバグを見つけ、エージェント間の handoff を回し、47 分で動く結果を出しました。投稿では open source 層として npx cotal-ai setup --full も示しています。

タイプ: デモ | 日付: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Legacy Migration Cost-Cut Pilot](https://x.com/chamath/status/2072390507628540213) (作者 [@chamath](https://x.com/chamath))

**このケースは、レガシーアプリ刷新ループの中で GLM-5.2 を低コスト側の実行役として評価するのに使えます。8090 のパイロットでは、GLM と Software Factory の組み合わせが Opus 4.8 単体比で 16.4 倍安く、ただし約 3 倍遅いとされています。**

Chamath は PHP から Next.js への初期モダナイズ実験を共有しています。8090 の Software Factory を載せた Opus 4.8 は Opus 単体より 1.4 倍安く 1.5 倍速く、一方で同じファクトリーに GLM 5.2 を組み合わせると Opus 単体比で 16.4 倍安くなる代わりに約 3 倍遅くなったとされています。投稿では n=1 の方向性確認にすぎず、10 から 15 件の実案件で再検証すべきだと明言しています。

タイプ: 評価 | 日付: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio Browser-Use Local Loop](https://x.com/MaziyarPanahi/status/2071955191260151862) (作者 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**完全ローカルな GLM-5.2 スタックが consumer hardware 上で軽い browser agent 作業をこなせるか試したいならこの事例が役立ちます。作者は Mac Studio 上の llama.cpp と browser-use で Hugging Face の PII モデルを探しました。**

MaziyarPanahi は、Mac Studio 上で llama.cpp により GLM-5.2 をローカル実行し、その上に browser-use の agent loop を載せたと述べています。公開例では Hugging Face を操作して `privacy-filter-nemotron` を見つけています。

タイプ: デモ | 日付: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop Agent Swap Cost Cut](https://x.com/aronkor/status/2072032854675218538) (作者 [@aronkor](https://x.com/aronkor))

**既存の agent harness の中で単純なモデル差し替えを試したいならこの事例が役立ちます。Gumloop は GLM-5.2 へ移した後、品質低下をほぼ感じずに credit 消費を約 50% 下げたと言っているからです。**

aronkor は、同じ harness と同じ prompt のまま、Gumloop で最も使われる agent 群を GLM 5.2 に置き換えた内部実験を説明しています。報告では、出力品質の差はほとんど気づかれず、credit 消費だけがほぼ半分になりました。

タイプ: 評価 | 日付: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (作者 [@KELMAND1](https://x.com/KELMAND1))

**このケースは、TDD、レビュー担当者のフィードバック、回帰チェックによる長時間にわたる自律的なフロントエンド リファクタリングのパターンとして使用してください。**

この投稿では、88 回のモデル回転と 102 回のツール呼び出しを含む、1 時間 42 分の GLM-5.2 リファクタリング タスクについて説明しています。ワークフローには、ハンドオフ、4 つのブロッカーの修正、12 のテストの TDD 実装、2 ラウンドの P2 修正、および最終回帰が含まれていました。

タイプ: デモ | 日付: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (作者 [@altudev](https://x.com/altudev))

**このケースを使用して、バグ修正と小規模な実装タスクのための OpenCode コーディング エージェントとして GLM-5.2 をテストします。**

著者は、6 つのバグ修正と OpenCode での 1 つの実装を含む GLM-5.2 のテストを報告し、変更は確実な計画と GLM-5.1 よりも速い速度できれいに完了したと述べています。

タイプ: デモ | 日付: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (作者 [@AskVenice](https://x.com/AskVenice))

**このチュートリアルを使用して、単一のプロンプトから GLM-5.2 と OpenCode を使用して小規模なゲームを構築し、モデルが実装の詳細をどのように処理するかを検査します。**

Venice は、GLM-5.2 と OpenCode を使用してレトロ ビデオ ゲームを構築するための完全なチュートリアルを共有し、これをプライベートなオープンソースの長期的なコーディング ワークフローとして位置づけました。

タイプ: チュートリアル | 日付: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**このケースを使用して、ライブラリを使用しない自己完結型 HTML5 物理シミュレーションで GLM-5.2 コードと Kim K2.7 コードを比較します。**

Atomic Chat は、両方のモデルにプールブレイク、スプリングブロック、ゴルトンボードのシミュレーションを構築するよう依頼したと報告しました。彼らの投稿によると、GLM-5.2 は 3 つすべてをより詳細かつ洗練して処理し、一方、キミは身体的動作に苦労していました。

タイプ: 評価 | 日付: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (作者 [@anshuc](https://x.com/anshuc))

**このケースを使用して、GLM-5.2 に洗練された個人サイトを求め、複数のターンで UI/UX がどの程度改善されるかを検証します。**

著者によると、GLM-5.2 は適切なプロンプトでプッシュされた後、クリエイティブな個人サイトを作成し、その結果のビデオを共有しました。これは、単発のベンチマーク要求ではなく、フロントエンド設計の反復に役立ちます。

タイプ: デモ | 日付: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (作者 [@laozhang2579](https://x.com/laozhang2579))

**このケースを使用して、PRD、時間予算、ステップ数、使用量割り当て、およびコード品質の比較を使用して製品構築タスクで GLM-5.2 を評価します。**

中国の投稿では、AI 契約レビュー製品 PRD で GLM-5.2、Kimi K2.7、および Claude Opus 4.8 を比較しています。ビルド時間、ステップ数、5 時間のクォータ使用量、コード品質スコアがレポートされます。

タイプ: 評価 | 日付: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (作者 [@zcode_ai](https://x.com/zcode_ai))

**このケースを使用して、大規模なエージェント開発タスクのために GLM-5.2 がどのように ZCode 3.0 に統合されるかを理解してください。**

ZCode は、コーディング プラン ユーザー向けの GLM-5.2 の提供、より強力なエージェント タスクの実行、より優れたロング コンテキスト コーディング、および計画から完了までのより大きな目標を管理するための目標機能を発表しました。

タイプ: 統合 | 日付: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [GLM-5.2 で構築された ZCode 用 Linux ラッパー](https://x.com/gosrum/status/2066484949755269510) (作者 [@gosrum](https://x.com/gosrum))

**このケースは、コーディング エージェント環境に関するツールを支援する GLM-5.2 の例として使用してください。**

著者は、GLM-5.2 と Claude Code を使用して zcode-linux を完成させ、Linux ユーザーが Linux 環境で ZCode を実行し、ローカル LLM エンドポイントを含む任意の API エンドポイントを追加できるようにしたと報告しています。

タイプ: デモ | 日付: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (作者 [@0xSero](https://x.com/0xSero))

**このケースを使用して、オープンソースのコンピューター使用リポジトリを再利用可能なスキルに変えるためのヘルパーとして GLM-5.2 を検討してください。**

この投稿では、GLM-5.2 がコンピューターの使用を設定し、高度なオープンソース リポジトリを見つけて、それをスキルに変換したと述べています。これは、ツールのラッピングとエージェントの統合作業のための実践的なシグナルです。

タイプ: デモ | 日付: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (作者 [@laogui](https://x.com/laogui))

**このケースを使用して、単一のチャット セッションではなく完全なエージェント開発環境内で GLM-5.2 を評価します。**

中国のレビューによると、ZCode 3.0 はシェルのような以前のバージョンから、GLM-5.2 と組み合わせた自社開発のエージェント コアに書き直され、国内のエージェント開発環境の中でより優れたエクスペリエンスを備えているとのことです。

タイプ: デモ | 日付: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [ローカルサービスを備えた OpenCode ハーネス](https://x.com/PatrickToulme/status/2068134212587184442) (作者 [@PatrickToulme](https://x.com/PatrickToulme))

**このケースを使用して、Claude Opus と比較する前に、OpenCode ハーネス、ローカル サービング、およびツールを多用するコーディング ワークフローを使用して GLM-5.2 をテストします。**

著者は、ローカル展開、ネストされたサブエージェント、調査/計画動作、および動作するアプリケーションのビルドを報告します。

タイプ: 評価 | 日付: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (作者 [@neural_avb](https://x.com/neural_avb))

**このケースを使用して、指示を RLM システム プロンプトに移動することで、GLM-5.2 のロング コンテキストのカウントと REPL エージェントの動作を改善します。**

リリース ノートでは、具体的なエージェント スキャフォールディングの変更と GLM-5.2 ロング コンテキスト ベンチマーク効果について説明しています。

タイプ: 統合 | 日付: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (作者 [@sydneyrunkle](https://x.com/sydneyrunkle))

**このケースを使用して、オープン コーディング エージェント ハーネスで GLM-5.2 を試し、再現可能なエージェント シェルでモデルを比較します。**

著者は、DeepAgents コードで GLM-5.2 を使用することを報告し、オープン モデルとオープン ハーネスをテスト パターンとして示しています。

タイプ: デモ | 日付: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [本番マーケティング agent stack のルーティング](https://x.com/DeRonin_/status/2068303752671477820) (作者 [@DeRonin_](https://x.com/DeRonin_))

**構造化、速度、self-hosting を重視する production agent workflow に GLM-5.2 を割り当てつつ、曖昧な判断はより強い closed model に任せるためのケースです。**

作者は agency stack で 6 日間の side-by-side run を行った後、GLM-5.2 は drift するまで 60 を超える agent step を維持し、800 回以上連続で structured format に一致し、低遅延の self-hosted response を返したと述べています。同じ投稿では voice が重要な task や曖昧な task では依然として Opus を好むとしており、その routing rule 自体が有用な takeaway です。

タイプ: 評価 | 日付: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (作者 [@hxiao](https://x.com/hxiao))

**M3 Ultra 上での長時間ローカル coding agent 実行において、GLM-5.2 を評価するためのケースです。約半日かけて Pokemon Red を HTML で再現しようとした実例を追えます。**

作者は Claude Code の model をローカル GLM 5.2 に差し替え、M3 Ultra 512GB マシンで 12 時間の `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` を実行しました。投稿では実行時間、token 使用量、code churn、RAM 使用量、GGUF と KV-cache 構成が共有されており、品質は frontier 級に感じる一方でローカル推論速度が主なボトルネックだと述べています。

タイプ: デモ | 日付: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (作者 [@cline](https://x.com/cline))

**実際のリポジトリのバグ修正で GLM-5.2 と Opus 4.8 を比較するためのケースです。GLM はより多くのトークンを使いましたが、より安価でクリーンな最終パッチを出しました。**

Cline は同じハーネスとツールの下で、Cline リポジトリの同一バグに対して両モデルをテストしました。投稿によれば、GLM は約 110 万トークン、Opus は 66 万トークンを使用し、コストは 0.41 ドル対 0.81 ドル、所要時間は 4.7 分と 28 回のツール呼び出し対 1.6 分と 12 回でした。さらに、GLM はデッドコードの整理と本番ビルド成功で終えた一方、Opus はテストは通ったものの型エラーを残しました。

タイプ: 評価 | 日付: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 Background Agent](https://x.com/colemurray/status/2069485572339707938) (作者 [@colemurray](https://x.com/colemurray))

**ホスト型チャットではなく、GLM-5.2 を FP8 で回すセルフホストの background-agent stack を調べるためのケースです。**

colemurray は、Modal Inference 上の OpenInspect を、GLM-5.2 を FP8 で動かす完全セルフホストの background agent system として共有し、重要なインフラに対する速度と制御性を強調しています。投稿自体は短いですが、使っているツールスタックとデプロイ形態を明確に示しています。

タイプ: 統合 | 日付: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [OpenCode と Fireworks へのコスト削減移行](https://x.com/SeekingN0rth/status/2071484711327985696) (作者 [@SeekingN0rth](https://x.com/SeekingN0rth))

**open-model harness への切り替えだけで十分か確かめたいならこの事例が役立ちます。作者は個人の coding と loop task を Fireworks 上の GLM-5.2 + OpenCode に移し、日常品質をほぼ保ったまま token コストが 3 分の 1 になったと言っているからです。**

SeekingN0rth は、個人の coding と loop task を週末のうちに Fireworks 上の GLM 5.2 + OpenCode へ移したことで、token 支出が約 3 分の 1 になったと述べています。投稿では、体験を決めたのは frontier かどうかより harness だとされており、OpenCode は terminal での Claude Code に近い感触で、日常タスクでは目立った品質低下もなかったといいます。この例は、コストを絶対的な SOTA より重視する大企業にも通じるモデル切り替えパターンとして語られています。

タイプ: 評価 | 日付: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA の GLM アグリゲーターワークフロー](https://x.com/IBuzovskyi/status/2071601107944571249) (作者 [@IBuzovskyi](https://x.com/IBuzovskyi))

**価値の高い agent の 1 ターンに追加のオーケストレーションをかける価値があるなら、この事例が役立ちます。Hermes Agent の Mixture of Agents 構成は、GLM-5.2 と他モデルを組み合わせ、小さな追加コストで目に見えて良い出力を出したからです。**

IBuzovskyi は Hermes Agent の Mixture of Agents モードを、ツールアクセスを持つ 1 つのアグリゲーターモデルと、私的な助言だけを返す複数の参照モデルの組み合わせとして説明しています。投稿では、GLM 5.2 単体だと 13 分・0.38 ドルだった coding テストが、GLM 5.2 をアグリゲーターにして Kimi K2.6 と MiniMax M3 を組み合わせると 35 分・0.47 ドルになった一方で、アニメーション、ビジュアル、ゲームメカニクスはより良くなったと報告しています。プリセット設計、機能の有効化場所、追加レイテンシを許容すべき場面も整理されています。

タイプ: 統合 | 日付: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline の推論オン/オフによるハーネス差分](https://x.com/akshay_pachaar/status/2071638409022763292) (作者 [@akshay_pachaar](https://x.com/akshay_pachaar))

**モデルの重みだけでなく harness 設計を見たいならこの事例が役立ちます。同じ GLM-5.2 が同じ coding task で、reasoning を有効にしただけで 57.3% から 68.5% に伸びたからです。**

akshay_pachaar は、同じ GLM 5.2 に同じ coding task 群を与えた Cline のテストを引用しています。reasoning をオフにすると 57.3%、オンにすると 68.5% でした。この差を使って投稿は、出力が単なるテキストではなく出荷可能なコードになるかどうかは、コンテキスト保持、ツール利用、編集適用、検証ループが基盤モデルと同じくらい重要だと論じています。

タイプ: 評価 | 日付: 2026-06-29

<a id="case-136"></a>
### Case 136: [Cursor + Fireworks 455M-Token Field Test](https://x.com/robinebers/status/2071246749210190132) (作者 [@robinebers](https://x.com/robinebers))

**高速な Fireworks 提供と 4.55 億 tokens の実運用を作者が報告しており、すぐに Opus や GPT-5.5 に戻る気がないとしているため、GLM-5.2 を Cursor の本格的な常用モデルとして判断するためのケースです。**

robinebers は、Cursor で GLM 5.2 に切り替えて 36 時間使ったことで、このモデルへの見方が Fireworks と組み合わせた時点で大きく変わったと述べています。投稿では、image support、ゼロデータ保持の主張、毎秒約 80-100 tokens の throughput、そして 4 億 5500 万 tokens に対して約 145 ドルかかった点を具体的に挙げています。汎用的な benchmark 賞賛よりも、provider の選択が実運用体験を変えることを示す、harness 固有の強い評価例です。

タイプ: Evaluation | 日付: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Devin Desktop Harness With Skill Portability](https://x.com/lily_gpupoor/status/2071297351801794850) (作者 [@lily_gpupoor](https://x.com/lily_gpupoor))

**Z.ai 自身の coding surface が不安定に感じられるときに、GLM-5.2 を Devin Desktop 内で試すためのケースです。作者は、より簡単な skill 移植、高速さ、そして hackability の高さを報告しています。**

lily_gpupoor は、API が不安定だった時期に、Devin Desktop 経由で大量に使った GLM-5.2 の体験が、Z.ai の直接の coding plan より明確に良かったと述べています。投稿では、custom Solarized Green theme の JSON を GLM が編集して extension の登録まで成功したこと、Devin が異様に速く感じられたこと、そして既存の skill の大半がデフォルトの Windsurf Cascade agent から Devin Local へ切り替えてもそのまま移植できたこと、という 3 つの具体的な workflow 上の利点が挙げられています。

タイプ: Evaluation | 日付: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi インライン GLM レビュアー](https://x.com/xpasky/status/2070831715518460177) (作者 [@xpasky](https://x.com/xpasky))

**Pi スタイルの coding-agent loop に第 2 のレビュー担当を加えたいときに使うケースです。作者によれば、GLM-5.2 は Opus に turn ごとに助言でき、コスト増はおよそ 10% に収まるとのことです。**

xpasky は、チームが GLM-5.2 を Pi workflow の第 2 レビュアーとして使っており、1 つの Opus がコーディングし、もう 1 つの Opus が難題を解き、その横で GLM が turn ごとに Opus へ助言していると述べています。投稿では、この reviewer を追加してもコスト増は約 10% にとどまり、これまでで最良の code が得られているとも評価しています。

タイプ: 統合 | 日付: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter による一発 Telegram Bot](https://x.com/MatinSenPai/status/2070259817818812701) (作者 [@MatinSenPai](https://x.com/MatinSenPai))

**最低限動くだけのコードではなく、本番運用を意識した default を GLM-5.2 が one-shot の coding-agent build で自力推論できるか試すためのケースです。**

MatinSenPai は、動画と同じ prompt から GLM 5.2 で Telegram bot を one shot で作ったと報告し、頼んでいない実務的な配慮までモデルが自動で入れたと述べています。投稿では、動画送信後の自動ファイル削除、Telegram Bot API のサイズ制限を踏まえたデフォルト 50MB cap、完了前の繰り返し self-test、以前の MiMo build よりきれいな structure、そして AgentRouter 経由で約 140K tokens、概算 5 ドル程度の利用が挙げられています。

タイプ: デモ | 日付: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go リファクタリング初回成功](https://x.com/vedovelli74/status/2069889605969592500) (作者 [@vedovelli74](https://x.com/vedovelli74))

**ベンチマーク主張だけに頼らず、OpenCode 内の中規模 Go リファクタリングで GLM-5.2 を評価するためのケースです。**

vedovelli74 は、中規模の GoLang コードベースを対象にした最初の OpenCode 実行を報告し、GLM-5.2 は Opus 4.8 より高速で、トークン効率も高く、何をリファクタリングすべきかを初回判断で正しく見抜いたと述べています。さらに、その結果は後から Codex と Opus でも検証され、それでも納品品質では GLM-5.2 が上回ったとしています。

タイプ: 評価 | 日付: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 3.36ドル常用実行](https://x.com/clairevo/status/2069828122640548204) (作者 [@clairevo](https://x.com/clairevo))

**より自律的な coding work を open weights に移す前に、Claude Code と Cursor で日常利用モデルとしての GLM-5.2 を見極めるためのケースです。**

clairevo は、GLM 5.2 が Claude Code と Cursor におけるデフォルトモデルになっており、ここまでの利用コストは 3.36 ドルだと述べています。投稿では、Opus に近い coding quality を感じたことに加え、OpenRouter 経由のセットアップ経路、フロントエンドのデザイン感、長時間の autonomous task に関する評価が、常用モデルとして採用した理由だと説明しています。

タイプ: 評価 | 日付: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 実演デモとショーケースビルド
<a id="case-161"></a>
### Case 161: [REAP NVFP4 Rubiks Cube One-Shot](https://x.com/RoundtableSpace/status/2072700573145788914) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**このケースは、単一プロンプトの対話型 build で GLM-5.2 を試すのに向いています。REAP-NVFP4 の demo では、1 回の prompt だけで 3D Rubiks Cube、実際の scramble、live state、solve button まで生成したと述べています。**

RoundtableSpace によると、GLM-5.2-REAP-NVFP4 には HTML prompt を 1 つだけ渡し、live state、real scramble logic、solve action を備えた 3D Rubiks Cube app が返ってきました。コード詳細は薄いものの、generic な benchmark screenshot ではなく、具体的な one-shot build demo です。

タイプ: デモ | 日付: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP Relay iPhone Client](https://x.com/mov_axbx/status/2072192903762288721) (作者 [@mov_axbx](https://x.com/mov_axbx))

**このケースは、ローカル GLM-5.2 エージェントを素早くモバイル面に載せたいときに使えます。著者によれば、Codex の build-ios-app plugin が、すでに GLM-5.2 と Cloudflare トンネルを使う OMP relay 向けに、数時間で整った iPhone クライアントを作りました。**

mov_axbx は、ローカルホストの OMP エージェント向けに電話アプリが欲しくなり、Codex の build-ios-app plugin を使って数時間で整った版を得たと言っています。バックエンド側は GLM-5.2 と OMP で書かれた custom relay を使い、トンネルは Cloudflare が担っていました。

タイプ: デモ | 日付: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [オープンソースの DevRel リサーチエージェント](https://x.com/Astrodevil_/status/2071572680470655253) (作者 [@Astrodevil_](https://x.com/Astrodevil_))

**GLM-5.2 を汎用チャットではなく縦型の調査アシスタントに変えたいならこの事例が役立ちます。作者は、製品とオーディエンスの入力を根拠付きのコンテンツ候補とアウトラインに変えるオープンソース DevRel エージェントを作ったからです。**

Astrodevil_ は GLM-5.2 上に、製品とターゲットの説明を受け取る chat-first の DevRel 調査アプリを構築しました。Hacker News から需要シグナルを探し、DEV のコンテンツギャップを調べ、Engram memory で事実を更新し、根拠付きで優先順位付けされたトピック案とアウトラインを返します。投稿では Agno、Weaviate Engram、Nebius inference、そしてオープンソースのコードベースも明示しています。

タイプ: デモ | 日付: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 6 バリエーションの LP 反復ループ](https://x.com/nutlope/status/2070199649818779914) (作者 [@nutlope](https://x.com/nutlope))

**まず複数の GLM-5.2 案を作ってから最良案を coding agent に引き継ぎ、低コストで landing page を試作するためのケースです。**

nutlope は、GLM 5.2 と Recast を使った web iteration workflow を説明しています。1 つの prompt から landing page を 6 variations 生成し、最も良い design を選び、その code をダウンロードして別の coding agent で反復を続ける流れです。投稿では、GLM-5.2 は fast で cheap かつ design に強いためこの用途に向いており、同じ予算で Opus 4.8 の 1 ページに対して GLM では 3〜6 案ほど作れることが多いと述べています。

タイプ: チュートリアル | 日付: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (作者 [@aimlapi](https://x.com/aimlapi))

**このケースを使用して、GLM-5.2 と Opus 4.8 の間で同じプロンプトのゲーム構築の出力、ランタイム、コストを比較します。**

AI/ML API は、GLM-5.2 および Opus 4.8 に、プレイ可能なバックルーム ゲームをワンショットで実行するよう要求すると報告しました。彼らの投稿によると、GLM-5.2 はより充実した機構を 1:08 で 0.37 ドルで構築したが、Opus は 2:14 で 1.94 ドルかかったという。

タイプ: デモ | 日付: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [結果がまちまちの 3 つの実際のビルド](https://x.com/bridgemindai/status/2065840871929442319) (作者 [@bridgemindai](https://x.com/bridgemindai))

**このケースは、注意深いデモ セットとして使用してください。実稼働ゲームやビデオ タスクのモデルを信頼する前に、複数の実際のビルドをテストしてください。**

BridgeMind は、ホラー ハウス ゲーム、3D ステルス ゲーム、およびリモート マーケティング ビデオで GLM-5.2 をテストしました。この投稿では、壊れたゲーム ロジックを含むさまざまな結果が報告されており、根拠のある制限信号として役立ちます。

タイプ: 評価 | 日付: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースを使用して、いくつかの修正と機能のパスにわたって GLM-5.2 と ZCode を使用した反復的なゲーム構築を評価します。**

著者は、スーパー マリオ スタイルのクローンを作成して GLM-5.2 で ZCode 3.0 をテストし、問題修正と機能追加を 5 回繰り返した後に結果を共有しました。

タイプ: デモ | 日付: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**このケースを使用して、インタラクティブなゲーム スタイルのタスクで GLM-5.2、MiniMax M3、および Kim K2.7 コードを比較します。**

この投稿では、ローカル モデルの開発に戻る前の実用的なベンチマークとしてビデオ結果を使用して、MiniMax M3、GLM-5.2、および Kim K2.7 コード間の月着陸船コンテストについて説明しています。

タイプ: 評価 | 日付: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (作者 [@grx_xce](https://x.com/grx_xce))

**このケースを使用して、GLM-5.2 がアリーナ コンテキスト内の単一のデザイン プロンプトから何を生成できるかを検査します。**

著者は、デザイン アリーナで 1 つのプロンプトから作成された GLM-5.2 作成の例を共有し、それを使用してオープン ウェイト モデルとクローズド ウェイト モデル間のギャップが縮まっていることを示しました。

タイプ: デモ | 日付: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [研究論文のワークフローを理解する](https://x.com/askalphaxiv/status/2066996976445706745) (作者 [@askalphaxiv](https://x.com/askalphaxiv))

**このケースを使用して、状況に応じた質問や論文間の参照を含む論文読書ワークフローに GLM-5.2 を適用します。**

AlphaXiv は、研究論文を理解するために GLM-5.2 を導入しました。ユーザーはセクションを強調表示したり、質問したり、文脈、比較、ベンチマークの参考として他の論文を参照したりできます。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (作者 [@emollick](https://x.com/emollick))

**GLM-5.2 を寓話スタイルのモデルと比較する場合は、このケースを使用して、正確性とクリエイティブの品質を区別します。**

Ethan Mollick 氏は、GLM-5.2 Max が正しい制約のある詩を生み出したことを認め、一方で、Fable は消える文字の制約をより創造的に詩のテーマに組み込んだと指摘しました。

タイプ: 評価 | 日付: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (作者 [@0xSero](https://x.com/0xSero))

**このケースを軽量のビジュアル デザイン シグナルとして使用し、独自のプロンプトと UI レビューで検証します。**

著者は、GLM-5.2 のデザインセンスを気に入って、視覚的な例を共有したと述べています。これは、生産設計品質の独立した証拠としてではなく、検査の指針として役立ちます。

タイプ: デモ | 日付: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 風ボクセルゲームのワンショット生成](https://x.com/pseudokid/status/2068431546143649829) (作者 [@pseudokid](https://x.com/pseudokid))

**単一プロンプトのゲーム生成で GLM-5.2 を stress-test し、視覚的にリッチなビルドで何が追加修正を要するかを確認するためのケースです。**

作者は、Temple Run に着想を得た voxel biker game の大半を 1 ターン目で作れたと述べ、その後 camera と movement の修正のために数回の follow-up を行ったと報告しています。さらに、この投稿では Z.ai の tooling が screenshot と gameplay video を生成し、text model が結果を評価する助けになるとも述べられています。

タイプ: デモ | 日付: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go ワンショット実例セット](https://x.com/LyalinDotCom/status/2068378281636982990) (作者 [@LyalinDotCom](https://x.com/LyalinDotCom))

**より open-ended な agent loop に投入する前に、OpenCode Go 内の quick one-shot build で GLM-5.2 を benchmark するためのケースです。**

作者は、OpenCode Go を通じて solar-system web app、system-info Electron app、simple explore-island web game にわたる one-shot 例を報告しています。同じ投稿では、GLM-5.2 はこれまで使った中で最高の open model だとしつつ、frontier-equal と断言することは避けています。

タイプ: デモ | 日付: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (作者 [@DeryaTR_](https://x.com/DeryaTR_))

**単一プロンプトのゲーム生成で GLM-5.2 を試し、その後の数回の追加入力で asset 差し替えや軽い polish がどう進むかを見るためのケースです。**

作者は GLM-5.2 が 1 つのメインプロンプトから遊べる Space Invaders 風ゲームを作り、その後 3 回の追加プロンプトで sprite 差し替えや leaderboard などの小さな追加を行ったと報告しています。公開結果は軽量なゲーム生成例として有用ですが、完全な benchmark ではありません。

タイプ: デモ | 日付: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (作者 [@threepointone](https://x.com/threepointone))

**対話的な agent failure simulation を素早く試作するためのケースです。作者は約 3.50 ドルで動く recovery lab を one-shot で作れたと報告しています。**

作者は 4,000 語の分析と Agents SDK repository を渡した後、OpenCode と GLM-5.2 で完全に操作可能な recovery lab を構築しました。投稿では 176k tokens の実行、one-shot の成功、polish 前で約 3.50 ドルという end-to-end cost が示されています。

タイプ: デモ | 日付: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (作者 [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**参照ベースの Web 再現で GLM-5.2 を試すためのケースです。1 つのプロンプトと元 URL だけで、ほぼピクセルレベルの忠実さでサイトを再現しました。**

Open Design は、組み込みの AMR で参照 URL と簡単な 1 つのプロンプトだけを使って GLM-5.2 をテストし、デモではウェブサイトをほぼ完璧に再現したと述べています。完全なベンチマークではなく、参照ベース UI 生成の実演的な証拠として扱うべきケースです。

タイプ: デモ | 日付: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**フルスタック UI 構築で GLM-5.2 を比較するためのケースです。最も洗練された取引デスク出力にかなり近づきながら、コストはそのごく一部に収まりました。**

Atomic Chat は、フロントエンド、バックエンド、8 銘柄の市場データ、カスタムのダークテーマ UI を含む同一の Trader Desk ビルドプロンプトで 4 つのモデルを比較しました。投稿によると、GLM-5.2 は 13,677 トークンで 0.03 ドル、Fugu Ultra は 22,225 トークンで 0.51 ドルでした。GLM は、はるかに低コストで、ライブデータ付きの同程度に完成したマルチパネル UI を出力したとされています。

タイプ: 評価 | 日付: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Luddite Game After Claude Refusal](https://x.com/atmoio/status/2069559053114577088) (作者 [@atmoio](https://x.com/atmoio))

**クローズドモデルが拒否したゲーム案を GLM-5.2 で代替試作し、実際に動く出力を自分で検証するためのケースです。**

atmoio は、AI を破壊する Plague Inc 風のユーモアゲームが Claude で利用規約違反と判定されたため、代わりに GLM 5.2 で Luddite を制作し、デモ動画も添付したと述べています。ポリシー上の理由でクローズドモデルが拒否しがちな creative coding task に対する実地の代替例として扱えます。

タイプ: デモ | 日付: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 プロバイダ・ツール統合
<a id="case-165"></a>
### Case 165: [ZCode Launch With Mobile Agent Control](https://x.com/Digiato/status/2072663459850829985) (作者 [@Digiato](https://x.com/Digiato))

**このケースは、ZCode を GLM-5.2 の公式 coding surface として評価するのに役立ちます。launch report では、この無料の agentic IDE が Windows、macOS、Linux で動き、Telegram、WeChat、Feishu から project progress を確認できるとされています。**

Digiato は、ZCode を GLM-5.2 を中心に構築された無料の agentic development environment と説明し、Cursor、Claude Code、Copilot の対抗軸として位置付けています。投稿では、Windows、macOS、Linux で提供され、GLM-5.2 と深く統合され、Telegram、WeChat、Feishu から進捗を確認できると述べています。単なる model launch よりも実務的な access surface です。

タイプ: 統合 | 日付: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki Auto-Maintained Agent Docs](https://x.com/LangChain/status/2072745455788933321) (作者 [@LangChain](https://x.com/LangChain))

**このケースは、agent が読めるドキュメントを自動で最新化したいときに役立ちます。LangChain によると、OpenWiki はコード変更に合わせて repo docs を再生成・維持し、GLM 5.2 のような open model で動きます。**

LangChain は OpenWiki を coding agent 向けの open-source ドキュメント保守レイヤーとして紹介しています。投稿では、open harness と open CLI workflows を組み合わせ、codebase が変わるたびに docs を更新し、GLM 5.2 や Kimi K2.7 のような open model で動くと説明しています。手動 wiki に頼らず、agent に新しい repo docs を読ませたいチーム向けの実用的な file-based memory パターンです。

タイプ: 統合 | 日付: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [Foundry PTUs Through FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**このケースを使えば、エージェント用クライアントを書き直さずに企業向け Foundry 予算で GLM-5.2 を流せます。Fireworks によれば、FireConnect が Microsoft Foundry の PTU を Codex、OpenCode、Pi のフローにつなぐからです。**

Fireworks によると、GLM 5.2 は Microsoft Foundry で利用可能です。FireConnect を有効にすると、チームは Foundry の PTU を使いながら、Codex、OpenCode、Pi からそのままリクエストを流せます。エージェント面ごとに別のアクセス経路を立てる必要はありません。

タイプ: 統合 | 日付: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM Eval Workbench](https://x.com/ankrgyl/status/2072042305108722040) (作者 [@ankrgyl](https://x.com/ankrgyl))

**GLM-5.2 と Opus を同じ eval スタックで比べたいならこの事例が役立ちます。Braintrust と Baseten が、long-context の精度とコスト差を具体例つきで公開したからです。**

ankrgyl は、Braintrust が Baseten 対応付きで GLM-5.2 を追加し、チームが eval と production trace の両方で回せるようにしたと述べています。公開例では 25K / 50K token の long-context retrieval を比較し、Opus 4.8 は約 3.5 ポイント上回る一方で trace あたり 4.1 倍から 4.5 倍ほど高いとされています。

タイプ: 統合 | 日付: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass のオープンウェイト定額購読](https://x.com/iam_elias1/status/2071655509611151674) (作者 [@iam_elias1](https://x.com/iam_elias1))

**複数のオープンウェイト coding model を 1 つの agent harness にまとめたいならこの事例が役立ちます。ClinePass は GLM-5.2 と関連モデルを、個別の provider key や請求管理ではなく月額固定で束ねているからです。**

iam_elias1 は ClinePass を、GLM-5.2、DeepSeek、Kimi、Qwen、MiniMax、MiMo などのオープンウェイトモデルを Cline の IDE 拡張と CLI で使える月額 9.99 ドルの導線として紹介しています。投稿によれば、provider ごとの API key を置き換え、標準 API 制限の 2-5 倍を使え、作業フェーズごとにセッション途中でモデルを切り替えられ、CLI 経由の登録なら初月は 1.99 ドルです。

タイプ: 統合 | 日付: 2026-06-29

<a id="case-137"></a>
### Case 137: [Free GLM API Service For Coding Agents](https://x.com/mcwangcn/status/2071261128575897901) (作者 [@mcwangcn](https://x.com/mcwangcn))

**登録なしで Hermes や他の coding agent で GLM-5.2 を試すためのケースです。共有サービスは短時間有効な API key を発行し、セットアップを軽量に保ちます。**

mcwangcn は、signup も login も不要で、Lobster、Hermes、そのほかの coding agent から利用できる無料の GLM-5.2 API service を共有しています。同じ投稿では、生成された各 API key は更新前に 1 時間だけ有効だと説明しており、これは具体的な anti-abuse 制約です。そのため、この service は unattended な長期本番運用よりも、素早い workflow テスト向きだと考えるべきです。

タイプ: Integration | 日付: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (作者 [@opencode](https://x.com/opencode))

**このケースを使用して、テキスト、1M コンテキスト、GLM-5.1 のような価格設定を使用して OpenCode Go ワークフロー内で GLM-5.2 の可用性を追跡します。**

OpenCode は、Go での GLM-5.2 の利用可能性を発表し、テキストのサポート、1M コンテキスト ウィンドウ、および 5.1 と同じ価格を強調しました。

タイプ: 統合 | 日付: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (作者 [@ollama](https://x.com/ollama))

**このケースを使用して、アクセス可能なオープンソースのコーディング モデル実験のために GLM-5.2 を Ollama Cloud にルーティングします。**

Ollama は GLM-5.2 の提供を発表し、これを 1M コンテキストを備えた長期コーディングおよびエージェント タスク モデルとして説明しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (作者 [@OpenRouter](https://x.com/OpenRouter))

**プロバイダー ルーティングまたはマルチモデル スタックを比較する場合は、OpenRouter 経由で GLM-5.2 にアクセスする場合にこのケースを使用します。**

OpenRouter は、1M トークンのロングホライズン モデルとして GLM-5.2 が利用可能になることを発表し、ユーザーにそれを呼び出すためのプロバイダー中立のパスを提供しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (作者 [@vllm_project](https://x.com/vllm_project))

**このケースを使用して、デイゼロ サポートを備えた vLLM を介して GLM-5.2 をセルフホストまたは提供します。**

vLLM プロジェクトは、v0.23.0 での GLM-5.2 サポートを発表し、これを 1M コンテキストのロングホライズン コーディング エージェントの主力モデルとして位置づけました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (作者 [@NotionHQ](https://x.com/NotionHQ))

**このケースを使用して、Notion ワークフロー内で利用可能なオープンウェイト モデルとして GLM-5.2 を識別します。**

Notion は、長期タスク向けに構築され、Baseten 経由で提供されるオープンウェイト モデルとして GLM-5.2 が提供されることを発表しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (作者 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**このケースを使用して、ホスト型インフラストラクチャを必要とする GLM-5.2 ワークロードのサービス提供ルートとして Fireworks を評価します。**

Fireworks は、1M コンテキスト、コーディングファーストの位置付け、SWE ベンチ、ターミナル ベンチ、GPQA、および AIME での独立した検証を強調して、GLM-5.2 を 0 日目にライブで発表しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Google Cloud モデル ガーデン リンク](https://x.com/CarolGLMs/status/2067127223216419088) (作者 [@CarolGLMs](https://x.com/CarolGLMs))

**このケースを使用して、Google Cloud 指向のデプロイメントおよびエージェント プラットフォームのコンテキストで GLM-5.2 を見つけます。**

CarolGLM は GLM-5.2 の Google Cloud リンクを共有し、クラウド モデル カタログを使用して作業するチームへの直接の指針としました。

タイプ: 統合 | 日付: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (作者 [@AskVenice](https://x.com/AskVenice))

**プライバシー モード、TEE、またはエンドツーエンド暗号化が GLM-5.2 を試行する際の決定要因となる場合は、このケースを使用してください。**

Venice は、プライベート エージェント コーディングと長期にわたるタスクを目的とした、TEE/E2EE フレーミングによるプライバシー モードでの GLM-5.2 の利用可能性を発表しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**このケースを使用して、低コストのエントリー プランとロング コンテキスト コーディング機能を備えたコマンド コードで GLM-5.2 を試してください。**

Command Code は、100 万のコンテキスト、強力な推論、オープンソースのステータス、および 1 ドルの Go プランによるアクセスを指摘して、GLM-5.2 の提供を発表しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [ヌースポータルのヘルメスエージェント](https://x.com/Teknium/status/2066954081575592282) (作者 [@Teknium](https://x.com/Teknium))

**このケースを使用して、Nous Portal および OpenRouter を介して GLM-5.2 を Hermes Agent ワークフローに接続します。**

Teknium は、Nous Portal および OpenRouter の Hermes Agent で GLM-5.2 が利用可能であることを報告しました。これは、エージェント フレームワークのルーティング実験に役立ちます。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (作者 [@ionet](https://x.com/ionet))

**753B パラメータのロングコンテキスト モデルのコンピューティング支援型サービスを評価する場合は、このケースを使用してください。**

io.net は、1M コンテキスト、エージェントファースト設計、ロングホライズンコーディング、および 753B パラメータモデルのコンピューティングニーズを強調して、GLM-5.2 のデイゼロローンチパートナーであることを発表しました。

タイプ: 統合 | 日付: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (作者 [@clattner_llvm](https://x.com/clattner_llvm))

**このケースを使用して、プロバイダー規模でサービスを提供するロングコンテキスト GLM-5.2 のモジュラー クラウドを検討してください。**

Chris Lattner 氏は、GLM-5.2 が初日から Modular Cloud 上で稼働し、オープン ウェイト、コーディング、ロングホライズン エージェント、および 1M コンテキストを強調していると投稿しました。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (作者 [@agentnative_](https://x.com/agentnative_))

**このケースを使用して、低コストのオープン モデル コーディング ワークフローのために OpenRouter を介して Cursor で GLM-5.2 を構成します。**

ソースは、モデルの可用性を発表するだけでなく、具体的な Cursor/OpenRouter セットアップ パスを提供します。

タイプ: チュートリアル | 日付: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (作者 [@beyang](https://x.com/beyang))

**テキストのみのモデルでデザイン タスクのビジュアル レビュー サポートが必要な場合は、このケースを使用して GLM-5.2 と Amp カスタム エージェントを組み合わせます。**

この投稿では、GLM-5.2 ビジュアル デザイン ベンチマーク結果を、レビュー レイヤーを提供できる Amp プラグイン エージェントと接続します。

タイプ: 統合 | 日付: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (作者 [@alphatozeta8148](https://x.com/alphatozeta8148))

**Factory Droid、OpenCode、およびコーディング ハーネスでロング コンテキストの処理速度が重要な場合は、このケースを使用して GLM-5.2 を Baseten 経由でルーティングします。**

ソースでは、GLM-5.2 がフル 1M コンテキストで 4 倍高速に動作していると報告しており、コーディング ハーネスでそれを示しています。

タイプ: 統合 | 日付: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [Web デザイン向け Browser Use QA subagents](https://x.com/browser_use/status/2068405699340853541) (作者 [@browser_use](https://x.com/browser_use))

**text-only model に視覚確認が必要なとき、GLM-5.2 を Browser Use v2 の multimodal QA subagents と組み合わせ、反復的な website 修正に使うためのケースです。**

Browser Use は、GLM-5.2 が website design task で Fable 5 を上回り、その後 result を inspection し、美観を判断し、bug を見つけ、targeted fix を GLM に返す QA subagents を追加したと報告しています。build と QA を含む全体ループのコストは $0.75 未満だったとされています。

タイプ: 統合 | 日付: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 公式 IDE の daily free tokens](https://x.com/Alan_Earn/status/2068223665268006924) (作者 [@Alan_Earn](https://x.com/Alan_Earn))

**大きな daily token allowance と Cursor 風 workflow を備えた無料の公式 coding IDE として、ZCode 経由で GLM-5.2 にアクセスするためのケースです。**

この投稿では、ZCode を Zhipu の公式 coding IDE と説明し、GLM-5.2 を default model、1 日 300 万 token、1M context、Mac/Windows client を備えると紹介しています。短い setup flow も含まれており、単なる launch announcement より実用的です。

タイプ: チュートリアル | 日付: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (作者 [@skirano](https://x.com/skirano))

**Fireworks 経由で GLM-5.2 を Cursor に最小構成で接続し、独自クライアントコードなしで試すためのケースです。**

Skirano は Cursor の OpenAI API key 欄に Fireworks key を貼り、base URL に `https://api.fireworks.ai/inference/v1` を使い、model として `accounts/fireworks/models/glm-5p2` を選んで再起動する最小セットアップを示しています。GLM-5.2 を慣れた coding IDE で試す具体的な導線です。

タイプ: チュートリアル | 日付: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (作者 [@vulcanbench](https://x.com/vulcanbench))

**専用の ZAI provider 対応と API key 導線を備えたオープン benchmark harness で GLM-5.2 を走らせるためのケースです。**

VulcanBench v0.2.0 は first-class の ZAI support を追加し、GLM-5.2 を `zai:glm-5.2` として OpenAI や Anthropic model と並べて実行できるようにしました。専用の `ZAI_API_KEY` も用意されており、単発 screenshot ではなく開かれた benchmark harness を求める人に向いています。

タイプ: 統合 | 日付: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (作者 [@OpenCodeLog](https://x.com/OpenCodeLog))

**OpenCode 内で GLM-5.2 の High / Max reasoning variant にアクセスしつつ、より安定した step-limit 処理も取り込むためのケースです。**

OpenCode v1.17.9 は GLM-5.2 の High / Max thinking variant を OpenAI 互換および Anthropic 互換 provider で追加し、OpenRouter の effort mapping も native に扱えるようにしました。同じ release では agent step-limit の挙動も修正されており、長めの実行でより実用的になっています。

タイプ: 統合 | 日付: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**GLM-5.2 の coding plan トラフィックを、汎用 API ではなく coding 最適化済みの Z.ai endpoint に向けるためのケースです。**

この投稿では coding plan workload 向けに、一般的な `https://api.z.ai/api/paas/v4/` ではなく `https://api.z.ai/api/coding/paas/v4` を使うよう案内しています。また、Claude Code や OpenCode が対応している場合は `https://api.z.ai/api/anthropic` を使うことが多いとも述べています。GLM-5.2 が misroute されていると感じるときの具体的な設定修正です。

タイプ: チュートリアル | 日付: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (作者 [@0x_kaize](https://x.com/0x_kaize))

**無料の GLM-5.2 API key と base URL を取得し、Claude、Cursor、Hermes などに差し込むためのケースです。**

作者は 5 分程度で無料の ZenMux API key と base URL を取得し、GLM-5.2 を Claude、Cursor、Hermes などに接続する流れを共有しています。一方で無料 tier はすぐ rate-limit に達すると書かれており、永続的な保証というより access note として使うのが適切です。

タイプ: チュートリアル | 日付: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (作者 [@_xjdr](https://x.com/_xjdr))

**標準エンドポイントと 1M コンテキスト用エンドポイントを分け、デフォルトモデル対応も備えた ncode と Noumena 系エージェント環境に GLM-5.2 を組み込むためのケースです。**

Noumena の更新では、チームがツール呼び出し、関数解析、アプリのルーティング、推論トレース全体で GLM を第一級対応にしたと説明しています。さらに、1M コンテキストの高負荷トラフィック下で TTFT を制御するため、API を `glm-5.2` と `glm-5.2[1m]` に分離しました。加えて、新しい ncode ビルドでは、利用者の反応が良かったため opus 級のデフォルトモデルを Kimi から GLM に切り替えたとも述べています。

タイプ: 統合 | 日付: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (作者 [@thealexker](https://x.com/thealexker))

**Baseten のキー、カスタム base URL、`~/.claude/settings.json` のモデル再マッピングを使って Claude Code 内で GLM-5.2 を動かすためのケースです。**

このチュートリアルでは、Claude Code のインストール、Baseten アカウントの作成、API キーの取得、そして `~/.claude/settings.json` の編集手順を説明しています。3 つの Claude モデル階層すべてを、カスタム Anthropic 環境変数を通して `zai-org/GLM-5.2` に向ける構成です。Claude Code クライアントで GLM-5.2 を使うための具体的な差し替え設定パターンです。

タイプ: チュートリアル | 日付: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (作者 [@cramforce](https://x.com/cramforce))

**セキュリティハーネス内で GLM-5.2 を試すためのケースです。`deepsec` は Pi agent のデフォルトモデルに採用し、競争力のある eval 結果を報告しました。**

この投稿は、`@badlogicgames` の Pi agent に対する `deepsec` 対応を告知し、GLM-5.2 をデフォルトモデルに設定したうえで、`pnpm deepsec process --agent pi` という実行可能コマンドを示しています。さらに著者は Deepsec evals を実行し、他のフロンティアモデルと比べても競争力があったと述べており、セキュリティ指向の具体的な統合面となっています。

タイプ: 統合 | 日付: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid Harness Quickstart](https://x.com/RayFernando1337/status/2069523126384525639) (作者 [@RayFernando1337](https://x.com/RayFernando1337))

**Baseten と Droid harness 経由で GLM-5.2 を素早く動かし、他の IDE にも流用できる短いセットアップ手順を得るためのケースです。**

RayFernando1337 は、Baseten API key の取得、Droid AI 設定の自動化、GLM-5.2 統合のテスト、代替セットアップと制約の確認、さらに他 IDE 向けの補足セットアップまで、タイムスタンプ付きで手順をまとめています。

タイプ: チュートリアル | 日付: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI-Compatible GLM API Workflow](https://x.com/Marktechpost/status/2069308807570915500) (作者 [@Marktechpost](https://x.com/Marktechpost))

**reasoning control、tool calling、長文脈 retrieval、cost tracking を備えた OpenAI 互換 GLM-5.2 クライアントを Python で組むためのケースです。**

Marktechpost は、GLM-5.2 を 1 つの OpenAI 互換クライアントで扱うチュートリアルとコード notebook を共有しています。投稿によると、thinking effort の制御（`off` / `high` / `max`）、reasoning と answer のストリーム分離、multi-step agent の tool calling、structured JSON output、long-context retrieval、token cost tracking まで含まれています。

タイプ: チュートリアル | 日付: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API Search Sandbox](https://x.com/perplexitydevs/status/2069252848647606584) (作者 [@perplexitydevs](https://x.com/perplexitydevs))

**search 対応の sandboxed agent を単一 API call で使いたいとき、Perplexity Agent API に GLM-5.2 を接続するためのケースです。**

Perplexity Devs は、GLM-5.2 を Agent API に追加し、長期の coding や agentic workflow と相性が良いと説明しています。投稿では Search as Code、OpenAI 互換インターフェース、そしてマークアップなしの first-party pricing を特に強調しています。

タイプ: 統合 | 日付: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (作者 [@aqaderb](https://x.com/aqaderb))

**プロバイダー遅延が重要なとき、Baseten が主張する GLM-5.2 の高速 serving を確認するためのケースです。sub-second の first-token time と高い decoding throughput が示されています。**

aqaderb は、Baseten の GLM-5.2 API が 1 秒未満の TTFT と毎秒 280 tokens を達成したと発表しています。投稿では、その理由として PD disaggregation、multi-token prediction heads を使った speculative decoding、KV-cache-aware routing などの serving 最適化を挙げ、関連する engineering write-up も案内しています。

タイプ: 統合 | 日付: 2026-06-23

---

<a id="case-124"></a>
### Case 124: [HuggingChat で作るサイトから HF Space 配置まで](https://x.com/victormustar/status/2070190742991994967) (作者 [@victormustar](https://x.com/victormustar))

**HuggingChat での下調べから Hugging Face Spaces への static deploy まで、ほぼ無料の personal-site flow で GLM-5.2 を試すためのケースです。**

victormustar は、Hugging Face account があれば HuggingChat 上の GLM-5.2 に website を作らせるだけの free credits があり、Exa がユーザーについての background research も行うと述べています。さらに、その結果の site は static な Hugging Face Space として無料で deploy できるため、personal site 実験の具体的で低コストな経路になります。

タイプ: チュートリアル | 日付: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 提供開始](https://x.com/digitalocean/status/2070177703911719301) (作者 [@digitalocean](https://x.com/digitalocean))

**1M context model を自前でホストせずに、official provider access を managed infrastructure 経由で使いたいときのケースです。**

DigitalOcean は、自社の Inference Engine で GLM-5.1 と GLM-5.2 の提供開始を発表し、1M-token context window と最大 8 時間の agentic coding workflow を想定したモデルとして位置づけています。投稿では、usage-based pricing と fully managed infrastructure によって既存 stack に直接統合できる route としても紹介しています。

タイプ: 統合 | 日付: 2026-06-25

---

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI での OpenCode セットアップ](https://x.com/RoundtableSpace/status/2070820686243959276) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**独自のモデルホストを用意せず、coding agent 向けの無料の OpenAI 互換ルートとして Cloudflare Workers AI 経由で GLM-5.2 を動かしたいときに使うケースです。**

RoundtableSpace は、無料の Cloudflare account を作成し、Account ID を控え、API token を作り、OpenCode に Cloudflare を provider として追加して `@cf/zai-org/glm-5.2` を指定できると述べています。投稿では、この経路が OpenCode、Cursor、Aider、Hermes Agent、Claude Code など他の OpenAI 互換ツールでも使えるとしており、coding agent 向け hosted access の実用的な近道になっています。

タイプ: チュートリアル | 日付: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js ノーセットアップのブラウザクライアント](https://x.com/FareaNFts/status/2070848321212792945) (作者 [@FareaNFts](https://x.com/FareaNFts))

**API key、課金、バックエンド設定に触れる前に、ブラウザだけの試作で GLM-5.2 を試したいときに使うケースです。**

FareaNFts は、Puter.js が単一の CDN script tag だけで GLM 系列をクライアント側に公開しており、`z-ai/glm-5.2` をブラウザコードから直接呼び出せて、サーバや開発者側の課金設定も不要だと説明しています。投稿では、個人ツール、vibe coding app、軽量 agent の素早い試作に向く一方で、Puter は user-pays の browser model であり、高スループットの本番トラフィック向けではないという tradeoff も明記されています。

タイプ: チュートリアル | 日付: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 統合エンドポイントアクセス](https://x.com/FareaNFts/status/2070900056736379288) (作者 [@FareaNFts](https://x.com/FareaNFts))

**中国系と西洋系のモデルを free trial credit 付きの単一 OpenAI 互換 SiliconFlow endpoint にまとめて扱えると投稿が説明しているため、GLM-5.2 をより広い multi-model stack に組み込みたいときに使うケースです。**

FareaNFts は、SiliconFlow が GLM-5.2 を DeepSeek、Qwen、Llama 4、Hunyuan、Mistral、Yi、Gemma、Phi など 200 以上のモデルと並べて、1 つの OpenAI 互換 endpoint から利用できると述べています。投稿では、登録時にカード不要で 1 ドル分の free credit が付き、一部モデルは無料のまま使え、spending limit も設定でき、その key を Cursor、Claude Code、Aider などにそのまま入れられるとも説明しています。

タイプ: 統合 | 日付: 2026-06-27

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S ティア](https://x.com/CommandCodeAI/status/2069891896881857016) (作者 [@CommandCodeAI](https://x.com/CommandCodeAI))

**最安の入口価格だけでなく、長期コーディング速度を重視するときに Command Code の高速な GLM-5.2 tier にアクセスするためのケースです。**

Command Code は、GLM-5.2 Fast を high-throughput build として発表し、同じ frontier-coding の位置づけを保ったまま、速度を毎秒 120-250 tokens に引き上げたと述べています。投稿では、この tier が 1M context、tool use、reasoning を維持しつつ、1 ドルの Go plan と 10 ドル分の usage credits 以上で使えることも明記しています。

タイプ: 統合 | 日付: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI Gateway Fast GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (作者 [@wafer_ai](https://x.com/wafer_ai))

**サーバレス速度と明示的なトークン価格が必要なときに、Vercel AI Gateway 経由で GLM-5.2 Fast を使うためのケースです。**

wafer_ai は、GLM-5.2 Fast が Vercel AI Gateway で利用可能になり、速度は毎秒 150-250 tokens、context window は 1M tokens、価格は 100 万 tokens あたり input 3.00 ドル、output 10.25 ドル、cache 0.50 ドルだと述べています。スループット重視かつ gateway 価格を明示して使いたいチームにとって、具体的な hosted-access 情報です。

タイプ: 統合 | 日付: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 コスト、価格、ローカル運用
<a id="case-166"></a>
### Case 166: [Full 744B On 5x ASUS GX10s](https://x.com/thatcofffeeguy/status/2072525885077434743) (作者 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**このケースは、極端な home-lab GLM-5.2 deployment を見積もるためのものです。著者によると、744B の full model が 5 台の ASUS GX10 上で full context 付きで動作し、real workloads 向けの causal harness にもすでに接続されています。**

thatcofffeeguy は、744B のフル GLM-5.2 が 5 台の ASUS GX10 システム上で full context 付きで動作し、token rate も想定より良く、stack はすでに causal harness に接続されていると述べています。正確な throughput 数値はまだ公開されていませんが、この規模の local cluster で full model を載せられることを示す具体的な公開 proof point です。

タイプ: デモ | 日付: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Agent Route Swap In China Stack](https://x.com/0xluffy_eth/status/2072548580183900430) (作者 [@0xluffy_eth](https://x.com/0xluffy_eth))

**このケースは、最高品質よりコスト圧力が重要なときに、mixed-model stack の agent layer へ GLM-5.2 を routing する参考になります。著者によれば、Sonnet を GLM-5.2 に置き換えると、その slot の input cost は 5 倍安くなり、品質低下は約 3 percent でした。**

この thread は、reasoning、code generation、agent calls、batch work、image、video をまたぐ 6 つの routing 変更を示しています。agent layer では Sonnet を GLM 5.2 に置き換え、性能低下は約 3 percent、input cost は 5 倍安くなったと報告しています。30 日のまとめでは、総 AI 運用コストが 87 percent 下がり、revenue は横ばいでした。

タイプ: 評価 | 日付: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B Local Hardware Floor](https://x.com/devjuninho/status/2072151237840007399) (作者 [@devjuninho](https://x.com/devjuninho))

**このケースを使えば、GLM-5.2 のローカル計画を現実的に見積もれます。情報源によれば、量子化しても 2bit で約 239GB、4bit で約 466GB あり、RAM や VRAM は 256GB 超が実用ラインになるからです。**

devjuninho は、open weights だからといって一般向けローカル実行が簡単とは限らないと反論しています。スレッドでは、GLM-5.2 はおよそ 744B パラメータで active は約 40B、2bit で約 239GB、4bit で約 466GB と見積もり、まともなローカル運用にはサーバー級メモリ、SSD の余裕、そして忍耐が必要だと述べています。

タイプ: 制限 | 日付: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Local NVFP4 Rust Port At 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (作者 [@mov_axbx](https://x.com/mov_axbx))

**調整済みローカル GLM-5.2 配置が実際の coding 作業で何をできるか見積もりたいならこの事例が役立ちます。作者は NVFP4 で 140 tok/s と、Python から Rust への全面移植を数分で終えたと報告しています。**

mov_axbx は、OMP 上のローカル GLM-5.2 NVFP4 構成で毎秒約 140 token に達したと報告しています。同じ投稿では、Python 製の衛星位置計算サービスを約 10 分で Rust に移植し、その数分後にデモ web app まで作ったと述べています。

タイプ: 評価 | 日付: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 Agent-Led Dual-Stack Bring-Up](https://x.com/TheValueist/status/2071261052080148607) (作者 [@TheValueist](https://x.com/TheValueist))

**本格的なセルフホスト型 GLM-5.2 deployment の規模感を見積もるためのケースです。スレッドでは、分析 agent がベアメタル B300 上で vLLM と SGLang の両方に NVFP4 推論を 1 日未満で立ち上げています。**

TheValueist は、analyst-agent workflow が、ベアメタルの NVIDIA B300 x2 クラスタ上で GLM 5.2 NVFP4 を vLLM と SGLang の両方に展開し、それぞれの stack で 24 時間未満のうちに benchmark suite 全体を走らせたと述べています。スレッドでは、制約要因は生の compute ではなく HBM capacity であり、KV cache が spill したときには DRAM も効いてくると説明しており、ローカル推論の経済性や hardware bottleneck を評価するチームにとって具体的な運用メモになっています。

タイプ: Evaluation | 日付: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 Ultra Prefill Speedup](https://x.com/jundotkim/status/2071287585297887510) (作者 [@jundotkim](https://x.com/jundotkim))

**最近の kernel work 後に Apple silicon でのローカル運用可能性を再確認するためのケースです。M3 Ultra 512GB での GLM-5.2 prefill speed が、簡単なテストで品質を大きく落とさずほぼ倍増したと報告されています。**

jundotkim は、oMLX 0.4.5.dev1 が custom MLX kernels を追加し、M3 Ultra 512GB マシン上で GLM-5.2-oQ4 の 32k prefill を 87.7 tok/s から 174.4 tok/s へ引き上げ、98.9% の伸びになったと述べています。同じ投稿では、この経路はまだ experimental だとしつつも、needle-in-a-haystack の確認や Claude Code 風の coding test では明確な regression は見られなかったとしており、単なる release note ではなく、実用的なローカル推論アップデートになっています。

タイプ: Evaluation | 日付: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [20M Token Signup Credit Burst](https://x.com/Bitbro4crypto/status/2071150218872283262) (作者 [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**直接 signup でも実用的な GLM-5.2 試用ができるかを判断するためのケースです。投稿では、新規アカウントに 2000 万 free tokens、カード不要、完全な OpenAI 互換 access が付くとされています。**

Bitbro4crypto は、現在の GLM 5.2 signup 導線では、2000 万 free tokens、120 件の image / video credits、high / max thinking mode、1M-context window、そして Cursor や Claude Code のようなツールに subscription なしで差し込める OpenAI 互換 API が得られると述べています。短期テスト向けの具体的な access と pricing のシグナルとして扱う一方で、この promotional quota は変わり得る前提で見るべきです。

タイプ: Integration | 日付: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark ローカル GLM 運用ガイド](https://x.com/TraffAlex/status/2071020631072616698) (作者 [@TraffAlex](https://x.com/TraffAlex))

**DGX Spark クラスタが現実的なローカル GLM-5.2 の道筋かどうかを見極めるためのケースです。収集されたガイドは、具体的なハードウェア費用、クラスタ構成、vLLM コマンドを 1M context の GLM 目標に結び付けています。**

TraffAlex は、コミュニティで検証された知見と NVIDIA の公式情報をまとめ、各ユニットが 4,699 ドル、他モデルでは 2x Spark クラスタがスイートスポット、4x Sparks なら GLM 5.2 NVFP4 を 1M-token context で毎秒約 20 tokens で動かせると説明しています。投稿には CX7 ネットワーク設定、passwordless SSH、NCCL チェック、vLLM の Docker コマンド例も含まれており、単なるハードウェア感想ではなく、実用的なローカル deployment playbook になっています。

タイプ: チュートリアル | 日付: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (作者 [@Hesamation](https://x.com/Hesamation))

**このケースを使用して、GLM-5.2 出力トークンの経済性を Opus、Fable、および GPT-5.5 スタイルのモデルと比較します。**

この投稿では、100万出力トークンの価格を比較し、GLM-5.2がフロンティアクローズドモデルよりも大幅に安価になる可能性があると主張しています。この数字は、予算を立てる前に再確認する必要がある、ソースにリンクされた価格比較として扱います。

タイプ: 評価 | 日付: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (作者 [@Jeyffre](https://x.com/Jeyffre))

**このケースを使用して、セルフホスティング GLM-5.2 のようなモデルがエージェントのヘビー ユーザーのハードウェア コストを返済できるかどうかを検討してください。**

著者は、複数の DGX Spark クラスのマシンで 700B クラスのモデルを実行できると推定し、約 20,000 ドルのハードウェア購入と、コーディングとエージェントのワークロードにかかる高額な月々の API 支出を比較します。

タイプ: 評価 | 日付: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (作者 [@pcuenq](https://x.com/pcuenq))

**このケースを使用して、Apple ハードウェアおよび MLX 指向のセットアップ上で実行されるローカル GLM-5.2 を調べます。**

この投稿では、GLM-5.2 がリリースされたばかりで、すでに 2 台の Mac Studio M3 Ultra マシンで MLX とともに実行されており、オープンウェイトを備えた最近のクローズド モデルと同等であると述べられています。

タイプ: デモ | 日付: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (作者 [@ai_xiaomu](https://x.com/ai_xiaomu))

**このケースは、サブスクリプションとセルフホスティングのどちらかを選択する前に、ローカル展開の前提条件を確認するためのコスト比較プロンプトとして使用します。**

中国の投稿では、主張されている SWE-Bench の数値、商用オープンソースの使用、および単一の H100 のローカル展開コストの推定値と、Claude Pro のサブスクリプションを比較しています。現在のインフラストラクチャの価格設定に合わせて数値を再検証する必要があります。

タイプ: 評価 | 日付: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (作者 [@RoundtableSpace](https://x.com/RoundtableSpace))

**このケースを使用して、GLM-5.2 に関する無料クレジットと代替エージェントの物語を検証し、マーケティング上の主張と検証済みのワークロード適合性を区別します。**

この投稿では、GLM-5.2 を、毎日のクレジット、オープンソース制御、セルフホスティング、および長時間のコーディング セッションに対する強力な価値を備えた、低コストの Claude の競合製品として紹介しています。

タイプ: 評価 | 日付: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (作者 [@0xSero](https://x.com/0xSero))

**このケースを使用して、有料プロバイダーまたはローカル展開にコミットする前に、無料の ZCode 許容量を通じて GLM-5.2 をテストします。**

著者は、ZCode を介した GLM-5.2 の可用性と、1 日あたりの大量の無料トークン許容量について説明し、vLLM Studio またはローカル ホスティングのセットアップに使用できる可能性について説明しています。

タイプ: 統合 | 日付: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (作者 [@JZiyue_](https://x.com/JZiyue_))

**このケースを使用して、GLM-5.2 テスト用のタイムボックス化されたフリーアクセス ウィンドウを見つけます。**

この投稿では、GLM-5.2 が ZenMux 上でライブ配信され、1 週間の無料期間、100 万コンテキスト、コーディングとエージェントの改善、および 5.1 と同じ価格設定が宣伝されています。

タイプ: 統合 | 日付: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAIのトークンごとの価格設定](https://x.com/nahcrof/status/2067166596523765781) (作者 [@nahcrof](https://x.com/nahcrof))

**このケースを使用して、ルートを選択する前に GLM-5.2 のサードパーティ プロバイダーの価格を比較します。**

この投稿では、入力、出力、およびキャッシュの価格をリスト化した crofAI の GLM-5.2 を発表し、安価なフロンティア インテリジェンスとして位置づけています。

タイプ: 統合 | 日付: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (作者 [@scaling01](https://x.com/scaling01))

**GLM-5.2 を他のフロンティア ラボやオープン モデルと比較するときは、このケースを市場価格の批評として使用してください。**

著者は、出力トークンの価格設定に関して GLM-5.2 と他の大規模なオープン モデルを比較し、その比較を利用して、一部のフロンティア ラボ API マージンが高いと主張しています。

タイプ: 評価 | 日付: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (作者 [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**このケースを使用して、オフライン コーディングのセットアップを計画する前に、大容量メモリの Apple ハードウェアでのローカル GLM-5.2 推論スループットを見積もります。**

ソースは、ローカルの高メモリ Mac セットアップで 1 秒あたり 44.1 トークンを報告し、大量のツール呼び出しによるデコード繰り返しの問題について言及しています。

タイプ: デモ | 日付: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (作者 [@mrblock](https://x.com/mrblock))

**このケースは、完全なモデルの重みが通常のローカル ハードウェアにとって大きすぎる場合に、量子化された GLM-5.2 デプロイメント パスを評価するために使用します。**

この投稿では、Unsloth の動的 2 ビットおよび 1 ビット GGUF オプション、メモリ削減、および llama.cpp または Unsloth Studio のデプロイ ルートについて説明します。

タイプ: チュートリアル | 日付: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**より大きな Apple Silicon 構成を組む前に、2 台の M3 Ultra で分散 MLX 実行した GLM-5.2 8-bit serving の実態を見積もるためのケースです。**

投稿では 2 台の M3 Ultra 512GB マシンにまたがる MLX distributed 実行で、GLM-5.2 8-bit が約 17.9 tokens/sec、総メモリがおよそ 760GB で動いています。作者はまだ work-in-progress の PR だとも明記しており、完成ガイドではなく deployment signal として見るべきです。

タイプ: デモ | 日付: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (作者 [@buildwithhassan](https://x.com/buildwithhassan))

**peak / off-peak の multiplier 引き下げ期間を使って、GLM-5.2 の plan credits を引き延ばすためのケースです。**

この投稿では ZCode が GLM coding plan の multiplier を peak 時間帯で 3x から 2x、off-peak で 2x から 0.67x に下げ、その新しい window が 9 月末まで続くと述べています。GLM-5.2 の credits を伸ばしたい人にとって、具体的な access / pricing note です。

タイプ: 統合 | 日付: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**ハイエンドなローカル GLM-5.2 ワークステーションを見積もるためのケースです。Blackwell 2 枚のデスクトップで、4-bit 量子化ビルドの二桁デコード速度を維持しました。**

CardilloSamuel は、GLM-5.2 UD-Q4_K_XL を 2x RTX PRO 6000 Blackwell、Threadripper PRO 9995WX、1TB DDR5 で動かしたと報告しています。投稿では、prefill が約 64 tok/s、decode が 13-15 tok/s、Aider Polyglot スコアが 69.7% で BF16 に 2 ポイント差以内だったとされ、ボトルネックはシステム RAM 帯域であり、構成の合わない 5090 は分割実行から外したと述べています。

タイプ: デモ | 日付: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (作者 [@karminski3](https://x.com/karminski3))

**ローカル GLM-5.2 推論のために Mac Studio を買う意味があるかを現実的に確認するためのケースです。投稿された回収計算では、多くの利用者にとって API やプラン利用の方が有利です。**

この投稿では、32,999 RMB の Mac Studio は、引用された価格では GLM-5.2 API トークン約 11.78 億に相当すると試算しています。さらに、より小さい Qwen 構成ですら回収期間は約 209 日だと主張しています。そのうえで、512GB Mac Studio で量子化 GLM-5.2 を約 17 tok/s で動かしても損益分岐まで約 7 年かかる可能性があるため、ローカル保有が意味を持つのは、すでにハードウェアを持っているか、遊休時間を活用できる場合に限られると述べています。

タイプ: 評価 | 日付: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM Local Outage Save](https://x.com/CardilloSamuel/status/2069431311463236078) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**ホスト型 frontier API が停止や上限到達を起こしても、LiteLLM 経由でローカル GLM-5.2 に切り替えて納品を前に進めるためのケースです。**

CardilloSamuel は、友人がトークン切れと Claude 停止に直面したため、自身のローカル GLM-5.2 デプロイを指す LiteLLM API key を発行したと述べています。その友人は約 500 万 tokens を 0 ドルで生成し、速度の遅さを受け入れつつも納期に間に合わせたとされています。

タイプ: デモ | 日付: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [Individual Versus Team Local ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**ローカル GLM-5.2 デプロイが個人に見合うのか、より大きな開発チーム向きなのかを判断するためのケースです。**

この投稿では、個人のローカル構成には 512GB のシステムメモリ、複数 GPU、強力な CPU が必要で、それでも速度は毎秒 6-10 tokens 程度だと主張しています。一方で、プライバシー、無制限トークン、週次上限なし、プロバイダー障害やポリシー変更からの独立を重視する 10 人以上の開発チームなら、共有の社内サーバーの方が理にかなうと述べています。

タイプ: 評価 | 日付: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 実行](https://x.com/0xSero/status/2069871347010838586) (作者 [@0xSero](https://x.com/0xSero))

**高性能ワークステーションを組む前に、4 GPU のローカル GLM-5.2 構成を厳しい terminal benchmark に照らして見積もるためのケースです。**

0xSero は、GLM-5.2-REAP-NVFP4 が Terminal Bench 2.0 で 69.1% を記録し、4x RTX PRO 6000 に収まるモデル群の中で最高の terminal-bench 結果だと述べています。量子化した open-weight 構成と hosted frontier terminal を比較検討するチームにとって、具体的なローカル導入シグナルです。

タイプ: 評価 | 日付: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell でのローカル Crackme 解読](https://x.com/CardilloSamuel/status/2069887782508753302) (作者 [@CardilloSamuel](https://x.com/CardilloSamuel))

**デバッガなしでも、本格的なローカル GLM-5.2 構成が長時間のリバースエンジニアリング課題を完了できるかを判断するためのケースです。**

CardilloSamuel は、約 300GB RAM を積んだ 2x RTX PRO 6000 Blackwell 上のローカル GLM 5.2 が、OpenCode 経由で crackme challenge を 78 分、約毎秒 14 tokens で解いたと述べています。投稿では、harness にデバッガや MCP へのアクセスはなかったものの、モデルがメモリアドレスをダンプし、仮説を検証し、バイナリをパッチせず指示に従って進めたことが強調されています。

タイプ: デモ | 日付: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 制約、注意点、安全性シグナル
<a id="case-163"></a>
### Case 163: [Preliminary Cyber Research Parity](https://x.com/Irregular/status/2072682835798831168) (作者 [@Irregular](https://x.com/Irregular))

**このケースは、vulnerability research の部分タスクで GLM-5.2 を測るためのものです。Irregular は、狭い cyber suite で GPT-5.4 と Opus 4.6 に近い初期内部評価を報告しつつ、end-to-end の attack scenario はまだ未検証だと明言しています。**

Irregular は、限定的な内部 vulnerability research task suite で、試した範囲では GLM-5.2 が GPT-5.4 と Claude Opus 4.6 におおむね近かったと述べています。同じ投稿では、suite が狭く、CyScenarioBench や FrontierCyber のような scenario-level benchmark はまだ実施していないとも付け加えています。完全な offensive-agent parity の証明ではなく、初期の cyber capability signal として扱うべきです。

タイプ: 制約 | 日付: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter Spend-Cut Skill Rewrite](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (作者 [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**このケースは、エージェントモデルを入れ替える前に移行コストを見積もるのに役立ちます。あるファンドの OpenRouter 試行では GLM-5.2 が Opus の約 8 分の 1 のコストでしたが、skill の書き換え、routing ロジック、そして遅く弱い出力を受け入れる前提が必要でした。**

Rahul J Mathur によると、彼のチームのエージェントはそれまで年換算で約 10 万ドル規模の Opus 専用運用でしたが、6 月に支出を約 40 パーセント下げることを狙って OpenRouter のマルチモデル試行を始めました。本人の観測では、GLM-5.2 は Opus 4.8 より遅く、エッジケースや skill file 全読みに失敗しやすい一方で、受け手から見た出力品質はコスト 8 分の 1 前後でも許容範囲でした。同じスレッドでは、Opus や GPT 向けの skill はそのまま移植できず、更新済み skill、新しい筋肉記憶、ハードコードした routing ロジックが必要だと警告しています。

タイプ: 制限 | 日付: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA Verbosity And Reasoning Tradeoff](https://x.com/ArtificialAnlys/status/2072022576394821859) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**GLM-5.2 の frontier 級 open-weight 性能と reasoning 効率コストを切り分けたいならこの事例が役立ちます。Artificial Analysis が、open-weight 首位でありながら出力 token 消費が極端に大きいことも示しているからです。**

Artificial Analysis は、GLM-5.2 Max が Intelligence Index を回すのに約 1.41 億の出力 token を使い、その 95% が reasoning token だったと述べています。Opus 4.8 の 1.17 億、GPT-5.5 の 7200 万と比べても多い一方で、GLM-5.2 を最強 open weight と位置づけています。

タイプ: 評価 | 日付: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR Narrow-Win Caveat](https://x.com/leploutos/status/2071121981551047039) (作者 [@leploutos](https://x.com/leploutos))

**ソースによれば GLM-5.2 は 1 つの IDOR benchmark で Claude Code を上回った一方、Mythos 自体とは比較されていないため、実際の security signal と見出し先行の誇張を切り分けるためのケースです。**

leploutos は、拡散している「GLM が Mythos と同等」という読み方は誤りだと述べています。Semgrep の結果は、単一の IDOR detection benchmark で GLM-5.2 が F1 39% を記録し、28-37% の Claude Code 構成を上回ったというもので、コストは 1 bug あたり約 0.17 ドル、frontier model の約 6 分の 1 だったとされています。同じ投稿では、実務上重要な制約も明示されており、1 bug class、1 dataset、1 run、しかも vendor-owned benchmark であるため、これは GLM が Anthropic の専用 cyber model に並ぶ証拠ではなく、狭いながら実在する vulnerability detection signal として扱うべきだとしています。

タイプ: Limit | 日付: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 推論効率ギャップ](https://x.com/scaling01/status/2070961852008509918) (作者 [@scaling01](https://x.com/scaling01))

**reasoning 負荷の高い workload で GLM-5.2 を確認したいときに使うケースです。投稿された LisanBench 結果では GLM-5 より改善していますが、他の open model と比べるとまだ効率が低いことが示されています。**

scaling01 は、LisanBench において GLM-5.2-high がスコア 1834 で 29 位、GLM-5 は 986.83 だったと報告しています。同じ投稿では、Kimi-K2.5 Thinking が平均約 19K tokens で近いスコアに達する一方、GLM-5.2 は約 32K tokens を使うとしており、過去の GLM 世代より改善しているものの、reasoning efficiency ではまだ相対的に弱いと位置づけています。

タイプ: 制限 | 日付: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench ドメイン不一致の注意点](https://x.com/yuhasbeentaken/status/2070928066797351300) (作者 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**弱い PrinzBench スコアと、はるかに強い software・tool-use benchmark を投稿が対比しているため、GLM-5.2 を法務調査ではなく coding と agent execution に集中させるためのケースです。**

yuhasbeentaken は、GLM-5.2 が法務調査と難しい web search に特化した狭い benchmark である PrinzBench で 30/99 にとどまる一方、SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0、MCP-Atlas 77.0、ProgramBench 63.7 などでは強い公開成績を示していると述べています。投稿では、この差を矛盾ではなく domain fit の問題として扱い、法務調査にはより強い proprietary model、coding と agentic execution には GLM-5.2 を推奨しています。

タイプ: 制限 | 日付: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (作者 [@sawyerhood](https://x.com/sawyerhood))

**この場合は、GLM-5.2 がネイティブ ビジョン機能を必要とするワークフローにはあまり役に立たない可能性があることを覚えておいてください。**

著者は、Design Arena のランキング投稿を引用して、ビジョンを欠いた GLM モデルは有用性を低下させると指摘しています。これは、マルチモーダルな製品計画における実際的な注意事項です。

タイプ: 制限 | 日付: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [現実世界のエージェントギャップに関する警告](https://x.com/ml_angelopoulos/status/2067013545431269405) (作者 [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**このケースを使用して、GLM-5.2 がデプロイされたすべてのエージェント タスクで最適な独自モデルに一致することを証明するベンチマークの勝利を読みすぎないようにします。**

著者によれば、GLM-5.2 は素晴らしいものですが、エージェント アリーナ手法に基づいた、現実世界のエージェント タスクの一般的な分布に対する、寓話レベルや Opus 4.8 の思考レベルのパフォーマンスにはまだ及んでいません。

タイプ: 制限 | 日付: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (作者 [@VittoStack](https://x.com/VittoStack))

**このケースは、機密性の高いドメインに GLM-5.2 を展開する前に安全性評価を実行するためのリマインダーとして使用してください。**

この投稿は、比較安全性テストで有害なコンテンツの拒否に失敗したことを報告しています。リポジトリは、安全でない詳細ではなく、安全性の信号のみを記録し、これを展開リスクの警告として扱います。

タイプ: 制限 | 日付: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [ベンチマーク方法論の批評](https://x.com/josepha_mayo/status/2066951013337112661) (作者 [@josepha_mayo](https://x.com/josepha_mayo))

**このケースを使用して、ヘッドラインの結果が GLM-5.2 を支持する場合でも、ベンチマーク手法に疑問を持ちます。**

著者は、GLM-5.2 が強力であることを認めながらも、Design Arena の方法論を批判しており、リーダーボードの主張と並行してベンチマークに対する懐疑論を求める読者にとって有益なものとなっています。

タイプ: 制限 | 日付: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (作者 [@k_matsumaru](https://x.com/k_matsumaru))

**このケースは、コーディング プランを切り替える前、またはクロード コード スタイルのワークフローを GLM-5.2 にルーティングする前に、プロバイダーの遅延をテストするために使用します。**

日本の投稿では、コーディング計画内で GLM-5.2 を使用することを検討していますが、ピーク時の応答遅延についての事前の懸念があると述べています。

タイプ: 制限 | 日付: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (作者 [@nikhilchandak29](https://x.com/nikhilchandak29))

**このケースを使用して、広範囲に展開する前に、コーディングの利点が非コーディング ドメインに一般化するかどうかを確認します。**

この投稿では、FutureSim では GLM-5.2 が GLM-5.1 と同等であると報告しており、その結果を利用して、コーディングの改善がすべてのドメインで均等に一般化するわけではない可能性があると警告しています。

タイプ: 制限 | 日付: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (作者 [@bridgemindai](https://x.com/bridgemindai))

**このケースを使用して、モデルの機能を起動の実行、ドキュメント、API の準備から分離します。**

この投稿では、当時はベンチマークと API アクセスがまだ利用できておらず、モデルの品質の判断ではなく、リリースの準備のレビューに関連しているため、初期リリースは厄介であると述べています。

タイプ: 制限 | 日付: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [コーディングプランの値上げ](https://x.com/bridgemindai/status/2065799843658793092) (作者 [@bridgemindai](https://x.com/bridgemindai))

**GLM-5.2 を低コストの代替品として推奨する前に、このケースを使用してプランの価格を確認してください。**

著者は、GLMcoding Pro プランに月額 65 ドルを支払っていると報告しており、プランは前回のサブスクリプションからほぼ 2 倍になったと述べています。現在の価格を確認するためのリマインダーとして使用してください。

タイプ: 制限 | 日付: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [短い並列作業と長いエージェント実行](https://x.com/thekuchh/status/2068010332501479865) (作者 [@thekuchh](https://x.com/thekuchh))

**このケースを使用して、GLM-5.2 を短期間のコーディング タスクにルーティングしながら、より深い数時間にわたるエージェント実行用に強力なモデルを確保します。**

この投稿では、実用的な分割について報告しています。GLM-5.2 は、短い並列タスクにはうまく機能しますが、エージェントを長時間実行するとドリフトします。

タイプ: 制限 | 日付: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [コード検閲とバイアスのチェック](https://x.com/wongmjane/status/2068424945663893936) (作者 [@wongmjane](https://x.com/wongmjane))

**コードと政治的バイアス検証の実用的な safety signal として使うためのケースであり、広範な alignment 上の懸念が解決済みだと示すものではありません。**

作者は、GLM-5.2 がコード内に中国の政治検閲を埋め込まなかったこと、また Vietnam War に関する false な US-bias claim を訂正しつつ、意見に近いケースはそのまま残したことを述べています。これにより、政治的に敏感な coding と factuality の挙動を検証するための具体的な公開例になっています。

タイプ: 制限 | 日付: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高難度推論での課金 failure](https://x.com/s_batzoglou/status/2068297051247350154) (作者 [@s_batzoglou](https://x.com/s_batzoglou))

**hard reasoning workload に対して GLM-5.2 を慎重に試すためのケースです。公開報告では長い実行時間、低い完了率、予想外に高い課金出力量が示されています。**

作者は 11 件の induction problem を実行し、完了は 4 件、正答は 2 件、実行時間は数時間に及び、請求額は可視 token count よりかなり高く見えたと報告しています。これは単なる benchmark score ではなく、reasoning efficiency と billing behavior に関する具体的な警告です。

タイプ: 制限 | 日付: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard Multiturn Hallucination Signal](https://x.com/dyfan22/status/2069335764295438532) (作者 [@dyfan22](https://x.com/dyfan22))

**他のベンチマーク成績を信頼しすぎる前に、幻覚に敏感なマルチターンタスクで GLM-5.2 を検証するためのケースです。**

HalluHard は、最大 reasoning effort を伴う adaptive thinking 設定で GLM-5.2 をリーダーボードに追加しました。この更新では、他ベンチマークで強い結果が出ていても、HalluHard の難しいマルチターンベンチマークでは GLM-5.2 が依然として頻繁に hallucinate すると述べています。

タイプ: 制限 | 日付: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Open-Weight Security Emergency Warning](https://x.com/joshua_saxe/status/2069289170107842572) (作者 [@joshua_saxe](https://x.com/joshua_saxe))

**安全計画のシグナルとして、open-weight の GLM-5.2 が offensive security agents の運用摩擦を下げる点を確認するためのケースです。**

Joshua Saxe は、GLM-5.2 によって、これまで frontier coding agents を使う攻撃者を抑えていた監視やアカウント面の摩擦の多くが取り払われると論じています。このスレッドは、open weights と private deployment の組み合わせを攻撃能力の重大な変化として捉え、API gatekeeping に頼るのではなく、防御側の導入加速を求めています。

タイプ: 制限 | 日付: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Rust バグは通るがターン数は 7 倍](https://x.com/BohuTANG/status/2069979942608425364) (作者 [@BohuTANG](https://x.com/BohuTANG))

**GLM-5.2 の code quality の強みと、現時点の agent harness overhead を切り分けて考えるためのケースです。bug 自体は通せても Opus より大幅に多くの turns を消費します。**

BohuTANG は、Rust の同じ bug、serde_json issue 979 を対象に、evot、Claude Code、Pi の 3 agent で GLM-5.2 と Opus 4.6 を比較しました。6 session すべてが pass し、著者は GLM の bug 理解と最終 code quality は十分だったと述べていますが、GLM は 38 / 43 / 61 turns を使ったのに対し、Opus は 3 agent 全体で約 18 turns、約 80 秒で終えたとしています。trace note では、その差は cargo と環境処理の反復、収束の悪さ、長い self-verification loop にあると説明されています。

タイプ: 評価 | 日付: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust モデル差し替えコストの注意点](https://x.com/ankrgyl/status/2069869387549446597) (作者 [@ankrgyl](https://x.com/ankrgyl))

**実際の agentic coding workflow で、安価なモデルへの差し替えが品質を保つと安易に仮定しないためのケースです。**

ankrgyl は、Braintrust がリポジトリの commit と bug description から始めて修正結果を評価する workflow で、Opus 4.8 と GLM-5.2 を比較したと述べています。その単純な置き換えでは、GLM-5.2 はコストがほぼ同程度で、実行時間は長く、pass rate は低く、総合的には効率が劣ったと報告されています。

タイプ: 評価 | 日付: 2026-06-24

---

<a id="acknowledge"></a>
## 🙏 謝辞

このリポジトリは、実際の GLM-5.2 利用の証拠を公開で共有してくれたクリエイター、開発者、ベンチマークチーム、プロバイダー、コミュニティに触発されて作られました。

ここで紹介した高シグナルな情報源とクリエイターに感謝します: [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan), [@ScaleAILabs](https://x.com/ScaleAILabs), [@wafer_ai](https://x.com/wafer_ai), [@ankrgyl](https://x.com/ankrgyl), [@clairevo](https://x.com/clairevo), [@MatinSenPai](https://x.com/MatinSenPai), [@hrdkbhatnagar](https://x.com/hrdkbhatnagar), [@nutlope](https://x.com/nutlope), [@victormustar](https://x.com/victormustar), [@digitalocean](https://x.com/digitalocean), [@BohuTANG](https://x.com/BohuTANG).

最近追加したクリエイター: [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy).

*帰属に修正が必要な場合はご連絡ください。確認のうえ更新します。*

興味深い GLM-5.2 の実利用ケースがあれば、issue や pull request でぜひ共有してください。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)