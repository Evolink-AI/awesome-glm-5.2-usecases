<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="GLM-5.2 고신뢰 유스케이스 저장소 banner" width="760"></a>

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

# GLM-5.2 고신뢰 유스케이스 저장소

## 🍌 소개

GLM-5.2 고신뢰 유스케이스 저장소에 오신 것을 환영합니다.

**공개 데모와 크리에이터 커뮤니티에서 GLM-5.2의 실제 사례, 튜토리얼, 통합, 평가, 가격 신호, 한계를 수집합니다.**

이 현지화 README는 구체적인 워크플로, 공개 벤치마크 근거, 실사용 데모, 통합, 비용, 실무상 주의점이 있는 사례에 집중합니다.

각 사례 제목은 공개 출처로, 작성자 핸들은 크리에이터 프로필로 연결됩니다.

[Evolink에서 GLM-5.2 사용해 보기](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 개요

- 공개 크리에이터, 벤치마크 팀, 도구 개발자, 제공업체, 실사용자가 공유한 **209개의 선별된 GLM-5.2 사례**입니다.
- 벤치마크와 프런티어 평가, 코딩 에이전트와 장기 컨텍스트 워크플로, 실사용 데모와 쇼케이스 빌드, 공급자 및 도구 통합, 비용, 가격, 로컬 배포, 한계, 주의점, 안전 신호를 다룹니다.
- 각 사례에는 원본 출처, 작성자 표기, 간결한 활용 포인트, 근거 유형, 게시 날짜가 포함됩니다.
- 실용 워크플로, 강점과 한계 비교, 공급자 경로, 실제 실험을 찾는 데 사용하세요.

> [!NOTE]
> 이 컬렉션은 과장보다 구체적 근거를 우선합니다: 출시된 데모, 벤치마크 방법, 통합 노트, 비용 데이터, 명시된 caveat입니다.

> [!NOTE]
> 현지화 README는 영어 원본과 같은 사례 순서, 링크, anchor, 출처 표기를 유지합니다. 추적성을 위해 일부 제목은 원문에 가깝게 유지됩니다.

<a id="quick-start"></a>
## ⚡ Quick Start

Evolink의 OpenAI 호환 Chat Completions API로 GLM-5.2를 사용할 수 있습니다. [Evolink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key)에서 API key를 받은 뒤 요청 전에 `EVOLINK_API_KEY`로 설정하세요.

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

전체 GLM-5.2 API reference: [GLM-5.2 API docs 열기](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases).

## 📑 메뉴

| 섹션 | 사례 |
|---|---|
| [📏 벤치마크와 프런티어 평가](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207 |
| [💻 코딩 에이전트와 장기 컨텍스트 워크플로](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194 |
| [🎮 실사용 데모와 쇼케이스 빌드](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202 |
| [🔌 공급자 및 도구 통합](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208 |
| [💸 비용, 가격, 로컬 배포](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209 |
| [🧭 한계, 주의점, 안전 신호](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205 |
| [🙏 감사의 말](#acknowledge) | 출처 표기 및 수정 정책 |

### [📏 벤치마크와 프런티어 평가](#benchmarks-frontier-evaluation)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 207: Stable Fluids Browser Benchmark](#case-207) | 이 사례는 알고리즘 비중이 큰 브라우저 물리 빌드에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0가 Stable Fluids HTML benchmark를 돌려 GLM 5.2 Max에 100점 만점 중 88점을 줬기 때문입니다. | 평가 |
| [Case 199: Epoch Open-Weight Index Lead](#case-199) | 이 사례는 GLM-5.2를 장기 capability curve 위에 놓고 볼 때 유용합니다. Epoch AI가 Capabilities Index 추정 점수 152를 제시했고, 자신들이 평가한 open-weight 모델 중 최고라고 했기 때문입니다. | 벤치마크 |
| [Case 196: Databricks Internal Harness Eval](#case-196) | 이 사례는 GLM-5.2를 대규모 private engineering codebase에서 benchmark할 때 유용합니다. Databricks에 따르면 3,000명 넘는 엔지니어의 작업을 포함한 내부 평가에서 GLM 5.2가 매우 강했고, harness 선택만으로도 비용을 약 2x 줄일 수 있었기 때문입니다. | 평가 |
| [Case 190: NatureBench Open-Weight Runner-Up](#case-190) | 이 사례는 GLM-5.2를 scientific-agent workflow에서 benchmark할 때 유용합니다. NatureBench가 6개 scientific domain, 90개 task에서 GLM-5.2가 전체 2위이자 open-weight 1위로 데뷔했다고 말하기 때문입니다. | 벤치마크 |
| [Case 189: Terminal-Bench 45-Task Cost Tradeoff](#case-189) | 이 사례는 같은 agent harness에서 GLM-5.2와 GPT-5.5를 비교할 때 유용합니다. 45개 Terminal-Bench 작업에서 GLM-5.2는 25승, GPT-5.5는 29승이었고, GLM은 prompt caching 기준 약 40% 더 저렴했기 때문입니다. | 평가 |
| [Case 188: Harvey LAB-AA Legal-Agent Tie](#case-188) | 이 사례는 GLM-5.2를 실제 법률 에이전트 업무에서 benchmark할 때 유용합니다. Harvey LAB-AA에서 GLM-5.2 Max가 24개 practice area, 120개 private task 기준으로 Claude Opus 4.8과 같은 7.5% all-pass를 기록했기 때문입니다. | 벤치마크 |
| [Case 184: AutomationBench-AA Open-Weights Lead](#case-184) | 이 사례는 GLM-5.2를 coding benchmark뿐 아니라 비즈니스 규칙을 지켜야 하는 SaaS automation에서 비교할 때 유용합니다. Artificial Analysis가 AutomationBench-AA에서 GLM-5.2 Max를 27.8%로 보고하며 open weights 중 1위라고 했기 때문입니다. | 평가 |
| [Case 178: Three-Body Simulator Benchmark Win](#case-178) | 이 사례는 수치물리 코딩 벤치마크에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0가 혼돈적인 3체 시뮬레이터 과제를 돌려 GLM 5.2 Max에 100점 만점 중 91점의 최고 점수를 줬기 때문입니다. | 평가 |
| [Case 175: Cursor Double Pendulum Scorecard](#case-175) | 이 사례는 제약이 있는 Cursor coding benchmark에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0는 HTML double-pendulum simulator로 6개 모델을 비교해 GLM 5.2 Max에 100점 만점 중 88점을 줬고, Fable과 Sonnet에는 뒤졌지만 GPT-5.5, Kimi K2.7 Code, Composer보다는 앞섰습니다. | 평가 |
| [Case 162: VulcanBench 10-Task 80 Percent Tie](#case-162) | 이 사례는 cost와 score가 모두 중요한 post-cutoff 실제 엔지니어링 작업에서 GLM-5.2를 비교할 때 유용합니다. Morgan Linton에 따르면 VulcanBench에서 GLM 5.2 High, Fable 5 Low, Sonnet 5 High가 10개 repo에서 모두 80 percent를 기록했고, GLM의 비용은 중간이었습니다. | 평가 |
| [Case 159: SWE-Rebench 51.1 Percent Checkpoint](#case-159) | 이 사례는 계속 업데이트되는 SWE 에이전트 리더보드에서 GLM-5.2를 추적할 때 유용합니다. 최신 SWE rebench 게시물은 2.62 million tokens에서 51.1 percent를 보고하며, 새로 추가된 DeepSeek, MiMo, Qwen, Gemma 런보다 분명히 앞섭니다. | 평가 |
| [Case 154: LaunchDarkly Edge-Case Win At 40/41](#case-154) | 이 사례는 채팅 전용 평가가 아니라 비즈니스 도구를 쓰는 에이전트 작업에서 GLM-5.2를 시험할 때 유용합니다. Composio에 따르면 GitHub, Jira, LaunchDarkly 작업 41개 중 40개를 맞혔고, 보류 중 승인이라는 엣지 케이스를 잡아낸 모델은 GLM뿐이었습니다. | 평가 |
| [Case 110: AA-Briefcase 작업당 시간 프런티어](#case-110) | 벤치마크 점수뿐 아니라 작업당 시간이 중요한 장기 지식 노동에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오. | 벤치마크 |
| [Case 111: Code Arena Frontend 정면 대결 마진](#case-111) | 단일 순위 스크린샷이 아니라 쌍대 정면 대결 결과로 GLM-5.2의 프런트엔드 우위를 확인하려면 이 사례를 사용하십시오. | 벤치마크 |
| [Case 113: SWE Atlas Codebase QnA 준우승](#case-113) | 단일 작업 SWE 리더보드만이 아니라 Codebase QnA, 테스트 작성, 리팩터링 전반에서 GLM-5.2를 추적하려면 이 사례를 사용하십시오. | 벤치마크 |
| [Artificial Analysis Intelligence Index](#case-1) | 인공 분석 게시물을 사용하여 GLM-5.2를 인텔리전스 및 작업당 비용에 대한 다른 개방형 및 독점 프론티어 모델과 비교하세요. | 벤치마크 |
| [Code Arena Frontend Ranking](#case-2) | 이 사례를 사용하여 경기장 스타일 비교로 판단된 실제 프런트엔드 코딩 작업에서 GLM-5.2를 평가합니다. | 벤치마크 |
| [Design Arena First Place](#case-3) | 이 사례를 사용하여 GLM-5.2가 텍스트가 많은 코딩 벤치마크가 아닌 디자인과 코드 작업을 처리할 수 있는지 판단합니다. | 벤치마크 |
| [FrontierSWE Result](#case-4) | FrontierSWE 게시물을 사용하여 소프트웨어 엔지니어링 작업에 대한 GLM-5.2를 GPT-5.5, Opus 및 Fable 스타일 모델과 비교하세요. | 벤치마크 |
| [DeepSWE Open-Source Lead](#case-5) | DeepSWE 사례를 사용하여 GLM-5.2를 어려운 소프트웨어 엔지니어링 평가 작업을 위한 강력한 개방형 모델로 이해하세요. | 벤치마크 |
| [Terminal-Bench Over 80 Percent](#case-6) | 터미널 지향 코딩 및 에이전트 워크플로우에 대해 GLM-5.2를 평가할 때 이 사례를 사용하십시오. | 벤치마크 |
| [GPT-5.5에 대한 SWELancer 비교](#case-7) | 이 SWELancer 사례를 작업 성공, 보상 및 완료 시간에 대한 GLM-5.2와 GPT-5.5 간의 구체적인 다중 측정 비교로 사용하세요. | 평가 |
| [BridgeBench Perfect Score Signal](#case-8) | 코딩 순위표만 사용하는 것이 아니라 기반 다단계 추론을 통해 GLM-5.2를 검사하려면 이 사례를 사용하세요. | 벤치마크 |
| [BridgeBench Reasoning Number One](#case-9) | 근거 추론 작업에 대한 폐쇄 프론티어 모델과 GLM-5.2를 비교하려면 이 사례를 사용하십시오. | 벤치마크 |
| [KernelBench-Hard Without Shortcutting](#case-10) | 벤치마크 이득이 지름길 대신 유효한 구현 동작에서 나오는지 확인할 때 이 사례를 사용하세요. | 평가 |
| [Runescape Bench Catch-Up](#case-11) | 이 사례를 게임과 같은 벤치마크 작업에서 개방형 모델 진행에 대한 빠른 신호로 사용하세요. | 벤치마크 |
| [BridgeBench Speed Improvement](#case-12) | 이 사례를 사용하여 인텔리전스와 함께 속도가 중요한 지연 시간에 민감한 워크플로를 평가하세요. | 벤치마크 |
| [KernelBench 하드 및 메가 GPU 코딩](#case-60) | 공개 에이전트 추적을 통해 결과를 검사할 수 있는 KernelBench-Hard 및 KernelBench-Mega 전반의 GPU 커널 코딩에서 GLM-5.2를 평가하려면 이 사례를 사용하세요. | 벤치마크 |
| [DeepSWE Max-Effort 오픈소스 선두](#case-70) | 최대 effort 설정의 DeepSWE에서 GLM-5.2를 추적하는 데 쓰는 사례입니다. 공개 리더보드에서는 open model 가운데 1위, pass@1 44%로 제시됩니다. | 벤치마크 |
| [LLM Debate Benchmark 준우승](#case-72) | 코딩 외 작업에서도 GLM-5.2를 평가하기 위한 사례입니다. 적대적 multi-turn debate 에서 max-reasoning variant 가 Claude 계열 다음인 2위를 기록했습니다. | 벤치마크 |
| [AA-Omniscience hallucination rate](#case-76) | 불확실성 처리 성능을 비교하기 위한 사례입니다. 공개된 AA-Omniscience 결과에서는 GLM-5.2의 hallucination rate 가 여러 frontier model 보다 낮게 나옵니다. | 평가 |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | 코딩 전용 리더보드가 아니라 장기 지식 노동에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오. | 평가 |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | 게임 제작 품질에서 GLM-5.2를 판단하려면 이 사례를 사용하십시오. Game Dev Arena에서 2위를 기록했고, 그 순위에서 오픈 웨이트 진영 최고 성적을 냈습니다. | 평가 |

### [💻 코딩 에이전트와 장기 컨텍스트 워크플로](#coding-agents-long-context-workflows)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 194: CuTeDSL Kernel Skill Open Source](#case-194) | 이 사례는 GLM-5.2를 재사용 가능한 kernel-debugging skill 안에서 살펴볼 때 유용합니다. 작성자가 CuTeDSL용 Hermes skill을 오픈소스로 공개했고, kernel 디버깅과 작성에서 GLM-5.2의 비용 효율이 특히 좋았다고 말했기 때문입니다. | 튜토리얼 |
| [Case 180: Hermes SSD Recovery Skill Loop](#case-180) | 이 사례는 수리 지향 agent loop 안에서 GLM-5.2를 시험할 때 유용합니다. ShankhadeepSho1에 따르면 Hermes와 GLM 5.2가 고장 난 NAS SSD를 진단하고 문제를 고친 뒤 그 해결책을 재사용 가능한 skill로 패키징했기 때문입니다. | 데모 |
| [Case 174: Role-Routed Heavy-Duty Coder Stack](#case-174) | 이 사례는 역할별로 라우팅하는 개인 스택에서 GLM-5.2를 무거운 coding 작업 담당으로 둘 때 유용합니다. denizirgin은 Codex와 OpenCode를 한 달간 시험한 뒤, 월 120~140달러 수준의 총예산을 유지하면서 더 무거운 coding work를 GLM 5.2로 보내는 운영에 정착했다고 말합니다. | 평가 |
| [Case 155: Cotal Four-Agent TUI Loop](#case-155) | 이 사례는 코딩 루프를 전문 에이전트들로 분담할 때 유용합니다. 작성자는 Opus 리드와 GPT 리뷰어 아래에서 GLM-5.2 워커 두 개를 써서 lazygit 스타일 TUI를 47분 만에 사람 개입 없이 완성했습니다. | 데모 |
| [Case 153: Legacy Migration Cost-Cut Pilot](#case-153) | 이 사례는 레거시 앱 현대화 루프에서 GLM-5.2를 더 저렴한 작업 모델로 가격 평가할 때 유용합니다. 8090의 파일럿에 따르면 GLM과 Software Factory 조합은 Opus 4.8 단독 대비 비용을 16.4배 줄였지만 속도는 약 3배 느렸습니다. | 평가 |
| [Case 145: OpenCode + Fireworks 비용 절감 전환](#case-145) | open-model harness로만 바꿔도 충분한지 시험하고 싶다면 이 사례가 유용합니다. 작성자가 개인 coding과 loop 작업을 Fireworks 위 GLM-5.2 + OpenCode로 옮긴 뒤 token 비용이 3분의 1로 줄었고 일상 품질 저하도 거의 없었다고 말하기 때문입니다. | 평가 |
| [Case 143: Hermes MoA의 GLM 집계자 워크플로](#case-143) | 고가치 agent 턴에 추가 오케스트레이션이 아깝지 않다면 이 사례가 유용합니다. Hermes Agent의 Mixture of Agents 구성이 GLM-5.2와 다른 모델을 조합해, 공개된 데모에서 작은 추가 비용으로 눈에 띄게 더 나은 결과를 냈기 때문입니다. | 통합 |
| [Case 142: Cline 추론 온오프 하네스 격차](#case-142) | 모델 가중치보다 harness 설계를 보고 싶다면 이 사례가 유용합니다. 같은 GLM-5.2가 같은 코딩 작업에서 reasoning만 켰을 때 57.3%에서 68.5%로 뛰었기 때문입니다. | 평가 |
| [Case 136: Cursor + Fireworks 455M-Token 현장 테스트](#case-136) | 작성자는 Fireworks의 빠른 서빙과 함께 4억5500만 토큰 실사용을 보고하며 Opus나 GPT-5.5로 당장 돌아갈 이유가 없다고 말하므로, GLM-5.2를 Cursor 일상용 모델로 판단하려면 이 사례를 사용하십시오. | 평가 |
| [Case 135: Devin Desktop 하네스와 Skill 이식성](#case-135) | Z.ai 자체 coding surface가 불안정하게 느껴질 때 GLM-5.2를 Devin Desktop 안에서 시험하려면 이 사례를 사용하십시오. 작성자는 더 쉬운 skill 이식, 더 빠른 속도, 더 높은 hackability를 보고합니다. | 평가 |
| [Case 127: Pi 인라인 GLM 리뷰어](#case-127) | Pi 스타일 coding-agent loop에 두 번째 리뷰어를 넣고 싶을 때 쓰는 사례입니다. 작성자는 GLM-5.2가 Opus에 turn마다 조언할 수 있고, 비용 증가는 대략 10% 수준이라고 말합니다. | 통합 |
| [Case 122: AgentRouter 원샷 Telegram 봇](#case-122) | 최소 동작 코드만 내는 대신 GLM-5.2가 one-shot coding-agent build 안에서 운영 친화적인 defaults를 스스로 추론하는지 시험하려면 이 사례를 사용하십시오. | 데모 |
| [Case 117: OpenCode Go 리팩터 첫 패스 성공](#case-117) | 벤치마크 주장만 보지 않고 OpenCode 안의 중간 규모 Go 리팩터링에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오. | 평가 |
| [Case 119: Claude Code + Cursor 3.36달러 기본 실행](#case-119) | 더 자율적인 coding work를 open weights로 옮기기 전에 Claude Code와 Cursor에서 일상용 모델로서 GLM-5.2를 가늠하려면 이 사례를 사용하십시오. | 평가 |
| [One Hour Forty Two Minute Refactor Loop](#case-13) | 이 사례를 TDD, 검토자 피드백 및 회귀 확인을 통한 장기 자율 프런트엔드 리팩토링을 위한 패턴으로 사용하세요. | 데모 |
| [OpenCode Bug Fix And Implementation Test](#case-14) | 이 사례를 사용하여 버그 수정과 작은 구현 작업을 위한 OpenCode 코딩 에이전트로 GLM-5.2를 테스트하세요. | 데모 |
| [OpenCode Retro Video Game Walkthrough](#case-15) | 이 연습을 사용하여 단일 프롬프트에서 GLM-5.2 및 OpenCode를 사용하여 작은 게임을 구축한 다음 모델이 구현 세부 사항을 처리하는 방법을 검사하십시오. | 튜토리얼 |
| [HTML5 Physics Simulations Contest](#case-16) | 라이브러리 없이 자체 포함된 HTML5 물리 시뮬레이션에서 GLM-5.2와 Kimi K2.7 코드를 비교하려면 이 사례를 사용하십시오. | 평가 |
| [Personal Site UI UX Build](#case-17) | 이 사례를 사용하여 세련된 개인 사이트에 대해 GLM-5.2를 요청하고 여러 차례 전환하여 UI/UX를 얼마나 향상시킬 수 있는지 검사하십시오. | 데모 |
| [AI Contract Review Product Build](#case-18) | PRD, 시간 예산, 단계 수, 사용 할당량 및 코드 품질 비교를 통해 제품 구축 작업에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오. | 평가 |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | 더 큰 에이전트 개발 작업을 위해 GLM-5.2가 ZCode 3.0에 통합되는 방법을 이해하려면 이 사례를 사용하십시오. | 통합 |
| [GLM-5.2로 구축된 ZCode용 Linux 래퍼](#case-20) | 코딩 에이전트 환경에 대한 도구 사용을 지원하는 GLM-5.2의 예로 이 사례를 사용하십시오. | 데모 |
| [Computer Use Skill Packaging](#case-21) | 오픈 소스 컴퓨터 사용 저장소를 재사용 가능한 기술로 전환하기 위한 도우미로서 GLM-5.2를 연구하려면 이 사례를 사용하십시오. | 데모 |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | 단일 채팅 세션이 아닌 전체 에이전트 개발 환경 내에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오. | 데모 |
| [로컬 서비스를 제공하는 OpenCode 하네스](#case-62) | Claude Opus와 비교하기 전에 OpenCode 하네스, 로컬 제공 및 도구가 많은 코딩 워크플로를 사용하여 GLM-5.2를 테스트하려면 이 사례를 사용하십시오. | 평가 |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | 이 사례를 사용하면 지침을 RLM 시스템 프롬프트로 이동하여 GLM-5.2 긴 컨텍스트 계산 및 REPL 에이전트 동작을 개선할 수 있습니다. | 통합 |
| [DeepAgents Code Open Harness Trial](#case-66) | 이 사례를 사용하여 개방형 코딩 에이전트 하네스로 GLM-5.2를 시도하고 재현 가능한 에이전트 쉘에서 모델을 비교하십시오. | 데모 |
| [프로덕션 마케팅 agent stack 라우팅](#case-77) | 구조화, 속도, self-hosting 을 중시하는 production agent workflow 에 GLM-5.2를 배치하고, 모호한 판단은 더 강한 closed model 에 맡기는 라우팅 사례입니다. | 평가 |
| [M3 Ultra Pokemon Red Goal Run](#case-80) | M3 Ultra에서의 장시간 로컬 coding agent 실행에서 GLM-5.2를 판단하기 위한 사례입니다. 거의 반나절 동안 Pokemon Red를 HTML로 재현하려 한 목표 실행을 따라갈 수 있습니다. | 데모 |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | 실제 리포지토리 버그 수정에서 GLM-5.2와 Opus 4.8을 비교하려면 이 사례를 사용하십시오. GLM은 더 많은 토큰을 썼지만 더 저렴하고 더 깔끔한 최종 패치를 만들었습니다. | 평가 |
| [Case 102: OpenInspect FP8 Background Agent](#case-102) | 호스팅 챗 대신 GLM-5.2를 FP8로 돌리는 셀프호스트 background-agent stack을 살펴보려면 이 사례를 사용하십시오. | 통합 |

### [🎮 실사용 데모와 쇼케이스 빌드](#hands-on-demos-showcase-builds)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 202: Command Code Space Shooter Feature Win](#case-202) | 이 사례는 one-shot interactive UI build에서 GLM-5.2를 비교할 때 유용합니다. Command Code가 같은 retro space-shooter prompt를 Fable 5, GPT 5.5, GLM 5.2, DeepSeek V4 Pro에 돌렸고, features 기준으로 GLM을 가장 높게 평가했기 때문입니다. | 평가 |
| [Case 200: ZCode Nintendo DS Emulator](#case-200) | 이 사례는 장시간 이어지는 로컬 coding build를 살펴볼 때 유용합니다. 작성자가 4x RTX 6000 위의 ZCode에서 GLM-5.2를 돌리며 C++로 Nintendo DS 에뮬레이터를 처음부터 만드는 목표를 줬기 때문입니다. | 데모 |
| [Case 192: Command Code Flappy Bird UX Split](#case-192) | 이 사례는 GLM-5.2를 가벼운 디자인 게임 작업에서 비교할 때 유용합니다. 작성자가 같은 Flappy Bird prompt를 Command Code로 돌린 뒤, Fable 5가 GLM-5.2보다 거의 9배 비싸면서도 UX에서 결정적 우위를 보이지 못했다고 결론냈기 때문입니다. | 평가 |
| [Case 161: REAP NVFP4 Rubiks Cube One-Shot](#case-161) | 이 사례는 단일 프롬프트 상호작용 build 작업에서 GLM-5.2를 시험할 때 유용합니다. REAP-NVFP4 demo는 한 번의 prompt만으로 3D Rubiks Cube, 실제 scramble, live state, solve button까지 만들었다고 말합니다. | 데모 |
| [Case 158: OMP Relay iPhone Client](#case-158) | 이 사례는 로컬 GLM-5.2 에이전트를 빠르게 모바일 표면으로 감쌀 때 유용합니다. 작성자에 따르면 Codex의 build-ios-app plugin이 이미 GLM-5.2와 Cloudflare 터널을 쓰는 OMP relay용으로 몇 시간 만에 매끈한 iPhone 클라이언트를 만들었습니다. | 데모 |
| [Case 144: 오픈소스 DevRel 리서치 에이전트](#case-144) | GLM-5.2를 범용 채팅이 아니라 세로형 리서치 도우미로 바꾸고 싶다면 이 사례가 유용합니다. 작성자가 제품과 타깃 입력을 근거와 아웃라인이 붙은 우선순위 콘텐츠 기회로 바꿔 주는 오픈소스 DevRel 에이전트를 만들었기 때문입니다. | 데모 |
| [Case 123: Recast 6개 변형 랜딩페이지 루프](#case-123) | 먼저 여러 GLM-5.2 변형을 만든 뒤 가장 강한 결과를 coding agent로 넘겨 저비용으로 landing page를 프로토타이핑하려면 이 사례를 사용하십시오. | 튜토리얼 |
| [Playable Backrooms One-Shot](#case-23) | 이 사례를 사용하여 GLM-5.2와 Opus 4.8 간의 동일한 프롬프트 게임 구축 출력, 런타임 및 비용을 비교하세요. | 데모 |
| [결과가 혼합된 세 가지 실제 빌드](#case-24) | 이 사례를 주의사항 데모 세트로 사용하십시오. 프로덕션 게임 또는 비디오 작업에 대한 모델을 신뢰하기 전에 여러 실제 빌드를 테스트하십시오. | 평가 |
| [Super Mario Clone In ZCode](#case-25) | 이 사례를 사용하여 여러 수정 및 기능 단계에 걸쳐 GLM-5.2 및 ZCode를 사용한 반복적인 게임 구축을 평가합니다. | 데모 |
| [Lunar Lander Contest](#case-26) | 대화형 게임 스타일 작업에서 GLM-5.2, MiniMax M3 및 Kimi K2.7 코드를 비교하려면 이 사례를 사용하십시오. | 평가 |
| [One-Prompt Design Arena Creation](#case-27) | 이 사례를 사용하여 경기장 상황에서 단일 디자인 프롬프트에서 GLM-5.2가 생성할 수 있는 내용을 검사합니다. | 데모 |
| [연구 논문 워크플로우 이해](#case-28) | 상황에 맞는 질문과 논문 간 참조가 포함된 논문 읽기 작업 흐름에 GLM-5.2를 적용하려면 이 사례를 사용하세요. | 통합 |
| [Constrained Poem Comparison](#case-29) | GLM-5.2를 Fable 스타일 모델과 비교할 때 창의적 품질과 정확성을 분리하려면 이 사례를 사용하십시오. | 평가 |
| [Design Sense Example](#case-30) | 이 사례를 간단한 시각적 디자인 신호로 사용한 다음 자체 프롬프트와 UI 검토를 통해 확인하세요. | 데모 |
| [Temple Run 스타일 복셀 게임 원샷 생성](#case-71) | 단일 프롬프트 게임 생성에서 GLM-5.2를 stress-test 하고, 시각적으로 풍부한 빌드에서 무엇이 추가 수정이 필요한지 확인하는 사례입니다. | 데모 |
| [OpenCode Go 원샷 예시 세트](#case-78) | 더 open-ended 한 agent loop 에 투입하기 전에 OpenCode Go 안의 quick one-shot build 에서 GLM-5.2를 benchmark 하는 사례입니다. | 데모 |
| [Space Invaders One-Prompt Build](#case-81) | 단일 프롬프트 게임 생성에서 GLM-5.2를 시험하고, 몇 번의 추가 프롬프트로 asset 교체와 가벼운 polish가 어떻게 진행되는지 보기 위한 사례입니다. | 데모 |
| [OpenCode Recovery Lab One-Shot](#case-82) | 대화형 agent failure simulation을 빠르게 프로토타이핑하기 위한 사례입니다. 작성자는 약 3.50달러로 동작하는 recovery lab을 one-shot으로 만들었다고 보고합니다. | 데모 |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | 참조 기반 웹 재현에서 GLM-5.2를 시험하려면 이 사례를 사용하십시오. 소스 URL 하나와 간단한 프롬프트 하나만으로 사이트를 거의 픽셀 수준으로 재현했습니다. | 데모 |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | 풀스택 UI 빌드에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오. 가장 세련된 트레이딩 데스크 결과에 근접했지만 비용은 최상위 결과의 일부에 불과했습니다. | 평가 |
| [Case 100: Luddite Game After Claude Refusal](#case-100) | 폐쇄형 모델이 거절한 게임 아이디어를 GLM-5.2로 대체 프로토타이핑하고 실제 출력물을 직접 검토하려면 이 사례를 사용하십시오. | 데모 |

### [🔌 공급자 및 도구 통합](#provider-tool-integrations)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 208: Open Molecular Viewer Agent Stack](#case-208) | 이 사례는 GLM-5.2를 열린 scientific inspection workflow에 연결할 때 유용합니다. MaziyarPanahi가 Hugging Face Inference Providers 경유 GLM-5.2를 llama.cpp 위의 Qwen3-VL, Mol*, PydanticAI와 묶어 하나의 prompt로 EGFR와 erlotinib 구조를 렌더링하고 비평했기 때문입니다. | 통합 |
| [Case 204: Perplexity Advisor WANDR Cost Baseline](#case-204) | 이 사례는 routing된 computer-use harness 안에서 GLM-5.2의 경제성을 추정할 때 유용합니다. Perplexity가 GLM 5.2 plus advisor setup이 WANDR 2.1x, Opus 6.1x라고 밝히며 전체 benchmark에서도 비용이 거의 절반 수준이라고 했기 때문입니다. | 평가 |
| [Case 203: Coworker Open Artifacts Routing](#case-203) | 이 사례는 GLM-5.2를 enterprise artifact workflow에 넣고 싶을 때 유용합니다. Coworker는 Open Artifacts가 docs, decks, PDF, spreadsheets, dashboards, apps를 만들 수 있고, optimized router가 토큰 사용량을 약 5배 줄이면서도 미국 호스팅 GLM 5.2를 제공한다고 말합니다. | 통합 |
| [Case 201: DotCode Context Upload Workflow](#case-201) | 이 사례는 private coding sandbox 안에서 GLM-5.2에 더 풍부한 project context를 주고 싶을 때 유용합니다. DotCode가 GLM 5.2 지원과 함께 screenshot, image, CSV, PDF, source file, zip 업로드를 같은 filesystem-and-terminal workflow로 넣을 수 있게 했기 때문입니다. | 통합 |
| [Case 198: Dahl 100M Free GLM Endpoint](#case-198) | 이 사례는 카드 없이 OpenAI-compatible 경로로 GLM-5.2를 시험해 볼 때 유용합니다. Dahl Inference가 GLM 5.2 FP8에 대해 100M 무료 토큰을 제공하고, key 생성과 `/v1/chat/completions` 호출 방법까지 보여 주기 때문입니다. | 튜토리얼 |
| [Case 195: NVIDIA Free Endpoint GLM Setup](#case-195) | 이 사례는 self-hosting 없이 coding tool에서 GLM-5.2를 시험해 볼 때 유용합니다. source가 무료 NVIDIA endpoint 흐름으로 GLM-5.2 API key를 Claude Code, Cursor, Cline에 넣는 방법을 설명하기 때문입니다. | 튜토리얼 |
| [Case 193: 0G TeeML Private Inference Route](#case-193) | 이 사례는 GLM-5.2를 privacy-first provider 경로로 붙일 때 유용합니다. 0G가 GLM 5.2가 TeeML에서 TEE enclave 안에 prompt를 봉인한 채 실행되고, 가격도 공식 경로보다 낮다고 말했기 때문입니다. | 통합 |
| [Case 185: DuckDB Flock Open-SQL PR](#case-185) | 이 사례는 GLM-5.2를 완전히 열린 로컬 SQL analysis 스택에 넣고 싶을 때 유용합니다. lhoestq에 따르면 duckdb와 flock PR로 GLM-5.2를 100% open-source 데이터 스택 안에서 쓸 수 있기 때문입니다. | 통합 |
| [Case 179: One-Key 26-Model API Access](#case-179) | 이 사례는 하나의 OpenAI 호환 제공자 경로로 GLM-5.2를 시험할 때 유용합니다. Alan_Earn에 따르면 API 키 하나로 GLM-5.2를 포함한 26개 모델에 접근할 수 있고 시작 크레딧 26달러도 함께 제공되기 때문입니다. | 튜토리얼 |
| [Case 176: NVIDIA NIM OpenCode Thinking Setup](#case-176) | 이 사례는 thinking을 명시적으로 켠 무비용 경로로 NVIDIA 무료 NIM endpoint를 통해 GLM-5.2를 OpenCode에 연결하고 싶을 때 쓰기 좋습니다. Dracoshowumore는 API key 발급 흐름, base URL, 그리고 tool layer가 function calls를 맡는 동안 GLM은 enable_thinking=true로 돌리는 OpenCode 설정을 공유합니다. | 튜토리얼 |
| [Case 165: ZCode Launch With Mobile Agent Control](#case-165) | 이 사례는 ZCode를 GLM-5.2의 공식 coding surface로 평가할 때 유용합니다. launch report에 따르면 이 무료 agentic IDE는 Windows, macOS, Linux에서 제공되며 Telegram, WeChat, Feishu로 프로젝트 진행 상황을 확인할 수 있습니다. | 통합 |
| [Case 160: OpenWiki Auto-Maintained Agent Docs](#case-160) | 이 사례는 agent가 읽는 문서를 자동으로 최신 상태로 유지하고 싶을 때 유용합니다. LangChain에 따르면 OpenWiki는 코드 변경에 맞춰 repo docs를 다시 만들고 유지하며 GLM 5.2 같은 open model 위에서 동작합니다. | 통합 |
| [Case 152: Foundry PTUs Through FireConnect](#case-152) | 이 사례를 쓰면 에이전트 클라이언트를 다시 만들지 않고도 기업용 Foundry 예산으로 GLM-5.2를 라우팅할 수 있습니다. Fireworks에 따르면 FireConnect가 Microsoft Foundry PTU를 Codex, OpenCode, Pi 워크플로에 연결해 주기 때문입니다. | 통합 |
| [Case 141: ClinePass 오픈웨이트 정액 구독](#case-141) | 여러 open-weight 코딩 모델을 하나의 agent harness 안에 모으고 싶다면 이 사례가 유용합니다. ClinePass가 GLM-5.2와 관련 모델을 provider별 키와 청구서 대신 월정액으로 묶기 때문입니다. | 통합 |
| [Case 137: 코딩 에이전트를 위한 무료 GLM API 서비스](#case-137) | Hermes나 다른 coding agent에서 가입 없이 GLM-5.2를 시험하려면 이 사례를 사용하십시오. 공유 서비스가 짧게 유지되는 API key를 발급해 설정을 가볍게 유지한다고 설명합니다. | 통합 |
| [Case 128: Cloudflare Workers AI OpenCode 설정](#case-128) | 직접 모델 호스트를 준비하지 않고, coding agent용 무료 OpenAI 호환 경로로 Cloudflare Workers AI를 통해 GLM-5.2를 돌리고 싶을 때 쓰는 사례입니다. | 튜토리얼 |
| [Case 129: Puter.js 무설정 브라우저 클라이언트](#case-129) | API key, 과금, 백엔드 설정을 건드리기 전에 브라우저 전용 프로토타입에서 GLM-5.2를 시험하고 싶을 때 쓰는 사례입니다. | 튜토리얼 |
| [Case 130: SiliconFlow 통합 엔드포인트 접근](#case-130) | 게시물은 무료 체험 credit이 붙은 단일 OpenAI 호환 SiliconFlow endpoint로 중국계와 서구권 모델을 함께 다룰 수 있다고 설명하므로, GLM-5.2를 더 넓은 multi-model stack 안에 넣고 싶을 때 쓰는 사례입니다. | 통합 |
| [Case 124: HuggingChat 웹사이트 빌드와 HF Space 배포](#case-124) | HuggingChat 조사부터 Hugging Face Spaces 정적 배포까지, 거의 무료에 가까운 개인 사이트 흐름에서 GLM-5.2를 써보고 싶을 때 쓰는 사례입니다. | 튜토리얼 |
| [Case 125: DigitalOcean Inference Engine 제공](#case-125) | 1M context 모델을 직접 호스팅하지 않고 공식 provider access를 managed infrastructure로 쓰고 싶을 때 GLM-5.2를 라우팅하는 사례입니다. | 통합 |
| [Case 115: Command Code Fast 120-250 Tok/S 티어](#case-115) | 가장 싼 진입 가격만이 아니라 장기 코딩 속도를 중시할 때 Command Code의 더 빠른 GLM-5.2 tier에 접근하려면 이 사례를 사용하십시오. | 통합 |
| [Case 116: Vercel AI Gateway Fast GLM-5.2 API](#case-116) | 서버리스 속도와 명시적 토큰 가격이 필요할 때 Vercel AI Gateway를 통해 GLM-5.2 Fast를 쓰려면 이 사례를 사용하십시오. | 통합 |
| [OpenCode Go Availability](#case-31) | 이 사례를 사용하면 텍스트, 1M 컨텍스트 및 GLM-5.1과 유사한 가격으로 OpenCode Go 워크플로 내에서 GLM-5.2 가용성을 추적할 수 있습니다. | 통합 |
| [Ollama Cloud Availability](#case-32) | 이 사례를 사용하여 액세스 가능한 오픈 소스 코딩 모델 실험을 위해 GLM-5.2를 Ollama Cloud로 라우팅합니다. | 통합 |
| [OpenRouter One API Call Access](#case-33) | 공급자 라우팅 또는 다중 모델 스택을 비교할 때 OpenRouter를 통해 GLM-5.2에 액세스하려면 이 사례를 사용하십시오. | 통합 |
| [vLLM Day-Zero Support](#case-34) | 이 사례를 사용하면 Day-Zero 지원이 포함된 vLLM을 통해 GLM-5.2를 자체 호스팅하거나 제공할 수 있습니다. | 통합 |
| [Notion Availability Via Baseten](#case-35) | 이 사례를 사용하여 GLM-5.2를 Notion 워크플로 내에서 사용할 수 있는 개방형 모델로 식별하세요. | 통합 |
| [Fireworks Day-Zero Serving](#case-36) | 이 사례를 사용하여 Fireworks를 호스팅된 인프라가 필요한 GLM-5.2 워크로드에 대한 제공 경로로 평가합니다. | 통합 |
| [Google Cloud 모델 Garden 링크](#case-37) | 이 사례를 사용하여 Google Cloud 기반 배포 및 에이전트 플랫폼 컨텍스트에서 GLM-5.2를 찾으세요. | 통합 |
| [Venice Privacy Mode](#case-38) | 개인 정보 보호 모드, TEE 또는 종단 간 암호화가 GLM-5.2를 시도하는 데 결정적인 요소인 경우 이 사례를 사용하십시오. | 통합 |
| [Command Code Availability](#case-39) | 이 사례를 통해 저렴한 진입 계획과 긴 컨텍스트 코딩 기능을 갖춘 명령 코드의 GLM-5.2를 사용해 보세요. | 통합 |
| [Nous Portal의 헤르메스 에이전트](#case-40) | Nous Portal 및 OpenRouter를 통해 GLM-5.2를 Hermes Agent 워크플로에 연결하려면 이 사례를 사용하세요. | 통합 |
| [io.net Day-Zero Launch Partner](#case-41) | 753B 매개변수 긴 컨텍스트 모델에 대한 컴퓨팅 지원 제공을 평가할 때 이 사례를 사용하세요. | 통합 |
| [Modular Cloud Day-Zero Serving](#case-42) | 공급자 규모에서 제공되는 장기 컨텍스트 GLM-5.2용 Modular Cloud를 고려하려면 이 사례를 사용하세요. | 통합 |
| [Cursor Setup Through OpenRouter](#case-61) | 저렴한 개방형 모델 코딩 워크플로우를 위해 OpenRouter를 통해 Cursor에서 GLM-5.2를 구성하려면 이 사례를 사용하십시오. | 튜토리얼 |
| [Amp Agentic Eyes For Visual Design](#case-63) | 텍스트 전용 모델에 디자인 작업을 위한 시각적 검토 지원이 필요한 경우 이 사례를 사용하여 GLM-5.2를 Amp 사용자 지정 에이전트와 페어링합니다. | 통합 |
| [Baseten Faster One-Million-Context Serving](#case-69) | Factory Droid, OpenCode 및 코딩 하네스에 대해 긴 컨텍스트 제공 속도가 중요한 경우 이 사례를 사용하여 Baseten을 통해 GLM-5.2를 라우팅합니다. | 통합 |
| [웹 디자인용 Browser Use QA subagents](#case-74) | text-only model 에 시각 검수가 필요할 때 GLM-5.2를 Browser Use v2의 multimodal QA subagents 와 조합해 반복적인 웹사이트 수정에 쓰는 사례입니다. | 통합 |
| [ZCode 공식 IDE 일일 무료 토큰](#case-79) | 큰 daily token allowance 와 Cursor 유사 workflow 를 제공하는 무료 공식 coding IDE 로 ZCode 를 통해 GLM-5.2에 접근하는 사례입니다. | 튜토리얼 |
| [Cursor Setup Through Fireworks](#case-83) | Fireworks를 통해 GLM-5.2를 Cursor에 최소 설정으로 연결하고, 별도 클라이언트 코드 없이 시험하기 위한 사례입니다. | 튜토리얼 |
| [VulcanBench ZAI Provider Support](#case-84) | 전용 ZAI provider 지원과 API key 경로를 갖춘 오픈 benchmark harness에서 GLM-5.2를 실행하기 위한 사례입니다. | 통합 |
| [OpenCode High/Max Reasoning Variants](#case-85) | OpenCode 안에서 GLM-5.2의 High / Max reasoning variant에 접근하면서 step-limit 처리 개선까지 함께 가져오기 위한 사례입니다. | 통합 |
| [Z.ai Coding Endpoint Selection](#case-86) | GLM-5.2 coding plan 트래픽을 일반 API가 아니라 coding 최적화 Z.ai endpoint로 보내기 위한 사례입니다. | 튜토리얼 |
| [ZenMux Free GLM-5.2 API Setup](#case-87) | 무료 GLM-5.2 API key와 base URL을 받아 Claude, Cursor, Hermes 같은 도구에 연결하기 위한 사례입니다. | 튜토리얼 |
| [Case 93: Noumena ncode GLM Default](#case-93) | 기본 모델 지원과 함께 표준 엔드포인트와 1M 컨텍스트 엔드포인트를 분리한 ncode 및 Noumena 스타일 에이전트 환경에 GLM-5.2를 라우팅하려면 이 사례를 사용하십시오. | 통합 |
| [Case 95: Claude Code Through Baseten](#case-95) | Baseten 키, 커스텀 base URL, `~/.claude/settings.json`의 모델 재매핑을 통해 Claude Code 안에서 GLM-5.2를 실행하려면 이 사례를 사용하십시오. | 튜토리얼 |
| [Case 96: Deepsec Pi Agent Default](#case-96) | 보안 하네스에서 GLM-5.2를 시험하려면 이 사례를 사용하십시오. `deepsec`는 Pi agent의 기본 모델로 채택했고 경쟁력 있는 eval 결과를 보고했습니다. | 통합 |
| [Case 101: Baseten + Droid Harness Quickstart](#case-101) | Baseten과 Droid harness를 통해 GLM-5.2를 빠르게 띄우고 다른 IDE에도 재사용할 수 있는 짧은 설정 흐름을 확보하려면 이 사례를 사용하십시오. | 튜토리얼 |
| [Case 104: OpenAI-Compatible GLM API Workflow](#case-104) | reasoning control, tool calling, 장문맥 retrieval, cost tracking을 갖춘 OpenAI 호환 GLM-5.2 클라이언트를 Python으로 구성하려면 이 사례를 사용하십시오. | 튜토리얼 |
| [Case 105: Perplexity Agent API Search Sandbox](#case-105) | search 지원 sandboxed agent를 단일 API call 뒤에 두고 싶을 때 Perplexity Agent API에 GLM-5.2를 연결하려면 이 사례를 사용하십시오. | 통합 |
| [Case 109: Baseten 280 TPS GLM API](#case-109) | 제공업체 지연 시간이 중요할 때 Baseten이 주장한 GLM-5.2의 고속 serving 신호를 확인하려면 이 사례를 사용하십시오. | 통합 |

### [💸 비용, 가격, 로컬 배포](#cost-pricing-local-deployment)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 209: Colibri 25GB RAM Sparse Streaming](#case-209) | 이 사례는 로컬 GLM-5.2 실험의 새로운 하한을 파악할 때 유용합니다. techNmak이 Colibrì가 NVMe에서 expert를 스트리밍해 약 25GB RAM으로 744B MoE를 돌리지만, 가장 작은 구성은 대략 0.05~0.1 tok/s에 머문다고 설명하기 때문입니다. | 데모 |
| [Case 206: SGLang NVFP4 Production Throughput](#case-206) | 이 사례는 GLM-5.2 NVFP4용 프로덕션 SGLang serving 규모를 가늠할 때 유용합니다. 공식 SGLang v0.5.15 release가 batch size 1에서 8x B300은 사용자당 500+ tok/s, 4x GB300은 450 tok/s에 도달했다고 말하기 때문입니다. | 평가 |
| [Case 191: Hermes-Built LiteLLM Local Lab](#case-191) | 이 사례는 GLM-5.2를 coding agent로 써서 local inference lab을 부트스트랩할 때 유용합니다. source에서 Hermes Agent와 GLM-5.2가 M3 Ultra 기반으로 LiteLLM, Postgres, Prometheus, Grafana를 연결했다고 말하기 때문입니다. | 통합 |
| [Case 187: Dual M5 Max Offline Droneship Sim](#case-187) | 이 사례는 완전 offline Apple Silicon 환경에서 GLM-5.2 agent가 어디까지 가능한지 가늠할 때 유용합니다. XavierLocalAI가 두 대의 128GB M5 Max로 753B 구성을 돌리며 droneship landing simulator를 26 tok/s로 작성했다고 보고했기 때문입니다. | 데모 |
| [Case 186: 5x DGX Spark Production Harness](#case-186) | 이 사례는 5노드 DGX Spark 구성이 production GLM-5.2 작업에 충분한지 판단할 때 유용합니다. thatcofffeeguy가 400K context에서 단일 스트림 약 13.9 tok/s와 3개 lane 합산 19.9 tok/s를 live harness에서 보고했기 때문입니다. | 데모 |
| [Case 183: M3 Ultra ds4-eval Q4 Checkpoint](#case-183) | 이 사례는 Apple Silicon 단일 박스 GLM-5.2 구성을 ds4-eval로 benchmark할 때 유용합니다. ivanfioravanti가 M3 Ultra 512GB 머신에서 q4 실행 약 16 tok/s, 92개 중 76개 통과, 총 8시간 53분을 보고했기 때문입니다. | 평가 |
| [Case 182: 4x RTX PRO 6000 Build Guide](#case-182) | 이 사례는 진지한 로컬 GLM-5.2-594B 구축 범위를 잡을 때 유용합니다. QingQ77가 4장의 RTX PRO 6000, opencode로 노출한 API, 그리고 agent 작업용 sandbox VM을 중심으로 한 전체 하드웨어 및 운영 가이드를 공유했기 때문입니다. | 튜토리얼 |
| [Case 181: 4x DGX Spark QuantTrio Run](#case-181) | 이 사례는 4노드 DGX Spark 클러스터에서 GLM-5.2 QuantTrio가 어느 정도까지 나오는지 추정할 때 유용합니다. Tech2Wild가 200K context와 함께 단일 스트림 30 tok/s, 6동시 요청에서 총 60.5 tok/s를 보고했기 때문입니다. | 데모 |
| [Case 177: Single M3 Ultra 4-Bit Video Run](#case-177) | 이 사례는 Apple Silicon 단일 머신에서 GLM-5.2가 어느 정도 실용적인지 가늠할 때 유용합니다. ivanfioravanti는 M3 Ultra 512GB 한 대에서 4-bit 실행이 약 16 tok/s로 도는 모습을 보여주고, q2 ds4-eval 영상이 약 17 tok/s라는 점과 비교합니다. | 데모 |
| [Case 166: Full 744B On 5x ASUS GX10s](#case-166) | 이 사례는 극단적인 home-lab GLM-5.2 배치를 가늠할 때 유용합니다. 작성자에 따르면 744B 풀 모델이 5대의 ASUS GX10 박스에서 full context로 돌고 있고, 실제 workload용 causal harness에도 이미 연결돼 있습니다. | 데모 |
| [Case 164: Agent Route Swap In China Stack](#case-164) | 이 사례는 최고 품질보다 비용 압박이 더 중요한 상황에서 mixed-model stack의 agent layer로 GLM-5.2를 라우팅할 때 참고가 됩니다. 작성자에 따르면 Sonnet을 GLM-5.2로 바꾸자 해당 slot의 input cost가 5배 줄고 품질 저하는 약 3 percent였습니다. | 평가 |
| [Case 156: 744B Local Hardware Floor](#case-156) | 이 사례를 쓰면 GLM-5.2 로컬 운용 계획을 현실적으로 잡을 수 있습니다. 출처에 따르면 양자화 버전도 2비트 약 239GB, 4비트 약 466GB 수준이라서 RAM이나 VRAM 256GB 이상이 사실상 바닥선이기 때문입니다. | 제한 |
| [Case 140: B300 x2 에이전트 주도 듀얼 스택 Bring-Up](#case-140) | thread는 분석가들이 베어메탈 B300 두 장에서 vLLM과 SGLang 양쪽으로 NVFP4 추론을 하루도 안 돼 세웠다고 보여 주므로, 본격적인 셀프호스트 GLM-5.2 배포 범위를 가늠하려면 이 사례를 사용하십시오. | 평가 |
| [Case 139: oMLX M3 Ultra Prefill 속도 향상](#case-139) | 최근 커널 작업 이후 Apple Silicon 로컬 실행 가능성을 다시 확인하려면 이 사례를 사용하십시오. 보고된 M3 Ultra 512GB의 GLM-5.2 prefill 속도는 간단한 테스트에서 뚜렷한 품질 붕괴 없이 거의 두 배가 됐습니다. | 평가 |
| [Case 138: 가입 시 2천만 토큰 크레딧 버스트](#case-138) | 직접 가입 크레딧만으로도 실제 GLM-5.2 체험이 가능한지 평가하려면 이 사례를 사용하십시오. 게시물은 신규 계정에 카드 없이 2천만 무료 토큰과 완전한 OpenAI 호환 접근이 제공된다고 주장합니다. | 통합 |
| [Case 131: 4x DGX Spark 로컬 GLM 운영 가이드](#case-131) | DGX Spark 클러스터가 현실적인 로컬 GLM-5.2 경로인지 가늠하려 할 때 쓰는 사례입니다. 모아둔 가이드는 구체적 하드웨어 비용, 클러스터 토폴로지, vLLM 명령을 1M context GLM 목표와 연결합니다. | 튜토리얼 |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 실행](#case-112) | 고성능 워크스테이션을 들이기 전에 4 GPU 로컬 GLM-5.2 구성을 까다로운 terminal benchmark에 맞춰 가늠하려면 이 사례를 사용하십시오. | 평가 |
| [Case 118: 2x RTX PRO 6000 Blackwell 로컬 Crackme 풀이](#case-118) | 디버거 없이도 본격적인 로컬 GLM-5.2 구성이 장시간 리버스엔지니어링 과제를 끝낼 수 있는지 판단하려면 이 사례를 사용하십시오. | 데모 |
| [Output Token Cost Comparison](#case-43) | 이 사례를 사용하여 GLM-5.2 출력 토큰 경제성을 Opus, Fable 및 GPT-5.5 스타일 모델과 비교합니다. | 평가 |
| [Local Near-Frontier Hardware ROI](#case-44) | 이 사례를 사용하여 자체 호스팅 GLM-5.2 유사 모델이 헤비 에이전트 사용자의 하드웨어 비용을 상환할 수 있는지 여부를 추론합니다. | 평가 |
| [MLX On Two Mac Studios](#case-45) | 이 사례를 사용하여 Apple 하드웨어 및 MLX 지향 설정에서 실행되는 로컬 GLM-5.2를 살펴보세요. | 데모 |
| [H100 Monthly Local Deployment Claim](#case-46) | 구독과 자체 호스팅 중에서 선택하기 전에 로컬 배포 가정을 확인하기 위한 비용 비교 프롬프트로 이 사례를 사용하세요. | 평가 |
| [Daily Credits And Claude Replacement Claim](#case-47) | 이 사례를 사용하여 GLM-5.2에 대한 무료 크레딧 및 교체 에이전트 설명을 검사하는 동시에 마케팅 주장과 검증된 워크로드 적합성을 분리합니다. | 평가 |
| [Free ZCode Token Window](#case-48) | 유료 공급자 또는 로컬 배포를 시작하기 전에 무료 ZCode 허용을 통해 GLM-5.2를 테스트하려면 이 사례를 사용하십시오. | 통합 |
| [ZenMux Free Week Offer](#case-49) | GLM-5.2 테스트를 위해 시간 제한이 있는 무료 액세스 창을 찾으려면 이 사례를 사용하십시오. | 통합 |
| [crofAI 토큰별 가격](#case-50) | 경로를 선택하기 전에 이 사례를 사용하여 GLM-5.2에 대한 타사 공급자 가격을 비교하세요. | 통합 |
| [API Price Margin Comparison](#case-51) | GLM-5.2를 다른 개척 연구실 및 개방형 모델과 비교할 때 이 사례를 시장 가격 비평으로 사용하십시오. | 평가 |
| [Basement Local Inference Speed](#case-64) | 오프라인 코딩 설정을 계획하기 전에 이 사례를 사용하여 대용량 메모리 Apple 하드웨어에서 로컬 GLM-5.2 추론 처리량을 추정하세요. | 데모 |
| [Unsloth Quantized Local Deployment](#case-68) | 전체 모델 가중치가 일반 로컬 하드웨어에 비해 너무 큰 경우 이 사례를 사용하여 양자화된 GLM-5.2 배포 경로를 평가합니다. | 튜토리얼 |
| [Two M3 Ultra MLX Distributed Run](#case-88) | 더 큰 Apple Silicon 구성을 짜기 전에, 두 대의 M3 Ultra에 분산 MLX로 올린 GLM-5.2 8-bit serving 모습을 가늠하기 위한 사례입니다. | 데모 |
| [ZCode Multiplier Cut Through September](#case-89) | peak / off-peak multiplier 인하 기간을 활용해 GLM-5.2 plan credits를 더 오래 쓰기 위한 사례입니다. | 통합 |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | 고급 로컬 GLM-5.2 워크스테이션 규모를 가늠하려면 이 사례를 사용하십시오. Blackwell 두 장을 쓴 데스크톱이 4-bit 양자화 빌드에서 두 자릿수 디코드 속도를 유지했습니다. | 데모 |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | 로컬 GLM-5.2 추론용 Mac Studio 구매가 합리적인지 점검하려면 이 사례를 사용하십시오. 게시된 회수 계산은 대부분의 사용자에게 API나 플랜 접근이 더 유리하다는 쪽에 무게를 둡니다. | 평가 |
| [Case 106: LiteLLM Local Outage Save](#case-106) | 호스팅 frontier API가 다운되거나 한도에 걸려도 LiteLLM을 통해 로컬 GLM-5.2로 우회해 납기 작업을 계속하려면 이 사례를 사용하십시오. | 데모 |
| [Case 107: Individual Versus Team Local ROI](#case-107) | 로컬 GLM-5.2 배포가 개인에게 맞는지, 더 큰 개발팀에 더 적합한지 판단하려면 이 사례를 사용하십시오. | 평가 |

### [🧭 한계, 주의점, 안전 신호](#limits-caveats-safety-signals)

| 사례 | 핵심 포인트 | 유형 |
|---|---|---|
| [Case 205: Static HTML Rewrite Executor Misses](#case-205) | 이 사례는 1:1 legacy rewrite를 GLM-5.2에게 executor로 통째로 맡기지 않기 위해 유용합니다. 큰 static HTML을 React와 Vite로 옮기는 작업에서 OpenCode Go와 Cline을 써도 디테일이 많이 빠졌고, 작성자가 GLM을 executor보다 planner 쪽으로 보게 됐기 때문입니다. | 한계 |
| [Case 197: Composio 47-Task Agent Gaps](#case-197) | 이 사례는 GLM-5.2가 실제 SaaS-agent 작업에서 어디서 아직 무너지는지 이해할 때 유용합니다. Composio가 17개 도구와 47개 작업에 연결해 45개는 통과했지만, 완전성 점검과 모호한 SLA 판단에서 실패했기 때문입니다. | 평가 |
| [Case 163: Preliminary Cyber Research Parity](#case-163) | 이 사례는 vulnerability research 하위 작업에서 GLM-5.2를 가늠할 때 유용합니다. Irregular는 좁은 cyber suite에서 GPT-5.4와 Opus 4.6에 필적하는 초기 내부 평가를 보고하면서도, end-to-end attack scenario는 아직 검증되지 않았다고 명시합니다. | 제약 |
| [Case 157: OpenRouter Spend-Cut Skill Rewrite](#case-157) | 이 사례는 에이전트 모델을 바꾸기 전에 마이그레이션 비용을 잡을 때 유용합니다. 한 펀드의 OpenRouter 시험에서 GLM-5.2는 Opus 비용의 약 8분의 1 수준이었지만, 스킬 재작성과 라우팅 로직, 그리고 더 느리고 약한 출력을 감수해야 했습니다. | 제한 |
| [Case 134: Semgrep IDOR 좁은 승리 주의점](#case-134) | 출처는 GLM-5.2가 하나의 IDOR benchmark에서 Claude Code를 이겼다고 말하지만 Mythos 자체와의 비교는 아니라고 하므로, 실제 보안 신호와 과장된 헤드라인을 분리하려면 이 사례를 사용하십시오. | 한계 |
| [Case 132: LisanBench 추론 효율 격차](#case-132) | reasoning 비중이 큰 workload에서 GLM-5.2를 확인하려 할 때 쓰는 사례입니다. 게시된 LisanBench 결과는 GLM-5보다 낫지만 다른 오픈 모델과 비교하면 아직 비효율적이라는 점을 보여줍니다. | 한계 |
| [Case 133: PrinzBench 도메인 불일치 주의점](#case-133) | 게시물은 약한 PrinzBench 점수와 훨씬 강한 software·tool-use benchmark를 대비하므로, GLM-5.2를 법률 리서치보다 coding과 agent execution에 집중시키려 할 때 쓰는 사례입니다. | 한계 |
| [Case 126: Rust 버그는 통과하지만 턴 수는 7배](#case-126) | GLM-5.2가 버그 자체는 통과시켜도 Opus보다 훨씬 많은 턴을 태울 수 있으므로, 코드 품질의 장점과 현재 agent harness overhead를 분리해 보려는 사례입니다. | 평가 |
| [Case 114: Braintrust 모델 교체 비용 경고](#case-114) | 실제 agentic coding workflow에서 더 싼 모델로 바꾸면 품질도 유지될 것이라고 쉽게 가정하지 않으려면 이 사례를 사용하십시오. | 평가 |
| [No Vision Caveat](#case-52) | 이 사례를 사용하여 GLM-5.2는 기본 비전 기능이 필요한 작업 흐름에 덜 유용할 수 있다는 점을 기억하세요. | 한계 |
| [실제 에이전트 격차 주의 사항](#case-53) | 이 사례를 사용하면 GLM-5.2가 배포된 모든 에이전트 작업에서 최고의 독점 모델과 일치한다는 증거로 벤치마크 승리를 과도하게 읽는 것을 방지할 수 있습니다. | 한계 |
| [Safety Guardrail Concern](#case-54) | 민감한 도메인에 GLM-5.2를 배포하기 전에 안전성 평가를 실행하라는 알림으로 이 사례를 사용하십시오. | 한계 |
| [벤치마크 방법론 비평](#case-55) | 헤드라인 결과가 GLM-5.2를 선호하는 경우에도 이 사례를 사용하여 벤치마크 방법론에 의문을 제기합니다. | 한계 |
| [Peak-Time Latency Concern](#case-56) | 코딩 계획을 전환하거나 Claude Code 스타일 워크플로를 GLM-5.2로 라우팅하기 전에 이 사례를 사용하여 공급자 대기 시간을 테스트하세요. | 한계 |
| [FutureSim Non-Improvement Result](#case-57) | 광범위한 배포 전에 코딩 이득이 비코딩 도메인에 일반화되는지 확인하려면 이 사례를 사용하십시오. | 한계 |
| [Launch Readiness Critique](#case-58) | 이 사례를 사용하여 실행 실행, 문서화, API 준비와 모델 기능을 분리하세요. | 한계 |
| [코딩플랜 가격 인상](#case-59) | GLM-5.2를 저렴한 대체품으로 추천하기 전에 이 사례를 사용하여 요금제 가격을 확인하세요. | 한계 |
| [짧은 병렬 작업과 긴 에이전트 실행 비교](#case-67) | 이 사례를 사용하여 GLM-5.2를 짧은 제한 코딩 작업으로 라우팅하는 동시에 더 깊은 다중 시간 에이전트 실행을 위해 더 강력한 모델을 예약합니다. | 한계 |
| [코드 검열과 편향 점검](#case-73) | 코드와 정치적 편향 테스트를 위한 실용적인 safety signal 로 보는 사례이며, 더 넓은 alignment 문제가 해결됐다는 증거로 봐서는 안 됩니다. | 한계 |
| [고난도 추론 과금 failure](#case-75) | hard reasoning workload 에서 GLM-5.2를 신중히 테스트하기 위한 사례입니다. 공개 보고에는 긴 실행 시간, 낮은 완료율, 예상 밖으로 높은 과금 출력이 나타납니다. | 한계 |
| [Case 103: HalluHard Multiturn Hallucination Signal](#case-103) | 다른 벤치마크 성능을 신뢰하기 전에 환각에 민감한 멀티턴 작업에서 GLM-5.2를 검증하려면 이 사례를 사용하십시오. | 한계 |
| [Case 108: Open-Weight Security Emergency Warning](#case-108) | open-weight GLM-5.2가 offensive security agent의 운영 마찰을 낮춘다는 안전 계획 신호로 이 사례를 사용하십시오. | 한계 |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 벤치마크와 프런티어 평가
---
<a id="case-207"></a>
### Case 207: [Stable Fluids Browser Benchmark](https://x.com/AlicanKiraz0/status/2075639232169705781) (작성자 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**이 사례는 알고리즘 비중이 큰 브라우저 물리 빌드에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0가 Stable Fluids HTML benchmark를 실행해 GLM 5.2 Max에 100점 만점 중 88점과 약 1.17달러의 비용을 매겼고, Opus 4.8과 Fable 5를 앞섰지만 GPT 5.6 Sol에는 뒤졌기 때문입니다.**

이 benchmark는 각 모델에게 semi-Lagrangian advection, iterative diffusion, pressure projection, live divergence reporting, 그리고 interactive paint와 velocity injection이 들어간 Jos Stam stable fluids를 하나의 self-contained HTML file로 구현하게 합니다. AlicanKiraz0는 GLM 5.2 Max가 100점 중 88점을 기록해 Opus 4.8의 86점과 Fable 5의 81점을 앞섰고 비용도 훨씬 낮았다고 말하며, 이 포스트를 단순 취향형 frontend 비교가 아니라 수치적 정확성과 실시간 브라우저 성능을 보는 engineering-style evaluation으로 만듭니다.

유형: 평가 | 날짜: 2026-07-10

<a id="case-199"></a>
### Case 199: [Epoch Open-Weight Index Lead](https://x.com/EpochAIResearch/status/2074894535558300103) (작성자 [@EpochAIResearch](https://x.com/EpochAIResearch))

**이 사례는 GLM-5.2를 장기 capability curve 위에 놓고 볼 때 유용합니다. Epoch AI가 Capabilities Index 추정 점수 152를 제시했고, 자신들이 평가한 open-weight 모델 중 최고라고 했기 때문입니다.**

Epoch AI는 GLM-5.2가 Epoch Capabilities Index에서 추정 152점을 기록했고, 자신들이 평가한 open-weight 모델 가운데 가장 높은 점수라고 말합니다. 그래서 이 게시물은 좁은 coding 전용 leaderboard 대신, 단일 capability-positioning 신호가 필요할 때 참고할 만한 benchmark 기준점이 됩니다.

유형: 벤치마크 | 날짜: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Databricks Internal Harness Eval](https://x.com/alighodsi/status/2074996561306955958) (작성자 [@alighodsi](https://x.com/alighodsi))

**이 사례는 GLM-5.2를 대규모 private engineering codebase에서 benchmark할 때 유용합니다. Databricks에 따르면 3,000명 넘는 엔지니어의 작업을 포함한 내부 평가에서 GLM 5.2가 매우 강했고, harness 선택만으로도 비용을 약 2x 줄일 수 있었기 때문입니다.**

Ali Ghodsi는 Databricks가 자체 task, codebase, infrastructure를 대상으로 포괄적인 평가를 수행했고, 그 범위가 3,000명 이상의 software engineer, 3개의 hyperscaler cloud, 다양한 language에 걸쳤다고 말합니다. 게시물은 GLM 5.2가 매우 좋은 성능을 냈고, 같은 model이라도 올바른 harness를 고르면 비용을 약 2x 줄일 수 있다고 설명하며, Omnigent가 task별로 model과 harness를 multiplex했다고 덧붙입니다.

유형: 평가 | 날짜: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [NatureBench Open-Weight Runner-Up](https://x.com/OkhayIea/status/2074498200262889837) (작성자 [@OkhayIea](https://x.com/OkhayIea))

**이 사례는 GLM-5.2를 scientific-agent workflow에서 benchmark할 때 유용합니다. NatureBench가 6개 scientific domain, 90개 task에서 GLM-5.2가 전체 2위이자 open-weight 1위로 데뷔했다고 말하기 때문입니다.**

NatureBench는 웹 검색 없이 coding agent가 실제 Nature 계열 논문의 공개 SOTA를 넘는 방법을 찾아낼 수 있는지를 6개 scientific domain과 90개 task에서 묻는 benchmark입니다. 이번 업데이트에 따르면 GLM-5.2는 Claude Opus 4.7 바로 뒤인 전체 2위로 데뷔했고 open-weight 진영 1위를 차지했습니다. 그래서 이것은 단순한 코드 생성이 아니라 scientific-agent workflow용 구체적 benchmark입니다.

유형: 벤치마크 | 날짜: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [Terminal-Bench 45-Task Cost Tradeoff](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (작성자 [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**이 사례는 같은 agent harness에서 GLM-5.2와 GPT-5.5를 비교할 때 유용합니다. 45개 Terminal-Bench 작업에서 GLM-5.2는 25승, GPT-5.5는 29승이었고, GLM은 prompt caching 기준 약 40% 더 저렴했기 때문입니다.**

benchmark 게시물에 따르면 팀은 GPT-5.5와 GLM-5.2를 45개의 Terminal-Bench 작업에 대해 같은 agent, 같은 prompt, 같은 evaluation setup, 같은 harness로 돌렸고 바뀐 것은 모델뿐이었습니다. GLM은 45개 중 25개를 해결했고 GPT-5.5는 29개를 해결했지만, prompt caching을 고려한 비용은 GLM 쪽이 약 40% 낮았습니다. 그래서 이 글은 막연한 workflow 취향이 아니라 가격 대비 성공률을 보여 주는 구체적인 체크포인트입니다.

유형: 평가 | 날짜: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Harvey LAB-AA Legal-Agent Tie](https://x.com/ArtificialAnlys/status/2074541975186165887) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**이 사례는 GLM-5.2를 실제 법률 에이전트 업무에서 benchmark할 때 유용합니다. Harvey LAB-AA에서 GLM-5.2 Max가 24개 practice area, 120개 private task 기준으로 Claude Opus 4.8과 같은 7.5% all-pass를 기록했기 때문입니다.**

Artificial Analysis에 따르면 Harvey LAB-AA는 24개 practice area에 걸친 120개의 private legal task를 평가하고, 결과를 binary rubric으로 채점합니다. launch 결과에서 GLM-5.2 Max는 7.5% all-pass와 91.0% criteria-pass를 기록해 Claude Opus 4.8과 동률이었고, task당 비용은 Claude Fable 5의 약 6% 수준이라고 합니다. 그래서 이 사례는 frontier-domain benchmark이면서 비용 효율 신호이기도 합니다.

유형: 벤치마크 | 날짜: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [AutomationBench-AA Open-Weights Lead](https://x.com/ArtificialAnlys/status/2074194764510208230) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**이 사례는 GLM-5.2를 coding benchmark뿐 아니라 비즈니스 규칙을 지켜야 하는 SaaS automation에서 비교할 때 유용합니다. Artificial Analysis가 AutomationBench-AA에서 GLM-5.2 Max를 27.8%로 보고하며 open weights 중 1위라고 했기 때문입니다.**

Artificial Analysis에 따르면 AutomationBench-AA는 40개의 simulated SaaS app에 걸친 657개의 private workflow task를 거의 12,000개의 objective 및 guardrail assertion으로 채점합니다. launch post는 GLM-5.2 Max를 27.8%로 두고 open weights 선두라고 말하지만, 더 강한 closed model보다 여전히 뒤처지고 task당 guardrail violation도 꽤 높다고 덧붙입니다. 그래서 이 사례는 agentic business automation에서 능력 신호이면서 동시에 limitation 신호이기도 합니다.

유형: 평가 | 날짜: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [Three-Body Simulator Benchmark Win](https://x.com/AlicanKiraz0/status/2073823792543998170) (작성자 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**이 사례는 수치물리 코딩 벤치마크에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0가 혼돈적인 3체 시뮬레이터 과제를 돌려 GLM 5.2 Max에 100점 만점 중 91점의 최고 점수를 줬기 때문입니다.**

이 benchmark는 3체 물리, 실제 RK4, 근접 조우 안정성, 실시간 보존량 그래프, 상호작용 제어를 함께 요구합니다. thread에 따르면 GLM 5.2 Max는 Float64Array state, 재사용 가능한 RK4 buffer, Plummer softening, adaptive substep으로 돋보였고, 단순한 순위표가 아니라 engineering quality에 대한 구체적 평가가 되었습니다.

유형: 평가 | 날짜: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [GameDevBench 333-Task Open-Source Lead](https://x.com/iamwaynechi/status/2073081777091182633) (작성자 [@iamwaynechi](https://x.com/iamwaynechi))

**이 사례는 agentic 게임 개발 benchmark에서 GLM-5.2를 추적할 때 유용합니다. GameDevBench가 333개 작업으로 확장됐고, 시각 기능이 없어도 GLM-5.2가 leaderboard에서 가장 강한 open-source model이라고 말하기 때문입니다.**

iamwaynechi는 GameDevBench가 333개 작업으로 3배 확장됐고, paper를 업데이트했으며, leaderboard에 GLM-5.2와 Opus 4.8을 추가했다고 말합니다. 게시물에 따르면 전체 1위는 근소하게 Opus지만, GLM-5.2는 가장 강한 open-source model로 남아 있어 텍스트 coding만이 아니라 게임 제작형 workflow를 보는 benchmark signal로 유용합니다.

유형: 평가 | 날짜: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [Cursor Double Pendulum Scorecard](https://x.com/AlicanKiraz0/status/2073386918813778143) (작성자 [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**이 사례는 제약이 있는 Cursor coding benchmark에서 GLM-5.2를 비교할 때 유용합니다. AlicanKiraz0는 HTML double-pendulum simulator로 6개 모델을 비교해 GLM 5.2 Max에 100점 만점 중 88점을 줬고, Fable과 Sonnet에는 뒤졌지만 GPT-5.5, Kimi K2.7 Code, Composer보다는 앞섰습니다.**

AlicanKiraz0는 Cursor 안에서 단일 HTML double-pendulum simulator task로 6개 모델을 비교하고 총점과 모델별 약점을 함께 공개했습니다. GLM 5.2 Max는 시각적 완성도와 교육적 설명은 강하지만, 성능 아키텍처 측면에서는 Fable이나 Sonnet보다 덜 정교하며 RK4 wrapper의 allocation 위험과 trail buffer resize 경로의 견고성 부족이 지적됩니다. 막연한 취향 평이 아니라 구체적인 comparative evaluation로 볼 수 있는 스레드입니다.

유형: 평가 | 날짜: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10-Task 80 Percent Tie](https://x.com/morganlinton/status/2072689409011679642) (작성자 [@morganlinton](https://x.com/morganlinton))

**이 사례는 cost와 score가 모두 중요한 post-cutoff 실제 엔지니어링 작업에서 GLM-5.2를 비교할 때 유용합니다. Morgan Linton에 따르면 VulcanBench에서 GLM 5.2 High, Fable 5 Low, Sonnet 5 High가 10개 repo에서 모두 80 percent를 기록했고, GLM의 비용은 중간이었습니다.**

Morgan Linton에 따르면 이 benchmark는 Flask, aiohttp, sqlglot 같은 프로젝트의 실제 엔지니어링 task 10개를 사용했고, 모두 post-training-cutoff로 설명됩니다. Fable 5 Low, GLM 5.2 High, Sonnet 5 High는 모두 80 percent였고, reported cost는 각각 2.27, 8.41, 15.81 dollars였습니다. 단일 모델 자랑이 아니라 세 모델의 가격 대비 품질 체크포인트입니다.

유형: 평가 | 날짜: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-Rebench 51.1 Percent Checkpoint](https://x.com/ibragim_bad/status/2072318238407483593) (작성자 [@ibragim_bad](https://x.com/ibragim_bad))

**이 사례는 계속 업데이트되는 SWE 에이전트 리더보드에서 GLM-5.2를 추적할 때 유용합니다. 최신 SWE rebench 게시물은 2.62 million tokens에서 51.1 percent를 보고하며, 새로 추가된 DeepSeek, MiMo, Qwen, Gemma 런보다 분명히 앞섭니다.**

ibragim_bad에 따르면 최신 SWE rebench 업데이트는 GLM-5.2를 여러 새 오픈 모델과 함께 추가했습니다. 공개된 숫자에서는 GLM이 2.62 million tokens로 51.1 percent를 기록했고, DeepSeek V4 Pro는 42.7 percent, MiMo V2.5 Pro는 42.4 percent, Qwen과 Gemma는 그보다 더 낮아 공개 리더보드의 구체적 체크포인트가 됩니다.

유형: 평가 | 날짜: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case Win At 40/41](https://x.com/composio/status/2072355937415827950) (작성자 [@composio](https://x.com/composio))

**이 사례는 채팅 전용 평가가 아니라 비즈니스 도구를 쓰는 에이전트 작업에서 GLM-5.2를 시험할 때 유용합니다. Composio에 따르면 GitHub, Jira, LaunchDarkly 작업 41개 중 40개를 맞혔고, 보류 중 승인이라는 엣지 케이스를 잡아낸 모델은 GLM뿐이었습니다.**

Composio는 GitHub, Jira, LaunchDarkly 같은 실제 도구를 쓰는 41개의 에이전트 작업에서 GLM-5.2를 Claude Opus 4.8과 GPT-5.5와 비교했습니다. GLM은 40/41을 기록했고 Opus와 GPT는 각각 39/41이었습니다. LaunchDarkly 작업 하나에서는 GLM만 플래그를 stale이라고 부르기 전에 pending approval을 확인했고, 나머지 두 모델은 켜짐과 꺼짐 상태만 보고 멈췄습니다.

유형: 평가 | 날짜: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench Open-Weight Patch Runner-Up](https://x.com/ValsAI/status/2072099011398627639) (작성자 [@ValsAI](https://x.com/ValsAI))

**GLM-5.2를 공격형 취약점 탐지와 패치 작업에서 측정하고 싶다면 이 사례가 유용합니다. CyberBench가 60개의 실제 OSS-Fuzz 취약점에서 이 모델을 종합 2위에 올려놨기 때문입니다.**

ValsAI는 CyberBench가 취약한 빌드만 크래시시키는 PoC 제출과 동작을 깨뜨리지 않는 패치 작성을 함께 평가한다고 설명합니다. 60개의 OSS-Fuzz 메모리 안전 취약점에서 GPT-5.5가 선두였고 GLM 5.2는 가장 강한 open-weight 그룹 중 하나로 나타났습니다.

유형: 평가 | 날짜: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**인공 분석 게시물을 사용하여 GLM-5.2를 인텔리전스 및 작업당 비용에 대한 다른 개방형 및 독점 프론티어 모델과 비교하세요.**

인공 분석에서는 GLM-5.2를 인텔리전스 지수에서 최고의 개방형 가중치 모델로 보고했으며, 점수는 51점이고 인텔리전스 대 작업당 비용에 대한 파레토 프론티어 위치를 차지했습니다. 게시물에는 모델 크기, 컨텍스트 창, 가격 및 공급자 가용성도 기록됩니다.

유형: 벤치마크 | 날짜: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (작성자 [@arena](https://x.com/arena))

**이 사례를 사용하여 경기장 스타일 비교로 판단된 실제 프런트엔드 코딩 작업에서 GLM-5.2를 평가합니다.**

Arena 계정은 GLM-5.2 Max가 Code Arena Frontend에서 다른 공개 모델보다 앞서며 최상위 진입에 가까운 2위를 차지했다고 보고했습니다. 이 게시물은 프런트 엔드, React, HTML, 게임, 시뮬레이션 및 참조 기반 디자인 사용 사례에 특히 유용합니다.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (작성자 [@Designarena](https://x.com/Designarena))

**이 사례를 사용하여 GLM-5.2가 텍스트가 많은 코딩 벤치마크가 아닌 디자인과 코드 작업을 처리할 수 있는지 판단합니다.**

Design Arena는 GLM-5.2가 1360의 Elo 점수로 1위를 차지했다고 보고했으며, 이는 개방형 가중치 모델의 디자인 코드 성능이 향상되었음을 강조합니다. 프로젝트별 UI 검토를 대체하는 것이 아니라 디자인 벤치마크 신호로 취급하십시오.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (작성자 [@ProximalHQ](https://x.com/ProximalHQ))

**FrontierSWE 게시물을 사용하여 소프트웨어 엔지니어링 작업에 대한 GLM-5.2를 GPT-5.5, Opus 및 Fable 스타일 모델과 비교하세요.**

이 게시물에서는 GLM-5.2가 FrontierSWE에서 3위를 차지했으며 이를 구현이 많은 엔지니어링 작업에서 최고 독점 모델과의 격차를 줄이기 위한 최초의 개방형 모델 중 하나로 구성했습니다.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (작성자 [@AiBattle_](https://x.com/AiBattle_))

**DeepSWE 사례를 사용하여 GLM-5.2를 어려운 소프트웨어 엔지니어링 평가 작업을 위한 강력한 개방형 모델로 이해하세요.**

AiBattle은 GLM-5.2에 대해 46.2% DeepSWE 점수를 보고했으며 이를 해당 벤치마크 맥락에서 오픈 소스 모델에 대한 가장 높은 점수라고 설명했습니다.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (작성자 [@cline](https://x.com/cline))

**터미널 지향 코딩 및 에이전트 워크플로우에 대해 GLM-5.2를 평가할 때 이 사례를 사용하십시오.**

Cline은 GLM-5.2를 터미널 벤치에서 80%를 넘은 최초의 개방형 가중치 모델로 강조하고 접근 가능한 도구 기반 개발을 위한 최전선 수준의 옵션으로 포지셔닝했습니다.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [GPT-5.5에 대한 SWELancer 비교](https://x.com/gosrum/status/2067153091842203676) (작성자 [@gosrum](https://x.com/gosrum))

**이 SWELancer 사례를 작업 성공, 보상 및 완료 시간에 대한 GLM-5.2와 GPT-5.5 간의 구체적인 다중 측정 비교로 사용하세요.**

저자는 GLM-5.2가 작업 성공, 획득한 보상 및 완료 시간에 대한 최신 SWELancer 결과에서 예기치 않게 GPT-5.5를 앞섰던 일본 벤치마크 업데이트를 공유했으며, 액세스할 수 없는 두 작업은 제외되었습니다.

유형: 평가 | 날짜: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (작성자 [@bridgemindai](https://x.com/bridgemindai))

**코딩 순위표만 사용하는 것이 아니라 기반 다단계 추론을 통해 GLM-5.2를 검사하려면 이 사례를 사용하세요.**

BridgeMind는 GLM-5.2를 BridgeBench BS 벤치마크에서 만점을 받은 최초의 모델로 보고하여 추론이 많은 평가 주장에 유용한 소스가 되었습니다.

유형: 벤치마크 | 날짜: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (작성자 [@bridgebench](https://x.com/bridgebench))

**근거 추론 작업에 대한 폐쇄 프론티어 모델과 GLM-5.2를 비교하려면 이 사례를 사용하십시오.**

BridgeBench는 GLM-5.2가 추론 벤치마크에서 1위를 차지했으며 측정 측면에서 Claude Fable 5를 능가했다고 보고했습니다.

유형: 벤치마크 | 날짜: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (작성자 [@elliotarledge](https://x.com/elliotarledge))

**벤치마크 이득이 지름길 대신 유효한 구현 동작에서 나오는지 확인할 때 이 사례를 사용하세요.**

KernelBench-Hard 게시물에서는 흥미로운 결과가 단순한 점수가 아니라 GLM-5.2가 fp8 GEMM 문제에 대한 부적절한 지름길 사용을 중단하여 벤치마크 무결성과 관련이 있다고 말합니다.

유형: 평가 | 날짜: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (작성자 [@maxbittker](https://x.com/maxbittker))

**이 사례를 게임과 같은 벤치마크 작업에서 개방형 모델 진행에 대한 빠른 신호로 사용하세요.**

이 게시물에서는 GLM-5.2가 Runescape 벤치의 최근 독점 모델보다 더 나은 점수를 받았다고 보고하며, 그 결과를 사용하여 오픈 소스 프론티어 기능이 얼마나 빨리 따라잡는지 프레임을 정합니다.

유형: 벤치마크 | 날짜: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (작성자 [@bridgebench](https://x.com/bridgebench))

**이 사례를 사용하여 인텔리전스와 함께 속도가 중요한 지연 시간에 민감한 워크플로를 평가하세요.**

BridgeBench는 GLM-5.2가 GLM-5.1보다 3배 빠르고 속도 벤치마크에서 4번째로 빠르다고 보고하여 반복 속도가 유용성에 영향을 미치는 워크플로와 관련이 있습니다.

유형: 벤치마크 | 날짜: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench 하드 및 메가 GPU 코딩](https://x.com/elliotarledge/status/2068177175640240323) (작성자 [@elliotarledge](https://x.com/elliotarledge))

**공개 에이전트 추적을 통해 결과를 검사할 수 있는 KernelBench-Hard 및 KernelBench-Mega 전반의 GPU 커널 코딩에서 GLM-5.2를 평가하려면 이 사례를 사용하세요.**

KernelBench 업데이트는 H100, B200 및 RTX PRO 6000 테스트, 오픈 소스 에이전트 추적 및 GLM-5.2를 비교에서 최고의 개방형 모델로 보고합니다.

유형: 벤치마크 | 날짜: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE Max-Effort 오픈소스 선두](https://x.com/datacurve/status/2068473057107476680) (작성자 [@datacurve](https://x.com/datacurve))

**최대 effort 설정의 DeepSWE에서 GLM-5.2를 추적하는 데 쓰는 사례입니다. 공개 리더보드에서는 open model 가운데 1위, pass@1 44%로 제시됩니다.**

DataCurve는 DeepSWE leaderboard update 를 공유하며 GLM-5.2가 pass@1 44%를 기록했고, open model 기준으로 Kimi K2.7 Code보다 17포인트 앞섰다고 설명했습니다. 이는 benchmark update 로 받아들여야 하며, 모든 실전 agent workflow 가 이미 해결됐다는 증거로 보면 안 됩니다.

유형: 벤치마크 | 날짜: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM Debate Benchmark 준우승](https://x.com/LechMazur/status/2068428300460974279) (작성자 [@LechMazur](https://x.com/LechMazur))

**코딩 외 작업에서도 GLM-5.2를 평가하기 위한 사례입니다. 적대적 multi-turn debate 에서 max-reasoning variant 가 Claude 계열 다음인 2위를 기록했습니다.**

Lech Mazur 는 GLM-5.2 Max 가 2위를 차지한 LLM Debate Benchmark 결과를 공유했습니다. 이 benchmark 는 다양한 주제에 걸친 적대적 multi-turn debate 를 측정하므로, 표준 코딩 리더보드 바깥의 reasoning signal 로 볼 수 있습니다.

유형: 벤치마크 | 날짜: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience hallucination rate](https://x.com/yuhasbeentaken/status/2068259921519423855) (작성자 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**불확실성 처리 성능을 비교하기 위한 사례입니다. 공개된 AA-Omniscience 결과에서는 GLM-5.2의 hallucination rate 가 여러 frontier model 보다 낮게 나옵니다.**

이 게시물은 AA-Omniscience 에서 GLM-5.2의 hallucination rate 가 28%였고, Fable 5와 DeepSeek V4 Pro 보다 더 높은 rate 를 보인 다른 모델들보다 낮았다고 전합니다. 이 benchmark 는 추측 대신 모델이 거부하거나 불확실성을 인정하는지를 중심으로 설명됩니다.

유형: 평가 | 날짜: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**코딩 전용 리더보드가 아니라 장기 지식 노동에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오.**

Artificial Analysis는 GDPval-AA에서 GLM-5.2가 Elo 1524를 기록해 Claude Fable 5와 Opus 4.8에 이어 전체 3위였고, GPT-5.5 xhigh의 1509를 근소하게 앞섰다고 보고했습니다. 오픈 웨이트 모델 중에서는 큰 차이로 1위였으며, 게시물은 1,999개 매치 전반에서 작업당 평균 약 31턴이 오갔다고 말합니다.

유형: 평가 | 날짜: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (작성자 [@Designarena](https://x.com/Designarena))

**게임 제작 품질에서 GLM-5.2를 판단하려면 이 사례를 사용하십시오. Game Dev Arena에서 2위를 기록했고, 그 순위에서 오픈 웨이트 진영 최고 성적을 냈습니다.**

Design Arena는 Game Dev Arena에서 GLM-5.2가 Elo 1368을 기록해 GLM-5.1 대비 29포인트 상승했고 순위도 6계단 올랐다고 보고했습니다. 게시물은 이 모델이 Claude Fable 5와 같은 성능대에 있다고 말하며, 전체 2위이자 연구소 단위로는 OpenAI를 앞서고 Anthropic만 뒤쫓았다고 설명합니다.

유형: 평가 | 날짜: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [PostTrainBench 신뢰성 선두](https://x.com/hrdkbhatnagar/status/2070244540108423427) (작성자 [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**헤드라인 점수뿐 아니라 84개 작업에서 failed run 0건을 기록한 agent reliability까지 포함해 GLM-5.2 Max를 비교하려면 이 사례를 사용하십시오.**

hrdkbhatnagar는 GLM 5.2 Max reasoning이 34.29%로 Opus 4.8 Max의 34.08%를 근소하게 앞선 PostTrainBench leaderboard를 공유했습니다. 같은 게시물은 GLM이 84 runs에서 failed run 0건을 기록한 반면 Opus agents는 대략 10% 정도의 failure rate를 보였다고도 말합니다. 그래서 이 평가는 raw pass rate만이 아니라 agent reliability까지 중시하는 팀에 유용합니다.

유형: 벤치마크 | 날짜: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211개 저장소 태스크 평가](https://x.com/FireworksAI_HQ/status/2070181898962534570) (작성자 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**공개 benchmark만이 아니라 private repo의 실제 engineering task에서 GLM-5.2를 판단하려면 이 사례를 사용하십시오. 공개 수치에는 점수, 속도, 작업당 비용이 함께 들어 있습니다.**

Fireworks는 Faros와 함께 진행한 211개의 실제 engineering task 평가에서 Claude Code + GLM-5.2가 Claude Code + Opus 4.8과 Codex + GPT-5.5를 모두 앞섰다고 말합니다. 게시된 수치는 judge score 0.568 대 0.521 / 0.466, 작업당 321초 대 775 / 392, 작업당 0.92달러 대 1.76 / 2.06이며, Faros가 공개 benchmark만이 아니라 자기 repositories와 실제 업무를 사용했다는 점도 함께 적혀 있습니다.

유형: 평가 | 날짜: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase 작업당 시간 프런티어](https://x.com/ArtificialAnlys/status/2069914443639635978) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**벤치마크 점수뿐 아니라 작업당 시간이 중요한 장기 지식 노동에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오.**

Artificial Analysis는 GLM-5.2가 AA-Briefcase의 파레토 프런티어에 올라 있으며, 점수 1261, 작업당 평균 16.3분을 기록해 GPT-5.5 xhigh의 1159를 앞섰고, 동시에 해당 벤치마크에서 최고 성능의 open-weights model이라고 말합니다. 단순한 리더보드 순위가 아니라 장기 과제 결과물의 품질과 실행 시간을 함께 비교하려는 팀에 유용한 benchmark입니다.

유형: 벤치마크 | 날짜: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena Frontend 정면 대결 마진](https://x.com/arena/status/2069885722333769963) (작성자 [@arena](https://x.com/arena))

**단일 순위 스크린샷이 아니라 쌍대 정면 대결 결과로 GLM-5.2의 프런트엔드 우위를 확인하려면 이 사례를 사용하십시오.**

arena는 GLM-5.2 Max가 Code Arena: Frontend 정상에 오른 이유를 풀어 설명하며, 한 쌍을 제외한 모든 매치업에서 상대보다 더 높은 win share를 기록했다고 말합니다. 스레드에는 Kimi-K2.6 상대로 61.0%, Sonnet 4.6 상대로 59.4%, Opus 4.7 Thinking 상대로 55.0%, GPT-5.5 xHigh와의 41.7% 대 40.0% 접전, 그리고 GLM-5.1과의 45.5% 무승부가 제시됩니다.

유형: 벤치마크 | 날짜: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas Codebase QnA 준우승](https://x.com/ScaleAILabs/status/2069864932913631617) (작성자 [@ScaleAILabs](https://x.com/ScaleAILabs))

**단일 작업 SWE 리더보드만이 아니라 Codebase QnA, 테스트 작성, 리팩터링 전반에서 GLM-5.2를 추적하려면 이 사례를 사용하십시오.**

Scale AI Labs는 GLM 5.2가 SWE Atlas의 세 리더보드, Codebase QnA, Test Writing, Refactoring 전부에 올라왔다고 말합니다. 특히 Codebase QnA에서 2위를 기록한 점을 강조하며, 오픈 모델이 전반적으로 frontier system을 바짝 따라붙고 있다고 설명합니다.

유형: 벤치마크 | 날짜: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 코딩 에이전트와 장기 컨텍스트 워크플로
<a id="case-168"></a>
### Case 168: [Synthwave Hard-Slice Ensemble At $2.66](https://x.com/TracNetwork/status/2073038214592360522) (작성자 [@TracNetwork](https://x.com/TracNetwork))

**이 사례는 GLM-5.2를 단독 모델이 아니라 multi-model coding ensemble 안에서 시험할 때 유용합니다. TracNetwork에 따르면 GLM이 포함된 Synthwave 조합은 LiveCodeBench hard에서 46.3 percent를 약 2.66달러에 기록했고, 각 generator 단독보다 더 나았습니다.**

TracNetwork는 OpenRouter에서 qwen3-coder-next를 synthesizer로, GLM-5.2와 qwen3.5-122b, qwen3-coder-next를 coding generator로 묶은 Synthwave ensemble을 사용했다고 말합니다. 82개의 LiveCodeBench hard 작업에서 46.3 percent와 약 2.66달러를 기록했고, 어떤 개별 generator도 그 점수에 도달하지 못했다고 합니다. GLM-5.2를 유일한 coding model이 아니라 비용 효율적인 ensemble의 한 구성원으로 쓰는 구체적인 예시입니다.

유형: 통합 | 날짜: 2026-07-03

---

<a id="case-194"></a>
### Case 194: [CuTeDSL Kernel Skill Open Source](https://x.com/SubhoGhosh02/status/2074466050557739469) (작성자 [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**이 사례는 GLM-5.2를 재사용 가능한 kernel-debugging skill 안에서 살펴볼 때 유용합니다. 작성자가 CuTeDSL용 Hermes skill을 오픈소스로 공개했고, kernel 디버깅과 작성에서 GLM-5.2의 비용 효율이 특히 좋았다고 말했기 때문입니다.**

게시물은 skill의 대부분이 여러 모델을 넘나드는 Hermes agentic conversation으로 만들어졌고, 그 과정에서 GLM-5.2가 kernel debugging과 kernel writing에서 비용 효율 면에서 두드러졌다고 설명합니다. 또한 source에는 `hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` 와 `hermes chat -s cutedsl-kernels` 라는 정확한 설치 및 실행 명령도 들어 있어, 이것을 막연한 칭찬이 아니라 재사용 가능한 tutorial-style workflow로 만들어 줍니다.

유형: 튜토리얼 | 날짜: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Hermes SSD Recovery Skill Loop](https://x.com/ShankhadeepSho1/status/2073658918937473444) (작성자 [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**이 사례는 수리 지향 agent loop 안에서 GLM-5.2를 시험할 때 유용합니다. ShankhadeepSho1에 따르면 Hermes와 GLM 5.2가 고장 난 NAS SSD를 진단하고 문제를 고친 뒤 그 해결책을 재사용 가능한 skill로 패키징했기 때문입니다.**

작성자에 따르면 QNAP NAS의 SSD가 죽어서 예비 머신에 연결한 뒤 Hermes에 진단을 맡겼다고 합니다. 공개된 결과는 꽤 구체적입니다. stack이 문제를 복구했고, 스스로를 위한 skill을 만들고, recovery 전략을 infrastructure wiki에 기록했다고 합니다.

유형: 데모 | 날짜: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [Role-Routed Heavy-Duty Coder Stack](https://x.com/denizirgin/status/2073462071639876004) (작성자 [@denizirgin](https://x.com/denizirgin))

**이 사례는 역할별로 라우팅하는 개인 스택에서 GLM-5.2를 무거운 coding 작업 담당으로 둘 때 유용합니다. denizirgin은 Codex와 OpenCode를 한 달간 시험한 뒤, 월 120~140달러 수준의 총예산을 유지하면서 더 무거운 coding work를 GLM 5.2로 보내는 운영에 정착했다고 말합니다.**

denizirgin은 현재 개인 설정이 Codex, OpenCode, DeepSeek, OpenRouter, 그리고 coding, review, research, speed, cost를 판단하는 자체 sub-agent skill과 decision table로 이루어져 있다고 설명합니다. 그 라우팅 구조에서 GLM 5.2는 보조 provider를 통한 heavy-duty coder 역할을 맡고, Codex는 main backbone으로 남으며, OpenRouter는 모델 실험용으로 더 선택적으로 씁니다. 일반적인 모델 순위가 아니라 비용 감각이 있는 실전 workflow 메모라는 점이 핵심입니다.

유형: 평가 | 날짜: 2026-07-04

<a id="case-155"></a>
### Case 155: [Cotal Four-Agent TUI Loop](https://x.com/silvanrec/status/2072335315822403656) (작성자 [@silvanrec](https://x.com/silvanrec))

**이 사례는 코딩 루프를 전문 에이전트들로 분담할 때 유용합니다. 작성자는 Opus 리드와 GPT 리뷰어 아래에서 GLM-5.2 워커 두 개를 써서 lazygit 스타일 TUI를 47분 만에 사람 개입 없이 완성했습니다.**

silvanrec에 따르면 Cotal은 네 개의 모델을 조율했습니다. 프런트엔드와 백엔드 개발자로 GLM-5.2 두 인스턴스, 백그라운드 리뷰어로 GPT-5.5, 그리고 전체 루프를 이끄는 Claude Opus입니다. 실제 TUI 콘솔을 만들라는 하나의 프롬프트에서 시작해 네 번의 라운드를 돌며 렌더링과 탭 배선 버그를 찾아내고 에이전트 사이 handoff를 조정해 47분 만에 동작하는 결과를 냈습니다. 게시물은 오픈소스 층으로 npx cotal-ai setup --full도 가리킵니다.

유형: 데모 | 날짜: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Legacy Migration Cost-Cut Pilot](https://x.com/chamath/status/2072390507628540213) (작성자 [@chamath](https://x.com/chamath))

**이 사례는 레거시 앱 현대화 루프에서 GLM-5.2를 더 저렴한 작업 모델로 가격 평가할 때 유용합니다. 8090의 파일럿에 따르면 GLM과 Software Factory 조합은 Opus 4.8 단독 대비 비용을 16.4배 줄였지만 속도는 약 3배 느렸습니다.**

Chamath는 PHP에서 Next.js로 가는 초기 현대화 파일럿을 공유했습니다. 8090의 Software Factory를 얹은 Opus 4.8은 Opus 단독보다 1.4배 저렴하고 1.5배 빨랐고, 같은 팩토리에 GLM 5.2를 붙이면 Opus 단독 대비 비용은 16.4배 줄었지만 속도는 약 3배 느렸다고 합니다. 게시물은 이 결과가 n=1의 방향성 확인일 뿐이며, 실제 구매자 관련 레거시 작업 10~15개에서 다시 돌려야 한다고 분명히 말합니다.

유형: 평가 | 날짜: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio Browser-Use Local Loop](https://x.com/MaziyarPanahi/status/2071955191260151862) (작성자 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**완전 로컬 GLM-5.2 스택이 소비자용 하드웨어에서 가벼운 browser agent 작업을 할 수 있는지 시험하고 싶다면 이 사례가 유용합니다. 작성자는 Mac Studio의 llama.cpp와 browser-use로 Hugging Face에서 PII 모델을 찾았습니다.**

MaziyarPanahi는 Mac Studio에서 llama.cpp로 GLM-5.2를 로컬 실행한 뒤 browser-use agent loop를 얹었다고 말합니다. 공개된 예시에서는 Hugging Face를 탐색해 `privacy-filter-nemotron`을 찾아냈습니다.

유형: 데모 | 날짜: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop Agent Swap Cost Cut](https://x.com/aronkor/status/2072032854675218538) (작성자 [@aronkor](https://x.com/aronkor))

**기존 agent harness 안에서 단순한 모델 교체를 시험하고 싶다면 이 사례가 유용합니다. Gumloop은 가장 많이 쓰는 agent를 GLM-5.2로 옮긴 뒤 체감 품질 저하 없이 credit 소모를 약 50% 줄였다고 말합니다.**

aronkor는 동일한 harness와 동일한 prompt를 유지한 채 Gumloop의 핵심 agent들을 GLM 5.2로 교체한 내부 실험을 설명합니다. 결과로는 출력 품질 차이를 거의 아무도 알아채지 못했고, credit 사용량만 거의 절반으로 줄었다고 합니다.

유형: 평가 | 날짜: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (작성자 [@KELMAND1](https://x.com/KELMAND1))

**이 사례를 TDD, 검토자 피드백 및 회귀 확인을 통한 장기 자율 프런트엔드 리팩토링을 위한 패턴으로 사용하세요.**

이 게시물에서는 88개의 모델 전환과 102개의 도구 호출이 포함된 1시간 42분의 GLM-5.2 리팩터링 작업에 대해 설명합니다. 워크플로우에는 핸드오프, 4개의 차단 수정, 12개 테스트의 TDD 구현, 2회의 P2 수정 및 최종 회귀가 포함되었습니다.

유형: 데모 | 날짜: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (작성자 [@altudev](https://x.com/altudev))

**이 사례를 사용하여 버그 수정과 작은 구현 작업을 위한 OpenCode 코딩 에이전트로 GLM-5.2를 테스트하세요.**

저자는 6개의 버그 수정과 1개의 OpenCode 구현으로 GLM-5.2를 테스트했다고 보고하며, 변경 사항이 GLM-5.1보다 탄탄한 계획과 더 빠른 속도로 깔끔하게 진행되었다고 말했습니다.

유형: 데모 | 날짜: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (작성자 [@AskVenice](https://x.com/AskVenice))

**이 연습을 사용하여 단일 프롬프트에서 GLM-5.2 및 OpenCode를 사용하여 작은 게임을 구축한 다음 모델이 구현 세부 사항을 처리하는 방법을 검사하십시오.**

Venice는 GLM-5.2 및 OpenCode를 사용하여 복고풍 비디오 게임을 구축하기 위한 전체 연습을 공유하여 이를 비공개, 오픈 소스, 장거리 코딩 워크플로로 포지셔닝했습니다.

유형: 튜토리얼 | 날짜: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (작성자 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**라이브러리 없이 자체 포함된 HTML5 물리 시뮬레이션에서 GLM-5.2와 Kimi K2.7 코드를 비교하려면 이 사례를 사용하십시오.**

Atomic Chat은 두 모델 모두에 풀 브레이크, 스프링 블록 및 Galton 보드 시뮬레이션을 구축하도록 요청했다고 보고했습니다. 그들의 게시물에 따르면 GLM-5.2는 세 가지 모두를 더 세밀하고 세련되게 처리한 반면 Kimi는 신체적 행동으로 어려움을 겪었습니다.

유형: 평가 | 날짜: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (작성자 [@anshuc](https://x.com/anshuc))

**이 사례를 사용하여 세련된 개인 사이트에 대해 GLM-5.2를 요청하고 여러 차례 전환하여 UI/UX를 얼마나 향상시킬 수 있는지 검사하십시오.**

저자는 GLM-5.2가 적절한 메시지를 받은 후 창의적인 개인 사이트를 제작하고 그 결과를 비디오로 공유했다고 말합니다. 단일 벤치마크 주장보다는 프런트 엔드 디자인 반복에 유용합니다.

유형: 데모 | 날짜: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (작성자 [@laozhang2579](https://x.com/laozhang2579))

**PRD, 시간 예산, 단계 수, 사용 할당량 및 코드 품질 비교를 통해 제품 구축 작업에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오.**

중국 게시물은 AI 계약 검토 제품 PRD에서 GLM-5.2, Kimi K2.7 및 Claude Opus 4.8을 비교합니다. 빌드 기간, 단계 수, 5시간 할당량 사용량 및 코드 품질 점수를 보고합니다.

유형: 평가 | 날짜: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (작성자 [@zcode_ai](https://x.com/zcode_ai))

**더 큰 에이전트 개발 작업을 위해 GLM-5.2가 ZCode 3.0에 통합되는 방법을 이해하려면 이 사례를 사용하십시오.**

ZCode는 코딩 계획 사용자를 위한 GLM-5.2 가용성, 더욱 강력한 에이전트 작업 실행, 향상된 장기 컨텍스트 코딩, 계획부터 완료까지 더 큰 목표를 관리하기 위한 목표 기능을 발표했습니다.

유형: 통합 | 날짜: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [GLM-5.2로 구축된 ZCode용 Linux 래퍼](https://x.com/gosrum/status/2066484949755269510) (작성자 [@gosrum](https://x.com/gosrum))

**코딩 에이전트 환경에 대한 도구 사용을 지원하는 GLM-5.2의 예로 이 사례를 사용하십시오.**

저자는 Linux 사용자가 Linux 환경에서 ZCode를 실행하고 로컬 LLM 엔드포인트를 포함한 임의의 API 엔드포인트를 추가할 수 있도록 GLM-5.2 및 Claude Code를 사용하여 zcode-linux를 완료했다고 보고합니다.

유형: 데모 | 날짜: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (작성자 [@0xSero](https://x.com/0xSero))

**오픈 소스 컴퓨터 사용 저장소를 재사용 가능한 기술로 전환하기 위한 도우미로서 GLM-5.2를 연구하려면 이 사례를 사용하십시오.**

게시물에는 GLM-5.2가 컴퓨터 사용을 설정하고 고급 오픈 소스 저장소를 찾아 이를 기술로 변환했다고 나와 있습니다. 도구 래핑 및 에이전트 통합 작업을 위한 실제 신호입니다.

유형: 데모 | 날짜: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (작성자 [@laogui](https://x.com/laogui))

**단일 채팅 세션이 아닌 전체 에이전트 개발 환경 내에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오.**

중국 리뷰에 따르면 ZCode 3.0은 쉘과 유사한 이전 버전에서 GLM-5.2와 쌍을 이루는 자체 개발 에이전트 코어로 재작성되었으며 국내 에이전트 개발 환경에서 더 나은 경험을 제공합니다.

유형: 데모 | 날짜: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [로컬 서비스를 제공하는 OpenCode 하네스](https://x.com/PatrickToulme/status/2068134212587184442) (작성자 [@PatrickToulme](https://x.com/PatrickToulme))

**Claude Opus와 비교하기 전에 OpenCode 하네스, 로컬 제공 및 도구가 많은 코딩 워크플로를 사용하여 GLM-5.2를 테스트하려면 이 사례를 사용하십시오.**

저자는 로컬 배포, 중첩된 하위 에이전트, 연구/계획 동작 및 작동 중인 애플리케이션 빌드를 보고합니다.

유형: 평가 | 날짜: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (작성자 [@neural_avb](https://x.com/neural_avb))

**이 사례를 사용하면 지침을 RLM 시스템 프롬프트로 이동하여 GLM-5.2 긴 컨텍스트 계산 및 REPL 에이전트 동작을 개선할 수 있습니다.**

릴리스 노트에서는 구체적인 에이전트 스캐폴딩 변경 사항과 GLM-5.2 장기 컨텍스트 벤치마크 효과에 대해 설명합니다.

유형: 통합 | 날짜: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (작성자 [@sydneyrunkle](https://x.com/sydneyrunkle))

**이 사례를 사용하여 개방형 코딩 에이전트 하네스로 GLM-5.2를 시도하고 재현 가능한 에이전트 쉘에서 모델을 비교하십시오.**

저자는 DeepAgents 코드 및 프레임 개방형 모델과 개방형 하네스를 테스트 패턴으로 사용하여 GLM-5.2를 사용했다고 보고합니다.

유형: 데모 | 날짜: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [프로덕션 마케팅 agent stack 라우팅](https://x.com/DeRonin_/status/2068303752671477820) (작성자 [@DeRonin_](https://x.com/DeRonin_))

**구조화, 속도, self-hosting 을 중시하는 production agent workflow 에 GLM-5.2를 배치하고, 모호한 판단은 더 강한 closed model 에 맡기는 라우팅 사례입니다.**

작성자는 agency stack 에서 6일간 side-by-side run 을 한 뒤, GLM-5.2가 drift 하기 전까지 60개가 넘는 agent step 을 유지했고, 800회 이상 연속으로 structured format 을 맞췄으며, 낮은 지연의 self-hosted response 를 제공했다고 말합니다. 같은 글에서 voice 가 중요한 작업이나 모호한 작업에는 여전히 Opus 를 선호한다고 밝혀, 그 라우팅 규칙 자체가 핵심 takeaway 가 됩니다.

유형: 평가 | 날짜: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (작성자 [@hxiao](https://x.com/hxiao))

**M3 Ultra에서의 장시간 로컬 coding agent 실행에서 GLM-5.2를 판단하기 위한 사례입니다. 거의 반나절 동안 Pokemon Red를 HTML로 재현하려 한 목표 실행을 따라갈 수 있습니다.**

작성자는 Claude Code의 model을 로컬 GLM 5.2로 바꾸고 M3 Ultra 512GB 머신에서 12시간짜리 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 작업을 돌렸습니다. 게시물은 실행 시간, token 사용량, code churn, RAM 사용량, GGUF와 KV-cache 구성을 함께 공유하며, 품질은 frontier급으로 느껴졌지만 로컬 추론 속도가 가장 큰 병목이었다고 말합니다.

유형: 데모 | 날짜: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (작성자 [@cline](https://x.com/cline))

**실제 리포지토리 버그 수정에서 GLM-5.2와 Opus 4.8을 비교하려면 이 사례를 사용하십시오. GLM은 더 많은 토큰을 썼지만 더 저렴하고 더 깔끔한 최종 패치를 만들었습니다.**

Cline은 같은 하네스와 도구 아래에서 Cline 리포지토리의 동일한 버그로 두 모델을 테스트했습니다. 게시물에 따르면 GLM은 약 110만 토큰을 사용했고 Opus는 66만 토큰을 사용했으며, 비용은 0.41달러 대 0.81달러, 시간은 4.7분과 도구 호출 28회 대 1.6분과 12회였습니다. 또한 GLM은 죽은 코드 정리와 프로덕션 빌드 성공으로 마무리했지만, Opus는 테스트는 통과했어도 타입 에러를 남겼다고 합니다.

유형: 평가 | 날짜: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 Background Agent](https://x.com/colemurray/status/2069485572339707938) (작성자 [@colemurray](https://x.com/colemurray))

**호스팅 챗 대신 GLM-5.2를 FP8로 돌리는 셀프호스트 background-agent stack을 살펴보려면 이 사례를 사용하십시오.**

colemurray는 Modal Inference 위의 OpenInspect를 GLM-5.2를 FP8로 구동하는 완전 셀프호스트 background agent system으로 소개하며, 핵심 인프라에 대한 속도와 제어성을 강조했습니다. 게시물 자체는 짧지만 사용한 도구 스택과 배포 방식을 분명하게 드러냅니다.

유형: 통합 | 날짜: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [OpenCode + Fireworks 비용 절감 전환](https://x.com/SeekingN0rth/status/2071484711327985696) (작성자 [@SeekingN0rth](https://x.com/SeekingN0rth))

**open-model harness로만 바꿔도 충분한지 시험하고 싶다면 이 사례가 유용합니다. 작성자가 개인 coding과 loop 작업을 Fireworks 위 GLM-5.2 + OpenCode로 옮긴 뒤 token 비용이 3분의 1로 줄었고 일상 품질 저하도 거의 없었다고 말하기 때문입니다.**

SeekingN0rth는 개인 coding과 loop 작업을 주말 동안 Fireworks 위 GLM 5.2 + OpenCode로 옮긴 결과 token 지출이 약 3분의 1로 줄었다고 말합니다. 이 스레드는 경험을 좌우한 것은 frontier 여부보다 harness였다고 설명합니다. OpenCode는 터미널에서 Claude Code와 비슷한 감각이었고, 일상 작업에서는 눈에 띄는 품질 저하가 없었으며, 이 예시는 절대적인 SOTA보다 비용을 더 중시하는 큰 기업에도 적용할 수 있는 모델 전환 패턴으로 제시됩니다.

유형: 평가 | 날짜: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA의 GLM 집계자 워크플로](https://x.com/IBuzovskyi/status/2071601107944571249) (작성자 [@IBuzovskyi](https://x.com/IBuzovskyi))

**고가치 agent 턴에 추가 오케스트레이션이 아깝지 않다면 이 사례가 유용합니다. Hermes Agent의 Mixture of Agents 구성이 GLM-5.2와 다른 모델을 조합해, 공개된 데모에서 작은 추가 비용으로 눈에 띄게 더 나은 결과를 냈기 때문입니다.**

IBuzovskyi는 Hermes Agent의 Mixture of Agents 모드를, 도구 접근 권한이 있는 하나의 집계 모델과 비공개 조언만 제공하는 여러 참고 모델의 조합으로 설명합니다. 이 스레드는 코딩 테스트에서 GLM 5.2 단독은 13분과 0.38달러가 들었고, GLM 5.2 집계자에 Kimi K2.6과 MiniMax M3를 붙이면 35분과 0.47달러가 들었지만 애니메이션, 비주얼, 게임 메커닉은 더 좋아졌다고 보고합니다. 프리셋 설계, 기능을 켜는 위치, 추가 지연을 감수할 가치가 있는 상황도 함께 설명합니다.

유형: 통합 | 날짜: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline 추론 온오프 하네스 격차](https://x.com/akshay_pachaar/status/2071638409022763292) (작성자 [@akshay_pachaar](https://x.com/akshay_pachaar))

**모델 가중치보다 harness 설계를 보고 싶다면 이 사례가 유용합니다. 같은 GLM-5.2가 같은 코딩 작업에서 reasoning만 켰을 때 57.3%에서 68.5%로 뛰었기 때문입니다.**

akshay_pachaar는 Cline 테스트를 인용해 GLM 5.2가 동일한 코딩 작업 세트를 두 가지 방식으로 수행했다고 설명합니다. reasoning을 끄면 57.3%, 켜면 68.5%였습니다. 이 스레드는 이 차이를 통해, 단순한 텍스트가 아니라 실제로 배포 가능한 코드를 원할 때는 컨텍스트 유지, 도구 접근, 편집 적용, 검증 루프가 기반 모델만큼 중요할 수 있다고 주장합니다.

유형: 평가 | 날짜: 2026-06-29

<a id="case-136"></a>
### Case 136: [Cursor + Fireworks 455M-Token 현장 테스트](https://x.com/robinebers/status/2071246749210190132) (작성자 [@robinebers](https://x.com/robinebers))

**작성자는 Fireworks의 빠른 서빙과 함께 4억5500만 토큰 실사용을 보고하며 Opus나 GPT-5.5로 당장 돌아갈 이유가 없다고 말하므로, GLM-5.2를 Cursor 일상용 모델로 판단하려면 이 사례를 사용하십시오.**

robinebers는 Cursor에서 GLM 5.2로 36시간 전환한 뒤 Fireworks와 함께 썼을 때 모델에 대한 인식이 바뀌었다고 말합니다. 게시물은 이미지 지원, 주장된 zero data retention, 초당 약 80-100 tokens 처리량, 그리고 4억5500만 tokens에 약 145달러 비용을 구체적으로 언급합니다. 일반적인 benchmark 찬사보다 하네스 수준에서 더 강한 평가 신호이며, provider 선택이 실사용 경험을 바꿀 수 있음을 보여 줍니다.

유형: 평가 | 날짜: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Devin Desktop 하네스와 Skill 이식성](https://x.com/lily_gpupoor/status/2071297351801794850) (작성자 [@lily_gpupoor](https://x.com/lily_gpupoor))

**Z.ai 자체 coding surface가 불안정하게 느껴질 때 GLM-5.2를 Devin Desktop 안에서 시험하려면 이 사례를 사용하십시오. 작성자는 더 쉬운 skill 이식, 더 빠른 속도, 더 높은 hackability를 보고합니다.**

lily_gpupoor는 API 불안정 기간에 Devin Desktop을 통한 GLM-5.2 고사용 경험이 직접 Z.ai coding plan보다 확실히 나았다고 말합니다. 게시물은 세 가지 구체적 워크플로 승리를 강조합니다. GLM이 커스텀 Solarized Green 테마 JSON을 수정하고 extension 등록까지 성공했고, Devin은 유난히 빨랐으며, 기본 Windsurf Cascade agent에서 Devin Local로 바꾼 뒤에도 기존 skill 대부분이 그대로 옮겨졌습니다.

유형: 평가 | 날짜: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi 인라인 GLM 리뷰어](https://x.com/xpasky/status/2070831715518460177) (작성자 [@xpasky](https://x.com/xpasky))

**Pi 스타일 coding-agent loop에 두 번째 리뷰어를 넣고 싶을 때 쓰는 사례입니다. 작성자는 GLM-5.2가 Opus에 turn마다 조언할 수 있고, 비용 증가는 대략 10% 수준이라고 말합니다.**

xpasky는 팀이 GLM-5.2를 Pi workflow의 두 번째 리뷰어로 쓰고 있으며, 하나의 Opus는 코딩을 맡고 다른 Opus는 어려운 문제를 풀고, 그 옆에서 GLM이 turn마다 Opus에 조언한다고 말합니다. 게시물은 이 reviewer를 추가해도 비용 증가는 약 10%에 머물고, 지금까지 가장 좋은 code가 나오고 있다고 평가합니다.

유형: 통합 | 날짜: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter 원샷 Telegram 봇](https://x.com/MatinSenPai/status/2070259817818812701) (작성자 [@MatinSenPai](https://x.com/MatinSenPai))

**최소 동작 코드만 내는 대신 GLM-5.2가 one-shot coding-agent build 안에서 운영 친화적인 defaults를 스스로 추론하는지 시험하려면 이 사례를 사용하십시오.**

MatinSenPai는 영상과 같은 prompt로 GLM 5.2를 써서 Telegram bot을 one shot으로 만들었고, 모델이 요청하지 않은 실무적 디테일까지 스스로 추가했다고 말합니다. 게시물은 영상 전송 후 자동 파일 정리, 기본 50 MB cap을 둔 Telegram Bot API 크기 제한 고려, 완료 전 반복 self-test, 이전 MiMo build보다 더 깔끔한 구조, 그리고 AgentRouter 기준 약 140K tokens 또는 대략 5달러 사용량을 강조합니다.

유형: 데모 | 날짜: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go 리팩터 첫 패스 성공](https://x.com/vedovelli74/status/2069889605969592500) (작성자 [@vedovelli74](https://x.com/vedovelli74))

**벤치마크 주장만 보지 않고 OpenCode 안의 중간 규모 Go 리팩터링에서 GLM-5.2를 평가하려면 이 사례를 사용하십시오.**

vedovelli74는 중간 규모 GoLang 코드베이스 리팩터링을 대상으로 한 첫 OpenCode 실행을 공유하며, GLM-5.2가 Opus 4.8보다 더 빨랐고 토큰 효율도 높았으며 무엇을 리팩터링해야 하는지 첫 패스에서 정확히 짚었다고 말합니다. 또한 그 결과를 나중에 Codex와 Opus로 다시 검증했음에도 납품 품질 면에서는 GLM-5.2가 앞섰다고 덧붙입니다.

유형: 평가 | 날짜: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 3.36달러 기본 실행](https://x.com/clairevo/status/2069828122640548204) (작성자 [@clairevo](https://x.com/clairevo))

**더 자율적인 coding work를 open weights로 옮기기 전에 Claude Code와 Cursor에서 일상용 모델로서 GLM-5.2를 가늠하려면 이 사례를 사용하십시오.**

clairevo는 GLM 5.2가 Claude Code와 Cursor에서 기본 모델이 되었고, 지금까지 든 비용은 3.36달러라고 말합니다. 게시물은 Opus 같은 coding quality를 느꼈다는 점에 더해, OpenRouter 경유 설정 경로, 프런트엔드 디자인 감각, 장시간 autonomous task에 대한 검토가 기본 모델로 채택한 이유라고 설명합니다.

유형: 평가 | 날짜: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 실사용 데모와 쇼케이스 빌드
<a id="case-202"></a>
### Case 202: [Command Code Space Shooter Feature Win](https://x.com/CommandCodeAI/status/2075264795817972107) (작성자 [@CommandCodeAI](https://x.com/CommandCodeAI))

**이 사례는 one-shot interactive UI build에서 GLM-5.2를 비교할 때 유용합니다. Command Code가 같은 retro space-shooter prompt를 Fable 5, GPT 5.5, GLM 5.2, DeepSeek V4 Pro에 돌렸고, features 기준으로 GLM을 가장 높게 평가했기 때문입니다.**

Command Code는 같은 `/design` prompt로 네 모델 모두 비슷한 retro pixel-art space-shooter layout을 만들었지만, GLM 5.2가 sound, controls, leveling, overall UX 같은 features에서 특히 돋보였고 비용도 Fable 5의 $0.80 대비 $0.07이었다고 말합니다. 단순한 benchmark 스크린샷이 아니라 가벼운 game/UI build에 대한 실제 비교로 볼 수 있습니다.

유형: 평가 | 날짜: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [ZCode Nintendo DS Emulator](https://x.com/0xSero/status/2074870153267818638) (작성자 [@0xSero](https://x.com/0xSero))

**이 사례는 장시간 이어지는 로컬 coding build를 살펴볼 때 유용합니다. 작성자가 4x RTX 6000 위의 ZCode에서 GLM-5.2를 돌리며 C++로 Nintendo DS 에뮬레이터를 처음부터 만드는 목표를 줬기 때문입니다.**

source는 GLM-5.2가 4개의 RTX 6000 GPU 구성의 ZCode 안에서 돌아가는 모습을 보여 주고, ready-made emulator를 쓰지 않고 C++로 Nintendo DS emulator를 만든 뒤 Mario 64 DS ROM이 실행될 때까지 계속하라는 구체적 목표를 제시합니다. 그래서 이것은 막연한 '장난감 앱 만들기'가 아니라 명확한 종료 조건을 가진 실제 coding-agent 데모입니다.

유형: 데모 | 날짜: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [Command Code Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (작성자 [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**이 사례는 GLM-5.2를 가벼운 디자인 게임 작업에서 비교할 때 유용합니다. 작성자가 같은 Flappy Bird prompt를 Command Code로 돌린 뒤, Fable 5가 GLM-5.2보다 거의 9배 비싸면서도 UX에서 결정적 우위를 보이지 못했다고 결론냈기 때문입니다.**

게시물은 같은 게임 prompt와 같은 Command Code `/design` 설정을 DeepSeek V4 Pro, GLM 5.2, Fable 5에 똑같이 적용했다고 말합니다. GLM 5.2는 순수 가격 면에서 DeepSeek와 Fable 사이에 있었지만, 작성자는 Fable이 가격 차이를 정당화할 만큼 큰 UX 우위를 보여 주지 못했다고 적었습니다. 그래서 이것은 단순한 arena 주장보다 현장형 UX-versus-cost 비교에 가깝습니다.

유형: 평가 | 날짜: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [REAP NVFP4 Rubiks Cube One-Shot](https://x.com/RoundtableSpace/status/2072700573145788914) (작성자 [@RoundtableSpace](https://x.com/RoundtableSpace))

**이 사례는 단일 프롬프트 상호작용 build 작업에서 GLM-5.2를 시험할 때 유용합니다. REAP-NVFP4 demo는 한 번의 prompt만으로 3D Rubiks Cube, 실제 scramble, live state, solve button까지 만들었다고 말합니다.**

RoundtableSpace에 따르면 GLM-5.2-REAP-NVFP4에는 HTML prompt 하나만 주어졌고, live state, real scramble logic, solve action을 갖춘 3D Rubiks Cube 앱이 돌아왔습니다. 코드 상세는 많지 않지만, 일반적인 benchmark 스크린샷이 아니라 구체적인 one-shot build demo라는 점이 중요합니다.

유형: 데모 | 날짜: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP Relay iPhone Client](https://x.com/mov_axbx/status/2072192903762288721) (작성자 [@mov_axbx](https://x.com/mov_axbx))

**이 사례는 로컬 GLM-5.2 에이전트를 빠르게 모바일 표면으로 감쌀 때 유용합니다. 작성자에 따르면 Codex의 build-ios-app plugin이 이미 GLM-5.2와 Cloudflare 터널을 쓰는 OMP relay용으로 몇 시간 만에 매끈한 iPhone 클라이언트를 만들었습니다.**

mov_axbx는 로컬 호스팅 OMP 에이전트용 휴대폰 앱이 필요해졌고, Codex의 build-ios-app plugin을 사용해 몇 시간 만에 완성도 높은 버전을 얻었다고 말합니다. 백엔드 경로는 GLM-5.2와 OMP로 작성한 custom relay를 쓰고, 터널은 Cloudflare가 처리했습니다.

유형: 데모 | 날짜: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [오픈소스 DevRel 리서치 에이전트](https://x.com/Astrodevil_/status/2071572680470655253) (작성자 [@Astrodevil_](https://x.com/Astrodevil_))

**GLM-5.2를 범용 채팅이 아니라 세로형 리서치 도우미로 바꾸고 싶다면 이 사례가 유용합니다. 작성자가 제품과 타깃 입력을 근거와 아웃라인이 붙은 우선순위 콘텐츠 기회로 바꿔 주는 오픈소스 DevRel 에이전트를 만들었기 때문입니다.**

Astrodevil_는 GLM-5.2 위에 제품과 오디언스 브리프를 입력받는 chat-first DevRel 리서치 앱을 만들었습니다. 이 앱은 Hacker News에서 수요 신호를 찾고, DEV에서 콘텐츠 공백을 확인하고, Engram memory로 사실을 갱신한 뒤, 근거와 아웃라인이 포함된 주제 아이디어를 우선순위로 반환합니다. 게시물은 Agno, Weaviate Engram, Nebius inference, 그리고 오픈소스 코드베이스라는 스택도 명시합니다.

유형: 데모 | 날짜: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 6개 변형 랜딩페이지 루프](https://x.com/nutlope/status/2070199649818779914) (작성자 [@nutlope](https://x.com/nutlope))

**먼저 여러 GLM-5.2 변형을 만든 뒤 가장 강한 결과를 coding agent로 넘겨 저비용으로 landing page를 프로토타이핑하려면 이 사례를 사용하십시오.**

nutlope는 GLM 5.2와 Recast를 중심으로 한 web iteration workflow를 설명합니다. 하나의 prompt에서 landing page 6 variants를 만들고, 가장 좋은 design을 고른 뒤, 그 code를 내려받아 다른 coding agent에서 반복을 이어가는 흐름입니다. 작성자는 GLM-5.2가 빠르고 저렴하며 design에 강해서 이 용도에 잘 맞고, 같은 예산이면 Opus 4.8이 만드는 한 페이지당 GLM 쪽에서는 보통 3~6개의 변형을 만들 수 있다고 말합니다.

유형: 튜토리얼 | 날짜: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (작성자 [@aimlapi](https://x.com/aimlapi))

**이 사례를 사용하여 GLM-5.2와 Opus 4.8 간의 동일한 프롬프트 게임 구축 출력, 런타임 및 비용을 비교하세요.**

AI/ML API는 GLM-5.2 및 Opus 4.8에 플레이 가능한 백룸 게임을 원샷하도록 요청했다고 보고했습니다. 그들의 게시물에 따르면 GLM-5.2는 $0.37에 1:08에 더 완전한 메커니즘을 구축한 반면 Opus는 $1.94에 2:14를 차지했습니다.

유형: 데모 | 날짜: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [결과가 혼합된 세 가지 실제 빌드](https://x.com/bridgemindai/status/2065840871929442319) (작성자 [@bridgemindai](https://x.com/bridgemindai))

**이 사례를 주의사항 데모 세트로 사용하십시오. 프로덕션 게임 또는 비디오 작업에 대한 모델을 신뢰하기 전에 여러 실제 빌드를 테스트하십시오.**

BridgeMind는 공포 하우스 게임, 3D 스텔스 게임 및 Remotion 마케팅 비디오에서 GLM-5.2를 테스트했습니다. 이 게시물은 손상된 게임 로직을 포함하여 혼합된 결과를 보고하므로 접지된 제한 신호로 유용합니다.

유형: 평가 | 날짜: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**이 사례를 사용하여 여러 수정 및 기능 단계에 걸쳐 GLM-5.2 및 ZCode를 사용한 반복적인 게임 구축을 평가합니다.**

저자는 Super Mario 스타일 복제본을 생성하여 GLM-5.2로 ZCode 3.0을 테스트한 후 문제 수정 및 기능 추가를 5회 반복한 후 결과를 공유했습니다.

유형: 데모 | 날짜: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**대화형 게임 스타일 작업에서 GLM-5.2, MiniMax M3 및 Kimi K2.7 코드를 비교하려면 이 사례를 사용하십시오.**

이 게시물에서는 로컬 모델 개발로 돌아가기 전 비디오 결과를 실제 벤치마크로 사용하여 MiniMax M3, GLM-5.2 및 Kimi K2.7 코드 간의 달 착륙선 콘테스트에 대해 설명합니다.

유형: 평가 | 날짜: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (작성자 [@grx_xce](https://x.com/grx_xce))

**이 사례를 사용하여 경기장 상황에서 단일 디자인 프롬프트에서 GLM-5.2가 생성할 수 있는 내용을 검사합니다.**

저자는 하나의 프롬프트로 만든 Design Arena의 GLM-5.2 생성 사례를 공유하여 이를 사용하여 개방형 및 폐쇄형 가중치 모델 사이의 간격이 좁아지는 것을 보여주었습니다.

유형: 데모 | 날짜: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [연구 논문 워크플로우 이해](https://x.com/askalphaxiv/status/2066996976445706745) (작성자 [@askalphaxiv](https://x.com/askalphaxiv))

**상황에 맞는 질문과 논문 간 참조가 포함된 논문 읽기 작업 흐름에 GLM-5.2를 적용하려면 이 사례를 사용하세요.**

AlphaXiv는 사용자가 섹션을 강조 표시하고, 질문을 하고, 맥락, 비교 및 ​​벤치마크 참조를 위해 다른 논문을 참조하는 연구 논문 이해를 위해 GLM-5.2를 도입했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (작성자 [@emollick](https://x.com/emollick))

**GLM-5.2를 Fable 스타일 모델과 비교할 때 창의적 품질과 정확성을 분리하려면 이 사례를 사용하십시오.**

Ethan Mollick은 올바른 제한된 시를 생성한 GLM-5.2 Max의 공로를 인정했으며, Fable은 사라지는 글자 제약 조건을 시 주제에 보다 창의적으로 통합했다고 언급했습니다.

유형: 평가 | 날짜: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (작성자 [@0xSero](https://x.com/0xSero))

**이 사례를 간단한 시각적 디자인 신호로 사용한 다음 자체 프롬프트와 UI 검토를 통해 확인하세요.**

저자는 GLM-5.2의 디자인 센스가 마음에 들었다며 시각적 예시를 공유했다고 합니다. 이는 생산 설계 품질에 대한 독립형 증거가 아니라 검사를 위한 지침으로 유용합니다.

유형: 데모 | 날짜: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 스타일 복셀 게임 원샷 생성](https://x.com/pseudokid/status/2068431546143649829) (작성자 [@pseudokid](https://x.com/pseudokid))

**단일 프롬프트 게임 생성에서 GLM-5.2를 stress-test 하고, 시각적으로 풍부한 빌드에서 무엇이 추가 수정이 필요한지 확인하는 사례입니다.**

작성자는 Temple Run 에서 영감을 받은 voxel biker game 의 대부분을 첫 턴에 만들었고, 이후 camera 와 movement 수정을 위해 몇 차례 follow-up 을 진행했다고 말합니다. 또 이 글은 Z.ai tooling 이 screenshot 과 gameplay video 를 생성해 text model 이 결과를 평가하는 데 도움을 준다고 덧붙입니다.

유형: 데모 | 날짜: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 원샷 예시 세트](https://x.com/LyalinDotCom/status/2068378281636982990) (작성자 [@LyalinDotCom](https://x.com/LyalinDotCom))

**더 open-ended 한 agent loop 에 투입하기 전에 OpenCode Go 안의 quick one-shot build 에서 GLM-5.2를 benchmark 하는 사례입니다.**

작성자는 OpenCode Go 를 통해 solar-system web app, system-info Electron app, simple explore-island web game 에 걸친 one-shot 예시를 공유합니다. 같은 글에서 GLM-5.2를 지금까지 써본 최고의 open model 이라고 평가하면서도 frontier-equal 이라고 단정하지는 않습니다.

유형: 데모 | 날짜: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (작성자 [@DeryaTR_](https://x.com/DeryaTR_))

**단일 프롬프트 게임 생성에서 GLM-5.2를 시험하고, 몇 번의 추가 프롬프트로 asset 교체와 가벼운 polish가 어떻게 진행되는지 보기 위한 사례입니다.**

작성자는 GLM-5.2가 하나의 메인 프롬프트만으로 플레이 가능한 Space Invaders 스타일 게임을 만들었고, 이후 sprite 교체와 leaderboard 같은 작은 추가를 위해 세 번의 후속 프롬프트를 썼다고 말합니다. 공개 결과물은 가벼운 게임 생성 예시로는 유용하지만 완전한 benchmark는 아닙니다.

유형: 데모 | 날짜: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (작성자 [@threepointone](https://x.com/threepointone))

**대화형 agent failure simulation을 빠르게 프로토타이핑하기 위한 사례입니다. 작성자는 약 3.50달러로 동작하는 recovery lab을 one-shot으로 만들었다고 보고합니다.**

작성자는 4,000단어 분석과 Agents SDK repository를 입력한 뒤 OpenCode와 GLM-5.2로 완전히 상호작용 가능한 recovery lab을 구축했습니다. 게시물에는 176k-token 실행, one-shot 결과, polish 전 기준 약 3.50달러의 end-to-end cost가 함께 적혀 있습니다.

유형: 데모 | 날짜: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (작성자 [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**참조 기반 웹 재현에서 GLM-5.2를 시험하려면 이 사례를 사용하십시오. 소스 URL 하나와 간단한 프롬프트 하나만으로 사이트를 거의 픽셀 수준으로 재현했습니다.**

Open Design은 내장 AMR에서 참조 URL과 간단한 프롬프트 하나만 사용해 GLM-5.2를 테스트했고, 데모에서 웹사이트를 거의 완벽하게 재현했다고 말합니다. 완전한 벤치마크라기보다 참조 기반 UI 생성의 실사용 데모 증거로 보는 것이 맞습니다.

유형: 데모 | 날짜: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (작성자 [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**풀스택 UI 빌드에서 GLM-5.2를 비교하려면 이 사례를 사용하십시오. 가장 세련된 트레이딩 데스크 결과에 근접했지만 비용은 최상위 결과의 일부에 불과했습니다.**

Atomic Chat은 프런트엔드, 백엔드, 8개 종목의 시장 데이터, 커스텀 다크 테마 UI를 포함한 동일한 Trader Desk 빌드 프롬프트로 4개 모델을 비교했습니다. 게시물에 따르면 GLM-5.2는 13,677토큰에 0.03달러였고, Fugu Ultra는 22,225토큰에 0.51달러였습니다. GLM은 훨씬 낮은 비용으로 라이브 데이터가 포함된 유사한 수준의 완성도 높은 멀티패널 인터페이스를 만들었다고 합니다.

유형: 평가 | 날짜: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Luddite Game After Claude Refusal](https://x.com/atmoio/status/2069559053114577088) (작성자 [@atmoio](https://x.com/atmoio))

**폐쇄형 모델이 거절한 게임 아이디어를 GLM-5.2로 대체 프로토타이핑하고 실제 출력물을 직접 검토하려면 이 사례를 사용하십시오.**

atmoio는 AI를 파괴하는 Plague Inc 스타일의 유머 게임이 Claude에서 허용 정책 위반으로 막혀, 대신 GLM 5.2로 Luddite를 만들고 데모 영상까지 첨부했다고 말합니다. 정책 이유로 폐쇄형 모델이 거절할 수 있는 creative coding task에서의 실사용 대안 사례로 볼 수 있습니다.

유형: 데모 | 날짜: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 공급자 및 도구 통합
<a id="case-170"></a>
### Case 170: [NVIDIA Free API Plug-And-Play Access](https://x.com/hqmank/status/2072855265612030010) (작성자 [@hqmank](https://x.com/hqmank))

**이 사례는 무료 hosted endpoint를 통해 GLM-5.2를 빠르게 시험할 때 유용합니다. hqmank는 NVIDIA가 OpenAI 호환 API 경로를 열었고, plug-and-play 대체 경로로 바로 동작했다고 확인했습니다.**

hqmank는 GLM-5.2가 NVIDIA 무료 API에 추가됐고, 간단한 hands-on test에서 정상 동작했다고 말합니다. 게시물은 이를 OpenAI 호환이면서 plug-and-play라고 설명하지만, 무료 tier는 수요가 몰리면 빠르게 제한될 수 있다고도 경고합니다. 빠른 평가나 임시 agent routing을 위한 실용적인 access note입니다.

유형: 통합 | 날짜: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [Free Workers AI Coding-Agent Route](https://x.com/ClaudeCode_UT/status/2072881775408456066) (작성자 [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**이 사례는 coding agent용 무료 GLM-5.2 경로를 세울 때 유용합니다. 이 튜토리얼은 OpenAI 호환 `cf/zai-org/glm-5.2` endpoint를 통해 Workers AI를 Claude Code, OpenCode, Cursor, Aider에 연결합니다.**

ClaudeCode_UT는 Cloudflare 무료 계정 생성, Workers AI account ID 복사, API token 발급, OpenAI 호환 도구에 Cloudflare provider 추가, `cf/zai-org/glm-5.2` 선택, 그리고 Claude Code나 Cursor, Aider, OpenCode 실행까지 6단계를 제시합니다. 토큰 과금을 시작하기 전에 coding-agent workflow를 시험하려는 팀에게 실용적인 access tutorial입니다.

유형: 튜토리얼 | 날짜: 2026-07-03

---

<a id="case-208"></a>
### Case 208: [Open Molecular Viewer Agent Stack](https://x.com/MaziyarPanahi/status/2075913552854933869) (작성자 [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**이 사례는 GLM-5.2를 열린 scientific inspection workflow에 연결할 때 유용합니다. MaziyarPanahi가 Hugging Face Inference Providers 경유 GLM-5.2를 llama.cpp 위의 Qwen3-VL, Mol*, PydanticAI와 묶어 하나의 prompt로 EGFR와 erlotinib 구조를 렌더링하고 비평했기 때문입니다.**

MaziyarPanahi는 GLM-5.2가 Hugging Face Inference Providers를 통해 language brain 역할을 하고, Qwen3-VL이 llama.cpp로 시각 검토를 맡고, Mol*가 구조를 렌더링하며, PydanticAI가 agent layer를 조정하는 완전히 열린 스택을 설명합니다. 게시물에 따르면 이 workflow는 RCSB PDB의 EGFR와 erlotinib 예제를 하나의 prompt에서 여섯 개의 render로 만들었고, 그래서 단순한 availability announcement가 아니라 여러 도구를 잇는 과학 워크플로 통합 사례가 됩니다.

유형: 통합 | 날짜: 2026-07-11

---
<a id="case-204"></a>
### Case 204: [Perplexity Advisor WANDR Cost Baseline](https://x.com/perplexity_ai/status/2075229779716973030) (작성자 [@perplexity_ai](https://x.com/perplexity_ai))

**이 사례는 routing된 computer-use harness 안에서 GLM-5.2의 경제성을 추정할 때 유용합니다. Perplexity가 GLM 5.2 plus advisor setup이 WANDR 2.1x, Opus 6.1x라고 밝히며 전체 benchmark에서도 비용이 거의 절반 수준이라고 했기 때문입니다.**

Perplexity는 task당 비용을 GLM 5.2 baseline으로 측정했고, WANDR에서 GLM 5.2 plus advisor route가 2.1x, Opus가 6.1x였다고 말합니다. 더 비싼 closed model을 모든 step에 쓰는 대신, 더 저렴한 GLM core를 selective escalation과 조합하는 computer-agent routing의 구체적인 신호로 볼 수 있습니다.

유형: 평가 | 날짜: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [Coworker Open Artifacts Routing](https://x.com/coworkerapp/status/2075233366266310905) (작성자 [@coworkerapp](https://x.com/coworkerapp))

**이 사례는 GLM-5.2를 enterprise artifact workflow에 넣고 싶을 때 유용합니다. Coworker는 Open Artifacts가 docs, decks, PDF, spreadsheets, dashboards, apps를 만들 수 있고, optimized router가 토큰 사용량을 약 5배 줄이면서도 미국 호스팅 GLM 5.2를 제공한다고 말합니다.**

Coworker는 Open Artifacts가 docs, decks, dashboards, spreadsheets, PDF, full apps 같은 공유 가능한 결과물을 만들 수 있다고 설명합니다. 같은 launch post에서 optimized mode가 task별로 적절한 model을 골라 토큰 사용량을 약 다섯 배 줄이면서도, 팀이 미국 호스팅, SOC 2, connector가 풍부한 환경에서 GLM 5.2를 쓸 수 있게 한다고도 말합니다.

유형: 통합 | 날짜: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [DotCode Context Upload Workflow](https://x.com/stagedhappen/status/2074775356867789241) (작성자 [@stagedhappen](https://x.com/stagedhappen))

**이 사례는 private coding sandbox 안에서 GLM-5.2에 더 풍부한 project context를 주고 싶을 때 유용합니다. DotCode가 GLM 5.2 지원과 함께 screenshot, image, CSV, PDF, source file, zip 업로드를 같은 filesystem-and-terminal workflow로 넣을 수 있게 했기 때문입니다.**

DotCode는 GLM 5.2가 contextual workspace upload와 함께 동작해 agent가 파일을 검사하고, 프로젝트 구조를 탐색하고, 코드를 수정하고, terminal command를 실행하고, 같은 sandbox에서 이어서 작업할 수 있다고 말합니다. 게시물은 지원 입력 형식을 나열하고 prompt plus files에서 sandbox execution으로 가는 흐름도 설명하며, 이를 실제 프로젝트 context에서 시작하는 진짜 coding-agent 작업으로 가는 한 걸음으로 제시합니다.

유형: 통합 | 날짜: 2026-07-08

---
<a id="case-209"></a>
### Case 209: [Colibri 25GB RAM Sparse Streaming](https://x.com/techNmak/status/2075872446197158361) (작성자 [@techNmak](https://x.com/techNmak))

**이 사례는 로컬 GLM-5.2 실험의 새로운 하한을 파악할 때 유용합니다. techNmak이 Colibrì가 NVMe에서 expert를 스트리밍해 약 25GB RAM으로 744B MoE를 돌리지만, 가장 작은 구성은 대략 0.05~0.1 tok/s에 머문다고 설명하기 때문입니다.**

techNmak은 Colibrì를 항상 뜨거운 가중치만 RAM에 두고 라우팅된 expert는 NVMe에 보관하는 순수 C 기반 로컬 inference 엔진으로 요약합니다. 상주 메모리는 약 9.9GB, 채팅 중 RAM 피크는 약 20GB, int4 가중치는 디스크에서 약 370GB 수준이며, 게시물은 이를 빠른 프로덕션 serving이 아니라 시스템 차원의 proof of concept라고 분명히 말합니다. 25GB 머신의 cold generation은 0.05~0.1 tok/s 정도에 그치고 int4 양자화가 품질에 미치는 영향도 아직 충분히 benchmark되지 않았기 때문입니다.

유형: 데모 | 날짜: 2026-07-11

---
<a id="case-206"></a>
### Case 206: [SGLang NVFP4 Production Throughput](https://x.com/sgl_project/status/2075721488456654861) (작성자 [@sgl_project](https://x.com/sgl_project))

**이 사례는 GLM-5.2 NVFP4용 프로덕션 SGLang serving 규모를 가늠할 때 유용합니다. 공식 SGLang v0.5.15 릴리스가 batch size 1 기준 8x B300에서 사용자당 500+ tok/s, 4x GB300에서 450 tok/s에 도달했다고 밝혔기 때문입니다.**

SGLang v0.5.15의 공식 발표에 따르면 이번 릴리스 사이클은 GLM-5.2 NVFP4의 프로덕션 튜닝에 집중했습니다. 이 포스트는 bs=1 기준 8x B300에서 사용자당 500이 넘는 tok/s, 4x GB300에서 450 tok/s를 보고하고 있어, hosted 또는 self-managed inference stack을 평가하는 팀에게 구체적인 배포 throughput 기준점을 제공합니다. 같은 발표는 이것을 일회성 실험실 해킹이 아니라 업스트림 제품 지원으로 설명합니다.

유형: 평가 | 날짜: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Dahl 100M Free GLM Endpoint](https://x.com/pengsonal/status/2074908680106180669) (작성자 [@pengsonal](https://x.com/pengsonal))

**이 사례는 카드 없이 OpenAI-compatible 경로로 GLM-5.2를 시험해 볼 때 유용합니다. Dahl Inference가 GLM 5.2 FP8에 대해 100M 무료 토큰을 제공하고, key 생성과 `/v1/chat/completions` 호출 방법까지 보여 주기 때문입니다.**

게시물은 GLM 5.2 FP8을 Dahl의 무료 오픈모델 endpoint 목록에 넣고, 가입이나 카드가 필요 없다고 설명합니다. 또한 웹 UI에서 key를 만들고 OpenAI-compatible `/v1/chat/completions` endpoint를 쓰는 구체적 setup 흐름을 주며, direct `curl` 요청은 Cloudflare 403을 맞을 수 있지만 web chat 경로는 동작한다는 점도 함께 적고 있습니다.

유형: 튜토리얼 | 날짜: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [NVIDIA Free Endpoint GLM Setup](https://x.com/undefinedKi/status/2074491917333655948) (작성자 [@undefinedKi](https://x.com/undefinedKi))

**이 사례는 self-hosting 없이 coding tool에서 GLM-5.2를 시험해 볼 때 유용합니다. source가 무료 NVIDIA endpoint 흐름으로 GLM-5.2 API key를 Claude Code, Cursor, Cline에 넣는 방법을 설명하기 때문입니다.**

게시물은 NVIDIA가 GLM-5.2를 포함한 주요 모델용 무료 API key를 공개했고, 이어서 직접적인 setup path를 설명합니다. 방법은 NVIDIA 계정을 만들고, free endpoint 모델의 Build 탭을 열고, API key를 생성한 뒤 base URL과 key를 Claude Code, Cursor, Cline에 붙여 넣는 것입니다. 그래서 이것은 per-token billing이나 로컬 GPU 스택 없이 GLM-5.2를 시험하는 실용적인 access tutorial입니다.

유형: 튜토리얼 | 날짜: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [0G TeeML Private Inference Route](https://x.com/0G_labs/status/2074496704959676682) (작성자 [@0G_labs](https://x.com/0G_labs))

**이 사례는 GLM-5.2를 privacy-first provider 경로로 붙일 때 유용합니다. 0G가 GLM 5.2가 TeeML에서 TEE enclave 안에 prompt를 봉인한 채 실행되고, 가격도 공식 경로보다 낮다고 말했기 때문입니다.**

0G는 TeeML을 private inference tier로 설명하며, GLM 5.2가 trusted execution environment 안에서 verifiable하게 실행된다고 말합니다. 게시물 자체는 짧지만 provider integration과 privacy, pricing 관점을 동시에 제공하므로, 모델 품질 주장보다는 deployment route 신호로 읽는 편이 맞습니다.

유형: 통합 | 날짜: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [DuckDB Flock Open-SQL PR](https://x.com/lhoestq/status/2074143736624275629) (작성자 [@lhoestq](https://x.com/lhoestq))

**이 사례는 GLM-5.2를 완전히 열린 로컬 SQL analysis 스택에 넣고 싶을 때 유용합니다. lhoestq에 따르면 duckdb와 flock PR로 GLM-5.2를 100% open-source 데이터 스택 안에서 쓸 수 있기 때문입니다.**

게시물은 duckdb에서 flock를 통해 GLM-5.2를 활성화하는 PR을 열었다고 말하며, frontier급 open intelligence를 직접 데이터 작업에 붙이는 경로로 설명합니다. 다만 source는 merge된 release note가 아니라 PR-open 신호이므로, 이 사례는 local analytics와 SQL-native workflow를 위한 integration-in-progress로 보는 편이 맞습니다.

유형: 통합 | 날짜: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [One-Key 26-Model API Access](https://x.com/Alan_Earn/status/2073663239028924680) (작성자 [@Alan_Earn](https://x.com/Alan_Earn))

**이 사례는 하나의 OpenAI 호환 제공자 경로로 GLM-5.2를 시험할 때 유용합니다. Alan_Earn에 따르면 API 키 하나로 GLM-5.2를 포함한 26개 모델에 접근할 수 있고 시작 크레딧 26달러도 함께 제공되기 때문입니다.**

게시물은 계정 생성, 카드 추가, dashboard 잠금 해제, credits 수령, API 키 생성, 그리고 그 키를 Codex, Cursor, OpenCode, OpenClaw, Hermes 등에 붙여 넣는 짧은 setup을 설명합니다. pay as you go 방식과 큰 frontier model이 무료 credits를 빠르게 소모한다는 점도 적어 두어, 주로 access와 pricing 메모로 유용합니다.

유형: 튜토리얼 | 날짜: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [NVIDIA NIM OpenCode Thinking Setup](https://x.com/Dracoshowumore/status/2073384581256929717) (작성자 [@Dracoshowumore](https://x.com/Dracoshowumore), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI))

**이 사례는 thinking을 명시적으로 켠 무비용 경로로 NVIDIA 무료 NIM endpoint를 통해 GLM-5.2를 OpenCode에 연결하고 싶을 때 쓰기 좋습니다. Dracoshowumore는 API key 발급 흐름, base URL, 그리고 tool layer가 function calls를 맡는 동안 GLM은 enable_thinking=true로 돌리는 OpenCode 설정을 공유합니다.**

Dracoshowumore는 NVIDIA developer platform 등록, GLM-5.2 API key 생성, 공개된 base URL을 OpenCode에 연결, 모델의 native tool calling 비활성화, provider options에 chat_template_kwargs.enable_thinking=true 전달까지 전체 설정 경로를 정리합니다. 같은 게시물은 NIM 경로가 기본적으로 function calling이나 reasoning traces를 노출하지 않으므로 도구 오케스트레이션을 OpenCode가 맡아야 한다고도 말합니다. 단순한 무료 endpoint 공지가 아니라 실전 구성 메모에 가깝습니다.

유형: 튜토리얼 | 날짜: 2026-07-04

<a id="case-165"></a>
### Case 165: [ZCode Launch With Mobile Agent Control](https://x.com/Digiato/status/2072663459850829985) (작성자 [@Digiato](https://x.com/Digiato))

**이 사례는 ZCode를 GLM-5.2의 공식 coding surface로 평가할 때 유용합니다. launch report에 따르면 이 무료 agentic IDE는 Windows, macOS, Linux에서 제공되며 Telegram, WeChat, Feishu로 프로젝트 진행 상황을 확인할 수 있습니다.**

Digiato는 ZCode를 GLM-5.2 중심으로 구축된 무료 agentic development environment로 설명하며 Cursor, Claude Code, Copilot의 대안으로 배치합니다. 게시물에 따르면 Windows, macOS, Linux에서 제공되고, GLM-5.2와 깊게 통합되며, Telegram, WeChat, Feishu를 통해 진행 상황을 확인할 수 있습니다. 단순한 모델 발표보다 더 실무적인 access surface입니다.

유형: 통합 | 날짜: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki Auto-Maintained Agent Docs](https://x.com/LangChain/status/2072745455788933321) (작성자 [@LangChain](https://x.com/LangChain))

**이 사례는 agent가 읽는 문서를 자동으로 최신 상태로 유지하고 싶을 때 유용합니다. LangChain에 따르면 OpenWiki는 코드 변경에 맞춰 repo docs를 다시 만들고 유지하며 GLM 5.2 같은 open model 위에서 동작합니다.**

LangChain은 OpenWiki를 coding agent용 open-source 문서 유지 레이어로 설명합니다. 게시물에 따르면 open harness와 open CLI workflows를 결합하고, codebase가 바뀔 때마다 docs를 갱신하며, GLM 5.2와 Kimi K2.7 같은 open model에서 실행됩니다. 수동 wiki 대신 agent가 최신 repo docs를 읽게 하고 싶은 팀에 맞는 실용적인 file-based memory 패턴입니다.

유형: 통합 | 날짜: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [Foundry PTUs Through FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (작성자 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**이 사례를 쓰면 에이전트 클라이언트를 다시 만들지 않고도 기업용 Foundry 예산으로 GLM-5.2를 라우팅할 수 있습니다. Fireworks에 따르면 FireConnect가 Microsoft Foundry PTU를 Codex, OpenCode, Pi 워크플로에 연결해 주기 때문입니다.**

Fireworks에 따르면 GLM 5.2는 이제 Microsoft Foundry에서 사용할 수 있습니다. FireConnect를 켜면 팀은 Foundry PTU를 쓰면서도 Codex, OpenCode, Pi에서 그대로 요청을 보낼 수 있어, 에이전트 표면마다 별도 모델 경로를 세울 필요가 없습니다.

유형: 통합 | 날짜: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM Eval Workbench](https://x.com/ankrgyl/status/2072042305108722040) (작성자 [@ankrgyl](https://x.com/ankrgyl))

**GLM-5.2와 Opus를 같은 eval 스택 안에서 비교하고 싶다면 이 사례가 유용합니다. Braintrust와 Baseten이 long-context 정확도 대 비용 차이를 구체적인 예와 함께 공개했기 때문입니다.**

ankrgyl은 Braintrust가 Baseten 지원과 함께 GLM-5.2를 추가해 팀들이 eval과 production trace 양쪽에서 모델을 돌릴 수 있게 했다고 말합니다. 공개된 예시는 25K와 50K token long-context retrieval을 비교하며, Opus 4.8이 약 3.5포인트 앞서지만 trace당 비용은 약 4.1배에서 4.5배 더 든다고 설명합니다.

유형: 통합 | 날짜: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass 오픈웨이트 정액 구독](https://x.com/iam_elias1/status/2071655509611151674) (작성자 [@iam_elias1](https://x.com/iam_elias1))

**여러 open-weight 코딩 모델을 하나의 agent harness 안에 모으고 싶다면 이 사례가 유용합니다. ClinePass가 GLM-5.2와 관련 모델을 provider별 키와 청구서 대신 월정액으로 묶기 때문입니다.**

iam_elias1은 ClinePass를 GLM-5.2, DeepSeek, Kimi, Qwen, MiniMax, MiMo 등 오픈웨이트 모델을 Cline의 IDE 확장과 CLI에서 쓸 수 있게 해 주는 월 9.99달러 경로로 설명합니다. 이 스레드는 provider별 API key를 대체하고, 표준 API 한도의 2-5배를 제공하며, 작업 단계에 따라 세션 중간에 모델을 바꿀 수 있고, CLI로 가입하면 첫 달이 1.99달러라고 말합니다.

유형: 통합 | 날짜: 2026-06-29

<a id="case-137"></a>
### Case 137: [코딩 에이전트를 위한 무료 GLM API 서비스](https://x.com/mcwangcn/status/2071261128575897901) (작성자 [@mcwangcn](https://x.com/mcwangcn))

**Hermes나 다른 coding agent에서 가입 없이 GLM-5.2를 시험하려면 이 사례를 사용하십시오. 공유 서비스가 짧게 유지되는 API key를 발급해 설정을 가볍게 유지한다고 설명합니다.**

mcwangcn은 가입이나 로그인 없이 Lobster, Hermes, 기타 coding agent에서 사용할 수 있다고 하는 무료 GLM-5.2 API 서비스를 공유했습니다. 같은 게시물은 생성된 API key가 갱신 전까지 1시간만 유지된다고 말하며, 이것이 구체적인 anti-abuse 제약이자 장기 무인 운영보다 빠른 워크플로 테스트에 더 적합한 이유라고 설명합니다.

유형: 통합 | 날짜: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (작성자 [@opencode](https://x.com/opencode))

**이 사례를 사용하면 텍스트, 1M 컨텍스트 및 GLM-5.1과 유사한 가격으로 OpenCode Go 워크플로 내에서 GLM-5.2 가용성을 추적할 수 있습니다.**

OpenCode는 Go에서 GLM-5.2 가용성을 발표하여 텍스트 지원, 1M 컨텍스트 창 및 5.1과 동일한 가격을 강조했습니다.

유형: 통합 | 날짜: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (작성자 [@ollama](https://x.com/ollama))

**이 사례를 사용하여 액세스 가능한 오픈 소스 코딩 모델 실험을 위해 GLM-5.2를 Ollama Cloud로 라우팅합니다.**

Ollama는 GLM-5.2 가용성을 발표하면서 이를 1M 컨텍스트를 갖춘 장거리 코딩 및 에이전트 작업 모델로 설명했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (작성자 [@OpenRouter](https://x.com/OpenRouter))

**공급자 라우팅 또는 다중 모델 스택을 비교할 때 OpenRouter를 통해 GLM-5.2에 액세스하려면 이 사례를 사용하십시오.**

OpenRouter는 GLM-5.2 가용성을 100만 토큰 장기 모델로 발표하여 사용자에게 공급자 중립적인 호출 경로를 제공했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (작성자 [@vllm_project](https://x.com/vllm_project))

**이 사례를 사용하면 Day-Zero 지원이 포함된 vLLM을 통해 GLM-5.2를 자체 호스팅하거나 제공할 수 있습니다.**

vLLM 프로젝트는 v0.23.0에서 GLM-5.2 지원을 발표하여 이를 1M 컨텍스트를 갖춘 장거리 코딩 에이전트를 위한 주력 모델로 구성했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (작성자 [@NotionHQ](https://x.com/NotionHQ))

**이 사례를 사용하여 GLM-5.2를 Notion 워크플로 내에서 사용할 수 있는 개방형 모델로 식별하세요.**

Notion은 장거리 작업을 위해 구축되고 Baseten을 통해 제공되는 개방형 모델로 GLM-5.2 가용성을 발표했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (작성자 [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**이 사례를 사용하여 Fireworks를 호스팅된 인프라가 필요한 GLM-5.2 워크로드에 대한 제공 경로로 평가합니다.**

Fireworks는 SWE-Bench, Terminal-Bench, GPQA 및 AIME에 대한 1M 컨텍스트, 코딩 우선 포지셔닝 및 독립적 검증을 강조하는 GLM-5.2를 첫날 라이브로 발표했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Google Cloud 모델 Garden 링크](https://x.com/CarolGLMs/status/2067127223216419088) (작성자 [@CarolGLMs](https://x.com/CarolGLMs))

**이 사례를 사용하여 Google Cloud 기반 배포 및 에이전트 플랫폼 컨텍스트에서 GLM-5.2를 찾으세요.**

CarolGLM은 GLM-5.2용 Google Cloud 링크를 공유하여 클라우드 모델 카탈로그를 통해 작업하는 팀을 위한 직접적인 포인터가 되었습니다.

유형: 통합 | 날짜: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (작성자 [@AskVenice](https://x.com/AskVenice))

**개인 정보 보호 모드, TEE 또는 종단 간 암호화가 GLM-5.2를 시도하는 데 결정적인 요소인 경우 이 사례를 사용하십시오.**

베니스는 개인 에이전트 코딩 및 장거리 작업을 목표로 하는 TEE/E2EE 프레이밍을 갖춘 개인 정보 보호 모드에서 GLM-5.2 가용성을 발표했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (작성자 [@CommandCodeAI](https://x.com/CommandCodeAI))

**이 사례를 통해 저렴한 진입 계획과 긴 컨텍스트 코딩 기능을 갖춘 명령 코드의 GLM-5.2를 사용해 보세요.**

Command Code는 1M 컨텍스트, 강력한 추론, 오픈 소스 상태 및 1달러 Go 계획을 통한 액세스를 언급하면서 GLM-5.2 가용성을 발표했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Nous Portal의 헤르메스 에이전트](https://x.com/Teknium/status/2066954081575592282) (작성자 [@Teknium](https://x.com/Teknium))

**Nous Portal 및 OpenRouter를 통해 GLM-5.2를 Hermes Agent 워크플로에 연결하려면 이 사례를 사용하세요.**

Teknium은 에이전트 프레임워크 라우팅 실험에 유용한 Nous Portal 및 OpenRouter의 Hermes Agent에서 GLM-5.2 가용성을 보고했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (작성자 [@ionet](https://x.com/ionet))

**753B 매개변수 긴 컨텍스트 모델에 대한 컴퓨팅 지원 제공을 평가할 때 이 사례를 사용하세요.**

io.net은 1M 컨텍스트, 에이전트 우선 설계, 장거리 코딩 및 753B 매개변수 모델의 컴퓨팅 요구 사항을 강조하면서 GLM-5.2의 Day-Zero 출시 파트너로 발표했습니다.

유형: 통합 | 날짜: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (작성자 [@clattner_llvm](https://x.com/clattner_llvm))

**공급자 규모에서 제공되는 장기 컨텍스트 GLM-5.2용 Modular Cloud를 고려하려면 이 사례를 사용하세요.**

Chris Lattner는 GLM-5.2가 첫날 Modular Cloud에 게시되어 공개 가중치, 코딩, 장거리 에이전트 및 1M 컨텍스트를 강조했다고 게시했습니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (작성자 [@agentnative_](https://x.com/agentnative_))

**저렴한 개방형 모델 코딩 워크플로우를 위해 OpenRouter를 통해 Cursor에서 GLM-5.2를 구성하려면 이 사례를 사용하십시오.**

소스는 모델 가용성만 발표하는 것이 아니라 구체적인 Cursor/OpenRouter 설정 경로를 제공합니다.

유형: 튜토리얼 | 날짜: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (작성자 [@beyang](https://x.com/beyang))

**텍스트 전용 모델에 디자인 작업을 위한 시각적 검토 지원이 필요한 경우 이 사례를 사용하여 GLM-5.2를 Amp 사용자 지정 에이전트와 페어링합니다.**

이 게시물은 GLM-5.2 시각적 디자인 벤치마크 결과를 리뷰 레이어를 제공할 수 있는 Amp 플러그인 에이전트와 연결합니다.

유형: 통합 | 날짜: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (작성자 [@alphatozeta8148](https://x.com/alphatozeta8148))

**Factory Droid, OpenCode 및 코딩 하네스에 대해 긴 컨텍스트 제공 속도가 중요한 경우 이 사례를 사용하여 Baseten을 통해 GLM-5.2를 라우팅합니다.**

소스는 전체 1M 컨텍스트에서 4배 더 빠르게 실행되는 GLM-5.2를 보고하고 이를 코딩 하네스에 보여줍니다.

유형: 통합 | 날짜: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [웹 디자인용 Browser Use QA subagents](https://x.com/browser_use/status/2068405699340853541) (작성자 [@browser_use](https://x.com/browser_use))

**text-only model 에 시각 검수가 필요할 때 GLM-5.2를 Browser Use v2의 multimodal QA subagents 와 조합해 반복적인 웹사이트 수정에 쓰는 사례입니다.**

Browser Use 는 GLM-5.2가 웹사이트 디자인 작업에서 Fable 5를 이긴 뒤, 결과를 inspection 하고 미감을 판단하며 bug 를 찾고 targeted fix 를 GLM 에 다시 넘기는 QA subagents 를 추가했다고 전합니다. build 와 QA 를 포함한 전체 루프 비용은 $0.75 미만이었다고 합니다.

유형: 통합 | 날짜: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 공식 IDE 일일 무료 토큰](https://x.com/Alan_Earn/status/2068223665268006924) (작성자 [@Alan_Earn](https://x.com/Alan_Earn))

**큰 daily token allowance 와 Cursor 유사 workflow 를 제공하는 무료 공식 coding IDE 로 ZCode 를 통해 GLM-5.2에 접근하는 사례입니다.**

이 글은 ZCode 를 Zhipu 의 공식 coding IDE 로 소개하며, GLM-5.2를 default model 로 두고 하루 300만 token, 1M context, Mac/Windows client 를 제공한다고 설명합니다. 짧은 setup flow 도 포함되어 있어 단순한 launch announcement 보다 실용적입니다.

유형: 튜토리얼 | 날짜: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (작성자 [@skirano](https://x.com/skirano))

**Fireworks를 통해 GLM-5.2를 Cursor에 최소 설정으로 연결하고, 별도 클라이언트 코드 없이 시험하기 위한 사례입니다.**

Skirano는 Cursor의 OpenAI API key 칸에 Fireworks key를 붙여 넣고, base URL로 `https://api.fireworks.ai/inference/v1` 를 쓰며, model로 `accounts/fireworks/models/glm-5p2` 를 고른 뒤 재시작하는 최소 설정 흐름을 보여 줍니다. 익숙한 coding IDE 안에서 GLM-5.2를 바로 시도할 수 있는 구체적인 경로입니다.

유형: 튜토리얼 | 날짜: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (작성자 [@vulcanbench](https://x.com/vulcanbench))

**전용 ZAI provider 지원과 API key 경로를 갖춘 오픈 benchmark harness에서 GLM-5.2를 실행하기 위한 사례입니다.**

VulcanBench v0.2.0은 first-class ZAI support를 추가해 GLM-5.2를 `zai:glm-5.2` 로 OpenAI, Anthropic 모델과 나란히 실행할 수 있게 했습니다. 전용 `ZAI_API_KEY` 경로도 제공해, 일회성 screenshot보다 재현 가능한 오픈 benchmark harness를 원하는 사람에게 유용합니다.

유형: 통합 | 날짜: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (작성자 [@OpenCodeLog](https://x.com/OpenCodeLog))

**OpenCode 안에서 GLM-5.2의 High / Max reasoning variant에 접근하면서 step-limit 처리 개선까지 함께 가져오기 위한 사례입니다.**

OpenCode v1.17.9는 GLM-5.2를 위한 High와 Max thinking variant를 OpenAI 호환 및 Anthropic 호환 provider 전반에 추가했고, OpenRouter effort mapping도 native하게 다룹니다. 같은 release에서 agent step-limit 동작도 고쳐져 더 긴 실행에 실용성이 높아졌습니다.

유형: 통합 | 날짜: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**GLM-5.2 coding plan 트래픽을 일반 API가 아니라 coding 최적화 Z.ai endpoint로 보내기 위한 사례입니다.**

이 게시물은 coding plan workload에 대해 일반 `https://api.z.ai/api/paas/v4/` 대신 `https://api.z.ai/api/coding/paas/v4` 를 쓰라고 안내합니다. 또한 Claude Code와 OpenCode 같은 도구가 지원하는 경우 `https://api.z.ai/api/anthropic` 을 주로 사용한다고 덧붙입니다. GLM-5.2가 잘못 라우팅되는 것처럼 보일 때 쓸 수 있는 구체적인 설정 수정입니다.

유형: 튜토리얼 | 날짜: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (작성자 [@0x_kaize](https://x.com/0x_kaize))

**무료 GLM-5.2 API key와 base URL을 받아 Claude, Cursor, Hermes 같은 도구에 연결하기 위한 사례입니다.**

작성자는 5분 정도면 무료 ZenMux API key와 base URL을 발급받아 GLM-5.2를 Claude, Cursor, Hermes 등에 연결할 수 있는 흐름을 공유합니다. 다만 무료 tier는 빠르게 rate-limit에 걸린다고 덧붙여, 지속성 보장보다는 access note로 보는 편이 맞습니다.

유형: 튜토리얼 | 날짜: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (작성자 [@_xjdr](https://x.com/_xjdr))

**기본 모델 지원과 함께 표준 엔드포인트와 1M 컨텍스트 엔드포인트를 분리한 ncode 및 Noumena 스타일 에이전트 환경에 GLM-5.2를 라우팅하려면 이 사례를 사용하십시오.**

Noumena 업데이트에 따르면 팀은 도구 호출, 함수 파싱, 앱 라우팅, 추론 추적 전반에 걸쳐 GLM을 1급 지원으로 추가했습니다. 이어서 1M 컨텍스트 트래픽이 몰릴 때 TTFT를 제어하기 위해 API를 `glm-5.2`와 `glm-5.2[1m]` 엔드포인트로 분리했습니다. 또한 최근 ncode 빌드는 사용 피드백이 좋았기 때문에 opus급 기본 모델을 Kimi에서 GLM으로 바꿨다고 설명합니다.

유형: 통합 | 날짜: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (작성자 [@thealexker](https://x.com/thealexker))

**Baseten 키, 커스텀 base URL, `~/.claude/settings.json`의 모델 재매핑을 통해 Claude Code 안에서 GLM-5.2를 실행하려면 이 사례를 사용하십시오.**

이 튜토리얼은 Claude Code 설치, Baseten 계정 생성, API 키 확보, 그리고 `~/.claude/settings.json` 편집 과정을 안내합니다. 세 가지 Claude 모델 티어 모두를 커스텀 Anthropic 환경 변수로 `zai-org/GLM-5.2`에 연결하는 방식입니다. Claude Code 클라이언트에서 GLM-5.2를 사용하는 구체적인 드롭인 설정 패턴입니다.

유형: 튜토리얼 | 날짜: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (작성자 [@cramforce](https://x.com/cramforce))

**보안 하네스에서 GLM-5.2를 시험하려면 이 사례를 사용하십시오. `deepsec`는 Pi agent의 기본 모델로 채택했고 경쟁력 있는 eval 결과를 보고했습니다.**

이 게시물은 `@badlogicgames`의 Pi agent에 대한 `deepsec` 지원을 발표하면서 GLM-5.2를 기본 모델로 설정했고, 실행 가능한 명령 `pnpm deepsec process --agent pi`도 제공합니다. 또한 작성자는 Deepsec evals를 돌려 본 결과 다른 프런티어 모델과 비교해도 경쟁력이 있었다고 말하며, 이를 구체적인 보안 지향 통합 지점으로 제시합니다.

유형: 통합 | 날짜: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid Harness Quickstart](https://x.com/RayFernando1337/status/2069523126384525639) (작성자 [@RayFernando1337](https://x.com/RayFernando1337))

**Baseten과 Droid harness를 통해 GLM-5.2를 빠르게 띄우고 다른 IDE에도 재사용할 수 있는 짧은 설정 흐름을 확보하려면 이 사례를 사용하십시오.**

RayFernando1337는 Baseten API key 발급, Droid AI 설정 자동화, GLM-5.2 통합 테스트, 대체 설정과 제약 검토, 다른 IDE를 위한 보너스 설정 노트까지 타임스탬프와 함께 정리합니다.

유형: 튜토리얼 | 날짜: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI-Compatible GLM API Workflow](https://x.com/Marktechpost/status/2069308807570915500) (작성자 [@Marktechpost](https://x.com/Marktechpost))

**reasoning control, tool calling, 장문맥 retrieval, cost tracking을 갖춘 OpenAI 호환 GLM-5.2 클라이언트를 Python으로 구성하려면 이 사례를 사용하십시오.**

Marktechpost는 GLM-5.2를 하나의 OpenAI 호환 클라이언트로 감싸는 튜토리얼과 연결된 코드 notebook을 공유했습니다. 게시물에 따르면 thinking effort 제어(`off` / `high` / `max`), reasoning과 answer의 스트리밍 분리, multi-step agent용 tool calling, structured JSON output, long-context retrieval, token cost tracking까지 포함합니다.

유형: 튜토리얼 | 날짜: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API Search Sandbox](https://x.com/perplexitydevs/status/2069252848647606584) (작성자 [@perplexitydevs](https://x.com/perplexitydevs))

**search 지원 sandboxed agent를 단일 API call 뒤에 두고 싶을 때 Perplexity Agent API에 GLM-5.2를 연결하려면 이 사례를 사용하십시오.**

Perplexity Devs는 Agent API에 GLM-5.2를 추가하면서 장기 코딩과 agentic workflow에 잘 맞는다고 설명했습니다. 게시물은 Search as Code, OpenAI 호환 인터페이스, 그리고 마크업 없는 first-party pricing을 구체적으로 강조합니다.

유형: 통합 | 날짜: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (작성자 [@aqaderb](https://x.com/aqaderb))

**제공업체 지연 시간이 중요할 때 Baseten이 주장한 GLM-5.2의 고속 serving 신호를 확인하려면 이 사례를 사용하십시오. sub-second 수준의 first-token time과 높은 decoding throughput이 핵심입니다.**

aqaderb는 Baseten의 GLM-5.2 API가 0.8초 미만의 TTFT와 초당 280 tokens를 달성했다고 발표했습니다. 게시물은 PD disaggregation, multi-token prediction heads를 이용한 speculative decoding, KV-cache-aware routing 등 serving 최적화를 이유로 들며 관련 engineering write-up도 연결합니다.

유형: 통합 | 날짜: 2026-06-23

---

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI OpenCode 설정](https://x.com/RoundtableSpace/status/2070820686243959276) (작성자 [@RoundtableSpace](https://x.com/RoundtableSpace))

**직접 모델 호스트를 준비하지 않고, coding agent용 무료 OpenAI 호환 경로로 Cloudflare Workers AI를 통해 GLM-5.2를 돌리고 싶을 때 쓰는 사례입니다.**

RoundtableSpace는 무료 Cloudflare account를 만들고, Account ID를 확인하고, API token을 만든 뒤, OpenCode에 Cloudflare를 provider로 추가해 `@cf/zai-org/glm-5.2`를 지정할 수 있다고 말합니다. 게시물은 같은 경로가 OpenCode, Cursor, Aider, Hermes Agent, Claude Code 등 다른 OpenAI 호환 도구에도 통하고, coding agent용 hosted access의 실용적인 지름길이 된다고 덧붙입니다.

유형: 튜토리얼 | 날짜: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js 무설정 브라우저 클라이언트](https://x.com/FareaNFts/status/2070848321212792945) (작성자 [@FareaNFts](https://x.com/FareaNFts))

**API key, 과금, 백엔드 설정을 건드리기 전에 브라우저 전용 프로토타입에서 GLM-5.2를 시험하고 싶을 때 쓰는 사례입니다.**

FareaNFts는 Puter.js가 단일 CDN script tag만으로 GLM 계열을 클라이언트 측에 노출하며, `z-ai/glm-5.2`를 브라우저 코드에서 직접 호출할 수 있고 서버나 개발자 측 과금 설정도 필요 없다고 설명합니다. 게시물은 개인 도구, vibe coding app, 가벼운 agent를 빠르게 프로토타이핑하는 데 유용하다고 보면서도, Puter는 user-pays browser model이라 고처리량 프로덕션 트래픽용은 아니라는 tradeoff도 함께 적어 둡니다.

유형: 튜토리얼 | 날짜: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 통합 엔드포인트 접근](https://x.com/FareaNFts/status/2070900056736379288) (작성자 [@FareaNFts](https://x.com/FareaNFts))

**게시물은 무료 체험 credit이 붙은 단일 OpenAI 호환 SiliconFlow endpoint로 중국계와 서구권 모델을 함께 다룰 수 있다고 설명하므로, GLM-5.2를 더 넓은 multi-model stack 안에 넣고 싶을 때 쓰는 사례입니다.**

FareaNFts는 SiliconFlow가 GLM-5.2를 DeepSeek, Qwen, Llama 4, Hunyuan, Mistral, Yi, Gemma, Phi 등 200개가 넘는 모델과 함께 하나의 OpenAI 호환 endpoint로 제공한다고 말합니다. 게시물은 가입 시 카드 없이 1달러의 free credit이 주어지고, 일부 모델은 계속 무료이며, spending limit도 지원하고, 그 key를 Cursor, Claude Code, Aider 같은 도구에 그대로 넣을 수 있다고 설명합니다.

유형: 통합 | 날짜: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [HuggingChat 웹사이트 빌드와 HF Space 배포](https://x.com/victormustar/status/2070190742991994967) (작성자 [@victormustar](https://x.com/victormustar))

**HuggingChat 조사부터 Hugging Face Spaces의 static deploy까지 이어지는 거의 무료 personal-site flow에서 GLM-5.2를 써보려면 이 사례를 사용하십시오.**

victormustar는 Hugging Face account만 있으면 HuggingChat 안의 GLM-5.2에게 website를 만들라고 시킬 만큼의 free credits가 있고, 사용자에 대한 background research에는 Exa가 쓰인다고 말합니다. 같은 게시물은 결과 사이트를 static Hugging Face Space로 무료 배포할 수 있다고 덧붙여, 개인 사이트 실험을 위한 구체적이고 저비용인 경로를 보여 줍니다.

유형: 튜토리얼 | 날짜: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 제공](https://x.com/digitalocean/status/2070177703911719301) (작성자 [@digitalocean](https://x.com/digitalocean))

**1M context 모델을 직접 호스팅하지 않고 official provider access를 managed infrastructure로 쓰고 싶을 때 GLM-5.2를 연결하려면 이 사례를 사용하십시오.**

DigitalOcean은 자사 Inference Engine에 GLM-5.1과 GLM-5.2를 추가한다고 발표하며, 1M-token context window와 최대 8시간 agentic coding workflow를 겨냥한 모델로 포지셔닝했습니다. 게시물은 또한 사용량 기반 가격과 완전 관리형 인프라를 통해 기존 stack에 직접 통합할 수 있는 경로라고 설명합니다.

유형: 통합 | 날짜: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S 티어](https://x.com/CommandCodeAI/status/2069891896881857016) (작성자 [@CommandCodeAI](https://x.com/CommandCodeAI))

**가장 싼 진입 가격만이 아니라 장기 코딩 속도를 중시할 때 Command Code의 더 빠른 GLM-5.2 tier에 접근하려면 이 사례를 사용하십시오.**

Command Code는 GLM-5.2 Fast를 high-throughput build로 공개하며, 같은 frontier-coding 포지셔닝을 유지한 채 속도를 초당 120-250 tokens로 끌어올렸다고 말합니다. 게시물은 이 tier가 1M context, tool use, reasoning을 유지하면서 1달러 Go plan과 10달러 usage credits 이상에서 제공된다고도 명시합니다.

유형: 통합 | 날짜: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI Gateway Fast GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (작성자 [@wafer_ai](https://x.com/wafer_ai))

**서버리스 속도와 명시적 토큰 가격이 필요할 때 Vercel AI Gateway를 통해 GLM-5.2 Fast를 쓰려면 이 사례를 사용하십시오.**

wafer_ai는 GLM-5.2 Fast가 Vercel AI Gateway에 올라왔고, 속도는 초당 150-250 tokens, context window는 1M tokens, 가격은 100만 tokens당 input 3.00달러, output 10.25달러, cache 0.50달러라고 말합니다. 처리량과 예측 가능한 gateway 가격을 중시하는 팀에게 구체적인 hosted-access 정보입니다.

유형: 통합 | 날짜: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 비용, 가격, 로컬 배포
<a id="case-191"></a>
### Case 191: [Hermes-Built LiteLLM Local Lab](https://x.com/ivanfioravanti/status/2074609005272375329) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**이 사례는 GLM-5.2를 coding agent로 써서 local inference lab을 부트스트랩할 때 유용합니다. source에서 Hermes Agent와 GLM-5.2가 M3 Ultra 기반으로 LiteLLM, Postgres, Prometheus, Grafana를 연결했다고 말하기 때문입니다.**

게시물에 따르면 LiteLLM은 이미 M3 Ultra에서 돌아가고 있었고, 초기 테스트 경로로 DGX Spark 기반 Qwen 모델을 노출하고 있었습니다. 이 repo에 더 중요한 점은 저자가 Hermes Agent와 GLM-5.2가 LiteLLM, Postgres, Prometheus, Grafana 구성을 맡았다고 적은 부분입니다. 그래서 이 사례는 단순한 칭찬이 아니라 routing, persistence, observability를 포함한 local lab integration의 구체적 예시가 됩니다.

유형: 통합 | 날짜: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [Dual M5 Max Offline Droneship Sim](https://x.com/XavierLocalAI/status/2073938465121833452) (작성자 [@XavierLocalAI](https://x.com/XavierLocalAI))

**이 사례는 완전 offline Apple Silicon 환경에서 GLM-5.2 agent가 어디까지 가능한지 가늠할 때 유용합니다. XavierLocalAI가 두 대의 128GB M5 Max로 753B 구성을 돌리며 droneship landing simulator를 26 tok/s로 작성했다고 보고했기 때문입니다.**

source post에 따르면 이 구성은 GLM-5.2 753B build, 디스크 기준 약 222GB의 Unsloth dynamic IQ2_M quant, Thunderbolt 5로 연결한 두 대의 M5 Max에서 약 256GB pooled memory, 그리고 llama.cpp RPC를 사용합니다. 결과는 단순한 throughput이 아닙니다. 모델이 Falcon 9 droneship landing simulator를 완전 offline으로 live-coding하고 있었다는 점이 핵심이라서, 이 사례는 로컬 배포와 privacy-first agent의 구체적 데모가 됩니다.

유형: 데모 | 날짜: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x DGX Spark Production Harness](https://x.com/thatcofffeeguy/status/2074245620207058981) (작성자 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**이 사례는 5노드 DGX Spark 구성이 production GLM-5.2 작업에 충분한지 판단할 때 유용합니다. thatcofffeeguy가 400K context에서 단일 스트림 약 13.9 tok/s와 3개 lane 합산 19.9 tok/s를 live harness에서 보고했기 때문입니다.**

게시물은 여러 실험 끝에 이 구성이 가장 잘 나왔고 pruning 없이 같은 날 production에 올렸다고 말합니다. workload도 단순한 실험실 테스트보다 구체적입니다. 이 harness는 이미 약 30분 안에 content를 만들고 일일 ERP 데이터를 검토하는 데 쓰이고 있었다고 하므로, 단순한 하드웨어 자랑이 아니라 실전 배포 체크포인트로 볼 수 있습니다.

유형: 데모 | 날짜: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [M3 Ultra ds4-eval Q4 Checkpoint](https://x.com/ivanfioravanti/status/2073742792044446194) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**이 사례는 Apple Silicon 단일 박스 GLM-5.2 구성을 ds4-eval로 benchmark할 때 유용합니다. ivanfioravanti가 M3 Ultra 512GB 머신에서 q4 실행 약 16 tok/s, 92개 중 76개 통과, 총 8시간 53분을 보고했기 때문입니다.**

ivanfioravanti에 따르면 이 q4 ds4-eval 실행은 M3 Ultra 512GB 머신에서 수행되었고, 예전 branch도 batch inference로 다시 시험할 예정입니다. 그래서 이 thread는 기존의 영상 중심 M3 사례를 보완하는 더 강한 근거가 되며, 단순한 throughput clip이 아니라 통과 수와 실행 시간이 함께 들어 있습니다.

유형: 평가 | 날짜: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [4x RTX PRO 6000 Build Guide](https://x.com/QingQ77/status/2073589933567094981) (작성자 [@QingQ77](https://x.com/QingQ77))

**이 사례는 진지한 로컬 GLM-5.2-594B 구축 범위를 잡을 때 유용합니다. QingQ77가 4장의 RTX PRO 6000, opencode로 노출한 API, 그리고 agent 작업용 sandbox VM을 중심으로 한 전체 하드웨어 및 운영 가이드를 공유했기 때문입니다.**

guide는 GLM-5.2-594B를 위해 4장의 RTX PRO 6000과 384GB VRAM을 쓰는 상위 예산 경로와 중고 EPYC, DDR4 부품을 설명합니다. 또 PCIe Gen4 switching, BIOS bifurcation과 ASPM, iommu=off, 110V 회로에서의 350W 제한, opencode를 통한 Docker container, host를 보호하는 sandbox VM까지 다룹니다.

유형: 튜토리얼 | 날짜: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [4x DGX Spark QuantTrio Run](https://x.com/Tech2Wild/status/2073637530960826787) (작성자 [@Tech2Wild](https://x.com/Tech2Wild))

**이 사례는 4노드 DGX Spark 클러스터에서 GLM-5.2 QuantTrio가 어느 정도까지 나오는지 추정할 때 유용합니다. Tech2Wild가 200K context와 함께 단일 스트림 30 tok/s, 6동시 요청에서 총 60.5 tok/s를 보고했기 때문입니다.**

Tech2Wild에 따르면 최종 측정 런은 256 experts를 모두 유지한 채 k=4의 MTP speculative decoding을 사용했습니다. 이전의 Spark 계획형 thread와 달리 이것은 완료된 local inference 결과로, 단일 스트림 30 tok/s, 6개 동시 요청에서 총 60.5 tok/s, 그리고 200K context를 목표로 한 구성입니다.

유형: 데모 | 날짜: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [Single M3 Ultra 4-Bit Video Run](https://x.com/ivanfioravanti/status/2073502277449486460) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**이 사례는 Apple Silicon 단일 머신에서 GLM-5.2가 어느 정도 실용적인지 가늠할 때 유용합니다. ivanfioravanti는 M3 Ultra 512GB 한 대에서 4-bit 실행이 약 16 tok/s로 도는 모습을 보여주고, q2 ds4-eval 영상이 약 17 tok/s라는 점과 비교합니다.**

ivanfioravanti는 단일 M3 Ultra 512GB 머신에서 GLM 5.2 4-bit가 초당 약 16토큰으로 도는 영상을 올렸고, ds4-eval 영상은 q2 build로 약 17 tokens per second라고 덧붙였습니다. 아직 진행 중인 local test라고 선을 긋지만, 기존의 multi-M3 및 oMLX 관련 사례와 함께 볼 수 있는 Apple Silicon 단일 박스 처리량 체크포인트로는 충분히 구체적입니다.

유형: 데모 | 날짜: 2026-07-04

<a id="case-173"></a>
### Case 173: [AMD MI355X 2626 Tok/s Node Serve](https://x.com/wafer_ai/status/2073155792182907085) (작성자 [@wafer_ai](https://x.com/wafer_ai))

**이 사례는 AMD 하드웨어에서 고처리량 GLM-5.2 추론을 가늠할 때 유용합니다. wafer_ai에 따르면 MI355X는 노드당 2626 tok/s, single-stream에서 213 tok/s에 도달했고, 비용은 Blackwell보다 2배 이상 낮았습니다.**

wafer_ai는 엔지니어들이 AMD MI355X에서 GLM 5.2를 서빙해 노드당 초당 2626토큰, single-stream 모드에서 초당 213토큰을 기록했다고 말합니다. 게시물은 이를 B200 처리량의 약 80 percent를 2배 이상 낮은 비용으로 달성한 것으로 설명하며, NVIDIA 단일 스택을 넘어 open-weight 추론 경제성을 검토하는 팀에게 구체적인 deployment reference가 됩니다.

유형: 데모 | 날짜: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel Gateway 287 Tok/s Serverless](https://x.com/wafer_ai/status/2072861749104288074) (작성자 [@wafer_ai](https://x.com/wafer_ai))

**이 사례는 serverless gateway를 거칠 때 사용자가 체감할 GLM-5.2 지연 특성을 추정하는 데 유용합니다. wafer_ai는 GLM 5.2 Fast 경로가 benchmark harness가 아니라 Vercel AI Gateway에서 287 tokens per second를 기록했다고 말합니다.**

wafer_ai는 자사의 GLM 5.2 Fast 경로가 Vercel AI Gateway에서 초당 287토큰에 도달했고, 이것이 serverless 구성에서 최종 사용자가 실제로 보게 될 숫자라고 설명합니다. raw 추론 benchmark와 gateway overhead가 포함된 production형 hosted access 사이를 연결해 주는 실용적인 지표입니다.

유형: 데모 | 날짜: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [One-Click RTX PRO 6000 Deployment](https://x.com/XciD_/status/2073035324272328733) (작성자 [@XciD_](https://x.com/XciD_))

**이 사례는 격리된 hosted GLM-5.2 배포의 최소 비용 감각을 잡는 데 유용합니다. XciD_에 따르면 GLM-5.2-NVFP4는 8x RTX PRO 6000 기반 Inference Endpoints에서 시간당 22달러로 one-click 배포가 가능합니다.**

XciD_는 753B MoE 변형인 GLM-5.2-NVFP4가 전용 8x RTX PRO 6000 인스턴스를 사용하는 Inference Endpoints에서 one-click deployment로 제공된다고 말합니다. 예측 가능한 시간당 22달러 비용, zero setup, full isolation을 강조하므로 스택을 직접 운영하고 싶지 않은 팀에 구체적인 hosted deployment reference가 됩니다.

유형: 통합 | 날짜: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [Full 744B On 5x ASUS GX10s](https://x.com/thatcofffeeguy/status/2072525885077434743) (작성자 [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**이 사례는 극단적인 home-lab GLM-5.2 배치를 가늠할 때 유용합니다. 작성자에 따르면 744B 풀 모델이 5대의 ASUS GX10 박스에서 full context로 돌고 있고, 실제 workload용 causal harness에도 이미 연결돼 있습니다.**

thatcofffeeguy는 744B 전체 GLM-5.2가 다섯 대의 ASUS GX10 시스템에서 full context와 함께 실행되고 있으며, token rate도 예상보다 좋고 stack도 이미 causal harness에 연결됐다고 말합니다. 정확한 throughput 수치는 아직 없지만, 이런 규모의 local cluster가 축소판이 아니라 full model을 올릴 수 있다는 구체적인 공개 증거입니다.

유형: 데모 | 날짜: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Agent Route Swap In China Stack](https://x.com/0xluffy_eth/status/2072548580183900430) (작성자 [@0xluffy_eth](https://x.com/0xluffy_eth))

**이 사례는 최고 품질보다 비용 압박이 더 중요한 상황에서 mixed-model stack의 agent layer로 GLM-5.2를 라우팅할 때 참고가 됩니다. 작성자에 따르면 Sonnet을 GLM-5.2로 바꾸자 해당 slot의 input cost가 5배 줄고 품질 저하는 약 3 percent였습니다.**

이 thread는 reasoning, code generation, agent calls, batch work, image, video에 걸친 6개 routing 변경을 보여줍니다. agent layer에서는 Sonnet을 GLM 5.2로 교체했고, 성능 저하는 약 3 percent, input cost는 5배 저렴했다고 합니다. 30일 요약에서는 총 AI 운영비가 87 percent 줄고 revenue는 변하지 않았다고 말합니다.

유형: 평가 | 날짜: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B Local Hardware Floor](https://x.com/devjuninho/status/2072151237840007399) (작성자 [@devjuninho](https://x.com/devjuninho))

**이 사례를 쓰면 GLM-5.2 로컬 운용 계획을 현실적으로 잡을 수 있습니다. 출처에 따르면 양자화 버전도 2비트 약 239GB, 4비트 약 466GB 수준이라서 RAM이나 VRAM 256GB 이상이 사실상 바닥선이기 때문입니다.**

devjuninho는 open weights라고 해서 자동으로 소비자용 로컬 실행이 쉬운 것은 아니라고 반박합니다. 스레드는 GLM-5.2가 대략 744B 파라미터에 활성 파라미터는 약 40B이며, 2비트 약 239GB, 4비트 약 466GB로 추정합니다. 그리고 의미 있는 로컬 실행에는 일반 게이밍 PC가 아니라 서버급 메모리와 SSD 여유, 그리고 인내가 필요하다고 말합니다.

유형: 제한 | 날짜: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Local NVFP4 Rust Port At 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (작성자 [@mov_axbx](https://x.com/mov_axbx))

**튜닝된 로컬 GLM-5.2 배포가 실제 coding 작업에서 어디까지 가능한지 가늠하고 싶다면 이 사례가 유용합니다. 작성자는 NVFP4에서 140 tok/s와 Python에서 Rust로의 전체 포팅을 몇 분 만에 끝냈다고 보고합니다.**

mov_axbx는 OMP 기반 로컬 GLM-5.2 NVFP4 설정이 초당 약 140 token에 도달했다고 보고합니다. 같은 게시물에서 Python 위성 위치 서비스의 Rust 포팅을 약 10분 만에 마치고, 곧바로 데모 웹앱까지 만들었다고 말합니다.

유형: 평가 | 날짜: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 에이전트 주도 듀얼 스택 Bring-Up](https://x.com/TheValueist/status/2071261052080148607) (작성자 [@TheValueist](https://x.com/TheValueist))

**thread는 분석가들이 베어메탈 B300 두 장에서 vLLM과 SGLang 양쪽으로 NVFP4 추론을 하루도 안 돼 세웠다고 보여 주므로, 본격적인 셀프호스트 GLM-5.2 배포 범위를 가늠하려면 이 사례를 사용하십시오.**

TheValueist는 analyst-agent workflow가 베어메탈 NVIDIA B300 x2 클러스터에서 GLM 5.2 NVFP4를 vLLM과 SGLang 양쪽에 배포한 뒤, 각 스택에서 전체 benchmark suite를 24시간도 안 돼 돌렸다고 말합니다. thread는 병목이 순수 compute보다 HBM 용량이었고, KV cache가 spill되면 DRAM도 중요해진다고 덧붙입니다. 로컬 추론 경제성과 하드웨어 병목을 검토하는 팀에게 구체적인 운영 메모가 됩니다.

유형: 평가 | 날짜: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 Ultra Prefill 속도 향상](https://x.com/jundotkim/status/2071287585297887510) (작성자 [@jundotkim](https://x.com/jundotkim))

**최근 커널 작업 이후 Apple Silicon 로컬 실행 가능성을 다시 확인하려면 이 사례를 사용하십시오. 보고된 M3 Ultra 512GB의 GLM-5.2 prefill 속도는 간단한 테스트에서 뚜렷한 품질 붕괴 없이 거의 두 배가 됐습니다.**

jundotkim은 oMLX 0.4.5.dev1에 들어간 custom MLX kernels 덕분에 M3 Ultra 512GB 머신에서 GLM-5.2-oQ4 32k prefill이 87.7 tok/s에서 174.4 tok/s로 올라 98.9% 상승했다고 말합니다. 같은 게시물은 이 경로가 아직 experimental이지만 needle-in-a-haystack 점검과 Claude Code 스타일 coding test에서는 눈에 띄는 회귀가 없었다고 설명합니다. 단순 release note가 아니라 실용적인 로컬 추론 업데이트입니다.

유형: 평가 | 날짜: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [가입 시 2천만 토큰 크레딧 버스트](https://x.com/Bitbro4crypto/status/2071150218872283262) (작성자 [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**직접 가입 크레딧만으로도 실제 GLM-5.2 체험이 가능한지 평가하려면 이 사례를 사용하십시오. 게시물은 신규 계정에 카드 없이 2천만 무료 토큰과 완전한 OpenAI 호환 접근이 제공된다고 주장합니다.**

Bitbro4crypto는 현재 GLM 5.2 가입 경로에서 2천만 무료 tokens, 이미지와 비디오 크레딧 120개, high와 max thinking modes, 1M context window, 그리고 Cursor나 Claude Code 같은 도구에 그대로 꽂아 쓸 수 있는 OpenAI 호환 API가 제공된다고 말합니다. 단기 테스트를 위한 구체적인 접근 및 가격 신호로 볼 수 있지만, 프로모션 quota는 바뀔 수 있다고 가정해야 합니다.

유형: 통합 | 날짜: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark 로컬 GLM 운영 가이드](https://x.com/TraffAlex/status/2071020631072616698) (작성자 [@TraffAlex](https://x.com/TraffAlex))

**DGX Spark 클러스터가 현실적인 로컬 GLM-5.2 경로인지 가늠하려 할 때 쓰는 사례입니다. 모아둔 가이드는 구체적 하드웨어 비용, 클러스터 토폴로지, vLLM 명령을 1M context GLM 목표와 연결합니다.**

TraffAlex는 커뮤니티 검증 내용과 NVIDIA 공식 자료를 모아 각 유닛 가격이 4,699달러이고, 다른 모델에는 2x Spark 클러스터가 sweet spot이며, 4x Sparks로는 GLM 5.2 NVFP4를 1M-token context에서 초당 약 20 tokens로 돌릴 수 있다고 설명합니다. 같은 게시물에는 CX7 네트워킹 설정, passwordless SSH, NCCL 점검, 예시 vLLM Docker 명령도 포함되어 있어, 단순한 하드웨어 의견이 아니라 실전 로컬 deployment playbook 역할을 합니다.

유형: 튜토리얼 | 날짜: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (작성자 [@Hesamation](https://x.com/Hesamation))

**이 사례를 사용하여 GLM-5.2 출력 토큰 경제성을 Opus, Fable 및 GPT-5.5 스타일 모델과 비교합니다.**

이 게시물은 1M 출력 토큰 가격을 비교하고 GLM-5.2가 프론티어 폐쇄형 모델보다 의미 있게 저렴할 수 있다고 주장합니다. 이 수치를 예산 책정 전에 다시 확인해야 하는 소스 연결 가격 비교로 간주하세요.

유형: 평가 | 날짜: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (작성자 [@Jeyffre](https://x.com/Jeyffre))

**이 사례를 사용하여 자체 호스팅 GLM-5.2 유사 모델이 헤비 에이전트 사용자의 하드웨어 비용을 상환할 수 있는지 여부를 추론합니다.**

저자는 여러 DGX Spark급 시스템이 700B급 모델을 실행할 수 있을 것으로 추정하고 약 20,000달러의 하드웨어 구입 비용과 코딩 및 에이전트 워크로드에 대한 높은 월별 API 지출을 비교합니다.

유형: 평가 | 날짜: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (작성자 [@pcuenq](https://x.com/pcuenq))

**이 사례를 사용하여 Apple 하드웨어 및 MLX 지향 설정에서 실행되는 로컬 GLM-5.2를 살펴보세요.**

이 게시물에서는 GLM-5.2가 방금 출시되었으며 이미 두 대의 Mac Studio M3 Ultra 시스템에서 MLX와 함께 실행 중이라고 밝혔으며, 이는 개방형 무게를 갖춘 최근 폐쇄형 모델과 비교할 수 있는 것으로 구성되었습니다.

유형: 데모 | 날짜: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (작성자 [@ai_xiaomu](https://x.com/ai_xiaomu))

**구독과 자체 호스팅 중에서 선택하기 전에 로컬 배포 가정을 확인하기 위한 비용 비교 프롬프트로 이 사례를 사용하세요.**

중국 게시물은 Claude Pro 구독과 비교하여 주장된 SWE-Bench 수치, 상업용 오픈 소스 사용 및 예상 단일 H100 로컬 배포 비용을 비교합니다. 현재 인프라 가격에 맞게 수치를 재검증해야 합니다.

유형: 평가 | 날짜: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (작성자 [@RoundtableSpace](https://x.com/RoundtableSpace))

**이 사례를 사용하여 GLM-5.2에 대한 무료 크레딧 및 교체 에이전트 설명을 검사하는 동시에 마케팅 주장과 검증된 워크로드 적합성을 분리합니다.**

게시물에서는 GLM-5.2를 일일 크레딧, 오픈 소스 제어, 자체 호스팅 및 긴 코딩 세션에 대한 더 강력한 가치를 갖춘 저렴한 Claude 경쟁자로 구성합니다.

유형: 평가 | 날짜: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (작성자 [@0xSero](https://x.com/0xSero))

**유료 공급자 또는 로컬 배포를 시작하기 전에 무료 ZCode 허용을 통해 GLM-5.2를 테스트하려면 이 사례를 사용하십시오.**

저자는 ZCode를 통한 GLM-5.2 가용성에 대해 설명하고 일일 무료 토큰 허용량이 많으며 vLLM Studio 또는 로컬 호스팅 설정에 사용할 수 있는 방법에 대해 설명합니다.

유형: 통합 | 날짜: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (작성자 [@JZiyue_](https://x.com/JZiyue_))

**GLM-5.2 테스트를 위해 시간 제한이 있는 무료 액세스 창을 찾으려면 이 사례를 사용하십시오.**

이 게시물은 1주일 무료 기간, 1M 컨텍스트, 코딩 및 에이전트 개선, 5.1과 동일한 가격 포지셔닝을 통해 ZenMux에서 실시간으로 GLM-5.2를 광고합니다.

유형: 통합 | 날짜: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAI 토큰별 가격](https://x.com/nahcrof/status/2067166596523765781) (작성자 [@nahcrof](https://x.com/nahcrof))

**경로를 선택하기 전에 이 사례를 사용하여 GLM-5.2에 대한 타사 공급자 가격을 비교하세요.**

이 게시물은 입력, 출력 및 캐시 가격이 나열된 crofAI의 GLM-5.2를 발표하여 이를 저렴한 프론티어 인텔리전스로 포지셔닝합니다.

유형: 통합 | 날짜: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (작성자 [@scaling01](https://x.com/scaling01))

**GLM-5.2를 다른 개척 연구실 및 개방형 모델과 비교할 때 이 사례를 시장 가격 비평으로 사용하십시오.**

저자는 출력 토큰 가격 책정에 대해 GLM-5.2와 기타 대규모 개방형 모델을 비교하고 이 비교를 사용하여 일부 프론티어 랩 API 마진이 높다고 주장합니다.

유형: 평가 | 날짜: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (작성자 [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**오프라인 코딩 설정을 계획하기 전에 이 사례를 사용하여 대용량 메모리 Apple 하드웨어에서 로컬 GLM-5.2 추론 처리량을 추정하세요.**

소스는 로컬 대용량 Mac 설정에서 초당 44.1개의 토큰을 보고하고 과도한 도구 호출로 인한 디코드 반복 문제를 언급합니다.

유형: 데모 | 날짜: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (작성자 [@mrblock](https://x.com/mrblock))

**전체 모델 가중치가 일반 로컬 하드웨어에 비해 너무 큰 경우 이 사례를 사용하여 양자화된 GLM-5.2 배포 경로를 평가합니다.**

이 게시물에서는 Unsloth 동적 2비트 및 1비트 GGUF 옵션, 메모리 감소, llama.cpp 또는 Unsloth Studio 배포 경로에 대해 설명합니다.

유형: 튜토리얼 | 날짜: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**더 큰 Apple Silicon 구성을 짜기 전에, 두 대의 M3 Ultra에 분산 MLX로 올린 GLM-5.2 8-bit serving 모습을 가늠하기 위한 사례입니다.**

게시물은 두 대의 M3 Ultra 512GB 머신에 걸친 MLX distributed 실행에서 GLM-5.2 8-bit가 약 17.9 tokens/sec, 총 약 760GB 메모리로 동작한다고 보여 줍니다. 작성자는 아직 work-in-progress PR이라고도 밝혀, 완성된 가이드라기보다 deployment signal로 보는 편이 적절합니다.

유형: 데모 | 날짜: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (작성자 [@buildwithhassan](https://x.com/buildwithhassan))

**peak / off-peak multiplier 인하 기간을 활용해 GLM-5.2 plan credits를 더 오래 쓰기 위한 사례입니다.**

이 게시물은 ZCode가 GLM coding plan multiplier를 peak 시간에는 3x에서 2x로, off-peak에는 2x에서 0.67x로 낮췄고, 그 창이 9월 말까지 이어진다고 말합니다. GLM-5.2 credits를 오래 끌고 가려는 사람에게 구체적인 access / pricing note가 됩니다.

유형: 통합 | 날짜: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (작성자 [@CardilloSamuel](https://x.com/CardilloSamuel))

**고급 로컬 GLM-5.2 워크스테이션 규모를 가늠하려면 이 사례를 사용하십시오. Blackwell 두 장을 쓴 데스크톱이 4-bit 양자화 빌드에서 두 자릿수 디코드 속도를 유지했습니다.**

CardilloSamuel은 GLM-5.2 UD-Q4_K_XL을 2x RTX PRO 6000 Blackwell, Threadripper PRO 9995WX, 1TB DDR5 조합에서 실행했다고 보고합니다. 게시물은 prefill 약 64 tok/s, decode 13-15 tok/s, BF16과 2점 이내 차이인 69.7% Aider Polyglot 점수를 언급하며, 병목은 시스템 RAM 대역폭이었고 구성에 맞지 않는 5090은 분할 구성에서 제외했다고 덧붙입니다.

유형: 데모 | 날짜: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (작성자 [@karminski3](https://x.com/karminski3))

**로컬 GLM-5.2 추론용 Mac Studio 구매가 합리적인지 점검하려면 이 사례를 사용하십시오. 게시된 회수 계산은 대부분의 사용자에게 API나 플랜 접근이 더 유리하다는 쪽에 무게를 둡니다.**

이 게시물은 32,999 RMB의 Mac Studio가 제시된 가격 기준으로 대략 11억 7,800만 GLM-5.2 API 토큰과 맞먹는다고 추산합니다. 더 작은 Qwen 구성조차 투자 회수 기간이 약 209일이라고 주장합니다. 이어서 512GB Mac Studio에서 양자화된 GLM-5.2를 약 17 tok/s로 돌려도 손익분기까지 약 7년이 걸릴 수 있으므로, 이미 하드웨어를 갖고 있거나 유휴 시간을 활용할 수 있을 때만 로컬 보유가 의미 있다고 말합니다.

유형: 평가 | 날짜: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM Local Outage Save](https://x.com/CardilloSamuel/status/2069431311463236078) (작성자 [@CardilloSamuel](https://x.com/CardilloSamuel))

**호스팅 frontier API가 다운되거나 한도에 걸려도 LiteLLM을 통해 로컬 GLM-5.2로 우회해 납기 작업을 계속하려면 이 사례를 사용하십시오.**

CardilloSamuel은 친구가 토큰을 다 쓰고 Claude 장애까지 겪자, 자신의 로컬 GLM-5.2 배포를 가리키는 LiteLLM API key를 발급했다고 말합니다. 그 친구는 약 500만 tokens를 0달러로 생성해 속도 저하를 감수하면서도 납기를 맞췄다고 합니다.

유형: 데모 | 날짜: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [Individual Versus Team Local ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (작성자 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**로컬 GLM-5.2 배포가 개인에게 맞는지, 더 큰 개발팀에 더 적합한지 판단하려면 이 사례를 사용하십시오.**

이 게시물은 개인용 로컬 구성에 512GB 시스템 메모리, 여러 GPU, 강력한 CPU가 필요하고, 그래도 속도는 초당 6-10 tokens 수준일 수 있다고 주장합니다. 반면 프라이버시, 무제한 토큰, 주간 캡 부재, 제공업체 장애나 정책 변화로부터의 독립성을 중시하는 10명 이상 개발팀이라면 공유 사내 서버가 더 합리적이라고 말합니다.

유형: 평가 | 날짜: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 실행](https://x.com/0xSero/status/2069871347010838586) (작성자 [@0xSero](https://x.com/0xSero))

**고성능 워크스테이션을 들이기 전에 4 GPU 로컬 GLM-5.2 구성을 까다로운 terminal benchmark에 맞춰 가늠하려면 이 사례를 사용하십시오.**

0xSero는 GLM-5.2-REAP-NVFP4가 Terminal Bench 2.0에서 69.1%를 기록했고, 4x RTX PRO 6000에 들어가는 모델들 가운데 최고 terminal-bench 결과라고 말합니다. 양자화된 open-weight 구성을 hosted frontier terminal과 비교하려는 팀에게 구체적인 로컬 배포 신호가 됩니다.

유형: 평가 | 날짜: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell 로컬 Crackme 풀이](https://x.com/CardilloSamuel/status/2069887782508753302) (작성자 [@CardilloSamuel](https://x.com/CardilloSamuel))

**디버거 없이도 본격적인 로컬 GLM-5.2 구성이 장시간 리버스엔지니어링 과제를 끝낼 수 있는지 판단하려면 이 사례를 사용하십시오.**

CardilloSamuel은 약 300GB RAM을 갖춘 2x RTX PRO 6000 Blackwell 위의 로컬 GLM 5.2가 OpenCode를 통해 crackme challenge를 78분, 초당 약 14 tokens 속도로 풀었다고 말합니다. 게시물은 하네스에 디버거나 MCP 접근이 없었는데도 모델이 메모리 주소를 덤프하고, 가설을 시험하고, 바이너리를 패치하지 않은 채 지시를 따라갔다고 강조합니다.

유형: 데모 | 날짜: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 한계, 주의점, 안전 신호
<a id="case-205"></a>
### Case 205: [Static HTML Rewrite Executor Misses](https://x.com/petruknisme/status/2075092910182387759) (작성자 [@petruknisme](https://x.com/petruknisme))

**이 사례는 1:1 legacy rewrite를 GLM-5.2에게 executor로 통째로 맡기지 않기 위해 유용합니다. 큰 static HTML을 React와 Vite로 옮기는 작업에서 OpenCode Go와 Cline을 써도 디테일이 많이 빠졌고, 작성자가 GLM을 executor보다 planner 쪽으로 보게 됐기 때문입니다.**

작성자는 큰 static HTML 프로젝트를 React와 Vite로 다시 쓰는 작업을 GLM-5.2로 진행했지만, 이미 OpenCode Go와 Cline 사용량을 꽤 태운 뒤에도 1:1 이행에 필요한 디테일이 많이 빠졌다고 설명합니다. 충실도가 중요한 legacy migration에서는 GLM을 planning loop에 남기되 execution review를 훨씬 더 엄격하게 해야 한다는 실무적인 시사점입니다.

유형: 한계 | 날짜: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Composio 47-Task Agent Gaps](https://x.com/composio/status/2074908761970393265) (작성자 [@composio](https://x.com/composio))

**이 사례는 GLM-5.2가 실제 SaaS-agent 작업에서 어디서 아직 무너지는지 이해할 때 유용합니다. Composio가 17개 도구와 47개 작업에 연결해 45개는 통과했지만, 완전성 점검과 모호한 SLA 판단에서 실패했기 때문입니다.**

Composio에 따르면 GLM-5.2와 Fable 5는 GitHub, LaunchDarkly, Zendesk를 포함한 17개의 실제 SaaS 제품에 에이전트로 연결되었습니다. GLM-5.2는 47개 중 45개를 해결했고 Fable 5는 47개 중 47개를 해결했습니다. trace review는 두 가지 구체적 실패 모드를 지적했는데, 130개의 예상 결과가 있던 GitHub secret audit에서 너무 일찍 멈춘 점과, 출력 형식은 그럴듯했지만 Zendesk SLA breach를 잘못 분류한 점입니다.

유형: 평가 | 날짜: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [Preliminary Cyber Research Parity](https://x.com/Irregular/status/2072682835798831168) (작성자 [@Irregular](https://x.com/Irregular))

**이 사례는 vulnerability research 하위 작업에서 GLM-5.2를 가늠할 때 유용합니다. Irregular는 좁은 cyber suite에서 GPT-5.4와 Opus 4.6에 필적하는 초기 내부 평가를 보고하면서도, end-to-end attack scenario는 아직 검증되지 않았다고 명시합니다.**

Irregular는 제한된 내부 vulnerability research task suite에서 테스트한 부분에 한해 GLM-5.2가 GPT-5.4와 Claude Opus 4.6에 대체로 비슷했다고 말합니다. 같은 게시물은 suite가 좁고 CyScenarioBench나 FrontierCyber 같은 scenario-level benchmark는 아직 돌리지 않았다고 덧붙입니다. 완전한 offensive-agent parity 증거가 아니라 초기 cyber capability 신호로 보는 편이 맞습니다.

유형: 제약 | 날짜: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter Spend-Cut Skill Rewrite](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (작성자 [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**이 사례는 에이전트 모델을 바꾸기 전에 마이그레이션 비용을 잡을 때 유용합니다. 한 펀드의 OpenRouter 시험에서 GLM-5.2는 Opus 비용의 약 8분의 1 수준이었지만, 스킬 재작성과 라우팅 로직, 그리고 더 느리고 약한 출력을 감수해야 했습니다.**

Rahul J Mathur에 따르면 그의 팀 에이전트는 이전까지 연간 약 10만 달러 수준으로 Opus 모델만 써 왔고, 6월에는 지출을 약 40퍼센트 줄이기 위해 OpenRouter 멀티모델 시험을 시작했습니다. 직접 기록한 관찰에서는 GLM-5.2가 Opus 4.8보다 느리고 edge case나 skill file 전체 읽기에서 더 자주 놓쳤지만, 수신자 기준 출력 품질은 비용이 약 8분의 1이어도 여전히 수용 가능했습니다. 같은 스레드는 Opus나 GPT 지향 skill이 깔끔하게 옮겨지지 않으며, 마이그레이션에는 업데이트된 skill과 새로운 사용 습관, 하드코딩된 routing 로직이 필요하다고 경고합니다.

유형: 제한 | 날짜: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA Verbosity And Reasoning Tradeoff](https://x.com/ArtificialAnlys/status/2072022576394821859) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**GLM-5.2의 frontier급 open-weight 성능과 reasoning 효율 비용을 분리해서 보고 싶다면 이 사례가 유용합니다. Artificial Analysis가 open-weight 1위를 인정하면서도 출력 token 소모가 비정상적으로 크다고 보여주기 때문입니다.**

Artificial Analysis는 GLM-5.2 Max가 Intelligence Index를 돌리는 데 약 1억 4100만 개의 출력 token을 사용했고 그중 95%가 reasoning token이었다고 말합니다. 이는 Opus 4.8의 1억 1700만, GPT-5.5의 7200만보다 많지만, 동시에 GLM-5.2를 최고 open-weight로 유지합니다.

유형: 평가 | 날짜: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR 좁은 승리 주의점](https://x.com/leploutos/status/2071121981551047039) (작성자 [@leploutos](https://x.com/leploutos))

**출처는 GLM-5.2가 하나의 IDOR benchmark에서 Claude Code를 이겼다고 말하지만 Mythos 자체와의 비교는 아니라고 하므로, 실제 보안 신호와 과장된 헤드라인을 분리하려면 이 사례를 사용하십시오.**

leploutos는 바이럴하게 퍼진 "GLM equals Mythos" 해석이 틀렸다고 말합니다. Semgrep 결과는 단일 IDOR 탐지 benchmark에서 GLM-5.2가 F1 39%로 Claude Code 구성의 28-37%를 앞섰고, 버그당 약 0.17달러, frontier model 비용의 약 6분의 1 수준이었다는 내용입니다. 같은 게시물은 실무자가 봐야 할 한계도 함께 지적합니다. 한 가지 bug class, 하나의 dataset, 단일 run, vendor 소유 benchmark였으므로, Anthropic의 전용 cyber model과 동급이라는 증거가 아니라 좁지만 실제적인 vulnerability-detection signal로 다뤄야 합니다.

유형: 한계 | 날짜: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 추론 효율 격차](https://x.com/scaling01/status/2070961852008509918) (작성자 [@scaling01](https://x.com/scaling01))

**reasoning 비중이 큰 workload에서 GLM-5.2를 확인하려 할 때 쓰는 사례입니다. 게시된 LisanBench 결과는 GLM-5보다 낫지만 다른 오픈 모델과 비교하면 아직 비효율적이라는 점을 보여줍니다.**

scaling01은 LisanBench에서 GLM-5.2-high가 점수 1834로 29위, GLM-5는 986.83이었다고 보고합니다. 같은 게시물은 Kimi-K2.5 Thinking이 평균 약 19K tokens로 비슷한 점수에 도달하는 반면, GLM-5.2는 약 32K tokens를 사용한다고 말하며, 이전 GLM 세대보다 개선되었지만 reasoning efficiency에서는 여전히 상대적으로 약하다고 정리합니다.

유형: 한계 | 날짜: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench 도메인 불일치 주의점](https://x.com/yuhasbeentaken/status/2070928066797351300) (작성자 [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**게시물은 약한 PrinzBench 점수와 훨씬 강한 software·tool-use benchmark를 대비하므로, GLM-5.2를 법률 리서치보다 coding과 agent execution에 집중시키려 할 때 쓰는 사례입니다.**

yuhasbeentaken은 GLM-5.2가 법률 리서치와 어려운 web search에 초점을 둔 좁은 benchmark인 PrinzBench에서 30/99에 그친 반면, SWE-Bench Pro 62.1, Terminal-Bench 2.1 81.0, MCP-Atlas 77.0, ProgramBench 63.7 등에서는 더 강한 공개 성적을 보였다고 말합니다. 게시물은 이 격차를 모순이 아니라 domain fit 문제로 해석하며, 법률 리서치에는 더 강한 proprietary model을, coding과 agentic execution에는 GLM-5.2를 권합니다.

유형: 한계 | 날짜: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (작성자 [@sawyerhood](https://x.com/sawyerhood))

**이 사례를 사용하여 GLM-5.2는 기본 비전 기능이 필요한 작업 흐름에 덜 유용할 수 있다는 점을 기억하세요.**

저자는 Design Arena 순위 게시물을 인용하여 비전이 부족한 GLM 모델이 유용성을 감소시킨다고 지적합니다. 이는 다중 모드 제품 계획에 대한 실질적인 주의 사항입니다.

유형: 한계 | 날짜: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [실제 에이전트 격차 주의 사항](https://x.com/ml_angelopoulos/status/2067013545431269405) (작성자 [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**이 사례를 사용하면 GLM-5.2가 배포된 모든 에이전트 작업에서 최고의 독점 모델과 일치한다는 증거로 벤치마크 승리를 과도하게 읽는 것을 방지할 수 있습니다.**

저자는 GLM-5.2가 인상적이지만 Agent Arena 방법론을 기반으로 한 실제 에이전트 작업의 일반적인 분포에 대한 Fable 수준 또는 Opus 4.8 사고 수준 성능에 아직 근접하지 못했다고 말합니다.

유형: 한계 | 날짜: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (작성자 [@VittoStack](https://x.com/VittoStack))

**민감한 도메인에 GLM-5.2를 배포하기 전에 안전성 평가를 실행하라는 알림으로 이 사례를 사용하십시오.**

해당 게시물은 비교 안전성 테스트에서 유해 콘텐츠 거부 실패를 신고하고 있습니다. 저장소는 안전하지 않은 세부 정보가 아닌 안전 신호만 기록하며 이를 배포 위험 경고로 처리합니다.

유형: 한계 | 날짜: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [벤치마크 방법론 비평](https://x.com/josepha_mayo/status/2066951013337112661) (작성자 [@josepha_mayo](https://x.com/josepha_mayo))

**헤드라인 결과가 GLM-5.2를 선호하는 경우에도 이 사례를 사용하여 벤치마크 방법론에 의문을 제기합니다.**

저자는 GLM-5.2가 강력하다는 점을 인정하면서도 Design Arena 방법론을 비판하므로 리더보드 주장과 함께 벤치마크 회의론을 원하는 독자에게 유용합니다.

유형: 한계 | 날짜: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (작성자 [@k_matsumaru](https://x.com/k_matsumaru))

**코딩 계획을 전환하거나 Claude Code 스타일 워크플로를 GLM-5.2로 라우팅하기 전에 이 사례를 사용하여 공급자 대기 시간을 테스트하세요.**

일본 게시물에서는 코딩 계획 내에서 GLM-5.2 사용을 고려하고 있지만 피크 타임 응답 대기 시간에 대한 사전 우려를 언급했습니다.

유형: 한계 | 날짜: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (작성자 [@nikhilchandak29](https://x.com/nikhilchandak29))

**광범위한 배포 전에 코딩 이득이 비코딩 도메인에 일반화되는지 확인하려면 이 사례를 사용하십시오.**

이 게시물은 FutureSim에서 GLM-5.2가 GLM-5.1보다 나을 것이 없다고 보고하고 그 결과를 사용하여 코딩 개선 사항이 모든 도메인에서 동일하게 일반화되지 않을 수 있음을 경고합니다.

유형: 한계 | 날짜: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (작성자 [@bridgemindai](https://x.com/bridgemindai))

**이 사례를 사용하여 실행 실행, 문서화, API 준비와 모델 기능을 분리하세요.**

게시물에서는 당시 벤치마크와 API 액세스가 아직 제공되지 않았기 때문에 초기 릴리스가 지저분하다고 말하며 모델 품질 판단보다는 출시 준비 상태 검토와 관련이 있습니다.

유형: 한계 | 날짜: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [코딩플랜 가격 인상](https://x.com/bridgemindai/status/2065799843658793092) (작성자 [@bridgemindai](https://x.com/bridgemindai))

**GLM-5.2를 저렴한 대체품으로 추천하기 전에 이 사례를 사용하여 요금제 가격을 확인하세요.**

저자는 GLM Coding Pro 플랜에 대해 월 65달러를 지불하고 있으며 마지막 구독 이후 플랜이 거의 두 배로 늘어났다고 보고했습니다. 현재 가격을 확인하기 위한 알림으로 사용하세요.

유형: 한계 | 날짜: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [짧은 병렬 작업과 긴 에이전트 실행 비교](https://x.com/thekuchh/status/2068010332501479865) (작성자 [@thekuchh](https://x.com/thekuchh))

**이 사례를 사용하여 GLM-5.2를 짧은 제한 코딩 작업으로 라우팅하는 동시에 더 깊은 다중 시간 에이전트 실행을 위해 더 강력한 모델을 예약합니다.**

게시물에서는 실용적인 분할을 보고합니다. GLM-5.2는 짧은 병렬 작업에는 잘 작동하지만 더 긴 에이전트 실행에서는 드리프트됩니다.

유형: 한계 | 날짜: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [코드 검열과 편향 점검](https://x.com/wongmjane/status/2068424945663893936) (작성자 [@wongmjane](https://x.com/wongmjane))

**코드와 정치적 편향 테스트를 위한 실용적인 safety signal 로 보는 사례이며, 더 넓은 alignment 문제가 해결됐다는 증거로 봐서는 안 됩니다.**

작성자는 GLM-5.2가 코드 안에 중국 정치 검열을 삽입하지 않았고, 베트남전과 관련된 잘못된 US-bias claim 을 바로잡는 한편 의견에 가까운 사례는 그대로 두었다고 설명합니다. 따라서 정치적으로 민감한 코딩과 factuality 동작을 시험할 수 있는 구체적인 공개 사례가 됩니다.

유형: 한계 | 날짜: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [고난도 추론 과금 failure](https://x.com/s_batzoglou/status/2068297051247350154) (작성자 [@s_batzoglou](https://x.com/s_batzoglou))

**hard reasoning workload 에서 GLM-5.2를 신중히 테스트하기 위한 사례입니다. 공개 보고에는 긴 실행 시간, 낮은 완료율, 예상 밖으로 높은 과금 출력이 나타납니다.**

작성자는 11개의 induction problem 을 실행해 완료는 4개, 정답은 2개였고, 실행 시간은 수 시간에 달했으며, 청구 금액은 눈에 보이는 token count 보다 훨씬 높아 보였다고 보고합니다. 이는 단순 benchmark score 가 아니라 reasoning efficiency 와 billing behavior 에 대한 구체적인 경고입니다.

유형: 한계 | 날짜: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard Multiturn Hallucination Signal](https://x.com/dyfan22/status/2069335764295438532) (작성자 [@dyfan22](https://x.com/dyfan22))

**다른 벤치마크 성능을 신뢰하기 전에 환각에 민감한 멀티턴 작업에서 GLM-5.2를 검증하려면 이 사례를 사용하십시오.**

HalluHard는 최대 reasoning effort의 adaptive thinking 설정으로 GLM-5.2를 리더보드에 추가했습니다. 이 업데이트는 다른 벤치마크에서 강한 결과가 나와도 HalluHard의 어려운 멀티턴 벤치마크에서는 GLM-5.2가 여전히 자주 hallucinate한다고 말합니다.

유형: 한계 | 날짜: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Open-Weight Security Emergency Warning](https://x.com/joshua_saxe/status/2069289170107842572) (작성자 [@joshua_saxe](https://x.com/joshua_saxe))

**open-weight GLM-5.2가 offensive security agent의 운영 마찰을 낮춘다는 안전 계획 신호로 이 사례를 사용하십시오.**

Joshua Saxe는 GLM-5.2가 기존에 프런티어 코딩 에이전트를 쓰는 공격자들을 제약하던 모니터링과 계정 마찰의 상당 부분을 제거한다고 주장합니다. 이 스레드는 open weights와 private deployment의 조합을 공격 역량의 중대한 변화로 보며, API gatekeeping에 기대기보다 방어 측의 더 빠른 도입을 촉구합니다.

유형: 한계 | 날짜: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Rust 버그는 통과하지만 턴 수는 7배](https://x.com/BohuTANG/status/2069979942608425364) (작성자 [@BohuTANG](https://x.com/BohuTANG))

**GLM-5.2의 code quality 장점과 현재 agent harness overhead를 분리해서 보려면 이 사례를 사용하십시오. bug는 통과하지만 Opus보다 훨씬 많은 turns를 소모합니다.**

BohuTANG은 같은 Rust bug인 serde_json issue 979를 대상으로 evot, Claude Code, Pi 세 agent에서 GLM-5.2와 Opus 4.6을 비교했습니다. 여섯 세션 모두 pass였고, 작성자는 GLM의 bug 이해와 최종 code quality는 충분했다고 말합니다. 하지만 GLM은 38 / 43 / 61 turns가 필요했던 반면 Opus는 세 agent 전체에서 약 18 turns와 80초 정도로 끝났습니다. trace note는 이 차이를 cargo와 환경 처리 반복, 낮은 수렴성, 훨씬 긴 self-verification loop로 설명합니다.

유형: 평가 | 날짜: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust 모델 교체 비용 경고](https://x.com/ankrgyl/status/2069869387549446597) (작성자 [@ankrgyl](https://x.com/ankrgyl))

**실제 agentic coding workflow에서 더 싼 모델로 바꾸면 품질도 유지될 것이라고 쉽게 가정하지 않으려면 이 사례를 사용하십시오.**

ankrgyl은 Braintrust가 리포지토리 commit과 bug description에서 시작해 수정 결과를 평가하는 workflow에서 Opus 4.8과 GLM-5.2를 비교했다고 말합니다. 그 단순 교체 실험에서는 GLM-5.2가 비용은 비슷했지만 실행 시간은 더 길고 pass rate는 더 낮아, 전체적으로는 덜 효율적이었다고 보고합니다.

유형: 평가 | 날짜: 2026-06-24

---

<a id="acknowledge"></a>
## 🙏 감사의 글

이 저장소는 실제 GLM-5.2 사용 증거를 공유한 공개 제작자, 개발자, 벤치마크 팀, 제공자 및 커뮤니티로부터 영감을 받았습니다.

여기에 포함된 고신뢰 출처와 크리에이터에게 감사드립니다: [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan), [@ScaleAILabs](https://x.com/ScaleAILabs), [@wafer_ai](https://x.com/wafer_ai), [@ankrgyl](https://x.com/ankrgyl), [@clairevo](https://x.com/clairevo), [@MatinSenPai](https://x.com/MatinSenPai), [@hrdkbhatnagar](https://x.com/hrdkbhatnagar), [@nutlope](https://x.com/nutlope), [@victormustar](https://x.com/victormustar), [@digitalocean](https://x.com/digitalocean), [@BohuTANG](https://x.com/BohuTANG), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@denizirgin](https://x.com/denizirgin), [@Dracoshowumore](https://x.com/Dracoshowumore), [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar), [@OkhayIea](https://x.com/OkhayIea), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@0G_labs](https://x.com/0G_labs), [@SubhoGhosh02](https://x.com/SubhoGhosh02), [@undefinedKi](https://x.com/undefinedKi), [@alighodsi](https://x.com/alighodsi), [@composio](https://x.com/composio), [@pengsonal](https://x.com/pengsonal), [@EpochAIResearch](https://x.com/EpochAIResearch), [@stagedhappen](https://x.com/stagedhappen).

[@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), 최근 추가된 크리에이터: [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy).

*출처 표기에 수정이 필요하면 알려 주세요. 확인 후 업데이트하겠습니다.*

흥미로운 GLM-5.2 실사용 사례가 더 있다면 issue나 pull request로 공유해 주세요.

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
