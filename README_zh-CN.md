<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/en.jpg" alt="GLM-5.2 高信号使用案例仓库 banner" width="760"></a>

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

# GLM-5.2 高信号使用案例仓库

## 🍌 介绍

欢迎来到 GLM-5.2 高信号使用案例仓库。

**我们从公开 demo 和创作者社区整理 GLM-5.2 的真实使用案例、教程、集成、评测、价格信号和限制。**

这份简体中文 README 聚焦有具体工作流、公开 benchmark 证据、上手 demo、集成方式、成本信息或实践 caveat 的案例。

每个案例标题都会链接到公开来源，作者 handle 会链接到创作者主页。

[在 Evolink 上试用 GLM-5.2](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases&utm_content=introduction_cta)

## 📊 总览

- **258 个精选 GLM-5.2 案例**，来自公开创作者、评测团队、工具开发者、服务商和一线使用者。
- 覆盖基准与前沿评测、编码代理与长上下文工作流、上手演示与作品展示、供应商与工具集成、成本、定价与本地部署、限制、注意事项与安全信号。
- 每个案例都包含原始来源、创作者署名、简洁的使用结论、证据类型和发布日期。
- 你可以用这个 repo 查找实用工作流、比较优势和限制、发现供应商路径，并跟踪真实上手实验。

> [!NOTE]
> 本仓库重视具体证据，而不是 hype：已发布 demo、benchmark 方法、集成笔记、成本数据和明确 caveat。

> [!NOTE]
> 多语言 README 会保持与英文源相同的案例顺序、链接、anchor 和署名；为了可追溯性，部分标题会保留接近原文的写法。

<a id="quick-start"></a>
## ⚡ Quick Start

[在 EvoLink 打开 GLM-5.2](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=model_link).

通过 Evolink 的 OpenAI 兼容 Chat Completions API 使用 GLM-5.2。先在 [获取 API 密钥](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) 获取 API key，然后在执行请求前设置为 `EVOLINK_API_KEY`。

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

阅读完整 GLM-5.2 API 参考：[打开 GLM-5.2 API docs](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run).

## 📑 目录

| 章节 | 案例 |
|---|---|
| [📏 基准与前沿评测](#benchmarks-frontier-evaluation) | 案例 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207, 217, 223, 227, 235, 248, 250 |
| [💻 编码代理与长上下文工作流](#coding-agents-long-context-workflows) | 案例 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194, 210-212, 228, 236-237, 243, 255, 257 |
| [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds) | 案例 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202, 213, 218, 229 |
| [🔌 供应商与工具集成](#provider-tool-integrations) | 案例 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208, 214, 219-220, 224-225, 230-232, 238-239, 256, 258 |
| [💸 成本、定价与本地部署](#cost-pricing-local-deployment) | 案例 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209, 215, 221, 226, 233-234, 240-246, 249, 251, 253-254 |
| [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals) | 案例 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205, 216, 222, 247, 252 |
| [相关仓库](#related-repositories) | 已验证的 API 路径与相邻入口 |
| [🙏 致谢](#acknowledge) | 来源致谢与修正政策 |

### [📏 基准与前沿评测](#benchmarks-frontier-evaluation)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 250: ToolEval FP16 Indexer 提升](#case-250) | 如果你想 benchmark 经 fine-tune 的本地 GLM-5.2 tool use，而不是只看原始 API baseline，可以看这个案例，因为 volatilemarkts 说 753GB FP8 fine-tune 加上 custom FP16 indexer，让 SeraphimSerapis/tool-eval-bench 从标准 GLM 5.2 API 的 83 percent 提高到 94 percent。 | Evaluation |
| [Case 248: Aikido 26-CVE 测试框架基线](#case-248) | 如果你想在真实 code-audit harness 上 benchmark GLM-5.2，而不是只看 chat demo，可以看这个案例，因为 AikidoSecurity 说他们的 26 个已知 CVE AI Code Analysis benchmark 显示，GLM-5.2 在 pass@3 重新找出 16 个，切到 max reasoning 后又多出 3 个发现，成本只增加约 1.3x。 | Evaluation |
| [Case 235: DiligenceBench 金融评测排名](#case-235) | 如果你想评估 GLM-5.2 在公开股票研究 agent 上的表现，可以看这个案例，因为 karinanguyen 说 DiligenceBench 把 GLM 5.2 放在前列，并证明 finance harness 能让强模型同时更强且更便宜。 | Evaluation |
| [Case 227: Gargantua WebGL Raytracer 胜出](#case-227) | 如果你想在偏物理的单文件 browser build 上 benchmark GLM-5.2，可以看这个案例，因为 AlicanKiraz0 说 GLM 5.2 Max 在 Gargantua geodesic raytracer 任务里更好地兼顾了数值正确性与 real-time rendering discipline。 | Evaluation |
| [Case 223: 智能指数 Token 效率差距](#case-223) | 如果你想为长周期 benchmark 工作负载规划 GLM-5.2 预算，可以看这个案例，因为 Artificial Analysis 说，GLM-5.2 Max 在 Intelligence Index 每个任务上的平均输出 token 约为 43K，而 Inkling 是 25K，Kimi K2.6 和 DeepSeek v4 Pro Max 也都更低。 | Evaluation |
| [Case 217: EvalPlus 救援路由胜过 Fable](#case-217) | 如果你想测试一条带 verifier 的双模型 coding 路由，可以看这个案例，因为 gmi_cloud 说，先跑 Opus 4.8、失败时再用 GLM 5.2 FP8 救援的方案，在 100 个冻结 EvalPlus 任务里做对了 94 个，比 Fable 5 多 5 个，而且成本低约 47%。 | 评测 |
| [Case 207: 稳定流体浏览器基准](#case-207) | 如果你想在算法负载很重的浏览器物理 build 上比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 跑了一个 Stable Fluids HTML benchmark，给 GLM 5.2 Max 打了 88/100、成本约 1.17 美元，高于 Opus 4.8 和 Fable 5，但仍低于 GPT 5.6 Sol。 | Evaluation |
| [Case 199: Epoch 开放权重指数领先](#case-199) | 如果你想把 GLM-5.2 放到一条更长期的能力曲线上看，可以看这个案例，因为 Epoch AI 给它的 Capabilities Index 估分是 152，并称它是自己评估过的 open-weight 模型里最高的。 | Benchmark |
| [Case 196: Databricks 内部线束评估](#case-196) | 如果你想看 GLM-5.2 在大型私有工程 codebase 上的表现，可以看这个案例，因为 Databricks 说，他们覆盖 3000 多名工程师工作的内部评估发现 GLM 5.2 表现非常强，而且仅仅 harness 选择不同就能把成本压到约 2x。 | Evaluation |
| [Case 190: NatureBench 公开重量级亚军](#case-190) | 如果你想看 GLM-5.2 在 scientific-agent 工作里的基准表现，可以看这个案例，因为 NatureBench 说它在 6 个科学领域、90 个任务上首发即总榜第二，并拿到 open-weight 第一。 | Benchmark |
| [Case 189: 终端-工作台 45-任务成本权衡](#case-189) | 如果你想在同一套 agent harness 下比较 GLM-5.2 和 GPT-5.5，可以看这个案例，因为一组 45 个 Terminal-Bench 任务里，GLM-5.2 解出 25 个，GPT-5.5 解出 29 个，但前者在 prompt caching 下便宜约 40%。 | Evaluation |
| [Case 188: Harvey LAB-AA 法律代理领带](#case-188) | 如果你想看 GLM-5.2 在真实法律 agent 工作里的基准表现，可以看这个案例，因为 Harvey LAB-AA 显示 GLM-5.2 Max 在 24 个法律领域、120 个私有任务上拿到 7.5% all-pass，并列 Claude Opus 4.8。 | Benchmark |
| [Case 184: AutomationBench-AA 开放式重量领先](#case-184) | 如果你想比较 GLM-5.2 在遵守业务规则的 SaaS automation 里的表现，而不只是看 coding benchmark，可以看这个案例，因为 Artificial Analysis 报告 GLM-5.2 Max 在 AutomationBench-AA 上拿到 27.8%，并称它是 open weights 里的第一名。 | Evaluation |
| [Case 178: 三体模拟器基准获胜](#case-178) | 如果你想在带数值物理约束的 coding benchmark 里比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 跑了一个混沌三体模拟器任务，并给 GLM 5.2 Max 打出了 91/100 的最高分。 | Evaluation |
| [Case 167: GameDevBench 333 任务开源负责人](#case-167) | 如果你想在 agentic 游戏开发 benchmark 里追踪 GLM-5.2，可以看这个案例，因为 GameDevBench 已扩充到 333 个任务，并表示即使没有 vision，GLM-5.2 仍是排行榜上最强的 open-source model。 | Evaluation |
| [Case 175: 光标双摆记分卡](#case-175) | 如果你想在一个受限的 Cursor coding benchmark 里比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 用 HTML double-pendulum simulator 跑了 6 个模型，给 GLM 5.2 Max 打了 88/100，虽然落后于 Fable 和 Sonnet，但仍高于 GPT-5.5、Kimi K2.7 Code 和 Composer。 | Evaluation |
| [Case 162: VulcanBench 10 项任务 80% 平局](#case-162) | 如果你想在成本和分数同样重要的 post-cutoff 真实工程任务中比较 GLM-5.2，可以看这个案例，因为 Morgan Linton 说 VulcanBench 让 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 个 repo 上都拿到 80%，而 GLM 的成本落在中间。 | Evaluation |
| [Case 159: SWE-重新基准 51.1% 检查点](#case-159) | 如果你想持续跟踪 GLM-5.2 在 SWE agent 榜单上的位置，可以看这个案例，因为最新一条 SWE rebench 帖子给出的成绩是 51.1%，消耗 262 万 token，明显高于新加入的 DeepSeek、MiMo、Qwen 和 Gemma。 | Evaluation |
| [Case 154: 推出 Darkly Edge-Case 以 40/41 获胜](#case-154) | 如果你想看 GLM-5.2 在企业工具型 agent 任务里的表现，而不是只看聊天评测，可以用这个案例，因为 Composio 说它在 GitHub、Jira 和 LaunchDarkly 的 41 个任务里做对了 40 个，而且只有 GLM 抓到了一个待审批边界条件。 | Evaluation |
| [Case 146: CyberBench 开放重量补丁亚军](#case-146) | 如果你想衡量 GLM-5.2 在偏攻防式漏洞发现与补丁生成上的能力，可以用这个案例，因为 CyberBench 把它放在 60 个真实 OSS-Fuzz 漏洞上的总榜第二。 | Evaluation |
| [Case 1: 人工智能分析智能指数](#case-1) | 使用人工分析帖子将 GLM-5.2 与其他开放权重和专有前沿模型在智能和每项任务成本方面进行比较。 | Benchmark |
| [Case 2: Code Arena 前端排名](#case-2) | 使用此案例在通过竞技场式比较判断的真实前端编码任务上评估 GLM-5.2。 | Benchmark |
| [Case 3: 设计竞技场第一名](#case-3) | 使用此案例来判断 GLM-5.2 是否可以处理设计加代码任务，而不仅仅是文本密集型编码基准。 | Benchmark |
| [Case 4: FrontierSWE 结果](#case-4) | 使用 FrontierSWE 帖子将 GLM-5.2 与 GPT-5.5、Opus 和 Fable 风格的模型在软件工程任务上进行比较。 | Benchmark |
| [Case 5: DeepSWE 开源负责人](#case-5) | 使用 DeepSWE 案例了解 GLM-5.2 作为用于困难的软件工程评估任务的强大开放模型。 | Benchmark |
| [Case 6: 终端工作台超过 80%](#case-6) | 在评估面向终端的编码和代理工作流程的 GLM-5.2 时使用此案例。 | Benchmark |
| [Case 7: SWELancer 与 GPT-5.5 的比较](#case-7) | 使用此 SWELancer 案例作为 GLM-5.2 和 GPT-5.5 在任务成功、奖励和完成时间方面的具体多指标比较。 | Evaluation |
| [Case 8: BridgeBench 满分信号](#case-8) | 使用此案例来检查基于多步骤推理的 GLM-5.2，而不仅仅是编码排行榜。 | Benchmark |
| [Case 9: BridgeBench 推理排名第一](#case-9) | 使用此案例在扎根推理任务上将 GLM-5.2 与封闭边界模型进行比较。 | Benchmark |
| [Case 10: KernelBench-Hard 没有捷径](#case-10) | 在检查基准测试收益是否来自有效的实现行为而不是捷径时使用此案例。 | Evaluation |
| [Case 11: Runescape 长凳追赶](#case-11) | 使用此案例作为开放权重模型在类似游戏的基准任务上取得进展的快速信号。 | Benchmark |
| [Case 12: BridgeBench 速度提升](#case-12) | 使用此案例来评估对延迟敏感的工作流程，其中速度与智能同样重要。 | Benchmark |
| [Case 60: KernelBench 硬核和巨型 GPU 编码](#case-60) | 使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 评估 GPU 内核编码上的 GLM-5.2，其中开放代理跟踪使结果可检查。 | Benchmark |
| [Case 70: DeepSWE 高强度模式开源领先](#case-70) | 用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。 | Benchmark |
| [Case 72: LLM 辩论基准第二名](#case-72) | 用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。 | Benchmark |
| [Case 76: AA-Omniscience 幻觉率](#case-76) | 用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。 | Evaluation |
| [Case 90: GDPval-AA 代理工作指数](#case-90) | 如果你想比较 GLM-5.2 在长期知识工作中的表现，而不是只看编码榜单，可以用这个案例。 | Evaluation |
| [Case 94: 游戏开发竞技场亚军](#case-94) | 如果你想判断 GLM-5.2 的游戏构建质量，可以用这个案例。它在 Game Dev Arena 拿到第二名，并成为该榜单里开源权重阵营的第一名。 | Evaluation |
| [Case 120: PostTrainBench 可靠性领先](#case-120) | 如果你想比较 GLM-5.2 Max，不只看 headline 分数，也看它在 84 个任务上 failed run 为 0 的 agent reliability，可以用这个案例。 | Benchmark |
| [Case 121: Fireworks + Faros 211 项仓库任务评测](#case-121) | 如果你想在 private repo 的真实 engineering task 上评估 GLM-5.2，而不是只看公开 benchmark，可以用这个案例；帖子同时给出了分数、速度和每任务成本。 | Evaluation |
| [Case 110: AA-Briefcase 每任务耗时前沿](#case-110) | 用这个案例比较 GLM-5.2 在长周期知识工作上的表现，因为除了 benchmark 分数，单任务耗时同样关键。 | Benchmark |
| [Case 111: Code Arena 前端对战优势](#case-111) | 用这个案例查看 GLM-5.2 在前端任务上的成对对战优势，而不是只看一张排名截图。 | Benchmark |
| [Case 113: SWE Atlas 代码库问答亚军](#case-113) | 用这个案例跟踪 GLM-5.2 在代码库问答、测试编写和重构三条 SWE Atlas 榜单上的表现，而不是只看单项 SWE 榜单。 | Benchmark |

### [💻 编码代理与长上下文工作流](#coding-agents-long-context-workflows)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 243: Hermes 混合式 API 对等部署](#case-243) | 如果你想把一套 self-hosted 的 GLM-5.2 coding agent 和官方路线对照验证，可以看这个案例，因为 dangerm00se 说一套跑在 4x RTX 6000 PCIe 上的 Hermes + GLM-5.2 hybrid，和官方 API 的 60 个任务对上了 59 个，同时做到了 3,149 tok/s prefill、0.37 秒 warm TTFT 与 35.9 tok/s decode。 | Evaluation |
| [Case 237: LM Studio Bionic GLM 代理](#case-237) | 如果你想评估一套 local-first 的 GLM-5.2 coding agent，可以看这个案例，因为 chenzeling4 说 LM Studio Bionic 把 GLM 5.2 与本地文档 sandbox、inline code diff、rollback checkpoint 和端侧语音转写结合在了一起。 | Integration |
| [Case 236: Claude Code Web 开发质量优势](#case-236) | 如果你想比较首轮生成的 Web 开发质量，而不是单看完成速度，可以看这个案例，因为 Lumenix0 说在三个真实任务里，Claude Code 上的 GLM 5.2 在设计质量和功能完成度上都超过了 Codex 上的 GPT 5.5。 | Evaluation |
| [Case 168: Synthwave Hard-Slice Ensemble 售价 2.66 美元](#case-168) | 如果你想把 GLM-5.2 放进多模型 coding ensemble，而不是单独使用，可以看这个案例，因为 TracNetwork 表示一个含 GLM 的 Synthwave 组合在 LiveCodeBench hard 上以约 2.66 美元拿到 46.3%，并超过每个单独 generator。 | Integration |
| [Case 228: OpenCode 本地 agentic coding 底座](#case-228) | 如果你想在付费订阅 frontier 模型前先验证本地 coding-agent stack，可以看这个案例，因为 comma_ai 说他们已经移除 Anthropic，并发现 GLM 5.2 加 OpenCode 的 agentic coding 流程更好用。 | Demo |
| [Case 212: Dell Hub GLM Agent 教程](#case-212) | 如果你想为开放权重训练工作流搭一套 GLM-5.2 coding agent，可以看这个案例，因为 juanjucm 表示，一篇新指南把 Dell Enterprise Hub 新增 GLM-5.2-FP8 目录更新，与一套围绕该模型构建 agent 的逐步搭建流程放在了一起。 | Tutorial |
| [Case 211: 8xB200 开放权重报告流水线](#case-211) | 如果你想把 GLM-5.2 作为主写手，接进一条贴近本地部署的报告流水线，可以看这个案例，因为 TheZachMueller 表示，一台 8xB200 节点按 4/4 切分后，可以让 GLM 5.2 NVFP4 负责报告生成、Kimi K2.7 Code 负责检索，以相对 Claude API 只是零头的成本产出一份更密实的 36 页报告。 | Demo |
| [Case 210: Spettro 的 Liquid Glass 多代理改版](#case-210) | 如果你想把 GLM-5.2 当成一个研究密集型 frontend fixer，放进多代理网站改版流程里测试，可以看这个案例，因为 spettrotoken 表示在 Fable 5 和 GPT-5.5 都失败之后，GLM 5.2 通过整合好的 web scraping 和 data fetching 工具，做出了可在 Firefox 运行的跨浏览器 Liquid Glass 实现。 | Demo |
| [Case 194: CuTeDSL 内核技能开源](#case-194) | 如果你想研究 GLM-5.2 在可复用 kernel 调试 skill 里的表现，可以看这个案例，因为作者把一个 CuTeDSL 的 Hermes skill 开源出来，并明确说 GLM-5.2 在调试和编写 kernels 时特别省成本。 | Tutorial |
| [Case 180: Hermes SSD 恢复技能循环](#case-180) | 如果你想在面向修复的 agent loop 里测试 GLM-5.2，可以看这个案例，因为 ShankhadeepSho1 说 Hermes 加 GLM 5.2 诊断了一块故障 NAS SSD，修好了问题，然后把修复方案封装成了可复用 skill。 | Demo |
| [Case 174: 角色路由的重型编码器堆栈](#case-174) | 如果你想把 GLM-5.2 放进一套按角色路由的个人 stack，专门承担更重的 coding 工作，可以看这个案例，因为 denizirgin 表示，在用 Codex 和 OpenCode 测了一个月之后，他把更重的 coding work 交给了 GLM 5.2，同时把总月预算控制在 120 到 140 美元左右。 | Evaluation |
| [Case 155: Cotal 四代理 TUI 循环](#case-155) | 如果你想把一个编码循环拆给不同专长的 agent，可以看这个案例，因为作者用两个 GLM-5.2 worker，外加一个 Opus 负责人和一个 GPT reviewer，在 47 分钟内无人干预地做完了一个 lazygit 风格的完整 TUI。 | Demo |
| [Case 153: 旧版迁移成本削减试点](#case-153) | 如果你想评估 GLM-5.2 在遗留应用改造流程里能不能当更便宜的执行模型，可以看这个案例，因为 8090 的试点说 GLM 加 Software Factory 相比单跑 Opus 4.8 把成本压到了 1/16.4，但速度大约慢了 3 倍。 | Evaluation |
| [Case 150: Mac Studio浏览器-使用本地循环](#case-150) | 如果你想测试一套完全本地的 GLM-5.2 栈，是否已经能在消费级硬件上完成轻量 browser agent 工作，可以用这个案例，因为作者在 Mac Studio 上用 llama.cpp 和 browser-use 去 Hugging Face 找到了一个 PII 模型。 | Demo |
| [Case 148: Gumloop 代理交换成本削减](#case-148) | 如果你想在现有 agent harness 里直接试一次模型替换，可以用这个案例，因为 Gumloop 表示把最常用的 agent 换成 GLM-5.2 后，用户几乎没感到质量下降，而 credits 消耗大约少了 50%。 | Evaluation |
| [Case 13: 一小时四十二分钟重构循环](#case-13) | 使用此案例作为使用 TDD、审阅者反馈和回归检查进行长时间自主前端重构的模式。 | Demo |
| [Case 14: OpenCode Bug 修复和实施测试](#case-14) | 使用此案例来测试 GLM-5.2 作为 OpenCode 编码代理的错误修复以及小型实施任务。 | Demo |
| [Case 15: OpenCode 复古视频游戏演练](#case-15) | 使用此演练通过单个提示使用 GLM-5.2 和 OpenCode 构建一个小游戏，然后检查模型如何处理实现细节。 | Tutorial |
| [Case 16: HTML5 物理模拟竞赛](#case-16) | 使用此案例在没有库的独立 HTML5 物理模拟上比较 GLM-5.2 和 Kimi K2.7 代码。 | Evaluation |
| [Case 17: 个人网站 UI UX 构建](#case-17) | 使用此案例提示 GLM-5.2 打造一个精美的个人网站，并检查多次转动可以在多大程度上改善 UI/UX。 | Demo |
| [Case 18: AI合约审查产品构建](#case-18) | 使用此案例通过 PRD、时间预算、步骤计数、使用配额和代码质量比较来评估产品构建任务上的 GLM-5.2。 | Evaluation |
| [Case 19: ZCode 目标功能可实现更大的开发目标](#case-19) | 使用此案例了解如何将 GLM-5.2 集成到 ZCode 3.0 中以执行更大的代理开发任务。 | Integration |
| [Case 20: 使用 GLM-5.2 构建的 ZCode 的 Linux 包装器](#case-20) | 使用此案例作为 GLM-5.2 协助编码代理环境工具的示例。 | Demo |
| [Case 21: 计算机使用技能包装](#case-21) | 使用此案例来研究 GLM-5.2，将其作为将开源计算机使用存储库转变为可重用技能的助手。 | Demo |
| [Case 22: ZCode 3.0代理开发环境审查](#case-22) | 使用此案例在完整的代理开发环境而不是单个聊天会话中评估 GLM-5.2。 | Demo |
| [Case 62: 具有本地服务的 OpenCode Harness](#case-62) | 使用此案例通过 OpenCode 工具、本地服务和工具密集型编码工作流程来测试 GLM-5.2，然后将其与 Claude Opus 进行比较。 | Evaluation |
| [Case 65: Fast-RLM 长上下文指令注入](#case-65) | 使用此案例通过将指令移至 RLM 系统提示符来改进 GLM-5.2 长上下文计数和 REPL 代理行为。 | Integration |
| [Case 66: DeepAgents 代码开放式线束试用](#case-66) | 使用此案例尝试使用开放编码代理工具的 GLM-5.2，并在可重现的代理 shell 下比较模型。 | Demo |
| [Case 77: 生产级营销 Agent 栈路由策略](#case-77) | 用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。 | Evaluation |
| [Case 80: M3 究极精灵宝可梦 红色目标跑](#case-80) | 用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。 | Demo |
| [Case 91: Cline Repo 错误修复摊牌](#case-91) | 如果你想比较 GLM-5.2 和 Opus 4.8 在真实仓库 bug 修复中的表现，可以用这个案例。GLM 虽然消耗了更多 token，但最终补丁更便宜也更干净。 | Evaluation |
| [Case 102: OpenInspect FP8 后台代理](#case-102) | 如果你想研究自托管的 GLM-5.2 后台 agent 栈，而不是托管聊天工作流，可以用这个案例。 | Integration |
| [Case 145: OpenCode + Fireworks 降本迁移](#case-145) | 如果你想测试只换 open-model harness 是否已经足够，可以用这个案例，因为作者把个人 coding 和 loop task 迁到 Fireworks 上的 GLM-5.2 + OpenCode 后，称 token 成本降到了三分之一，而且日常质量没有明显掉档。 | Evaluation |
| [Case 143: Hermes MoA 的 GLM 聚合器工作流](#case-143) | 如果你愿意为高价值 agent 回合多做一层编排，可以用这个案例，因为 Hermes Agent 的 MoA 设置把 GLM-5.2 和其他模型组合后，在帖子里的 demo 中用很小的增量成本换来了更好的输出。 | Integration |
| [Case 142: Cline 推理开关带来的 Harness 差值](#case-142) | 如果你想判断决定结果的是 harness 还是权重本身，可以用这个案例，因为同一个 GLM-5.2 在同一批 coding task 上，仅仅打开 reasoning，结果就从 57.3% 跳到 68.5%。 | Evaluation |
| [Case 136: 光标 + Fireworks 455M-Token 现场测试](#case-136) | 如果你想判断 GLM-5.2 是否足以作为严肃的 Cursor 日常默认模型，可以用这个案例，因为作者报告了 4.55 亿 token 的真实使用量、快速的 Fireworks 服务体验，以及暂时不想切回 Opus 或 GPT-5.5。 | Evaluation |
| [Case 135: Devin 桌面安全带，具有技能便携性](#case-135) | 如果你觉得 Z.ai 自家的 coding surface 不稳定，想在 Devin Desktop 里测试 GLM-5.2，可以用这个案例，因为作者报告了更容易迁移 skill、更高速度和更好的可 hack 性。 | Evaluation |
| [Case 127: Pi 内联 GLM 审阅者](#case-127) | 如果你想在 Pi 风格的 coding-agent loop 里加入第二位审阅者，可以用这个案例。作者表示，GLM-5.2 可以逐回合给 Opus 提建议，成本增幅大约只有 10%。 | Integration |
| [Case 122: AgentRouter 一次成型 Telegram Bot](#case-122) | 如果你想测试 GLM-5.2 在 one-shot coding-agent build 里，是否能主动补上偏向生产环境的 defaults，而不是只写出最低限度可运行的路径，可以用这个案例。 | Demo |
| [Case 117: OpenCode Go 重构首轮取胜](#case-117) | 用这个案例评估 GLM-5.2 在 OpenCode 中处理中等规模 Go 重构任务的表现，而不是只看 benchmark 宣传。 | Evaluation |
| [Case 119: Claude Code + Cursor 默认运行成本 3.36 美元](#case-119) | 用这个案例判断 GLM-5.2 是否适合作为 Claude Code 和 Cursor 的日常默认模型，再决定是否把更多自主编码工作迁移到开放权重模型上。 | Evaluation |

### [🎮 上手演示与作品展示](#hands-on-demos-showcase-builds)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 229: Hyperagent 个人主页作品集对决](#case-229) | 如果你想在真实 browser-based agent 任务里比较 GLM-5.2 和其他 open model，可以看这个案例，因为 arsh_goyal 把 GLM 5.2、DeepSeek V4、Kimi K2.6 和 Qwen 3.7 并排放到 Hyperagent 上，用公开资料自动生成个人作品集。 | Demo |
| [Case 218: 用 OpenCode 重建作品集与操作系统](#case-218) | 如果你想衡量 GLM-5.2 在更有野心的 OpenCode build 里的表现，可以看这个案例，因为 MarkSShenouda 说，OpenCode Go 加上 GLM-5.2 帮他重建了一个作品集网站，以及一个用 C 和 Assembly 编写、能跑在 WASM 或 Qemu emulator 里的真实操作系统。 | 演示 |
| [Case 213: LlamaCoder v4 GLM 重构](#case-213) | 如果你想围绕 GLM-5.2 的规划和设计优势，原型化一条 one-prompt app generation 工作流，可以看这个案例，因为 nutlope 表示，LlamaCoder v4 已围绕 GLM 5.2 重构，改进了解析与规划，并且现在在一套免费开源 stack 上直接交付 WebAssembly renderer。 | Demo |
| [Case 202: 命令代码太空射击游戏功能获胜](#case-202) | 如果你想看 GLM-5.2 在 one-shot 交互式 UI build 里的表现，可以看这个案例，因为 Command Code 把同一个 retro space-shooter prompt 跑在 Fable 5、GPT 5.5、GLM 5.2 和 DeepSeek V4 Pro 上，并把 GLM 排在 features 第一。 | Evaluation |
| [Case 200: ZCode 任天堂 DS 模拟器](#case-200) | 如果你想看一个长时程、本地执行的 coding build，可以看这个案例，因为作者让 GLM-5.2 在 4x RTX 6000 的 ZCode 里，从零开始用 C++ 去做一个 Nintendo DS 模拟器。 | Demo |
| [Case 192: 命令代码 Flappy Bird UX Split](#case-192) | 如果你想看 GLM-5.2 在轻量设计类小游戏任务里的性价比，可以看这个案例，因为作者用同一个 Flappy Bird prompt 跑了 Command Code，最后认为 Fable 5 虽然价格接近 GLM-5.2 的 9 倍，但在 UX 上并没有明显更好。 | Evaluation |
| [Case 161: REAP NVFP4 魔方一击](#case-161) | 如果你想测试 GLM-5.2 在单一 prompt 的互动式 build 任务上的表现，可以看这个案例，因为 REAP-NVFP4 的 demo 说它只靠一个 prompt 就做出了 3D Rubiks Cube、真实 scramble、实时状态和 solve 按钮。 | Demo |
| [Case 158: OMP 中继 iPhone 客户端](#case-158) | 如果你想把一个本地 GLM-5.2 agent 很快包进移动端界面，可以看这个案例，因为作者说 Codex 的 build-ios-app plugin 只用了几个小时，就给一个已经接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很强的 iPhone 客户端。 | Demo |
| [Case 144: 开源 DevRel 研究 Agent](#case-144) | 如果你想把 GLM-5.2 从通用聊天模型变成垂直研究助手，可以用这个案例，因为作者做了一个开源 DevRel agent，能把产品和受众输入转成带证据和提纲的选题列表。 | Demo |
| [Case 123: Recast 六版本落地页迭代流程](#case-123) | 如果你想先用 GLM-5.2 生成多个版本，再把最佳结果交给 coding agent 继续做，以低成本试作 landing page，可以用这个案例。 | Tutorial |
| [Case 23: 可玩的密室一击](#case-23) | 使用此案例来比较 GLM-5.2 和 Opus 4.8 之间相同提示的游戏构建输出、运行时间和成本。 | Demo |
| [Case 24: 三个真实的构建结果参差不齐](#case-24) | 将此案例用作警示演示集：在信任用于生产游戏或视频任务的模型之前测试多个真实构建。 | Evaluation |
| [Case 25: ZCode 中的超级马里奥克隆](#case-25) | 使用此案例来评估使用 GLM-5.2 和 ZCode 在多个修复和功能过程中进行的迭代游戏构建。 | Demo |
| [Case 26: 月球登陆器竞赛](#case-26) | 使用此案例在交互式游戏类型任务上比较 GLM-5.2、MiniMax M3 和 Kimi K2.7 代码。 | Evaluation |
| [Case 27: 一键设计竞技场创建](#case-27) | 使用此案例来检查 GLM-5.2 可以从竞技场上下文中的单个设计提示生成什么。 | Demo |
| [Case 28: 研究论文理解工作流程](#case-28) | 使用此案例将 GLM-5.2 应用于包含上下文问题和跨论文参考的论文阅读工作流程。 | Integration |
| [Case 29: 受限制的诗歌比较](#case-29) | 在将 GLM-5.2 与寓言风格模型进行比较时，使用此案例将正确性与创意质量分开。 | Evaluation |
| [Case 30: 设计感示例](#case-30) | 使用此案例作为轻量级视觉设计信号，然后使用您自己的提示和 UI 审查进行验证。 | Demo |
| [Case 71: Temple Run 体素游戏单次生成](#case-71) | 用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。 | Demo |
| [Case 78: OpenCode Go 单次生成案例集](#case-78) | 用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。 | Demo |
| [Case 81: 太空侵略者一键构建](#case-81) | 用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。 | Demo |
| [Case 82: OpenCode 恢复实验室一次性](#case-82) | 用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。 | Demo |
| [Case 92: 打开设计参考 URL 重建](#case-92) | 如果你想测试 GLM-5.2 在参考驱动网页复刻上的能力，可以用这个案例。只给一个源 URL 和一条提示词，就几乎像素级复现了网站。 | Demo |
| [Case 99: 交易台成本质量测试](#case-99) | 如果你想比较 GLM-5.2 在全栈 UI 构建上的表现，可以用这个案例。它做出的交易终端效果接近最精致的结果，但成本只有头部结果的一小部分。 | Evaluation |
| [Case 100: 克劳德拒绝后的勒德分子游戏](#case-100) | 如果闭源模型因策略原因拒绝请求，而你又想原型化带策略敏感性的游戏概念，可以用这个案例测试 GLM-5.2。 | Demo |

### [🔌 供应商与工具集成](#provider-tool-integrations)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 239: TokenRouter 免费 GLM API 窗口](#case-239) | 如果你想拿到一个限时免费的 GLM-5.2 API 路径，可以看这个案例，因为 meliasiih 说 TokenRouter 在 2026 年 7 月 25 日前提供免费访问，并给出了清晰的注册流程、API key 路径和公开 base URL。 | Tutorial |
| [Case 238: Agentuity 上的 Wafer GLM 网关](#case-238) | 如果你想把 GLM-5.2 接入 Agentuity gateway stack，可以看这个案例，因为 wafer_ai 说其 serverless 路径已经在 Agentuity 上提供 GLM 5.2 regular / Fast，两档都带 1M context，速度约 100 到 250 tok/s。 | Integration |
| [Case 232: Macroscope Check Run GLM 代理](#case-232) | 如果你想在保留 check-run workflow 的同时压低 PR review agent 成本，可以看这个案例，因为 kayvz 说 Macroscope 的 Check Run Agents 现在可以直接从常规 `.md` repo 配置里选用 GLM 5.2。 | Integration |
| [Case 231: Aster 281 TPS 研究代理 API](#case-231) | 如果你想 benchmark 一个高速 hosted GLM-5.2 endpoint，可以看这个案例，因为 asterailabs 说 Aster Inference 把来自 research-agent 优化的 API 路由以 281 tokens per second 提供给 GLM 5.2。 | Integration |
| [Case 230: TrueFoundry 原生 Wafer GLM 路由](#case-230) | 如果你想把 GLM-5.2 接进现有 TrueFoundry AI Gateway stack，可以看这个案例，因为 wafer_ai 说这条 native provider integration 从 GLM 5.2 和 GLM 5.2 Fast 开始，而且不需要改动网关其余部分。 | Integration |
| [Case 225: TogetherLink Codex Harness 桥接](#case-225) | 如果你想把 GLM-5.2 跑进现有 coding-agent CLI，可以看这个案例，因为 nutlope 说 TogetherLink 是一个开源 CLI，能让 Codex 和 Claude Code 直接调用 GLM 5.2 这类 open model。 | Integration |
| [Case 224: Vorflux 开放模型 Harness 路由](#case-224) | 如果你想在不写自定义胶水代码的前提下，把 GLM-5.2 接进完整 agent session，可以看这个案例，因为 vorfluxai 说它的 Open Model Harness 会把 GLM 5.2 分配给 design、build 和 simplify 步骤，同时保留 Vorflux 其余流程不变。 | Integration |
| [Case 170: NVIDIA 免费 API 即插即用访问](#case-170) | 如果你想通过免费 hosted endpoint 快速试用 GLM-5.2，可以看这个案例，因为 hqmank 表示 NVIDIA 已开放 OpenAI 兼容的 API 路径，而且确认可以直接 plug-and-play 接上。 | Integration |
| [Case 169: Free Workers AI 编码代理路线](#case-169) | 如果你想为 coding agent 建立一条零成本的 GLM-5.2 路线，可以看这个案例，因为这篇教程用 OpenAI 兼容的 `cf/zai-org/glm-5.2` endpoint，把 Workers AI 接到 Claude Code、OpenCode、Cursor 和 Aider。 | Tutorial |
| [Case 220: OpenMed 去标识临床代理](#case-220) | 如果你想把 GLM-5.2 放进一条更注重隐私的临床 agent 流程里，可以看这个案例，因为 MaziyarPanahi 说，在 OpenMed 本地去标识、Gemma 4 负责结构化之后，GLM 5.2 完成了整例的规划、工具调用和 disposition 编写。 | 集成 |
| [Case 219: Katana 的 USDC GLM 接入路径](#case-219) | 如果你想通过一条 wallet 原生的按次付费路径接入 GLM-5.2，可以看这个案例，因为 imgn_ai 说 Katana 在 Base 上通过 x402 提供 GLM-5.2，不需要账号，使用 USDC 结算，并公开了可直接集成的 llms.txt。 | 集成 |
| [Case 214: Databricks AI Gateway GLM 路由](#case-214) | 如果你想在 agent tooling 里测试一条托管式且响应很快的 GLM-5.2 接入路径，可以看这个案例，因为 QCXINT_ 表示，Databricks AI Gateway 提供了组织专属 base URL 和 token 流程，暴露出一条速度非常快、看起来支持 1M context 的 GLM 5.2 路由，但后端身份仍未确认。 | Integration |
| [Case 208: 打开分子查看器代理堆栈](#case-208) | 如果你想把 GLM-5.2 接入一条开放的科学检视 workflow，可以看这个案例，因为 MaziyarPanahi 把经由 Hugging Face Inference Providers 的 GLM-5.2，和跑在 llama.cpp 上的 Qwen3-VL、Mol*、PydanticAI 串在一起，用单个 prompt 就把 EGFR 加 erlotinib 的结构 render 并做出评论。 | Integration |
| [Case 204: 困惑顾问 WANDR 成本基准](#case-204) | 如果你想估算 GLM-5.2 在 routing 式 computer-use harness 里的成本结构，可以看这个案例，因为 Perplexity 说它的 GLM 5.2 加 advisor 配置在 WANDR 上是 2.1x，而 Opus 是 6.1x，整体 benchmark 成本也接近一半。 | Evaluation |
| [Case 203: 同事开放工件路由](#case-203) | 如果你想把 GLM-5.2 放进企业 artifact 工作流，可以看这个案例，因为 Coworker 说 Open Artifacts 能做 docs、decks、PDF、spreadsheets、dashboards 和 apps，而且 optimized router 能把 token 使用量压到约 5 分之 1，同时仍提供美国托管的 GLM 5.2。 | Integration |
| [Case 201: DotCode 上下文上传工作流程](#case-201) | 如果你想在私有 coding sandbox 里给 GLM-5.2 更多项目上下文，可以看这个案例，因为 DotCode 给 GLM 5.2 加上了 screenshot、图片、CSV、PDF、源码文件和 zip 上传，并把这些都接进同一条 filesystem + terminal 工作流。 | Integration |
| [Case 221: SGLang TopK-V2 的 B300 agentic 服务](#case-221) | 如果你想 benchmark GLM-5.2 在长上下文 agent workload 上的生产服务能力，可以看这个案例，因为 lmsysorg 说，SGLang 在 8xB300、batch size 1 下达到了每用户 500+ tok/s，同时把单用户交互性提升了 18% 到 34%。 | 评测 |
| [Case 215: llm-d H200 Prefix-Cache 路由](#case-215) | 如果你想在 H200 上 benchmark GLM-5.2 的托管 serving economics，可以看这个案例，因为 RedHat_AI 表示，llm-d 的 Wide EP 加 prefix-cache 路由，让一条 700B+ 的 GLM-5.2 路线实现了超过 90% 的 cache reuse、低于 3 秒的 TTFT，以及每百万输出 token 约 2 美元的成本。 | Integration |
| [Case 209: Colibri 25GB RAM 稀疏流媒体](#case-209) | 如果你想理解本地 GLM-5.2 实验的新下限，可以看这个案例，因为 techNmak 详细说明 Colibrì 如何靠从 NVMe 串流 experts，用大约 25GB RAM 跑起 744B MoE，不过最小配置只有大约 0.05 到 0.1 tok/s。 | Demo |
| [Case 206: SGLang NVFP4 生产吞吐量](#case-206) | 如果你想估算 GLM-5.2 NVFP4 的正式生产 SGLang serving 规模，可以看这个案例，因为官方 SGLang v0.5.15 release 说它现在在 8x B300 上可达每位用户 500+ tok/s，在 4x GB300 上则是 450 tok/s，batch size 为 1。 | Evaluation |
| [Case 198: Dahl 100M 免费 GLM 端点](#case-198) | 如果你想走一条不用绑卡、又兼容 OpenAI 的路径来试 GLM-5.2，可以看这个案例，因为 Dahl Inference 给 GLM 5.2 FP8 提供了 1 亿免费 tokens，并且写清了如何建 key、如何调用 `/v1/chat/completions`。 | Tutorial |
| [Case 195: NVIDIA 免费端点 GLM 设置](#case-195) | 如果你想在不 self-hosting 的情况下把 GLM-5.2 接进 coding tools 里测试，可以看这个案例，因为原帖给出了一条免费的 NVIDIA endpoint 路线，直接把 GLM-5.2 的 API key 用到 Claude Code、Cursor 或 Cline。 | Tutorial |
| [Case 193: 0G TeeML 私有推理路由](#case-193) | 如果你想把 GLM-5.2 接到一条更注重隐私的 provider 路线上，可以看这个案例，因为 0G 说 GLM 5.2 已经跑在 TeeML 上，prompts 被封装在 TEE enclave 里，而且价格低于官方路线。 | Integration |
| [Case 185: DuckDB Flock 的 Open-SQL PR](#case-185) | 如果你想把 GLM-5.2 带进完全开源的本地 SQL analysis，可以看这个案例，因为 lhoestq 说，一个 duckdb + flock 的 PR 已经让 GLM-5.2 进入 100% open-source 的数据栈。 | Integration |
| [Case 179: 一键26款API接入](#case-179) | 如果你想先通过单一 OpenAI 兼容 provider 试用 GLM-5.2，可以看这个案例，因为 Alan_Earn 说一把 API key 就能访问 GLM-5.2 和另外 25 个模型，还带 26 美元起始 credits。 | Tutorial |
| [Case 176: NVIDIA NIM OpenCode 思维设置](#case-176) | 如果你想通过 NVIDIA 免费 NIM endpoint 把 GLM-5.2 接进 OpenCode，并且走一条明确开启 thinking 的零成本路线，可以看这个案例，因为 Dracoshowumore 分享了 API key 流程、base URL，以及一份由工具层接管 function calls、让 GLM 以 enable_thinking=true 运行的 OpenCode 配置。 | Tutorial |
| [Case 165: 通过移动代理控制启动 ZCode](#case-165) | 如果你想把 ZCode 当成 GLM-5.2 的官方 coding surface 来评估，可以看这个案例，因为 launch report 说这个免费的 agentic IDE 会上 Windows、macOS、Linux，还能通过 Telegram、WeChat、Feishu 跟踪项目进度。 | Integration |
| [Case 160: OpenWiki 自动维护代理文档](#case-160) | 如果你想让 agent 可读的文档自动保持最新，可以看这个案例，因为 LangChain 说 OpenWiki 会随着代码变化重建并维护 repo docs，而且能跑在 GLM 5.2 这类开源模型上。 | Integration |
| [Case 152: 通过 FireConnect 铸造 PTU](#case-152) | 如果你想在不重写 agent 客户端的前提下，把 GLM-5.2 接到企业级 Foundry 预算里，可以用这个案例，因为 Fireworks 说 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。 | Integration |
| [Case 147: Braintrust GLM 评估工作台](#case-147) | 如果你想把 GLM-5.2 和 Opus 放进同一套 eval 栈里比较，可以用这个案例，因为 Braintrust 联合 Baseten 给出了一个带长上下文成本与精度对照的接入样例。 | Integration |
| [Case 141: ClinePass 开放权重模型统一订阅](#case-141) | 如果你想把多个开放权重 coding model 收拢到同一个 agent harness 里，可以用这个案例，因为 ClinePass 把 GLM-5.2 和相关模型打包成统一月付，而不是分别维护 provider key 和账单。 | Integration |
| [Case 137: 面向编码代理的免费 GLM API 服务](#case-137) | 如果你想在 Hermes 或其他 coding agent 里无注册测试 GLM-5.2，可以用这个案例，因为共享服务会发放短时有效的 API key，整体接入足够轻量。 | Integration |
| [Case 31: OpenCode Go 可用性](#case-31) | 使用此案例通过文本、1M 上下文和类似 GLM-5.1 的定价来跟踪 OpenCode Go 工作流程中的 GLM-5.2 可用性。 | Integration |
| [Case 32: 奥拉马云可用性](#case-32) | 使用此案例将 GLM-5.2 路由到 Ollama Cloud 中，以进行可访问的开源编码模型实验。 | Integration |
| [Case 33: OpenRouter One API 调用访问](#case-33) | 在比较提供商路由或多模型堆栈时，使用此案例通过 OpenRouter 访问 GLM-5.2。 | Integration |
| [Case 34: vLLM 零日支持](#case-34) | 使用此案例通过 vLLM 自行托管或提供 GLM-5.2 服务，并提供零日支持。 | Integration |
| [Case 35: 通过 Baseten 获得概念可用性](#case-35) | 使用此案例将 GLM-5.2 识别为 Notion 工作流程中可用的开放权重模型。 | Integration |
| [Case 36: 烟花零日服务](#case-36) | 使用此案例来评估 Fireworks 作为需要托管基础设施的 GLM-5.2 工作负载的服务路径。 | Integration |
| [Case 37: 谷歌云模型花园链接](#case-37) | 使用此案例在面向 Google Cloud 的部署和代理平台上下文中查找 GLM-5.2。 | Integration |
| [Case 38: 威尼斯隐私模式](#case-38) | 当隐私模式、TEE 或端到端加密是尝试 GLM-5.2 的决定因素时，请使用此案例。 | Integration |
| [Case 39: 命令代码可用性](#case-39) | 使用此案例尝试命令代码中的 GLM-5.2，具有低成本入门计划和长上下文编码功能。 | Integration |
| [Case 40: 来自 Nous Portal 的赫尔墨斯特工](#case-40) | 使用此案例通过 Nous Portal 和 OpenRouter 将 GLM-5.2 连接到 Hermes Agent 工作流程。 | Integration |
| [Case 41: io.net 零日启动合作伙伴](#case-41) | 在评估 753B 参数长上下文模型的计算支持服务时使用此案例。 | Integration |
| [Case 42: 模块化云零日服务](#case-42) | 使用此案例来考虑在提供商规模提供长上下文 GLM-5.2 服务的模块化云。 | Integration |
| [Case 61: 通过 OpenRouter 设置光标](#case-61) | 使用此案例通过 OpenRouter 在 Cursor 中配置 GLM-5.2，以实现低成本的开放模型编码工作流程。 | Tutorial |
| [Case 63: 放大视觉设计的代理眼睛](#case-63) | 当纯文本模型需要视觉审核支持来完成设计任务时，可以使用此案例将 GLM-5.2 与 Amp 自定义代理配对。 | Integration |
| [Case 69: Baseten 更快的一百万上下文服务](#case-69) | 当长上下文服务速度对于 Factory Droid、OpenCode 和编码工具很重要时，可以使用此案例通过 Baseten 路由 GLM-5.2。 | Integration |
| [Case 74: 面向网页设计的 Browser Use QA 子代理](#case-74) | 当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。 | Integration |
| [Case 79: ZCode 官方 IDE 每日免费额度](#case-79) | 当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。 | Tutorial |
| [Case 83: 通过 Fireworks 设置光标](#case-83) | 用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。 | Tutorial |
| [Case 84: VulcanBench ZAI 提供商支持](#case-84) | 用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。 | Integration |
| [Case 85: OpenCode 高/最大推理变体](#case-85) | 用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。 | Integration |
| [Case 86: Z.ai编码端点选择](#case-86) | 用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。 | Tutorial |
| [Case 87: ZenMux 免费 GLM-5.2 API 设置](#case-87) | 用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。 | Tutorial |
| [Case 93: 本体 ncode GLM 默认值](#case-93) | 如果你想把 GLM-5.2 接入 ncode 和 Noumena 风格的 agent 环境，并同时使用标准版与 1M 上下文端点以及默认模型支持，可以用这个案例。 | Integration |
| [Case 95: 克劳德代码通过 Baseten](#case-95) | 如果你想通过 Baseten key、自定义 base URL 和 `~/.claude/settings.json` 里的模型映射，在 Claude Code 里运行 GLM-5.2，可以用这个案例。 | Tutorial |
| [Case 96: Deepsec Pi 代理默认值](#case-96) | 如果你想在安全 harness 中测试 GLM-5.2，可以用这个案例。`deepsec` 把它设成了 Pi agent 默认模型，并报告了有竞争力的 eval 结果。 | Integration |
| [Case 101: Baseten + Droid 安全带快速入门](#case-101) | 如果你想通过 Baseten 和 Droid harness 快速跑通 GLM-5.2，并复用一套也适用于其他 IDE 的短配置流程，可以用这个案例。 | Tutorial |
| [Case 104: OpenAI 兼容的 GLM API 工作流程](#case-104) | 如果你想在 Python 里用一个 OpenAI 兼容客户端统一接入 GLM-5.2 的推理控制、tool calling、长上下文检索和成本统计，可以用这个案例。 | Tutorial |
| [Case 105: Perplexity Agent API 搜索沙箱](#case-105) | 如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，并通过单个 API 调用获得带搜索能力的沙盒 agent，可以用这个案例。 | Integration |
| [Case 109: Baseten 的 280 TPS GLM 接口](#case-109) | 如果你在意 provider 延迟表现，可以用这个案例查看 Baseten 对 GLM-5.2 高吞吐、低首 token 延迟的公开性能说法。 | Integration |
| [Case 128: Cloudflare Workers AI OpenCode 设置](#case-128) | 如果你想在不自备模型主机的情况下，通过 Cloudflare Workers AI 这条免费的 OpenAI 兼容路线运行 GLM-5.2 做 coding agent，可以用这个案例。 | Tutorial |
| [Case 129: Puter.js 零配置浏览器客户端](#case-129) | 如果你想在接触 API key、账单或后端配置之前，先用纯浏览器原型测试 GLM-5.2，可以用这个案例。 | Tutorial |
| [Case 130: SiliconFlow 统一端点接入](#case-130) | 如果你想把 GLM-5.2 放进更大的多模型栈里，可以用这个案例，因为帖子描述了一个带 free trial credit 的单一 OpenAI 兼容 SiliconFlow endpoint，同时覆盖中文和西方模型。 | Integration |
| [Case 124: HuggingChat 建站到 HF Space 部署](#case-124) | 如果你想在几乎免费的 personal-site flow 里试用 GLM-5.2，从 HuggingChat 搜集资料到部署到 Hugging Face Spaces，都可以参考这个案例。 | Tutorial |
| [Case 125: DigitalOcean Inference Engine 上线](#case-125) | 如果你想通过 managed infrastructure 获得官方 provider access，而不自己托管 1M context 的模型，可以用这个案例接入 GLM-5.2。 | Integration |
| [Case 115: Command Code Fast 120-250 Tok/S 档位](#case-115) | 如果你更在意长周期编码任务的响应速度，而不只是最低入门价格，可以用这个案例接入更快的 GLM-5.2 档位。 | Integration |
| [Case 116: Vercel AI 网关快速 GLM-5.2 API](#case-116) | 如果你需要 serverless 速度和明确的 token 定价，可以用这个案例通过 Vercel AI Gateway 接入 GLM-5.2 Fast。 | Integration |

### [💸 成本、定价与本地部署](#cost-pricing-local-deployment)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 251: Ollama Pro 重负载 GLM 预算](#case-251) | 如果你想按 heavy-task quota 而不是标价来估算 flat-rate GLM-5.2 subscription，可以看这个案例，因为 iamcheyan 说 OpenCode Go 的周配额大概只够约 5 次重型 GLM-5.2 任务，但 Ollama Pro 的周池大约能支撑 3 天的持续 GLM 使用。 | Limit |
| [Case 249: Alibaba 统一 Token 方案](#case-249) | 如果你想比较的是跨模型 monthly access，而不是每家 provider 各自的储值余额，可以看这个案例，因为 Alibaba Cloud 说 Token Plan for Individuals 会把 text、image、video 工具共用同一池 credits，并把 GLM-5.2 列入 frontier text models，首月套用 coupon 后从 4 US dollars 起。 | Integration |
| [Case 246: 8x DGX Spark 400K 集群](#case-246) | 如果你想判断桌边 GLM-5.2 集群何时能替代 hosted API 开支，可以看这个案例，因为 thelichhh 说 8 台 DGX Spark 被连成一台拥有 1TB unified memory 的机器，把 GLM-5.2 载入到所有节点后，以 400K context 跑起来了。 | Demo |
| [Case 245: Pulsar CPU Expert Lane](#case-245) | 如果你想测一套低 VRAM 的 GLM-5.2 本地堆栈，可以看这个案例，因为 Giannisanii 说 Pulsar 的 CPU expert lane 让 GLM-5.2 744B 在两张 16GB GeForce、一块 NVMe 和 32GB RAM 的机器上，从 1.6 tok/s 提高到最高 2.8 tok/s。 | Demo |
| [Case 244: Peezy Go 3K GLM 窗口](#case-244) | 如果你想用 request cap 而不是 token 计价来比较 flat-rate 的 GLM-5.2 coding access，可以看这个案例，因为 SerPepeXBT 说 Peezy Go plan 现在会重置 limits、每 5 小时给到最多 3,000 次 GLM 5.2 requests，价格仍是每月 10 美元，首月降到 5 美元。 | Integration |
| [Case 242: ZenMux 249M Token Receipt](#case-242) | 如果你想用账单回执而不是目录价格来核对 GLM-5.2 的真实经济性，可以看这个案例，因为 AstridWiegner 说一张 ZenMux Token Receipt 显示处理了超过 249M token，原始成本为 105.81 美元，最终总额却是 0 美元。 | Evaluation |
| [Case 241: Zro Pro 300M GLM 试用](#case-241) | 如果你想用很小的预算测试 private hosted GLM-5.2 agent workflow，可以看这个案例，因为 AndarkFomo 说 Zro Pro 的 promo 大约用 1 美元就能换来约 300M 的 GLM-5.2 token，以及 OpenAI 兼容接入、EU 基础设施与 zero-retention 定位。 | Tutorial |
| [Case 240: DGX Station 256K 桌面部署](#case-240) | 如果你想估算桌面级 GLM-5.2 部署能力，可以看这个案例，因为 TheAhmadOsman 说 GLM 5.2 NVFP4 在 DGX Station 上以 256K context 跑出了约 3,000 tok/s prefill 和 32 tok/s decode。 | Demo |
| [Case 234: Jatevo 折扣 GLM 接入](#case-234) | 如果你想快速掌握一条带公开定价的 hosted GLM-5.2 接入路径，可以看这个案例，因为 JatevoId 说其平台上 GLM 5.2 的 input 价格是 $1.40 / 1M、output 价格是 $4.40 / 1M，符合条件的 JTVO holder 还能拿到 50% 折扣。 | Integration |
| [Case 233: MI325x 上低于 0.1 美分的 GLM 服务](#case-233) | 如果你想评估 AMD 硬件上的 self-hosted GLM-5.2 inference 成本，可以看这个案例，因为 picocreator 说 4xMI325x 配置把 GLM 5.2 跑到了 1,482 tok/s，成本低于每百万 token 0.10 美元。 | Demo |
| [Case 226: Bonsai Mac Studio 病历分诊](#case-226) | 如果你想让一份很长的临床病历留在本地，同时让 GLM-5.2 在其上做推理，可以看这个案例，因为 MaziyarPanahi 说 GLM 5.2 通过 Mac Studio 上的 Bonsai 27B 分诊一份三年期病历，并找出了埋在 17 个月前的造影风险问题。 | Demo |
| [Case 191: Hermes 建立的 LiteLLM 本地实验室](#case-191) | 如果你想把 GLM-5.2 当作 coding agent 来搭一个本地 inference lab，可以看这个案例，因为原帖说 Hermes Agent + GLM-5.2 把 LiteLLM、Postgres、Prometheus 和 Grafana 都接在了一套 M3 Ultra 环境上。 | Integration |
| [Case 187: 双 M5 Max 离线无人机模拟器](#case-187) | 如果你想估算一套完全离线的 Apple Silicon GLM-5.2 agent 到底能做什么，可以看这个案例，因为 XavierLocalAI 报告了一个 753B 配置：在两台 128GB M5 Max 上以 26 tok/s 编写 droneship landing simulator。 | Demo |
| [Case 186: 5x DGX Spark 生产线束](#case-186) | 如果你想判断 5 节点 DGX Spark 配置是否已经够支撑生产级 GLM-5.2 工作，可以看这个案例，因为 thatcofffeeguy 报告了在 400K context 下单流约 13.9 tok/s，以及 3 条 lane 合计 19.9 tok/s 的 live harness 结果。 | Demo |
| [Case 183: M3 Ultra ds4-eval Q4 检查点](#case-183) | 如果你想用 ds4-eval 真正 benchmark 一台 Apple Silicon 单机上的 GLM-5.2，可以看这个案例，因为 ivanfioravanti 报告了一次 q4 运行：M3 Ultra 512GB 机器上约 16 tok/s，92 项里过了 76 项，总时长 8 小时 53 分。 | Evaluation |
| [Case 182: 4x RTX PRO 6000 构建指南](#case-182) | 如果你想评估一套严肃的本地 GLM-5.2-594B 方案，可以看这个案例，因为 QingQ77 分享了一份完整的硬件与运维指南，核心是 4 张 RTX PRO 6000、通过 opencode 暴露的 API，以及给 agent 用的 sandbox VM。 | Tutorial |
| [Case 181: 4x DGX Spark QuantTrio 运行](#case-181) | 如果你想估算 4 节点 DGX Spark 集群跑 GLM-5.2 QuantTrio 的上限，可以看这个案例，因为 Tech2Wild 给出了 200K context、单流 30 tok/s，以及 6 并发下总计 60.5 tok/s 的结果。 | Demo |
| [Case 177: 单个 M3 Ultra 4 位视频运行](#case-177) | 如果你想估算 GLM-5.2 在 Apple Silicon 单机上的可行性，可以看这个案例，因为 ivanfioravanti 展示了在一台 M3 Ultra 512GB 机器上以约 16 tok/s 跑 4-bit 版本，并拿它和约 17 tok/s 的 q2 ds4-eval 视频做比较。 | Demo |
| [Case 173: AMD MI355X 2626 Tok/s 节点服务](#case-173) | 如果你想估算 AMD 硬件上的高吞吐 GLM-5.2 推理能力，可以看这个案例，因为 wafer_ai 表示 MI355X 达到每节点 2626 tok/s、单流 213 tok/s，而且成本比 Blackwell 低超过 2 倍。 | Demo |
| [Case 172: Vercel 网关 287 Tok/s 无服务器](#case-172) | 如果你想估算 GLM-5.2 经过 serverless gateway 时的真实用户延迟，可以看这个案例，因为 wafer_ai 表示它的 GLM 5.2 Fast 路线不是只在 benchmark harness 中，而是在 Vercel AI Gateway 上跑到 287 tokens per second。 | Demo |
| [Case 171: 一键 RTX PRO 6000 部署](#case-171) | 如果你想估算隔离式 hosted GLM-5.2 部署的最低门槛，可以看这个案例，因为 XciD_ 表示 GLM-5.2-NVFP4 现在可在 8x RTX PRO 6000 的 Inference Endpoints 上以每小时 22 美元 one-click 部署。 | Integration |
| [Case 166: 5x ASUS GX10s 上的完整 744B](#case-166) | 如果你想估一个极端 home-lab GLM-5.2 部署的规模，可以看这个案例，因为作者说完整 744B 模型已经能在 5 台 ASUS GX10 上带 full context 跑起来，而且已经接到处理真实 workload 的 causal harness。 | Demo |
| [Case 164: 中国堆栈中的代理路由交换](#case-164) | 如果你更在乎成本压力而不是绝对最高质量，想把 GLM-5.2 放进 mixed-model stack 的 agent 层，可以看这个案例，因为作者说把 Sonnet 换成 GLM-5.2 之后，这个 slot 的输入成本降到五分之一，质量大约只掉了 3%。 | Evaluation |
| [Case 156: 744B 本地硬件层](#case-156) | 如果你想更现实地评估 GLM-5.2 的本地部署门槛，可以看这个案例，因为原帖说即便量化后，2bit 也大约要 239GB、4bit 大约要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比较实际的起步线。 | Limit |
| [Case 151: 本地 NVFP4 Rust 端口速度为 140 Tok/s](#case-151) | 如果你想估算一套调优后的本地 GLM-5.2 部署在真实 coding 工作里能做到什么，可以用这个案例，因为作者报告了 140 tok/s 的 NVFP4 推理速度，以及几分钟内完成的 Python 到 Rust 全量移植。 | Evaluation |
| [Case 140: B300 x2 代理主导的双栈启动](#case-140) | 如果你想评估严肃的自托管 GLM-5.2 部署范围，可以用这个案例，因为线程展示了分析师在不到一天内就在裸金属 B300 上同时拉起了 vLLM 和 SGLang 的 NVFP4 推理。 | Evaluation |
| [Case 139: oMLX M3 超预填充加速](#case-139) | 如果你想在最近的 kernel 工作之后重新判断 Apple Silicon 本地可行性，可以用这个案例，因为作者报告 M3 Ultra 512GB 上的 GLM-5.2 prefill 速度几乎翻倍，而且快速测试里没有明显质量崩塌。 | Evaluation |
| [Case 138: 20M 代币注册信用爆发](#case-138) | 如果你想判断官方注册赠送额度是否足以支持一次真正的 GLM-5.2 试用，可以用这个案例，因为帖子声称新账号可获 2000 万免费 token、无需绑卡，并提供完整 OpenAI 兼容访问。 | Integration |
| [Case 131: 4x DGX Spark 本地 GLM 操作手册](#case-131) | 如果你想判断 DGX Spark 集群是否是现实可行的本地 GLM-5.2 路线，可以用这个案例。整理出来的指南把具体硬件成本、集群拓扑和 vLLM 命令都对应到了 1M context 的 GLM 目标上。 | Tutorial |
| [Case 43: 输出代币成本比较](#case-43) | 使用此案例将 GLM-5.2 输出代币经济学与 Opus、Fable 和 GPT-5.5 风格的模型进行比较。 | Evaluation |
| [Case 44: 本地近前沿硬件投资回报率](#case-44) | 使用此案例来推理自托管类似 GLM-5.2 的模型是否可以为重度代理用户偿还硬件成本。 | Evaluation |
| [Case 45: 两个 Mac 工作室上的 MLX](#case-45) | 使用此案例探索在 Apple 硬件和面向 MLX 的设置上运行的本地 GLM-5.2。 | Demo |
| [Case 46: H100 每月本地部署索赔](#case-46) | 使用此案例作为成本比较提示，用于在订阅和自托管之间进行选择之前检查本地部署假设。 | Evaluation |
| [Case 47: 每日积分和克劳德更换索赔](#case-47) | 使用此案例来检查围绕 GLM-5.2 的免费信用和替代代理叙述，同时将营销声明与经过验证的工作负载适合度分开。 | Evaluation |
| [Case 48: 免费 ZCode 令牌窗口](#case-48) | 在承诺付费提供商或本地部署之前，使用此案例通过免费 ZCode 津贴测试 GLM-5.2。 | Integration |
| [Case 49: ZenMux 免费周优惠](#case-49) | 使用此案例来查找用于 GLM-5.2 测试的时间限制的自由访问窗口。 | Integration |
| [Case 50: crofAI 每代币定价](#case-50) | 在选择路线之前，使用此案例比较 GLM-5.2 的第三方提供商定价。 | Integration |
| [Case 51: API价差对比](#case-51) | 将 GLM-5.2 与其他前沿实验室和开放模型进行比较时，请使用此案例作为市场定价批评。 | Evaluation |
| [Case 64: 地下室本地推理速度](#case-64) | 在规划离线编码设置之前，使用此案例来估计大内存 Apple 硬件上的本地 GLM-5.2 推理吞吐量。 | Demo |
| [Case 68: Unsloth量化本地部署](#case-68) | 当完整模型权重对于普通本地硬件来说太大时，使用此案例来评估量化的 GLM-5.2 部署路径。 | Tutorial |
| [Case 88: 两台 M3 Ultra MLX 分布式运行](#case-88) | 用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。 | Demo |
| [Case 89: ZCode 乘数贯穿 9 月份](#case-89) | 用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。 | Integration |
| [Case 97: RTX PRO 6000 本地吞吐量](#case-97) | 如果你想评估高端本地 GLM-5.2 工作站的规模，可以用这个案例。双 Blackwell 桌面机在 4-bit 量化版本上保持了两位数的 decode 速度。 | Demo |
| [Case 98: Mac Studio API 投资回报率现实检查](#case-98) | 如果你想判断为了本地 GLM-5.2 推理购买 Mac Studio 是否划算，可以用这个案例。帖子里的回本测算明显更倾向于 API 或套餐访问。 | Evaluation |
| [Case 106: LiteLLM 本地中断保存](#case-106) | 如果托管前沿 API 宕机或额度耗尽，而你又要保证交付不中断，可以用这个案例参考本地部署的 GLM-5.2 与 LiteLLM 兜底。 | Demo |
| [Case 107: 个人与团队本地投资回报率](#case-107) | 如果你想判断本地部署 GLM-5.2 更适合个人还是团队，可以用这个案例做成本与组织规模判断。 | Evaluation |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 跑分](#case-112) | 如果你在评估高端本地工作站方案，可以用这个案例把四卡 GLM-5.2 配置放到高难终端 benchmark 里衡量。 | Evaluation |
| [Case 118: 2x RTX PRO 6000 Blackwell 本地 Crackme 解题](#case-118) | 如果你想判断严肃的本地 GLM-5.2 配置能否在没有 debugger 的情况下完成长时逆向任务，可以用这个案例。 | Demo |

### [🧭 限制、注意事项与安全信号](#limits-caveats-safety-signals)

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [Case 247: ZCode 默认开放 RCE 修补](#case-247) | 如果你需要为 GLM-5.2 coding agent 采用更严格的 sandboxing 提供理由，可以看这个案例，因为 weezerOSINT 说只用一个 prompt 的 ZCode 执行，就会在默认情况下用 full RCE 跑起 repo 内代码，而这个问题已通报并在 3.3.6 版修补。 | Limit |
| [Case 222: 面向生产的 GLM 护栏警告](#case-222) | 如果你需要为 GLM-5.2 coding agent 设更严格的 guardrail 提供理由，可以看这个案例，因为 mitsuhiko 说，这个模型很容易主动去 force-push、未经允许应用 Pulumi 变更，甚至触碰生产数据库。 | 限制 |
| [Case 216: KV-Cache 调试器边界条件漏检](#case-216) | 如果你想测试 GLM-5.2 在矛盾输入处理上的表现，而不是只看 clean-pass benchmark 数字，可以看这个案例，因为 cyrilXBT 表示，一次 KV-cache debugger 的正面对比显示，GLM 在干净配置上和其他模型一样答对，但会悄悄漏掉一个坏变量，并在没有任何警告的情况下给出一个 2.667x 错误的 preset。 | Evaluation |
| [Case 205: 静态 HTML 重写执行器未命中](#case-205) | 如果你不想把 1:1 legacy rewrite 完全交给 GLM-5.2 当 executor，可以看这个案例，因为一个大型 static HTML 到 React/Vite 的迁移在 OpenCode Go 和 Cline 上仍掉了太多细节，让作者更倾向把 GLM 当 planner 而不是 executor。 | Limit |
| [Case 197: Composio 47-任务代理差距](#case-197) | 如果你想看 GLM-5.2 在真实 SaaS agent 工作里还会在哪里出错，可以看这个案例，因为 Composio 把它接到 17 个工具、47 个任务上后，只通过了 45 个，主要失误点在完整性检查和模糊 SLA 判断。 | Evaluation |
| [Case 163: 初步网络研究平等](#case-163) | 如果你想衡量 GLM-5.2 在漏洞研究子任务上的能力，可以看这个案例，因为 Irregular 报告说，在一组范围很窄的 cyber suite 上，它的早期内部评测可与 GPT-5.4 和 Opus 4.6 接近，同时也明确提醒 end-to-end 攻击场景尚未测试。 | Limit |
| [Case 157: OpenRouter 削减开支技能重写](#case-157) | 如果你想在切换 agent 模型前把迁移成本算清楚，可以看这个案例，因为某个基金团队的 OpenRouter 试验里，GLM-5.2 的成本大约只有 Opus 的八分之一，但依然要重写 skill、补 routing 逻辑，还得接受更慢、更弱一些的输出。 | Limit |
| [Case 149: AA 冗长和推理权衡](#case-149) | 如果你想把 GLM-5.2 的 frontier 级 open-weight 智力表现和它的推理效率成本拆开看，可以用这个案例，因为 Artificial Analysis 一边把它列为开源权重最强，一边也指出它消耗了异常多的输出 token。 | Evaluation |
| [Case 134: Semgrep IDOR 狭赢警告](#case-134) | 如果你想把真实安全信号和标题党式放大区分开，可以用这个案例，因为来源明确说 GLM-5.2 只是在一个 IDOR benchmark 上赢过 Claude Code，并没有直接测试 Mythos 本身。 | Limit |
| [Case 132: LisanBench 推理效率差距](#case-132) | 如果你想先检查 GLM-5.2 在高推理负载任务上的表现，再决定是否把编码优势外推到其他场景，可以用这个案例。帖子里的 LisanBench 结果显示它虽然比 GLM-5 好，但相较其他开源模型仍然不够高效。 | Limit |
| [Case 133: PrinzBench 领域错配提醒](#case-133) | 如果你想让 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用这个案例，因为帖子把它较弱的 PrinzBench 分数和更强的软件、工具使用 benchmark 做了对照。 | Limit |
| [Case 52: 无视力警告](#case-52) | 使用此案例请记住，GLM-5.2 对于需要本机视觉功能的工作流程可能不太有用。 | Limit |
| [Case 53: 现实世界的代理差距警告](#case-53) | 使用此案例可以避免过度阅读基准测试胜利，以证明 GLM-5.2 与所有已部署的代理任务上的最佳专有模型相匹配。 | Limit |
| [Case 54: 安全护栏关注](#case-54) | 使用此案例提醒您在敏感域中部署 GLM-5.2 之前运行安全评估。 | Limit |
| [Case 55: 基准方法论批评](#case-55) | 即使总体结果有利于 GLM-5.2，也可以使用此案例来质疑基准方法。 | Limit |
| [Case 56: 高峰时段延迟问题](#case-56) | 在切换编码计划或将 Claude 代码式工作流程路由到 GLM-5.2 之前，使用此案例测试提供程序延迟。 | Limit |
| [Case 57: FutureSim 无改进结果](#case-57) | 在广泛部署之前，使用此案例检查编码增益是否推广到非编码领域。 | Limit |
| [Case 58: 发射准备情况批评](#case-58) | 使用此案例将模型功能与启动执行、文档和 API 准备情况分开。 | Limit |
| [Case 59: 编码计划价格上涨](#case-59) | 在推荐 GLM-5.2 作为低成本替代品之前，请使用此案例验证计划定价。 | Limit |
| [Case 67: 短时间并行工作与长代理运行](#case-67) | 使用此案例将 GLM-5.2 路由到短边界编码任务，同时为更深的多小时代理运行保留更强的模型。 | Limit |
| [Case 73: 代码审查与偏见检查](#case-73) | 用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。 | Limit |
| [Case 75: 高难推理计费异常](#case-75) | 用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。 | Limit |
| [Case 103: HalluHard 多圈幻觉信号](#case-103) | 如果你想在信任其他强基准结果前，先测试 GLM-5.2 在多轮幻觉敏感任务上的表现，可以用这个案例。 | Limit |
| [Case 108: 开放式安全紧急警告](#case-108) | 如果你在做安全规划，可以用这个案例理解开放权重 GLM-5.2 如何降低进攻性安全 agent 的实际操作门槛。 | Limit |
| [Case 126: Rust 错误修复通过但回合数高 7 倍](#case-126) | 如果你想把 GLM-5.2 的 code quality 优势和当前的 agent harness overhead 分开来看，可以用这个案例。它能修好 bug，但会比 Opus 消耗得多得多。 | Evaluation |
| [Case 114: Braintrust 模型替换成本警示](#case-114) | 用这个案例避免想当然地认为，在真实 agentic coding workflow 里把模型换成更便宜的选项后，质量还能保持不变。 | Evaluation |

<a id="benchmarks-frontier-evaluation"></a>
## 📏 基准与前沿评测
---
<a id="case-250"></a>
### Case 250: [FP16 Indexer 带来的 ToolEval 提升](https://x.com/volatilemarkts/status/2078663037825831172) (by [@volatilemarkts](https://x.com/volatilemarkts))

**如果你想 benchmark 的是 fine-tune 之后的本地 GLM-5.2 tool use，而不是原始 API baseline，可以看这个案例；volatilemarkts 表示，一个 753GB 的 FP8 fine-tune 再加上 custom FP16 indexer，让 SeraphimSerapis/tool-eval-bench 从标准 GLM 5.2 API 的 83% 提升到 94%。**

作者表示，这个 setup 使用了 fine-tuned GLM 5.2 model、753GB 的 FP8 weights，以及一个仍在积极开发中的 custom FP16 indexer。同一条帖子还说，相比标准 API baseline，这套配置大约多了 10 个百分点，并补充 tuned model 抓到了几行 Fable run 漏掉的内容。这让它成为一条具体的本地 benchmarking 与 fine-tuning 参考，而不是泛泛的 open-source 背书。

Type: Evaluation | Date: 2026-07-19

---
<a id="case-248"></a>
### Case 248: [Aikido 26-CVE 测试框架基线](https://x.com/AikidoSecurity/status/2078816460865253714) (by [@AikidoSecurity](https://x.com/AikidoSecurity))

**如果你想在真实的 code-audit harness，而不是 chat demo 里评估 GLM-5.2，可以看这个案例；Aikido 表示，他们针对 26 个已知 CVE 的 AI Code Analysis benchmark 让 GLM-5.2 在 pass@3 下重找出 16 个，并在 max reasoning 下以大约 1.3 倍成本再多拿到 3 个发现。**

这条帖子指向 Aikido 7 月 16 日的 benchmark report。该报告在公司的 production analysis harness 中，用 13 个模型去测 GitHub Advisory Database 的 26 个已知漏洞。报告把 GLM-5.2 放在完整 pass@3 表的中段，明确表示 open-weight model 正在追上，并展示 GLM-5.2 从 high 切到 max reasoning 后，能以约 1.3 倍成本多拿 3 个发现。这让它成为一条具体的 cyber code-review 基线，而不是泛泛的 security claim。

Type: Evaluation | Date: 2026-07-19

---
---
<a id="case-235"></a>
### Case 235: [DiligenceBench 金融评测排名](https://x.com/karinanguyen/status/2078245092855525578) (by [@karinanguyen](https://x.com/karinanguyen))

**如果你想评估 GLM-5.2 在公开股票研究 agent 上的表现，可以看这个案例，因为 karinanguyen 说 DiligenceBench 把 GLM 5.2 放在前列，并证明 finance harness 能让强模型同时更强且更便宜。**

karinanguyen 把 DiligenceBench 介绍为一个面向公开股票研究的 rubric-based evaluation，并表示 Meta Muse Spark 1.1 以 57.4% 拿下 finance harness 第一，GLM 5.2 紧随其后，排在 Sonnet 4.6 和 GPT-5.6 Sol 一带。她还提到，泛用工具主要放大的是强模型的执行能力，较弱模型则更依赖 domain-specific scaffolding；而这个 finance harness 已经足以改写 price-performance frontier，让 GLM 5.2 在绝对表现上非常突出，同时 MiniMax M3 在效率上更有优势。

Type: Evaluation | Date: 2026-07-17

---
<a id="case-227"></a>
### Case 227: [Gargantua WebGL Raytracer 胜出](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在偏物理的单文件 browser build 上 benchmark GLM-5.2，可以看这个案例，因为 AlicanKiraz0 说 GLM 5.2 Max 在 Gargantua geodesic raytracer 任务里更好地兼顾了数值正确性与 real-time rendering discipline。**

AlicanKiraz0 描述的是一个 one-file raw WebGL2 任务，要实现带 RK4 null-geodesic integration、accretion disk、gravitational lensing、redshift、Doppler effects、camera controls 和完整 control panel 的 Schwarzschild black-hole renderer。帖子强调，决定胜负的不只是 visuals，而是 numerical correctness、boundary handling 和 solver discipline；最终 GLM 5.2 Max 拿到 92/100，高于 GPT5.6 Sol Ultra 的 90、Kimi K3 Thinking Max 的 85，以及 Fable 5 Max 的 80。

Type: Evaluation | Date: 2026-07-16

<a id="case-223"></a>
### Case 223: [智能指数 Token 效率差距](https://x.com/ArtificialAnlys/status/2077466596528832678) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想为长周期 benchmark 工作负载规划 GLM-5.2 预算，可以看这个案例，因为 Artificial Analysis 说，GLM-5.2 Max 在 Intelligence Index 每个任务上的平均输出 token 约为 43K，而 Inkling 是 25K，Kimi K2.6 和 DeepSeek v4 Pro Max 也都更低。**

Artificial Analysis 这次拆出来看的不是 leaderboard 分数，而是输出 token 消耗，因此它直接把 GLM-5.2 放到了同类 open-weight 模型里偏贵的一侧。帖子对比了 Inkling 的 25K 平均输出 token、GLM-5.2 Max 的 43K、Kimi K2.6 的 38K，以及 DeepSeek v4 Pro Max 的 37K；如果团队已经认可 GLM 的质量，但还要预估 agent loop 的 token 消耗，这就是一条很实用的效率提示。

Type: Evaluation | Date: 2026-07-15

---
<a id="case-217"></a>
### Case 217: [EvalPlus 救援路由胜过 Fable](https://x.com/gmi_cloud/status/2077124979397947824) (by [@gmi_cloud](https://x.com/gmi_cloud))

**如果你想测试一条带 verifier 的双模型 coding 路由，可以看这个案例，因为 gmi_cloud 说，先跑 Opus 4.8、失败时再用 GLM 5.2 FP8 救援的方案，在 100 个冻结 EvalPlus 任务里做对了 94 个，比 Fable 5 多 5 个，而且成本低约 47%。**

gmi_cloud 说，这套 stack 跑了 50 个 HumanEval+ 和 50 个 MBPP+ 任务，只有在 Opus 没通过 verifier 时才调用 GLM 5.2 FP8，但最终 pass rate 仍然超过所有单模型。帖子也把 trade-off 说得很清楚：这套组合比 Fable 5 多用了 85.4% 的 tokens，但成本是 0.4251 美元对 0.8033 美元，而且 GLM 把 Opus 的 10 个失败里救回了 4 个。

类型: 评测 | 日期: 2026-07-14

---
<a id="case-207"></a>
### Case 207: [稳定流体浏览器基准](https://x.com/AlicanKiraz0/status/2075639232169705781) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在算法负载很重的浏览器物理 build 上比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 跑了一个 Stable Fluids HTML benchmark，给 GLM 5.2 Max 打了 88/100、成本约 1.17 美元，高于 Opus 4.8 和 Fable 5，但仍低于 GPT 5.6 Sol。**

这个 benchmark 要求每个模型交付一个单文件、self-contained 的 HTML，实现 Jos Stam stable fluids，并包含 semi-Lagrangian advection、iterative diffusion、pressure projection、实时 divergence 报告，以及交互式 paint 和 velocity injection。AlicanKiraz0 表示，GLM 5.2 Max 拿到 88/100，高于 Opus 4.8 的 86 分和 Fable 5 的 81 分，而且成本明显更低，因此这更像是一条检验数值正确性与实时浏览器性能的 engineering-style 评测，而不是只看审美的 frontend 比较。

Type: Evaluation | Date: 2026-07-10

<a id="case-199"></a>
### Case 199: [Epoch 开放权重指数领先](https://x.com/EpochAIResearch/status/2074894535558300103) (by [@EpochAIResearch](https://x.com/EpochAIResearch))

**如果你想把 GLM-5.2 放到一条更长期的能力曲线上看，可以看这个案例，因为 Epoch AI 给它的 Capabilities Index 估分是 152，并称它是自己评估过的 open-weight 模型里最高的。**

Epoch AI 说，GLM-5.2 在 Epoch Capabilities Index 上拿到了估算 152 分，而且这是他们评估过的 open-weight 模型里最高的分数。所以当你需要一个更总览的能力定位信号，而不只是狭义 coding 榜单时，这条帖子就很适合作为 benchmark 参考。

Type: Benchmark | Date: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Databricks 内部线束评估](https://x.com/alighodsi/status/2074996561306955958) (by [@alighodsi](https://x.com/alighodsi))

**如果你想看 GLM-5.2 在大型私有工程 codebase 上的表现，可以看这个案例，因为 Databricks 说，他们覆盖 3000 多名工程师工作的内部评估发现 GLM 5.2 表现非常强，而且仅仅 harness 选择不同就能把成本压到约 2x。**

Ali Ghodsi 说，Databricks 在自家任务、codebase 和基础设施上做了一次全面评估，覆盖 3000 多名软件工程师、三家 hyperscaler cloud，以及很多编程语言。帖子里说 GLM 5.2 表现非常好，而且同一个模型只要选对 harness，成本就能大约降低 2x，同时前面还用了 Omnigent 按任务去复用不同模型和 harness。

Type: Evaluation | Date: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [NatureBench 公开重量级亚军](https://x.com/OkhayIea/status/2074498200262889837) (by [@OkhayIea](https://x.com/OkhayIea))

**如果你想看 GLM-5.2 在 scientific-agent 工作里的基准表现，可以看这个案例，因为 NatureBench 说它在 6 个科学领域、90 个任务上首发即总榜第二，并拿到 open-weight 第一。**

NatureBench 要回答的问题是：一个 coding agent 在不使用 web search 的情况下，能不能发现一个方法，超过真实 Nature 系论文里公开发表的 SOTA。这个 benchmark 覆盖 6 个科学领域、90 个任务。更新里说，GLM-5.2 首发即排在 Claude Opus 4.7 之后的总榜第二，同时成为 open-weight 阵营第一，所以这是一条很具体的 scientific-agent workflow benchmark，而不只是普通代码生成信号。

Type: Benchmark | Date: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [终端-工作台 45-任务成本权衡](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (by [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**如果你想在同一套 agent harness 下比较 GLM-5.2 和 GPT-5.5，可以看这个案例，因为一组 45 个 Terminal-Bench 任务里，GLM-5.2 解出 25 个，GPT-5.5 解出 29 个，但前者在 prompt caching 下便宜约 40%。**

这条 benchmark 帖子说，团队用同一个 agent、同一套 prompts、同一套评测设置和同一个 harness 跑了 GPT-5.5 与 GLM-5.2，唯一变化的只有模型。GLM 解出 45 个任务中的 25 个，GPT-5.5 解出 29 个，但在 prompt caching 条件下，GLM 的成本大约低 40%。所以这是一条很具体的价格与成功率对照，而不是模糊的 workflow 偏好。

Type: Evaluation | Date: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Harvey LAB-AA 法律代理领带](https://x.com/ArtificialAnlys/status/2074541975186165887) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想看 GLM-5.2 在真实法律 agent 工作里的基准表现，可以看这个案例，因为 Harvey LAB-AA 显示 GLM-5.2 Max 在 24 个法律领域、120 个私有任务上拿到 7.5% all-pass，并列 Claude Opus 4.8。**

Artificial Analysis 说，Harvey LAB-AA 用 24 个法律 practice area 的 120 个私有任务来评估真实法律工作，并用二元 rubric 打分。首发结果里，GLM-5.2 Max 拿到 7.5% all-pass 和 91.0% criteria-pass，和 Claude Opus 4.8 并列，同时单任务成本大约只有 Claude Fable 5 的 6%。所以这既是一个 frontier 领域 benchmark，也是一条成本效率信号。

Type: Benchmark | Date: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [AutomationBench-AA 开放式重量领先](https://x.com/ArtificialAnlys/status/2074194764510208230) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想比较 GLM-5.2 在遵守业务规则的 SaaS automation 里的表现，而不只是看 coding benchmark，可以看这个案例，因为 Artificial Analysis 报告 GLM-5.2 Max 在 AutomationBench-AA 上拿到 27.8%，并称它是 open weights 里的第一名。**

Artificial Analysis 说，AutomationBench-AA 会在 40 个模拟 SaaS 应用上跑 657 个私有工作流任务，并用接近 12,000 条 objective 与 guardrail assertions 来打分。首发帖子里，GLM-5.2 Max 以 27.8% 领跑 open weights，但同时也明确写到，它仍然落后于更强的 closed models，而且每个任务的 guardrail violation 明显更高。所以这条案例既是 agentic business automation 的能力信号，也是限制信号。

Type: Evaluation | Date: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [三体模拟器基准获胜](https://x.com/AlicanKiraz0/status/2073823792543998170) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在带数值物理约束的 coding benchmark 里比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 跑了一个混沌三体模拟器任务，并给 GLM 5.2 Max 打出了 91/100 的最高分。**

这个 benchmark 同时要求三体物理、真实 RK4、近距离相遇稳定性、守恒量实时图表和交互控制。帖子说 GLM 5.2 Max 靠 Float64Array 状态、可复用 RK4 buffer、Plummer softening 和 adaptive substep 脱颖而出，所以它是一条很具体的工程质量评测，而不只是排行榜截图。

Type: Evaluation | Date: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [GameDevBench 333 任务开源负责人](https://x.com/iamwaynechi/status/2073081777091182633) (by [@iamwaynechi](https://x.com/iamwaynechi))

**如果你想在 agentic 游戏开发 benchmark 里追踪 GLM-5.2，可以看这个案例，因为 GameDevBench 已扩充到 333 个任务，并表示即使没有 vision，GLM-5.2 仍是排行榜上最强的 open-source model。**

iamwaynechi 表示，GameDevBench 的任务数量已经增至 333，论文也同步更新，并把 GLM-5.2 和 Opus 4.8 加入排行榜。贴文指出，Opus 以小幅差距领先整体排名，而 GLM-5.2 则是最强的 open-source model，因此这不只是文字 coding 的信号，也是一个实用的游戏构建型 workflow benchmark 观察点。

Type: Evaluation | Date: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [光标双摆记分卡](https://x.com/AlicanKiraz0/status/2073386918813778143) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**如果你想在一个受限的 Cursor coding benchmark 里比较 GLM-5.2，可以看这个案例，因为 AlicanKiraz0 用 HTML double-pendulum simulator 跑了 6 个模型，给 GLM 5.2 Max 打了 88/100，虽然落后于 Fable 和 Sonnet，但仍高于 GPT-5.5、Kimi K2.7 Code 和 Composer。**

AlicanKiraz0 在 Cursor 里用一个 HTML double-pendulum simulator 任务比较了 6 个模型，并公开了总分和各模型的具体弱点。贴文把 GLM 5.2 Max 描述为在视觉表现和教学性上都很强，但在 performance architecture 上不如 Fable 和 Sonnet 精致，比如 RK4 wrapper 有额外 allocation 风险，trail buffer 在 resize 时的处理也不够稳健。这让它成为一条具体的 comparative evaluation，而不是模糊的主观偏好判断。

Type: Evaluation | Date: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10 项任务 80% 平局](https://x.com/morganlinton/status/2072689409011679642) (by [@morganlinton](https://x.com/morganlinton))

**如果你想在成本和分数同样重要的 post-cutoff 真实工程任务中比较 GLM-5.2，可以看这个案例，因为 Morgan Linton 说 VulcanBench 让 GLM 5.2 High、Fable 5 Low 和 Sonnet 5 High 在 10 个 repo 上都拿到 80%，而 GLM 的成本落在中间。**

Morgan Linton 说，这个 benchmark 用了来自 Flask、aiohttp、sqlglot 等项目的 10 个真实工程任务，而且都被描述为 post-training-cutoff。Fable 5 Low、GLM 5.2 High 和 Sonnet 5 High 都拿到 80%，对应成本分别是 2.27、8.41、15.81 美元。这让它成为一个很有用的三方价格与质量检查点。

Type: Evaluation | Date: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [SWE-重新基准 51.1% 检查点](https://x.com/ibragim_bad/status/2072318238407483593) (by [@ibragim_bad](https://x.com/ibragim_bad))

**如果你想持续跟踪 GLM-5.2 在 SWE agent 榜单上的位置，可以看这个案例，因为最新一条 SWE rebench 帖子给出的成绩是 51.1%，消耗 262 万 token，明显高于新加入的 DeepSeek、MiMo、Qwen 和 Gemma。**

ibragim_bad 说，这次 SWE rebench 更新把 GLM-5.2 和几款新的开源模型一起加进来了。帖文里的数字显示，GLM 用 262 万 token 跑到 51.1%，而 DeepSeek V4 Pro 是 42.7%，MiMo V2.5 Pro 是 42.4%，Qwen 和 Gemma 更低，因此它是一个很具体的公开榜单检查点。

Type: Evaluation | Date: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [推出 Darkly Edge-Case 以 40/41 获胜](https://x.com/composio/status/2072355937415827950) (by [@composio](https://x.com/composio))

**如果你想看 GLM-5.2 在企业工具型 agent 任务里的表现，而不是只看聊天评测，可以用这个案例，因为 Composio 说它在 GitHub、Jira 和 LaunchDarkly 的 41 个任务里做对了 40 个，而且只有 GLM 抓到了一个待审批边界条件。**

Composio 把 GLM-5.2、Claude Opus 4.8 和 GPT-5.5 放到 41 个真实工具型 agent 任务里对比，这些任务会用到 GitHub、Jira 和 LaunchDarkly。GLM 做对了 40 个，Opus 和 GPT 都是 39 个。其中一个 LaunchDarkly 任务里，GLM 会先检查待审批项，再判断某个 flag 是否 stale，而另外两个模型只看开关状态就停了。

Type: Evaluation | Date: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [CyberBench 开放重量补丁亚军](https://x.com/ValsAI/status/2072099011398627639) (by [@ValsAI](https://x.com/ValsAI))

**如果你想衡量 GLM-5.2 在偏攻防式漏洞发现与补丁生成上的能力，可以用这个案例，因为 CyberBench 把它放在 60 个真实 OSS-Fuzz 漏洞上的总榜第二。**

ValsAI 解释说，CyberBench 同时考察两个任务：提交一个只会打崩漏洞版本的 PoC，以及在不破坏行为的前提下修补源码。帖子称，在 60 个来自 OSS-Fuzz 的内存安全漏洞上，GPT-5.5 总体第一，而 GLM 5.2 是表现最强的 open-weight 之一。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [人工智能分析智能指数](https://x.com/ArtificialAnlys/status/2067135640249209175) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**使用人工分析帖子将 GLM-5.2 与其他开放权重和专有前沿模型在智能和每项任务成本方面进行比较。**

Artificial Analysis 将 GLM-5.2 报告为其智能指数中领先的开放权重模型，得分为 51，在智能与每项任务成本方面处于帕累托前沿位置。该帖子还记录了模型大小、上下文窗口、定价和提供商可用性。

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena 前端排名](https://x.com/arena/status/2066957802741043641) (by [@arena](https://x.com/arena))

**使用此案例在通过竞技场式比较判断的真实前端编码任务上评估 GLM-5.2。**

Arena 账户报告称，GLM-5.2 Max 在 Code Arena 前端排名第二，领先于其他开放型号，接近顶级前沿入口。这篇文章对于前端、React、HTML、游戏、模拟和基于参考的设计用例特别有用。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [设计竞技场第一名](https://x.com/Designarena/status/2066940737011560652) (by [@Designarena](https://x.com/Designarena))

**使用此案例来判断 GLM-5.2 是否可以处理设计加代码任务，而不仅仅是文本密集型编码基准。**

Design Arena 报告称，GLM-5.2 以 1360 的 Elo 分数排名第一，凸显了开放权重模型设计代码性能的飞跃。将其视为设计基准信号，而不是替代特定于项目的 UI 审查。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE 结果](https://x.com/ProximalHQ/status/2066939701026787583) (by [@ProximalHQ](https://x.com/ProximalHQ))

**使用 FrontierSWE 帖子将 GLM-5.2 与 GPT-5.5、Opus 和 Fable 风格的模型在软件工程任务上进行比较。**

该帖子报告称 GLM-5.2 在 FrontierSWE 上排名第三，并将其定义为首批开放权重模型之一，以缩小与实施繁重的工程工作中顶级专有模型的差距。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE 开源负责人](https://x.com/AiBattle_/status/2066938378512126024) (by [@AiBattle_](https://x.com/AiBattle_))

**使用 DeepSWE 案例了解 GLM-5.2 作为用于困难的软件工程评估任务的强大开放模型。**

AiBattle 报告 GLM-5.2 的 DeepSWE 得分为 46.2%，并将其描述为该基准测试环境中开源模型的最高得分。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [终端工作台超过 80%](https://x.com/cline/status/2066951439793242193) (by [@cline](https://x.com/cline))

**在评估面向终端的编码和代理工作流程的 GLM-5.2 时使用此案例。**

Cline 强调 GLM-5.2 是第一个在 Terminal-Bench 上突破 80% 的开放权重模型，并将其定位为可访问的基于工具的开发的前沿选项。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [SWELancer 与 GPT-5.5 的比较](https://x.com/gosrum/status/2067153091842203676) (by [@gosrum](https://x.com/gosrum))

**使用此 SWELancer 案例作为 GLM-5.2 和 GPT-5.5 在任务成功、奖励和完成时间方面的具体多指标比较。**

作者分享了日本基准更新，其中 GLM-5.2 在最新的 SWELancer 结果上意外领先 GPT-5.5，包括任务成功率、获得的奖励和完成时间，其中排除了两项无法完成的任务。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench 满分信号](https://x.com/bridgemindai/status/2065874542321426819) (by [@bridgemindai](https://x.com/bridgemindai))

**使用此案例来检查基于多步骤推理的 GLM-5.2，而不仅仅是编码排行榜。**

BridgeMind 报告称，GLM-5.2 是第一个在 BridgeBench BS 基准测试中获得满分的模型，这使其成为推理密集型评估声明的有用来源。

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench 推理排名第一](https://x.com/bridgebench/status/2066123398816624743) (by [@bridgebench](https://x.com/bridgebench))

**使用此案例在扎根推理任务上将 GLM-5.2 与封闭边界模型进行比较。**

BridgeBench 报告称，GLM-5.2 在推理基准测试中排名第一，并在该测量环境中击败了 Claude Fable 5。

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard 没有捷径](https://x.com/elliotarledge/status/2065735912370417760) (by [@elliotarledge](https://x.com/elliotarledge))

**在检查基准测试收益是否来自有效的实现行为而不是捷径时使用此案例。**

KernelBench-Hard 帖子表示，有趣的结果不仅仅是分数，而且 GLM-5.2 停止在 fp8 GEMM 问题上使用不适当的快捷方式，使其与基准完整性相关。

Type: Evaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape 长凳追赶](https://x.com/maxbittker/status/2066985743197577433) (by [@maxbittker](https://x.com/maxbittker))

**使用此案例作为开放权重模型在类似游戏的基准任务上取得进展的快速信号。**

该帖子报告称，GLM-5.2 在 Runescape 平台上的得分优于最新的专有模型，并使用该结果来衡量开源前沿功能的追赶速度。

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench 速度提升](https://x.com/bridgebench/status/2065845045752648159) (by [@bridgebench](https://x.com/bridgebench))

**使用此案例来评估对延迟敏感的工作流程，其中速度与智能同样重要。**

BridgeBench 报告称，GLM-5.2 比 GLM-5.1 快三倍，在其速度基准上排名第四，这使其与迭代速度影响可用性的工作流程相关。

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench 硬核和巨型 GPU 编码](https://x.com/elliotarledge/status/2068177175640240323) (by [@elliotarledge](https://x.com/elliotarledge))

**使用此案例跨 KernelBench-Hard 和 KernelBench-Mega 评估 GPU 内核编码上的 GLM-5.2，其中开放代理跟踪使结果可检查。**

KernelBench 更新报告了 H100、B200 和 RTX PRO 6000 测试、开源代理跟踪以及 GLM-5.2 作为比较中排名最高的开放模型。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE 高强度模式开源领先](https://x.com/datacurve/status/2068473057107476680) (by [@datacurve](https://x.com/datacurve))

**用这个案例跟踪 GLM-5.2 在 DeepSWE 高强度设置下的表现；帖文榜单显示它以 44% pass@1 位列开源模型第一。**

DataCurve 分享的 DeepSWE 榜单更新显示，GLM-5.2 在开源模型中达到 44% pass@1，并领先 Kimi K2.7 Code 17 个点。应将其视为一次 benchmark 更新，而不是所有真实世界 agent 工作流都已被解决的证明。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM 辩论基准第二名](https://x.com/LechMazur/status/2068428300460974279) (by [@LechMazur](https://x.com/LechMazur))

**用这个案例评估 GLM-5.2 在编码之外的对抗式多轮辩论表现；max-reasoning 版本在结果中位列 Claude 系列之后的第二名。**

Lech Mazur 分享了一项 LLM Debate Benchmark 结果，其中 GLM-5.2 Max 排名第二。这个基准衡量的是跨广泛主题的对抗式多轮辩论能力，因此它提供的是编码榜单之外的推理信号。

Type: Benchmark | Date: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience 幻觉率](https://x.com/yuhasbeentaken/status/2068259921519423855) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**用这个案例比较 GLM-5.2 的不确定性处理能力；帖文中的 AA-Omniscience 结果显示，它的幻觉率低于若干其他前沿模型。**

帖子报告 GLM-5.2 在 AA-Omniscience 上的幻觉率为 28%，低于 Fable 5 和 DeepSeek V4 Pro 的对应结果。这个基准关注的是模型在不确定时是否会拒答或承认不确定，而不是继续猜测。

Type: Evaluation | Date: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA 代理工作指数](https://x.com/ArtificialAnlys/status/2069121548670406947) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想比较 GLM-5.2 在长期知识工作中的表现，而不是只看编码榜单，可以用这个案例。**

Artificial Analysis 报告称，GLM-5.2 在 GDPval-AA 上拿到 1524 Elo，综合排名第 3，落后于 Claude Fable 5 和 Opus 4.8，略高于 1509 的 GPT-5.5 xhigh。它也是断层领先的开源权重模型第一名。帖子还提到，这个 benchmark 在 1,999 场对局中平均每个任务大约进行了 31 轮交互。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [游戏开发竞技场亚军](https://x.com/Designarena/status/2069166634976371084) (by [@Designarena](https://x.com/Designarena))

**如果你想判断 GLM-5.2 的游戏构建质量，可以用这个案例。它在 Game Dev Arena 拿到第二名，并成为该榜单里开源权重阵营的第一名。**

Design Arena 报告称，GLM-5.2 在 Game Dev Arena 上拿到 1368 Elo，比 GLM-5.1 提高 29 分，排名提升 6 位。帖子表示，它已经进入与 Claude Fable 5 相同的性能区间，并且综合排名第二；如果按实验室维度看，它超过了 OpenAI，仅次于 Anthropic。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [PostTrainBench 可靠性领先](https://x.com/hrdkbhatnagar/status/2070244540108423427) (by [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**如果你想比较 GLM-5.2 Max，不只看 headline 分数，也看它在 84 个任务上 failed run 为 0 的 agent reliability，可以用这个案例。**

hrdkbhatnagar 分享了一张 PostTrainBench leaderboard，显示 GLM 5.2 Max reasoning 以 34.29% 略高于 Opus 4.8 Max 的 34.08%。同一条帖子还提到，GLM 在 84 次 runs 中 failed run 为 0，而 Opus agents 的 failure rate 大约在 10% 左右。对于既看重 raw pass rate、也重视 agent reliability 的团队来说，这是一个很有价值的 benchmark。

Type: Benchmark | Date: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fireworks + Faros 211 项仓库任务评测](https://x.com/FireworksAI_HQ/status/2070181898962534570) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在 private repo 的真实 engineering task 上评估 GLM-5.2，而不是只看公开 benchmark，可以用这个案例；帖子同时给出了分数、速度和每任务成本。**

Fireworks 表示，他们与 Faros 联合进行的 211 项真实 engineering task 评测中，Claude Code + GLM-5.2 同时领先于 Claude Code + Opus 4.8 和 Codex + GPT-5.5。帖子给出的数字包括 judge score 0.568 对 0.521 / 0.466、每任务 321 秒 对 775 / 392，以及每任务 0.92 美元 对 1.76 / 2.06，并特别说明 Faros 使用的是自家 repositories 与实际工作，而不只是公开 benchmark。

Type: Evaluation | Date: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase 每任务耗时前沿](https://x.com/ArtificialAnlys/status/2069914443639635978) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用这个案例比较 GLM-5.2 在长周期知识工作上的表现，因为除了 benchmark 分数，单任务耗时同样关键。**

Artificial Analysis 表示，GLM-5.2 位于 AA-Briefcase 的 Pareto 前沿，得分为 1261，单任务平均耗时 16.3 分钟，分数高于 1159 的 GPT-5.5 xhigh，同时仍是该 benchmark 中表现最强的开放权重模型。对于要同时比较长周期交付质量与运行时长的团队来说，这个案例比单看排行榜名次更有参考价值。

Type: Benchmark | Date: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Code Arena 前端对战优势](https://x.com/arena/status/2069885722333769963) (by [@arena](https://x.com/arena))

**用这个案例查看 GLM-5.2 在前端任务上的成对对战优势，而不是只看一张排名截图。**

arena 拆解了 GLM-5.2 Max 为什么能登上 Code Arena: Frontend 榜首，称它在除一组之外的所有对战配对里都拿到了更高胜率。帖子点名了它对 Kimi-K2.6 的 61.0%、对 Sonnet 4.6 的 59.4%、对 Opus 4.7 Thinking 的 55.0%，以及对 GPT-5.5 xHigh 的 41.7% 对 40.0% 险胜，并提到它与 GLM-5.1 直接打成 45.5% 平手。

Type: Benchmark | Date: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas 代码库问答亚军](https://x.com/ScaleAILabs/status/2069864932913631617) (by [@ScaleAILabs](https://x.com/ScaleAILabs))

**用这个案例跟踪 GLM-5.2 在代码库问答、测试编写和重构三条 SWE Atlas 榜单上的表现，而不是只看单项 SWE 榜单。**

Scale AI Labs 表示，GLM 5.2 已经上线 SWE Atlas 的三条榜单：Codebase QnA、Test Writing 和 Refactoring。帖子特别提到它在 Codebase QnA 上拿到第 2 名，并把这一结果描述为开放模型已经能在这些任务上全面逼近前沿闭源系统。

Type: Benchmark | Date: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 编码代理与长上下文工作流
---
<a id="case-257"></a>
### Case 257: [OpenCodex 模型切换工作流](https://x.com/vista8/status/2079239701391675404) (by [@vista8](https://x.com/vista8))

**如果你想在以 Codex 为中心的 coding loop 里给 GLM-5.2 做路由，而不是被锁定在单一模型上，可以看这个案例，因为 vista8 说 OpenCodex 让同一套环境可以在 GLM 5.2、Kimi K3、GPT-5.6 Sol 和 Grok 4.5 之间切换，用于前端设计、后端工作和实时 X 搜索。**

vista8 说，Codex 依然是自己日常使用最频繁的 coding tool，但前端审美是它的弱项，所以工作流转到了一个可以按需切模型的 OpenCodex 项目里。帖文给出的路由说明很实用：前端设计走通过 OAuth 接入的 Kimi K3，后端工作切到 GPT-5.6 Sol，实时 X 搜索交给 Grok 4.5，同时把 GLM 5.2 作为同一 coding surface 里的可替换选项之一。因此，这更像是一条面向 coding agents 的具体模型路由工作流，而不是单纯的模型排名观点。

Type: Integration | Date: 2026-07-20

---
<a id="case-255"></a>
### Case 255: [Hermes 11 代理混合实验室](https://x.com/MichaelGannotti/status/2079168568478912834) (by [@MichaelGannotti](https://x.com/MichaelGannotti))

**如果你想围绕 GLM-5.2 搭一套按角色分工的多代理实验室，而不是只用一个单体助手，可以看这个案例，因为 MichaelGannotti 说一套 11 代理的 Hermes 配置，会在 DGX Spark、Ryzen 工作站和云端模型之间动态路由任务，其中就包括用于软件、研究、营销和协调工作的 GLM 5.2。**

MichaelGannotti 给出了一套很具体的实验室架构：一台带 128GB unified memory 的 DGX Spark 作为主要本地推理服务器，一台 Ryzen 9 Halo Strix 机器运行 8 个负责工程与组织角色的 Hermes agents，另一台 Ryzen 7 Windows 机器再运行 3 个面向内容与微软生态工作的 agents。在这套配置里，每个 agent 会按任务在云端的 GPT-5.6、GLM 5.2、Grok 4.5，以及本地的 Qwen、Nemotron、Gemma 模型之间做选择，因此这条帖子更像是一份混合本地加云端 agent 团队的操作模型参考，而不是含糊的效率宣传。

Type: Integration | Date: 2026-07-20

---
<a id="case-243"></a>
### Case 243: [Hermes 混合式 API 对等部署](https://x.com/dangerm00se/status/2078369336239313368) (by [@dangerm00se](https://x.com/dangerm00se))

**如果你想把一套 self-hosted 的 GLM-5.2 coding agent 和官方路线对照验证，可以看这个案例，因为 dangerm00se 说一套跑在 4x RTX 6000 PCIe 上的 Hermes + GLM-5.2 hybrid，和官方 API 的 60 个任务对上了 59 个，同时做到了 3,149 tok/s prefill、0.37 秒 warm TTFT 与 35.9 tok/s decode。**

dangerm00se 把这个结果描述成 autonomy milestone，而不是单纯的 throughput 截图。帖文表示，这套 Hermes + GLM-5.2 hybrid 跑在 DDR4 主机上的 4x RTX 6000 PCIe 上，达到了 3,149 tok/s prefill、0.37 秒 warm TTFT 与 35.9 tok/s decode，并在 60 个任务里有 59 个和官方 GLM API 一致。它还另外指向 setup instructions 与和官方路线对照的 accuracy report，因此更像一条具体的 local-agent 参考，而不是含糊的 self-hosting 炫耀。

Type: Evaluation | Date: 2026-07-18

<a id="case-237"></a>
### Case 237: [LM Studio Bionic GLM 代理](https://x.com/chenzeling4/status/2077967277698515184) (by [@chenzeling4](https://x.com/chenzeling4))

**如果你想评估一套 local-first 的 GLM-5.2 coding agent，可以看这个案例，因为 chenzeling4 说 LM Studio Bionic 把 GLM 5.2 与本地文档 sandbox、inline code diff、rollback checkpoint 和端侧语音转写结合在了一起。**

chenzeling4 把 LM Studio Bionic 描述为一套围绕 open-weight 模型构建的 standalone agent，可按任务选择本地或云端算力，并在两条路径上都强调 zero retention。帖文还明确指出，coding 由 GLM 5.2 与 Kimi K2.7 Code 负责，文档处理运行在带自动 rollback checkpoint 的 sandbox 里，代码改动通过 inline diff 展示，语音转写则通过 Voxtral 完全在设备端完成，因此它更像是一条具体的 local-agent workflow 更新，而不是单纯的模型上架信息。

Type: Integration | Date: 2026-07-17

---
<a id="case-236"></a>
### Case 236: [Claude Code Web 开发质量优势](https://x.com/Lumenix0/status/2078241726897230164) (by [@Lumenix0](https://x.com/Lumenix0))

**如果你想比较首轮生成的 Web 开发质量，而不是单看完成速度，可以看这个案例，因为 Lumenix0 说在三个真实任务里，Claude Code 上的 GLM 5.2 在设计质量和功能完成度上都超过了 Codex 上的 GPT 5.5。**

Lumenix0 总结了一次 head-to-head 对比：一边是通过 Claude Code 运行的 GLM 5.2，另一边是通过 Codex 运行的 GPT 5.5，任务包括 website redesign、React bug hunt 和从零构建 Kanban board。帖文表示，GPT 在每个任务上的完成速度都更快，但 GLM 做出了更强的 redesign、在 bug 修复时给出更清晰的解释，并且交付了唯一一个 one-shot 就完全可用的 Kanban board，包含 task naming、priority、status change 和 reset button。帖文还补充，这三次测试总共只消耗了 16 美元订阅周额度的 7%。

Type: Evaluation | Date: 2026-07-17

---
<a id="case-168"></a>
### Case 168: [Synthwave Hard-Slice Ensemble 售价 2.66 美元](https://x.com/TracNetwork/status/2073038214592360522) (by [@TracNetwork](https://x.com/TracNetwork))

**如果你想把 GLM-5.2 放进多模型 coding ensemble，而不是单独使用，可以看这个案例，因为 TracNetwork 表示一个含 GLM 的 Synthwave 组合在 LiveCodeBench hard 上以约 2.66 美元拿到 46.3%，并超过每个单独 generator。**

TracNetwork 表示，他们通过 OpenRouter 建立了一个 Synthwave ensemble，用 qwen3-coder-next 当 synthesizer，并以 GLM-5.2、qwen3.5-122b、qwen3-coder-next 作为 coding generator。在 82 个 LiveCodeBench hard 任务上，贴文报告成绩为 46.3%，成本约 2.66 美元，且没有任何单一 generator 能单独达到这个分数。这是一个具体例子，说明 GLM-5.2 适合作为成本导向 ensemble 的一员，而不一定要当唯一的 coding model。

Type: Integration | Date: 2026-07-03

---

---

<a id="case-228"></a>
### Case 228: [OpenCode 本地 agentic coding 底座](https://x.com/comma_ai/status/2077819467267186700) (by [@comma_ai](https://x.com/comma_ai))

**如果你想在付费订阅 frontier 模型前先验证本地 coding-agent stack，可以看这个案例，因为 comma_ai 说他们已经移除 Anthropic，并发现 GLM 5.2 加 OpenCode 的 agentic coding 流程更好用。**

comma_ai 说，自家的 GLM deployment 就跑在训练 open-source driving agent 的机器旁边，因此这更像是本地所有权信号，而不是单纯偏爱 cloud。thread 明确把 GLM 5.2 和 OpenCode 绑在一起，并说团队在把 Anthropic 移出 stack 后，日常 agentic coding 体验反而更好，所以它更适合被视为一条实操型的 local-first workflow 参考，而不是泛泛的开源口号。

Type: Demo | Date: 2026-07-16

<a id="case-212"></a>
### Case 212: [Dell Hub GLM Agent 教程](https://x.com/juanjucm/status/2076714987569963508) (by [@juanjucm](https://x.com/juanjucm))

**如果你想为开放权重训练工作流搭一套 GLM-5.2 coding agent，可以看这个案例，因为 juanjucm 表示，一篇新指南把 Dell Enterprise Hub 新增 GLM-5.2-FP8 目录更新，与一套围绕该模型构建 agent 的逐步搭建流程放在了一起。**

juanjucm 表示，他写了一篇公开指南，介绍如何搭建一个基于 GLM-5.2 的 coding agent，用来训练两个小型语言模型，并把这份教程与 Dell Enterprise Hub 将 GLM-5.2-FP8 加入目录这件事连在一起。链接到的 Hugging Face 文章给出了公开教程入口，而帖文本身则把这套 stack 定位为一条面向动手训练和 agent 实验的 open-weight 路线，而不是一条泛泛的可用性通知。

Type: Tutorial | Date: 2026-07-13

---

<a id="case-211"></a>
### Case 211: [8xB200 开放权重报告流水线](https://x.com/TheZachMueller/status/2076746035758502275) (by [@TheZachMueller](https://x.com/TheZachMueller))

**如果你想把 GLM-5.2 作为主写手，接进一条贴近本地部署的报告流水线，可以看这个案例，因为 TheZachMueller 表示，一台 8xB200 节点按 4/4 切分后，可以让 GLM 5.2 NVFP4 负责报告生成、Kimi K2.7 Code 负责检索，以相对 Claude API 只是零头的成本产出一份更密实的 36 页报告。**

TheZachMueller 表示，他花了一个周末调参后，把一条真实工作流水线从 Claude Code 迁到了 Pi dot dev 加 open-weight stack 上。发布的配置把一台 8xB200 节点拆成两半：GLM 5.2 NVFP4 作为主 agent 和 driver，Kimi K2.7 Code 作为 retriever，最终产出一份 36 页报告，而 Claude 的版本只有 21 页。帖子也把 tradeoff 说得很清楚：整体周转时间从大约 20 分钟变成约 30 到 40 分钟，而质量上最大的修正，是不要反复总结源文章，而是把完整文章保存在磁盘上以便做更深的检索。

Type: Demo | Date: 2026-07-13

---

<a id="case-210"></a>
### Case 210: [Spettro 的 Liquid Glass 多代理改版](https://x.com/spettrotoken/status/2076330234492698844) (by [@spettrotoken](https://x.com/spettrotoken))

**如果你想把 GLM-5.2 当成一个研究密集型 frontend fixer，放进多代理网站改版流程里测试，可以看这个案例，因为 spettrotoken 表示在 Fable 5 和 GPT-5.5 都失败之后，GLM 5.2 通过整合好的 web scraping 和 data fetching 工具，做出了可在 Firefox 运行的跨浏览器 Liquid Glass 实现。**

spettrotoken 表示，一次真实上线中的 Spettro 网站改版被拆成四个 Spettro instance，各自负责不同的 frontend 区块，而 GLM-5.2 则负责最难的视觉组件：一个通常会在 Firefox 坏掉的折射式 Liquid Glass 效果。帖子指出，GLM 5.2 会自行搜索 web、阅读 CSS 和 SVG filter workaround、逆向拆解这个效果，最后交付一个已部署到 live site 的可用跨浏览器实现；更大范围的改版则还有 Kimi K2.7 与并行 sub-agent 一起支持。

Type: Demo | Date: 2026-07-12

---

<a id="case-194"></a>
### Case 194: [CuTeDSL 内核技能开源](https://x.com/SubhoGhosh02/status/2074466050557739469) (by [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**如果你想研究 GLM-5.2 在可复用 kernel 调试 skill 里的表现，可以看这个案例，因为作者把一个 CuTeDSL 的 Hermes skill 开源出来，并明确说 GLM-5.2 在调试和编写 kernels 时特别省成本。**

帖子说，这个 skill 的大部分内容，是通过 Hermes 里跨多个模型的 agentic conversations 构建出来的，而 GLM-5.2 在 kernel debugging 和 kernel writing 过程中尤其体现了成本效率。原帖还给出了精确的安装和启动命令：`hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` 与 `hermes chat -s cutedsl-kernels`，所以这不是一句模糊推荐，而是一条可复用的 tutorial-style workflow。

Type: Tutorial | Date: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Hermes SSD 恢复技能循环](https://x.com/ShankhadeepSho1/status/2073658918937473444) (by [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**如果你想在面向修复的 agent loop 里测试 GLM-5.2，可以看这个案例，因为 ShankhadeepSho1 说 Hermes 加 GLM 5.2 诊断了一块故障 NAS SSD，修好了问题，然后把修复方案封装成了可复用 skill。**

作者说，一块 QNAP NAS 的 SSD 坏了，他把它接到一台备用机器上，然后交给 Hermes 做诊断。这个结果很具体：帖子称这套 stack 修好了问题，随后还为自己生成了一个 skill，并把恢复策略写进了 infrastructure wiki。

Type: Demo | Date: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [角色路由的重型编码器堆栈](https://x.com/denizirgin/status/2073462071639876004) (by [@denizirgin](https://x.com/denizirgin))

**如果你想把 GLM-5.2 放进一套按角色路由的个人 stack，专门承担更重的 coding 工作，可以看这个案例，因为 denizirgin 表示，在用 Codex 和 OpenCode 测了一个月之后，他把更重的 coding work 交给了 GLM 5.2，同时把总月预算控制在 120 到 140 美元左右。**

denizirgin 表示，他目前的个人配置把 Codex、OpenCode、DeepSeek、OpenRouter，以及一套用来判断 coding、review、research、speed、cost 的自制 sub-agent skill 和 decision table 组合在一起。在这个 routing 方案里，GLM 5.2 通过补充 provider 承担 heavy-duty coder 的角色，Codex 保留为 main backbone，而 OpenRouter 则更偏向用来做模型实验。它因此更像一条来自一线使用者的成本敏感 workflow 笔记，而不是泛泛的模型排名。

Type: Evaluation | Date: 2026-07-04

<a id="case-155"></a>
### Case 155: [Cotal 四代理 TUI 循环](https://x.com/silvanrec/status/2072335315822403656) (by [@silvanrec](https://x.com/silvanrec))

**如果你想把一个编码循环拆给不同专长的 agent，可以看这个案例，因为作者用两个 GLM-5.2 worker，外加一个 Opus 负责人和一个 GPT reviewer，在 47 分钟内无人干预地做完了一个 lazygit 风格的完整 TUI。**

silvanrec 说，Cotal 协调了四个模型：两个 GLM-5.2 实例分别做前端和后端开发，GPT-5.5 在后台做 reviewer，Claude Opus 负责领导整个 loop。系统从一个做出真实 TUI 控制台的单一 prompt 出发，跑了四轮，找出了渲染和 tab wiring 的 bug，管理了 agent 之间的 handoff，最后在 47 分钟内产出了可运行结果。帖子还给出了 open source 层的入口：npx cotal-ai setup --full。

Type: Demo | Date: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [旧版迁移成本削减试点](https://x.com/chamath/status/2072390507628540213) (by [@chamath](https://x.com/chamath))

**如果你想评估 GLM-5.2 在遗留应用改造流程里能不能当更便宜的执行模型，可以看这个案例，因为 8090 的试点说 GLM 加 Software Factory 相比单跑 Opus 4.8 把成本压到了 1/16.4，但速度大约慢了 3 倍。**

Chamath 分享了一个把 PHP 迁到 Next.js 的初步试点。接入 8090 Software Factory 的 Opus 4.8 相比单跑 Opus，成本低了 1.4 倍、速度快了 1.5 倍；而同样的 factory 配上 GLM 5.2，则把成本压到了单跑 Opus 的 1/16.4，但运行速度大约慢了 3 倍。帖子也明确说这只是 n=1 的方向性结果，后面还要在 10 到 15 个真实遗留改造任务上重跑。

Type: Evaluation | Date: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Mac Studio浏览器-使用本地循环](https://x.com/MaziyarPanahi/status/2071955191260151862) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想测试一套完全本地的 GLM-5.2 栈，是否已经能在消费级硬件上完成轻量 browser agent 工作，可以用这个案例，因为作者在 Mac Studio 上用 llama.cpp 和 browser-use 去 Hugging Face 找到了一个 PII 模型。**

MaziyarPanahi 表示，他先在 Mac Studio 上通过 llama.cpp 本地运行 GLM-5.2，再把它包进一个 browser-use agent loop。帖子里的例子是让模型去 Hugging Face 找 PII 模型，最终定位到了 `privacy-filter-nemotron`。

Type: Demo | Date: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Gumloop 代理交换成本削减](https://x.com/aronkor/status/2072032854675218538) (by [@aronkor](https://x.com/aronkor))

**如果你想在现有 agent harness 里直接试一次模型替换，可以用这个案例，因为 Gumloop 表示把最常用的 agent 换成 GLM-5.2 后，用户几乎没感到质量下降，而 credits 消耗大约少了 50%。**

aronkor 描述了一次 Gumloop 内部实验：在保留同一套 harness 和同一份 prompt 的情况下，把最常用的一批 agent 直接换成了 GLM 5.2。结果是，几乎没人察觉输出质量差异，但 credits 消耗接近减半。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [一小时四十二分钟重构循环](https://x.com/KELMAND1/status/2066012493315723610) (by [@KELMAND1](https://x.com/KELMAND1))

**使用此案例作为使用 TDD、审阅者反馈和回归检查进行长时间自主前端重构的模式。**

该帖子描述了一项耗时 1 小时 42 分钟的 GLM-5.2 重构任务，其中包含 88 次模型转换和 102 次工具调用。工作流程包括交接、四个阻止程序修复、12 项测试的 TDD 实施、两轮 P2 修复和最终回归。

Type: Demo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug 修复和实施测试](https://x.com/altudev/status/2065868921341632881) (by [@altudev](https://x.com/altudev))

**使用此案例来测试 GLM-5.2 作为 OpenCode 编码代理的错误修复以及小型实施任务。**

作者报告称，测试 GLM-5.2 时修复了 6 个错误，并在 OpenCode 中实现了一项，并称这些更改通过可靠的规划和比 GLM-5.1 更快的速度顺利完成。

Type: Demo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode 复古视频游戏演练](https://x.com/AskVenice/status/2067047775783534789) (by [@AskVenice](https://x.com/AskVenice))

**使用此演练通过单个提示使用 GLM-5.2 和 OpenCode 构建一个小游戏，然后检查模型如何处理实现细节。**

Venice 分享了使用 GLM-5.2 和 OpenCode 构建复古视频游戏的完整演练，将其定位为私有、开源、长期编码工作流程。

Type: Tutorial | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 物理模拟竞赛](https://x.com/atomic_chat_hq/status/2067038851139334588) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**使用此案例在没有库的独立 HTML5 物理模拟上比较 GLM-5.2 和 Kimi K2.7 代码。**

Atomic Chat 报告要求两个模型构建泳池休息、弹簧块和高尔顿板模拟。他们的帖子称，GLM-5.2 以更详细和完善的方式处理了这三个问题，而 Kimi 则在身体行为方面遇到了困难。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [个人网站 UI UX 构建](https://x.com/anshuc/status/2067034697704857615) (by [@anshuc](https://x.com/anshuc))

**使用此案例提示 GLM-5.2 打造一个精美的个人网站，并检查多次转动可以在多大程度上改善 UI/UX。**

作者表示，GLM-5.2 在正确的提示下生成了一个富有创意的个人网站，并分享了结果的视频。它对于前端设计迭代而不是单次基准测试很有用。

Type: Demo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI合约审查产品构建](https://x.com/laozhang2579/status/2066339734956499301) (by [@laozhang2579](https://x.com/laozhang2579))

**使用此案例通过 PRD、时间预算、步骤计数、使用配额和代码质量比较来评估产品构建任务上的 GLM-5.2。**

这篇中文文章在人工智能合同审查产品 PRD 上比较了 GLM-5.2、Kimi K2.7 和 Claude Opus 4.8。它报告构建持续时间、步骤计数、五小时配额使用情况和代码质量评分。

Type: Evaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode 目标功能可实现更大的开发目标](https://x.com/zcode_ai/status/2066236605917188228) (by [@zcode_ai](https://x.com/zcode_ai))

**使用此案例了解如何将 GLM-5.2 集成到 ZCode 3.0 中以执行更大的代理开发任务。**

ZCode 宣布为编码计划用户提供 GLM-5.2、更强大的代理任务执行、更好的长上下文编码以及用于管理从计划到完成的更大目标的目标功能。

Type: Integration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [使用 GLM-5.2 构建的 ZCode 的 Linux 包装器](https://x.com/gosrum/status/2066484949755269510) (by [@gosrum](https://x.com/gosrum))

**使用此案例作为 GLM-5.2 协助编码代理环境工具的示例。**

作者报告使用 GLM-5.2 和 Claude Code 完成 zcode-linux，以便 Linux 用户可以在 Linux 环境中运行 ZCode 并添加任意 API 端点，包括本地 LLM 端点。

Type: Demo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [计算机使用技能包装](https://x.com/0xSero/status/2065952130054382079) (by [@0xSero](https://x.com/0xSero))

**使用此案例来研究 GLM-5.2，将其作为将开源计算机使用存储库转变为可重用技能的助手。**

该帖子称 GLM-5.2 正在设置计算机使用，找到了一个高级开源存储库，并将其转换为一项技能。它是工具包装和代理集成工作的实际操作信号。

Type: Demo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0代理开发环境审查](https://x.com/laogui/status/2066190262993559963) (by [@laogui](https://x.com/laogui))

**使用此案例在完整的代理开发环境而不是单个聊天会话中评估 GLM-5.2。**

国内评测称，ZCode 3.0由类似shell的早期版本重写为自主开发的代理核心，搭配GLM-5.2，在国内代理开发环境中具有更好的体验。

Type: Demo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [具有本地服务的 OpenCode Harness](https://x.com/PatrickToulme/status/2068134212587184442) (by [@PatrickToulme](https://x.com/PatrickToulme))

**使用此案例通过 OpenCode 工具、本地服务和工具密集型编码工作流程来测试 GLM-5.2，然后将其与 Claude Opus 进行比较。**

作者报告了本地部署、嵌套子代理、研究/规划行为和工作应用程序构建。

Type: Evaluation | Date: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM 长上下文指令注入](https://x.com/neural_avb/status/2067992817625088439) (by [@neural_avb](https://x.com/neural_avb))

**使用此案例通过将指令移至 RLM 系统提示符来改进 GLM-5.2 长上下文计数和 REPL 代理行为。**

发行说明描述了具体的代理脚手架更改和 GLM-5.2 长上下文基准测试效果。

Type: Integration | Date: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents 代码开放式线束试用](https://x.com/sydneyrunkle/status/2067947260369854830) (by [@sydneyrunkle](https://x.com/sydneyrunkle))

**使用此案例尝试使用开放编码代理工具的 GLM-5.2，并在可重现的代理 shell 下比较模型。**

作者报告使用 GLM-5.2 和 DeepAgents 代码，并框架开放模型和开放线束作为测试模式。

Type: Demo | Date: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [生产级营销 Agent 栈路由策略](https://x.com/DeRonin_/status/2068303752671477820) (by [@DeRonin_](https://x.com/DeRonin_))

**用这个案例把 GLM-5.2 路由到重视结构化、速度和自托管的生产 Agent 工作流中，同时把更强的闭源模型留给模糊判断任务。**

作者在一个代理机构栈里做了 6 天并行对比后表示，GLM-5.2 在开始漂移前可稳定执行 60 多个 agent 步骤，连续 800 多次匹配结构化格式，并提供低延迟的自托管响应。同一条帖子仍然更偏好用 Opus 处理语音关键或高歧义任务，因此真正有价值的是这条路由规则本身。

Type: Evaluation | Date: 2026-06-20

---

<a id="case-80"></a>
### Case 80: [M3 究极精灵宝可梦 红色目标跑](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**用这个案例评估 GLM-5.2 在长时间本地 coding agent 运行中的表现，跟踪它在 M3 Ultra 上用接近半天时间复刻 Pokemon Red HTML 版本的尝试。**

作者把 Claude Code 的模型切到本地 GLM 5.2，在一台 M3 Ultra 512GB 机器上跑了 12 小时的 `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.` 任务。帖文公开了运行时长、token 消耗、代码 churn、RAM 使用量以及 GGUF 和 KV-cache 配置，并指出模型质量感觉接近 frontier，但本地推理速度仍是主要瓶颈。

Type: Demo | Date: 2026-06-21

---


<a id="case-91"></a>
### Case 91: [Cline Repo 错误修复摊牌](https://x.com/cline/status/2069171146994729078) (by [@cline](https://x.com/cline))

**如果你想比较 GLM-5.2 和 Opus 4.8 在真实仓库 bug 修复中的表现，可以用这个案例。GLM 虽然消耗了更多 token，但最终补丁更便宜也更干净。**

Cline 在相同 harness 和相同工具条件下，用 Cline 仓库里的同一个 bug 测试了两个模型。帖子称，GLM 使用了约 110 万 token，而 Opus 使用了 66 万；成本分别是 0.41 美元和 0.81 美元；耗时分别是 4.7 分钟和 28 次工具调用，对比 1.6 分钟和 12 次工具调用。最终 GLM 还清理了死代码并成功完成 production build，而 Opus 留下了虽然能通过测试但仍存在的类型错误。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 后台代理](https://x.com/colemurray/status/2069485572339707938) (by [@colemurray](https://x.com/colemurray))

**如果你想研究自托管的 GLM-5.2 后台 agent 栈，而不是托管聊天工作流，可以用这个案例。**

colemurray 分享了一个由 OpenInspect 和 Modal Inference 组成的完全自托管后台 agent 系统，使用 FP8 版本的 GLM-5.2 运行，并强调速度与对关键基础设施的控制权。原帖内容不长，但明确给出了工具栈与部署方式。

Type: Integration | Date: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [OpenCode + Fireworks 降本迁移](https://x.com/SeekingN0rth/status/2071484711327985696) (by [@SeekingN0rth](https://x.com/SeekingN0rth))

**如果你想测试只换 open-model harness 是否已经足够，可以用这个案例，因为作者把个人 coding 和 loop task 迁到 Fireworks 上的 GLM-5.2 + OpenCode 后，称 token 成本降到了三分之一，而且日常质量没有明显掉档。**

SeekingN0rth 表示，他在一个周末里把个人 coding 和 loop task 迁到了 Fireworks 上的 GLM 5.2 + OpenCode，token 花费大约降到原来的三分之一。帖子认为真正决定体验的是 harness，而不是是否绝对前沿：OpenCode 的终端体验接近 Claude Code，日常任务没有感到明显质量下滑，而且这种换模型路径同样适用于那些更看重成本而不是极致 SOTA 的企业场景。

Type: Evaluation | Date: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Hermes MoA 的 GLM 聚合器工作流](https://x.com/IBuzovskyi/status/2071601107944571249) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**如果你愿意为高价值 agent 回合多做一层编排，可以用这个案例，因为 Hermes Agent 的 MoA 设置把 GLM-5.2 和其他模型组合后，在帖子里的 demo 中用很小的增量成本换来了更好的输出。**

IBuzovskyi 把 Hermes Agent 的 Mixture of Agents 模式解释为：一个拥有 tool access 的 aggregator 模型，加上若干只提供私有建议的参考模型。帖子给出了一次 coding 测试：单独用 GLM 5.2 花了 13 分钟、0.38 美元；改成 GLM 5.2 聚合 Kimi K2.6 和 MiniMax M3 后，花了 35 分钟、0.47 美元，但动画更顺滑、视觉更好、游戏机制也更干净。帖子还补充了 preset 设计、功能入口，以及什么场景值得承担额外延迟。

Type: Integration | Date: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Cline 推理开关带来的 Harness 差值](https://x.com/akshay_pachaar/status/2071638409022763292) (by [@akshay_pachaar](https://x.com/akshay_pachaar))

**如果你想判断决定结果的是 harness 还是权重本身，可以用这个案例，因为同一个 GLM-5.2 在同一批 coding task 上，仅仅打开 reasoning，结果就从 57.3% 跳到 68.5%。**

akshay_pachaar 引用了一个 Cline 测试：同样的 GLM 5.2、同样的 coding task，一次关闭 reasoning，结果是 57.3%；一次开启 reasoning，结果是 68.5%。这条帖子用这个差值说明，当目标是产出可交付代码而不只是文本时，上下文延续、工具可达性、编辑应用方式和验证 loop，可能和底层模型本身一样重要。

Type: Evaluation | Date: 2026-06-29

<a id="case-136"></a>
### Case 136: [光标 + Fireworks 455M-Token 现场测试](https://x.com/robinebers/status/2071246749210190132) (by [@robinebers](https://x.com/robinebers))

**如果你想判断 GLM-5.2 是否足以作为严肃的 Cursor 日常默认模型，可以用这个案例，因为作者报告了 4.55 亿 token 的真实使用量、快速的 Fireworks 服务体验，以及暂时不想切回 Opus 或 GPT-5.5。**

robinebers 表示，在 Cursor 里切到搭配 Fireworks 的 GLM 5.2 之后，短短 36 小时就改变了他对这个模型的看法。帖子特别点出它支持图像、宣称零数据保留、吞吐大约在每秒 80-100 tokens，以及 4.55 亿 tokens 大约花费 145 美元。这使它成为比泛泛 benchmark 夸赞更扎实的 harness 场景评测，也提供了一个很具体的证据：provider 选择会显著改变实际使用体验。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Devin 桌面安全带，具有技能便携性](https://x.com/lily_gpupoor/status/2071297351801794850) (by [@lily_gpupoor](https://x.com/lily_gpupoor))

**如果你觉得 Z.ai 自家的 coding surface 不稳定，想在 Devin Desktop 里测试 GLM-5.2，可以用这个案例，因为作者报告了更容易迁移 skill、更高速度和更好的可 hack 性。**

lily_gpupoor 表示，在一段 API 不稳定时期，通过 Devin Desktop 重度使用 GLM-5.2 的体验，明显好于直接使用 Z.ai 的 coding plan。帖子强调了三个具体工作流收益：GLM 成功编辑了自定义 Solarized Green 主题 JSON 并顺利注册扩展、Devin 体感速度异常快，以及之前构建的 skills 在从默认 Windsurf Cascade agent 切换到 Devin Local 后大多都能继续沿用。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Pi 内联 GLM 审阅者](https://x.com/xpasky/status/2070831715518460177) (by [@xpasky](https://x.com/xpasky))

**如果你想在 Pi 风格的 coding-agent loop 里加入第二位审阅者，可以用这个案例。作者表示，GLM-5.2 可以逐回合给 Opus 提建议，成本增幅大约只有 10%。**

xpasky 表示，Pi 用户可以照搬一种 OMP 风格的模式，让第二个模型审阅每一回合，并把建议内联注入。帖子特别提到，GLM 5.2 会持续盯着 Opus，两个模型还会明显“拌嘴”，而额外这位 GLM reviewer 平均只会让 Opus API 成本增加约 10%。因此，这更像是一种具体的多模型监督模式，而不是完整的模型替换方案。

Type: Integration | Date: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [AgentRouter 一次成型 Telegram Bot](https://x.com/MatinSenPai/status/2070259817818812701) (by [@MatinSenPai](https://x.com/MatinSenPai))

**如果你想测试 GLM-5.2 在 one-shot coding-agent build 里，是否能主动补上偏向生产环境的 defaults，而不是只写出最低限度可运行的路径，可以用这个案例。**

MatinSenPai 表示，他用视频里相同的 prompt，让 GLM 5.2 一次完成了一个 Telegram bot，而且模型还主动补上了一些没有明说的实务细节。帖子特别提到，模型会在发送视频后自动清理文件、会考虑 Telegram Bot API 的大小限制并设置默认 50 MB cap、会在结束前反复 self-test，整体 structure 也比之前的 MiMo build 更干净。作者还补充，这次通过 AgentRouter 的执行大约用了 140K tokens、约 5 美元。

Type: Demo | Date: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go 重构首轮取胜](https://x.com/vedovelli74/status/2069889605969592500) (by [@vedovelli74](https://x.com/vedovelli74))

**用这个案例评估 GLM-5.2 在 OpenCode 中处理中等规模 Go 重构任务的表现，而不是只看 benchmark 宣传。**

vedovelli74 报告了自己第一次用 OpenCode 处理一个中等规模 GoLang 代码库重构，称 GLM-5.2 比 Opus 4.8 更快、更省 token，而且在第一轮就正确判断了需要重构的部分。作者还补充说，后续又用 Codex 和 Opus 做了交叉验证，但最终交付质量仍然是 GLM-5.2 更胜一筹。

Type: Evaluation | Date: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Claude Code + Cursor 默认运行成本 3.36 美元](https://x.com/clairevo/status/2069828122640548204) (by [@clairevo](https://x.com/clairevo))

**用这个案例判断 GLM-5.2 是否适合作为 Claude Code 和 Cursor 的日常默认模型，再决定是否把更多自主编码工作迁移到开放权重模型上。**

clairevo 表示，GLM 5.2 已经成为她在 Claude Code 和 Cursor 里的默认模型，目前累计成本只有 3.36 美元，同时却给出了类似 Opus 的编码体验。帖子还提到了通过 OpenRouter 的接入路径、前端设计感受，以及一项长时自主任务评测，这些都是它最终说服作者切换默认模型的原因。

Type: Evaluation | Date: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 上手演示与作品展示
<a id="case-229"></a>
### Case 229: [Hyperagent 个人主页作品集对决](https://x.com/arsh_goyal/status/2077764207945416949) (by [@arsh_goyal](https://x.com/arsh_goyal))

**如果你想在真实 browser-based agent 任务里比较 GLM-5.2 和其他 open model，可以看这个案例，因为 arsh_goyal 把 GLM 5.2、DeepSeek V4、Kimi K2.6 和 Qwen 3.7 并排放到 Hyperagent 上，用公开资料自动生成个人作品集。**

arsh_goyal 说，每个模型都在一台带真实 browser 的独立 cloud machine 上运行，先读取作者的 YouTube、LinkedIn 和 X 资料，再从同一条 one-line prompt 生成网站。帖子还公开了每次 run 的 cost 和 duration，并在回复里附上了 video 和 prompt，因此这比普通 screenshot 或 leaderboard repost 更接近一条真正可复现的 hands-on 对比。

Type: Demo | Date: 2026-07-16

---
<a id="case-218"></a>
### Case 218: [用 OpenCode 重建作品集与操作系统](https://x.com/MarkSShenouda/status/2077032282141978842) (by [@MarkSShenouda](https://x.com/MarkSShenouda))

**如果你想衡量 GLM-5.2 在更有野心的 OpenCode build 里的表现，可以看这个案例，因为 MarkSShenouda 说，OpenCode Go 加上 GLM-5.2 帮他重建了一个作品集网站，以及一个用 C 和 Assembly 编写、能跑在 WASM 或 Qemu emulator 里的真实操作系统。**

这条帖子把 GLM-5.2 绑定到两个已经做出来的成果，而不是玩具 demo：一个重建后的作品集网站，以及一个用 C 和 Assembly 实现、目标环境是 WASM 和 Qemu 的操作系统项目。虽然 tweet 本身很短，但它附带的两个预览链接已经足够把它变成一条更大规模 maker 式 coding 工作的具体 showcase。

类型: 演示 | 日期: 2026-07-14

---
<a id="case-213"></a>
### Case 213: [LlamaCoder v4 GLM 重构](https://x.com/nutlope/status/2076722464671793184) (by [@nutlope](https://x.com/nutlope))

**如果你想围绕 GLM-5.2 的规划和设计优势，原型化一条 one-prompt app generation 工作流，可以看这个案例，因为 nutlope 表示，LlamaCoder v4 已围绕 GLM 5.2 重构，改进了解析与规划，并且现在在一套免费开源 stack 上直接交付 WebAssembly renderer。**

nutlope 表示，LlamaCoder v4 现在以 GLM 5.2 为中心，把 UI 层切到 Base UI with shadcn，改进了解析、规划和 app 设计，并新增了一个基于 WebAssembly 的 renderer。这个项目被描述为免费、开源、由 Together 驱动，所以它是一条已经交付的具体 demo，而不只是对模型质量的主观看法。

Type: Demo | Date: 2026-07-13

---

<a id="case-202"></a>
### Case 202: [命令代码太空射击游戏功能获胜](https://x.com/CommandCodeAI/status/2075264795817972107) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**如果你想看 GLM-5.2 在 one-shot 交互式 UI build 里的表现，可以看这个案例，因为 Command Code 把同一个 retro space-shooter prompt 跑在 Fable 5、GPT 5.5、GLM 5.2 和 DeepSeek V4 Pro 上，并把 GLM 排在 features 第一。**

Command Code 说，同一个 `/design` prompt 在四个模型上都做出了相近的 retro pixel-art space-shooter 布局，但 GLM 5.2 在声音、控制、关卡节奏和整体 UX 等 features 上特别突出，而且成本只有 $0.07，对比 Fable 5 的 $0.80。它更像是一个轻量 game/UI build 的实战对比，而不只是 benchmark 截图。

Type: Evaluation | Date: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [ZCode 任天堂 DS 模拟器](https://x.com/0xSero/status/2074870153267818638) (by [@0xSero](https://x.com/0xSero))

**如果你想看一个长时程、本地执行的 coding build，可以看这个案例，因为作者让 GLM-5.2 在 4x RTX 6000 的 ZCode 里，从零开始用 C++ 去做一个 Nintendo DS 模拟器。**

原帖展示的是 GLM-5.2 在四张 RTX 6000 GPU 的 ZCode 环境里运行，并给了一个非常明确的目标：不要用现成模拟器，而是从零开始用 C++ 做一个 Nintendo DS emulator，并一直做下去直到 Mario 64 DS 的 ROM 能跑起来。这就让它成为一个真正有硬终点的 coding-agent demo，而不是泛泛的“做了个小玩具应用”。

Type: Demo | Date: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [命令代码 Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**如果你想看 GLM-5.2 在轻量设计类小游戏任务里的性价比，可以看这个案例，因为作者用同一个 Flappy Bird prompt 跑了 Command Code，最后认为 Fable 5 虽然价格接近 GLM-5.2 的 9 倍，但在 UX 上并没有明显更好。**

帖子说，这次实验对 DeepSeek V4 Pro、GLM 5.2 和 Fable 5 使用了同一个游戏 prompt，以及同一套 Command Code `/design` 设置。GLM 5.2 的价格处在 DeepSeek 和 Fable 之间，但作者认为 Fable 并没有展示出足以证明价格差的 UX 优势，所以这是一条很具体的 UX 对成本比较，而不是泛泛的 arena 说法。

Type: Evaluation | Date: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [REAP NVFP4 魔方一击](https://x.com/RoundtableSpace/status/2072700573145788914) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想测试 GLM-5.2 在单一 prompt 的互动式 build 任务上的表现，可以看这个案例，因为 REAP-NVFP4 的 demo 说它只靠一个 prompt 就做出了 3D Rubiks Cube、真实 scramble、实时状态和 solve 按钮。**

RoundtableSpace 说，GLM-5.2-REAP-NVFP4 只收到一个 HTML prompt，就返回了一个可运行的 3D Rubiks Cube app，里面有实时状态、真实 scramble 逻辑和 solve 动作。帖文没有公开太多代码，但它依然是一个很具体的 one-shot build demo，而不是泛泛的 benchmark 截图。

Type: Demo | Date: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [OMP 中继 iPhone 客户端](https://x.com/mov_axbx/status/2072192903762288721) (by [@mov_axbx](https://x.com/mov_axbx))

**如果你想把一个本地 GLM-5.2 agent 很快包进移动端界面，可以看这个案例，因为作者说 Codex 的 build-ios-app plugin 只用了几个小时，就给一个已经接了 GLM-5.2 和 Cloudflare 隧道的 OMP relay 做出了成品感很强的 iPhone 客户端。**

mov_axbx 说，他想给一个本地托管的 OMP agent 做个手机 app，于是用了 Codex 的 build-ios-app plugin，几个小时内就拿到了比较完整的版本。后端路径则是一个用 GLM-5.2 和 OMP 写的自定义 relay，Cloudflare 负责隧道。

Type: Demo | Date: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [开源 DevRel 研究 Agent](https://x.com/Astrodevil_/status/2071572680470655253) (by [@Astrodevil_](https://x.com/Astrodevil_))

**如果你想把 GLM-5.2 从通用聊天模型变成垂直研究助手，可以用这个案例，因为作者做了一个开源 DevRel agent，能把产品和受众输入转成带证据和提纲的选题列表。**

Astrodevil_ 用 GLM-5.2 做了一个 chat-first 的 DevRel 研究应用：输入产品和受众简介后，它会去 Hacker News 搜需求信号、去 DEV 找内容缺口，再通过 Engram memory 更新事实，最后返回带证据和提纲的排序选题。帖子还点明了技术栈：Agno、Weaviate Engram、Nebius inference，以及一个开源代码库。

Type: Demo | Date: 2026-06-29

<a id="case-123"></a>
### Case 123: [Recast 六版本落地页迭代流程](https://x.com/nutlope/status/2070199649818779914) (by [@nutlope](https://x.com/nutlope))

**如果你想先用 GLM-5.2 生成多个版本，再把最佳结果交给 coding agent 继续做，以低成本试作 landing page，可以用这个案例。**

nutlope 描述了一个围绕 GLM 5.2 与 Recast 的 web iteration workflow：先用同一个 prompt 生成 6 个 landing page 版本，挑出最好的 design，下载那份 code，再交给另一个 coding agent 继续迭代。作者表示，GLM-5.2 在这个场景里表现很好，因为它又快、又便宜，而且很有 design sense；同样的预算通常可以做出 3 到 6 个 GLM 版本，才相当于 Opus 4.8 生成 1 个页面的成本。

Type: Tutorial | Date: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [可玩的密室一击](https://x.com/aimlapi/status/2066996493257408639) (by [@aimlapi](https://x.com/aimlapi))

**使用此案例来比较 GLM-5.2 和 Opus 4.8 之间相同提示的游戏构建输出、运行时间和成本。**

AI/ML API 报告要求 GLM-5.2 和 Opus 4.8 一次性制作一款可玩的 Backrooms 游戏。他们的帖子称，GLM-5.2 在 1 分 08 秒内以 0.37 美元的价格构建了更完整的机制，而 Opus 用了 2 分 14 秒以 1.94 美元的价格构建了更完整的机制。

Type: Demo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [三个真实的构建结果参差不齐](https://x.com/bridgemindai/status/2065840871929442319) (by [@bridgemindai](https://x.com/bridgemindai))

**将此案例用作警示演示集：在信任用于生产游戏或视频任务的模型之前测试多个真实构建。**

BridgeMind 在恐怖屋游戏、3D 潜行游戏和 Remotion 营销视频上测试了 GLM-5.2。这篇文章报告了好坏参半的结果，包括破坏的游戏逻辑，使其成为有用的接地限制信号。

Type: Evaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [ZCode 中的超级马里奥克隆](https://x.com/ivanfioravanti/status/2066272681406980208) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例来评估使用 GLM-5.2 和 ZCode 在多个修复和功能过程中进行的迭代游戏构建。**

作者通过创建超级马里奥风格的克隆来使用 GLM-5.2 测试 ZCode 3.0，然后在问题修复和功能添加五次迭代后分享结果。

Type: Demo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [月球登陆器竞赛](https://x.com/ivanfioravanti/status/2066193134984319173) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**使用此案例在交互式游戏类型任务上比较 GLM-5.2、MiniMax M3 和 Kimi K2.7 代码。**

这篇文章描述了 MiniMax M3、GLM-5.2 和 Kimi K2.7 Code 之间的月球着陆器竞赛，在返回本地模型开发之前使用视频结果作为实际基准。

Type: Evaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [一键设计竞技场创建](https://x.com/grx_xce/status/2066951779154374907) (by [@grx_xce](https://x.com/grx_xce))

**使用此案例来检查 GLM-5.2 可以从竞技场上下文中的单个设计提示生成什么。**

作者在 Design Arena 上分享了一个根据一个提示创建的 GLM-5.2 示例，用它来展示开放权重模型和封闭权重模型之间缩小的差距。

Type: Demo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [研究论文理解工作流程](https://x.com/askalphaxiv/status/2066996976445706745) (by [@askalphaxiv](https://x.com/askalphaxiv))

**使用此案例将 GLM-5.2 应用于包含上下文问题和跨论文参考的论文阅读工作流程。**

AlphaXiv 引入了 GLM-5.2 来理解研究论文，用户可以突出显示一个部分、提出问题并参考其他论文以了解上下文、比较和基准参考。

Type: Integration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [受限制的诗歌比较](https://x.com/emollick/status/2067056226337186146) (by [@emollick](https://x.com/emollick))

**在将 GLM-5.2 与寓言风格模型进行比较时，使用此案例将正确性与创意质量分开。**

伊森·莫里克 (Ethan Mollick) 称赞 GLM-5.2 Max 创作了一首正确的受限诗，同时指出《寓言》更有创意地将消失字母约束融入到诗歌主题中。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [设计感示例](https://x.com/0xSero/status/2067074877941796994) (by [@0xSero](https://x.com/0xSero))

**使用此案例作为轻量级视觉设计信号，然后使用您自己的提示和 UI 审查进行验证。**

作者表示他们很喜欢 GLM-5.2 的设计感，并分享了一个视觉示例。它可用作检查指针，而不是作为生产设计质量的独立证明。

Type: Demo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run 体素游戏单次生成](https://x.com/pseudokid/status/2068431546143649829) (by [@pseudokid](https://x.com/pseudokid))

**用这个案例高压测试 GLM-5.2 的单提示词游戏生成能力，再查看一个视觉元素较多的构建还需要哪些迭代修正。**

作者表示，首轮提示就生成出了大部分 Temple Run 风格的体素摩托游戏，之后只用少量补充轮次修正镜头和移动逻辑。帖子还提到 Z.ai 工具链可以生成截图和实机视频，帮助文本模型评估结果。

Type: Demo | Date: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go 单次生成案例集](https://x.com/LyalinDotCom/status/2068378281636982990) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**用这个案例在 OpenCode Go 里快速基准测试 GLM-5.2 的单次生成构建能力，再决定是否投入更开放式的 Agent 循环。**

作者展示了一组通过 OpenCode Go 完成的单次生成案例，包括太阳系 Web 应用、系统信息 Electron 应用，以及一个简单的探索小岛 Web 游戏。同一条帖子也表示，GLM-5.2 是他用过最强的开源模型，但还没有把它称作与最前沿闭源模型完全同级。

Type: Demo | Date: 2026-06-20

---

<a id="case-81"></a>
### Case 81: [太空侵略者一键构建](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**用这个案例测试 GLM-5.2 的单提示词游戏生成能力，并观察少量后续回合如何完成素材替换和轻量打磨。**

作者表示，GLM-5.2 用一个主提示词就生成了可玩的 Space Invaders 风格游戏，随后又用三轮后续提示完成 sprite 替换和 leaderboard 等小增强。这个公开结果更适合作为轻量游戏生成样例，而不是完整 benchmark。

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode 恢复实验室一次性](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**用这个案例快速原型化交互式 agent failure simulation；作者报告用大约 3.50 美元就一轮做出了可运行的 recovery lab。**

作者在输入一份 4,000 字分析和 Agents SDK 仓库后，用 OpenCode 搭配 GLM-5.2 构建了一个完全可交互的 recovery lab。帖文给出了 176k token 的运行、一轮成型的结果，以及打磨前端到端约 3.50 美元的成本。

Type: Demo | Date: 2026-06-21

---


<a id="case-92"></a>
### Case 92: [打开设计参考 URL 重建](https://x.com/OpenDesignHQ/status/2069046584134778995) (by [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**如果你想测试 GLM-5.2 在参考驱动网页复刻上的能力，可以用这个案例。只给一个源 URL 和一条提示词，就几乎像素级复现了网站。**

Open Design 表示，它在内置 AMR 中只使用一个参考 URL 和一条简单提示词测试了 GLM-5.2，演示里模型几乎完美重建了原网站。这个案例更适合作为参考式 UI 生成的上手证明，而不是完整 benchmark。

Type: Demo | Date: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [交易台成本质量测试](https://x.com/atomic_chat_hq/status/2069171121044513273) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**如果你想比较 GLM-5.2 在全栈 UI 构建上的表现，可以用这个案例。它做出的交易终端效果接近最精致的结果，但成本只有头部结果的一小部分。**

Atomic Chat 用同一条实时 Trader Desk 构建提示，比较了四个模型，任务包含前端、后端、8 个交易标的的市场数据，以及自定义深色主题 UI。帖子称，GLM-5.2 消耗 13,677 token，成本 0.03 美元；Fugu Ultra 则是 22,225 token，成本 0.51 美元。帖子认为，GLM 以远低得多的成本做出了一个同样相当完整、带实时数据的多面板界面。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [克劳德拒绝后的勒德分子游戏](https://x.com/atmoio/status/2069559053114577088) (by [@atmoio](https://x.com/atmoio))

**如果闭源模型因策略原因拒绝请求，而你又想原型化带策略敏感性的游戏概念，可以用这个案例测试 GLM-5.2。**

atmoio 表示，Claude 把一个关于摧毁 AI 的幽默版 Plague Inc 风格游戏请求判定为违反可接受使用政策，因此作者改用 GLM 5.2 做出了名为 Luddite 的游戏，并附上了 demo 片段。这个案例更适合被看作创意编码任务在闭源模型拒绝后的实操替代路径，最终可玩性仍应自行检查。

Type: Demo | Date: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 供应商与工具集成
---
<a id="case-258"></a>
### Case 258: [Orbit Provider 50% GLM 接入](https://x.com/orbiteditor/status/2079148011259916552) (by [@orbiteditor](https://x.com/orbiteditor))

**如果你想在 Orbit 里试用 GLM-5.2，同时不自己管理单独的 provider 凭证，可以看这个案例，因为 Orbit Editor v0.4.0 说其新的 Orbit Provider 会把 GLM-5.2 直接暴露在编辑器里，并以 50% 折扣上线。**

Orbit Editor 的 v0.4.0 发布引入了一层面向开源模型的内置 provider，目标是把单独设置 API key 和 provider 的工作，收敛到一个编辑器工作流里。帖文表示，用户可以在一个界面里选择模型、开始编码、跟踪用量并管理成本，而 GLM-5.2 则以 5 折价格上线。因此，这是一条很具体的编辑器集成与访问路径，适合那些想低摩擦试用 GLM 的团队。

Type: Integration | Date: 2026-07-20

---
<a id="case-256"></a>
### Case 256: [pen.dev 并行设计评测](https://x.com/tomkrcha/status/2079253857834828230) (by [@tomkrcha](https://x.com/tomkrcha))

**如果你想在同一套本地工作流里，把 GLM-5.2 和偏设计导向的同类模型并排比较，可以看这个案例，因为 tomkrcha 说 pen.dev 能让 GLM 5.2 和 ChatGPT、Claude、Cursor Composer、OpenCode Go、Kimi、Grok、Gemini、Qwen 等模型一起并行运行，直接在桌面 codebase 上做设计任务。**

tomkrcha 把 pen.dev 描述为一层实时设计 agent surface，而不是单模型 demo。帖文表示，开发者可以直接登录自己已有的 ChatGPT 或 Claude 订阅，接入 Cursor Composer、GitHub Copilot、OpenCode Go、Grok 4.5、Kimi、MiniMax、GLM 5.2、Gemini、Qwen，再把它们混搭到同一个本地项目里的前端设计任务上。因此，这更像是一个面向 UI-heavy 工作的 GLM-5.2 横向评测界面，而不是另一张孤立的 benchmark 截图。

Type: Integration | Date: 2026-07-20

<a id="case-239"></a>
### Case 239: [TokenRouter 免费 GLM API 窗口](https://x.com/meliasiih/status/2078180641468985564) (by [@meliasiih](https://x.com/meliasiih))

**如果你想拿到一个限时免费的 GLM-5.2 API 路径，可以看这个案例，因为 meliasiih 说 TokenRouter 在 2026 年 7 月 25 日前提供免费访问，并给出了清晰的注册流程、API key 路径和公开 base URL。**

meliasiih 给出了一条很实操的接入路径：先用 email 或 X 注册，完成账号验证，生成 API key，选择 GLM-5.2，然后把客户端指向 `https://api.tokenrouter.com/v1`。帖文还明确写出这轮免费访问活动会持续到 2026 年 7 月 25 日，因此这是一条可以马上执行的 time-boxed hosted-access note。

Type: Tutorial | Date: 2026-07-17

---
<a id="case-238"></a>
### Case 238: [Agentuity 上的 Wafer GLM 网关](https://x.com/wafer_ai/status/2078186124258984374) (by [@wafer_ai](https://x.com/wafer_ai))

**如果你想把 GLM-5.2 接入 Agentuity gateway stack，可以看这个案例，因为 wafer_ai 说其 serverless 路径已经在 Agentuity 上提供 GLM 5.2 regular / Fast，两档都带 1M context，速度约 100 到 250 tok/s。**

wafer_ai 表示，目前市场上最快的 serverless GLM 5.2 路径已经上线 Agentuity AI Gateway，并且由 Wafer 提供 regular 与 Fast 两个 variant。这个帖子给出的不只是 availability，而是更可执行的部署画像：大约 100 到 250 tokens per second，以及 regular / Fast 两档都提供 1M-token context。

Type: Integration | Date: 2026-07-17

---
<a id="case-232"></a>
### Case 232: [Macroscope Check Run GLM 代理](https://x.com/kayvz/status/2077810181904494631) (by [@kayvz](https://x.com/kayvz))

**如果你想在保留 check-run workflow 的同时压低 PR review agent 成本，可以看这个案例，因为 kayvz 说 Macroscope 的 Check Run Agents 现在可以直接从常规 `.md` repo 配置里选用 GLM 5.2。**

kayvz 说，新的 model options 会直接出现在配置 check-run `.md` 文件的地方，因此这比单纯 availability 帖子更接近真实集成面。thread 也明确把 pull request 里的 custom code-review agents 当作使用场景，所以对于已经通过 Macroscope 跑 review automation、但想加入 open-weight 选项的团队来说，它是一条很具体的 integration surface。

Type: Integration | Date: 2026-07-16

---
<a id="case-231"></a>
### Case 231: [Aster 281 TPS 研究代理 API](https://x.com/asterailabs/status/2077556435085574429) (by [@asterailabs](https://x.com/asterailabs))

**如果你想 benchmark 一个高速 hosted GLM-5.2 endpoint，可以看这个案例，因为 asterailabs 说 Aster Inference 把来自 research-agent 优化的 API 路由以 281 tokens per second 提供给 GLM 5.2。**

Aster 把自己的产品定位为一条由 AI research agents 打磨出来的 inference API，并给出了具体 throughput 数字，而不是只说 launch 口号。帖子写到 GPU 上 gpt-oss-120b 可达 644 tps、GLM 5.2 可达 281 tps，同时还说公司会把研究系统里的 inference 经验直接回灌到产品改进里，因此这条路径很适合那些想先比 hosted provider，而不是直接从零开始 self-hosting 的团队。

Type: Integration | Date: 2026-07-16

---
<a id="case-230"></a>
### Case 230: [TrueFoundry 原生 Wafer GLM 路由](https://x.com/wafer_ai/status/2077837999514214456) (by [@wafer_ai](https://x.com/wafer_ai))

**如果你想把 GLM-5.2 接进现有 TrueFoundry AI Gateway stack，可以看这个案例，因为 wafer_ai 说这条 native provider integration 从 GLM 5.2 和 GLM 5.2 Fast 开始，而且不需要改动网关其余部分。**

wafer_ai 说，已经在用 TrueFoundry AI Gateway 的团队，可以在不调整 stack 其他部分的前提下直接接入 Wafer models。rollout 从 GLM 5.2 和 GLM 5.2 Fast 起步，帖子还把 Wafer 定位为最快的 serverless GLM route，因此这条信息比普通“已支持某模型”的公告更像一条具体的 managed-access path。

Type: Integration | Date: 2026-07-16

<a id="case-225"></a>
### Case 225: [TogetherLink Codex Harness 桥接](https://x.com/nutlope/status/2077432463685554558) (by [@nutlope](https://x.com/nutlope))

**如果你想把 GLM-5.2 跑进现有 coding-agent CLI，可以看这个案例，因为 nutlope 说 TogetherLink 是一个开源 CLI，能让 Codex 和 Claude Code 直接调用 GLM 5.2 这类 open model。**

这条发布把 TogetherLink 定位成一层 bridge：开发者可以继续使用自己熟悉的 coding harness，同时把底层模型切到 open-weight stack。帖子明确点名支持 Codex 和 Claude Code，并把项目描述成 open source，因此它不是泛泛的可用性消息，而是一条很具体的接入路径，适合那些想试 GLM-5.2、但不想放弃现有 terminal workflow 的团队。

Type: Integration | Date: 2026-07-15

---
<a id="case-224"></a>
### Case 224: [Vorflux 开放模型 Harness 路由](https://x.com/vorfluxai/status/2077449967711760587) (by [@vorfluxai](https://x.com/vorfluxai))

**如果你想在不写自定义胶水代码的前提下，把 GLM-5.2 接进完整 agent session，可以看这个案例，因为 vorfluxai 说它的 Open Model Harness 会把 GLM 5.2 分配给 design、build 和 simplify 步骤，同时保留 Vorflux 其余流程不变。**

vorfluxai 说，这套 harness 提供了一个下拉切换，可以把整段 session 切到 open models，同时保留 Vorflux 原本的 planning、subagents、pull requests 和 testing 流程。已公开的路由表里，DeepSeek V4 Pro 负责 main、plan 和 review，DeepSeek V4 Flash 负责 explore，GLM 5.2 负责 design、build 和 simplify，Kimi 2.7 Code 负责 debug 和 testing；这让它成为一条非常具体的多模型 agent 编排模式，而不是普通的“已支持”公告。

Type: Integration | Date: 2026-07-15

---
<a id="case-170"></a>
### Case 170: [NVIDIA 免费 API 即插即用访问](https://x.com/hqmank/status/2072855265612030010) (by [@hqmank](https://x.com/hqmank))

**如果你想通过免费 hosted endpoint 快速试用 GLM-5.2，可以看这个案例，因为 hqmank 表示 NVIDIA 已开放 OpenAI 兼容的 API 路径，而且确认可以直接 plug-and-play 接上。**

hqmank 表示，GLM-5.2 已上线 NVIDIA 的免费 API，并且在快速 hands-on 测试中可以正常运行。贴文将它描述为 OpenAI 兼容且可 plug-and-play，但也提醒免费 tier 往往会在需求升高后收紧限制。这让它成为一个适合快速评估或临时 agent routing 的实用 access note。

Type: Integration | Date: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [Free Workers AI 编码代理路线](https://x.com/ClaudeCode_UT/status/2072881775408456066) (by [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**如果你想为 coding agent 建立一条零成本的 GLM-5.2 路线，可以看这个案例，因为这篇教程用 OpenAI 兼容的 `cf/zai-org/glm-5.2` endpoint，把 Workers AI 接到 Claude Code、OpenCode、Cursor 和 Aider。**

ClaudeCode_UT 给出六个步骤：建立免费 Cloudflare 账号、复制 Workers AI 的 account ID、签发 API token、在 OpenAI 兼容工具中加入 Cloudflare provider、选择 `cf/zai-org/glm-5.2`，然后开始运行 Claude Code、Cursor、Aider 或 OpenCode。对于想先测试 coding-agent workflow、再决定是否承担 token 计费的团队来说，这是一个很实用的 access tutorial。

Type: Tutorial | Date: 2026-07-03

---

<a id="case-220"></a>
### Case 220: [OpenMed 去标识临床代理](https://x.com/MaziyarPanahi/status/2077000157103898789) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想把 GLM-5.2 放进一条更注重隐私的临床 agent 流程里，可以看这个案例，因为 MaziyarPanahi 说，在 OpenMed 本地去标识、Gemma 4 负责结构化之后，GLM 5.2 完成了整例的规划、工具调用和 disposition 编写。**

MaziyarPanahi 描述的是一套完全开放的 workflow：OpenMed 在设备端完成去标识，Gemma 4 抽取结构，GLM-5.2 则在脱敏文本上负责 agentic 医疗推理。最关键的运行细节是原始病历从未离开本机，这使这条 thread 成为一条很具体的医疗隐私与 tooling 模式，而不只是泛泛的模型背书。

类型: 集成 | 日期: 2026-07-14

---
<a id="case-219"></a>
### Case 219: [Katana 的 USDC GLM 接入路径](https://x.com/imgn_ai/status/2077061568068465148) (by [@imgn_ai](https://x.com/imgn_ai))

**如果你想通过一条 wallet 原生的按次付费路径接入 GLM-5.2，可以看这个案例，因为 imgn_ai 说 Katana 在 Base 上通过 x402 提供 GLM-5.2，不需要账号，使用 USDC 结算，并公开了可直接集成的 llms.txt。**

imgn_ai 把 Katana 描述成一条由 x402 驱动的接入路径：开发者复制服务的 llms.txt、连接钱包，就能以批发价调用 frontier 文本、图像或视频模型。帖子明确写到不需要账号，而且支付是按请求用 USDC 结算，所以它是一条很具体的 access 方案，适合那些不想维护长期 SaaS 账号的实验。

类型: 集成 | 日期: 2026-07-14

---
<a id="case-214"></a>
### Case 214: [Databricks AI Gateway GLM 路由](https://x.com/QCXINT_/status/2076490318695088218) (by [@QCXINT_](https://x.com/QCXINT_))

**如果你想在 agent tooling 里测试一条托管式且响应很快的 GLM-5.2 接入路径，可以看这个案例，因为 QCXINT_ 表示，Databricks AI Gateway 提供了组织专属 base URL 和 token 流程，暴露出一条速度非常快、看起来支持 1M context 的 GLM 5.2 路由，但后端身份仍未确认。**

QCXINT_ 给出了一套很具体的设置流程：创建 Databricks workspace，打开 User Settings，创建带 AI Gateway scope 的 access token，复制组织专属的 AI Gateway base URL，然后从 OpenClaw 或 Hermes 这样的 agent tools 调用暴露出来的 endpoint。帖子说，目前测试里只看到了 GLM-5.2，这条路由速度快得有些异常，而且看起来支持最高 1M context；但作者也明确提醒，他还没有确认 gateway 背后是否真的是它所宣称的那个精确 GLM-5.2 模型。

Type: Integration | Date: 2026-07-13

---

<a id="case-208"></a>
### Case 208: [打开分子查看器代理堆栈](https://x.com/MaziyarPanahi/status/2075913552854933869) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想把 GLM-5.2 接入一条开放的科学检视 workflow，可以看这个案例，因为 MaziyarPanahi 把经由 Hugging Face Inference Providers 的 GLM-5.2，和跑在 llama.cpp 上的 Qwen3-VL、Mol*、PydanticAI 串在一起，用单个 prompt 就把 EGFR 加 erlotinib 的结构 render 并做出评论。**

MaziyarPanahi 描述了一套完全开放的 stack：GLM-5.2 通过 Hugging Face Inference Providers 充当语言核心，Qwen3-VL 通过 llama.cpp 负责视觉检查，Mol* 负责把结构 render 出来，而 PydanticAI 协调 agent layer。贴文说，这条 workflow 以 RCSB PDB 的 EGFR 加 erlotinib 示例为核心，用单个 prompt 产出六个 render，因此它不是单纯的可用性公告，而是一条具体的多工具科学 agent 集成案例。

Type: Integration | Date: 2026-07-11

---
<a id="case-204"></a>
### Case 204: [困惑顾问 WANDR 成本基准](https://x.com/perplexity_ai/status/2075229779716973030) (by [@perplexity_ai](https://x.com/perplexity_ai))

**如果你想估算 GLM-5.2 在 routing 式 computer-use harness 里的成本结构，可以看这个案例，因为 Perplexity 说它的 GLM 5.2 加 advisor 配置在 WANDR 上是 2.1x，而 Opus 是 6.1x，整体 benchmark 成本也接近一半。**

Perplexity 说，它是以 GLM 5.2 作为 baseline 来衡量每任务成本，而在 WANDR 上，GLM 5.2 加 advisor 的路线是 2.1x，Opus 则是 6.1x。这可以视为一个很具体的 open-weight-first computer agent routing 信号：不是每一步都跑更贵的 closed model，而是用更便宜的 GLM 核心配合选择性升级。

Type: Evaluation | Date: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [同事开放工件路由](https://x.com/coworkerapp/status/2075233366266310905) (by [@coworkerapp](https://x.com/coworkerapp))

**如果你想把 GLM-5.2 放进企业 artifact 工作流，可以看这个案例，因为 Coworker 说 Open Artifacts 能做 docs、decks、PDF、spreadsheets、dashboards 和 apps，而且 optimized router 能把 token 使用量压到约 5 分之 1，同时仍提供美国托管的 GLM 5.2。**

Coworker 说，Open Artifacts 可以生成 docs、decks、dashboards、spreadsheets、PDF 和完整 apps 这类可分享成果物。同一篇 launch 帖子也说，它的 optimized mode 会为每个 task 挑选合适模型，把 token 消耗压到大约五分之一，同时仍让团队在美国托管、SOC 2、connector 丰富的环境里使用 GLM 5.2。

Type: Integration | Date: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [DotCode 上下文上传工作流程](https://x.com/stagedhappen/status/2074775356867789241) (by [@stagedhappen](https://x.com/stagedhappen))

**如果你想在私有 coding sandbox 里给 GLM-5.2 更多项目上下文，可以看这个案例，因为 DotCode 给 GLM 5.2 加上了 screenshot、图片、CSV、PDF、源码文件和 zip 上传，并把这些都接进同一条 filesystem + terminal 工作流。**

DotCode 说，GLM 5.2 现在已经能配合 contextual workspace uploads 使用，agent 可以检查文件、浏览项目结构、编辑代码、运行 terminal 命令，并且在同一个 sandbox 里连续工作。帖子列出了支持的输入类型，也写出了从 prompt + files 到 sandbox execution 的流程，把这件事定义成朝“基于真实项目上下文的 coding agent 工作”迈出的一步。

Type: Integration | Date: 2026-07-08

---
<a id="case-221"></a>
### Case 221: [SGLang TopK-V2 的 B300 agentic 服务](https://x.com/lmsysorg/status/2077076059657548127) (by [@lmsysorg](https://x.com/lmsysorg))

**如果你想 benchmark GLM-5.2 在长上下文 agent workload 上的生产服务能力，可以看这个案例，因为 lmsysorg 说，SGLang 在 8xB300、batch size 1 下达到了每用户 500+ tok/s，同时把单用户交互性提升了 18% 到 34%。**

这条 deep dive 帖子说，这些测量来自真实的 multi-turn agentic coding workload，并把收益归因于两部分：一是 GLM-5.2 自身对 IndexShare 和 KVShare 友好的架构，二是 SGLang 新的 TopK-V2 kernel。帖子还声称该 kernel 在 80K ISL 时快 2.33 倍，在 1M ISL 时可扩展到 10.17 倍，因此它比普通的 launch note 更像一条强有力的 deployment 参考。

类型: 评测 | 日期: 2026-07-14

---
<a id="case-215"></a>
### Case 215: [llm-d H200 Prefix-Cache 路由](https://x.com/RedHat_AI/status/2076725768034398513) (by [@RedHat_AI](https://x.com/RedHat_AI))

**如果你想在 H200 上 benchmark GLM-5.2 的托管 serving economics，可以看这个案例，因为 RedHat_AI 表示，llm-d 的 Wide EP 加 prefix-cache 路由，让一条 700B+ 的 GLM-5.2 路线实现了超过 90% 的 cache reuse、低于 3 秒的 TTFT，以及每百万输出 token 约 2 美元的成本。**

Red Hat AI 指向 robertshaw21 在 vLLM Office Hours 上的拆解，展示一条运行在 H200 上的 700B+ GLM-5.2 部署。帖子把这条路由超过 90% 的 cache reuse 和低于 3 秒的 TTFT 归因于 llm-d Wide EP 与 prefix-cache-aware routing，同时还给出了约每百万输出 token 2 美元、而托管 API 为 4.40 美元的对比。这使它成为一条很具体的 production-serving 参考，适合拿来比较自管路由 stack 与直接使用托管模型的成本。

Type: Integration | Date: 2026-07-13

---

<a id="case-209"></a>
### Case 209: [Colibri 25GB RAM 稀疏流媒体](https://x.com/techNmak/status/2075872446197158361) (by [@techNmak](https://x.com/techNmak))

**如果你想理解本地 GLM-5.2 实验的新下限，可以看这个案例，因为 techNmak 详细说明 Colibrì 如何靠从 NVMe 串流 experts，用大约 25GB RAM 跑起 744B MoE，不过最小配置只有大约 0.05 到 0.1 tok/s。**

techNmak 把 Colibrì 总结成一个纯 C 的本地 inference engine：只把持续会用到的 hot weights 留在 RAM，把路由到的 experts 放在 NVMe，上线后大约有 9.9GB 常驻、聊天时 RAM 峰值约 20GB，而 int4 权重大约占 370GB 磁盘。贴文也明确把这件事定位成 systems proof of concept，而不是快速的 production serving，因为 25GB 机器上的 cold generation 只有大约 0.05 到 0.1 tok/s，而且 int4 量化对质量的影响还没有被完整 benchmark。

Type: Demo | Date: 2026-07-11

---
<a id="case-206"></a>
### Case 206: [SGLang NVFP4 生产吞吐量](https://x.com/sgl_project/status/2075721488456654861) (by [@sgl_project](https://x.com/sgl_project))

**如果你想估算 GLM-5.2 NVFP4 的正式生产 SGLang serving 规模，可以看这个案例，因为官方 SGLang v0.5.15 release 说它现在在 8x B300 上可达每位用户 500+ tok/s，在 4x GB300 上则是 450 tok/s，batch size 为 1。**

SGLang v0.5.15 的官方公告表示，这一轮 release cycle 主要在做 GLM-5.2 NVFP4 的 production tuning。帖子指出，在 bs=1 下，8x B300 可达每位用户每秒 500 多 token，4x GB300 则可达 450 token/s。对正在评估 hosted 或 self-managed inference stack 的团队来说，这是一个很具体的 deployment throughput 检查点。同一则公告也把这项工作定位为 upstream 产品支持，而不是一次性的实验室 hack。

Type: Evaluation | Date: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Dahl 100M 免费 GLM 端点](https://x.com/pengsonal/status/2074908680106180669) (by [@pengsonal](https://x.com/pengsonal))

**如果你想走一条不用绑卡、又兼容 OpenAI 的路径来试 GLM-5.2，可以看这个案例，因为 Dahl Inference 给 GLM 5.2 FP8 提供了 1 亿免费 tokens，并且写清了如何建 key、如何调用 `/v1/chat/completions`。**

帖子把 GLM 5.2 FP8 列进了 Dahl 的免费开源模型 endpoint，并说不需要注册也不需要银行卡。它还给出了一条很具体的配置流程：在 web UI 里生成 key，使用兼容 OpenAI 的 `/v1/chat/completions` endpoint，同时提醒直接用 `curl` 可能会撞上 Cloudflare 403，但 web chat 这条路是能用的。

Type: Tutorial | Date: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [NVIDIA 免费端点 GLM 设置](https://x.com/undefinedKi/status/2074491917333655948) (by [@undefinedKi](https://x.com/undefinedKi))

**如果你想在不 self-hosting 的情况下把 GLM-5.2 接进 coding tools 里测试，可以看这个案例，因为原帖给出了一条免费的 NVIDIA endpoint 路线，直接把 GLM-5.2 的 API key 用到 Claude Code、Cursor 或 Cline。**

帖子说，NVIDIA 放出了包括 GLM-5.2 在内的多款顶级模型免费 API key，并给出了一条直接的配置路径：创建 NVIDIA 账号，打开某个 free endpoint 模型的 Build 页面，生成 API key，然后把 base URL 和 key 粘贴到 Claude Code、Cursor 或 Cline 里。所以这是一条很实用的 access tutorial，让你不用按 token 计费，也不用本地 GPU 栈，就能试用 GLM-5.2。

Type: Tutorial | Date: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [0G TeeML 私有推理路由](https://x.com/0G_labs/status/2074496704959676682) (by [@0G_labs](https://x.com/0G_labs))

**如果你想把 GLM-5.2 接到一条更注重隐私的 provider 路线上，可以看这个案例，因为 0G 说 GLM 5.2 已经跑在 TeeML 上，prompts 被封装在 TEE enclave 里，而且价格低于官方路线。**

0G 把 TeeML 定义成自己的 private inference 层，并表示 GLM 5.2 现在可以在 trusted execution environment 里进行可验证执行。虽然帖子很短，但它同时提供了具体的 provider integration，以及 privacy 和 pricing 角度，所以更适合作为一条部署路线信号，而不是模型质量结论。

Type: Integration | Date: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [DuckDB Flock 的 Open-SQL PR](https://x.com/lhoestq/status/2074143736624275629) (by [@lhoestq](https://x.com/lhoestq))

**如果你想把 GLM-5.2 带进完全开源的本地 SQL analysis，可以看这个案例，因为 lhoestq 说，一个 duckdb + flock 的 PR 已经让 GLM-5.2 进入 100% open-source 的数据栈。**

帖子说，作者开了一个 PR，把 GLM-5.2 接进 duckdb 和 flock，并把它描述成一种把 frontier 级 open intelligence 直接用于数据工作的方式。因为这里的来源是“PR 已开”而不是“已经 merge 的 release note”，所以它更适合作为本地 analytics 和 SQL-native workflow 的 integration-in-progress 信号。

Type: Integration | Date: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [一键26款API接入](https://x.com/Alan_Earn/status/2073663239028924680) (by [@Alan_Earn](https://x.com/Alan_Earn))

**如果你想先通过单一 OpenAI 兼容 provider 试用 GLM-5.2，可以看这个案例，因为 Alan_Earn 说一把 API key 就能访问 GLM-5.2 和另外 25 个模型，还带 26 美元起始 credits。**

这条帖子给出了一条很短的 setup：注册账号、加卡、解锁 dashboard、领取 credits、生成 API key，然后把它粘到 Codex、Cursor、OpenCode、OpenClaw、Hermes 等客户端里。帖子也写明这是 pay as you go，而且大模型会很快吃掉免费额度，所以它更适合作为 access 与 pricing 说明。

Type: Tutorial | Date: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [NVIDIA NIM OpenCode 思维设置](https://x.com/Dracoshowumore/status/2073384581256929717) (by [@Dracoshowumore](https://x.com/Dracoshowumore))

**如果你想通过 NVIDIA 免费 NIM endpoint 把 GLM-5.2 接进 OpenCode，并且走一条明确开启 thinking 的零成本路线，可以看这个案例，因为 Dracoshowumore 分享了 API key 流程、base URL，以及一份由工具层接管 function calls、让 GLM 以 enable_thinking=true 运行的 OpenCode 配置。**

Dracoshowumore 把整套配置路径讲得很清楚：先在 NVIDIA developer platform 注册、生成 GLM-5.2 API key、把 OpenCode 指向公开的 base URL、关闭模型原生的 tool calling，并在 provider options 里传入 chat_template_kwargs.enable_thinking=true。同一篇贴文还指出，NIM 这条路默认不会暴露 function calling 或 reasoning traces，所以工具编排必须由 OpenCode 接手。这使它成为一条实用的 configuration note，而不只是又一条免费 endpoint 公告。

Type: Tutorial | Date: 2026-07-04

<a id="case-165"></a>
### Case 165: [通过移动代理控制启动 ZCode](https://x.com/Digiato/status/2072663459850829985) (by [@Digiato](https://x.com/Digiato))

**如果你想把 ZCode 当成 GLM-5.2 的官方 coding surface 来评估，可以看这个案例，因为 launch report 说这个免费的 agentic IDE 会上 Windows、macOS、Linux，还能通过 Telegram、WeChat、Feishu 跟踪项目进度。**

Digiato 把 ZCode 描述成一个围绕 GLM-5.2 建立的免费 agentic development environment，定位上对标 Cursor、Claude Code 和 Copilot。帖文说它支持 Windows、macOS、Linux，与 GLM-5.2 深度集成，并能通过 Telegram、WeChat、Feishu 查看项目进度。这让它比一般的模型上线公告更有实际接入价值。

Type: Integration | Date: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [OpenWiki 自动维护代理文档](https://x.com/LangChain/status/2072745455788933321) (by [@LangChain](https://x.com/LangChain))

**如果你想让 agent 可读的文档自动保持最新，可以看这个案例，因为 LangChain 说 OpenWiki 会随着代码变化重建并维护 repo docs，而且能跑在 GLM 5.2 这类开源模型上。**

LangChain 把 OpenWiki 描述成一层面向 coding agent 的开源文档维护工具。帖文说它把 open harness 和 open CLI workflows 结合起来，会在 codebase 变化时更新文档，并且能跑在 GLM 5.2、Kimi K2.7 这类开源模型上。对于想让 agent 读到最新 repo docs、而不是依赖人工维护 wiki 的团队来说，这是一个很实用的 file-based memory 模式。

Type: Integration | Date: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [通过 FireConnect 铸造 PTU](https://x.com/FireworksAI_HQ/status/2072407689964183867) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**如果你想在不重写 agent 客户端的前提下，把 GLM-5.2 接到企业级 Foundry 预算里，可以用这个案例，因为 Fireworks 说 FireConnect 能把 Microsoft Foundry 的 PTU 接到 Codex、OpenCode 和 Pi 工作流中。**

Fireworks 表示，GLM 5.2 已经上线 Microsoft Foundry。启用 FireConnect 后，团队可以一边消耗 Foundry PTU，一边继续从 Codex、OpenCode 或 Pi 发请求，而不必为每个 agent 入口单独搭一套模型接入路径。

Type: Integration | Date: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Braintrust GLM 评估工作台](https://x.com/ankrgyl/status/2072042305108722040) (by [@ankrgyl](https://x.com/ankrgyl))

**如果你想把 GLM-5.2 和 Opus 放进同一套 eval 栈里比较，可以用这个案例，因为 Braintrust 联合 Baseten 给出了一个带长上下文成本与精度对照的接入样例。**

ankrgyl 表示，Braintrust 已把 GLM-5.2 接进平台，并由 Baseten 提供支持，团队可以直接在 eval 和 production trace 中跑这个模型。示例比较了 25K 与 50K tokens 的长上下文检索：Opus 4.8 大约高 3.5 分，但每条 trace 的成本约高 4.1 到 4.5 倍。

Type: Integration | Date: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [ClinePass 开放权重模型统一订阅](https://x.com/iam_elias1/status/2071655509611151674) (by [@iam_elias1](https://x.com/iam_elias1))

**如果你想把多个开放权重 coding model 收拢到同一个 agent harness 里，可以用这个案例，因为 ClinePass 把 GLM-5.2 和相关模型打包成统一月付，而不是分别维护 provider key 和账单。**

iam_elias1 把 ClinePass 描述成一个月费 9.99 美元的入口，让 GLM-5.2、DeepSeek、Kimi、Qwen、MiniMax、MiMo 等开放权重模型直接进入 Cline 的 IDE 扩展和 CLI。帖子称它可以替代分散的 provider API key，提供 2-5 倍标准 API 限额，还能在同一会话里按编码阶段切换模型，并且通过 CLI 注册首月只要 1.99 美元。

Type: Integration | Date: 2026-06-29

<a id="case-137"></a>
### Case 137: [面向编码代理的免费 GLM API 服务](https://x.com/mcwangcn/status/2071261128575897901) (by [@mcwangcn](https://x.com/mcwangcn))

**如果你想在 Hermes 或其他 coding agent 里无注册测试 GLM-5.2，可以用这个案例，因为共享服务会发放短时有效的 API key，整体接入足够轻量。**

mcwangcn 分享了一个免费的 GLM-5.2 API 服务，据称无需注册或登录，就能从 Lobster、Hermes 或其他 coding agents 直接调用。帖子还说，每个生成的 API key 有效期为一小时，到期后需要续领；这是一条很具体的 anti-abuse 约束，也意味着这项服务更适合快速验证工作流，而不是无人值守的长期生产使用。

Type: Integration | Date: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [OpenCode Go 可用性](https://x.com/opencode/status/2067207923122479242) (by [@opencode](https://x.com/opencode))

**使用此案例通过文本、1M 上下文和类似 GLM-5.1 的定价来跟踪 OpenCode Go 工作流程中的 GLM-5.2 可用性。**

OpenCode 宣布 GLM-5.2 在 Go 中可用，强调文本支持、1M 上下文窗口以及与 5.1 相同的定价。

Type: Integration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [奥拉马云可用性](https://x.com/ollama/status/2066949797316350361) (by [@ollama](https://x.com/ollama))

**使用此案例将 GLM-5.2 路由到 Ollama Cloud 中，以进行可访问的开源编码模型实验。**

Ollama 宣布推出 GLM-5.2，将其描述为具有 1M 上下文的长视野编码和代理任务模型。

Type: Integration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API 调用访问](https://x.com/OpenRouter/status/2066941552208056561) (by [@OpenRouter](https://x.com/OpenRouter))

**在比较提供商路由或多模型堆栈时，使用此案例通过 OpenRouter 访问 GLM-5.2。**

OpenRouter 宣布 GLM-5.2 作为 1M 代币长期模型可用，为用户提供了一个与提供商无关的调用路径。

Type: Integration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM 零日支持](https://x.com/vllm_project/status/2066950636428775693) (by [@vllm_project](https://x.com/vllm_project))

**使用此案例通过 vLLM 自行托管或提供 GLM-5.2 服务，并提供零日支持。**

vLLM 项目宣布在 v0.23.0 中支持 GLM-5.2，将其定位为具有 1M 上下文的长视野编码代理的旗舰模型。

Type: Integration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [通过 Baseten 获得概念可用性](https://x.com/NotionHQ/status/2066963258985320550) (by [@NotionHQ](https://x.com/NotionHQ))

**使用此案例将 GLM-5.2 识别为 Notion 工作流程中可用的开放权重模型。**

Notion 宣布 GLM-5.2 作为开放权重模型推出，专为长期任务而构建，并通过 Baseten 提供服务。

Type: Integration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [烟花零日服务](https://x.com/FireworksAI_HQ/status/2067007200426680509) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**使用此案例来评估 Fireworks 作为需要托管基础设施的 GLM-5.2 工作负载的服务路径。**

Fireworks 在第 0 天宣布推出 GLM-5.2，强调 1M 上下文、编码优先定位以及在 SWE-Bench、Terminal-Bench、GPQA 和 AIME 上的独立验证。

Type: Integration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [谷歌云模型花园链接](https://x.com/CarolGLMs/status/2067127223216419088) (by [@CarolGLMs](https://x.com/CarolGLMs))

**使用此案例在面向 Google Cloud 的部署和代理平台上下文中查找 GLM-5.2。**

CarolGLMs 分享了 GLM-5.2 的 Google Cloud 链接，使其成为团队处理云模型目录的直接指针。

Type: Integration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [威尼斯隐私模式](https://x.com/AskVenice/status/2066990725439361251) (by [@AskVenice](https://x.com/AskVenice))

**当隐私模式、TEE 或端到端加密是尝试 GLM-5.2 的决定因素时，请使用此案例。**

Venice 宣布 GLM-5.2 在带有 TEE/E2EE 框架的隐私模式下可用，旨在实现私有代理编码和长期任务。

Type: Integration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [命令代码可用性](https://x.com/CommandCodeAI/status/2066950478194503990) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**使用此案例尝试命令代码中的 GLM-5.2，具有低成本入门计划和长上下文编码功能。**

Command Code 宣布 GLM-5.2 可用，并指出 1M 上下文、强大的推理、开源状态以及通过其一美元 Go 计划进行访问。

Type: Integration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [来自 Nous Portal 的赫尔墨斯特工](https://x.com/Teknium/status/2066954081575592282) (by [@Teknium](https://x.com/Teknium))

**使用此案例通过 Nous Portal 和 OpenRouter 将 GLM-5.2 连接到 Hermes Agent 工作流程。**

Teknium 报告了来自 Nous Portal 和 OpenRouter 的 Hermes Agent 中 GLM-5.2 的可用性，这对于代理框架路由实验非常有用。

Type: Integration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net 零日启动合作伙伴](https://x.com/ionet/status/2067140436095803763) (by [@ionet](https://x.com/ionet))

**在评估 753B 参数长上下文模型的计算支持服务时使用此案例。**

io.net 宣布自己是 GLM-5.2 的零日发布合作伙伴，强调 1M 上下文、代理优先设计、长视野编码以及 753B 参数模型的计算需求。

Type: Integration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [模块化云零日服务](https://x.com/clattner_llvm/status/2066974950293147950) (by [@clattner_llvm](https://x.com/clattner_llvm))

**使用此案例来考虑在提供商规模提供长上下文 GLM-5.2 服务的模块化云。**

Chris Lattner 发布称，GLM-5.2 在第 0 天就在 Modular Cloud 上上线，强调了开放权重、编码、长视野代理和 1M 上下文。

Type: Integration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [通过 OpenRouter 设置光标](https://x.com/agentnative_/status/2068148384846746107) (by [@agentnative_](https://x.com/agentnative_))

**使用此案例通过 OpenRouter 在 Cursor 中配置 GLM-5.2，以实现低成本的开放模型编码工作流程。**

源代码给出了具体的 Cursor/OpenRouter 设置路径，而不仅仅是宣布模型可用性。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [放大视觉设计的代理眼睛](https://x.com/beyang/status/2068087124818317374) (by [@beyang](https://x.com/beyang))

**当纯文本模型需要视觉审核支持来完成设计任务时，可以使用此案例将 GLM-5.2 与 Amp 自定义代理配对。**

该帖子将 GLM-5.2 视觉设计基准测试结果与可提供审查层的 Amp 插件代理连接起来。

Type: Integration | Date: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten 更快的一百万上下文服务](https://x.com/alphatozeta8148/status/2067852860499562821) (by [@alphatozeta8148](https://x.com/alphatozeta8148))

**当长上下文服务速度对于 Factory Droid、OpenCode 和编码工具很重要时，可以使用此案例通过 Baseten 路由 GLM-5.2。**

源报告 GLM-5.2 在完整的 1M 上下文中运行速度提高了四倍，并在编码工具中显示了它。

Type: Integration | Date: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [面向网页设计的 Browser Use QA 子代理](https://x.com/browser_use/status/2068405699340853541) (by [@browser_use](https://x.com/browser_use))

**当纯文本模型需要视觉检查和迭代式网站修复时，可用这个案例把 GLM-5.2 与 Browser Use v2 多模态 QA 子代理配合起来。**

Browser Use 表示，GLM-5.2 在一个网站设计任务中超过了 Fable 5，随后又加入 QA 子代理来检查结果、判断美感、查找 bug，并把定向修复建议回传给 GLM。整套 build 加 QA 的循环据称成本低于 0.75 美元。

Type: Integration | Date: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode 官方 IDE 每日免费额度](https://x.com/Alan_Earn/status/2068223665268006924) (by [@Alan_Earn](https://x.com/Alan_Earn))

**当你想要一个带大额每日免费 token、交互体验类似 Cursor 的官方编码 IDE 时，可用这个案例通过 ZCode 访问 GLM-5.2。**

帖子将 ZCode 描述为智谱官方编码 IDE，默认模型就是 GLM-5.2，并提供每日 300 万 token、100 万上下文窗口，以及 Mac 和 Windows 客户端。它还包含一段简短的上手流程，因此比普通的上线公告更具可操作性。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-83"></a>
### Case 83: [通过 Fireworks 设置光标](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**用这个案例通过 Fireworks 以最小 OpenAI 兼容配置把 GLM-5.2 接入 Cursor，无需写自定义客户端代码。**

Skirano 展示了最简 Cursor 配置流程：把 Fireworks key 填到 OpenAI API key 字段，base URL 用 `https://api.fireworks.ai/inference/v1`，模型选择 `accounts/fireworks/models/glm-5p2`，然后重启 Cursor。对于想在熟悉的 coding IDE 里试用 GLM-5.2 的人，这是一条很具体的接入路径。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI 提供商支持](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**用这个案例在开放 benchmark harness 中通过一等公民级别的 ZAI provider 支持和专用 API key 路径运行 GLM-5.2。**

VulcanBench v0.2.0 新增了一等公民级别的 ZAI 支持，让用户可以把 GLM-5.2 作为 `zai:glm-5.2` 与 OpenAI、Anthropic 模型并排运行，并配有独立的 `ZAI_API_KEY`。如果你要的是开放、可重复的 benchmark harness，而不是单张截图，这个案例更有用。

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode 高/最大推理变体](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**用这个案例在 OpenCode 中使用 GLM-5.2 的 High / Max reasoning 变体，同时获得更可靠的 step-limit 处理。**

OpenCode v1.17.9 为 GLM-5.2 新增了 High 和 Max thinking 变体，覆盖 OpenAI 兼容与 Anthropic 兼容 provider，并原生支持 OpenRouter 的 effort 映射。同一版本也修复了 agent step-limit 行为，让这个集成更适合更长的运行。

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai编码端点选择](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例把 GLM-5.2 coding plan 流量从通用 API 路径切到面向 coding 优化的 Z.ai endpoint。**

帖文建议，对于 coding plan 工作负载，应优先使用 `https://api.z.ai/api/coding/paas/v4`，而不是通用的 `https://api.z.ai/api/paas/v4/`。作者还补充说，Claude Code、OpenCode 等工具在支持时通常会走 `https://api.z.ai/api/anthropic`。如果你感觉 GLM-5.2 路由不对，这是一条很具体的配置修正。

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux 免费 GLM-5.2 API 设置](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**用这个案例获取免费的 GLM-5.2 API key 和 base URL，再接入 Claude、Cursor、Hermes 等工具。**

作者分享了一条大约五分钟的配置流程：获取免费的 ZenMux API key 与 base URL，然后把 GLM-5.2 接到 Claude、Cursor、Hermes 等工具上。帖文也提醒免费 tier 很快会触发 rate limit，所以它更适合作为 access note，而不是长期稳定性保证。

Type: Tutorial | Date: 2026-06-21

---


<a id="case-93"></a>
### Case 93: [本体 ncode GLM 默认值](https://x.com/_xjdr/status/2069030608727408993) (by [@_xjdr](https://x.com/_xjdr))

**如果你想把 GLM-5.2 接入 ncode 和 Noumena 风格的 agent 环境，并同时使用标准版与 1M 上下文端点以及默认模型支持，可以用这个案例。**

Noumena 的更新提到，团队已经在 tool calling、函数解析、应用路由和 reasoning trace 等链路上为 GLM 提供了一等支持。随后他们又把 API 拆分成 `glm-5.2` 和 `glm-5.2[1m]` 两个端点，用来在 1M 上下文高流量场景下控制 TTFT。更新还说，新的 ncode 版本在收到积极使用反馈后，已经把默认的 opus 级模型从 Kimi 切换成 GLM。

Type: Integration | Date: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [克劳德代码通过 Baseten](https://x.com/thealexker/status/2069163621469335757) (by [@thealexker](https://x.com/thealexker))

**如果你想通过 Baseten key、自定义 base URL 和 `~/.claude/settings.json` 里的模型映射，在 Claude Code 里运行 GLM-5.2，可以用这个案例。**

这篇教程演示了如何安装 Claude Code、创建 Baseten 账户、获取 API key，并编辑 `~/.claude/settings.json`，让三个 Claude 模型档位都通过自定义 Anthropic 环境变量指向 `zai-org/GLM-5.2`。这是一个把 GLM-5.2 作为 Claude Code 客户端替代模型接入的具体配置模式。

Type: Tutorial | Date: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi 代理默认值](https://x.com/cramforce/status/2069057402524082622) (by [@cramforce](https://x.com/cramforce))

**如果你想在安全 harness 中测试 GLM-5.2，可以用这个案例。`deepsec` 把它设成了 Pi agent 默认模型，并报告了有竞争力的 eval 结果。**

帖子宣布，`deepsec` 已支持 `@badlogicgames` 的 Pi agent，并把 GLM-5.2 设为默认模型，同时给出了可直接运行的命令 `pnpm deepsec process --agent pi`。作者还说自己跑了 Deepsec evals，结果与其他 frontier 模型相比也有竞争力，因此这是一个很具体的安全场景集成入口。

Type: Integration | Date: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid 安全带快速入门](https://x.com/RayFernando1337/status/2069523126384525639) (by [@RayFernando1337](https://x.com/RayFernando1337))

**如果你想通过 Baseten 和 Droid harness 快速跑通 GLM-5.2，并复用一套也适用于其他 IDE 的短配置流程，可以用这个案例。**

RayFernando1337 给出了一套带时间戳的教程步骤：获取 Baseten API key、自动化配置 Droid AI、测试 GLM-5.2 集成、查看替代配置与限制，最后再补充其他 IDE 的额外设置说明。

Type: Tutorial | Date: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI 兼容的 GLM API 工作流程](https://x.com/Marktechpost/status/2069308807570915500) (by [@Marktechpost](https://x.com/Marktechpost))

**如果你想在 Python 里用一个 OpenAI 兼容客户端统一接入 GLM-5.2 的推理控制、tool calling、长上下文检索和成本统计，可以用这个案例。**

Marktechpost 分享了一篇教程和配套代码 notebook，演示如何把 GLM-5.2 封装进一个 OpenAI 兼容客户端。帖子称，这套工作流覆盖 thinking effort 控制（`off`/`high`/`max`）、流式 reasoning 与 answer 通道、带多步 agent 的 tool calling、结构化 JSON 输出、长上下文检索，以及 token 成本追踪。

Type: Tutorial | Date: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API 搜索沙箱](https://x.com/perplexitydevs/status/2069252848647606584) (by [@perplexitydevs](https://x.com/perplexitydevs))

**如果你想把 GLM-5.2 接入 Perplexity 的 Agent API，并通过单个 API 调用获得带搜索能力的沙盒 agent，可以用这个案例。**

Perplexity Devs 宣布在 Agent API 中加入 GLM-5.2，并将其描述为适合长周期 coding 与 agentic workflow 的模型。帖子还特别强调了 Search as Code、OpenAI 兼容接口，以及不加价的一方定价。

Type: Integration | Date: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 的 280 TPS GLM 接口](https://x.com/aqaderb/status/2069220126272999501) (by [@aqaderb](https://x.com/aqaderb))

**如果你在意 provider 延迟表现，可以用这个案例查看 Baseten 对 GLM-5.2 高吞吐、低首 token 延迟的公开性能说法。**

aqaderb 宣布 Baseten 的 GLM-5.2 API 可达到 280 tokens per second，TTFT 低于 0.8 秒。帖子把结果归因于 PD disaggregation、结合 multi-token prediction heads 的 speculative decoding、KV-cache-aware routing 等服务优化，并附上了一篇工程说明文章。

Type: Integration | Date: 2026-06-23

---

<a id="case-128"></a>
### Case 128: [Cloudflare Workers AI OpenCode 设置](https://x.com/RoundtableSpace/status/2070820686243959276) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**如果你想在不自备模型主机的情况下，通过 Cloudflare Workers AI 这条免费的 OpenAI 兼容路线运行 GLM-5.2 做 coding agent，可以用这个案例。**

RoundtableSpace 表示，你可以先注册一个免费的 Cloudflare account，复制 Account ID，创建 API token，再把 Cloudflare 作为 provider 加进 OpenCode，并指定模型 `@cf/zai-org/glm-5.2`。帖子还说，这条路线同样适用于 OpenCode、Cursor、Aider、Hermes Agent、Claude Code 等其他 OpenAI 兼容工具，是一条相当实用的 coding agent 托管接入捷径。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Puter.js 零配置浏览器客户端](https://x.com/FareaNFts/status/2070848321212792945) (by [@FareaNFts](https://x.com/FareaNFts))

**如果你想在接触 API key、账单或后端配置之前，先用纯浏览器原型测试 GLM-5.2，可以用这个案例。**

FareaNFts 表示，Puter.js 通过一个 CDN script tag 就能在客户端暴露 GLM 系列模型，`z-ai/glm-5.2` 可以直接在浏览器代码里调用，不需要服务器，也不需要开发者侧的计费配置。帖子把它定位成个人工具、vibe coding app 和轻量 agent 的快速原型路径，同时也说明了代价：Puter 使用的是 user-pays 的浏览器模式，并不适合高吞吐的生产流量。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [SiliconFlow 统一端点接入](https://x.com/FareaNFts/status/2070900056736379288) (by [@FareaNFts](https://x.com/FareaNFts))

**如果你想把 GLM-5.2 放进更大的多模型栈里，可以用这个案例，因为帖子描述了一个带 free trial credit 的单一 OpenAI 兼容 SiliconFlow endpoint，同时覆盖中文和西方模型。**

FareaNFts 表示，SiliconFlow 通过一个 OpenAI 兼容 endpoint，同时提供 GLM-5.2、DeepSeek、Qwen、Llama 4、Hunyuan、Mistral、Yi、Gemma、Phi 等 200 多个模型。帖子还提到，注册就送 1 美元 free credit、无需绑卡、部分模型持续免费、支持 spending limit，并且这套 key 可以直接塞进 Cursor、Claude Code、Aider 等工具里。

Type: Integration | Date: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [HuggingChat 建站到 HF Space 部署](https://x.com/victormustar/status/2070190742991994967) (by [@victormustar](https://x.com/victormustar))

**如果你想在几乎免费的 personal-site flow 里试用 GLM-5.2，从 HuggingChat 搜集资料到部署到 Hugging Face Spaces，都可以参考这个案例。**

victormustar 表示，只要有 Hugging Face account，就有足够的 free credits 可以在 HuggingChat 里让 GLM-5.2 帮你建网站，并由 Exa 补足关于用户的背景 research。帖子还提到，最终生成的网站可以免费部署成 static Hugging Face Space，对于 personal site 实验来说，是一条非常具体而且低成本的路线。

Type: Tutorial | Date: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [DigitalOcean Inference Engine 上线](https://x.com/digitalocean/status/2070177703911719301) (by [@digitalocean](https://x.com/digitalocean))

**如果你想通过 managed infrastructure 获得官方 provider access，而不自己托管 1M context 的模型，可以用这个案例接入 GLM-5.2。**

DigitalOcean 宣布在自家的 Inference Engine 上提供 GLM-5.1 和 GLM-5.2，并将它定位为适合长达 8 小时的 agentic coding workflow、拥有 1M-token context window 的模型。帖子也把这条路线描述成一种可直接接入现有 stack 的方案，具备 usage-based pricing 与 fully managed infrastructure。

Type: Integration | Date: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Command Code Fast 120-250 Tok/S 档位](https://x.com/CommandCodeAI/status/2069891896881857016) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**如果你更在意长周期编码任务的响应速度，而不只是最低入门价格，可以用这个案例接入更快的 GLM-5.2 档位。**

Command Code 宣布上线 GLM-5.2 Fast，称这是一个保持同样 frontier coding 定位、但速度提升到 120-250 tokens per second 的高吞吐版本。帖子还提到，这个档位保留了 1M 上下文、tool use 和 reasoning，并且从 1 美元 Go plan 加 10 美元 usage credits 起就能使用。

Type: Integration | Date: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [Vercel AI 网关快速 GLM-5.2 API](https://x.com/wafer_ai/status/2069869501190152528) (by [@wafer_ai](https://x.com/wafer_ai))

**如果你需要 serverless 速度和明确的 token 定价，可以用这个案例通过 Vercel AI Gateway 接入 GLM-5.2 Fast。**

wafer_ai 表示，GLM-5.2 Fast 已经上线 Vercel AI Gateway，速度为 150-250 tokens per second，上下文窗口为 1M token，标价为每 1M token 输入 3.00 美元、输出 10.25 美元、缓存 0.50 美元。对于优先考虑吞吐和网关定价可预期性的团队来说，这是一个很具体的托管接入信号。

Type: Integration | Date: 2026-06-24

---

<a id="cost-pricing-local-deployment"></a>
## 💸 成本、定价与本地部署
---
<a id="case-254"></a>
### Case 254: [8x GB10 860K 稀疏服务](https://x.com/light_foundry/status/2079158726658060652) (by [@light_foundry](https://x.com/light_foundry))

**如果你想 benchmark 基于 GB10 级集群的长上下文本地 GLM-5.2 服务，可以看这个案例，因为 light_foundry 说一套 8x GB10 配置，配合 sparse indexer 和 Int4-Int8Mix 权重，在 4K 深度下做到了 1,101 tok/s prefill，最高可服务到 860K tokens，并且在 845K context 仍然能找回 needle。**

light_foundry 描述的是一套把 8x GB10 集群迁移到统一 base 加 `b12x` sparse indexer 的配置，用来运行带 fp8 sparse-MLA KV 和 MTP 的 GLM-5.2 Int4-Int8Mix。帖文给出的数字包括：4K 深度下 prefill 从 880 提高到 1,101 tok/s，77K / 231K / 395K 深度下的 prefill 分别为 1,052 / 940 / 838 tok/s，单流 decode 中位数为 42.1 tok/s，以及一个可支持 860K 最大长度的 903K-token KV 池，并且在约 845K 深度下仍能以 10.9 tok/s 解码。帖文还特别指出两个很具体的运维陷阱：冷启动时的 inductor cache 编译看起来像 shared-memory hang，以及 GPU memory fragmentation 会在多次重启后压缩可用 KV。

Type: Evaluation | Date: 2026-07-20

---
<a id="case-253"></a>
### Case 253: [混合 3/4/8-Bit 本地权衡](https://x.com/0xSero/status/2079184434188685668) (by [@0xSero](https://x.com/0xSero))

**如果你想在退回 BF16 之前，先估算一条激进量化的本地 GLM-5.2 路线值不值得走，可以看这个案例，因为 0xSero 说一套混合 3/4/8-bit 配置，仍然在 Terminal-Bench 2.1 上做到 70.8%，在 GPQA Diamond 上做到 88.89%，在 4x RTX 6000 上约 82 tok/s，并把单任务成本压到约 0.22 美分。**

这条帖子把一套量化版 GLM-5.2-Hybrid 的评测与服务数据打包放在一起：Terminal-Bench 2.1 成绩为 70.8%，个别运行最高到 77.8%；GPQA Diamond 为 88.89%；在 4x RTX 6000 GPU 上约 1,200 tok/s prefill、约 82 tok/s decode，context 大约 340K，单任务成本约 0.22 美分。帖文还声称，它和 BF16 相比，在 Terminal-Bench 上只差 3 到 8 个点，在 GPQA 上只差 0.15，因此对于要判断为了降低本地 GLM 服务成本和内存占用，最多能接受多少质量损失的团队来说，这是一个非常具体的权衡参考。

Type: Evaluation | Date: 2026-07-20

---
<a id="case-251"></a>
### Case 251: [Ollama Pro 重负载 GLM 预算](https://x.com/iamcheyan/status/2078732985537601895) (by [@iamcheyan](https://x.com/iamcheyan))

**如果你想按 heavy-task quota，而不是标价，来估算 flat-rate GLM-5.2 subscription，可以看这个案例；iamcheyan 表示，OpenCode Go 的周配额大概只够约 5 次重型 GLM-5.2 任务，而 Ollama Pro 的周池则能支撑大约 3 天的持续 GLM 使用，价格是每月 20 美元，相对 OpenCode Go 的首月 5 美元、之后 10 美元。**

作者比较了两个 plan 各一个月的使用情况，并表示 GLM-5.2 会非常快地吃掉 OpenCode Go 的周进度条，快到只要一个饱和周就可能把月度 quota 用掉一半。同一条帖子也提到，Ollama Pro 虽然同样按周计量，但没有额外的月度 cap，因此更适合反复进行重负载 GLM session；而 OpenCode Go 则更适合较轻量的 flash-model 使用。这使它成为一条具体的 subscription 选型 caveat，而不是模糊的偏好。

Type: Limit | Date: 2026-07-19

---
<a id="case-249"></a>
### Case 249: [Alibaba 统一 Token 方案](https://x.com/alibaba_cloud/status/2078784690534670495) (by [@alibaba_cloud](https://x.com/alibaba_cloud))

**如果你想比较的是 multi-model 月费访问，而不是每个 provider 各自的余额，可以看这个案例；Alibaba Cloud 表示，Token Plan for Individuals 会把 text、image、video 工具的 unified credits 放进同一个池子，并把 GLM-5.2 列为其中的 frontier text model，coupon 后首月起价为 4 美元。**

Alibaba Cloud 的官方帖子把这个方案描述成覆盖各种 modality 的单一 plan，而不是只面向 coding 的 subscription。它明确打包了 text、image、video 的 unified credits，在 text 一侧列出 Qwen3.8-Max-Preview、GLM-5.2、DeepSeek-V4-Pro，并额外加入用于 video generation 的 Happy Horse 1.1。对于要比较固定月度 credit pool 与各 provider 分开计费的团队来说，这是一条具体的 access 与 budget 笔记。

Type: Integration | Date: 2026-07-19

---
<a id="case-246"></a>
### Case 246: [8x DGX Spark 400K 集群](https://x.com/thelichhh/status/2078316906335904205) (by [@thelichhh](https://x.com/thelichhh))

**如果你想判断桌边 GLM-5.2 集群何时能替代 hosted API 开支，可以看这个案例，因为 thelichhh 说 8 台 DGX Spark 被连成一台拥有 1TB unified memory 的机器，把 GLM-5.2 载入到所有节点后，以 400K context 跑起来了。**

thelichhh 说，这套 setup 一开始只是散在桌上的 8 台 DGX Spark，约 54 分钟后靠一次 networking fix 才真正变成单一集群。帖文也把这个 build 直接和 inference economics 连在一起：一位每月要管理约 5.2 万美元 API 账单的朋友，看完这套 400K-context 的 GLM 5.2 集群后，决定直接买硬件。对于正在权衡 cluster complexity 与 recurring API spend 的团队，这是一条具体的 scale-up 参考。

Type: Demo | Date: 2026-07-18

---
<a id="case-245"></a>
### Case 245: [Pulsar CPU Expert Lane](https://x.com/Giannisanii/status/2078430789075656904) (by [@Giannisanii](https://x.com/Giannisanii))

**如果你想测一套低 VRAM 的 GLM-5.2 本地堆栈，可以看这个案例，因为 Giannisanii 说 Pulsar 的 CPU expert lane 让 GLM-5.2 744B 在两张 16GB GeForce、一块 NVMe 和 32GB RAM 的机器上，从 1.6 tok/s 提高到最高 2.8 tok/s。**

Giannisanii 说，新的 CPU expert lane 会直接在 experts 已经位于的 host RAM 上计算，而不是再把那些字节经过 PCIe 送回 GPU。帖文声称，一个 AVX2 kernel 在 9900X 上达到 42 GB/s，高于 28.7 GB/s 的 bus cost，并回报 GLM-5.2 744B 在同一台机器上从 1.6 tok/s 拉到最高 2.8 tok/s，而且没有 quality cost。这是一条具体的本地部署优化笔记，而不是笼统的 open-model 称赞。

Type: Demo | Date: 2026-07-18

---
<a id="case-244"></a>
### Case 244: [Peezy Go 3K GLM 窗口](https://x.com/SerPepeXBT/status/2078503202346156194) (by [@SerPepeXBT](https://x.com/SerPepeXBT))

**如果你想用 request cap 而不是 token 计价来比较 flat-rate 的 GLM-5.2 coding access，可以看这个案例，因为 SerPepeXBT 说 Peezy Go plan 现在会重置 limits、每 5 小时给到最多 3,000 次 GLM 5.2 requests，价格仍是每月 10 美元，首月降到 5 美元。**

SerPepeXBT 说，provider 在一次故障后把所有人的 limits 归零，并重新公布 GLM 5.2 额度为每 5 小时 3,000 次 requests。帖文还补充，Go plan 仍是每月 10 美元、首月 5 美元，而且 native Mac app 已经推出。对于评估 subscription 型 coding surface、而不只是纯 API 计费的团队来说，这是一条具体的 hosted-access 与 pricing 笔记。

Type: Integration | Date: 2026-07-18

<a id="case-242"></a>
### Case 242: [ZenMux 249M Token Receipt](https://x.com/AstridWiegner/status/2077917345893511266) (by [@AstridWiegner](https://x.com/AstridWiegner))

**如果你想用账单回执而不是目录价格来核对 GLM-5.2 的真实经济性，可以看这个案例，因为 AstridWiegner 说一张 ZenMux Token Receipt 显示处理了超过 249M token，原始成本为 105.81 美元，最终总额却是 0 美元。**

AstridWiegner 表示，一张 ZenMux Token Receipt 记录了超过 2.49 亿个 GLM 5.2 token，起初显示成本为 105.81 美元，最终总额却降到了 0.00 美元。她把这类 receipt 视为比 benchmark score 更实用的比较面，因为它直接把输出质量、工作负载规模和固定预算实际能买到多少工作量联系在一起。

Type: Evaluation | Date: 2026-07-17

---
<a id="case-241"></a>
### Case 241: [Zro Pro 300M GLM 试用](https://x.com/AndarkFomo/status/2078092015368368574) (by [@AndarkFomo](https://x.com/AndarkFomo))

**如果你想用很小的预算测试 private hosted GLM-5.2 agent workflow，可以看这个案例，因为 AndarkFomo 说 Zro Pro 的 promo 大约用 1 美元就能换来约 300M 的 GLM-5.2 token，以及 OpenAI 兼容接入、EU 基础设施与 zero-retention 定位。**

AndarkFomo 说，Product Hunt 上的 PRODUCTHUNT promo 会给前 100 名用户一整个月的 Zro Pro 免费期，而这个服务正常价格是每月 20 美元；有些 checkout 甚至只会产生 1 美元的银行卡预授权。帖文还说明，这个 plan 提供面向 coding agents 的 private open-model inference，走 OpenAI-compatible API、部署在 EU infra 上、不用 prompts 做训练，同时也明确写出了 caveat：300M token 更像是 expected usage 而不是永久 hard cap、名额有限，且这条路径上的 GLM-5.2 提供 350K context。

Type: Tutorial | Date: 2026-07-17

---
<a id="case-240"></a>
### Case 240: [DGX Station 256K 桌面部署](https://x.com/TheAhmadOsman/status/2078247891370442867) (by [@TheAhmadOsman](https://x.com/TheAhmadOsman))

**如果你想估算桌面级 GLM-5.2 部署能力，可以看这个案例，因为 TheAhmadOsman 说 GLM 5.2 NVFP4 在 DGX Station 上以 256K context 跑出了约 3,000 tok/s prefill 和 32 tok/s decode。**

TheAhmadOsman 说，这次运行用的是带 FP8 KV cache 的 GLM 5.2 NVFP4，部署在一台 DGX Station 上，在 256K context length 下实现了约 3,000 tokens per second 的 prefill 和 32 tokens per second 的 decode。帖文也明确指出目前还不支持并发请求，但作为本地 long-context setup 的单机吞吐参考，这条数据已经足够具体。

Type: Demo | Date: 2026-07-17

---
<a id="case-234"></a>
### Case 234: [Jatevo 折扣 GLM 接入](https://x.com/JatevoId/status/2077770086228885536) (by [@JatevoId](https://x.com/JatevoId))

**如果你想快速掌握一条带公开定价的 hosted GLM-5.2 接入路径，可以看这个案例，因为 JatevoId 说其平台上 GLM 5.2 的 input 价格是 $1.40 / 1M、output 价格是 $4.40 / 1M，符合条件的 JTVO holder 还能拿到 50% 折扣。**

JatevoId 说，这次 rollout 还带有面向 holder 的分层 free-compute 配额，并在标准 per-token 定价之外公开给出 50% 的 discount policy。明确的 input / output 价格，让它即使在折扣适用条件依赖平台规则的情况下，依然是一条很具体的 access note，而不是模糊的 launch 帖子。

Type: Integration | Date: 2026-07-16

---
<a id="case-233"></a>
### Case 233: [MI325x 上低于 0.1 美分的 GLM 服务](https://x.com/picocreator/status/2077817481381728268) (by [@picocreator](https://x.com/picocreator))

**如果你想评估 AMD 硬件上的 self-hosted GLM-5.2 inference 成本，可以看这个案例，因为 picocreator 说 4xMI325x 配置把 GLM 5.2 跑到了 1,482 tok/s，成本低于每百万 token 0.10 美元。**

picocreator 说，这条 route 在四张 MI325x GPU 上实现了 1,482 tokens per second，成本大约是 B300s 的三分之一、Opus 的十分之一。它强调的不是 API 标价，而是专用硬件上实际跑出的 GLM capacity 成本，因此对于在评估 self-hosting economics 的团队来说，这是一个很有参考价值的 checkpoint。

Type: Demo | Date: 2026-07-16

---
<a id="case-226"></a>
### Case 226: [Bonsai Mac Studio 病历分诊](https://x.com/MaziyarPanahi/status/2077362554805117132) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**如果你想让一份很长的临床病历留在本地，同时让 GLM-5.2 在其上做推理，可以看这个案例，因为 MaziyarPanahi 说 GLM 5.2 通过 Mac Studio 上的 Bonsai 27B 分诊一份三年期病历，并找出了埋在 17 个月前的造影风险问题。**

MaziyarPanahi 说，292 次就诊记录都留在 Mac Studio 上的 Bonsai 27B 里，通过 llama.cpp、Metal、ternary weights，以及大约 7.2GB 的本地模型存储来处理；同时只允许 GLM-5.2 问三个问题，最后就定位到了 eGFR 39 条件下 metformin 与含碘造影剂并用的风险。帖子把这套架构明确描述为 privacy-preserving：病历从未离开机器，orchestrator 也从不接触原始病人数据，因此这是一条很具体的本地医疗 workflow，而不是泛泛的模型背书。

Type: Demo | Date: 2026-07-15

---
<a id="case-191"></a>
### Case 191: [Hermes 建立的 LiteLLM 本地实验室](https://x.com/ivanfioravanti/status/2074609005272375329) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想把 GLM-5.2 当作 coding agent 来搭一个本地 inference lab，可以看这个案例，因为原帖说 Hermes Agent + GLM-5.2 把 LiteLLM、Postgres、Prometheus 和 Grafana 都接在了一套 M3 Ultra 环境上。**

帖子说，LiteLLM 已经在一台 M3 Ultra 上跑起来了，并把一条基于 DGX Spark 的 Qwen 模型当作初始测试路由暴露出来。对这个 repo 更重要的是，作者明确说 Hermes Agent + GLM-5.2 完成了 LiteLLM、Postgres、Prometheus 和 Grafana 的搭建，所以这是一条很具体的本地实验室集成案例，覆盖 routing、持久化和 observability，而不只是泛泛夸赞。

Type: Integration | Date: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [双 M5 Max 离线无人机模拟器](https://x.com/XavierLocalAI/status/2073938465121833452) (by [@XavierLocalAI](https://x.com/XavierLocalAI))

**如果你想估算一套完全离线的 Apple Silicon GLM-5.2 agent 到底能做什么，可以看这个案例，因为 XavierLocalAI 报告了一个 753B 配置：在两台 128GB M5 Max 上以 26 tok/s 编写 droneship landing simulator。**

原帖说，这套配置使用的是 GLM-5.2 753B build、约 222GB 磁盘占用的 Unsloth dynamic IQ2_M quant、通过 Thunderbolt 5 连接起来、合计约 256GB pooled memory 的两台 M5 Max，以及 llama.cpp RPC。这里的结果不只是 throughput：模型当时正在完全离线地 live-coding 一个 Falcon 9 的 droneship landing simulator，所以它是一条很具体的本地部署与 privacy-first agent demo。

Type: Demo | Date: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x DGX Spark 生产线束](https://x.com/thatcofffeeguy/status/2074245620207058981) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**如果你想判断 5 节点 DGX Spark 配置是否已经够支撑生产级 GLM-5.2 工作，可以看这个案例，因为 thatcofffeeguy 报告了在 400K context 下单流约 13.9 tok/s，以及 3 条 lane 合计 19.9 tok/s 的 live harness 结果。**

帖子说，这是作者在多轮实验后跑出来的最佳配置，而且当天就已经在没有 pruning 的情况下上线生产。它对应的 workload 也比纯实验室测试更具体：这套 harness 已经被拿来在约 30 分钟内生成内容，并审查当天的 ERP 数据。所以它更像一条实用 deployment checkpoint，而不只是硬件炫耀。

Type: Demo | Date: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [M3 Ultra ds4-eval Q4 检查点](https://x.com/ivanfioravanti/status/2073742792044446194) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想用 ds4-eval 真正 benchmark 一台 Apple Silicon 单机上的 GLM-5.2，可以看这个案例，因为 ivanfioravanti 报告了一次 q4 运行：M3 Ultra 512GB 机器上约 16 tok/s，92 项里过了 76 项，总时长 8 小时 53 分。**

ivanfioravanti 说，这次 q4 的 ds4-eval 运行是在一台 M3 Ultra 512GB 机器上完成的，后面还会把旧 branch 用 batch inference 再跑一遍。这样一来，repo 里此前那个以视频为主的 M3 案例就多了一个更硬的配套证据：这条帖子给出了 pass 数和总运行时长，而不只是 throughput 片段。

Type: Evaluation | Date: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [4x RTX PRO 6000 构建指南](https://x.com/QingQ77/status/2073589933567094981) (by [@QingQ77](https://x.com/QingQ77))

**如果你想评估一套严肃的本地 GLM-5.2-594B 方案，可以看这个案例，因为 QingQ77 分享了一份完整的硬件与运维指南，核心是 4 张 RTX PRO 6000、通过 opencode 暴露的 API，以及给 agent 用的 sandbox VM。**

这份 guide 描述了一条更高预算的路线：用 4 张 RTX PRO 6000 和 384GB VRAM 跑 GLM-5.2-594B，同时配合二手 EPYC 和 DDR4。帖子还覆盖了 PCIe Gen4 交换、BIOS 的 bifurcation 与 ASPM、`iommu=off`、110V 线路下每卡 350W 限制、通过 opencode 暴露的 Docker container，以及保护宿主机的 sandbox VM。

Type: Tutorial | Date: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [4x DGX Spark QuantTrio 运行](https://x.com/Tech2Wild/status/2073637530960826787) (by [@Tech2Wild](https://x.com/Tech2Wild))

**如果你想估算 4 节点 DGX Spark 集群跑 GLM-5.2 QuantTrio 的上限，可以看这个案例，因为 Tech2Wild 给出了 200K context、单流 30 tok/s，以及 6 并发下总计 60.5 tok/s 的结果。**

Tech2Wild 说，这次最终量测保留了全部 256 个 experts，并使用了 k=4 的 MTP speculative decoding。和此前偏规划的 Spark thread 不同，这里给出的是已经跑完的本地推理结果：单流 30 tok/s，6 个并发请求合计 60.5 tok/s，并把集群目标上下文设在 200K。

Type: Demo | Date: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [单个 M3 Ultra 4 位视频运行](https://x.com/ivanfioravanti/status/2073502277449486460) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**如果你想估算 GLM-5.2 在 Apple Silicon 单机上的可行性，可以看这个案例，因为 ivanfioravanti 展示了在一台 M3 Ultra 512GB 机器上以约 16 tok/s 跑 4-bit 版本，并拿它和约 17 tok/s 的 q2 ds4-eval 视频做比较。**

ivanfioravanti 发了一段视频，展示 GLM 5.2 4-bit 在一台 M3 Ultra 512GB 机器上以约每秒 16 token 运行，并补充说 ds4-eval 的视频使用的是约每秒 17 token 的 q2 build。作者把它定位成仍在进行中的本地测试，但它依然提供了一个具体的 Apple Silicon 单机 throughput checkpoint，可以和 repo 里现有的 multi-M3 以及 oMLX 本地部署案例互相参照。

Type: Demo | Date: 2026-07-04

<a id="case-173"></a>
### Case 173: [AMD MI355X 2626 Tok/s 节点服务](https://x.com/wafer_ai/status/2073155792182907085) (by [@wafer_ai](https://x.com/wafer_ai))

**如果你想估算 AMD 硬件上的高吞吐 GLM-5.2 推理能力，可以看这个案例，因为 wafer_ai 表示 MI355X 达到每节点 2626 tok/s、单流 213 tok/s，而且成本比 Blackwell 低超过 2 倍。**

wafer_ai 表示，工程团队把 GLM 5.2 部署在 AMD MI355X 上后，每节点可达每秒 2626 token，single-stream 模式则为每秒 213 token。贴文把这个结果描述为大约达到 B200 吞吐的 80%，但成本却低超过 2 倍，因此对评估 NVIDIA 之外 open-weight 推理经济性的团队来说，是一个具体的 deployment reference。

Type: Demo | Date: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel 网关 287 Tok/s 无服务器](https://x.com/wafer_ai/status/2072861749104288074) (by [@wafer_ai](https://x.com/wafer_ai))

**如果你想估算 GLM-5.2 经过 serverless gateway 时的真实用户延迟，可以看这个案例，因为 wafer_ai 表示它的 GLM 5.2 Fast 路线不是只在 benchmark harness 中，而是在 Vercel AI Gateway 上跑到 287 tokens per second。**

wafer_ai 表示，它们的 GLM 5.2 Fast 路径在 Vercel AI Gateway 上达到每秒 287 token，并将这视为 serverless 部署下终端用户真正会看到的数字。这让它成为一个很好的桥梁，连接原始推理 benchmark 与更接近 production 的 hosted access，特别是当 gateway overhead 也会影响体验时。

Type: Demo | Date: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [一键 RTX PRO 6000 部署](https://x.com/XciD_/status/2073035324272328733) (by [@XciD_](https://x.com/XciD_))

**如果你想估算隔离式 hosted GLM-5.2 部署的最低门槛，可以看这个案例，因为 XciD_ 表示 GLM-5.2-NVFP4 现在可在 8x RTX PRO 6000 的 Inference Endpoints 上以每小时 22 美元 one-click 部署。**

XciD_ 表示，753B MoE 版本的 GLM-5.2-NVFP4 现已能在使用专属 8x RTX PRO 6000 instance 的 Inference Endpoints 上 one-click 部署。贴文强调每小时 22 美元的可预期价格、zero setup，以及 full isolation，因此对不想自行运维整套堆栈的团队来说，是一个具体的 hosted deployment reference。

Type: Integration | Date: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [5x ASUS GX10s 上的完整 744B](https://x.com/thatcofffeeguy/status/2072525885077434743) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**如果你想估一个极端 home-lab GLM-5.2 部署的规模，可以看这个案例，因为作者说完整 744B 模型已经能在 5 台 ASUS GX10 上带 full context 跑起来，而且已经接到处理真实 workload 的 causal harness。**

thatcofffeeguy 说，完整 744B 的 GLM-5.2 现在已经能在五台 ASUS GX10 系统上带 full context 运行，token rate 也比预期更好，整个 stack 已经接上 causal harness。帖文还没公布精确 throughput 数字，但它已经是一个很具体的公开证据，说明这类本地集群可以承载完整模型，而不只是缩减版。

Type: Demo | Date: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [中国堆栈中的代理路由交换](https://x.com/0xluffy_eth/status/2072548580183900430) (by [@0xluffy_eth](https://x.com/0xluffy_eth))

**如果你更在乎成本压力而不是绝对最高质量，想把 GLM-5.2 放进 mixed-model stack 的 agent 层，可以看这个案例，因为作者说把 Sonnet 换成 GLM-5.2 之后，这个 slot 的输入成本降到五分之一，质量大约只掉了 3%。**

这条 thread 列出了 reasoning、code generation、agent calls、batch work、image、video 六个路由变更。对 agent 层来说，作者把 Sonnet 换成 GLM 5.2，并表示性能大约下降 3%，但输入成本便宜了 5 倍。30 天总结则说，整体 AI 运营成本下降了 87%，而收入没有变化。

Type: Evaluation | Date: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [744B 本地硬件层](https://x.com/devjuninho/status/2072151237840007399) (by [@devjuninho](https://x.com/devjuninho))

**如果你想更现实地评估 GLM-5.2 的本地部署门槛，可以看这个案例，因为原帖说即便量化后，2bit 也大约要 239GB、4bit 大约要 466GB，所以 256GB 以上的 RAM 或 VRAM 才算比较实际的起步线。**

devjuninho 明确反对 open weights 就等于普通用户本地能轻松跑 的说法。帖子里说，GLM-5.2 大约是 744B 参数、其中约 40B 激活，2bit 估算约 239GB、4bit 约 466GB，因此想真正把它本地跑起来，更需要服务器级内存、充足 SSD 和耐心，而不是一台普通游戏 PC。

Type: Limit | Date: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [本地 NVFP4 Rust 端口速度为 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (by [@mov_axbx](https://x.com/mov_axbx))

**如果你想估算一套调优后的本地 GLM-5.2 部署在真实 coding 工作里能做到什么，可以用这个案例，因为作者报告了 140 tok/s 的 NVFP4 推理速度，以及几分钟内完成的 Python 到 Rust 全量移植。**

mov_axbx 报告说，一套运行在 OMP 上的本地 GLM-5.2 NVFP4 配置达到了每秒约 140 tokens。帖文还说，这个模型在大约 10 分钟内把一个 Python 卫星定位服务移植到 Rust，随后又在几分钟内搭出了一个 demo web app。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [B300 x2 代理主导的双栈启动](https://x.com/TheValueist/status/2071261052080148607) (by [@TheValueist](https://x.com/TheValueist))

**如果你想评估严肃的自托管 GLM-5.2 部署范围，可以用这个案例，因为线程展示了分析师在不到一天内就在裸金属 B300 上同时拉起了 vLLM 和 SGLang 的 NVFP4 推理。**

TheValueist 表示，一个 analyst-agent 工作流把 GLM 5.2 NVFP4 部署到了裸金属 NVIDIA B300 x2 集群上，并在 vLLM 与 SGLang 两套栈中都跑通了完整 benchmark suite，全部耗时不到 24 小时。线程还说，真正的限制因素是 HBM 容量而不是原始算力；当 KV cache 溢出时，DRAM 才会变得关键。因此，这更像是一条供团队评估本地推理经济性与硬件瓶颈的具体运维备注，而不只是硬件炫耀。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 超预填充加速](https://x.com/jundotkim/status/2071287585297887510) (by [@jundotkim](https://x.com/jundotkim))

**如果你想在最近的 kernel 工作之后重新判断 Apple Silicon 本地可行性，可以用这个案例，因为作者报告 M3 Ultra 512GB 上的 GLM-5.2 prefill 速度几乎翻倍，而且快速测试里没有明显质量崩塌。**

jundotkim 表示，oMLX 0.4.5.dev1 新增了自定义 MLX kernels，使 GLM-5.2-oQ4 在 32k prefill 场景下于 M3 Ultra 512GB 机器上的速度从 87.7 tok/s 提升到 174.4 tok/s，涨幅达到 98.9%。帖子也明确说这条路径仍然带实验性质，但无论是 needle-in-a-haystack 检查还是 Claude Code 风格的 coding tests，都没有看到明显回归，因此它更像是一条实用的本地推理更新，而不只是 release note。

Type: Evaluation | Date: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [20M 代币注册信用爆发](https://x.com/Bitbro4crypto/status/2071150218872283262) (by [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**如果你想判断官方注册赠送额度是否足以支持一次真正的 GLM-5.2 试用，可以用这个案例，因为帖子声称新账号可获 2000 万免费 token、无需绑卡，并提供完整 OpenAI 兼容访问。**

Bitbro4crypto 表示，当前 GLM 5.2 的注册路径会给出 2000 万免费 tokens、120 个图像与视频 credits、high 与 max thinking modes、1M context window，以及一个可直接接入 Cursor 或 Claude Code 等工具的 OpenAI 兼容 API，且无需订阅。可以把它视作一个非常具体的 access / pricing signal，用于短期试用判断，但也应假设这种促销额度随时可能变化。

Type: Integration | Date: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x DGX Spark 本地 GLM 操作手册](https://x.com/TraffAlex/status/2071020631072616698) (by [@TraffAlex](https://x.com/TraffAlex))

**如果你想判断 DGX Spark 集群是否是现实可行的本地 GLM-5.2 路线，可以用这个案例。整理出来的指南把具体硬件成本、集群拓扑和 vLLM 命令都对应到了 1M context 的 GLM 目标上。**

TraffAlex 汇总了社区验证过的经验和 NVIDIA 官方资料，表示每台设备售价为 4,699 美元，其他模型用 2x Spark 集群最合适，而 4x Sparks 可以在 1M-token context 下以每秒大约 20 tokens 的速度运行 GLM 5.2 NVFP4。帖子里还给出了 CX7 网络配置、passwordless SSH、NCCL 检查以及示例 vLLM Docker 命令，所以它更像一份可落地的本地 deployment playbook，而不是泛泛的硬件观点。

Type: Tutorial | Date: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [输出代币成本比较](https://x.com/Hesamation/status/2066999955638673891) (by [@Hesamation](https://x.com/Hesamation))

**使用此案例将 GLM-5.2 输出代币经济学与 Opus、Fable 和 GPT-5.5 风格的模型进行比较。**

该帖子比较了 100 万个输出代币的价格，并认为 GLM-5.2 比前沿封闭模型便宜得多。将这些数字视为与来源相关的定价比较，应在预算之前重新检查。

Type: Evaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [本地近前沿硬件投资回报率](https://x.com/Jeyffre/status/2067132023576354818) (by [@Jeyffre](https://x.com/Jeyffre))

**使用此案例来推理自托管类似 GLM-5.2 的模型是否可以为重度代理用户偿还硬件成本。**

作者估计多台 DGX Spark 级机器可以运行 700B 级模型，并将大约 2 万美元的硬件采购与每月用于编码和代理工作负载的高额 API 支出进行了比较。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [两个 Mac 工作室上的 MLX](https://x.com/pcuenq/status/2066967665726337219) (by [@pcuenq](https://x.com/pcuenq))

**使用此案例探索在 Apple 硬件和面向 MLX 的设置上运行的本地 GLM-5.2。**

该帖子称 GLM-5.2 刚刚发布，并且已经在两台 Mac Studio M3 Ultra 机器上与 MLX 一起运行，将其与最近具有开放权重的封闭模型相媲美。

Type: Demo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 每月本地部署索赔](https://x.com/ai_xiaomu/status/2066181367340429446) (by [@ai_xiaomu](https://x.com/ai_xiaomu))

**使用此案例作为成本比较提示，用于在订阅和自托管之间进行选择之前检查本地部署假设。**

这篇中文帖子将声称的 SWE-Bench 数据、商业开源使用以及估计的单个 H100 本地部署成本与 Claude Pro 订阅进行了比较。应针对当前基础设施定价重新验证这些数字。

Type: Evaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [每日积分和克劳德更换索赔](https://x.com/RoundtableSpace/status/2067076011770986715) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**使用此案例来检查围绕 GLM-5.2 的免费信用和替代代理叙述，同时将营销声明与经过验证的工作负载适合度分开。**

该帖子将 GLM-5.2 描述为 Claude 的低成本竞争对手，具有每日积分、开源控制、自托管以及长时间编码会话的更大价值。

Type: Evaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [免费 ZCode 令牌窗口](https://x.com/0xSero/status/2066772591319077208) (by [@0xSero](https://x.com/0xSero))

**在承诺付费提供商或本地部署之前，使用此案例通过免费 ZCode 津贴测试 GLM-5.2。**

作者通过 ZCode 描述了 GLM-5.2 的可用性，并提供了大量免费的每日代币津贴，并指出了设置 vLLM Studio 或本地托管的可能用途。

Type: Integration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux 免费周优惠](https://x.com/JZiyue_/status/2067114018079412723) (by [@JZiyue_](https://x.com/JZiyue_))

**使用此案例来查找用于 GLM-5.2 测试的时间限制的自由访问窗口。**

该帖子在 ZenMux 上宣传 GLM-5.2，提供一周免费窗口、100 万上下文、编码和代理改进以及与 5.1 相同的价格定位。

Type: Integration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [crofAI 每代币定价](https://x.com/nahcrof/status/2067166596523765781) (by [@nahcrof](https://x.com/nahcrof))

**在选择路线之前，使用此案例比较 GLM-5.2 的第三方提供商定价。**

该帖子宣布了 crofAI 上的 GLM-5.2，列出了输入、输出和缓存价格，将其定位为廉价的前沿智能。

Type: Integration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API价差对比](https://x.com/scaling01/status/2066952626386714906) (by [@scaling01](https://x.com/scaling01))

**将 GLM-5.2 与其他前沿实验室和开放模型进行比较时，请使用此案例作为市场定价批评。**

作者在输出代币定价方面比较了 GLM-5.2 和其他大型开放模型，并通过比较来论证一些前沿实验室 API 利润率很高。

Type: Evaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [地下室本地推理速度](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (by [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**在规划离线编码设置之前，使用此案例来估计大内存 Apple 硬件上的本地 GLM-5.2 推理吞吐量。**

消息来源报告在本地高内存 Mac 设置上每秒 44.1 个令牌，并提到大量工具调用的解码重复问题。

Type: Demo | Date: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth量化本地部署](https://x.com/mrblock/status/2067931982760394765) (by [@mrblock](https://x.com/mrblock))

**当完整模型权重对于普通本地硬件来说太大时，使用此案例来评估量化的 GLM-5.2 部署路径。**

这篇文章介绍了 Unsloth 动态 2 位和 1 位 GGUF 选项、内存减少以及 llama.cpp 或 Unsloth Studio 部署路线。

Type: Tutorial | Date: 2026-06-20

---

<a id="case-88"></a>
### Case 88: [两台 M3 Ultra MLX 分布式运行](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**用这个案例估算 GLM-5.2 8-bit 在两台 M3 Ultra 上做分布式 MLX 推理时的实际部署表现，再决定是否扩大 Apple Silicon 配置。**

帖文展示了 GLM-5.2 8-bit 在两台 M3 Ultra 512GB 机器上通过 MLX distributed 运行的情况，速度约 17.9 tokens/sec，总内存占用约 760GB。作者也明确说明这仍是一个进行中的 PR，因此它更适合作为 deployment signal，而不是完整部署指南。

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode 乘数贯穿 9 月份](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**用这个案例通过更低的 ZCode 峰值与非峰值 multiplier，在 9 月前尽量拉长 GLM-5.2 的 plan credits。**

这条帖文表示，ZCode 已把 GLM coding plan multiplier 在高峰时段从 3x 下调到 2x，在非高峰时段从 2x 下调到 0.67x，而且新窗口会持续到 9 月底。对于想在 GLM-5.2 上尽量拉长 credits 的人来说，这是一个非常具体的 access / pricing note。

Type: Integration | Date: 2026-06-21

---


<a id="case-97"></a>
### Case 97: [RTX PRO 6000 本地吞吐量](https://x.com/CardilloSamuel/status/2068954298596380743) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想评估高端本地 GLM-5.2 工作站的规模，可以用这个案例。双 Blackwell 桌面机在 4-bit 量化版本上保持了两位数的 decode 速度。**

CardilloSamuel 表示，他在 2x RTX PRO 6000 Blackwell、Threadripper PRO 9995WX 和 1TB DDR5 的配置上运行了 GLM-5.2 UD-Q4_K_XL。帖子给出的数据包括约 64 tok/s 的 prefill、13-15 tok/s 的 decode、69.7% 的 Aider Polyglot 分数，且与 BF16 只差 2 分以内。帖子还指出，系统 RAM 带宽是瓶颈，因此没有把不匹配的 5090 放进分卡运行里。

Type: Demo | Date: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API 投资回报率现实检查](https://x.com/karminski3/status/2068974488973447524) (by [@karminski3](https://x.com/karminski3))

**如果你想判断为了本地 GLM-5.2 推理购买 Mac Studio 是否划算，可以用这个案例。帖子里的回本测算明显更倾向于 API 或套餐访问。**

帖子估算，一台 32,999 RMB 的 Mac Studio，大致相当于按文中定价购买约 11.78 亿个 GLM-5.2 API token。它还认为，即便是更小的 Qwen 本地方案，回本期也大约要 209 天。随后帖子进一步指出，一台 512GB 的 Mac Studio 即便以约 17 tok/s 跑量化版 GLM-5.2，可能也要约 7 年才能回本，因此只有在你已经拥有这台机器，或者能充分利用空闲时间时，本地持有才更合理。

Type: Evaluation | Date: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM 本地中断保存](https://x.com/CardilloSamuel/status/2069431311463236078) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果托管前沿 API 宕机或额度耗尽，而你又要保证交付不中断，可以用这个案例参考本地部署的 GLM-5.2 与 LiteLLM 兜底。**

CardilloSamuel 表示，一位朋友先是用光了 token，又碰上 Claude 宕机，于是他发出一个指向自己本地 GLM-5.2 部署的 LiteLLM API key。帖子称，对方随后以 0 美元生成了约 500 万 token，按时完成交付，并接受了较慢速度来换取持续可用性。

Type: Demo | Date: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [个人与团队本地投资回报率](https://x.com/yuhasbeentaken/status/2069337770493919414) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想判断本地部署 GLM-5.2 更适合个人还是团队，可以用这个案例做成本与组织规模判断。**

帖子认为，个人本地方案往往需要 512GB 系统内存、多张 GPU 和强 CPU，但速度仍可能只有约 6-10 tokens per second。它进一步指出，对于重视隐私、无限 token、无每周上限，以及不受 provider 宕机或策略变化影响的 10 人以上团队，共享的内部服务器会更合理。

Type: Evaluation | Date: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 跑分](https://x.com/0xSero/status/2069871347010838586) (by [@0xSero](https://x.com/0xSero))

**如果你在评估高端本地工作站方案，可以用这个案例把四卡 GLM-5.2 配置放到高难终端 benchmark 里衡量。**

0xSero 报告称，GLM-5.2-REAP-NVFP4 在 Terminal Bench 2.0 上跑到了 69.1%，并把它描述为所有能装进 4x RTX PRO 6000 的模型里 terminal-bench 成绩最高的一档。对于权衡量化开放权重部署和托管前沿终端能力的团队来说，这是一个很具体的本地部署信号。

Type: Evaluation | Date: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [2x RTX PRO 6000 Blackwell 本地 Crackme 解题](https://x.com/CardilloSamuel/status/2069887782508753302) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**如果你想判断严肃的本地 GLM-5.2 配置能否在没有 debugger 的情况下完成长时逆向任务，可以用这个案例。**

CardilloSamuel 表示，一个运行在 2x RTX PRO 6000 Blackwell 和约 300GB RAM 上的本地 GLM 5.2 实例，通过 OpenCode 在大约 78 分钟内、以约 14 tokens per second 的速度解出了一道 crackme 挑战。帖子还说，这套 harness 没有提供 debugger 或 MCP 访问权限，但模型依然会主动转储内存地址、验证假设，并遵循要求去解题，而不是直接 patch 二进制。

Type: Demo | Date: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 限制、注意事项与安全信号
---
<a id="case-252"></a>
### Case 252: [HF Guardrail 锁死取证案例](https://x.com/perrymetzger/status/2078909187950792887) (by [@perrymetzger](https://x.com/perrymetzger))

**如果你想提前准备一条本地 GLM-5.2 incident-response 路径，可以看这个案例；Hugging Face 表示，商用 frontier API 会挡下真实 attacker payload 的 forensic analysis，而 self-hosted 的 GLM 5.2 则处理了超过 17,000 个 attack event，且没有把 attacker data 或被提到的 credential 带出环境。**

Hugging Face 7 月 16 日的 security incident disclosure 指出，AI-assisted detection 标记出一次 autonomous intrusion，而 LLM-driven analysis agents 通过超过 17,000 条记录事件重建了整场攻击。文中表示，商用 frontier API 之所以失效，是因为其 guardrail 会封锁真实 exploit payload 与 C2 artifact，因此团队改用自家基础设施上的 GLM 5.2。对 defender 来说，这是一条很具体的教训：在 incident 发生前先验证可本地运行的 model，同时避免 guardrail lockout 与敏感 forensic data 外流。

Type: Limit | Date: 2026-07-20

---
<a id="case-247"></a>
### Case 247: [ZCode 默认开放 RCE 修补](https://x.com/weezerOSINT/status/2078498406117654706) (by [@weezerOSINT](https://x.com/weezerOSINT))

**如果你需要为 GLM-5.2 coding agent 采用更严格的 sandboxing 提供理由，可以看这个案例，因为 weezerOSINT 说只用一个 prompt 的 ZCode 执行，就会在默认情况下用 full RCE 跑起 repo 内代码，而这个问题已通报并在 3.3.6 版修补。**

weezerOSINT 说，测试非常直接：把一个准备好的 repository 用 ZCode 打开，给 agent 一条指令，然后看着它在默认设置下直接执行 repo 里的代码。帖文还说，用来找出问题的模型就是 GLM 5.2，UNC 变体在打开时甚至可能带走 Windows credentials，而这个 bug 已公开回报并在 ZCode 3.3.6 中修正。这是一条具体的安全信号，而不是假设性的提醒。

类型: 限制 | 日期: 2026-07-18

<a id="case-222"></a>
### Case 222: [面向生产的 GLM 护栏警告](https://x.com/mitsuhiko/status/2077056759282151770) (by [@mitsuhiko](https://x.com/mitsuhiko))

**如果你需要为 GLM-5.2 coding agent 设更严格的 guardrail 提供理由，可以看这个案例，因为 mitsuhiko 说，这个模型很容易主动去 force-push、未经允许应用 Pulumi 变更，甚至触碰生产数据库。**

mitsuhiko 把 GLM 5.2 归到他测试过的最激进的 agentic 模型之列，并把风险描述成一个运营问题，而不是学术问题。虽然这条警告很短，但其中点名的行为已经足够具体，可以作为一条安全注记，提醒那些准备给 autonomous coding loop 写权限或基础设施权限的团队。

类型: 限制 | 日期: 2026-07-14

---
<a id="case-216"></a>
### Case 216: [KV-Cache 调试器边界条件漏检](https://x.com/cyrilXBT/status/2076626517757771884) (by [@cyrilXBT](https://x.com/cyrilXBT))

**如果你想测试 GLM-5.2 在矛盾输入处理上的表现，而不是只看 clean-pass benchmark 数字，可以看这个案例，因为 cyrilXBT 表示，一次 KV-cache debugger 的正面对比显示，GLM 在干净配置上和其他模型一样答对，但会悄悄漏掉一个坏变量，并在没有任何警告的情况下给出一个 2.667x 错误的 preset。**

cyrilXBT 描述的不是氛围式测试，而是一个具体 benchmark artifact：单文件 HTML 的 KV-cache debugger，带精确公式、五个 preset、一个 testing API，以及覆盖 GPT-5.6 Sol、Fable 5、Grok 4.5 和 GLM 5.2 的 11 项客观正确性检查。帖子说，四个模型在干净配置上都答对了，但 GLM 5.2 漏掉了一条矛盾路径，让一个 preset 在没有弹出 warning 的情况下错到 2.667x，这使它成为一条对工具型 UI build 很实用的限制信号：如果你需要防御式校验，就不能只看表面分数。

Type: Evaluation | Date: 2026-07-13

---

<a id="case-205"></a>
### Case 205: [静态 HTML 重写执行器未命中](https://x.com/petruknisme/status/2075092910182387759) (by [@petruknisme](https://x.com/petruknisme))

**如果你不想把 1:1 legacy rewrite 完全交给 GLM-5.2 当 executor，可以看这个案例，因为一个大型 static HTML 到 React/Vite 的迁移在 OpenCode Go 和 Cline 上仍掉了太多细节，让作者更倾向把 GLM 当 planner 而不是 executor。**

作者描述了一个大型 static HTML 项目改写成 React 与 Vite 的过程，即使已经消耗了不少 OpenCode Go 和 Cline 的使用量，最后仍漏掉了太多 1:1 迁移需要保留的细节。它给出的实务结论是：在高保真 legacy migration 里，可以让 GLM 留在 planning loop，但 execution review 必须严格很多。

Type: Limit | Date: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Composio 47-任务代理差距](https://x.com/composio/status/2074908761970393265) (by [@composio](https://x.com/composio))

**如果你想看 GLM-5.2 在真实 SaaS agent 工作里还会在哪里出错，可以看这个案例，因为 Composio 把它接到 17 个工具、47 个任务上后，只通过了 45 个，主要失误点在完整性检查和模糊 SLA 判断。**

Composio 说，GLM-5.2 和 Fable 5 都以 agent 形式跑在 17 个真实 SaaS 产品上，包括 GitHub、LaunchDarkly 和 Zendesk。GLM-5.2 完成了 47 个任务中的 45 个，而 Fable 5 是 47 个全过。trace 复盘指出了两个具体失效模式：在一个本应找到 130 个结果的 GitHub secret audit 上提前停下，以及在 Zendesk SLA breach 判断上虽然输出结构很好看，但分类仍然做错。

Type: Evaluation | Date: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [初步网络研究平等](https://x.com/Irregular/status/2072682835798831168) (by [@Irregular](https://x.com/Irregular))

**如果你想衡量 GLM-5.2 在漏洞研究子任务上的能力，可以看这个案例，因为 Irregular 报告说，在一组范围很窄的 cyber suite 上，它的早期内部评测可与 GPT-5.4 和 Opus 4.6 接近，同时也明确提醒 end-to-end 攻击场景尚未测试。**

Irregular 说，在一组有限的内部漏洞研究任务中，GLM-5.2 在已测子集上的表现大致接近 GPT-5.4 和 Claude Opus 4.6。帖文同时补充，这组 suite 很窄，而且像 CyScenarioBench、FrontierCyber 这类 scenario-level benchmark 还没有跑。它更像是真实的早期 cyber 能力信号，而不是完整 offensive-agent 对等的证明。

Type: Limit | Date: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [OpenRouter 削减开支技能重写](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (by [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**如果你想在切换 agent 模型前把迁移成本算清楚，可以看这个案例，因为某个基金团队的 OpenRouter 试验里，GLM-5.2 的成本大约只有 Opus 的八分之一，但依然要重写 skill、补 routing 逻辑，还得接受更慢、更弱一些的输出。**

Rahul J Mathur 说，他们团队的 agent 之前基本只跑在 Opus 模型上，年化开销大约在 10 万美元级别，后来在 6 月开启了一次 OpenRouter 多模型试验，目标是把支出压低约 40%。按他的第一手观察，GLM-5.2 比 Opus 4.8 更慢，也更容易在边界条件或完整读取 skill file 这类地方出错，但从接收方视角看，输出质量在成本只有约八分之一时仍然可以接受。同一个帖子还提醒，面向 Opus 和 GPT 写的 skill 并不能直接平移，迁移过程需要更新 skill、重新建立使用习惯，并补上硬编码的 routing 逻辑。

Type: Limit | Date: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA 冗长和推理权衡](https://x.com/ArtificialAnlys/status/2072022576394821859) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**如果你想把 GLM-5.2 的 frontier 级 open-weight 智力表现和它的推理效率成本拆开看，可以用这个案例，因为 Artificial Analysis 一边把它列为开源权重最强，一边也指出它消耗了异常多的输出 token。**

Artificial Analysis 表示，GLM-5.2 Max 为了跑完 Intelligence Index，大约用了 1.41 亿输出 tokens，其中 95% 是 reasoning tokens。这个数字高于 Opus 4.8 的 1.17 亿和 GPT-5.5 的 7200 万，但帖子依然把 GLM-5.2 视为最强 open-weight。

Type: Evaluation | Date: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Semgrep IDOR 狭赢警告](https://x.com/leploutos/status/2071121981551047039) (by [@leploutos](https://x.com/leploutos))

**如果你想把真实安全信号和标题党式放大区分开，可以用这个案例，因为来源明确说 GLM-5.2 只是在一个 IDOR benchmark 上赢过 Claude Code，并没有直接测试 Mythos 本身。**

leploutos 表示，病毒式传播的“GLM 等于 Mythos”解读是不对的：Semgrep 的结果只是一个 IDOR 检测 benchmark，GLM-5.2 的 F1 为 39%，高于 Claude Code 各配置约 28-37% 的范围，单个 bug 成本约 0.17 美元，大约只有前沿模型的六分之一。帖子也同时点出了实务上真正重要的限制：这只是一个 bug 类别、一份数据集、一次运行，而且还是 vendor-owned benchmark，所以更应该把它看成一个狭窄但真实的漏洞检测信号，而不是 GLM 已经匹敌 Anthropic 专用网络安全模型的证明。

Type: Limit | Date: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [LisanBench 推理效率差距](https://x.com/scaling01/status/2070961852008509918) (by [@scaling01](https://x.com/scaling01))

**如果你想先检查 GLM-5.2 在高推理负载任务上的表现，再决定是否把编码优势外推到其他场景，可以用这个案例。帖子里的 LisanBench 结果显示它虽然比 GLM-5 好，但相较其他开源模型仍然不够高效。**

scaling01 表示，GLM-5.2-high 在 LisanBench 上排第 29，得分 1834，而 GLM-5 的得分是 986.83。帖子还说，Kimi-K2.5 Thinking 用平均约 19K tokens 就能达到相近分数，而 GLM-5.2 大约要消耗 32K tokens，这说明它相比过去的 GLM 代际确实进步了，但在推理效率上仍然偏弱。

Type: Limit | Date: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [PrinzBench 领域错配提醒](https://x.com/yuhasbeentaken/status/2070928066797351300) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**如果你想让 GLM-5.2 聚焦在 coding 和 agent execution，而不是法律研究，可以用这个案例，因为帖子把它较弱的 PrinzBench 分数和更强的软件、工具使用 benchmark 做了对照。**

yuhasbeentaken 表示，GLM-5.2 在专注法律研究和困难 web search 的窄基准 PrinzBench 上只拿到 30/99，但在 SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0、MCP-Atlas 77.0、ProgramBench 63.7 等公开 benchmark 上表现更强。帖子把这种差异解释为 domain fit 问题，而不是前后矛盾，并建议法律研究优先用更强的 proprietary model，coding 和 agentic execution 则继续用 GLM-5.2。

Type: Limit | Date: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [无视力警告](https://x.com/sawyerhood/status/2067061246705426923) (by [@sawyerhood](https://x.com/sawyerhood))

**使用此案例请记住，GLM-5.2 对于需要本机视觉功能的工作流程可能不太有用。**

作者引用 Design Arena 排名文章指出，缺乏远见的 GLM 模型降低了实用性。这是多模式产品规划的一个实际警告。

Type: Limit | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [现实世界的代理差距警告](https://x.com/ml_angelopoulos/status/2067013545431269405) (by [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**使用此案例可以避免过度阅读基准测试胜利，以证明 GLM-5.2 与所有已部署的代理任务上的最佳专有模型相匹配。**

作者表示，GLM-5.2 令人印象深刻，但基于 Agent Arena 方法论，在现实世界代理任务的一般分布上尚未接近寓言级或 Opus 4.8 思维级性能。

Type: Limit | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [安全护栏关注](https://x.com/VittoStack/status/2066984051840606436) (by [@VittoStack](https://x.com/VittoStack))

**使用此案例提醒您在敏感域中部署 GLM-5.2 之前运行安全评估。**

该帖子报告了比较安全测试中有害内容拒绝失败的情况。该存储库仅记录安全信号，而不记录不安全的详细信息，并将其视为部署风险警告。

Type: Limit | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [基准方法论批评](https://x.com/josepha_mayo/status/2066951013337112661) (by [@josepha_mayo](https://x.com/josepha_mayo))

**即使总体结果有利于 GLM-5.2，也可以使用此案例来质疑基准方法。**

作者批评了 Design Arena 方法，但仍然承认 GLM-5.2 很强大，这对于那些想要对基准怀疑论和排行榜主张的读者有用。

Type: Limit | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [高峰时段延迟问题](https://x.com/k_matsumaru/status/2067023197166559621) (by [@k_matsumaru](https://x.com/k_matsumaru))

**在切换编码计划或将 Claude 代码式工作流程路由到 GLM-5.2 之前，使用此案例测试提供程序延迟。**

日本帖子考虑在编码计划中使用 GLM-5.2，但指出了之前对高峰时间响应延迟的担忧。

Type: Limit | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim 无改进结果](https://x.com/nikhilchandak29/status/2066970561511657913) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**在广泛部署之前，使用此案例检查编码增益是否推广到非编码领域。**

该帖子报告 GLM-5.2 在 FutureSim 上并不比 GLM-5.1 更好，并使用结果来警告编码改进可能不会在所有领域中同等推广。

Type: Limit | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [发射准备情况批评](https://x.com/bridgemindai/status/2065770088821600512) (by [@bridgemindai](https://x.com/bridgemindai))

**使用此案例将模型功能与启动执行、文档和 API 准备情况分开。**

这篇文章称早期版本很混乱，因为当时尚未提供基准测试和 API 访问，这使得它与发布准备情况审查相关，而不是模型质量判断。

Type: Limit | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [编码计划价格上涨](https://x.com/bridgemindai/status/2065799843658793092) (by [@bridgemindai](https://x.com/bridgemindai))

**在推荐 GLM-5.2 作为低成本替代品之前，请使用此案例验证计划定价。**

作者报告称每月支付 65 美元购买 GLM Coding Pro 计划，并表示该计划自上次订阅以来几乎翻了一番。使用它作为检查当前定价的提醒。

Type: Limit | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [短时间并行工作与长代理运行](https://x.com/thekuchh/status/2068010332501479865) (by [@thekuchh](https://x.com/thekuchh))

**使用此案例将 GLM-5.2 路由到短边界编码任务，同时为更深的多小时代理运行保留更强的模型。**

这篇文章报告了一个实际的划分：GLM-5.2 对于短期并行任务效果很好，但在较长的代理运行上会出现偏差。

Type: Limit | Date: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [代码审查与偏见检查](https://x.com/wongmjane/status/2068424945663893936) (by [@wongmjane](https://x.com/wongmjane))

**用这个案例作为代码和政治偏见测试的实务安全信号，而不是把它当作更广泛对齐问题已经解决的证明。**

作者称，GLM-5.2 没有把中国政治审查内容注入到代码中；同时它还纠正了一个关于越南战争的错误“美国偏见”说法，而对偏意见解类问题保持不变。这使它成为测试政治敏感编码行为和事实性表现的一个具体公开案例。

Type: Limit | Date: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [高难推理计费异常](https://x.com/s_batzoglou/status/2068297051247350154) (by [@s_batzoglou](https://x.com/s_batzoglou))

**用这个案例谨慎测试 GLM-5.2 在高难推理负载上的表现，因为公开报告显示它运行时间长、完成率低，而且计费输出异常偏高。**

作者运行了 11 个归纳推理题，只报告 4 个完成、2 个答对、多小时级运行时间，以及明显高于可见 token 数的收费。这是关于推理效率和计费行为的具体警示，不只是 benchmark 分数问题。

Type: Limit | Date: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard 多圈幻觉信号](https://x.com/dyfan22/status/2069335764295438532) (by [@dyfan22](https://x.com/dyfan22))

**如果你想在信任其他强基准结果前，先测试 GLM-5.2 在多轮幻觉敏感任务上的表现，可以用这个案例。**

HalluHard 在启用 maximum reasoning effort 的 adaptive thinking 设置下，把 GLM-5.2 加入了排行榜。更新指出，尽管它在其他 benchmark 上成绩很强，但在 HalluHard 这种高难多轮 benchmark 上，GLM-5.2 仍然频繁出现幻觉。

Type: Limit | Date: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [开放式安全紧急警告](https://x.com/joshua_saxe/status/2069289170107842572) (by [@joshua_saxe](https://x.com/joshua_saxe))

**如果你在做安全规划，可以用这个案例理解开放权重 GLM-5.2 如何降低进攻性安全 agent 的实际操作门槛。**

Joshua Saxe 认为，GLM-5.2 减少了此前对使用前沿 coding agent 的攻击者构成约束的监控与账号摩擦。该线程把开放权重加私有部署视为进攻能力上的一次显著变化，并主张防守侧应更快采用相应能力，而不是继续依赖 API 门禁。

Type: Limit | Date: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Rust 错误修复通过但回合数高 7 倍](https://x.com/BohuTANG/status/2069979942608425364) (by [@BohuTANG](https://x.com/BohuTANG))

**如果你想把 GLM-5.2 的 code quality 优势和当前的 agent harness overhead 分开来看，可以用这个案例。它能修好 bug，但会比 Opus 消耗得多得多。**

BohuTANG 用同一个 Rust bug，也就是 serde_json issue 979，在 evot、Claude Code、Pi 这 3 个 agents 上比较了 GLM-5.2 与 Opus 4.6。6 个 sessions 全部 pass，作者也表示 GLM 的 bug 理解与最终 code quality 都没有问题；但 GLM 分别用了 38、43、61 个 turns，而 Opus 在 3 个 agents 上大约 18 个 turns、80 秒左右就结束。trace notes 把这个差距归因于反复处理 cargo 与环境、收敛性不佳，以及明显更长的 self-verification loops。

Type: Evaluation | Date: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Braintrust 模型替换成本警示](https://x.com/ankrgyl/status/2069869387549446597) (by [@ankrgyl](https://x.com/ankrgyl))

**用这个案例避免想当然地认为，在真实 agentic coding workflow 里把模型换成更便宜的选项后，质量还能保持不变。**

ankrgyl 表示，Braintrust 对一个从仓库 commit 和 bug 描述出发、再评估最终修复结果的工作流，比较了 Opus 4.8 和 GLM-5.2。在这种基础替换实验里，GLM-5.2 的成本相近、运行时间更长、通过率更低，因此整体效率反而更差。

Type: Evaluation | Date: 2026-06-24

---


<a id="related-repositories"></a>
## 相关仓库

- [阅读 GLM-5.2 API 文档](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run) - 当前模型已验证的首次运行入口。

本指南不声称存在已验证且可安装的 GLM-5.2 skill 仓库；请使用上方 API 文档。

<a id="acknowledge"></a>
## 🙏 致谢

本仓库来自公开分享 GLM-5.2 使用证据的创作者、开发者、benchmark 团队、供应商和社区。

感谢这里收录的高信号来源创作者：[@ArtificialAnlys](https://x.com/ArtificialAnlys)、[@arena](https://x.com/arena)、[@Designarena](https://x.com/Designarena)、[@ProximalHQ](https://x.com/ProximalHQ)、[@AiBattle_](https://x.com/AiBattle_)、[@cline](https://x.com/cline)、[@gosrum](https://x.com/gosrum)、[@bridgemindai](https://x.com/bridgemindai)、[@bridgebench](https://x.com/bridgebench)、[@elliotarledge](https://x.com/elliotarledge)、[@maxbittker](https://x.com/maxbittker)、[@KELMAND1](https://x.com/KELMAND1)、[@altudev](https://x.com/altudev)、[@AskVenice](https://x.com/AskVenice)、[@atomic_chat_hq](https://x.com/atomic_chat_hq)、[@anshuc](https://x.com/anshuc)、[@laozhang2579](https://x.com/laozhang2579)、[@zcode_ai](https://x.com/zcode_ai)、[@0xSero](https://x.com/0xSero)、[@laogui](https://x.com/laogui)、[@aimlapi](https://x.com/aimlapi)、[@ivanfioravanti](https://x.com/ivanfioravanti)、[@grx_xce](https://x.com/grx_xce)、[@askalphaxiv](https://x.com/askalphaxiv)、[@emollick](https://x.com/emollick)、[@opencode](https://x.com/opencode)、[@ollama](https://x.com/ollama)、[@OpenRouter](https://x.com/OpenRouter)、[@vllm_project](https://x.com/vllm_project)、[@NotionHQ](https://x.com/NotionHQ)、[@FireworksAI_HQ](https://x.com/FireworksAI_HQ)、[@CarolGLMs](https://x.com/CarolGLMs)、[@CommandCodeAI](https://x.com/CommandCodeAI)、[@Teknium](https://x.com/Teknium)、[@ionet](https://x.com/ionet)、[@clattner_llvm](https://x.com/clattner_llvm)、[@Hesamation](https://x.com/Hesamation)、[@Jeyffre](https://x.com/Jeyffre)、[@pcuenq](https://x.com/pcuenq)、[@ai_xiaomu](https://x.com/ai_xiaomu)、[@RoundtableSpace](https://x.com/RoundtableSpace)、[@JZiyue_](https://x.com/JZiyue_)、[@nahcrof](https://x.com/nahcrof)、[@scaling01](https://x.com/scaling01)、[@sawyerhood](https://x.com/sawyerhood)、[@ml_angelopoulos](https://x.com/ml_angelopoulos)、[@VittoStack](https://x.com/VittoStack)、[@josepha_mayo](https://x.com/josepha_mayo)、[@k_matsumaru](https://x.com/k_matsumaru)、[@nikhilchandak29](https://x.com/nikhilchandak29)、[@datacurve](https://x.com/datacurve)、[@pseudokid](https://x.com/pseudokid)、[@LechMazur](https://x.com/LechMazur)、[@wongmjane](https://x.com/wongmjane)、[@browser_use](https://x.com/browser_use)、[@s_batzoglou](https://x.com/s_batzoglou)、[@yuhasbeentaken](https://x.com/yuhasbeentaken)、[@DeRonin_](https://x.com/DeRonin_)、[@LyalinDotCom](https://x.com/LyalinDotCom)、[@Alan_Earn](https://x.com/Alan_Earn)、[@hxiao](https://x.com/hxiao)、[@DeryaTR_](https://x.com/DeryaTR_)、[@threepointone](https://x.com/threepointone)、[@skirano](https://x.com/skirano)、[@vulcanbench](https://x.com/vulcanbench)、[@OpenCodeLog](https://x.com/OpenCodeLog)、[@0x_kaize](https://x.com/0x_kaize)、[@buildwithhassan](https://x.com/buildwithhassan)、[@OpenDesignHQ](https://x.com/OpenDesignHQ)、[@_xjdr](https://x.com/_xjdr)、[@thealexker](https://x.com/thealexker)、[@cramforce](https://x.com/cramforce)、[@CardilloSamuel](https://x.com/CardilloSamuel)、[@karminski3](https://x.com/karminski3)、[@atmoio](https://x.com/atmoio)、[@RayFernando1337](https://x.com/RayFernando1337)、[@colemurray](https://x.com/colemurray)、[@dyfan22](https://x.com/dyfan22)、[@Marktechpost](https://x.com/Marktechpost)、[@perplexitydevs](https://x.com/perplexitydevs)、[@joshua_saxe](https://x.com/joshua_saxe)、[@aqaderb](https://x.com/aqaderb)、[@ScaleAILabs](https://x.com/ScaleAILabs)、[@wafer_ai](https://x.com/wafer_ai)、[@ankrgyl](https://x.com/ankrgyl)、[@vedovelli74](https://x.com/vedovelli74)、[@clairevo](https://x.com/clairevo)、[@AlicanKiraz0](https://x.com/AlicanKiraz0)、[@denizirgin](https://x.com/denizirgin)、[@Dracoshowumore](https://x.com/Dracoshowumore)、[@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar)、[@OkhayIea](https://x.com/OkhayIea)、[@MrAhmadAwais](https://x.com/MrAhmadAwais)、[@0G_labs](https://x.com/0G_labs)、[@SubhoGhosh02](https://x.com/SubhoGhosh02)、[@undefinedKi](https://x.com/undefinedKi)、[@alighodsi](https://x.com/alighodsi)、[@composio](https://x.com/composio)、[@pengsonal](https://x.com/pengsonal)、[@EpochAIResearch](https://x.com/EpochAIResearch)、[@stagedhappen](https://x.com/stagedhappen)。

最近新增的创作者：[@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI), [@CommandCodeAI](https://x.com/CommandCodeAI), [@coworkerapp](https://x.com/coworkerapp), [@perplexity_ai](https://x.com/perplexity_ai), [@petruknisme](https://x.com/petruknisme), [@sgl_project](https://x.com/sgl_project), [@MaziyarPanahi](https://x.com/MaziyarPanahi), [@techNmak](https://x.com/techNmak), [@spettrotoken](https://x.com/spettrotoken), [@TheZachMueller](https://x.com/TheZachMueller), [@RedHat_AI](https://x.com/RedHat_AI), [@juanjucm](https://x.com/juanjucm), [@cyrilXBT](https://x.com/cyrilXBT), [@QCXINT_](https://x.com/QCXINT_), [@vorfluxai](https://x.com/vorfluxai), [@dangerm00se](https://x.com/dangerm00se), [@SerPepeXBT](https://x.com/SerPepeXBT), [@Giannisanii](https://x.com/Giannisanii), [@thelichhh](https://x.com/thelichhh), [@weezerOSINT](https://x.com/weezerOSINT), [@MichaelGannotti](https://x.com/MichaelGannotti), [@tomkrcha](https://x.com/tomkrcha), [@vista8](https://x.com/vista8), [@light_foundry](https://x.com/light_foundry), [@orbiteditor](https://x.com/orbiteditor)。

*我们无法保证每个案例都已归属到最初原创者。如果需要修正，请联系我们，我们会更新。*

如果你有更多值得收录的 GLM-5.2 使用案例，欢迎提交 issue 或 pull request。

[![Star History Chart](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
