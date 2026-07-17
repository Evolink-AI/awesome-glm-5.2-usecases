<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/en.jpg" alt="Dépôt de cas d’usage GLM-5.2 banner" width="760"></a>

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

# Dépôt de cas d’usage GLM-5.2

## 🍌 Introduction

Bienvenue dans le dépôt de cas d’usage à forte valeur de GLM-5.2.

**Nous collectons des cas réels, tutoriels, intégrations, évaluations, signaux de prix et limites de GLM-5.2 depuis des démos publiques et des communautés de créateurs.**

Ce README localisé se concentre sur les cas avec workflows concrets, preuves publiques de benchmarks, démos pratiques, intégrations, coûts ou limites utiles.

Chaque titre de cas renvoie à sa source publique et chaque auteur renvoie au profil du créateur.

[Essayer GLM-5.2 sur Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases&utm_content=introduction_cta)

## 📊 Vue d’ensemble

- **234 cas GLM-5.2 sélectionnés** provenant de créateurs publics, équipes de benchmark, développeurs d’outils, fournisseurs et utilisateurs de terrain.
- Couvre les évaluations comparatives et l’évaluation des modèles de pointe, les agents de code et les flux de travail à long contexte, les démos pratiques et exemples, les intégrations fournisseurs et outils, les coûts, les prix et le déploiement local, ainsi que les limites, avertissements et signaux de sécurité.
- Chaque cas inclut la source d’origine, l’attribution du créateur, un takeaway d’usage concis, le type de preuve et la date de publication.
- Utilisez ce repo pour trouver des workflows pratiques, comparer les forces et limites, découvrir des routes fournisseur et suivre des expériences réelles.

> [!NOTE]
> La collection privilégie les preuves concrètes au hype: démos publiées, méthodes de benchmark, notes d’intégration, données de coût et limites explicites.

> [!NOTE]
> Les README localisés conservent le même ordre de cas, les mêmes liens, anchors et attributions que la source anglaise. Certains titres restent proches de la langue source pour préserver la traçabilité.

<a id="quick-start"></a>
## ⚡ Quick Start

[Ouvrir GLM-5.2 sur EvoLink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=model_link).

Utilisez GLM-5.2 via l’API Chat Completions compatible OpenAI d’Evolink. Obtenez une API key sur [Obtenir votre clé API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key), puis définissez-la comme `EVOLINK_API_KEY` avant d’exécuter la requête.

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

Référence complète de l’API GLM-5.2 : [Ouvrir la documentation API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run).

## 📑 Menu

| Section | Cas |
|---|---|
| [📏 Évaluations comparatives et modèles de pointe](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207, 217, 223, 227 |
| [💻 Agents de code et flux de travail à long contexte](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194, 210-212, 228 |
| [🎮 Démos pratiques et exemples](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202, 213, 218, 229 |
| [🔌 Intégrations fournisseurs et outils](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208, 214, 219-220, 224-225, 230-232 |
| [💸 Coût, prix et déploiement local](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209, 215, 221, 226, 233-234 |
| [🧭 Limites, avertissements et signaux de sécurité](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205, 216, 222 |
| [Dépôts associés](#related-repositories) | Parcours API vérifié et surfaces adjacentes |
| [🙏 Remerciements](#acknowledge) | Crédits et politique de correction |

### [📏 Évaluations comparatives et modèles de pointe](#benchmarks-frontier-evaluation)

| Cas | Point clé | Type |
|---|---|---|
| [Case 227: Victoire du raytracer WebGL Gargantua](#case-227) | Utilisez ce cas pour benchmarker GLM-5.2 sur des builds navigateur mono-fichier très chargés en physique, car AlicanKiraz0 dit que GLM 5.2 Max a gagné une tâche de raytracer géodésique Gargantua en équilibrant mieux que les autres modèles testés la correction numérique et la discipline de rendu en temps réel. | Evaluation |
| [Case 223: Écart d'efficacité en tokens de l'Intelligence Index](#case-223) | Utilisez ce cas pour budgéter GLM-5.2 sur des workloads de benchmark à long horizon, car Artificial Analysis dit que GLM-5.2 Max a consommé en moyenne environ 43K output tokens par tâche d'Intelligence Index contre 25K pour Inkling et des totaux plus faibles pour Kimi K2.6 et DeepSeek v4 Pro Max. | Evaluation |
| [Case 217: La route de secours EvalPlus bat Fable](#case-217) | Utilisez ce cas pour tester une route de code à deux modèles sous contrôle d’un vérificateur, car gmi_cloud dit que Opus 4.8 en premier puis GLM 5.2 FP8 en secours ont résolu 94 des 100 tâches EvalPlus figées, soit cinq de plus que Fable 5, pour environ 47 pour cent de coût en moins. | Évaluation |
| [Case 207: Benchmark du navigateur de fluides stables](#case-207) | Utilisez ce cas pour comparer GLM-5.2 sur des builds de physique navigateur très algorithmiques, car AlicanKiraz0 a exécuté un benchmark HTML Stable Fluids et a donné 88 sur 100 à GLM 5.2 Max pour environ 1,17 dollar, devant Opus 4.8 et Fable 5 mais derrière GPT 5.6 Sol. | Evaluation |
| [Case 199: Indice de poids ouvert Epoch](#case-199) | Utilisez ce cas pour situer GLM-5.2 sur une courbe de capacité de long terme, car Epoch AI estime un score de 152 sur son Capabilities Index et le présente comme le meilleur open weight de son ensemble évalué. | Benchmark |
| [Case 196: Évaluation du harnais interne Databricks](#case-196) | Utilisez ce cas pour benchmarker GLM-5.2 sur une grande codebase privée d’ingénierie, car Databricks dit que son évaluation interne sur le travail de plus de 3.000 engineers a montré que GLM 5.2 performait très bien et que le seul choix du harness peut réduire le coût d’environ 2x. | Evaluation |
| [Case 190: NatureBench finaliste poids ouvert](#case-190) | Utilisez ce cas pour benchmarker GLM-5.2 sur des workflows d’agent scientifique, car NatureBench dit que GLM-5.2 a débuté numéro deux au classement global et a pris la tête des open weights sur 90 tâches dans six domaines scientifiques. | Benchmark |
| [Case 189: Compromis entre le coût des tâches et Terminal-Bench 45](#case-189) | Utilisez ce cas pour comparer GLM-5.2 à GPT-5.5 dans le même harness agentique, car un run de 45 tâches Terminal-Bench donne 25 réussites à GLM-5.2 contre 29 à GPT-5.5, pour environ 40% de coût en moins avec prompt caching. | Evaluation |
| [Case 188: Cravate Harvey LAB-AA, agent juridique](#case-188) | Utilisez ce cas pour benchmarker GLM-5.2 sur du vrai travail d’agent juridique, car Harvey LAB-AA place GLM-5.2 Max à 7,5% d’all-pass, à égalité avec Claude Opus 4.8 sur 120 tâches privées couvrant 24 domaines juridiques. | Benchmark |
| [Case 184: Responsable des poids ouverts AutomationBench-AA](#case-184) | Utilisez ce cas pour comparer GLM-5.2 sur l’automatisation SaaS avec règles métier plutôt que sur des benchmarks de code בלבד, car Artificial Analysis rapporte 27,8% pour GLM-5.2 Max et le présente comme le meilleur modèle open weights sur AutomationBench-AA. | Evaluation |
| [Case 178: Victoire du benchmark du simulateur à trois corps](#case-178) | Utilisez ce cas pour comparer GLM-5.2 sur des benchmarks de code orientés physique numérique, car AlicanKiraz0 a lancé une tâche chaotique de simulateur à trois corps et a donné à GLM 5.2 Max la meilleure note avec 91 sur 100. | Evaluation |
| [Case 167: Responsable Open Source GameDevBench 333 tâches](#case-167) | Utilisez ce cas pour suivre GLM-5.2 dans les benchmarks de développement de jeux agentiques, car GameDevBench est passé à 333 tâches et affirme que GLM-5.2 est désormais le modèle open-source le plus fort de son leaderboard malgré l'absence de vision. | Evaluation |
| [Case 175: Carte de pointage à double pendule à curseur](#case-175) | Utilisez ce cas pour comparer GLM-5.2 dans un benchmark de coding sous Cursor à tâche contrainte, car AlicanKiraz0 a évalué six modèles sur un simulateur HTML de double pendule et a donné 88 sur 100 à GLM 5.2 Max, derrière Fable et Sonnet mais devant GPT-5.5, Kimi K2.7 Code et Composer. | Evaluation |
| [Case 162: VulcanBench 10 tâches 80 % d'attache](#case-162) | Utilisez ce cas pour comparer GLM-5.2 sur de vraies tâches d ingénierie post-cutoff où le coût compte autant que le score, car Morgan Linton dit que VulcanBench a donné à GLM 5.2 High, Fable 5 Low et Sonnet 5 High le même 80 pour cent sur 10 repos, tandis que GLM se situait au milieu sur le coût. | Evaluation |
| [Case 159: Point de contrôle de 51,1 pour cent de SWE-Rebench](#case-159) | Utilisez ce cas pour suivre GLM-5.2 sur un leaderboard de SWE agents mis à jour en continu : le dernier post SWE rebench annonce 51,1 pour cent avec 2,62 millions de tokens, nettement devant les nouveaux runs DeepSeek, MiMo, Qwen et Gemma. | Evaluation |
| [Case 154: LaunchDarkly Edge-Case Win à 40/41](#case-154) | Utilisez ce cas pour tester GLM-5.2 sur un travail agentique avec outils métier plutôt que sur de simples évaluations de chat : Composio annonce 40 sur 41 sur GitHub, Jira et LaunchDarkly et dit que GLM a été le seul modèle à repérer un edge case d approbation en attente. | Evaluation |
| [Case 146: Finaliste du patch CyberBench Open-Weight](#case-146) | Utilisez ce cas pour mesurer GLM-5.2 sur la recherche et le patch de vulnérabilités à tonalité offensive, car CyberBench le place deuxième sur 60 vraies vulnérabilités OSS-Fuzz. | Evaluation |
| [Case 1: Indice d'intelligence d'analyse artificielle](#case-1) | Utilisez la publication d'analyse artificielle pour comparer le GLM-5.2 à d'autres modèles frontières ouverts et propriétaires en termes d'intelligence et de coût par tâche. | Benchmark |
| [Case 2: Classement du front-end de Code Arena](#case-2) | Utilisez ce cas pour évaluer GLM-5.2 sur de véritables tâches de codage front-end jugées par des comparaisons de type arène. | Benchmark |
| [Case 3: Première place de Design Arena](#case-3) | Utilisez ce cas pour juger si GLM-5.2 peut gérer des tâches de conception plus code plutôt que uniquement des tests de codage contenant beaucoup de texte. | Benchmark |
| [Case 4: Résultat FrontierSWE](#case-4) | Utilisez la publication FrontierSWE pour comparer GLM-5.2 aux modèles de style GPT-5.5, Opus et Fable sur les tâches d'ingénierie logicielle. | Benchmark |
| [Case 5: Responsable Open Source DeepSWE](#case-5) | Utilisez le cas DeepSWE pour comprendre GLM-5.2 comme un modèle ouvert solide pour les tâches difficiles d'évaluation de génie logiciel. | Benchmark |
| [Case 6: Terminal-Bench plus de 80 pour cent](#case-6) | Utilisez ce cas lors de l’évaluation de GLM-5.2 pour le codage orienté terminal et les flux de travail d’agent. | Benchmark |
| [Case 7: Comparaison SWELancer avec GPT-5.5](#case-7) | Utilisez ce cas SWELancer comme comparaison multimétrique concrète entre GLM-5.2 et GPT-5.5 sur la réussite des tâches, la récompense et le temps d'achèvement. | Evaluation |
| [Case 8: Signal de score parfait BridgeBench](#case-8) | Utilisez ce cas pour inspecter GLM-5.2 sur la base d'un raisonnement en plusieurs étapes plutôt que de coder uniquement des classements. | Benchmark |
| [Case 9: Raisonnement numéro un de BridgeBench](#case-9) | Utilisez ce cas pour comparer GLM-5.2 avec des modèles à frontières fermées sur des tâches de raisonnement fondées. | Benchmark |
| [Case 10: KernelBench-Hard sans raccourci](#case-10) | Utilisez ce cas pour vérifier si les gains de référence proviennent d'un comportement d'implémentation valide plutôt que d'un raccourci. | Evaluation |
| [Case 11: Rattrapage du banc Runescape](#case-11) | Utilisez ce cas comme un signal rapide pour la progression du modèle à poids ouvert sur des tâches de référence de type jeu. | Benchmark |
| [Case 12: Amélioration de la vitesse de BridgeBench](#case-12) | Utilisez ce cas pour évaluer les flux de travail sensibles à la latence où la vitesse compte aux côtés de l'intelligence. | Benchmark |
| [Case 60: KernelBench Hard et Mega GPU Codage](#case-60) | Utilisez ce cas pour évaluer GLM-5.2 sur le codage du noyau GPU sur KernelBench-Hard et KernelBench-Mega, où les traces d'agent ouvertes rendent le résultat inspectable. | Benchmark |
| [Case 70: Responsable Open Source DeepSWE Max-Effort](#case-70) | Utilisez ce cas pour suivre GLM-5.2 sur DeepSWE en mode effort maximal, où le leaderboard publié le place premier parmi les modèles ouverts avec un score de 44 % pass@1. | Benchmark |
| [Case 72: Finaliste du débat LLM](#case-72) | Utilisez ce cas pour évaluer GLM-5.2 au-delà du code sur des débats adversariaux multi-tours, où la variante max-reasoning a pris la deuxième place derrière les modèles Claude. | Benchmark |
| [Case 76: Taux d'hallucinations AA-Omniscience](#case-76) | Utilisez ce cas pour comparer GLM-5.2 sur la gestion de l’incertitude, où le résultat AA-Omniscience publié montre un taux d’hallucination plus faible que plusieurs autres modèles frontier. | Evaluation |
| [Case 90: Indice de travail agent GDPval-AA](#case-90) | Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, plutôt que sur des classements limités au code. | Evaluation |
| [Case 120: Responsable de la fiabilité de PostTrainBench](#case-120) | Utilisez ce cas pour comparer GLM-5.2 Max sur la fiabilité des agents post-training, pas seulement sur le score headline, car le leaderboard signale aussi zéro run en échec sur 84 tâches. | Benchmark |
| [Case 121: Feux d'artifice + Faros 211-Task Repo Eval](#case-121) | Utilisez ce cas pour juger GLM-5.2 sur de vraies tâches d’ingénierie dans des repos privés plutôt que seulement sur des benchmarks publics, car le résultat publié couvre score, vitesse et coût par tâche. | Evaluation |
| [Case 110: AA-Briefcase Frontière du temps par tâche](#case-110) | Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, où le temps par tâche compte autant que le score de benchmark. | Benchmark |
| [Case 111: Marges face-à-face du frontend de Code Arena](#case-111) | Utilisez ce cas pour examiner l’avantage front-end de GLM-5.2 via des résultats head-to-head par paire plutôt qu’avec une simple capture de classement. | Benchmark |
| [Case 113: SWE Atlas Codebase QnA Finaliste](#case-113) | Utilisez ce cas pour suivre GLM-5.2 sur Codebase QnA, Test Writing et Refactoring plutôt qu’en ne regardant qu’un seul leaderboard SWE. | Benchmark |
| [Case 102: Agent d'arrière-plan OpenInspect FP8](#case-102) | Utilisez ce cas pour étudier une pile d’agent en arrière-plan auto-hébergée sous GLM-5.2 au lieu d’un workflow de chat hébergé. | Integration |
| [Case 145: Migration de réduction des coûts vers OpenCode + Fireworks](#case-145) | Utilisez ce cas pour tester si un simple basculement vers un harness open-model suffit, car l'auteur a déplacé ses tâches personnelles de coding et de loops vers GLM-5.2 sur Fireworks avec OpenCode et dit que la facture token est tombée à un tiers sans perte de qualité évidente au quotidien. | Evaluation |
| [Case 143: Workflow Hermes MoA avec GLM agrégateur](#case-143) | Utilisez ce cas lorsqu'un tour d'agent à fort enjeu mérite plus d'orchestration, car la configuration Mixture of Agents de Hermes Agent a combiné GLM-5.2 avec d'autres modèles pour produire un résultat visiblement meilleur avec seulement un petit surcoût par tâche dans la démo publiée. | Integration |
| [Case 142: Écart du harness avec le mode reasoning de Cline](#case-142) | Utilisez ce cas pour évaluer la conception du harness et pas seulement les poids du modèle, car le même GLM-5.2 est passé de 57,3 % à 68,5 % sur les mêmes tâches de coding lorsque le harness a activé le reasoning. | Evaluation |
| [Case 136: Test sur le terrain Cursor + Fireworks 455M-Token](#case-136) | Utilisez ce cas pour juger GLM-5.2 comme un vrai daily driver dans Cursor, car l’auteur rapporte 455M de tokens d’usage réel avec un serving Fireworks rapide et aucune envie immédiate de revenir à Opus ou GPT-5.5. | Evaluation |
| [Case 135: Harnais Devin Desktop avec portabilité des compétences](#case-135) | Utilisez ce cas pour tester GLM-5.2 dans Devin Desktop quand la surface de coding native de Z.ai paraît instable, car l’auteur rapporte un portage de skills plus simple, plus de vitesse et une meilleure hackability. | Evaluation |
| [Case 94: Finaliste de Game Dev Arena](#case-94) | Utilisez ce cas pour juger GLM-5.2 sur la qualité de création de jeux, où le modèle a atteint la deuxième place sur Game Dev Arena et est devenu le meilleur labo open-weight de ce classement. | Evaluation |
| [Case 100: Jeu luddite après le refus de Claude](#case-100) | Utilisez ce cas pour prototyper avec GLM-5.2 des concepts de jeu sensibles aux politiques lorsqu’un modèle fermé refuse la demande, puis inspectez vous-même le résultat jouable. | Demo |

### [💻 Agents de code et flux de travail à long contexte](#coding-agents-long-context-workflows)

| Cas | Point clé | Type |
|---|---|---|
| [Case 168: Ensemble Synthwave Hard-Slice à 2,66 $](#case-168) | Utilisez ce cas pour tester GLM-5.2 dans un ensemble de coding multi-modèle plutôt que seul, car TracNetwork rapporte qu'un mix Synthwave basé sur GLM a atteint 46.3 pour cent sur LiveCodeBench hard pour environ 2,66 dollars et a battu chaque générateur pris séparément. | Integration |
| [Case 228: Base locale de coding agentic avec OpenCode](#case-228) | Utilisez ce cas pour valider une stack on-prem de coding agent avant de payer des abonnements frontier, car comma_ai dit que l’équipe a abandonné Anthropic en interne et obtient maintenant de meilleurs résultats d’agentic coding avec GLM 5.2 plus OpenCode. | Demo |
| [Case 212: Tutoriel Dell Hub GLM Agent](#case-212) | Utilisez ce cas si vous voulez monter un coding agent GLM-5.2 pour un workflow d’entraînement open-weight, car juanjucm a relié un nouveau guide qui combine l’arrivée de GLM-5.2-FP8 dans le catalogue Dell Enterprise Hub avec un pas-à-pas pour construire un agent autour de ce modèle. | Tutorial |
| [Case 211: Pipeline de rapport open-weight sur 8xB200](#case-211) | Utilisez ce cas si vous voulez placer GLM-5.2 comme rédacteur principal dans un pipeline de rapport proche du déploiement local, car TheZachMueller explique qu’en divisant un nœud 8xB200 en 4/4 il a pu confier la rédaction à GLM 5.2 NVFP4 et la retrieval à Kimi K2.7 Code, pour produire un rapport de 36 pages à une fraction du coût de Claude API. | Demo |
| [Case 210: Refonte multi-agents Liquid Glass de Spettro](#case-210) | Utilisez ce cas pour tester GLM-5.2 comme réparateur frontend très orienté recherche dans une refonte web multi-agents, car spettrotoken dit que GLM 5.2 a utilisé des outils intégrés de web scraping et de data fetching pour livrer une implémentation Liquid Glass cross-browser qui fonctionnait dans Firefox après l'échec de Fable 5 et GPT-5.5. | Demo |
| [Case 194: Compétence du noyau CuTeDSL Open Source](#case-194) | Utilisez ce cas pour étudier GLM-5.2 dans une skill réutilisable de débogage de kernels, car l’auteur a open-sourcé une skill Hermes pour CuTeDSL et dit que GLM-5.2 était particulièrement efficace en coût pour déboguer et écrire des kernels. | Tutorial |
| [Case 180: Boucle de compétences de récupération SSD Hermes](#case-180) | Utilisez ce cas pour tester GLM-5.2 dans une boucle d’agent orientée réparation, car ShankhadeepSho1 dit que Hermes plus GLM 5.2 a diagnostiqué un SSD de NAS en panne, corrigé le problème puis empaqueté la solution sous forme de skill réutilisable. | Demo |
| [Case 174: Pile de codeurs robustes avec routage de rôles](#case-174) | Utilisez ce cas pour placer GLM-5.2 comme coder lourd dans une pile personnelle routée par rôles, car denizirgin dit qu’un mois de tests avec Codex et OpenCode l’a amené à envoyer le coding work le plus lourd vers GLM 5.2 tout en gardant le budget mensuel total autour de 120 à 140 dollars. | Evaluation |
| [Case 155: Boucle TUI à quatre agents Cotal](#case-155) | Utilisez ce cas pour répartir une boucle de codage entre agents spécialisés : l auteur a utilisé deux workers GLM-5.2 sous un lead Opus et un reviewer GPT pour terminer une TUI façon lazygit en 47 minutes sans intervention humaine. | Demo |
| [Case 153: Projet pilote de réduction des coûts de migration héritée](#case-153) | Utilisez ce cas pour estimer GLM-5.2 comme ouvrier moins cher dans une boucle de modernisation legacy : selon le pilote de 8090, GLM plus Software Factory réduit le coût de 16,4 fois face à Opus 4.8 seul, mais tourne environ 3 fois plus lentement. | Evaluation |
| [Case 150: Navigateur Mac Studio - Utiliser la boucle locale](#case-150) | Utilisez ce cas pour tester si une pile GLM-5.2 entièrement locale peut faire un léger travail de browser agent sur du matériel grand public, car l'auteur a exécuté llama.cpp sur un Mac Studio et browser-use pour trouver un modèle PII sur Hugging Face. | Demo |
| [Case 148: Réduction des coûts d'échange d'agent Gumloop](#case-148) | Utilisez ce cas pour tester un remplacement direct de modèle dans un harness existant, car Gumloop affirme avoir déplacé ses agents les plus utilisés vers GLM-5.2 avec environ 50% de crédits en moins et sans baisse visible de qualité. | Evaluation |
| [Case 13: Boucle de refactorisation d'une heure quarante-deux minutes](#case-13) | Utilisez ce cas comme modèle pour une longue refactorisation frontale autonome avec TDD, les commentaires des réviseurs et les contrôles de régression. | Demo |
| [Case 14: Correction de bugs OpenCode et test d'implémentation](#case-14) | Utilisez ce cas pour tester GLM-5.2 en tant qu'agent de codage OpenCode pour les corrections de bogues ainsi qu'une petite tâche d'implémentation. | Demo |
| [Case 15: Procédure pas à pas du jeu vidéo rétro OpenCode](#case-15) | Utilisez cette procédure pas à pas pour créer un petit jeu avec GLM-5.2 et OpenCode à partir d'une seule invite, puis inspectez la manière dont le modèle gère les détails d'implémentation. | Tutorial |
| [Case 16: Concours de simulations physiques HTML5](#case-16) | Utilisez ce cas pour comparer le code GLM-5.2 et Kimi K2.7 sur des simulations physiques HTML5 autonomes sans bibliothèques. | Evaluation |
| [Case 17: Construction UX de l'interface utilisateur du site personnel](#case-17) | Utilisez ce cas pour demander à GLM-5.2 un site personnel soigné et inspecter dans quelle mesure plusieurs tours peuvent améliorer l'UI/UX. | Demo |
| [Case 18: Création de produits d'examen des contrats d'IA](#case-18) | Utilisez ce cas pour évaluer GLM-5.2 sur une tâche de création de produit avec un PRD, un budget temps, un nombre d'étapes, un quota d'utilisation et une comparaison de la qualité du code. | Evaluation |
| [Case 19: Fonctionnalité d'objectif ZCode pour des objectifs de développement plus larges](#case-19) | Utilisez ce cas pour comprendre comment GLM-5.2 est intégré dans ZCode 3.0 pour des tâches de développement agent plus importantes. | Integration |
| [Case 20: Wrapper Linux pour ZCode construit avec GLM-5.2](#case-20) | Utilisez ce cas comme exemple d'aide de GLM-5.2 avec des outils autour des environnements d'agent de codage. | Demo |
| [Case 21: Emballage des compétences en utilisation informatique](#case-21) | Utilisez ce cas pour étudier GLM-5.2 en tant qu'aide pour transformer un dépôt informatique open source en une compétence réutilisable. | Demo |
| [Case 22: Examen de l'environnement de développement agent ZCode 3.0](#case-22) | Utilisez ce cas pour évaluer GLM-5.2 dans un environnement de développement agent complet plutôt que dans une seule session de discussion. | Demo |
| [Case 62: Harnais OpenCode avec service local](#case-62) | Utilisez ce cas pour tester GLM-5.2 avec l'exploitation OpenCode, le service local et les workflows de codage gourmands en outils avant de le comparer avec Claude Opus. | Evaluation |
| [Case 65: Injection d'instructions à contexte long Fast-RLM](#case-65) | Utilisez ce cas pour améliorer le comptage de contextes longs GLM-5.2 et le comportement de l'agent REPL en déplaçant les instructions dans l'invite système RLM. | Integration |
| [Case 66: Essai de harnais ouvert du code DeepAgents](#case-66) | Utilisez ce cas pour essayer GLM-5.2 avec un faisceau d'agents de codage ouvert et comparez le modèle sous un shell d'agent reproductible. | Demo |
| [Case 77: Routage de la pile d'agents de marketing de production](#case-77) | Utilisez ce cas pour orienter GLM-5.2 vers des workflows d’agents en production qui valorisent structure, vitesse et self-hosting, tout en gardant des modèles fermés plus forts pour les jugements ambigus. | Evaluation |
| [Case 80: M3 Ultra Pokémon Rouge Objectif Course](#case-80) | Utilisez ce cas pour évaluer GLM-5.2 sur un run local d’agent de code à long horizon, où le modèle a passé environ une demi-journée à essayer de recréer Pokemon Red en HTML sur une machine M3 Ultra. | Demo |
| [Case 91: Affrontement de correction de bug de Cline Repo](#case-91) | Utilisez ce cas pour comparer GLM-5.2 et Opus 4.8 sur un vrai bug de dépôt, où GLM a consommé plus de tokens mais a produit le patch final le moins cher et le plus propre. | Evaluation |
| [Case 127: Réviseur GLM en ligne Pi](#case-127) | Utilisez ce cas pour ajouter un second relecteur dans une boucle d’agent de code de style Pi, car l’auteur indique que GLM-5.2 peut conseiller Opus tour après tour pour une hausse de coût d’environ 10 %. | Integration |
| [Case 122: Bot Telegram One-Shot avec AgentRouter](#case-122) | Utilisez ce cas pour tester si GLM-5.2 peut inférer des defaults orientés production dans un build one-shot avec agent de code, au lieu de produire seulement le chemin minimal qui fonctionne. | Demo |
| [Case 117: OpenCode Go Refactor Victoire du premier passage](#case-117) | Utilisez ce cas pour évaluer GLM-5.2 sur des refactors Go de taille moyenne dans OpenCode plutôt que de vous fier seulement aux promesses de benchmark. | Evaluation |
| [Case 119: Code Claude + Curseur 3,36 $ Exécution par défaut](#case-119) | Utilisez ce cas pour jauger GLM-5.2 comme daily driver dans Claude Code et Cursor avant de déplacer davantage de travail de coding autonome vers les open weights. | Evaluation |

### [🎮 Démos pratiques et exemples](#hands-on-demos-showcase-builds)

| Cas | Point clé | Type |
|---|---|---|
| [Case 229: Duel de portfolios de profil sur Hyperagent](#case-229) | Utilisez ce cas pour comparer GLM-5.2 à d’autres modèles open sur une vraie tâche d’agent avec navigateur, car arsh_goyal a exécuté GLM 5.2, DeepSeek V4, Kimi K2.6 et Qwen 3.7 côte à côte sur Hyperagent pour construire un portfolio personnel à partir de profils publics. | Demo |
| [Case 218: Rebuild portfolio et OS avec OpenCode](#case-218) | Utilisez ce cas pour situer GLM-5.2 sur des builds OpenCode ambitieuses, car MarkSShenouda dit que OpenCode Go plus GLM-5.2 l’ont aidé à reconstruire un site portfolio et un vrai OS écrit en C et en Assembly, capable de tourner dans WASM ou un émulateur Qemu. | Démo |
| [Case 213: Refonte GLM de LlamaCoder v4](#case-213) | Utilisez ce cas si vous voulez prototyper un workflow de génération d’apps en one-shot prompt en vous appuyant sur les points forts de GLM-5.2 en planning et en design, car nutlope dit que LlamaCoder v4 a été reconstruit autour de GLM 5.2, avec un meilleur parsing, un meilleur planning et désormais un renderer WebAssembly dans un stack gratuit et open source. | Demo |
| [Case 202: Gagner la fonctionnalité Space Shooter du code de commande](#case-202) | Utilisez ce cas pour comparer GLM-5.2 sur une build d’UI interactive en one-shot, car Command Code a exécuté le même prompt de retro space shooter sur Fable 5, GPT 5.5, GLM 5.2 et DeepSeek V4 Pro, puis a placé GLM en tête sur les features. | Evaluation |
| [Case 200: Émulateur ZCode Nintendo DS](#case-200) | Utilisez ce cas pour inspecter une build locale de coding sur un horizon long, car l’auteur a lancé GLM-5.2 dans ZCode sur 4x RTX 6000 avec pour objectif de construire un émulateur Nintendo DS en C++ à partir de zéro. | Demo |
| [Case 192: Code de commande Flappy Bird UX Split](#case-192) | Utilisez ce cas pour comparer GLM-5.2 sur des tâches légères de design et de jeu, car l’auteur a passé le même prompt Flappy Bird dans Command Code et conclut que Fable 5 n’était pas vraiment meilleur en UX alors qu’il coûtait presque neuf fois plus que GLM-5.2. | Evaluation |
| [Case 161: Cube de Rubik REAP NVFP4 en un seul essai](#case-161) | Utilisez ce cas pour tester GLM-5.2 sur des builds interactifs en single prompt, car la démo REAP-NVFP4 affirme qu un seul prompt a produit un Rubiks Cube 3D avec vrais scrambles, état live et bouton solve. | Demo |
| [Case 158: Client iPhone Relais OMP](#case-158) | Utilisez ce cas pour emballer rapidement un agent local GLM-5.2 dans une surface mobile : selon l auteur, le plugin build-ios-app de Codex a produit en quelques heures un client iPhone propre pour un relay OMP qui utilisait déjà GLM-5.2 et des tunnels Cloudflare. | Demo |
| [Case 144: Agent open source de recherche DevRel](#case-144) | Utilisez ce cas pour transformer GLM-5.2 en assistant de recherche vertical plutôt qu'en chat générique, car l'auteur a construit un agent DevRel open source qui transforme un produit et une audience en opportunités de contenu classées avec preuves et plans. | Demo |
| [Case 123: Refondre la boucle de page de destination à six variantes](#case-123) | Utilisez ce cas pour prototyper des landing pages à faible coût en générant d’abord plusieurs variantes GLM-5.2, puis en faisant passer la meilleure dans un agent de code. | Tutorial |
| [Case 23: One-Shot jouable dans les coulisses](#case-23) | Utilisez ce cas pour comparer le résultat, la durée d'exécution et le coût de la création de jeux avec la même invite entre GLM-5.2 et Opus 4.8. | Demo |
| [Case 24: Trois constructions réelles avec des résultats mitigés](#case-24) | Utilisez ce cas comme un ensemble de démonstration d'avertissement : testez plusieurs versions réelles avant de faire confiance à un modèle pour des tâches de production de jeux ou de vidéos. | Evaluation |
| [Case 25: Cloner Super Mario en ZCode](#case-25) | Utilisez ce cas pour évaluer la création de jeux itérative avec GLM-5.2 et ZCode sur plusieurs passes de correctifs et de fonctionnalités. | Demo |
| [Case 26: Concours d'atterrisseur lunaire](#case-26) | Utilisez ce cas pour comparer les codes GLM-5.2, MiniMax M3 et Kimi K2.7 sur une tâche de style jeu interactif. | Evaluation |
| [Case 27: Création d'une arène de conception en une seule invite](#case-27) | Utilisez ce cas pour inspecter ce que GLM-5.2 peut générer à partir d'une seule invite de conception dans un contexte d'arène. | Demo |
| [Case 28: Document de recherche Comprendre le flux de travail](#case-28) | Utilisez ce cas pour appliquer GLM-5.2 aux flux de travail de lecture papier avec des questions contextuelles et des références croisées. | Integration |
| [Case 29: Comparaison de poèmes contraints](#case-29) | Utilisez ce cas pour séparer l'exactitude de la qualité créative lorsque vous comparez GLM-5.2 avec les modèles de style Fable. | Evaluation |
| [Case 30: Exemple de sens du design](#case-30) | Utilisez ce cas comme signal de conception visuelle léger, puis vérifiez avec votre propre invite et examen de l'interface utilisateur. | Demo |
| [Case 71: Temple Run Voxel Jeu One-Shot](#case-71) | Utilisez ce cas pour stress-tester GLM-5.2 sur la génération de jeu en un seul prompt, puis examiner ce qui nécessite encore des corrections itératives dans un build visuellement riche. | Demo |
| [Case 78: Ensemble d'exemples One-Shot OpenCode Go](#case-78) | Utilisez ce cas pour benchmarker GLM-5.2 sur des builds one-shot rapides dans OpenCode Go avant de l’engager dans des boucles d’agents plus ouvertes. | Demo |
| [Case 81: Construction en une seule invite de Space Invaders](#case-81) | Utilisez ce cas pour tester GLM-5.2 sur la création de jeu en un seul prompt, puis voir comment quelques passes supplémentaires gèrent les remplacements d’assets et un léger polissage. | Demo |
| [Case 82: Laboratoire de récupération OpenCode One-Shot](#case-82) | Utilisez ce cas pour prototyper rapidement des simulations interactives d’échec d’agent, car l’auteur dit avoir obtenu un recovery lab fonctionnel en one-shot pour environ 3,50 $. | Demo |
| [Case 92: Ouvrir la reconstruction de l'URL de référence de conception](#case-92) | Utilisez ce cas pour tester GLM-5.2 sur une recréation web pilotée par référence, où un prompt plus une URL source ont reproduit un site avec une fidélité presque pixel-perfect. | Demo |
| [Case 99: Test qualité-prix du Trader Desk](#case-99) | Utilisez ce cas pour comparer GLM-5.2 sur des builds UI full-stack, où il s’est rapproché du résultat Trader Desk le plus soigné tout en ne coûtant qu’une petite fraction du meilleur résultat. | Evaluation |

### [🔌 Intégrations fournisseurs et outils](#provider-tool-integrations)

| Cas | Point clé | Type |
|---|---|---|
| [Case 170: Accès Plug-And-Play à l'API gratuite NVIDIA](#case-170) | Utilisez ce cas pour tester rapidement GLM-5.2 via un endpoint hébergé gratuit, car hqmank dit que NVIDIA a ouvert une route API compatible OpenAI et a confirmé qu'elle fonctionnait comme un remplacement plug-and-play. | Integration |
| [Case 169: Route des agents de codage IA pour les travailleurs gratuits](#case-169) | Utilisez ce cas pour mettre en place une route GLM-5.2 gratuite pour les coding agents, car le tutoriel relie Workers AI à Claude Code, OpenCode, Cursor et Aider via l'endpoint compatible OpenAI `cf/zai-org/glm-5.2`. | Tutorial |
| [Case 232: Agents GLM de check run sur Macroscope](#case-232) | Utilisez ce cas pour réduire le coût des agents de review de PR tout en gardant un vrai workflow de check run, car kayvz dit que Macroscope permet maintenant d’exécuter des Check Run Agents sur GLM 5.2 via la configuration `.md` habituelle du dépôt. | Integration |
| [Case 231: API de research agents Aster à 281 TPS](#case-231) | Utilisez ce cas pour benchmarker un endpoint hébergé rapide de GLM-5.2, car asterailabs dit que Aster Inference sert GLM 5.2 à 281 tokens par seconde dans une API d’inférence construite à partir d’un travail d’optimisation pour research agents. | Integration |
| [Case 230: Route GLM native TrueFoundry via Wafer](#case-230) | Utilisez ce cas pour brancher GLM-5.2 dans une stack existante de TrueFoundry AI Gateway, car wafer_ai dit que son intégration provider native démarre désormais avec GLM 5.2 et GLM 5.2 Fast sans changer le reste de la configuration du gateway. | Integration |
| [Case 225: Pont TogetherLink pour le harness Codex](#case-225) | Utilisez ce cas pour exécuter GLM-5.2 dans des CLI de coding agents existants, car nutlope dit que TogetherLink est un CLI open source qui permet à Codex et Claude Code d'appeler directement des modèles ouverts comme GLM 5.2. | Integration |
| [Case 224: Routage du Open Model Harness de Vorflux](#case-224) | Utilisez ce cas pour faire passer GLM-5.2 dans une session agent complète sans glue personnalisée, car vorfluxai dit que son Open Model Harness assigne GLM 5.2 aux étapes design, build et simplify tout en conservant intact le reste du flux Vorflux. | Integration |
| [Case 220: Agent clinique OpenMed dé-identifié](#case-220) | Utilisez ce cas pour garder GLM-5.2 dans un flux clinique préservant la confidentialité, car MaziyarPanahi dit que GLM 5.2 a planifié, appelé des outils et rédigé la disposition d’un cas complet après qu’OpenMed a retiré les identifiants en local et que Gemma 4 a géré la structure. | Intégration |
| [Case 219: Route d’accès GLM USDC via Katana](#case-219) | Utilisez ce cas pour exposer GLM-5.2 via une route pay per request native wallet, car imgn_ai dit que Katana sert GLM-5.2 sur x402 via Base sans compte, avec USDC et un llms.txt publié pour l’intégration directe. | Intégration |
| [Case 214: Route GLM via Databricks AI Gateway](#case-214) | Utilisez ce cas si vous voulez tester un chemin d’accès managé et très rapide vers GLM-5.2 dans un agent tooling, car QCXINT_ a montré un flux avec base URL et token Databricks AI Gateway qui expose une route GLM 5.2 semblant aller jusqu’à 1M de contexte, même si l’identité exacte du backend reste non confirmée. | Integration |
| [Case 208: Pile d’agents Open Molecular Viewer](#case-208) | Utilisez ce cas pour brancher GLM-5.2 sur un workflow ouvert d’inspection scientifique, car MaziyarPanahi a combiné GLM-5.2 via Hugging Face Inference Providers avec Qwen3-VL sur llama.cpp, Mol* et PydanticAI afin de rendre et critiquer une structure EGFR plus erlotinib à partir d’un seul prompt. | Integration |
| [Case 204: Perplexity Advisor Coût de référence WANDR](#case-204) | Utilisez ce cas pour estimer l’économie de GLM-5.2 dans un harness de computer use routé, car Perplexity dit que sa configuration GLM 5.2 plus advisor atteint 2.1x sur WANDR contre 6.1x pour Opus, avec un coût moyen proche de la moitié. | Evaluation |
| [Case 203: Routage des artefacts ouverts par un collègue](#case-203) | Utilisez ce cas pour amener GLM-5.2 dans des workflows d’artifacts en entreprise, car Coworker dit que Open Artifacts peut créer docs, decks, PDF, spreadsheets, dashboards et apps tandis que son routeur optimisé réduit l’usage de tokens d’environ 5x tout en proposant GLM 5.2 hébergé aux États-Unis. | Integration |
| [Case 201: Flux de travail de téléchargement de contexte DotCode](#case-201) | Utilisez ce cas pour donner à GLM-5.2 davantage de contexte projet dans une sandbox privée de coding, car DotCode a ajouté le support de GLM 5.2 avec des uploads de captures, images, CSV, PDF, fichiers source et ZIP qui alimentent le même flux filesystem et terminal. | Integration |
| [Case 221: Serving agentique B300 avec SGLang TopK-V2](#case-221) | Utilisez ce cas pour benchmarker un serving GLM-5.2 de production sur des workloads agentiques à long contexte, car lmsysorg dit que SGLang a dépassé 500 tok/s par utilisateur sur 8xB300 en batch size 1 tout en améliorant l’interactivité mono-utilisateur de 18 à 34 pour cent. | Évaluation |
| [Case 215: Route llm-d H200 avec Prefix-Cache](#case-215) | Utilisez ce cas si vous voulez benchmarker l’économie d’un serving managé GLM-5.2 sur H200, car RedHat_AI dit que le couplage Wide EP plus prefix-cache routing dans llm-d a obtenu plus de 90 pour cent de cache reuse, un TTFT sous les 3 secondes et environ 2 dollars par million d’output tokens sur une route GLM-5.2 de plus de 700B. | Integration |
| [Case 209: Colibri 25 Go de RAM Streaming clairsemé](#case-209) | Utilisez ce cas pour comprendre la nouvelle borne basse des expériences locales avec GLM-5.2, car techNmak explique comment Colibrì exécute le MoE 744B avec environ 25 Go de RAM en streamant les experts depuis du NVMe, même si la plus petite configuration ne dépasse qu’environ 0,05 à 0,1 tok/s. | Demo |
| [Case 206: Débit de production SGlang NVFP4](#case-206) | Utilisez ce cas pour cadrer un serving SGLang de production pour GLM-5.2 NVFP4, car la release officielle SGLang v0.5.15 dit atteindre plus de 500 tok/s par utilisateur sur 8x B300 et 450 tok/s sur 4x GB300 avec batch size 1. | Evaluation |
| [Case 198: Point de terminaison GLM gratuit Dahl 100 millions](#case-198) | Utilisez ce cas pour essayer GLM-5.2 via une route OpenAI-compatible sans carte bancaire, car Dahl Inference propose 100M de tokens gratuits pour GLM 5.2 FP8 et montre comment créer une clé puis appeler `/v1/chat/completions`. | Tutorial |
| [Case 195: Configuration GLM gratuite du point de terminaison NVIDIA](#case-195) | Utilisez ce cas pour tester GLM-5.2 dans des outils de code sans self-hosting, car la source décrit un flux d’endpoint NVIDIA gratuit qui injecte des clés API GLM-5.2 dans Claude Code, Cursor ou Cline. | Tutorial |
| [Case 193: Route d'inférence privée 0G TeeML](#case-193) | Utilisez ce cas pour faire passer GLM-5.2 par une route fournisseur axée confidentialité, car 0G dit que GLM 5.2 tourne désormais dans TeeML avec des prompts scellés dans une enclave TEE et un prix inférieur à la voie officielle. | Integration |
| [Case 185: PR Open-SQL pour DuckDB Flock](#case-185) | Utilisez ce cas pour faire entrer GLM-5.2 dans une analyse SQL locale entièrement ouverte, car lhoestq dit qu’un PR duckdb plus flock active désormais GLM-5.2 dans une stack data 100% open source. | Integration |
| [Case 179: Accès à l'API One-Key à 26 modèles](#case-179) | Utilisez ce cas pour tester GLM-5.2 via un seul fournisseur compatible OpenAI, car Alan_Earn dit qu’une seule clé API expose GLM-5.2 plus 25 autres modèles et inclut 26 dollars de crédits de départ. | Tutorial |
| [Case 176: Configuration de la réflexion NVIDIA NIM OpenCode](#case-176) | Utilisez ce cas pour brancher GLM-5.2 dans OpenCode via le endpoint gratuit NVIDIA NIM quand vous voulez une route sans coût avec thinking activé explicitement, car Dracoshowumore partage le flux d’API key, la base URL et une configuration OpenCode où la couche outils gère les function calls pendant que GLM tourne avec enable_thinking=true. | Tutorial |
| [Case 165: Lancement de ZCode avec contrôle d'agent mobile](#case-165) | Utilisez ce cas pour évaluer ZCode comme surface officielle de coding pour GLM-5.2, car le rapport de lancement dit que cet IDE agentique gratuit arrive sur Windows, macOS et Linux et peut suivre les projets via Telegram, WeChat et Feishu. | Integration |
| [Case 160: Documentation de l'agent géré automatiquement par OpenWiki](#case-160) | Utilisez ce cas pour garder automatiquement à jour une documentation lisible par les agents, car LangChain explique que OpenWiki régénère et maintient les docs du repo à mesure que le code change et tourne sur des open models comme GLM 5.2. | Integration |
| [Case 152: PTU de fonderie via FireConnect](#case-152) | Utilisez ce cas pour faire passer GLM-5.2 par des budgets Foundry d entreprise sans reconstruire vos clients agents, car Fireworks explique que FireConnect relie les PTU de Microsoft Foundry aux workflows Codex, OpenCode et Pi. | Integration |
| [Case 147: Établi d'évaluation Braintrust GLM](#case-147) | Utilisez ce cas pour comparer GLM-5.2 et Opus dans une même pile d'evals, car Braintrust et Baseten ont lancé le modèle avec un exemple concret de coût contre précision en long contexte. | Integration |
| [Case 141: Abonnement ClinePass pour modèles open-weight](#case-141) | Utilisez ce cas pour regrouper plusieurs modèles de coding open-weight dans un seul agent harness, car ClinePass réunit GLM-5.2 et des modèles proches sous un forfait mensuel fixe au lieu de clés provider et de facturations séparées. | Integration |
| [Case 137: Service API GLM gratuit pour les agents de codage](#case-137) | Utilisez ce cas pour tester GLM-5.2 dans Hermes ou d’autres agents de code sans inscription, car le service partagé émet des API keys de courte durée et garde un setup léger. | Integration |
| [Case 31: Disponibilité d’OpenCode Go](#case-31) | Utilisez ce cas pour suivre la disponibilité de GLM-5.2 dans les workflows OpenCode Go avec du texte, un contexte 1M et une tarification de type GLM-5.1. | Integration |
| [Case 32: Disponibilité du cloud Ollama](#case-32) | Utilisez ce cas pour acheminer GLM-5.2 vers Ollama Cloud pour des expériences de modèle de codage open source accessibles. | Integration |
| [Case 33: Accès aux appels API OpenRouter One](#case-33) | Utilisez ce cas pour accéder à GLM-5.2 via OpenRouter lors de la comparaison du routage de fournisseur ou des piles multimodèles. | Integration |
| [Case 34: Prise en charge de vLLM Day-Zero](#case-34) | Utilisez ce cas pour auto-héberger ou servir GLM-5.2 via vLLM avec une prise en charge jour zéro. | Integration |
| [Case 35: Disponibilité de la notion via Baseten](#case-35) | Utilisez ce cas pour identifier GLM-5.2 en tant que modèle à poids ouvert disponible dans les flux de travail Notion. | Integration |
| [Case 36: Service de feux d'artifice jour zéro](#case-36) | Utilisez ce cas pour évaluer Fireworks en tant que route de diffusion pour les charges de travail GLM-5.2 nécessitant une infrastructure hébergée. | Integration |
| [Case 37: Lien vers le jardin modèle Google Cloud](#case-37) | Utilisez ce cas pour trouver GLM-5.2 dans des contextes de déploiement orientés Google Cloud et de plate-forme d'agent. | Integration |
| [Case 38: Mode de confidentialité de Venise](#case-38) | Utilisez ce cas lorsque le mode de confidentialité, TEE ou le chiffrement de bout en bout est un facteur décisif pour essayer GLM-5.2. | Integration |
| [Case 39: Disponibilité du code de commande](#case-39) | Utilisez ce cas pour essayer GLM-5.2 dans Command Code avec un plan d’entrée à faible coût et des fonctionnalités de codage à contexte long. | Integration |
| [Case 40: Agent Hermès du portail Nous](#case-40) | Utilisez ce cas pour connecter GLM-5.2 aux flux de travail Hermes Agent via Nous Portal et OpenRouter. | Integration |
| [Case 41: Partenaire de lancement io.net Day-Zero](#case-41) | Utilisez ce cas lors de l'évaluation de la diffusion basée sur le calcul pour un modèle à contexte long avec paramètres 753 B. | Integration |
| [Case 42: Service Day-Zero dans le cloud modulaire](#case-42) | Utilisez ce cas pour envisager Modular Cloud pour le service GLM-5.2 à contexte long à l'échelle du fournisseur. | Integration |
| [Case 61: Configuration du curseur via OpenRouter](#case-61) | Utilisez ce cas pour configurer GLM-5.2 dans Cursor via OpenRouter pour un flux de travail de codage en modèle ouvert à faible coût. | Tutorial |
| [Case 63: Amp Agentic Eyes pour la conception visuelle](#case-63) | Utilisez ce cas pour associer GLM-5.2 aux agents personnalisés Amp lorsqu'un modèle texte uniquement nécessite la prise en charge de la révision visuelle pour les tâches de conception. | Integration |
| [Case 69: Baseten Service plus rapide pour un million de contextes](#case-69) | Utilisez ce cas pour acheminer GLM-5.2 via Baseten lorsque la vitesse de diffusion dans un contexte long est importante pour Factory Droid, OpenCode et les faisceaux de codage. | Integration |
| [Case 74: Le navigateur utilise des sous-agents d'assurance qualité pour la conception Web](#case-74) | Utilisez ce cas pour associer GLM-5.2 à des sous-agents QA multimodaux Browser Use v2 lorsqu’un modèle purement textuel a besoin d’inspection visuelle et de corrections itératives de site web. | Integration |
| [Case 79: Jetons gratuits quotidiens officiels de l'IDE ZCode](#case-79) | Utilisez ce cas pour accéder à GLM-5.2 via ZCode si vous voulez un IDE de code officiel gratuit avec de grands quotas quotidiens de tokens et un workflow proche de Cursor. | Tutorial |
| [Case 83: Configuration du curseur via des feux d'artifice](#case-83) | Utilisez ce cas pour brancher GLM-5.2 dans Cursor via Fireworks avec une configuration minimale compatible OpenAI et sans code client personnalisé. | Tutorial |
| [Case 84: Prise en charge du fournisseur VulcanBench ZAI](#case-84) | Utilisez ce cas pour exécuter GLM-5.2 dans un harness de benchmark ouvert avec un support fournisseur ZAI de premier ordre et un chemin de clé API dédié. | Integration |
| [Case 85: Variantes de raisonnement OpenCode High/Max](#case-85) | Utilisez ce cas pour accéder aux variantes de raisonnement High et Max de GLM-5.2 dans OpenCode tout en profitant d’une gestion plus fiable des limites d’étapes. | Integration |
| [Case 86: Sélection du point de terminaison de codage Z.ai](#case-86) | Utilisez ce cas pour orienter le trafic de plan de code GLM-5.2 vers l’endpoint Z.ai optimisé pour le code plutôt que vers le chemin API générique. | Tutorial |
| [Case 87: Configuration de l'API ZenMux gratuite GLM-5.2](#case-87) | Utilisez ce cas pour obtenir gratuitement une clé API et une base URL GLM-5.2, puis l’intégrer dans Claude, Cursor, Hermes et des outils similaires. | Tutorial |
| [Case 93: Noumène ncode GLM Par défaut](#case-93) | Utilisez ce cas pour acheminer GLM-5.2 vers des environnements d’agents type ncode et Noumena avec des endpoints standard et 1M contexte séparés, plus un support de modèle par défaut. | Integration |
| [Case 101: Baseten + Harnais de droïde Démarrage rapide](#case-101) | Utilisez ce cas pour lancer rapidement GLM-5.2 via Baseten et le harness Droid, avec un court flux de configuration réutilisable dans d’autres IDE. | Tutorial |
| [Case 104: Flux de travail de l'API GLM compatible avec OpenAI](#case-104) | Utilisez ce cas pour construire en Python un client GLM-5.2 compatible OpenAI avec contrôle du raisonnement, tool calling, récupération long contexte et suivi des coûts. | Tutorial |
| [Case 105: Bac à sable de recherche de l'API de l'agent Perplexity](#case-105) | Utilisez ce cas pour brancher GLM-5.2 dans l’Agent API de Perplexity quand vous voulez des agents sandboxés avec recherche derrière un seul appel API. | Integration |
| [Case 109: API Baseten 280 TPS GLM](#case-109) | Utilisez ce cas lorsque la latence fournisseur compte: Baseten revendique un serving GLM-5.2 très rapide avec un time-to-first-token sous la seconde et un haut débit de décodage. | Integration |
| [Case 128: Configuration OpenCode de Cloudflare Workers AI](#case-128) | Utilisez ce cas pour faire tourner GLM-5.2 via Cloudflare Workers AI quand vous voulez une route gratuite compatible OpenAI pour des agents de code sans provisionner votre propre hébergement de modèle. | Tutorial |
| [Case 129: Client de navigateur sans configuration Puter.js](#case-129) | Utilisez ce cas pour tester GLM-5.2 dans un prototype 100 % navigateur avant de toucher aux API keys, à la facturation ou au backend. | Tutorial |
| [Case 130: Accès unifié aux points de terminaison SiliconFlow](#case-130) | Utilisez ce cas pour placer GLM-5.2 dans une stack multimodèle plus large, car le post décrit un endpoint unique compatible OpenAI de SiliconFlow couvrant des modèles chinois et occidentaux avec crédit d’essai gratuit. | Integration |
| [Case 124: Créateur de site Web HuggingChat vers HF Space](#case-124) | Utilisez ce cas pour essayer GLM-5.2 dans un flux presque gratuit de site personnel, de la recherche dans HuggingChat jusqu’au déploiement statique sur Hugging Face Spaces. | Tutorial |
| [Case 125: Disponibilité du moteur d'inférence DigitalOcean](#case-125) | Utilisez ce cas pour faire passer GLM-5.2 par une infrastructure managée quand vous voulez un accès provider officiel sans auto-héberger vous-même le modèle à contexte 1M. | Integration |
| [Case 115: Code de commande rapide 120-250 Tok/S Tier](#case-115) | Utilisez ce cas pour accéder à un palier GLM-5.2 plus rapide dans Command Code quand la vitesse de coding à long horizon compte plus que le prix d’entrée minimal. | Integration |
| [Case 116: API Vercel AI Gateway Fast GLM-5.2](#case-116) | Utilisez ce cas pour router GLM-5.2 Fast via Vercel AI Gateway quand vous avez besoin de vitesse serverless avec des prix token explicites. | Integration |
| [Case 95: Claude Code à travers Baseten](#case-95) | Utilisez ce cas pour exécuter GLM-5.2 dans Claude Code via une clé Baseten, une base URL personnalisée et un remapping de modèle dans `~/.claude/settings.json`. | Tutorial |
| [Case 96: Agent Deepsec Pi par défaut](#case-96) | Utilisez ce cas pour tester GLM-5.2 dans un harness de sécurité, où `deepsec` en a fait le modèle par défaut pour Pi agent et a rapporté des résultats d’évaluation compétitifs. | Integration |

### [💸 Coût, prix et déploiement local](#cost-pricing-local-deployment)

| Cas | Point clé | Type |
|---|---|---|
| [Case 234: Accès GLM remisé sur Jatevo](#case-234) | Utilisez ce cas pour obtenir une route simple d’accès hébergé à GLM-5.2 avec des prix publics, car JatevoId dit que GLM 5.2 est disponible sur sa plateforme à $1.40 par million d’input tokens et $4.40 par million d’output tokens, avec 50% de remise pour les holders JTVO éligibles. | Integration |
| [Case 233: Serving GLM sur MI325x sous un dixième de cent](#case-233) | Utilisez ce cas pour budgéter une inférence self-hosted de GLM-5.2 sur matériel AMD, car picocreator dit qu’une configuration 4xMI325x a servi GLM 5.2 à 1,482 tok/s pour moins de $0.10 par million de tokens. | Demo |
| [Case 226: Triage de dossier clinique sur Mac Studio avec Bonsai](#case-226) | Utilisez ce cas pour garder local un long dossier clinique pendant que GLM-5.2 raisonne dessus, car MaziyarPanahi dit que GLM 5.2 a trié un dossier patient sur trois ans via Bonsai 27B sur un Mac Studio et a repéré un risque lié au contraste enfoui 17 mois plus tôt. | Demo |
| [Case 191: Laboratoire local LiteLLM construit par Hermes](#case-191) | Utilisez ce cas pour amorcer un labo local d’inférence avec GLM-5.2 comme agent de code, car la source dit que Hermes Agent plus GLM-5.2 ont câblé LiteLLM, Postgres, Prometheus et Grafana autour d’une configuration M3 Ultra. | Integration |
| [Case 187: Sim de drone hors ligne Dual M5 Max](#case-187) | Utilisez ce cas pour estimer ce qu’un agent GLM-5.2 entièrement offline sur Apple Silicon peut faire, car XavierLocalAI rapporte une installation 753B écrivant un simulateur d’atterrissage sur droneship à 26 tok/s sur deux machines M5 Max de 128GB. | Demo |
| [Case 186: 5x harnais de production d'étincelles DGX](#case-186) | Utilisez ce cas pour juger si une configuration DGX Spark à cinq nœuds suffit pour un travail GLM-5.2 en production, car thatcofffeeguy rapporte environ 13,9 tok/s en flux unique à 400K de contexte et 19,9 tok/s agrégés sur trois lanes dans une harness en direct. | Demo |
| [Case 183: Point de contrôle M3 Ultra ds4-eval Q4](#case-183) | Utilisez ce cas pour benchmarker une installation GLM-5.2 sur Apple Silicon en machine unique avec ds4-eval, car ivanfioravanti rapporte un run q4 autour de 16 tok/s avec 76 réussites sur 92 en 8 h 53 sur une machine M3 Ultra 512GB. | Evaluation |
| [Case 182: Guide de construction de 4x RTX PRO 6000](#case-182) | Utilisez ce cas pour cadrer une vraie build locale GLM-5.2-594B, car QingQ77 partage un guide complet hardware plus opérations construit autour de quatre RTX PRO 6000, d’API exposées via opencode et d’une VM sandbox pour le travail des agents. | Tutorial |
| [Case 181: 4x exécution DGX Spark QuantTrio](#case-181) | Utilisez ce cas pour estimer ce qu’un cluster DGX Spark à quatre nœuds peut faire avec GLM-5.2 QuantTrio, car Tech2Wild rapporte un contexte de 200K ainsi que 30 tok/s en flux unique et 60,5 tok/s de débit agrégé à six requêtes concurrentes. | Demo |
| [Case 177: Exécution vidéo unique M3 Ultra 4 bits](#case-177) | Utilisez ce cas pour estimer la viabilité de GLM-5.2 sur une seule machine Apple Silicon, car ivanfioravanti montre une exécution 4-bit sur un M3 Ultra 512GB à environ 16 tok/s et la compare à une vidéo ds4-eval en q2 autour de 17 tok/s. | Demo |
| [Case 173: Service de nœud AMD MI355X 2626 Tok/s](#case-173) | Utilisez ce cas pour dimensionner une inférence GLM-5.2 à haut débit sur matériel AMD, car wafer_ai dit que MI355X a atteint 2626 tok/s par nœud et 213 tok/s en flux unique avec un coût de plus de 2 fois inférieur à Blackwell. | Demo |
| [Case 172: Vercel Gateway 287 Tok/s sans serveur](#case-172) | Utilisez ce cas pour estimer la latence GLM-5.2 réellement perçue par les utilisateurs via un gateway serverless, car wafer_ai dit que sa route GLM 5.2 Fast a atteint 287 tokens par seconde sur Vercel AI Gateway et pas seulement dans un harness de benchmark. | Demo |
| [Case 171: Déploiement RTX PRO 6000 en un clic](#case-171) | Utilisez ce cas pour estimer le plancher d'un déploiement GLM-5.2 hébergé et isolé, car XciD_ dit que GLM-5.2-NVFP4 est maintenant disponible en one-click sur Inference Endpoints avec 8x RTX PRO 6000 pour 22 dollars par heure. | Integration |
| [Case 166: 744B complet sur 5x ASUS GX10](#case-166) | Utilisez ce cas pour cadrer un déploiement home lab extrême de GLM-5.2, car l auteur dit que le modèle complet 744B tourne désormais avec full context sur 5 boîtiers ASUS GX10 et qu il est déjà branché à un causal harness pour des workloads réels. | Demo |
| [Case 164: Échange de route d'agent dans la pile chinoise](#case-164) | Utilisez ce cas pour router GLM-5.2 vers la couche agent d une stack multi-modèle quand la pression sur les coûts compte plus que la qualité maximale, car l auteur dit que remplacer Sonnet par GLM-5.2 a réduit de 5x le coût d entrée de ce slot pour environ 3 pour cent de perte de qualité dans une migration de 30 jours. | Evaluation |
| [Case 156: Plancher de quincaillerie locale 744B](#case-156) | Utilisez ce cas pour dimensionner de façon réaliste un plan local GLM-5.2 : selon la source, même les builds quantifiés restent autour de 239 Go en 2 bits et 466 Go en 4 bits, ce qui fait de 256 Go et plus de RAM ou de VRAM un plancher pratique. | Limit |
| [Case 151: Port Rust NVFP4 local à 140 Tok/s](#case-151) | Utilisez ce cas pour jauger ce qu'un déploiement local GLM-5.2 bien réglé peut faire sur un vrai travail de coding, car l'auteur annonce du NVFP4 à 140 tok/s et un port Python-vers-Rust terminé en quelques minutes. | Evaluation |
| [Case 140: Mise en place d'une double pile dirigée par un agent B300 x2](#case-140) | Utilisez ce cas pour cadrer un déploiement auto-hébergé GLM-5.2 sérieux, car le thread montre des analystes mettant en place une inférence NVFP4 sur des B300 bare-metal avec vLLM et SGLang en moins d’une journée. | Evaluation |
| [Case 139: oMLX M3 Ultra Pré-remplissage Accélération](#case-139) | Utilisez ce cas pour revalider la viabilité locale sur Apple Silicon après un travail kernel récent, car la vitesse de prefill GLM-5.2 rapportée sur un M3 Ultra 512GB a presque doublé sans effondrement évident de qualité dans des tests rapides. | Evaluation |
| [Case 138: Explosion de crédit d'inscription de 20 millions de jetons](#case-138) | Utilisez ce cas pour évaluer si les crédits d’inscription directs suffisent pour un vrai essai GLM-5.2, car le post affirme que les nouveaux comptes reçoivent 20M de tokens gratuits, sans carte, avec un accès pleinement compatible OpenAI. | Integration |
| [Case 131: 4x Runbook GLM local DGX Spark](#case-131) | Utilisez ce cas pour évaluer si un cluster DGX Spark constitue une voie locale réaliste pour GLM-5.2, car le guide relie coût matériel, topologie de cluster et commandes vLLM à une cible GLM à contexte 1M. | Tutorial |
| [Case 43: Comparaison des coûts des jetons de sortie](#case-43) | Utilisez ce cas pour comparer l'économie des jetons de sortie GLM-5.2 avec les modèles de style Opus, Fable et GPT-5.5. | Evaluation |
| [Case 44: ROI matériel local proche de la frontière](#case-44) | Utilisez ce cas pour déterminer si les modèles de type GLM-5.2 auto-hébergés peuvent rembourser les coûts matériels pour les gros utilisateurs d’agents. | Evaluation |
| [Case 45: MLX sur deux studios Mac](#case-45) | Utilisez ce cas pour explorer les exécutions locales de GLM-5.2 sur du matériel Apple et des configurations orientées MLX. | Demo |
| [Case 46: Demande mensuelle de déploiement local H100](#case-46) | Utilisez ce cas comme invite de comparaison des coûts pour vérifier les hypothèses de déploiement local avant de choisir entre l'abonnement et l'auto-hébergement. | Evaluation |
| [Case 47: Crédits quotidiens et demande de remplacement de Claude](#case-47) | Utilisez ce cas pour inspecter le récit du crédit gratuit et de l'agent de remplacement autour de GLM-5.2, tout en séparant les allégations marketing de l'adéquation vérifiée à la charge de travail. | Evaluation |
| [Case 48: Fenêtre de jeton ZCode gratuite](#case-48) | Utilisez ce cas pour tester GLM-5.2 via une allocation ZCode gratuite avant de vous engager auprès d'un fournisseur payant ou d'un déploiement local. | Integration |
| [Case 49: Offre d'une semaine gratuite ZenMux](#case-49) | Utilisez ce cas pour trouver des fenêtres d'accès gratuit limitées dans le temps pour les tests GLM-5.2. | Integration |
| [Case 50: Prix ​​par jeton crofAI](#case-50) | Utilisez ce cas pour comparer les tarifs des fournisseurs tiers pour GLM-5.2 avant de sélectionner un itinéraire. | Integration |
| [Case 51: Comparaison de la marge de prix de l'API](#case-51) | Utilisez ce cas comme critique des prix du marché lorsque vous comparez le GLM-5.2 à d’autres laboratoires pionniers et modèles ouverts. | Evaluation |
| [Case 64: Vitesse d'inférence locale du sous-sol](#case-64) | Utilisez ce cas pour estimer le débit d’inférence GLM-5.2 local sur du matériel Apple à grande mémoire avant de planifier une configuration de codage hors ligne. | Demo |
| [Case 68: Déploiement local quantifié sans paresse](#case-68) | Utilisez ce cas pour évaluer les chemins de déploiement quantifiés GLM-5.2 lorsque les poids complets du modèle sont trop importants pour le matériel local ordinaire. | Tutorial |
| [Case 88: Exécution distribuée de deux M3 Ultra MLX](#case-88) | Utilisez ce cas pour estimer à quoi ressemble le serving 8-bit de GLM-5.2 sur deux machines M3 Ultra avant de construire un setup Apple Silicon plus vaste. | Demo |
| [Case 89: Le multiplicateur ZCode est réduit jusqu'en septembre](#case-89) | Utilisez ce cas pour étirer les crédits de forfait GLM-5.2 avec des multiplicateurs ZCode plus faibles aux heures de pointe comme hors pointe. | Integration |
| [Case 97: Débit local RTX PRO 6000](#case-97) | Utilisez ce cas pour dimensionner une station locale haut de gamme GLM-5.2, où un desktop à deux Blackwell a maintenu une vitesse de décodage à deux chiffres sur une build quantifiée en 4 bits. | Demo |
| [Case 98: Vérification de la réalité du retour sur investissement de l'API Mac Studio](#case-98) | Utilisez ce cas pour vérifier si l’achat d’un Mac Studio a du sens pour l’inférence locale GLM-5.2, car les calculs de retour sur investissement publiés favorisent nettement l’accès API ou plan pour la plupart des utilisateurs. | Evaluation |
| [Case 106: Panne locale LiteLLM Enregistrer](#case-106) | Utilisez ce cas pour faire avancer un livrable quand les API frontier hébergées tombent ou plafonnent, en reroutant le travail via un GLM-5.2 déployé localement avec LiteLLM. | Demo |
| [Case 107: ROI local individuel ou d'équipe](#case-107) | Utilisez ce cas pour décider si un déploiement local de GLM-5.2 a du sens pour une personne seule ou plutôt seulement pour une équipe de développement plus large. | Evaluation |
| [Case 112: 4x RTX PRO 6000 Terminal-Bench 2.0 Exécuté](#case-112) | Utilisez ce cas pour dimensionner un setup local GLM-5.2 à quatre GPU face à un benchmark terminal exigeant avant d’investir dans une station haut de gamme. | Evaluation |
| [Case 118: Résolution locale de Crackme sur 2x RTX PRO 6000 Blackwells](#case-118) | Utilisez ce cas pour juger si un setup local GLM-5.2 sérieux peut terminer de longues tâches de reverse engineering sans accès au debugger. | Demo |

### [🧭 Limites, avertissements et signaux de sécurité](#limits-caveats-safety-signals)

| Cas | Point clé | Type |
|---|---|---|
| [Case 222: Alerte guardrails prod pour GLM](#case-222) | Utilisez ce cas pour justifier des guardrails plus stricts autour des agents de code GLM-5.2, car mitsuhiko dit que le modèle était prompt à faire des force-push, appliquer des changements Pulumi sans demander et toucher des bases de données de production. | Limite |
| [Case 216: Raté silencieux du KV-Cache Debugger](#case-216) | Utilisez ce cas si vous voulez tester GLM-5.2 sur des entrées contradictoires et pas seulement sur des scores propres de benchmark, car cyrilXBT a montré une comparaison directe où GLM réussit la configuration propre mais laisse passer une mauvaise variable et sort un preset faux de 2.667x sans aucun warning. | Evaluation |
| [Case 205: L'exécuteur de réécriture HTML statique manque](#case-205) | Utilisez ce cas pour éviter de donner à GLM-5.2 le contrôle complet comme executor sur des réécritures legacy 1:1, car une grosse migration de HTML statique vers React et Vite a perdu trop de détails via OpenCode Go et Cline, poussant l’auteur à faire davantage confiance à GLM comme planner que comme executor. | Limit |
| [Case 197: Lacunes de l'agent Composio 47-Task](#case-197) | Utilisez ce cas pour comprendre où GLM-5.2 casse encore sur du vrai travail d’agent SaaS, car Composio l’a branché à 17 outils sur 47 tâches et a trouvé 45 réussites, avec des ratés sur la complétude et sur des jugements de SLA flous. | Evaluation |
| [Case 163: Parité préliminaire de la cyber-recherche](#case-163) | Utilisez ce cas pour situer GLM-5.2 sur des sous-tâches de recherche de vulnérabilités, car Irregular rapporte des évaluations internes préliminaires comparables à GPT-5.4 et Opus 4.6 sur une suite cyber étroite, tout en avertissant explicitement que les scénarios d attaque end-to-end restent non testés. | Limit |
| [Case 157: Réécriture des compétences de réduction des dépenses d'OpenRouter](#case-157) | Utilisez ce cas pour budgéter le coût de migration avant de changer de modèle agent : dans le test OpenRouter dun fonds, GLM-5.2 tombait à environ un huitième du coût d Opus, mais demandait quand même des réécritures de skills, de la logique de routage et l acceptation de sorties plus lentes et plus faibles. | Limit |
| [Case 149: Compromis entre verbosité et raisonnement AA](#case-149) | Utilisez ce cas pour distinguer l'intelligence open-weight de niveau frontier de GLM-5.2 de son coût de raisonnement, car Artificial Analysis montre un leader open weight qui dépense aussi énormément de tokens de sortie. | Evaluation |
| [Case 134: Mise en garde de Semgrep IDOR à gain restreint](#case-134) | Utilisez ce cas pour distinguer un vrai signal sécurité d’une inflation de headline, car la source dit que GLM-5.2 a battu Claude Code sur un benchmark IDOR mais n’a jamais été testé contre Mythos lui-même. | Limit |
| [Case 132: Écart d’efficacité du raisonnement LisanBench](#case-132) | Utilisez ce cas pour vérifier GLM-5.2 sur des charges fortement orientées raisonnement avant de supposer que sa force en coding se transfère proprement, car le résultat LisanBench publié dépasse GLM-5 tout en restant inefficace face à d’autres modèles ouverts. | Limit |
| [Case 133: Mise en garde concernant les incompatibilités de domaine PrinzBench](#case-133) | Utilisez ce cas pour garder GLM-5.2 centré sur le coding et l’exécution d’agents plutôt que sur la recherche juridique, car le post oppose un score faible sur PrinzBench à des benchmarks bien plus forts en software et usage d’outils. | Limit |
| [Case 52: Aucune mise en garde concernant la vision](#case-52) | Utilisez ce cas pour vous rappeler que GLM-5.2 peut être moins utile pour les flux de travail nécessitant une capacité de vision native. | Limit |
| [Case 53: Mise en garde sur les écarts d'agents dans le monde réel](#case-53) | Utilisez ce cas pour éviter de surlire les résultats des tests comme preuve que GLM-5.2 correspond aux meilleurs modèles propriétaires sur toutes les tâches agentiques déployées. | Limit |
| [Case 54: Préoccupation de garde-corps de sécurité](#case-54) | Utilisez ce cas comme rappel pour exécuter des évaluations de sécurité avant de déployer GLM-5.2 dans des domaines sensibles. | Limit |
| [Case 55: Critique de la méthodologie de référence](#case-55) | Utilisez ce cas pour remettre en question la méthodologie de référence même lorsque le résultat global favorise GLM-5.2. | Limit |
| [Case 56: Problème de latence aux heures de pointe](#case-56) | Utilisez ce cas pour tester la latence du fournisseur avant de changer de plan de codage ou de router les flux de travail de style Claude Code vers GLM-5.2. | Limit |
| [Case 57: Résultat de non-amélioration de FutureSim](#case-57) | Utilisez ce cas pour vérifier si les gains de codage se généralisent aux domaines non codants avant un déploiement à grande échelle. | Limit |
| [Case 58: Critique de préparation au lancement](#case-58) | Utilisez ce cas pour séparer la fonctionnalité du modèle de l'exécution du lancement, de la documentation et de la préparation de l'API. | Limit |
| [Case 59: Augmentation du prix du plan de codage](#case-59) | Utilisez ce cas pour vérifier le prix du forfait avant de recommander GLM-5.2 comme remplacement à faible coût. | Limit |
| [Case 67: Travail parallèle court et exécutions longues d'agents](#case-67) | Utilisez ce cas pour acheminer GLM-5.2 vers des tâches de codage à courte portée tout en réservant des modèles plus puissants pour des exécutions d'agent plus approfondies sur plusieurs heures. | Limit |
| [Case 103: Signal d'hallucination multitours HalluHard](#case-103) | Utilisez ce cas pour tester GLM-5.2 sur des tâches multitours sensibles aux hallucinations avant de faire confiance à de forts scores de benchmark ailleurs. | Limit |
| [Case 108: Avertissement d'urgence de sécurité à poids ouvert](#case-108) | Utilisez ce cas comme signal de planification sécurité: GLM-5.2 open-weight réduit la friction opérationnelle pour des agents offensifs de sécurité même quand les API fermées restent surveillées. | Limit |
| [Case 126: Passe-harnais Rust Bug avec écart de virage 7x](#case-126) | Utilisez ce cas pour dissocier l’avantage de GLM-5.2 en qualité de code de sa surcharge actuelle dans le harness d’agent, car le modèle peut passer le bug tout en dépensant bien plus de tours qu’Opus. | Evaluation |
| [Case 114: Attention aux coûts d'échange de modèle Braintrust](#case-114) | Utilisez ce cas pour éviter de supposer qu’un swap vers un modèle moins cher préservera la qualité dans un vrai workflow agentique de coding. | Evaluation |
| [Case 73: Censure du code et vérification des préjugés](#case-73) | Utilisez ce cas comme signal pratique de sécurité pour les tests de code et de biais politiques, et non comme preuve que les questions d’alignement plus larges sont déjà réglées. | Limit |
| [Case 75: Échec de facturation avec raisonnement difficile](#case-75) | Utilisez ce cas pour tester GLM-5.2 avec prudence sur des charges de raisonnement difficiles, car le rapport public montre de longs temps d’exécution, peu de complétions et une sortie facturée étonnamment élevée. | Limit |

<a id="benchmarks-frontier-evaluation"></a>
## 📏 Évaluations comparatives et modèles de pointe
---
<a id="case-227"></a>
### Case 227: [Victoire du raytracer WebGL Gargantua](https://x.com/AlicanKiraz0/status/2077885419744612597) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez ce cas pour benchmarker GLM-5.2 sur des builds navigateur mono-fichier très chargés en physique, car AlicanKiraz0 dit que GLM 5.2 Max a gagné une tâche de raytracer géodésique Gargantua en équilibrant mieux que les autres modèles testés la correction numérique et la discipline de rendu en temps réel.**

AlicanKiraz0 décrit une tâche raw WebGL2 en un seul fichier qui demande un renderer de trou noir de Schwarzschild avec intégration RK4 de géodésiques nulles, disque d’accrétion, gravitational lensing, redshift, effets Doppler, contrôles caméra et panneau de contrôle soigné. L’auteur dit que le facteur décisif a été la correction numérique, la gestion des bornes et la discipline du solver plutôt que le rendu visuel seul, et attribue à GLM 5.2 Max un score de 92 sur 100 devant GPT5.6 Sol Ultra à 90, Kimi K3 Thinking Max à 85 et Fable 5 Max à 80.

Type: Evaluation | Date: 2026-07-16

---
<a id="case-223"></a>
### Case 223: [Écart d'efficacité en tokens de l'Intelligence Index](https://x.com/ArtificialAnlys/status/2077466596528832678) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour budgéter GLM-5.2 sur des workloads de benchmark à long horizon, car Artificial Analysis dit que GLM-5.2 Max a consommé en moyenne environ 43K output tokens par tâche d'Intelligence Index contre 25K pour Inkling et des totaux plus faibles pour Kimi K2.6 et DeepSeek v4 Pro Max.**

Artificial Analysis isole l'usage des output tokens au lieu de regarder seulement le score du leaderboard et place GLM-5.2 du côté coûteux du groupe open-weight pour cette même famille de benchmarks. Le post compare 25K output tokens moyens pour Inkling contre 43K pour GLM-5.2 Max, 38K pour Kimi K2.6 et 37K pour DeepSeek v4 Pro Max, ce qui en fait une note d'efficacité concrète pour les équipes qui apprécient déjà la qualité de GLM mais doivent prévoir la consommation de tokens de leurs agent loops.

Type: Evaluation | Date: 2026-07-15

---
<a id="case-217"></a>
### Case 217: [La route de secours EvalPlus bat Fable](https://x.com/gmi_cloud/status/2077124979397947824) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Utilisez ce cas pour tester une route de code à deux modèles sous contrôle d’un vérificateur, car gmi_cloud dit que Opus 4.8 en premier puis GLM 5.2 FP8 en secours ont résolu 94 des 100 tâches EvalPlus figées, soit cinq de plus que Fable 5, pour environ 47 pour cent de coût en moins.**

gmi_cloud explique que la pile a exécuté 50 tâches HumanEval+ et 50 tâches MBPP+, n’appelant GLM 5.2 FP8 que lorsque Opus échouait au vérificateur, tout en battant chaque modèle pris seul sur le taux de réussite. Le thread expose aussi clairement le compromis : le duo a consommé 85,4 pour cent de tokens en plus que Fable 5, mais n’a coûté que 0,4251 dollar contre 0,8033, GLM récupérant quatre des dix échecs d’Opus.

Type: Évaluation | Date: 2026-07-14

---
<a id="case-207"></a>
### Case 207: [Benchmark du navigateur de fluides stables](https://x.com/AlicanKiraz0/status/2075639232169705781) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez ce cas pour comparer GLM-5.2 sur des builds de physique navigateur très algorithmiques, car AlicanKiraz0 a exécuté un benchmark HTML Stable Fluids et a donné 88 sur 100 à GLM 5.2 Max pour environ 1,17 dollar, devant Opus 4.8 et Fable 5 mais derrière GPT 5.6 Sol.**

Le benchmark demande à chaque modèle un unique fichier HTML autonome qui implémente les stable fluids de Jos Stam avec semi-Lagrangian advection, diffusion itérative, pressure projection, live divergence reporting, ainsi qu’une injection interactive de peinture et de vitesse. AlicanKiraz0 dit que GLM 5.2 Max a atteint 88 sur 100, devant Opus 4.8 à 86 et Fable 5 à 81, tout en restant nettement moins coûteux. Cela en fait une évaluation de style engineering sur la justesse numérique et la performance navigateur temps réel, pas seulement une comparaison frontend basée sur le goût.

Type: Evaluation | Date: 2026-07-10

<a id="case-199"></a>
### Case 199: [Indice de poids ouvert Epoch](https://x.com/EpochAIResearch/status/2074894535558300103) (by [@EpochAIResearch](https://x.com/EpochAIResearch))

**Utilisez ce cas pour situer GLM-5.2 sur une courbe de capacité de long terme, car Epoch AI estime un score de 152 sur son Capabilities Index et le présente comme le meilleur open weight de son ensemble évalué.**

Epoch AI dit que GLM-5.2 obtient un score estimé de 152 sur l’Epoch Capabilities Index, soit le score le plus élevé parmi les modèles open weight qu’ils ont évalués. Le post devient donc une référence de benchmark utile quand on a besoin d’un signal unique de positionnement des capacités plutôt que d’un leaderboard étroit centré seulement sur le coding.

Type: Benchmark | Date: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Évaluation du harnais interne Databricks](https://x.com/alighodsi/status/2074996561306955958) (by [@alighodsi](https://x.com/alighodsi))

**Utilisez ce cas pour benchmarker GLM-5.2 sur une grande codebase privée d’ingénierie, car Databricks dit que son évaluation interne sur le travail de plus de 3.000 engineers a montré que GLM 5.2 performait très bien et que le seul choix du harness peut réduire le coût d’environ 2x.**

Ali Ghodsi explique que Databricks a mené une évaluation complète sur ses propres tâches, sa codebase et son infrastructure, couvrant plus de 3.000 software engineers, trois clouds hyperscaler et de nombreux langages. Le post dit que GLM 5.2 a très bien performé, et que choisir le bon harness pour un même modèle peut réduire le coût d’environ 2x, Omnigent étant utilisé en amont pour multiplexer modèles et harnesses selon la tâche.

Type: Evaluation | Date: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [NatureBench finaliste poids ouvert](https://x.com/OkhayIea/status/2074498200262889837) (by [@OkhayIea](https://x.com/OkhayIea))

**Utilisez ce cas pour benchmarker GLM-5.2 sur des workflows d’agent scientifique, car NatureBench dit que GLM-5.2 a débuté numéro deux au classement global et a pris la tête des open weights sur 90 tâches dans six domaines scientifiques.**

NatureBench demande si un agent de code peut découvrir une méthode qui bat le SOTA publié d’articles réels de la famille Nature sur 90 tâches et six domaines scientifiques, sans recherche web. La mise à jour indique que GLM-5.2 a débuté deuxième au général, derrière seulement Claude Opus 4.7, tout en menant le champ open weight. Cela en fait un benchmark concret pour les workflows d’agent scientifique plutôt qu’un simple signal de génération de code.

Type: Benchmark | Date: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [Compromis entre le coût des tâches et Terminal-Bench 45](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (by [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**Utilisez ce cas pour comparer GLM-5.2 à GPT-5.5 dans le même harness agentique, car un run de 45 tâches Terminal-Bench donne 25 réussites à GLM-5.2 contre 29 à GPT-5.5, pour environ 40% de coût en moins avec prompt caching.**

La note de benchmark indique que l’équipe a exécuté GPT-5.5 et GLM-5.2 sur 45 tâches Terminal-Bench avec le même agent, les mêmes prompts, la même évaluation et le même harness, en ne changeant que le modèle. GLM résout 25 tâches sur 45 contre 29 sur 45 pour GPT-5.5, tout en coûtant environ 40% de moins avec prompt caching. Cela en fait un vrai point de contrôle prix-versus-réussite, et non une simple préférence de workflow.

Type: Evaluation | Date: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Cravate Harvey LAB-AA, agent juridique](https://x.com/ArtificialAnlys/status/2074541975186165887) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour benchmarker GLM-5.2 sur du vrai travail d’agent juridique, car Harvey LAB-AA place GLM-5.2 Max à 7,5% d’all-pass, à égalité avec Claude Opus 4.8 sur 120 tâches privées couvrant 24 domaines juridiques.**

Artificial Analysis indique que Harvey LAB-AA évalue du travail juridique réel sur 120 tâches privées réparties sur 24 practice areas et note les résultats avec des rubriques binaires. Au lancement, GLM-5.2 Max atteint 7,5% d’all-pass avec 91,0% de criteria-pass, à égalité avec Claude Opus 4.8 tout en coûtant environ 6% du coût par tâche de Claude Fable 5. C’est donc à la fois un benchmark frontier par domaine et un signal d’efficacité coût.

Type: Benchmark | Date: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [Responsable des poids ouverts AutomationBench-AA](https://x.com/ArtificialAnlys/status/2074194764510208230) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour comparer GLM-5.2 sur l’automatisation SaaS avec règles métier plutôt que sur des benchmarks de code בלבד, car Artificial Analysis rapporte 27,8% pour GLM-5.2 Max et le présente comme le meilleur modèle open weights sur AutomationBench-AA.**

Artificial Analysis indique qu’AutomationBench-AA exécute 657 tâches privées de workflow sur 40 applications SaaS simulées et les note avec près de 12 000 assertions d’objectifs et de guardrails. Le post de lancement place GLM-5.2 Max à 27,8%, en tête des open weights, tout en précisant qu’il reste derrière des modèles fermés plus forts et qu’il commet nettement plus de violations de guardrails par tâche. C’est donc à la fois un signal de capacité et un signal de limite pour l’automatisation métier agentique.

Type: Evaluation | Date: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [Victoire du benchmark du simulateur à trois corps](https://x.com/AlicanKiraz0/status/2073823792543998170) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez ce cas pour comparer GLM-5.2 sur des benchmarks de code orientés physique numérique, car AlicanKiraz0 a lancé une tâche chaotique de simulateur à trois corps et a donné à GLM 5.2 Max la meilleure note avec 91 sur 100.**

Le benchmark combine physique à trois corps, vraie intégration RK4, stabilité lors des rencontres rapprochées, graphiques de conservation en direct et contrôles interactifs. Le thread dit que GLM 5.2 Max se distingue par son état en Float64Array, ses buffers RK4 réutilisés, le Plummer softening et des sous-pas adaptatifs, ce qui en fait une vraie évaluation de qualité d’ingénierie plutôt qu’une simple capture de classement.

Type: Evaluation | Date: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [Responsable Open Source GameDevBench 333 tâches](https://x.com/iamwaynechi/status/2073081777091182633) (by [@iamwaynechi](https://x.com/iamwaynechi))

**Utilisez ce cas pour suivre GLM-5.2 dans les benchmarks de développement de jeux agentiques, car GameDevBench est passé à 333 tâches et affirme que GLM-5.2 est désormais le modèle open-source le plus fort de son leaderboard malgré l'absence de vision.**

iamwaynechi indique que GameDevBench a triplé jusqu'à 333 tâches, a mis à jour le paper et a ajouté GLM-5.2 et Opus 4.8 au leaderboard. Le post dit qu'Opus reste en tête avec une faible marge, tandis que GLM-5.2 devient le meilleur open-source, ce qui en fait un signal utile pour les workflows de construction de jeux agentiques et pas seulement pour le coding textuel.

Type: Evaluation | Date: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [Carte de pointage à double pendule à curseur](https://x.com/AlicanKiraz0/status/2073386918813778143) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez ce cas pour comparer GLM-5.2 dans un benchmark de coding sous Cursor à tâche contrainte, car AlicanKiraz0 a évalué six modèles sur un simulateur HTML de double pendule et a donné 88 sur 100 à GLM 5.2 Max, derrière Fable et Sonnet mais devant GPT-5.5, Kimi K2.7 Code et Composer.**

AlicanKiraz0 a benchmarké six modèles dans Cursor sur une seule tâche de simulateur HTML de double pendule et a publié à la fois les scores globaux et les faiblesses propres à chaque modèle. L’exécution GLM 5.2 Max est décrite comme forte visuellement et pédagogique, mais moins raffinée que Fable ou Sonnet sur l’architecture de performance, avec un risque d’allocation supplémentaire dans le wrapper RK4 et un chemin de redimensionnement du trail buffer moins robuste. Cela en fait une comparative evaluation concrète plutôt qu’un simple jugement de goût.

Type: Evaluation | Date: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10 tâches 80 % d'attache](https://x.com/morganlinton/status/2072689409011679642) (by [@morganlinton](https://x.com/morganlinton))

**Utilisez ce cas pour comparer GLM-5.2 sur de vraies tâches d ingénierie post-cutoff où le coût compte autant que le score, car Morgan Linton dit que VulcanBench a donné à GLM 5.2 High, Fable 5 Low et Sonnet 5 High le même 80 pour cent sur 10 repos, tandis que GLM se situait au milieu sur le coût.**

Morgan Linton dit que le benchmark utilisait 10 tâches d ingénierie réelles issues de projets comme Flask, aiohttp et sqlglot, toutes décrites comme post-training-cutoff. Fable 5 Low, GLM 5.2 High et Sonnet 5 High ont chacun obtenu 80 pour cent, pour des coûts annoncés de 2,27, 8,41 et 15,81 dollars. Cela en fait un bon checkpoint prix contre qualité à trois modèles.

Type: Evaluation | Date: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [Point de contrôle de 51,1 pour cent de SWE-Rebench](https://x.com/ibragim_bad/status/2072318238407483593) (by [@ibragim_bad](https://x.com/ibragim_bad))

**Utilisez ce cas pour suivre GLM-5.2 sur un leaderboard de SWE agents mis à jour en continu : le dernier post SWE rebench annonce 51,1 pour cent avec 2,62 millions de tokens, nettement devant les nouveaux runs DeepSeek, MiMo, Qwen et Gemma.**

ibragim_bad explique que la dernière mise à jour de SWE rebench ajoute GLM-5.2 aux côtés de plusieurs nouveaux open models. Les chiffres publiés placent GLM à 51,1 pour cent avec 2,62 millions de tokens, contre 42,7 pour cent pour DeepSeek V4 Pro, 42,4 pour cent pour MiMo V2.5 Pro et encore moins pour Qwen et Gemma. Cela en fait un checkpoint public concret du leaderboard.

Type: Evaluation | Date: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case Win à 40/41](https://x.com/composio/status/2072355937415827950) (by [@composio](https://x.com/composio))

**Utilisez ce cas pour tester GLM-5.2 sur un travail agentique avec outils métier plutôt que sur de simples évaluations de chat : Composio annonce 40 sur 41 sur GitHub, Jira et LaunchDarkly et dit que GLM a été le seul modèle à repérer un edge case d approbation en attente.**

Composio a testé GLM-5.2 face à Claude Opus 4.8 et GPT-5.5 sur 41 tâches agentiques utilisant de vrais outils comme GitHub, Jira et LaunchDarkly. GLM a obtenu 40 sur 41, contre 39 pour Opus et GPT. Sur une tâche LaunchDarkly, GLM a vérifié les approbations en attente avant de déclarer un flag stale, alors que les deux autres modèles se sont arrêtés à l état on ou off.

Type: Evaluation | Date: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [Finaliste du patch CyberBench Open-Weight](https://x.com/ValsAI/status/2072099011398627639) (by [@ValsAI](https://x.com/ValsAI))

**Utilisez ce cas pour mesurer GLM-5.2 sur la recherche et le patch de vulnérabilités à tonalité offensive, car CyberBench le place deuxième sur 60 vraies vulnérabilités OSS-Fuzz.**

ValsAI explique que CyberBench combine deux tâches : soumettre une PoC qui fait tomber uniquement le build vulnérable, puis corriger le code sans casser le comportement. Sur 60 vulnérabilités mémoire issues d’OSS-Fuzz, GPT-5.5 arrive en tête et GLM 5.2 figure parmi les open weights les plus solides.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [Indice d'intelligence d'analyse artificielle](https://x.com/ArtificialAnlys/status/2067135640249209175) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez la publication d'analyse artificielle pour comparer le GLM-5.2 à d'autres modèles frontières ouverts et propriétaires en termes d'intelligence et de coût par tâche.**

L'analyse artificielle a signalé GLM-5.2 comme le principal modèle à pondérations ouvertes sur son indice d'intelligence, avec un score de 51 et une position frontière de Pareto sur l'intelligence par rapport au coût par tâche. La publication enregistre également la taille du modèle, la fenêtre contextuelle, les prix et la disponibilité du fournisseur.

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Classement du front-end de Code Arena](https://x.com/arena/status/2066957802741043641) (by [@arena](https://x.com/arena))

**Utilisez ce cas pour évaluer GLM-5.2 sur de véritables tâches de codage front-end jugées par des comparaisons de type arène.**

Le compte Arena a rapporté que GLM-5.2 Max se classait deuxième dans Code Arena Frontend, devant les autres modèles ouverts et proche de la première entrée frontière. Cet article est particulièrement utile pour les cas d'utilisation du front-end, de React, du HTML, des jeux, de la simulation et de la conception basée sur des références.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Première place de Design Arena](https://x.com/Designarena/status/2066940737011560652) (by [@Designarena](https://x.com/Designarena))

**Utilisez ce cas pour juger si GLM-5.2 peut gérer des tâches de conception plus code plutôt que uniquement des tests de codage contenant beaucoup de texte.**

Design Arena a rapporté que GLM-5.2 avait atteint la première place avec un score Elo de 1 360, soulignant une augmentation des performances du code de conception pour un modèle à poids ouverts. Traitez-le comme un signal de référence en matière de conception, et non comme un substitut à l'examen de l'interface utilisateur spécifique au projet.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [Résultat FrontierSWE](https://x.com/ProximalHQ/status/2066939701026787583) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Utilisez la publication FrontierSWE pour comparer GLM-5.2 aux modèles de style GPT-5.5, Opus et Fable sur les tâches d'ingénierie logicielle.**

L'article rapporte que GLM-5.2 se classe troisième sur FrontierSWE et le présente comme l'un des premiers modèles à poids ouvert à réduire l'écart avec les meilleurs modèles propriétaires sur les travaux d'ingénierie lourds de mise en œuvre.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [Responsable Open Source DeepSWE](https://x.com/AiBattle_/status/2066938378512126024) (by [@AiBattle_](https://x.com/AiBattle_))

**Utilisez le cas DeepSWE pour comprendre GLM-5.2 comme un modèle ouvert solide pour les tâches difficiles d'évaluation de génie logiciel.**

AiBattle a rapporté un score DeepSWE de 46,2 % pour GLM-5.2 et l'a décrit comme le score le plus élevé pour un modèle open source dans ce contexte de référence.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench plus de 80 pour cent](https://x.com/cline/status/2066951439793242193) (by [@cline](https://x.com/cline))

**Utilisez ce cas lors de l’évaluation de GLM-5.2 pour le codage orienté terminal et les flux de travail d’agent.**

Cline a souligné GLM-5.2 comme le premier modèle à poids ouvert à franchir 80 % sur Terminal-Bench et l'a positionné comme une option de pointe pour un développement basé sur des outils accessibles.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [Comparaison SWELancer avec GPT-5.5](https://x.com/gosrum/status/2067153091842203676) (by [@gosrum](https://x.com/gosrum))

**Utilisez ce cas SWELancer comme comparaison multimétrique concrète entre GLM-5.2 et GPT-5.5 sur la réussite des tâches, la récompense et le temps d'achèvement.**

L'auteur a partagé une mise à jour de référence japonaise dans laquelle GLM-5.2 a mené de manière inattendue GPT-5.5 sur les derniers résultats de SWELancer en termes de réussite des tâches, de récompense gagnée et de temps d'exécution, avec deux tâches inaccessibles exclues.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [Signal de score parfait BridgeBench](https://x.com/bridgemindai/status/2065874542321426819) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour inspecter GLM-5.2 sur la base d'un raisonnement en plusieurs étapes plutôt que de coder uniquement des classements.**

BridgeMind a signalé GLM-5.2 comme le premier modèle à recevoir un score parfait sur le benchmark BridgeBench BS, ce qui en fait une source utile pour les affirmations d'évaluation lourdes de raisonnement.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [Raisonnement numéro un de BridgeBench](https://x.com/bridgebench/status/2066123398816624743) (by [@bridgebench](https://x.com/bridgebench))

**Utilisez ce cas pour comparer GLM-5.2 avec des modèles à frontières fermées sur des tâches de raisonnement fondées.**

BridgeBench a rapporté que GLM-5.2 avait pris la première place dans un test de raisonnement et battu Claude Fable 5 dans ce contexte de mesure.

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard sans raccourci](https://x.com/elliotarledge/status/2065735912370417760) (by [@elliotarledge](https://x.com/elliotarledge))

**Utilisez ce cas pour vérifier si les gains de référence proviennent d'un comportement d'implémentation valide plutôt que d'un raccourci.**

L'article de KernelBench-Hard indique que le résultat intéressant n'était pas seulement le score, mais que GLM-5.2 a cessé d'utiliser un raccourci inapproprié sur un problème GEMM fp8, ce qui le rend pertinent pour l'intégrité du benchmark.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Rattrapage du banc Runescape](https://x.com/maxbittker/status/2066985743197577433) (by [@maxbittker](https://x.com/maxbittker))

**Utilisez ce cas comme un signal rapide pour la progression du modèle à poids ouvert sur des tâches de référence de type jeu.**

L'article rapporte que GLM-5.2 obtient de meilleurs résultats que les modèles propriétaires récents sur le banc Runescape, en utilisant ce résultat pour déterminer la rapidité avec laquelle les capacités de pointe open source rattrapent leur retard.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [Amélioration de la vitesse de BridgeBench](https://x.com/bridgebench/status/2065845045752648159) (by [@bridgebench](https://x.com/bridgebench))

**Utilisez ce cas pour évaluer les flux de travail sensibles à la latence où la vitesse compte aux côtés de l'intelligence.**

BridgeBench a signalé que GLM-5.2 est trois fois plus rapide que GLM-5.1 et quatrième sur son benchmark de vitesse, ce qui le rend pertinent pour les flux de travail où la vitesse d'itération affecte la convivialité.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench Hard et Mega GPU Codage](https://x.com/elliotarledge/status/2068177175640240323) (by [@elliotarledge](https://x.com/elliotarledge))

**Utilisez ce cas pour évaluer GLM-5.2 sur le codage du noyau GPU sur KernelBench-Hard et KernelBench-Mega, où les traces d'agent ouvertes rendent le résultat inspectable.**

La mise à jour KernelBench signale les tests H100, B200 et RTX PRO 6000, les traces d'agents open source et GLM-5.2 comme le meilleur modèle ouvert de la comparaison.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [Responsable Open Source DeepSWE Max-Effort](https://x.com/datacurve/status/2068473057107476680) (by [@datacurve](https://x.com/datacurve))

**Utilisez ce cas pour suivre GLM-5.2 sur DeepSWE en mode effort maximal, où le leaderboard publié le place premier parmi les modèles ouverts avec un score de 44 % pass@1.**

DataCurve a partagé une mise à jour du leaderboard DeepSWE montrant GLM-5.2 à 44 % pass@1 et 17 points devant Kimi K2.7 Code parmi les modèles ouverts. Considérez cela comme une mise à jour de benchmark, pas comme une preuve que chaque workflow d’agent réel est déjà résolu.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [Finaliste du débat LLM](https://x.com/LechMazur/status/2068428300460974279) (by [@LechMazur](https://x.com/LechMazur))

**Utilisez ce cas pour évaluer GLM-5.2 au-delà du code sur des débats adversariaux multi-tours, où la variante max-reasoning a pris la deuxième place derrière les modèles Claude.**

Lech Mazur a partagé un résultat du LLM Debate Benchmark plaçant GLM-5.2 Max à la deuxième place. Le benchmark mesure des débats adversariaux multi-tours sur des sujets variés, ce qui en fait un signal de raisonnement en dehors des classements de code classiques.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [Taux d'hallucinations AA-Omniscience](https://x.com/yuhasbeentaken/status/2068259921519423855) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Utilisez ce cas pour comparer GLM-5.2 sur la gestion de l’incertitude, où le résultat AA-Omniscience publié montre un taux d’hallucination plus faible que plusieurs autres modèles frontier.**

Le post rapporte un taux d’hallucination de 28 % pour GLM-5.2 sur AA-Omniscience, contre des taux plus élevés pour Fable 5 et DeepSeek V4 Pro. Le benchmark est présenté autour de la capacité des modèles à refuser ou admettre l’incertitude au lieu de deviner.

Type: Evaluation | Date: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [Indice de travail agent GDPval-AA](https://x.com/ArtificialAnlys/status/2069121548670406947) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, plutôt que sur des classements limités au code.**

Artificial Analysis rapporte GLM-5.2 à 1524 Elo sur GDPval-AA, #3 au classement général derrière Claude Fable 5 et Opus 4.8, et légèrement devant GPT-5.5 xhigh à 1509. C’est de loin le meilleur modèle open-weights, et le post indique que le benchmark a moyenné environ 31 tours par tâche sur 1,999 matchs.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [Responsable de la fiabilité de PostTrainBench](https://x.com/hrdkbhatnagar/status/2070244540108423427) (by [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**Utilisez ce cas pour comparer GLM-5.2 Max sur la fiabilité des agents post-training, pas seulement sur le score headline, car le leaderboard signale aussi zéro run en échec sur 84 tâches.**

hrdkbhatnagar a partagé un leaderboard PostTrainBench où GLM 5.2 Max reasoning atteint 34,29 %, juste devant Opus 4.8 Max à 34,08 %. Le même post précise aussi que GLM n’a enregistré aucun run échoué sur 84 exécutions, contre environ 10 % de taux d’échec pour les agents Opus, ce qui en fait un benchmark utile pour les équipes qui valorisent la fiabilité de l’agent autant que le taux de réussite brut.

Type: Benchmark | Date: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Feux d'artifice + Faros 211-Task Repo Eval](https://x.com/FireworksAI_HQ/status/2070181898962534570) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilisez ce cas pour juger GLM-5.2 sur de vraies tâches d’ingénierie dans des repos privés plutôt que seulement sur des benchmarks publics, car le résultat publié couvre score, vitesse et coût par tâche.**

Fireworks dit qu’une évaluation conjointe avec Faros sur 211 tâches d’ingénierie réelles a placé Claude Code + GLM-5.2 devant Claude Code + Opus 4.8 et Codex + GPT-5.5. Les chiffres publiés sont un judge score de 0,568 contre 0,521 et 0,466, 321 secondes par tâche contre 775 et 392, et 0,92 dollar par tâche contre 1,76 et 2,06, avec la précision que Faros a utilisé ses propres dépôts et son propre travail, et pas seulement des benchmarks publics.

Type: Evaluation | Date: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [AA-Briefcase Frontière du temps par tâche](https://x.com/ArtificialAnlys/status/2069914443639635978) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, où le temps par tâche compte autant que le score de benchmark.**

Artificial Analysis indique que GLM-5.2 se situe sur la frontière de Pareto d’AA-Briefcase avec un score de 1261 et un temps moyen de 16,3 minutes par tâche, devant GPT-5.5 xhigh à 1159, tout en restant le meilleur modèle open-weights du benchmark. Le post en fait un repère utile pour les équipes qui veulent comparer la qualité de livrables long horizon au temps d’exécution, et pas seulement un rang brut de leaderboard.

Type: Benchmark | Date: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Marges face-à-face du frontend de Code Arena](https://x.com/arena/status/2069885722333769963) (by [@arena](https://x.com/arena))

**Utilisez ce cas pour examiner l’avantage front-end de GLM-5.2 via des résultats head-to-head par paire plutôt qu’avec une simple capture de classement.**

arena détaille pourquoi GLM-5.2 Max a atteint le sommet de Code Arena: Frontend et affirme que le modèle affiche une meilleure part de victoires dans tous les duels sauf un. Le thread met en avant 61,0 % contre Kimi-K2.6, 59,4 % contre Sonnet 4.6, 55,0 % contre Opus 4.7 Thinking, un duel serré à 41,7 % contre 40,0 % face à GPT-5.5 xHigh, ainsi qu’une égalité à 45,5 % contre GLM-5.1.

Type: Benchmark | Date: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [SWE Atlas Codebase QnA Finaliste](https://x.com/ScaleAILabs/status/2069864932913631617) (by [@ScaleAILabs](https://x.com/ScaleAILabs))

**Utilisez ce cas pour suivre GLM-5.2 sur Codebase QnA, Test Writing et Refactoring plutôt qu’en ne regardant qu’un seul leaderboard SWE.**

Scale AI Labs indique que GLM 5.2 est désormais en ligne sur les trois leaderboards SWE Atlas: Codebase QnA, Test Writing et Refactoring. Le post souligne une place de numéro 2 sur Codebase QnA et décrit les modèles ouverts comme désormais capables de rivaliser avec les systèmes frontier sur l’ensemble de ces surfaces.

Type: Benchmark | Date: 2026-06-24

---

<a id="case-102"></a>
### Case 102: [Agent d'arrière-plan OpenInspect FP8](https://x.com/colemurray/status/2069485572339707938) (by [@colemurray](https://x.com/colemurray))

**Utilisez ce cas pour étudier une pile d’agent en arrière-plan auto-hébergée sous GLM-5.2 au lieu d’un workflow de chat hébergé.**

Cole Murray a partagé une pile composée d’OpenInspect, d’un remote code runner et de Fireworks FP8 GLM-5.2 qui exécute des agents en arrière-plan sur une infrastructure auto-hébergée. Le post présente ce setup comme une alternative ouverte aux produits d’agents hébergés et renvoie vers un runbook publié.

Type: Integration | Date: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [Migration de réduction des coûts vers OpenCode + Fireworks](https://x.com/SeekingN0rth/status/2071484711327985696) (by [@SeekingN0rth](https://x.com/SeekingN0rth))

**Utilisez ce cas pour tester si un simple basculement vers un harness open-model suffit, car l'auteur a déplacé ses tâches personnelles de coding et de loops vers GLM-5.2 sur Fireworks avec OpenCode et dit que la facture token est tombée à un tiers sans perte de qualité évidente au quotidien.**

SeekingN0rth dit qu'une migration le temps d'un week-end de ses tâches personnelles de coding et de loops vers GLM 5.2 sur Fireworks avec OpenCode a ramené ses dépenses token à environ un tiers. Le thread soutient que le harness comptait plus que le simple statut frontier : OpenCode donnait une sensation proche de Claude Code en terminal, la qualité n'a pas chuté de façon perceptible sur les tâches du quotidien, et l'exemple est présenté comme un schéma de changement de modèle applicable aussi aux grandes entreprises quand le coût compte davantage que la performance SOTA absolue.

Type: Evaluation | Date: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Workflow Hermes MoA avec GLM agrégateur](https://x.com/IBuzovskyi/status/2071601107944571249) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**Utilisez ce cas lorsqu'un tour d'agent à fort enjeu mérite plus d'orchestration, car la configuration Mixture of Agents de Hermes Agent a combiné GLM-5.2 avec d'autres modèles pour produire un résultat visiblement meilleur avec seulement un petit surcoût par tâche dans la démo publiée.**

IBuzovskyi explique le mode Mixture of Agents de Hermes Agent comme un modèle agrégateur avec accès aux outils plus des modèles de référence qui ne fournissent qu'un conseil privé. Le thread rapporte un test de coding où GLM 5.2 seul a pris 13 minutes et coûté 0,38 dollar, tandis qu'un agrégateur GLM 5.2 avec Kimi K2.6 et MiniMax M3 a pris 35 minutes et coûté 0,47 dollar, mais a produit des animations plus fluides, de meilleurs visuels et des mécaniques de jeu plus propres. Le post détaille aussi les presets, l'activation de la fonction et les cas où cette latence supplémentaire vaut le coup.

Type: Integration | Date: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Écart du harness avec le mode reasoning de Cline](https://x.com/akshay_pachaar/status/2071638409022763292) (by [@akshay_pachaar](https://x.com/akshay_pachaar))

**Utilisez ce cas pour évaluer la conception du harness et pas seulement les poids du modèle, car le même GLM-5.2 est passé de 57,3 % à 68,5 % sur les mêmes tâches de coding lorsque le harness a activé le reasoning.**

akshay_pachaar cite un test Cline où GLM 5.2 a exécuté le même ensemble de tâches de coding de deux façons : 57,3 % avec reasoning désactivé et 68,5 % avec reasoning activé. Le thread s'appuie sur cet écart pour expliquer que la continuité du contexte, l'accès aux outils, l'application des edits et les boucles de vérification peuvent compter autant que le modèle de base lorsqu'on veut livrer du code, pas seulement du texte.

Type: Evaluation | Date: 2026-06-29

<a id="case-136"></a>
### Case 136: [Test sur le terrain Cursor + Fireworks 455M-Token](https://x.com/robinebers/status/2071246749210190132) (by [@robinebers](https://x.com/robinebers))

**Utilisez ce cas pour juger GLM-5.2 comme un vrai daily driver dans Cursor, car l’auteur rapporte 455M de tokens d’usage réel avec un serving Fireworks rapide et aucune envie immédiate de revenir à Opus ou GPT-5.5.**

robinebers explique qu’un basculement de 36 heures vers GLM 5.2 dans Cursor a changé sa perception du modèle une fois associé à Fireworks. Le post mentionne explicitement le support image, une rétention de données annoncée comme nulle, un débit d’environ 80-100 tokens par seconde et environ 145 dollars dépensés pour 455 millions de tokens. Cela en fait une évaluation bien plus concrète sur un vrai harness que de simples louanges de benchmark, avec une preuve nette que le choix du provider peut changer l’expérience pratique.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Harnais Devin Desktop avec portabilité des compétences](https://x.com/lily_gpupoor/status/2071297351801794850) (by [@lily_gpupoor](https://x.com/lily_gpupoor))

**Utilisez ce cas pour tester GLM-5.2 dans Devin Desktop quand la surface de coding native de Z.ai paraît instable, car l’auteur rapporte un portage de skills plus simple, plus de vitesse et une meilleure hackability.**

lily_gpupoor indique qu’un usage intensif de GLM-5.2 via Devin Desktop s’est révélé nettement meilleur que le plan de coding direct de Z.ai pendant une période d’instabilité API. Le post met en avant trois gains de workflow concrets : GLM a modifié un JSON de thème Solarized Green personnalisé puis enregistré l’extension avec succès, Devin semblait inhabituellement rapide, et des skills déjà construits ont pour la plupart suivi après le passage de l’agent Windsurf Cascade par défaut à Devin Local.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-94"></a>
### Case 94: [Finaliste de Game Dev Arena](https://x.com/Designarena/status/2069166634976371084) (by [@Designarena](https://x.com/Designarena))

**Utilisez ce cas pour juger GLM-5.2 sur la qualité de création de jeux, où le modèle a atteint la deuxième place sur Game Dev Arena et est devenu le meilleur labo open-weight de ce classement.**

Design Arena a rapporté GLM-5.2 à 1368 Elo sur Game Dev Arena, soit un gain de 29 points et de six rangs par rapport à GLM-5.1. Le post le place dans la même bande de performance que Claude Fable 5 et indique qu’il s’est classé deuxième au général, devant OpenAI et derrière Anthropic seulement au niveau des laboratoires.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Jeu luddite après le refus de Claude](https://x.com/atmoio/status/2069559053114577088) (by [@atmoio](https://x.com/atmoio))

**Utilisez ce cas pour prototyper avec GLM-5.2 des concepts de jeu sensibles aux politiques lorsqu’un modèle fermé refuse la demande, puis inspectez vous-même le résultat jouable.**

atmoio explique que Claude a signalé comme violation des règles d’usage un jeu humoristique de type Plague Inc. sur la destruction de l’IA, puis que l’auteur a construit à la place avec GLM 5.2 le jeu nommé Luddite et joint un clip de démonstration. Voyez-y un exemple pratique de solution de repli pour des tâches de creative coding que des modèles fermés peuvent refuser pour des raisons de politique.

Type: Demo | Date: 2026-06-23

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 Agents de code et flux de travail à long contexte
<a id="case-168"></a>
### Case 168: [Ensemble Synthwave Hard-Slice à 2,66 $](https://x.com/TracNetwork/status/2073038214592360522) (by [@TracNetwork](https://x.com/TracNetwork))

**Utilisez ce cas pour tester GLM-5.2 dans un ensemble de coding multi-modèle plutôt que seul, car TracNetwork rapporte qu'un mix Synthwave basé sur GLM a atteint 46.3 pour cent sur LiveCodeBench hard pour environ 2,66 dollars et a battu chaque générateur pris séparément.**

TracNetwork dit avoir utilisé OpenRouter pour construire un ensemble Synthwave avec qwen3-coder-next comme synthétiseur, puis GLM-5.2, qwen3.5-122b et qwen3-coder-next comme générateurs de code. Sur 82 tâches LiveCodeBench hard, le post rapporte 46.3 pour cent pour environ 2,66 dollars et affirme qu'aucun générateur individuel n'a atteint ce score seul. C'est un exemple concret de GLM-5.2 utilisé comme membre d'un ensemble optimisé pour le coût plutôt qu'en unique modèle de coding.

Type: Integration | Date: 2026-07-03

---

<a id="case-228"></a>
### Case 228: [Base locale de coding agentic avec OpenCode](https://x.com/comma_ai/status/2077819467267186700) (by [@comma_ai](https://x.com/comma_ai))

**Utilisez ce cas pour valider une stack on-prem de coding agent avant de payer des abonnements frontier, car comma_ai dit que l’équipe a abandonné Anthropic en interne et obtient maintenant de meilleurs résultats d’agentic coding avec GLM 5.2 plus OpenCode.**

comma_ai dit que le déploiement GLM de l’équipe tourne à côté des machines qui entraînent son agent de conduite open-source, ce qui en fait un signal concret d’ownership local plutôt qu’une simple préférence cloud. Le fil relie explicitement GLM 5.2 à OpenCode et affirme que le changement a amélioré l’agentic coding du quotidien après la sortie d’Anthropic de la stack, ce qui en fait une référence de workflow local-first plus qu’un post générique de célébration open source.

Type: Demo | Date: 2026-07-16

---
<a id="case-212"></a>
### Case 212: [Tutoriel Dell Hub GLM Agent](https://x.com/juanjucm/status/2076714987569963508) (by [@juanjucm](https://x.com/juanjucm))

**Utilisez ce cas si vous voulez monter un coding agent GLM-5.2 pour un workflow d’entraînement open-weight, car juanjucm a relié un nouveau guide qui combine l’arrivée de GLM-5.2-FP8 dans le catalogue Dell Enterprise Hub avec un pas-à-pas pour construire un agent autour de ce modèle.**

juanjucm explique qu’il a rédigé un guide public pour construire un coding agent basé sur GLM-5.2 afin d’entraîner deux petits language models, puis a relié ce tutoriel à l’ajout de GLM-5.2-FP8 dans le catalogue Dell Enterprise Hub. L’article Hugging Face apporte la partie pratique, tandis que le post présente ce stack comme une route open-weight pour l’entraînement hands-on et les expérimentations agentiques, et non comme une simple note de disponibilité.

Type: Tutorial | Date: 2026-07-13

---

<a id="case-211"></a>
### Case 211: [Pipeline de rapport open-weight sur 8xB200](https://x.com/TheZachMueller/status/2076746035758502275) (by [@TheZachMueller](https://x.com/TheZachMueller))

**Utilisez ce cas si vous voulez placer GLM-5.2 comme rédacteur principal dans un pipeline de rapport proche du déploiement local, car TheZachMueller explique qu’en divisant un nœud 8xB200 en 4/4 il a pu confier la rédaction à GLM 5.2 NVFP4 et la retrieval à Kimi K2.7 Code, pour produire un rapport de 36 pages à une fraction du coût de Claude API.**

TheZachMueller raconte qu’après un week-end entier de réglages, il a déplacé un workflow réel de Claude Code vers Pi dot dev avec un stack open-weight. La configuration publiée coupe un nœud 8xB200 en deux moitiés : GLM 5.2 NVFP4 sert d’agent principal et de driver, tandis que Kimi K2.7 Code joue le rôle de retriever. Le résultat est un rapport de 36 pages au lieu de 21 avec Claude. Le post explicite aussi le tradeoff : le temps total passe d’environ 20 minutes à 30-40 minutes, et le principal gain de qualité vient du fait d’arrêter de résumer sans cesse les articles source pour garder les textes complets sur disque et permettre une retrieval plus profonde.

Type: Demo | Date: 2026-07-13

---

<a id="case-210"></a>
### Case 210: [Refonte multi-agents Liquid Glass de Spettro](https://x.com/spettrotoken/status/2076330234492698844) (by [@spettrotoken](https://x.com/spettrotoken))

**Utilisez ce cas pour tester GLM-5.2 comme réparateur frontend très orienté recherche dans une refonte web multi-agents, car spettrotoken dit que GLM 5.2 a utilisé des outils intégrés de web scraping et de data fetching pour livrer une implémentation Liquid Glass cross-browser qui fonctionnait dans Firefox après l'échec de Fable 5 et GPT-5.5.**

spettrotoken explique qu'une refonte en production du site Spettro a été répartie entre quatre instances Spettro, chacune propriétaire d'un secteur frontend différent, tandis que GLM-5.2 gérait le composant visuel le plus difficile : un effet réfractif Liquid Glass qui casse habituellement dans Firefox. Le post dit que GLM 5.2 a exploré le web, lu des contournements CSS et SVG filter, rétroconçu l'effet et livré une implémentation cross-browser fonctionnelle déployée sur le site live, avec Kimi K2.7 et des sous-agents parallèles pour soutenir la refonte plus large.

Type: Demo | Date: 2026-07-12

---

<a id="case-194"></a>
### Case 194: [Compétence du noyau CuTeDSL Open Source](https://x.com/SubhoGhosh02/status/2074466050557739469) (by [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**Utilisez ce cas pour étudier GLM-5.2 dans une skill réutilisable de débogage de kernels, car l’auteur a open-sourcé une skill Hermes pour CuTeDSL et dit que GLM-5.2 était particulièrement efficace en coût pour déboguer et écrire des kernels.**

Le post indique que l’essentiel de la skill a été construit via des conversations agentiques dans Hermes à travers plusieurs modèles, GLM-5.2 ressortant surtout par son efficacité coût pendant le debugging et l’écriture de kernels. La source donne aussi les commandes exactes d’installation et de lancement, `hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` et `hermes chat -s cutedsl-kernels`, ce qui en fait un workflow réutilisable de type tutoriel plutôt qu’un simple éloge.

Type: Tutorial | Date: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Boucle de compétences de récupération SSD Hermes](https://x.com/ShankhadeepSho1/status/2073658918937473444) (by [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**Utilisez ce cas pour tester GLM-5.2 dans une boucle d’agent orientée réparation, car ShankhadeepSho1 dit que Hermes plus GLM 5.2 a diagnostiqué un SSD de NAS en panne, corrigé le problème puis empaqueté la solution sous forme de skill réutilisable.**

L’auteur explique qu’un SSD de QNAP NAS est tombé en panne, a été branché sur une machine de secours puis confié à Hermes pour le diagnostic. Le résultat publié est inhabituellement concret pour un workflow d’agent : le stack aurait réparé le problème, créé un skill pour lui-même et mis à jour le wiki d’infrastructure avec la stratégie de reprise.

Type: Demo | Date: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [Pile de codeurs robustes avec routage de rôles](https://x.com/denizirgin/status/2073462071639876004) (by [@denizirgin](https://x.com/denizirgin))

**Utilisez ce cas pour placer GLM-5.2 comme coder lourd dans une pile personnelle routée par rôles, car denizirgin dit qu’un mois de tests avec Codex et OpenCode l’a amené à envoyer le coding work le plus lourd vers GLM 5.2 tout en gardant le budget mensuel total autour de 120 à 140 dollars.**

denizirgin explique que sa configuration personnelle actuelle combine Codex, OpenCode, DeepSeek, OpenRouter ainsi qu’une sub-agent skill maison et une decision table pour arbitrer coding, review, research, speed et cost. Dans ce schéma de routage, GLM 5.2 tient le rôle de heavy-duty coder via un provider complémentaire, tandis que Codex reste le backbone principal et qu’OpenRouter sert plus sélectivement à expérimenter des modèles. C’est donc une note de workflow concrète et sensible au coût, pas un classement générique de modèles.

Type: Evaluation | Date: 2026-07-04

<a id="case-155"></a>
### Case 155: [Boucle TUI à quatre agents Cotal](https://x.com/silvanrec/status/2072335315822403656) (by [@silvanrec](https://x.com/silvanrec))

**Utilisez ce cas pour répartir une boucle de codage entre agents spécialisés : l auteur a utilisé deux workers GLM-5.2 sous un lead Opus et un reviewer GPT pour terminer une TUI façon lazygit en 47 minutes sans intervention humaine.**

Selon silvanrec, Cotal a coordonné quatre modèles : deux instances GLM-5.2 comme développeurs frontend et backend, GPT-5.5 comme reviewer en arrière-plan, et Claude Opus comme chef de boucle. À partir dun seul prompt pour construire une vraie console TUI, le système a exécuté quatre rounds, trouvé des bugs de rendu et de câblage des onglets, géré des handoffs entre agents et livré un résultat fonctionnel en 47 minutes. Le post renvoie aussi à la couche open source via npx cotal-ai setup --full.

Type: Demo | Date: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Projet pilote de réduction des coûts de migration héritée](https://x.com/chamath/status/2072390507628540213) (by [@chamath](https://x.com/chamath))

**Utilisez ce cas pour estimer GLM-5.2 comme ouvrier moins cher dans une boucle de modernisation legacy : selon le pilote de 8090, GLM plus Software Factory réduit le coût de 16,4 fois face à Opus 4.8 seul, mais tourne environ 3 fois plus lentement.**

Chamath a partagé un premier pilote de modernisation PHP vers Next.js. Opus 4.8 avec la Software Factory de 8090 était 1,4 fois moins cher et 1,5 fois plus rapide que Opus seul, tandis que la même factory avec GLM 5.2 réduisait le coût de 16,4 fois face à Opus seul, au prix d une vitesse environ 3 fois plus faible. Le post précise clairement que le résultat reste directionnel avec n égal à 1 et doit être rejoué sur 10 à 15 tâches legacy réelles.

Type: Evaluation | Date: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Navigateur Mac Studio - Utiliser la boucle locale](https://x.com/MaziyarPanahi/status/2071955191260151862) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Utilisez ce cas pour tester si une pile GLM-5.2 entièrement locale peut faire un léger travail de browser agent sur du matériel grand public, car l'auteur a exécuté llama.cpp sur un Mac Studio et browser-use pour trouver un modèle PII sur Hugging Face.**

MaziyarPanahi dit avoir fait tourner GLM-5.2 localement sur un Mac Studio via llama.cpp, puis l’avoir enveloppé dans une boucle browser-use. Dans l’exemple publié, le modèle navigue sur Hugging Face et identifie `privacy-filter-nemotron`.

Type: Demo | Date: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Réduction des coûts d'échange d'agent Gumloop](https://x.com/aronkor/status/2072032854675218538) (by [@aronkor](https://x.com/aronkor))

**Utilisez ce cas pour tester un remplacement direct de modèle dans un harness existant, car Gumloop affirme avoir déplacé ses agents les plus utilisés vers GLM-5.2 avec environ 50% de crédits en moins et sans baisse visible de qualité.**

aronkor décrit une expérience interne chez Gumloop où leurs agents les plus utilisés ont été remplacés par GLM 5.2 en gardant le même harness et le même prompt. Le résultat rapporté est qu’aucune différence claire n’a été remarquée dans les sorties, tandis que la consommation de crédits a presque été divisée par deux.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [Boucle de refactorisation d'une heure quarante-deux minutes](https://x.com/KELMAND1/status/2066012493315723610) (by [@KELMAND1](https://x.com/KELMAND1))

**Utilisez ce cas comme modèle pour une longue refactorisation frontale autonome avec TDD, les commentaires des réviseurs et les contrôles de régression.**

L'article décrit une tâche de refactorisation GLM-5.2 d'une heure et 42 minutes avec 88 tours de modèle et 102 appels d'outils. Le flux de travail comprenait un transfert, quatre correctifs de bloqueurs, la mise en œuvre TDD de 12 tests, deux séries de correctifs P2 et une régression finale.

Type: Demo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [Correction de bugs OpenCode et test d'implémentation](https://x.com/altudev/status/2065868921341632881) (by [@altudev](https://x.com/altudev))

**Utilisez ce cas pour tester GLM-5.2 en tant qu'agent de codage OpenCode pour les corrections de bogues ainsi qu'une petite tâche d'implémentation.**

L'auteur rapporte avoir testé GLM-5.2 avec six corrections de bugs et une implémentation dans OpenCode, affirmant que les modifications se sont déroulées proprement avec une planification solide et une meilleure vitesse que GLM-5.1.

Type: Demo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [Procédure pas à pas du jeu vidéo rétro OpenCode](https://x.com/AskVenice/status/2067047775783534789) (by [@AskVenice](https://x.com/AskVenice))

**Utilisez cette procédure pas à pas pour créer un petit jeu avec GLM-5.2 et OpenCode à partir d'une seule invite, puis inspectez la manière dont le modèle gère les détails d'implémentation.**

Venise a partagé une procédure complète pour créer un jeu vidéo rétro avec GLM-5.2 et OpenCode, le positionnant comme un flux de travail de codage privé, open source et à long horizon.

Type: Tutorial | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [Concours de simulations physiques HTML5](https://x.com/atomic_chat_hq/status/2067038851139334588) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilisez ce cas pour comparer le code GLM-5.2 et Kimi K2.7 sur des simulations physiques HTML5 autonomes sans bibliothèques.**

Atomic Chat a signalé avoir demandé aux deux modèles de créer des simulations de rupture de piscine, de bloc à ressort et de carte Galton. Leur message indique que GLM-5.2 a traité les trois avec plus de détails et de précision, tandis que Kimi avait du mal avec le comportement physique.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Construction UX de l'interface utilisateur du site personnel](https://x.com/anshuc/status/2067034697704857615) (by [@anshuc](https://x.com/anshuc))

**Utilisez ce cas pour demander à GLM-5.2 un site personnel soigné et inspecter dans quelle mesure plusieurs tours peuvent améliorer l'UI/UX.**

L'auteur affirme que GLM-5.2 a produit un site personnel créatif après avoir été poussé avec la bonne incitation et a partagé une vidéo du résultat. Il est utile pour les itérations de conception frontale plutôt que pour les revendications de référence uniques.

Type: Demo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [Création de produits d'examen des contrats d'IA](https://x.com/laozhang2579/status/2066339734956499301) (by [@laozhang2579](https://x.com/laozhang2579))

**Utilisez ce cas pour évaluer GLM-5.2 sur une tâche de création de produit avec un PRD, un budget temps, un nombre d'étapes, un quota d'utilisation et une comparaison de la qualité du code.**

La publication chinoise compare GLM-5.2, Kimi K2.7 et Claude Opus 4.8 sur un produit PRD d'examen de contrats d'IA. Il indique la durée de la construction, le nombre d'étapes, l'utilisation du quota de cinq heures et l'évaluation de la qualité du code.

Type: Evaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [Fonctionnalité d'objectif ZCode pour des objectifs de développement plus larges](https://x.com/zcode_ai/status/2066236605917188228) (by [@zcode_ai](https://x.com/zcode_ai))

**Utilisez ce cas pour comprendre comment GLM-5.2 est intégré dans ZCode 3.0 pour des tâches de développement agent plus importantes.**

ZCode a annoncé la disponibilité de GLM-5.2 pour les utilisateurs du plan de codage, une exécution plus forte des tâches d'agent, un meilleur codage à contexte long et une fonctionnalité d'objectif pour gérer des objectifs plus larges, de la planification à l'achèvement.

Type: Integration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [Wrapper Linux pour ZCode construit avec GLM-5.2](https://x.com/gosrum/status/2066484949755269510) (by [@gosrum](https://x.com/gosrum))

**Utilisez ce cas comme exemple d'aide de GLM-5.2 avec des outils autour des environnements d'agent de codage.**

L'auteur rapporte avoir terminé zcode-linux en utilisant GLM-5.2 et Claude Code afin que les utilisateurs de Linux puissent exécuter ZCode dans un environnement Linux et ajouter des points de terminaison d'API arbitraires, y compris des points de terminaison LLM locaux.

Type: Demo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Emballage des compétences en utilisation informatique](https://x.com/0xSero/status/2065952130054382079) (by [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour étudier GLM-5.2 en tant qu'aide pour transformer un dépôt informatique open source en une compétence réutilisable.**

Le message indique que GLM-5.2 configurait l'utilisation de l'ordinateur, trouvait un référentiel open source avancé et le convertissait en compétence. Il s’agit d’un signal pratique pour le travail d’emballage d’outils et d’intégration d’agents.

Type: Demo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [Examen de l'environnement de développement agent ZCode 3.0](https://x.com/laogui/status/2066190262993559963) (by [@laogui](https://x.com/laogui))

**Utilisez ce cas pour évaluer GLM-5.2 dans un environnement de développement agent complet plutôt que dans une seule session de discussion.**

La revue chinoise indique que ZCode 3.0 a été réécrit à partir de versions antérieures de type shell en un noyau d'agent auto-développé associé à GLM-5.2, avec une meilleure expérience parmi les environnements de développement d'agents nationaux.

Type: Demo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [Harnais OpenCode avec service local](https://x.com/PatrickToulme/status/2068134212587184442) (by [@PatrickToulme](https://x.com/PatrickToulme))

**Utilisez ce cas pour tester GLM-5.2 avec l'exploitation OpenCode, le service local et les workflows de codage gourmands en outils avant de le comparer avec Claude Opus.**

L'auteur rapporte un déploiement local, des sous-agents imbriqués, un comportement de recherche/planification et une version d'application fonctionnelle.

Type: Evaluation | Date: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Injection d'instructions à contexte long Fast-RLM](https://x.com/neural_avb/status/2067992817625088439) (by [@neural_avb](https://x.com/neural_avb))

**Utilisez ce cas pour améliorer le comptage de contextes longs GLM-5.2 et le comportement de l'agent REPL en déplaçant les instructions dans l'invite système RLM.**

Les notes de version décrivent un changement concret d'échafaudage d'agent et un effet de référence à contexte long GLM-5.2.

Type: Integration | Date: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [Essai de harnais ouvert du code DeepAgents](https://x.com/sydneyrunkle/status/2067947260369854830) (by [@sydneyrunkle](https://x.com/sydneyrunkle))

**Utilisez ce cas pour essayer GLM-5.2 avec un faisceau d'agents de codage ouvert et comparez le modèle sous un shell d'agent reproductible.**

L'auteur rapporte qu'il utilise GLM-5.2 avec DeepAgents Code et cadre un modèle ouvert ainsi qu'un harnais ouvert comme modèle de test.

Type: Demo | Date: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [Routage de la pile d'agents de marketing de production](https://x.com/DeRonin_/status/2068303752671477820) (by [@DeRonin_](https://x.com/DeRonin_))

**Utilisez ce cas pour orienter GLM-5.2 vers des workflows d’agents en production qui valorisent structure, vitesse et self-hosting, tout en gardant des modèles fermés plus forts pour les jugements ambigus.**

Après six jours de test côte à côte dans un stack d’agence, l’auteur dit que GLM-5.2 a tenu plus de 60 étapes d’agent avant de dériver, a respecté des formats structurés plus de 800 fois de suite et a livré des réponses self-hosted à faible latence. Le même post préfère encore Opus pour les tâches sensibles à la voix ou ambiguës, ce qui fait justement de cette règle de routage le principal enseignement utile.

Type: Evaluation | Date: 2026-06-20

---



<a id="case-80"></a>
### Case 80: [M3 Ultra Pokémon Rouge Objectif Course](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**Utilisez ce cas pour évaluer GLM-5.2 sur un run local d’agent de code à long horizon, où le modèle a passé environ une demi-journée à essayer de recréer Pokemon Red en HTML sur une machine M3 Ultra.**

L’auteur a remplacé le modèle de Claude Code par GLM 5.2 en local sur une machine M3 Ultra 512GB et a lancé pendant 12 heures la tâche `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.`. Le post partage la durée d’exécution, l’usage des tokens, le churn de code, l’usage RAM ainsi que le setup GGUF et KV cache, tout en notant que la qualité du modèle semblait de niveau frontier, tandis que le débit d’inférence local restait le goulot d’étranglement.

Type: Demo | Date: 2026-06-21

---
<a id="case-91"></a>
### Case 91: [Affrontement de correction de bug de Cline Repo](https://x.com/cline/status/2069171146994729078) (by [@cline](https://x.com/cline))

**Utilisez ce cas pour comparer GLM-5.2 et Opus 4.8 sur un vrai bug de dépôt, où GLM a consommé plus de tokens mais a produit le patch final le moins cher et le plus propre.**

Cline a testé les deux modèles sur le même bug du dépôt Cline avec le même harness et les mêmes outils. Le post indique que GLM a utilisé environ 1.1M tokens contre 660K pour Opus, coûté $0.41 contre $0.81, pris 4.7 minutes et 28 appels d’outils contre 1.6 minute et 12 appels, puis terminé avec nettoyage de code mort et build de production réussie, alors qu’Opus a laissé des erreurs de type qui passaient quand même les tests.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-127"></a>
### Case 127: [Réviseur GLM en ligne Pi](https://x.com/xpasky/status/2070831715518460177) (by [@xpasky](https://x.com/xpasky))

**Utilisez ce cas pour ajouter un second relecteur dans une boucle d’agent de code de style Pi, car l’auteur indique que GLM-5.2 peut conseiller Opus tour après tour pour une hausse de coût d’environ 10 %.**

xpasky explique que les utilisateurs de Pi peuvent reprendre un schéma de type OMP où un second modèle relit chaque tour et injecte des conseils inline. Le post cite explicitement GLM 5.2 en train de surveiller Opus en continu, dit que le duo semble visiblement "se chamailler" et estime que ce relecteur GLM supplémentaire ajoute environ 10 % au coût moyen de l’API Opus. Cela en fait un schéma concret de supervision multimodèle plutôt qu’un remplacement complet de modèle.

Type: Integration | Date: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [Bot Telegram One-Shot avec AgentRouter](https://x.com/MatinSenPai/status/2070259817818812701) (by [@MatinSenPai](https://x.com/MatinSenPai))

**Utilisez ce cas pour tester si GLM-5.2 peut inférer des defaults orientés production dans un build one-shot avec agent de code, au lieu de produire seulement le chemin minimal qui fonctionne.**

MatinSenPai explique avoir construit un bot Telegram en une seule passe avec GLM 5.2 à partir du même prompt que dans la vidéo, et dit que le modèle a ajouté de lui-même des détails pratiques. Le post mentionne le nettoyage automatique des fichiers après l’envoi de vidéos, le respect des limites de taille du Telegram Bot API avec un plafond par défaut de 50 MB, des auto-tests répétés avant de finir, une structure plus propre qu’un build précédent avec MiMo et environ 140K tokens ou près de 5 dollars d’usage reporté via AgentRouter.

Type: Demo | Date: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [OpenCode Go Refactor Victoire du premier passage](https://x.com/vedovelli74/status/2069889605969592500) (by [@vedovelli74](https://x.com/vedovelli74))

**Utilisez ce cas pour évaluer GLM-5.2 sur des refactors Go de taille moyenne dans OpenCode plutôt que de vous fier seulement aux promesses de benchmark.**

vedovelli74 rapporte un premier run OpenCode sur le refactor d’une base de code GoLang de taille moyenne et dit que GLM-5.2 a été plus rapide qu’Opus 4.8, plus efficace en tokens et juste dès le premier passage pour identifier ce qui devait être refactoré. L’auteur ajoute que le résultat a ensuite été validé face à Codex et Opus et est resté devant sur la qualité de livraison.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Code Claude + Curseur 3,36 $ Exécution par défaut](https://x.com/clairevo/status/2069828122640548204) (by [@clairevo](https://x.com/clairevo))

**Utilisez ce cas pour jauger GLM-5.2 comme daily driver dans Claude Code et Cursor avant de déplacer davantage de travail de coding autonome vers les open weights.**

clairevo dit que GLM 5.2 est devenu le modèle par défaut dans Claude Code et Cursor pour un coût cumulé de 3,36 $ jusqu’ici, tout en donnant une qualité de coding proche d’Opus. Le post renvoie aussi vers un chemin de setup via OpenRouter, des impressions sur le design front-end et la revue d’une tâche autonome de longue durée comme raisons de cette préférence.

Type: Evaluation | Date: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 Démos pratiques et exemples
<a id="case-229"></a>
### Case 229: [Duel de portfolios de profil sur Hyperagent](https://x.com/arsh_goyal/status/2077764207945416949) (by [@arsh_goyal](https://x.com/arsh_goyal))

**Utilisez ce cas pour comparer GLM-5.2 à d’autres modèles open sur une vraie tâche d’agent avec navigateur, car arsh_goyal a exécuté GLM 5.2, DeepSeek V4, Kimi K2.6 et Qwen 3.7 côte à côte sur Hyperagent pour construire un portfolio personnel à partir de profils publics.**

arsh_goyal dit que chaque modèle a reçu sa propre machine cloud avec un vrai navigateur, a lu les profils YouTube, LinkedIn et X de l’auteur, puis a construit un site à partir du même prompt d’une seule ligne. Le post dit aussi que Hyperagent exposait le coût et la durée de chaque run et renvoyait vers une vidéo ainsi que vers le prompt dans le thread de réponses, ce qui en fait une comparaison terrain plus solide qu’un simple screenshot ou un repost de leaderboard.

Type: Demo | Date: 2026-07-16

---
<a id="case-218"></a>
### Case 218: [Rebuild portfolio et OS avec OpenCode](https://x.com/MarkSShenouda/status/2077032282141978842) (by [@MarkSShenouda](https://x.com/MarkSShenouda))

**Utilisez ce cas pour situer GLM-5.2 sur des builds OpenCode ambitieuses, car MarkSShenouda dit que OpenCode Go plus GLM-5.2 l’ont aidé à reconstruire un site portfolio et un vrai OS écrit en C et en Assembly, capable de tourner dans WASM ou un émulateur Qemu.**

Le post relie GLM-5.2 à deux artefacts réellement produits plutôt qu’à une simple démo : un site portfolio reconstruit et un projet de système d’exploitation implémenté en C et en Assembly avec des cibles WASM et Qemu. Même si le tweet est compact, les deux aperçus liés en font une vitrine concrète pour un travail de coding maker plus ambitieux.

Type: Démo | Date: 2026-07-14

---
<a id="case-213"></a>
### Case 213: [Refonte GLM de LlamaCoder v4](https://x.com/nutlope/status/2076722464671793184) (by [@nutlope](https://x.com/nutlope))

**Utilisez ce cas si vous voulez prototyper un workflow de génération d’apps en one-shot prompt en vous appuyant sur les points forts de GLM-5.2 en planning et en design, car nutlope dit que LlamaCoder v4 a été reconstruit autour de GLM 5.2, avec un meilleur parsing, un meilleur planning et désormais un renderer WebAssembly dans un stack gratuit et open source.**

nutlope explique que LlamaCoder v4 tourne maintenant autour de GLM 5.2, passe la couche UI sur Base UI with shadcn, améliore le parsing, le planning et l’app design, et ajoute un renderer WebAssembly. Le projet est présenté comme gratuit, open source et powered by Together : on a donc ici une démo concrète et livrée, pas une simple impression floue sur la qualité du modèle.

Type: Demo | Date: 2026-07-13

---

<a id="case-202"></a>
### Case 202: [Gagner la fonctionnalité Space Shooter du code de commande](https://x.com/CommandCodeAI/status/2075264795817972107) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilisez ce cas pour comparer GLM-5.2 sur une build d’UI interactive en one-shot, car Command Code a exécuté le même prompt de retro space shooter sur Fable 5, GPT 5.5, GLM 5.2 et DeepSeek V4 Pro, puis a placé GLM en tête sur les features.**

Command Code dit que le même prompt `/design` a produit des layouts retro pixel-art de space shooter assez proches sur les quatre modèles, mais que GLM 5.2 s’est distingué sur des features comme le son, les contrôles, la progression des niveaux et l’UX générale, tout en coûtant $0.07 contre $0.80 pour Fable 5. Cela en fait une comparaison pratique pour de petites builds de jeu et d’UI, et non un simple screenshot de benchmark.

Type: Evaluation | Date: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [Émulateur ZCode Nintendo DS](https://x.com/0xSero/status/2074870153267818638) (by [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour inspecter une build locale de coding sur un horizon long, car l’auteur a lancé GLM-5.2 dans ZCode sur 4x RTX 6000 avec pour objectif de construire un émulateur Nintendo DS en C++ à partir de zéro.**

La source montre GLM-5.2 tournant dans ZCode sur une configuration à quatre GPU RTX 6000 et fixe un objectif concret : construire un émulateur Nintendo DS en C++ sans utiliser d’émulateur prêt à l’emploi, puis continuer jusqu’à ce que la ROM Mario 64 DS fonctionne. Cela en fait une vraie démo de coding agent avec un état final dur, plutôt qu’un simple 'j’ai fait une petite app'.

Type: Demo | Date: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [Code de commande Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Utilisez ce cas pour comparer GLM-5.2 sur des tâches légères de design et de jeu, car l’auteur a passé le même prompt Flappy Bird dans Command Code et conclut que Fable 5 n’était pas vraiment meilleur en UX alors qu’il coûtait presque neuf fois plus que GLM-5.2.**

Le post dit que l’expérience a utilisé le même prompt de jeu et la même configuration `/design` de Command Code sur DeepSeek V4 Pro, GLM 5.2 et Fable 5. GLM 5.2 se situe entre DeepSeek et Fable en prix brut, mais l’auteur dit que Fable n’a pas montré d’avantage UX suffisant pour justifier l’écart de prix. Cela en fait une comparaison pratique UX-versus-coût plutôt qu’une simple affirmation d’arena.

Type: Evaluation | Date: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [Cube de Rubik REAP NVFP4 en un seul essai](https://x.com/RoundtableSpace/status/2072700573145788914) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilisez ce cas pour tester GLM-5.2 sur des builds interactifs en single prompt, car la démo REAP-NVFP4 affirme qu un seul prompt a produit un Rubiks Cube 3D avec vrais scrambles, état live et bouton solve.**

RoundtableSpace dit que GLM-5.2-REAP-NVFP4 n a reçu qu un prompt HTML et a renvoyé une application Rubiks Cube 3D fonctionnelle avec état live, logique de scramble réelle et action solve. Le post reste léger sur le code, mais cela reste une démo concrète de one-shot build, pas un simple screenshot de benchmark.

Type: Demo | Date: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [Client iPhone Relais OMP](https://x.com/mov_axbx/status/2072192903762288721) (by [@mov_axbx](https://x.com/mov_axbx))

**Utilisez ce cas pour emballer rapidement un agent local GLM-5.2 dans une surface mobile : selon l auteur, le plugin build-ios-app de Codex a produit en quelques heures un client iPhone propre pour un relay OMP qui utilisait déjà GLM-5.2 et des tunnels Cloudflare.**

mov_axbx explique quil voulait une app mobile pour un agent OMP hébergé localement, qu il a utilisé le plugin build-ios-app de Codex et qu il a obtenu une version propre en quelques heures. Le backend passait par un relay custom écrit avec GLM-5.2 et OMP, tandis que Cloudflare gérait le tunnel.

Type: Demo | Date: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [Agent open source de recherche DevRel](https://x.com/Astrodevil_/status/2071572680470655253) (by [@Astrodevil_](https://x.com/Astrodevil_))

**Utilisez ce cas pour transformer GLM-5.2 en assistant de recherche vertical plutôt qu'en chat générique, car l'auteur a construit un agent DevRel open source qui transforme un produit et une audience en opportunités de contenu classées avec preuves et plans.**

Astrodevil_ a construit une application DevRel de recherche chat-first sur GLM-5.2 qui prend un brief produit et audience, cherche des signaux de demande sur Hacker News, repère les manques de contenu sur DEV, met à jour les faits via Engram memory et renvoie des idées de sujets classées avec preuves et plans. Le post cite aussi la stack : Agno, Weaviate Engram, inférence Nebius et une base de code open source.

Type: Demo | Date: 2026-06-29

<a id="case-123"></a>
### Case 123: [Refondre la boucle de page de destination à six variantes](https://x.com/nutlope/status/2070199649818779914) (by [@nutlope](https://x.com/nutlope))

**Utilisez ce cas pour prototyper des landing pages à faible coût en générant d’abord plusieurs variantes GLM-5.2, puis en faisant passer la meilleure dans un agent de code.**

nutlope décrit un workflow d’itération web centré sur GLM 5.2 et Recast : générer six variations de landing page à partir d’un seul prompt, choisir le meilleur design, télécharger ce code et poursuivre l’itération dans un agent de coding séparé. L’auteur dit que GLM-5.2 fonctionne bien ici parce qu’il est rapide, peu coûteux et fort en design, et affirme qu’avec le même budget on peut généralement produire trois à six variantes GLM pour chaque page générée avec Opus 4.8.

Type: Tutorial | Date: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [One-Shot jouable dans les coulisses](https://x.com/aimlapi/status/2066996493257408639) (by [@aimlapi](https://x.com/aimlapi))

**Utilisez ce cas pour comparer le résultat, la durée d'exécution et le coût de la création de jeux avec la même invite entre GLM-5.2 et Opus 4.8.**

L'API AI/ML a signalé avoir demandé à GLM-5.2 et Opus 4.8 de créer un jeu Backrooms jouable en une seule fois. Leur message indique que GLM-5.2 a construit une mécanique plus complète en 1:08 à 0,37 $, tandis qu'Opus a pris 2:14 à 1,94 $.

Type: Demo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [Trois constructions réelles avec des résultats mitigés](https://x.com/bridgemindai/status/2065840871929442319) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas comme un ensemble de démonstration d'avertissement : testez plusieurs versions réelles avant de faire confiance à un modèle pour des tâches de production de jeux ou de vidéos.**

BridgeMind a testé GLM-5.2 sur un jeu de maison d'horreur, un jeu d'infiltration 3D et une vidéo marketing Remotion. Le message rapporte des résultats mitigés, y compris une logique de jeu brisée, ce qui le rend utile comme signal de limitation fondé.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Cloner Super Mario en ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour évaluer la création de jeux itérative avec GLM-5.2 et ZCode sur plusieurs passes de correctifs et de fonctionnalités.**

L'auteur a testé ZCode 3.0 avec GLM-5.2 en créant un clone de style Super Mario, puis a partagé le résultat après cinq itérations de corrections de problèmes et d'ajouts de fonctionnalités.

Type: Demo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Concours d'atterrisseur lunaire](https://x.com/ivanfioravanti/status/2066193134984319173) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour comparer les codes GLM-5.2, MiniMax M3 et Kimi K2.7 sur une tâche de style jeu interactif.**

L'article décrit un concours Lunar Lander entre MiniMax M3, GLM-5.2 et Kimi K2.7 Code, en utilisant un résultat vidéo comme référence pratique avant de revenir au développement de modèles locaux.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [Création d'une arène de conception en une seule invite](https://x.com/grx_xce/status/2066951779154374907) (by [@grx_xce](https://x.com/grx_xce))

**Utilisez ce cas pour inspecter ce que GLM-5.2 peut générer à partir d'une seule invite de conception dans un contexte d'arène.**

L'auteur a partagé un exemple de création GLM-5.2 sur Design Arena réalisée à partir d'une seule invite, en l'utilisant pour montrer l'écart réduit entre les modèles à poids ouvert et fermé.

Type: Demo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [Document de recherche Comprendre le flux de travail](https://x.com/askalphaxiv/status/2066996976445706745) (by [@askalphaxiv](https://x.com/askalphaxiv))

**Utilisez ce cas pour appliquer GLM-5.2 aux flux de travail de lecture papier avec des questions contextuelles et des références croisées.**

AlphaXiv a introduit GLM-5.2 pour comprendre les articles de recherche, dans lequel les utilisateurs mettent en évidence une section, posent des questions et référencent d'autres articles pour le contexte, les comparaisons et les références de référence.

Type: Integration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Comparaison de poèmes contraints](https://x.com/emollick/status/2067056226337186146) (by [@emollick](https://x.com/emollick))

**Utilisez ce cas pour séparer l'exactitude de la qualité créative lorsque vous comparez GLM-5.2 avec les modèles de style Fable.**

Ethan Mollick a crédité GLM-5.2 Max pour avoir produit un poème contraint correct, tout en notant que Fable a incorporé la contrainte de lettre disparue dans le thème du poème de manière plus créative.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Exemple de sens du design](https://x.com/0xSero/status/2067074877941796994) (by [@0xSero](https://x.com/0xSero))

**Utilisez ce cas comme signal de conception visuelle léger, puis vérifiez avec votre propre invite et examen de l'interface utilisateur.**

L'auteur dit avoir apprécié le sens de la conception de GLM-5.2 et a partagé un exemple visuel. Il s'agit d'un indicateur utile pour l'inspection, et non d'une preuve autonome de la qualité de la conception de la production.

Type: Demo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run Voxel Jeu One-Shot](https://x.com/pseudokid/status/2068431546143649829) (by [@pseudokid](https://x.com/pseudokid))

**Utilisez ce cas pour stress-tester GLM-5.2 sur la génération de jeu en un seul prompt, puis examiner ce qui nécessite encore des corrections itératives dans un build visuellement riche.**

L’auteur explique avoir obtenu dès le premier tour l’essentiel d’un jeu de biker voxel inspiré de Temple Run, puis n’avoir eu besoin que de quelques passes supplémentaires pour corriger la caméra et les mouvements. Le post précise aussi que les outils Z.ai peuvent générer des captures d’écran et des vidéos de gameplay pour aider le modèle textuel à évaluer le résultat.

Type: Demo | Date: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [Ensemble d'exemples One-Shot OpenCode Go](https://x.com/LyalinDotCom/status/2068378281636982990) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**Utilisez ce cas pour benchmarker GLM-5.2 sur des builds one-shot rapides dans OpenCode Go avant de l’engager dans des boucles d’agents plus ouvertes.**

L’auteur rapporte des exemples one-shot couvrant une web app de système solaire, une application Electron d’informations système et un petit jeu web d’exploration d’île via OpenCode Go. Le même post dit aussi que GLM-5.2 est le meilleur modèle ouvert qu’il ait utilisé, sans pour autant le déclarer au niveau frontier.

Type: Demo | Date: 2026-06-20

---



<a id="case-81"></a>
### Case 81: [Construction en une seule invite de Space Invaders](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**Utilisez ce cas pour tester GLM-5.2 sur la création de jeu en un seul prompt, puis voir comment quelques passes supplémentaires gèrent les remplacements d’assets et un léger polissage.**

L’autrice dit que GLM-5.2 a construit un jeu jouable de type Space Invaders à partir d’un prompt principal, puis a utilisé trois prompts de suivi pour remplacer les sprites et ajouter de petits éléments comme un leaderboard. Le résultat publié est un exemple public léger de qualité de création de jeu, pas un benchmark complet.

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [Laboratoire de récupération OpenCode One-Shot](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**Utilisez ce cas pour prototyper rapidement des simulations interactives d’échec d’agent, car l’auteur dit avoir obtenu un recovery lab fonctionnel en one-shot pour environ 3,50 $.**

L’auteur a construit un recovery lab entièrement interactif avec OpenCode et GLM-5.2 après avoir fourni au modèle une analyse de 4 000 mots et le dépôt Agents SDK. Le post mentionne un run de 176k tokens, un résultat one-shot et un coût end-to-end d’environ 3,50 $ avant polissage.

Type: Demo | Date: 2026-06-21

---
<a id="case-92"></a>
### Case 92: [Ouvrir la reconstruction de l'URL de référence de conception](https://x.com/OpenDesignHQ/status/2069046584134778995) (by [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**Utilisez ce cas pour tester GLM-5.2 sur une recréation web pilotée par référence, où un prompt plus une URL source ont reproduit un site avec une fidélité presque pixel-perfect.**

Open Design indique avoir testé GLM-5.2 dans son AMR intégré avec seulement une URL de référence et un prompt simple, et le modèle a recréé le site presque parfaitement dans la démo. Considérez cela comme une preuve pratique de génération d’UI fondée sur des références, pas comme un benchmark complet.

Type: Demo | Date: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Test qualité-prix du Trader Desk](https://x.com/atomic_chat_hq/status/2069171121044513273) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilisez ce cas pour comparer GLM-5.2 sur des builds UI full-stack, où il s’est rapproché du résultat Trader Desk le plus soigné tout en ne coûtant qu’une petite fraction du meilleur résultat.**

Atomic Chat a comparé quatre modèles sur le même prompt live Trader Desk avec frontend, backend, données de marché sur huit symboles et UI dark theme personnalisée. Le post rapporte GLM-5.2 à 13,677 tokens et $0.03, contre Fugu Ultra à 22,225 tokens et $0.51, et indique que GLM a produit une interface multi-panneaux tout aussi complète avec données en direct pour un coût bien plus faible.

Type: Evaluation | Date: 2026-06-22

---

<a id="provider-tool-integrations"></a>
## 🔌 Intégrations fournisseurs et outils
<a id="case-170"></a>
### Case 170: [Accès Plug-And-Play à l'API gratuite NVIDIA](https://x.com/hqmank/status/2072855265612030010) (by [@hqmank](https://x.com/hqmank))

**Utilisez ce cas pour tester rapidement GLM-5.2 via un endpoint hébergé gratuit, car hqmank dit que NVIDIA a ouvert une route API compatible OpenAI et a confirmé qu'elle fonctionnait comme un remplacement plug-and-play.**

hqmank dit que GLM-5.2 est arrivé sur l'API gratuite de NVIDIA et que l'endpoint a bien fonctionné lors d'un essai rapide. Le post le décrit comme compatible OpenAI et plug-and-play, tout en avertissant que les paliers gratuits se resserrent souvent quand la demande monte. Cela en fait une note d'accès pratique pour des évaluations rapides ou un routage temporaire d'agents.

Type: Integration | Date: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [Route des agents de codage IA pour les travailleurs gratuits](https://x.com/ClaudeCode_UT/status/2072881775408456066) (by [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**Utilisez ce cas pour mettre en place une route GLM-5.2 gratuite pour les coding agents, car le tutoriel relie Workers AI à Claude Code, OpenCode, Cursor et Aider via l'endpoint compatible OpenAI `cf/zai-org/glm-5.2`.**

ClaudeCode_UT décrit un parcours en six étapes : créer un compte Cloudflare gratuit, copier l'account ID de Workers AI, émettre un API token, ajouter Cloudflare comme provider dans les outils compatibles OpenAI, choisir `cf/zai-org/glm-5.2`, puis lancer Claude Code, Cursor, Aider ou OpenCode. C'est un tutoriel d'accès concret pour les équipes qui veulent tester des workflows de coding agents avant de payer une facturation au token.

Type: Tutorial | Date: 2026-07-03

---
<a id="case-232"></a>
### Case 232: [Agents GLM de check run sur Macroscope](https://x.com/kayvz/status/2077810181904494631) (by [@kayvz](https://x.com/kayvz))

**Utilisez ce cas pour réduire le coût des agents de review de PR tout en gardant un vrai workflow de check run, car kayvz dit que Macroscope permet maintenant d’exécuter des Check Run Agents sur GLM 5.2 via la configuration `.md` habituelle du dépôt.**

kayvz dit que les nouveaux choix de modèle apparaissent directement lors de la configuration d’un fichier `.md` de check run, ce qui rend le changement plus actionnable qu’un simple post de disponibilité. Le fil positionne explicitement cette fonction pour des agents personnalisés de code review dans les pull requests, donc c’est une surface d’intégration concrète pour les équipes qui font déjà passer leur automatisation de review par Macroscope et veulent une option open-weight.

Type: Integration | Date: 2026-07-16

---
<a id="case-231"></a>
### Case 231: [API de research agents Aster à 281 TPS](https://x.com/asterailabs/status/2077556435085574429) (by [@asterailabs](https://x.com/asterailabs))

**Utilisez ce cas pour benchmarker un endpoint hébergé rapide de GLM-5.2, car asterailabs dit que Aster Inference sert GLM 5.2 à 281 tokens par seconde dans une API d’inférence construite à partir d’un travail d’optimisation pour research agents.**

Aster présente le produit comme une API d’inférence créée par des AI research agents et donne des chiffres de throughput nominatifs au lieu d’un simple slogan de lancement : 644 tps pour gpt-oss-120b et 281 tps pour GLM 5.2 sur GPU. Le même post dit que l’entreprise transforme les découvertes d’inférence issues de son propre système de recherche en améliorations produit, ce qui rend cette route pertinente pour les équipes qui comparent des providers GLM hébergés rapides plutôt qu’un self-hosting depuis zéro.

Type: Integration | Date: 2026-07-16

---
<a id="case-230"></a>
### Case 230: [Route GLM native TrueFoundry via Wafer](https://x.com/wafer_ai/status/2077837999514214456) (by [@wafer_ai](https://x.com/wafer_ai))

**Utilisez ce cas pour brancher GLM-5.2 dans une stack existante de TrueFoundry AI Gateway, car wafer_ai dit que son intégration provider native démarre désormais avec GLM 5.2 et GLM 5.2 Fast sans changer le reste de la configuration du gateway.**

wafer_ai dit que les équipes qui utilisent déjà TrueFoundry AI Gateway peuvent employer les modèles Wafer sans rien changer d’autre dans leur stack, et que le rollout commence avec GLM 5.2 et GLM 5.2 Fast. Le post présente Wafer comme la route serverless GLM la plus rapide et l’associe à une intégration gateway nommée, ce qui en fait un chemin d’accès managé concret plutôt qu’une annonce générique de disponibilité de modèle.

Type: Integration | Date: 2026-07-16

---
<a id="case-225"></a>
### Case 225: [Pont TogetherLink pour le harness Codex](https://x.com/nutlope/status/2077432463685554558) (by [@nutlope](https://x.com/nutlope))

**Utilisez ce cas pour exécuter GLM-5.2 dans des CLI de coding agents existants, car nutlope dit que TogetherLink est un CLI open source qui permet à Codex et Claude Code d'appeler directement des modèles ouverts comme GLM 5.2.**

L'annonce présente TogetherLink comme une couche passerelle pour les développeurs qui veulent garder leur harness de coding préféré tout en remplaçant le modèle sous-jacent par une stack open-weight. Comme le post cite explicitement Codex et Claude Code parmi les harnesses pris en charge et positionne le projet comme open source, cela devient une voie d'accès concrète pour les équipes qui veulent tester GLM-5.2 sans abandonner leur workflow terminal actuel.

Type: Integration | Date: 2026-07-15

---
<a id="case-224"></a>
### Case 224: [Routage du Open Model Harness de Vorflux](https://x.com/vorfluxai/status/2077449967711760587) (by [@vorfluxai](https://x.com/vorfluxai))

**Utilisez ce cas pour faire passer GLM-5.2 dans une session agent complète sans glue personnalisée, car vorfluxai dit que son Open Model Harness assigne GLM 5.2 aux étapes design, build et simplify tout en conservant intact le reste du flux Vorflux.**

vorfluxai dit que le harness expose un menu déroulant qui bascule toute une session sur des modèles ouverts tout en conservant le flux normal de Vorflux pour planning, subagents, pull requests et testing. Dans la table de routing publiée, DeepSeek V4 Pro gère main, plan et review, DeepSeek V4 Flash gère explore, GLM 5.2 gère design, build et simplify, et Kimi 2.7 Code gère debug et testing, ce qui fait de ce cas un vrai schéma d'orchestration agentique multimodèle et non un simple post d'accès.

Type: Integration | Date: 2026-07-15

---
<a id="case-220"></a>
### Case 220: [Agent clinique OpenMed dé-identifié](https://x.com/MaziyarPanahi/status/2077000157103898789) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Utilisez ce cas pour garder GLM-5.2 dans un flux clinique préservant la confidentialité, car MaziyarPanahi dit que GLM 5.2 a planifié, appelé des outils et rédigé la disposition d’un cas complet après qu’OpenMed a retiré les identifiants en local et que Gemma 4 a géré la structure.**

MaziyarPanahi décrit un workflow totalement ouvert où OpenMed réalise la désidentification sur l’appareil, Gemma 4 extrait la structure et GLM-5.2 prend en charge le raisonnement médical agentique sur du texte expurgé. Le détail opérationnel clé est que la note brute ne quitte jamais la machine, ce qui transforme le thread en un modèle concret de confidentialité santé et de tooling, et non en simple promotion du modèle.

Type: Intégration | Date: 2026-07-14

---
<a id="case-219"></a>
### Case 219: [Route d’accès GLM USDC via Katana](https://x.com/imgn_ai/status/2077061568068465148) (by [@imgn_ai](https://x.com/imgn_ai))

**Utilisez ce cas pour exposer GLM-5.2 via une route pay per request native wallet, car imgn_ai dit que Katana sert GLM-5.2 sur x402 via Base sans compte, avec USDC et un llms.txt publié pour l’intégration directe.**

imgn_ai présente Katana comme une voie alimentée par x402 où les développeurs copient le llms.txt du service, connectent un wallet et appellent des modèles frontier texte, image ou vidéo à des prix de gros. Le post précise qu’aucun compte n’est requis et que le paiement se fait à la requête en USDC, ce qui en fait une option d’accès concrète pour des expériences sans abonnement SaaS durable.

Type: Intégration | Date: 2026-07-14

---
<a id="case-214"></a>
### Case 214: [Route GLM via Databricks AI Gateway](https://x.com/QCXINT_/status/2076490318695088218) (by [@QCXINT_](https://x.com/QCXINT_))

**Utilisez ce cas si vous voulez tester un chemin d’accès managé et très rapide vers GLM-5.2 dans un agent tooling, car QCXINT_ a montré un flux avec base URL et token Databricks AI Gateway qui expose une route GLM 5.2 semblant aller jusqu’à 1M de contexte, même si l’identité exacte du backend reste non confirmée.**

QCXINT_ décrit un enchaînement assez concret : créer un workspace Databricks, ouvrir User Settings, générer un access token avec scope AI Gateway, copier la AI Gateway base URL de l’organisation puis appeler l’endpoint exposé depuis des outils comme OpenClaw ou Hermes. D’après le post, les tests ne montraient pour l’instant que GLM-5.2, la vitesse semblait anormalement élevée et la route paraissait supporter jusqu’à 1M de contexte ; toutefois, l’auteur précise lui-même qu’il n’a pas encore confirmé si le backend est bien exactement le modèle GLM-5.2 annoncé.

Type: Integration | Date: 2026-07-13

---

<a id="case-208"></a>
### Case 208: [Pile d’agents Open Molecular Viewer](https://x.com/MaziyarPanahi/status/2075913552854933869) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Utilisez ce cas pour brancher GLM-5.2 sur un workflow ouvert d’inspection scientifique, car MaziyarPanahi a combiné GLM-5.2 via Hugging Face Inference Providers avec Qwen3-VL sur llama.cpp, Mol* et PydanticAI afin de rendre et critiquer une structure EGFR plus erlotinib à partir d’un seul prompt.**

MaziyarPanahi décrit une pile entièrement ouverte où GLM-5.2 sert de cerveau langage via Hugging Face Inference Providers, Qwen3-VL prend en charge l’inspection visuelle via llama.cpp, Mol* rend la structure et PydanticAI coordonne la couche agent. Le post dit que le workflow a produit six rendus à partir d’un seul prompt autour d’un exemple EGFR plus erlotinib venant du RCSB PDB, ce qui en fait une intégration scientifique multi-outils concrète plutôt qu’une simple annonce de disponibilité.

Type: Integration | Date: 2026-07-11

---
<a id="case-204"></a>
### Case 204: [Perplexity Advisor Coût de référence WANDR](https://x.com/perplexity_ai/status/2075229779716973030) (by [@perplexity_ai](https://x.com/perplexity_ai))

**Utilisez ce cas pour estimer l’économie de GLM-5.2 dans un harness de computer use routé, car Perplexity dit que sa configuration GLM 5.2 plus advisor atteint 2.1x sur WANDR contre 6.1x pour Opus, avec un coût moyen proche de la moitié.**

Perplexity dit avoir mesuré le coût par tâche avec GLM 5.2 comme baseline et que la route GLM 5.2 plus advisor sur WANDR est ressortie à 2.1x, contre 6.1x pour Opus. Il faut y voir un signal concret pour un routing d’agent informatique open-weight-first, où un cœur GLM moins coûteux est combiné à une escalade sélective plutôt que de faire tourner un modèle fermé plus puissant à chaque étape.

Type: Evaluation | Date: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [Routage des artefacts ouverts par un collègue](https://x.com/coworkerapp/status/2075233366266310905) (by [@coworkerapp](https://x.com/coworkerapp))

**Utilisez ce cas pour amener GLM-5.2 dans des workflows d’artifacts en entreprise, car Coworker dit que Open Artifacts peut créer docs, decks, PDF, spreadsheets, dashboards et apps tandis que son routeur optimisé réduit l’usage de tokens d’environ 5x tout en proposant GLM 5.2 hébergé aux États-Unis.**

Coworker dit que Open Artifacts peut générer des livrables partageables comme des docs, decks, dashboards, spreadsheets, PDF et apps complètes. Le même post de lancement indique que son mode optimisé choisit le bon modèle par tâche pour consommer environ cinq fois moins de tokens, tout en laissant les équipes utiliser GLM 5.2 dans un environnement hébergé aux États-Unis, SOC 2 et riche en connecteurs.

Type: Integration | Date: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [Flux de travail de téléchargement de contexte DotCode](https://x.com/stagedhappen/status/2074775356867789241) (by [@stagedhappen](https://x.com/stagedhappen))

**Utilisez ce cas pour donner à GLM-5.2 davantage de contexte projet dans une sandbox privée de coding, car DotCode a ajouté le support de GLM 5.2 avec des uploads de captures, images, CSV, PDF, fichiers source et ZIP qui alimentent le même flux filesystem et terminal.**

DotCode dit que GLM 5.2 fonctionne désormais avec des uploads contextuels de workspace, afin que les agents puissent inspecter des fichiers, parcourir la structure du projet, éditer du code, exécuter des commandes terminal et reprendre dans la même sandbox. Le post nomme les entrées prises en charge, décrit le flux prompt plus fichiers vers l’exécution en sandbox, et le présente comme une étape vers un vrai travail de coding agent à partir du contexte réel d’un projet.

Type: Integration | Date: 2026-07-08

---
<a id="case-234"></a>
### Case 234: [Accès GLM remisé sur Jatevo](https://x.com/JatevoId/status/2077770086228885536) (by [@JatevoId](https://x.com/JatevoId))

**Utilisez ce cas pour obtenir une route simple d’accès hébergé à GLM-5.2 avec des prix publics, car JatevoId dit que GLM 5.2 est disponible sur sa plateforme à $1.40 par million d’input tokens et $4.40 par million d’output tokens, avec 50% de remise pour les holders JTVO éligibles.**

JatevoId dit que le rollout inclut une allocation de free compute progressivement mise à jour pour les holders, ainsi qu’une politique publique de remise de 50 pour cent sur le prix standard au token. Le tableau explicite des prix input et output en fait une note d’accès concrète pour les utilisateurs qui comparent des routes GLM hébergées plutôt qu’une annonce vague, même si la remise holder dépend encore de conditions propres à la plateforme.

Type: Integration | Date: 2026-07-16

---
<a id="case-233"></a>
### Case 233: [Serving GLM sur MI325x sous un dixième de cent](https://x.com/picocreator/status/2077817481381728268) (by [@picocreator](https://x.com/picocreator))

**Utilisez ce cas pour budgéter une inférence self-hosted de GLM-5.2 sur matériel AMD, car picocreator dit qu’une configuration 4xMI325x a servi GLM 5.2 à 1,482 tok/s pour moins de $0.10 par million de tokens.**

picocreator dit que cette route a livré 1,482 tokens par seconde sur quatre GPU MI325x et présente le coût comme trois fois inférieur à celui des B300 et dix fois inférieur à celui d’Opus. Cela transforme le post en point de repère concret sur le hardware et l’économie pour les équipes qui veulent chiffrer une capacité GLM dédiée plutôt que comparer seulement des tarifs d’API ou des claims marketing.

Type: Demo | Date: 2026-07-16

---
<a id="case-226"></a>
### Case 226: [Triage de dossier clinique sur Mac Studio avec Bonsai](https://x.com/MaziyarPanahi/status/2077362554805117132) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Utilisez ce cas pour garder local un long dossier clinique pendant que GLM-5.2 raisonne dessus, car MaziyarPanahi dit que GLM 5.2 a trié un dossier patient sur trois ans via Bonsai 27B sur un Mac Studio et a repéré un risque lié au contraste enfoui 17 mois plus tôt.**

MaziyarPanahi dit que 292 encounters sont restées dans Bonsai 27B sur un Mac Studio en utilisant llama.cpp, Metal, des poids ternaires et environ 7.2GB de stockage local du modèle, avec GLM-5.2 autorisé à ne poser que trois questions avant d'identifier un risque metformine plus contraste iodé à eGFR 39. Le thread présente la configuration comme préservant la confidentialité par construction : le dossier n'a jamais quitté la machine et l'orchestrateur n'a jamais touché aux données brutes du patient, ce qui en fait un workflow santé local concret plutôt qu'une promotion générique du modèle.

Type: Demo | Date: 2026-07-15

---
<a id="case-221"></a>
### Case 221: [Serving agentique B300 avec SGLang TopK-V2](https://x.com/lmsysorg/status/2077076059657548127) (by [@lmsysorg](https://x.com/lmsysorg))

**Utilisez ce cas pour benchmarker un serving GLM-5.2 de production sur des workloads agentiques à long contexte, car lmsysorg dit que SGLang a dépassé 500 tok/s par utilisateur sur 8xB300 en batch size 1 tout en améliorant l’interactivité mono-utilisateur de 18 à 34 pour cent.**

Le post de deep dive dit que les mesures proviennent d’un vrai workload de coding agentique multi-tour et attribue les gains à la fois à l’architecture GLM-5.2 orientée IndexShare et KVShare et au nouveau kernel TopK-V2 de SGLang. Il affirme aussi que ce kernel est 2,33 fois plus rapide à 80K ISL et monte à 10,17 fois à 1M ISL, ce qui en fait une référence de déploiement plus solide qu’une simple note de lancement.

Type: Évaluation | Date: 2026-07-14

---
<a id="case-215"></a>
### Case 215: [Route llm-d H200 avec Prefix-Cache](https://x.com/RedHat_AI/status/2076725768034398513) (by [@RedHat_AI](https://x.com/RedHat_AI))

**Utilisez ce cas si vous voulez benchmarker l’économie d’un serving managé GLM-5.2 sur H200, car RedHat_AI dit que le couplage Wide EP plus prefix-cache routing dans llm-d a obtenu plus de 90 pour cent de cache reuse, un TTFT sous les 3 secondes et environ 2 dollars par million d’output tokens sur une route GLM-5.2 de plus de 700B.**

Red Hat AI renvoie à une explication de robertshaw21 pendant les vLLM Office Hours au sujet d’un déploiement GLM-5.2 de plus de 700B tournant sur H200. Le post attribue à llm-d Wide EP et au prefix-cache-aware routing à la fois le cache reuse supérieur à 90 pour cent et le TTFT inférieur à 3 secondes, tout en comparant environ 2 dollars par million d’output tokens à 4,40 dollars pour l’API hébergée. C’est une référence utile pour comparer un stack de routing auto-géré à l’usage direct du modèle hosted.

Type: Integration | Date: 2026-07-13

---

<a id="case-209"></a>
### Case 209: [Colibri 25 Go de RAM Streaming clairsemé](https://x.com/techNmak/status/2075872446197158361) (by [@techNmak](https://x.com/techNmak))

**Utilisez ce cas pour comprendre la nouvelle borne basse des expériences locales avec GLM-5.2, car techNmak explique comment Colibrì exécute le MoE 744B avec environ 25 Go de RAM en streamant les experts depuis du NVMe, même si la plus petite configuration ne dépasse qu’environ 0,05 à 0,1 tok/s.**

techNmak résume Colibrì comme un moteur local d’inférence en pur C qui garde en RAM uniquement les poids toujours chauds et laisse les experts routés sur NVMe, avec environ 9,9 Go résidents en permanence, environ 20 Go de pic RAM pendant le chat et près de 370 Go de poids int4 sur disque. Le post présente explicitement le résultat comme une preuve de concept systèmes plutôt que comme un serving de production rapide, car la génération à froid sur la machine 25 Go reste autour de 0,05 à 0,1 tok/s et l’impact qualité de la quantification int4 n’est pas encore pleinement benchmarké.

Type: Demo | Date: 2026-07-11

---
<a id="case-206"></a>
### Case 206: [Débit de production SGlang NVFP4](https://x.com/sgl_project/status/2075721488456654861) (by [@sgl_project](https://x.com/sgl_project))

**Utilisez ce cas pour cadrer un serving SGLang de production pour GLM-5.2 NVFP4, car la release officielle SGLang v0.5.15 dit atteindre plus de 500 tok/s par utilisateur sur 8x B300 et 450 tok/s sur 4x GB300 avec batch size 1.**

L’annonce officielle de SGLang v0.5.15 dit que ce cycle de release s’est concentré sur le tuning de production de GLM-5.2 NVFP4. Le post rapporte plus de 500 tokens par seconde par utilisateur sur 8x B300 et 450 sur 4x GB300 avec bs=1, ce qui en fait un checkpoint concret de throughput de déploiement pour les équipes qui évaluent des stacks d’inférence hébergés ou autogérés. La même annonce présente aussi ce travail comme un support produit upstream plutôt qu’un hack de labo ponctuel.

Type: Evaluation | Date: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Point de terminaison GLM gratuit Dahl 100 millions](https://x.com/pengsonal/status/2074908680106180669) (by [@pengsonal](https://x.com/pengsonal))

**Utilisez ce cas pour essayer GLM-5.2 via une route OpenAI-compatible sans carte bancaire, car Dahl Inference propose 100M de tokens gratuits pour GLM 5.2 FP8 et montre comment créer une clé puis appeler `/v1/chat/completions`.**

Le post place GLM 5.2 FP8 parmi les endpoints gratuits de modèles ouverts chez Dahl et précise qu’aucune inscription ni carte n’est requise. Il donne aussi un flux de configuration concret : générer une clé dans l’interface web, utiliser l’endpoint OpenAI-compatible `/v1/chat/completions`, et noter que des requêtes directes en `curl` peuvent tomber sur des 403 Cloudflare même si la voie web chat fonctionne.

Type: Tutorial | Date: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [Configuration GLM gratuite du point de terminaison NVIDIA](https://x.com/undefinedKi/status/2074491917333655948) (by [@undefinedKi](https://x.com/undefinedKi))

**Utilisez ce cas pour tester GLM-5.2 dans des outils de code sans self-hosting, car la source décrit un flux d’endpoint NVIDIA gratuit qui injecte des clés API GLM-5.2 dans Claude Code, Cursor ou Cline.**

Le post dit que NVIDIA a publié des clés API gratuites pour les meilleurs modèles, dont GLM-5.2, puis donne une route de configuration directe : créer un compte NVIDIA, ouvrir l’onglet Build d’un modèle free endpoint, générer la clé API, puis coller l’URL de base et la clé dans Claude Code, Cursor ou Cline. Cela en fait un tutoriel d’accès pratique pour essayer GLM-5.2 sans facturation au token ni stack GPU locale.

Type: Tutorial | Date: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [Route d'inférence privée 0G TeeML](https://x.com/0G_labs/status/2074496704959676682) (by [@0G_labs](https://x.com/0G_labs))

**Utilisez ce cas pour faire passer GLM-5.2 par une route fournisseur axée confidentialité, car 0G dit que GLM 5.2 tourne désormais dans TeeML avec des prompts scellés dans une enclave TEE et un prix inférieur à la voie officielle.**

0G présente TeeML comme sa couche d’inférence privée et dit que GLM 5.2 y tourne maintenant avec une exécution vérifiable dans un trusted execution environment. Le post est court, mais il fournit tout de même une intégration fournisseur concrète, avec un angle confidentialité et prix. Il vaut donc mieux le lire comme un signal de route de déploiement que comme une affirmation de qualité modèle.

Type: Integration | Date: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [PR Open-SQL pour DuckDB Flock](https://x.com/lhoestq/status/2074143736624275629) (by [@lhoestq](https://x.com/lhoestq))

**Utilisez ce cas pour faire entrer GLM-5.2 dans une analyse SQL locale entièrement ouverte, car lhoestq dit qu’un PR duckdb plus flock active désormais GLM-5.2 dans une stack data 100% open source.**

Le post explique que l’auteur a ouvert un PR pour activer GLM-5.2 dans duckdb avec flock et le présente comme une manière de mettre une intelligence open de niveau frontier directement au service des données. Comme la source est un PR ouvert et non une release note déjà mergée, ce cas fonctionne surtout comme signal d’intégration en cours pour l’analytics locale et les workflows natifs SQL.

Type: Integration | Date: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [Accès à l'API One-Key à 26 modèles](https://x.com/Alan_Earn/status/2073663239028924680) (by [@Alan_Earn](https://x.com/Alan_Earn))

**Utilisez ce cas pour tester GLM-5.2 via un seul fournisseur compatible OpenAI, car Alan_Earn dit qu’une seule clé API expose GLM-5.2 plus 25 autres modèles et inclut 26 dollars de crédits de départ.**

Le post donne un setup court : créer le compte, ajouter une carte, débloquer le dashboard, récupérer les crédits, générer une clé API puis la coller dans Codex, Cursor, OpenCode, OpenClaw, Hermes ou un autre client compatible OpenAI. Il rappelle aussi le pay as you go et le fait que les gros modèles frontier consomment vite les crédits gratuits ; le thread sert donc surtout comme note d’accès et de pricing.

Type: Tutorial | Date: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [Configuration de la réflexion NVIDIA NIM OpenCode](https://x.com/Dracoshowumore/status/2073384581256929717) (by [@Dracoshowumore](https://x.com/Dracoshowumore))

**Utilisez ce cas pour brancher GLM-5.2 dans OpenCode via le endpoint gratuit NVIDIA NIM quand vous voulez une route sans coût avec thinking activé explicitement, car Dracoshowumore partage le flux d’API key, la base URL et une configuration OpenCode où la couche outils gère les function calls pendant que GLM tourne avec enable_thinking=true.**

Dracoshowumore décrit tout le chemin de configuration : inscription sur la plateforme développeur NVIDIA, génération d’une API key GLM-5.2, pointage d’OpenCode vers la base URL publiée, désactivation du tool calling natif du modèle, puis passage de chat_template_kwargs.enable_thinking=true dans les options du provider. Le même post dit que la route NIM n’expose ni function calling ni reasoning traces en standard, donc OpenCode doit porter l’orchestration des outils. Cela en fait une note de configuration pratique, et pas seulement une autre annonce de endpoint gratuit.

Type: Tutorial | Date: 2026-07-04

<a id="case-165"></a>
### Case 165: [Lancement de ZCode avec contrôle d'agent mobile](https://x.com/Digiato/status/2072663459850829985) (by [@Digiato](https://x.com/Digiato))

**Utilisez ce cas pour évaluer ZCode comme surface officielle de coding pour GLM-5.2, car le rapport de lancement dit que cet IDE agentique gratuit arrive sur Windows, macOS et Linux et peut suivre les projets via Telegram, WeChat et Feishu.**

Digiato décrit ZCode comme un environnement de développement agentique gratuit construit autour de GLM-5.2 et positionné face à Cursor, Claude Code et Copilot. Le post dit qu il existe sur Windows, macOS et Linux, qu il est profondément intégré à GLM-5.2 et qu il permet de suivre la progression d un projet via Telegram, WeChat et Feishu. C est une surface d accès plus distinctive qu une simple annonce de modèle.

Type: Integration | Date: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [Documentation de l'agent géré automatiquement par OpenWiki](https://x.com/LangChain/status/2072745455788933321) (by [@LangChain](https://x.com/LangChain))

**Utilisez ce cas pour garder automatiquement à jour une documentation lisible par les agents, car LangChain explique que OpenWiki régénère et maintient les docs du repo à mesure que le code change et tourne sur des open models comme GLM 5.2.**

LangChain présente OpenWiki comme une couche open-source de maintenance documentaire pour coding agents. Le post dit qu il combine un open harness avec des workflows CLI ouverts, garde la documentation à jour quand le codebase évolue et tourne sur des open models comme GLM 5.2 et Kimi K2.7. C est un pattern pratique de mémoire en fichiers pour les équipes qui veulent que leurs agents lisent des docs repo fraîches plutôt que des wikis mises à la main.

Type: Integration | Date: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [PTU de fonderie via FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilisez ce cas pour faire passer GLM-5.2 par des budgets Foundry d entreprise sans reconstruire vos clients agents, car Fireworks explique que FireConnect relie les PTU de Microsoft Foundry aux workflows Codex, OpenCode et Pi.**

Fireworks indique que GLM 5.2 est désormais disponible sur Microsoft Foundry. Avec FireConnect activé, les équipes peuvent consommer des PTU Foundry tout en continuant à faire passer les requêtes par Codex, OpenCode ou Pi, sans ouvrir un chemin d accès séparé pour chaque surface agent.

Type: Integration | Date: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Établi d'évaluation Braintrust GLM](https://x.com/ankrgyl/status/2072042305108722040) (by [@ankrgyl](https://x.com/ankrgyl))

**Utilisez ce cas pour comparer GLM-5.2 et Opus dans une même pile d'evals, car Braintrust et Baseten ont lancé le modèle avec un exemple concret de coût contre précision en long contexte.**

ankrgyl dit que Braintrust a ajouté GLM-5.2 avec le support de Baseten afin que les équipes puissent l’exécuter dans leurs evals et leurs traces de production. L’exemple compare la récupération long contexte à 25K et 50K tokens : Opus 4.8 mène d’environ 3,5 points, mais coûte environ 4,1x à 4,5x plus par trace.

Type: Integration | Date: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [Abonnement ClinePass pour modèles open-weight](https://x.com/iam_elias1/status/2071655509611151674) (by [@iam_elias1](https://x.com/iam_elias1))

**Utilisez ce cas pour regrouper plusieurs modèles de coding open-weight dans un seul agent harness, car ClinePass réunit GLM-5.2 et des modèles proches sous un forfait mensuel fixe au lieu de clés provider et de facturations séparées.**

iam_elias1 présente ClinePass comme une formule à 9,99 dollars par mois pour utiliser GLM-5.2, DeepSeek, Kimi, Qwen, MiniMax, MiMo et d'autres modèles open-weight dans l'extension IDE et la CLI de Cline. Le thread dit que cela remplace les API keys par provider, offre 2 à 5 fois les limites API standard, permet de changer de modèle au milieu d'une session selon la phase de coding et fait tomber le premier mois à 1,99 dollar via l'inscription en CLI.

Type: Integration | Date: 2026-06-29

<a id="case-137"></a>
### Case 137: [Service API GLM gratuit pour les agents de codage](https://x.com/mcwangcn/status/2071261128575897901) (by [@mcwangcn](https://x.com/mcwangcn))

**Utilisez ce cas pour tester GLM-5.2 dans Hermes ou d’autres agents de code sans inscription, car le service partagé émet des API keys de courte durée et garde un setup léger.**

mcwangcn a partagé un service API GLM-5.2 gratuit qui, d’après le post, ne demande ni inscription ni connexion et peut être utilisé depuis Lobster, Hermes ou d’autres agents de code. Le même post précise que chaque API key générée dure une heure avant renouvellement, ce qui constitue une contrainte anti-abus concrète et rend le service mieux adapté à des tests rapides de workflow qu’à un usage de production autonome sur le long terme.

Type: Integration | Date: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [Disponibilité d’OpenCode Go](https://x.com/opencode/status/2067207923122479242) (by [@opencode](https://x.com/opencode))

**Utilisez ce cas pour suivre la disponibilité de GLM-5.2 dans les workflows OpenCode Go avec du texte, un contexte 1M et une tarification de type GLM-5.1.**

OpenCode a annoncé la disponibilité de GLM-5.2 dans Go, mettant en évidence la prise en charge du texte, une fenêtre contextuelle de 1 million et le même prix que la version 5.1.

Type: Integration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Disponibilité du cloud Ollama](https://x.com/ollama/status/2066949797316350361) (by [@ollama](https://x.com/ollama))

**Utilisez ce cas pour acheminer GLM-5.2 vers Ollama Cloud pour des expériences de modèle de codage open source accessibles.**

Ollama a annoncé la disponibilité du GLM-5.2, le décrivant comme un modèle de codage et de tâches agentiques à long terme avec un contexte 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [Accès aux appels API OpenRouter One](https://x.com/OpenRouter/status/2066941552208056561) (by [@OpenRouter](https://x.com/OpenRouter))

**Utilisez ce cas pour accéder à GLM-5.2 via OpenRouter lors de la comparaison du routage de fournisseur ou des piles multimodèles.**

OpenRouter a annoncé la disponibilité du GLM-5.2 en tant que modèle à long terme de 1 million de jetons, offrant aux utilisateurs un chemin indépendant du fournisseur pour l'appeler.

Type: Integration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [Prise en charge de vLLM Day-Zero](https://x.com/vllm_project/status/2066950636428775693) (by [@vllm_project](https://x.com/vllm_project))

**Utilisez ce cas pour auto-héberger ou servir GLM-5.2 via vLLM avec une prise en charge jour zéro.**

Le projet vLLM a annoncé la prise en charge de GLM-5.2 dans la version 0.23.0, le présentant comme un modèle phare pour les agents de codage à long horizon avec un contexte 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Disponibilité de la notion via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (by [@NotionHQ](https://x.com/NotionHQ))

**Utilisez ce cas pour identifier GLM-5.2 en tant que modèle à poids ouvert disponible dans les flux de travail Notion.**

Notion a annoncé la disponibilité du GLM-5.2 en tant que modèle ouvert conçu pour les tâches à long terme et servi via Baseten.

Type: Integration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Service de feux d'artifice jour zéro](https://x.com/FireworksAI_HQ/status/2067007200426680509) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilisez ce cas pour évaluer Fireworks en tant que route de diffusion pour les charges de travail GLM-5.2 nécessitant une infrastructure hébergée.**

Fireworks a annoncé GLM-5.2 en direct le jour zéro, en mettant l'accent sur le contexte 1M, le positionnement axé sur le codage et la validation indépendante sur SWE-Bench, Terminal-Bench, GPQA et AIME.

Type: Integration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Lien vers le jardin modèle Google Cloud](https://x.com/CarolGLMs/status/2067127223216419088) (by [@CarolGLMs](https://x.com/CarolGLMs))

**Utilisez ce cas pour trouver GLM-5.2 dans des contextes de déploiement orientés Google Cloud et de plate-forme d'agent.**

CarolGLMs a partagé un lien Google Cloud pour GLM-5.2, ce qui en fait un pointeur direct pour les équipes travaillant via des catalogues de modèles cloud.

Type: Integration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Mode de confidentialité de Venise](https://x.com/AskVenice/status/2066990725439361251) (by [@AskVenice](https://x.com/AskVenice))

**Utilisez ce cas lorsque le mode de confidentialité, TEE ou le chiffrement de bout en bout est un facteur décisif pour essayer GLM-5.2.**

Venice a annoncé la disponibilité du GLM-5.2 en mode confidentialité avec le cadrage TEE/E2EE, destiné au codage agent privé et aux tâches à long terme.

Type: Integration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Disponibilité du code de commande](https://x.com/CommandCodeAI/status/2066950478194503990) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilisez ce cas pour essayer GLM-5.2 dans Command Code avec un plan d’entrée à faible coût et des fonctionnalités de codage à contexte long.**

Command Code a annoncé la disponibilité du GLM-5.2, en notant le contexte 1M, un raisonnement solide, le statut open source et l'accès via son plan Go à un dollar.

Type: Integration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Agent Hermès du portail Nous](https://x.com/Teknium/status/2066954081575592282) (by [@Teknium](https://x.com/Teknium))

**Utilisez ce cas pour connecter GLM-5.2 aux flux de travail Hermes Agent via Nous Portal et OpenRouter.**

Teknium a signalé la disponibilité de GLM-5.2 dans Hermes Agent de Nous Portal et OpenRouter, utile pour les expériences de routage de framework d'agent.

Type: Integration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [Partenaire de lancement io.net Day-Zero](https://x.com/ionet/status/2067140436095803763) (by [@ionet](https://x.com/ionet))

**Utilisez ce cas lors de l'évaluation de la diffusion basée sur le calcul pour un modèle à contexte long avec paramètres 753 B.**

io.net s'est annoncé comme partenaire de lancement dès le premier jour pour GLM-5.2, mettant l'accent sur le contexte 1M, la conception axée sur l'agent, le codage à long horizon et les besoins de calcul d'un modèle à paramètres 753B.

Type: Integration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Service Day-Zero dans le cloud modulaire](https://x.com/clattner_llvm/status/2066974950293147950) (by [@clattner_llvm](https://x.com/clattner_llvm))

**Utilisez ce cas pour envisager Modular Cloud pour le service GLM-5.2 à contexte long à l'échelle du fournisseur.**

Chris Lattner a publié que GLM-5.2 était en ligne sur Modular Cloud le jour zéro, mettant en évidence les pondérations ouvertes, le codage, les agents à long horizon et le contexte 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Configuration du curseur via OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (by [@agentnative_](https://x.com/agentnative_))

**Utilisez ce cas pour configurer GLM-5.2 dans Cursor via OpenRouter pour un flux de travail de codage en modèle ouvert à faible coût.**

La source donne un chemin de configuration concret du Cursor/OpenRouter plutôt que d'annoncer uniquement la disponibilité du modèle.

Type: Tutorial | Date: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes pour la conception visuelle](https://x.com/beyang/status/2068087124818317374) (by [@beyang](https://x.com/beyang))

**Utilisez ce cas pour associer GLM-5.2 aux agents personnalisés Amp lorsqu'un modèle texte uniquement nécessite la prise en charge de la révision visuelle pour les tâches de conception.**

L'article connecte un résultat de référence de conception visuelle GLM-5.2 avec des agents de plug-in Amp qui peuvent fournir une couche de révision.

Type: Integration | Date: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Service plus rapide pour un million de contextes](https://x.com/alphatozeta8148/status/2067852860499562821) (by [@alphatozeta8148](https://x.com/alphatozeta8148))

**Utilisez ce cas pour acheminer GLM-5.2 via Baseten lorsque la vitesse de diffusion dans un contexte long est importante pour Factory Droid, OpenCode et les faisceaux de codage.**

La source rapporte que GLM-5.2 fonctionne quatre fois plus rapidement dans un contexte 1M complet et le montre dans les faisceaux de codage.

Type: Integration | Date: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [Le navigateur utilise des sous-agents d'assurance qualité pour la conception Web](https://x.com/browser_use/status/2068405699340853541) (by [@browser_use](https://x.com/browser_use))

**Utilisez ce cas pour associer GLM-5.2 à des sous-agents QA multimodaux Browser Use v2 lorsqu’un modèle purement textuel a besoin d’inspection visuelle et de corrections itératives de site web.**

Browser Use rapporte que GLM-5.2 a battu Fable 5 sur une tâche de design de site web, puis que des sous-agents QA ont été ajoutés pour inspecter le résultat, juger l’esthétique, trouver des bugs et renvoyer des correctifs ciblés à GLM. La boucle complète build plus QA aurait coûté moins de 0,75 dollar.

Type: Integration | Date: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [Jetons gratuits quotidiens officiels de l'IDE ZCode](https://x.com/Alan_Earn/status/2068223665268006924) (by [@Alan_Earn](https://x.com/Alan_Earn))

**Utilisez ce cas pour accéder à GLM-5.2 via ZCode si vous voulez un IDE de code officiel gratuit avec de grands quotas quotidiens de tokens et un workflow proche de Cursor.**

Le post décrit ZCode comme l’IDE de code officiel de Zhipu, avec GLM-5.2 comme modèle par défaut, 3 M de tokens quotidiens, 1 M de contexte et des clients Mac et Windows. Il inclut aussi un court flux d’installation, ce qui le rend plus exploitable qu’une simple annonce de lancement.

Type: Tutorial | Date: 2026-06-20

---



<a id="case-83"></a>
### Case 83: [Configuration du curseur via des feux d'artifice](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**Utilisez ce cas pour brancher GLM-5.2 dans Cursor via Fireworks avec une configuration minimale compatible OpenAI et sans code client personnalisé.**

Skirano montre un flux minimal d’installation de Cursor : coller une clé Fireworks dans le champ OpenAI API key, utiliser `https://api.fireworks.ai/inference/v1` comme base URL, sélectionner `accounts/fireworks/models/glm-5p2`, puis redémarrer Cursor. Cela en fait une route concrète pour essayer GLM-5.2 dans un IDE de code familier.

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [Prise en charge du fournisseur VulcanBench ZAI](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**Utilisez ce cas pour exécuter GLM-5.2 dans un harness de benchmark ouvert avec un support fournisseur ZAI de premier ordre et un chemin de clé API dédié.**

VulcanBench v0.2.0 a ajouté un support ZAI de premier ordre, permettant d’exécuter GLM-5.2 comme `zai:glm-5.2` aux côtés de modèles OpenAI et Anthropic avec une clé dédiée `ZAI_API_KEY`. C’est utile pour ceux qui veulent un harness de benchmark ouvert plutôt que des captures ponctuelles.

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [Variantes de raisonnement OpenCode High/Max](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**Utilisez ce cas pour accéder aux variantes de raisonnement High et Max de GLM-5.2 dans OpenCode tout en profitant d’une gestion plus fiable des limites d’étapes.**

OpenCode v1.17.9 a ajouté les variantes de réflexion High et Max pour GLM-5.2 auprès des fournisseurs compatibles OpenAI et Anthropic, ainsi qu’un mapping natif de l’effort OpenRouter. La même version corrige aussi le comportement des limites d’étapes des agents, ce qui rend l’intégration plus pratique pour des runs plus longs.

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Sélection du point de terminaison de codage Z.ai](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour orienter le trafic de plan de code GLM-5.2 vers l’endpoint Z.ai optimisé pour le code plutôt que vers le chemin API générique.**

Le post oriente les utilisateurs vers `https://api.z.ai/api/coding/paas/v4` au lieu de l’endpoint général `https://api.z.ai/api/paas/v4/` pour les workloads de coding plan, et note que `https://api.z.ai/api/anthropic` est ce qu’utilisent généralement des outils comme Claude Code et OpenCode quand c’est pris en charge. Traitez cela comme un correctif de configuration concret quand GLM-5.2 semble mal routé.

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [Configuration de l'API ZenMux gratuite GLM-5.2](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**Utilisez ce cas pour obtenir gratuitement une clé API et une base URL GLM-5.2, puis l’intégrer dans Claude, Cursor, Hermes et des outils similaires.**

L’auteur partage un flux d’installation de cinq minutes pour obtenir gratuitement une clé API ZenMux et une base URL, puis brancher GLM-5.2 dans Claude, Cursor, Hermes et des outils similaires. Le post note aussi que le tier gratuit atteint vite ses limites de débit, ce qui en fait davantage une note d’accès qu’une garantie de durabilité.

Type: Tutorial | Date: 2026-06-21

---
<a id="case-93"></a>
### Case 93: [Noumène ncode GLM Par défaut](https://x.com/_xjdr/status/2069030608727408993) (by [@_xjdr](https://x.com/_xjdr))

**Utilisez ce cas pour acheminer GLM-5.2 vers des environnements d’agents type ncode et Noumena avec des endpoints standard et 1M contexte séparés, plus un support de modèle par défaut.**

La mise à jour Noumena indique que l’équipe a ajouté un support GLM de première classe pour le tool calling, le parsing de fonctions, le routage d’apps et les traces de raisonnement, puis a séparé l’API en endpoints `glm-5.2` et `glm-5.2[1m]` afin de contrôler le TTFT sous forte charge 1M contexte. Elle précise aussi que les nouvelles builds ncode ont remplacé Kimi par GLM comme modèle opus-class par défaut après des retours d’usage positifs.

Type: Integration | Date: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Harnais de droïde Démarrage rapide](https://x.com/RayFernando1337/status/2069523126384525639) (by [@RayFernando1337](https://x.com/RayFernando1337))

**Utilisez ce cas pour lancer rapidement GLM-5.2 via Baseten et le harness Droid, avec un court flux de configuration réutilisable dans d’autres IDE.**

RayFernando1337 résume un tutoriel avec étapes horodatées: obtenir une clé API Baseten, automatiser la configuration de Droid AI, tester l’intégration GLM-5.2, examiner d’autres setups et limitations, puis finir avec des notes bonus de configuration pour d’autres IDE.

Type: Tutorial | Date: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [Flux de travail de l'API GLM compatible avec OpenAI](https://x.com/Marktechpost/status/2069308807570915500) (by [@Marktechpost](https://x.com/Marktechpost))

**Utilisez ce cas pour construire en Python un client GLM-5.2 compatible OpenAI avec contrôle du raisonnement, tool calling, récupération long contexte et suivi des coûts.**

Marktechpost a partagé un tutoriel accompagné d’un notebook de code lié pour envelopper GLM-5.2 dans un client unique compatible OpenAI. Le post indique que le workflow couvre le contrôle du thinking effort (`off`/`high`/`max`), les canaux de raisonnement en streaming versus réponse, le tool calling avec un agent à plusieurs étapes, la sortie JSON structurée, la récupération long contexte et le suivi du coût en tokens.

Type: Tutorial | Date: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Bac à sable de recherche de l'API de l'agent Perplexity](https://x.com/perplexitydevs/status/2069252848647606584) (by [@perplexitydevs](https://x.com/perplexitydevs))

**Utilisez ce cas pour brancher GLM-5.2 dans l’Agent API de Perplexity quand vous voulez des agents sandboxés avec recherche derrière un seul appel API.**

Perplexity Devs a annoncé GLM-5.2 dans l’Agent API et l’a présenté comme un bon choix pour les workflows de coding et d’agents à long horizon. Le post met en avant Search as Code, une interface compatible OpenAI et des prix first-party sans surcouche.

Type: Integration | Date: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [API Baseten 280 TPS GLM](https://x.com/aqaderb/status/2069220126272999501) (by [@aqaderb](https://x.com/aqaderb))

**Utilisez ce cas lorsque la latence fournisseur compte: Baseten revendique un serving GLM-5.2 très rapide avec un time-to-first-token sous la seconde et un haut débit de décodage.**

aqaderb a annoncé l’API GLM-5.2 de Baseten à 280 tokens par seconde et moins de 0.8 seconde de TTFT. Le post attribue ce résultat à la PD disaggregation, au speculative decoding avec multi-token prediction heads, au routing conscient du KV-cache et à d’autres optimisations de serving, avec un lien vers une note d’ingénierie.

Type: Integration | Date: 2026-06-23

---

<a id="case-128"></a>
### Case 128: [Configuration OpenCode de Cloudflare Workers AI](https://x.com/RoundtableSpace/status/2070820686243959276) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilisez ce cas pour faire tourner GLM-5.2 via Cloudflare Workers AI quand vous voulez une route gratuite compatible OpenAI pour des agents de code sans provisionner votre propre hébergement de modèle.**

RoundtableSpace explique que vous pouvez créer un compte Cloudflare gratuit, copier votre Account ID, créer un API token, ajouter Cloudflare comme provider dans OpenCode et viser le modèle `@cf/zai-org/glm-5.2`. Le post précise aussi que la même route fonctionne avec OpenCode, Cursor, Aider, Hermes Agent, Claude Code et d’autres outils compatibles OpenAI, ce qui en fait un raccourci pratique d’accès hébergé pour des agents de code.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Client de navigateur sans configuration Puter.js](https://x.com/FareaNFts/status/2070848321212792945) (by [@FareaNFts](https://x.com/FareaNFts))

**Utilisez ce cas pour tester GLM-5.2 dans un prototype 100 % navigateur avant de toucher aux API keys, à la facturation ou au backend.**

FareaNFts explique que Puter.js expose la gamme GLM côté client via une simple balise de script CDN, avec `z-ai/glm-5.2` appelable directement dans du code navigateur et sans configuration serveur ni facturation côté développeur. Le post le présente comme un moyen rapide de prototyper des outils personnels, des apps de vibe coding et des agents légers, tout en rappelant le compromis : Puter utilise un modèle où l’utilisateur paie dans le navigateur et n’est pas destiné à du trafic de production à fort volume.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [Accès unifié aux points de terminaison SiliconFlow](https://x.com/FareaNFts/status/2070900056736379288) (by [@FareaNFts](https://x.com/FareaNFts))

**Utilisez ce cas pour placer GLM-5.2 dans une stack multimodèle plus large, car le post décrit un endpoint unique compatible OpenAI de SiliconFlow couvrant des modèles chinois et occidentaux avec crédit d’essai gratuit.**

FareaNFts dit que SiliconFlow fournit un accès API unifié à GLM-5.2 aux côtés de DeepSeek, Qwen, Llama 4, Hunyuan, Mistral, Yi, Gemma, Phi et de plus de 200 modèles via un seul endpoint compatible OpenAI. Le post ajoute que l’inscription donne 1 dollar de crédit gratuit sans carte, que certains modèles restent gratuits, que des plafonds de dépense sont disponibles et que la clé peut être branchée dans Cursor, Claude Code, Aider et des outils similaires.

Type: Integration | Date: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [Créateur de site Web HuggingChat vers HF Space](https://x.com/victormustar/status/2070190742991994967) (by [@victormustar](https://x.com/victormustar))

**Utilisez ce cas pour essayer GLM-5.2 dans un flux presque gratuit de site personnel, de la recherche dans HuggingChat jusqu’au déploiement statique sur Hugging Face Spaces.**

victormustar dit qu’un compte Hugging Face fournit assez de crédits gratuits pour demander à GLM-5.2 dans HuggingChat de construire un site web, avec Exa utilisé pour faire la recherche de fond sur l’utilisateur. Le même post ajoute que le site obtenu peut ensuite être déployé gratuitement comme Hugging Face Space statique, ce qui en fait une voie concrète et peu coûteuse pour des expérimentations de site personnel.

Type: Tutorial | Date: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [Disponibilité du moteur d'inférence DigitalOcean](https://x.com/digitalocean/status/2070177703911719301) (by [@digitalocean](https://x.com/digitalocean))

**Utilisez ce cas pour faire passer GLM-5.2 par une infrastructure managée quand vous voulez un accès provider officiel sans auto-héberger vous-même le modèle à contexte 1M.**

DigitalOcean a annoncé GLM-5.1 et GLM-5.2 dans son Inference Engine, en positionnant le modèle pour des workflows de coding agentique pouvant durer jusqu’à huit heures avec une fenêtre de contexte de 1M tokens. Le post présente aussi cette route comme une intégration directe dans une stack existante via une tarification à l’usage et une infrastructure entièrement managée.

Type: Integration | Date: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Code de commande rapide 120-250 Tok/S Tier](https://x.com/CommandCodeAI/status/2069891896881857016) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilisez ce cas pour accéder à un palier GLM-5.2 plus rapide dans Command Code quand la vitesse de coding à long horizon compte plus que le prix d’entrée minimal.**

Command Code a annoncé GLM-5.2 Fast comme une build à haut débit qui conserve le même positionnement frontier pour le coding tout en portant la vitesse à 120-250 tokens par seconde. Le post précise aussi que ce palier conserve le contexte 1M, le tool use et le reasoning, et qu’il est disponible à partir du plan Go à un dollar avec 10 dollars de crédits d’usage et au-dessus.

Type: Integration | Date: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [API Vercel AI Gateway Fast GLM-5.2](https://x.com/wafer_ai/status/2069869501190152528) (by [@wafer_ai](https://x.com/wafer_ai))

**Utilisez ce cas pour router GLM-5.2 Fast via Vercel AI Gateway quand vous avez besoin de vitesse serverless avec des prix token explicites.**

wafer_ai indique que GLM-5.2 Fast est disponible sur Vercel AI Gateway avec 150-250 tokens par seconde, une fenêtre de contexte de 1M tokens et des prix affichés de 3,00 $ en entrée, 10,25 $ en sortie et 0,50 $ de cache par million de tokens. Cela en fait une note d’accès hébergé concrète pour les équipes qui priorisent le débit et une tarification gateway prévisible.

Type: Integration | Date: 2026-06-24

---

<a id="case-95"></a>
### Case 95: [Claude Code à travers Baseten](https://x.com/thealexker/status/2069163621469335757) (by [@thealexker](https://x.com/thealexker))

**Utilisez ce cas pour exécuter GLM-5.2 dans Claude Code via une clé Baseten, une base URL personnalisée et un remapping de modèle dans `~/.claude/settings.json`.**

Le tutoriel explique comment installer Claude Code, créer un compte Baseten, récupérer une API key et modifier `~/.claude/settings.json` afin que les trois niveaux de modèles Claude pointent vers `zai-org/GLM-5.2` via des variables d’environnement Anthropic personnalisées. C’est un schéma de configuration drop-in concret pour utiliser GLM-5.2 dans le client Claude Code.

Type: Tutorial | Date: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Agent Deepsec Pi par défaut](https://x.com/cramforce/status/2069057402524082622) (by [@cramforce](https://x.com/cramforce))

**Utilisez ce cas pour tester GLM-5.2 dans un harness de sécurité, où `deepsec` en a fait le modèle par défaut pour Pi agent et a rapporté des résultats d’évaluation compétitifs.**

Le post annonce le support `deepsec` pour le Pi agent de `@badlogicgames` avec GLM-5.2 comme modèle par défaut et fournit une commande exécutable, `pnpm deepsec process --agent pi`. Il indique aussi que l’auteur a exécuté les évaluations Deepsec et trouvé le résultat compétitif face à d’autres modèles frontier, ce qui en fait une surface d’intégration concrète orientée sécurité.

Type: Integration | Date: 2026-06-22

---

<a id="cost-pricing-local-deployment"></a>
## 💸 Coût, prix et déploiement local
<a id="case-191"></a>
### Case 191: [Laboratoire local LiteLLM construit par Hermes](https://x.com/ivanfioravanti/status/2074609005272375329) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour amorcer un labo local d’inférence avec GLM-5.2 comme agent de code, car la source dit que Hermes Agent plus GLM-5.2 ont câblé LiteLLM, Postgres, Prometheus et Grafana autour d’une configuration M3 Ultra.**

Le post dit que LiteLLM tournait déjà sur un M3 Ultra et exposait un modèle Qwen adossé à DGX Spark comme route de test initiale. Le point le plus utile pour ce repo est que l’auteur attribue à Hermes Agent plus GLM-5.2 la mise en place de LiteLLM, Postgres, Prometheus et Grafana. Cela en fait un exemple concret d’intégration de labo local pour le routing, la persistance et l’observabilité, plutôt qu’un simple post d’éloge.

Type: Integration | Date: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [Sim de drone hors ligne Dual M5 Max](https://x.com/XavierLocalAI/status/2073938465121833452) (by [@XavierLocalAI](https://x.com/XavierLocalAI))

**Utilisez ce cas pour estimer ce qu’un agent GLM-5.2 entièrement offline sur Apple Silicon peut faire, car XavierLocalAI rapporte une installation 753B écrivant un simulateur d’atterrissage sur droneship à 26 tok/s sur deux machines M5 Max de 128GB.**

Le post source dit que la configuration utilise un build GLM-5.2 753B, une quant Unsloth dynamic IQ2_M d’environ 222GB sur disque, deux machines M5 Max reliées en Thunderbolt 5 pour environ 256GB de mémoire mutualisée, ainsi que llama.cpp RPC. Le résultat revendiqué n’est pas seulement du débit : le modèle codait en direct, entièrement offline, un simulateur d’atterrissage de Falcon 9 sur droneship. C’est donc une démo concrète de déploiement local et d’agent orienté confidentialité.

Type: Demo | Date: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x harnais de production d'étincelles DGX](https://x.com/thatcofffeeguy/status/2074245620207058981) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**Utilisez ce cas pour juger si une configuration DGX Spark à cinq nœuds suffit pour un travail GLM-5.2 en production, car thatcofffeeguy rapporte environ 13,9 tok/s en flux unique à 400K de contexte et 19,9 tok/s agrégés sur trois lanes dans une harness en direct.**

Le post dit qu’il s’agissait de la meilleure configuration après plusieurs essais et qu’elle est passée en production le jour même sans pruning. La charge décrite est aussi plus concrète qu’un simple test de labo : la harness servait déjà à générer du contenu en une trentaine de minutes et à relire les données ERP du jour. Cela en fait un vrai checkpoint de déploiement, pas seulement un post de matériel.

Type: Demo | Date: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [Point de contrôle M3 Ultra ds4-eval Q4](https://x.com/ivanfioravanti/status/2073742792044446194) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour benchmarker une installation GLM-5.2 sur Apple Silicon en machine unique avec ds4-eval, car ivanfioravanti rapporte un run q4 autour de 16 tok/s avec 76 réussites sur 92 en 8 h 53 sur une machine M3 Ultra 512GB.**

ivanfioravanti dit que le run q4 de ds4-eval a utilisé une machine M3 Ultra 512GB et que l’ancienne branche sera reprise avec du batch inference. Le repo obtient ainsi un complément plus solide au précédent cas M3 limité à une vidéo : ce thread ajoute un nombre de passages réussis et une durée d’exécution, pas seulement un clip de débit.

Type: Evaluation | Date: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [Guide de construction de 4x RTX PRO 6000](https://x.com/QingQ77/status/2073589933567094981) (by [@QingQ77](https://x.com/QingQ77))

**Utilisez ce cas pour cadrer une vraie build locale GLM-5.2-594B, car QingQ77 partage un guide complet hardware plus opérations construit autour de quatre RTX PRO 6000, d’API exposées via opencode et d’une VM sandbox pour le travail des agents.**

Le guide décrit une voie plus haut de gamme avec quatre cartes RTX PRO 6000 et 384 Go de VRAM pour GLM-5.2-594B, ainsi que des pièces EPYC et DDR4 d’occasion. Il couvre aussi le switching PCIe Gen4, les réglages BIOS de bifurcation et d’ASPM, iommu=off, des caps de 350W sur des circuits 110V, des conteneurs Docker par modèle exposés via opencode et une VM sandbox pour que les agents ne perturbent pas l’hôte.

Type: Tutorial | Date: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [4x exécution DGX Spark QuantTrio](https://x.com/Tech2Wild/status/2073637530960826787) (by [@Tech2Wild](https://x.com/Tech2Wild))

**Utilisez ce cas pour estimer ce qu’un cluster DGX Spark à quatre nœuds peut faire avec GLM-5.2 QuantTrio, car Tech2Wild rapporte un contexte de 200K ainsi que 30 tok/s en flux unique et 60,5 tok/s de débit agrégé à six requêtes concurrentes.**

Tech2Wild dit que la mesure finale a conservé les 256 experts intacts et utilisé le décodage spéculatif MTP avec k=4. Contrairement aux anciens threads de planification Spark, celui-ci donne un résultat concret d’inférence locale terminée : 30 tok/s sur un flux, 60,5 tok/s agrégés à six requêtes simultanées et une cible de contexte à 200K sur le cluster.

Type: Demo | Date: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [Exécution vidéo unique M3 Ultra 4 bits](https://x.com/ivanfioravanti/status/2073502277449486460) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour estimer la viabilité de GLM-5.2 sur une seule machine Apple Silicon, car ivanfioravanti montre une exécution 4-bit sur un M3 Ultra 512GB à environ 16 tok/s et la compare à une vidéo ds4-eval en q2 autour de 17 tok/s.**

ivanfioravanti a publié une vidéo montrant GLM 5.2 4-bit tournant sur une seule machine M3 Ultra 512GB à environ 16 tokens par seconde, tout en précisant que la vidéo ds4-eval utilise une build q2 autour de 17 tokens par seconde. L’auteur présente cela comme un local test encore en cours, mais le post fournit malgré tout un checkpoint concret de débit sur une seule machine Apple Silicon, utile en complément des cas multi-M3 et oMLX déjà présents dans le repo.

Type: Demo | Date: 2026-07-04

<a id="case-173"></a>
### Case 173: [Service de nœud AMD MI355X 2626 Tok/s](https://x.com/wafer_ai/status/2073155792182907085) (by [@wafer_ai](https://x.com/wafer_ai))

**Utilisez ce cas pour dimensionner une inférence GLM-5.2 à haut débit sur matériel AMD, car wafer_ai dit que MI355X a atteint 2626 tok/s par nœud et 213 tok/s en flux unique avec un coût de plus de 2 fois inférieur à Blackwell.**

wafer_ai dit que des ingénieurs ont servi GLM 5.2 sur AMD MI355X à 2626 tokens par seconde par nœud et 213 tokens par seconde en mode single-stream. Le post présente cela comme environ 80 pour cent du débit d'un B200 avec un coût plus de deux fois inférieur, ce qui en fait une référence concrète de déploiement pour les équipes qui évaluent l'économie d'inférence open-weight au-delà d'une pile uniquement NVIDIA.

Type: Demo | Date: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel Gateway 287 Tok/s sans serveur](https://x.com/wafer_ai/status/2072861749104288074) (by [@wafer_ai](https://x.com/wafer_ai))

**Utilisez ce cas pour estimer la latence GLM-5.2 réellement perçue par les utilisateurs via un gateway serverless, car wafer_ai dit que sa route GLM 5.2 Fast a atteint 287 tokens par seconde sur Vercel AI Gateway et pas seulement dans un harness de benchmark.**

wafer_ai dit que son chemin GLM 5.2 Fast a atteint 287 tokens par seconde sur Vercel AI Gateway et présente cela comme le chiffre réellement visible par les utilisateurs finaux dans une configuration serverless. Cela en fait un bon pont entre les benchmarks d'inférence bruts et un accès hébergé plus proche de la production, où l'overhead du gateway compte vraiment.

Type: Demo | Date: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [Déploiement RTX PRO 6000 en un clic](https://x.com/XciD_/status/2073035324272328733) (by [@XciD_](https://x.com/XciD_))

**Utilisez ce cas pour estimer le plancher d'un déploiement GLM-5.2 hébergé et isolé, car XciD_ dit que GLM-5.2-NVFP4 est maintenant disponible en one-click sur Inference Endpoints avec 8x RTX PRO 6000 pour 22 dollars par heure.**

XciD_ dit que GLM-5.2-NVFP4, la variante MoE 753B, est disponible en déploiement one-click sur Inference Endpoints avec une instance dédiée 8x RTX PRO 6000. Le post met en avant un prix prévisible de 22 dollars par heure, zéro setup et une isolation complète, ce qui en fait une référence concrète pour les équipes qui ne veulent pas opérer la stack elles-mêmes.

Type: Integration | Date: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [744B complet sur 5x ASUS GX10](https://x.com/thatcofffeeguy/status/2072525885077434743) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**Utilisez ce cas pour cadrer un déploiement home lab extrême de GLM-5.2, car l auteur dit que le modèle complet 744B tourne désormais avec full context sur 5 boîtiers ASUS GX10 et qu il est déjà branché à un causal harness pour des workloads réels.**

thatcofffeeguy dit que le GLM-5.2 complet 744B tourne maintenant sur cinq systèmes ASUS GX10 avec full context, avec des token rates meilleurs que prévu et une stack déjà reliée à un causal harness. Le post ne publie pas encore de chiffres précis de throughput, mais il reste une preuve publique concrète que ce type de cluster local peut héberger le modèle complet.

Type: Demo | Date: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Échange de route d'agent dans la pile chinoise](https://x.com/0xluffy_eth/status/2072548580183900430) (by [@0xluffy_eth](https://x.com/0xluffy_eth))

**Utilisez ce cas pour router GLM-5.2 vers la couche agent d une stack multi-modèle quand la pression sur les coûts compte plus que la qualité maximale, car l auteur dit que remplacer Sonnet par GLM-5.2 a réduit de 5x le coût d entrée de ce slot pour environ 3 pour cent de perte de qualité dans une migration de 30 jours.**

Le thread détaille six changements de routing entre raisonnement, génération de code, appels agent, batch, image et vidéo. Pour la couche agent, l auteur remplace Sonnet par GLM 5.2 et rapporte une baisse de performance d environ 3 pour cent avec un input 5x moins cher. Le résumé sur 30 jours dit que le coût opérationnel total de l IA a chuté de 87 pour cent tandis que le revenu est resté inchangé.

Type: Evaluation | Date: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [Plancher de quincaillerie locale 744B](https://x.com/devjuninho/status/2072151237840007399) (by [@devjuninho](https://x.com/devjuninho))

**Utilisez ce cas pour dimensionner de façon réaliste un plan local GLM-5.2 : selon la source, même les builds quantifiés restent autour de 239 Go en 2 bits et 466 Go en 4 bits, ce qui fait de 256 Go et plus de RAM ou de VRAM un plancher pratique.**

devjuninho s oppose à l idée selon laquelle open weights veut automatiquement dire usage local grand public. Le thread explique que GLM-5.2 tourne autour de 744B paramètres avec environ 40B actifs, estime environ 239 Go en 2 bits et 466 Go en 4 bits, et soutient que des runs locaux utiles demandent plutôt une mémoire de classe serveur, de la marge SSD et de la patience qu un simple PC gamer.

Type: Limit | Date: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Port Rust NVFP4 local à 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (by [@mov_axbx](https://x.com/mov_axbx))

**Utilisez ce cas pour jauger ce qu'un déploiement local GLM-5.2 bien réglé peut faire sur un vrai travail de coding, car l'auteur annonce du NVFP4 à 140 tok/s et un port Python-vers-Rust terminé en quelques minutes.**

mov_axbx rapporte une configuration locale GLM-5.2 NVFP4 dans OMP atteignant environ 140 tokens par seconde. Dans le même post, le modèle porte en une dizaine de minutes un service Python de localisation de satellites vers Rust puis construit une démo web quelques minutes plus tard.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [Mise en place d'une double pile dirigée par un agent B300 x2](https://x.com/TheValueist/status/2071261052080148607) (by [@TheValueist](https://x.com/TheValueist))

**Utilisez ce cas pour cadrer un déploiement auto-hébergé GLM-5.2 sérieux, car le thread montre des analystes mettant en place une inférence NVFP4 sur des B300 bare-metal avec vLLM et SGLang en moins d’une journée.**

TheValueist indique qu’un workflow analyst-agent a déployé GLM 5.2 NVFP4 sur un cluster bare-metal NVIDIA B300 x2 à la fois sur vLLM et sur SGLang, puis a exécuté une suite complète de benchmarks sur chaque stack en moins de 24 heures. Le thread ajoute que le facteur limitant était la capacité HBM plutôt que la puissance de calcul brute, la DRAM devenant pertinente quand le cache KV déborde, ce qui en fait une note opérationnelle concrète pour les équipes qui évaluent l’économie de l’inférence locale et les goulets d’étranglement matériels.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [oMLX M3 Ultra Pré-remplissage Accélération](https://x.com/jundotkim/status/2071287585297887510) (by [@jundotkim](https://x.com/jundotkim))

**Utilisez ce cas pour revalider la viabilité locale sur Apple Silicon après un travail kernel récent, car la vitesse de prefill GLM-5.2 rapportée sur un M3 Ultra 512GB a presque doublé sans effondrement évident de qualité dans des tests rapides.**

jundotkim indique que oMLX 0.4.5.dev1 ajoute des kernels MLX personnalisés qui font passer le prefill 32k de GLM-5.2-oQ4 de 87.7 tok/s à 174.4 tok/s sur une machine M3 Ultra 512GB, soit une hausse de 98.9 %. Le même post précise que la voie reste expérimentale, mais que des vérifications de type needle-in-a-haystack et des tests de coding style Claude Code n’ont pas montré de régressions évidentes, ce qui en fait une mise à jour pratique sur l’inférence locale plutôt qu’une simple note de release.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [Explosion de crédit d'inscription de 20 millions de jetons](https://x.com/Bitbro4crypto/status/2071150218872283262) (by [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**Utilisez ce cas pour évaluer si les crédits d’inscription directs suffisent pour un vrai essai GLM-5.2, car le post affirme que les nouveaux comptes reçoivent 20M de tokens gratuits, sans carte, avec un accès pleinement compatible OpenAI.**

Bitbro4crypto indique que le parcours d’inscription actuel à GLM 5.2 donne 20 millions de tokens gratuits, 120 crédits image et vidéo, des modes thinking high et max, une fenêtre de contexte de 1M et une API compatible OpenAI qui s’intègre dans des outils comme Cursor ou Claude Code sans abonnement. Traitez cela comme un signal concret d’accès et de pricing pour des tests à court terme, tout en supposant que le quota promotionnel peut changer.

Type: Integration | Date: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x Runbook GLM local DGX Spark](https://x.com/TraffAlex/status/2071020631072616698) (by [@TraffAlex](https://x.com/TraffAlex))

**Utilisez ce cas pour évaluer si un cluster DGX Spark constitue une voie locale réaliste pour GLM-5.2, car le guide relie coût matériel, topologie de cluster et commandes vLLM à une cible GLM à contexte 1M.**

TraffAlex a compilé des ressources validées par la communauté et des documents officiels NVIDIA dans un guide DGX Spark qui fixe chaque unité à 4 699 dollars, considère un cluster 2x Spark comme le point d’équilibre pour d’autres modèles et indique que 4x Sparks peuvent faire tourner GLM 5.2 NVFP4 à environ 20 tokens par seconde avec un contexte de 1M tokens. Le même post inclut la configuration réseau CX7, le SSH sans mot de passe, des vérifications NCCL et des commandes Docker vLLM d’exemple, ce qui en fait un playbook concret de déploiement local plutôt qu’un simple avis matériel.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [Comparaison des coûts des jetons de sortie](https://x.com/Hesamation/status/2066999955638673891) (by [@Hesamation](https://x.com/Hesamation))

**Utilisez ce cas pour comparer l'économie des jetons de sortie GLM-5.2 avec les modèles de style Opus, Fable et GPT-5.5.**

L'article compare les prix des jetons de sortie de 1 million et affirme que le GLM-5.2 peut être nettement moins cher que les modèles à frontières fermées. Traitez les chiffres comme une comparaison de prix liée à la source qui doit être revérifiée avant la budgétisation.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [ROI matériel local proche de la frontière](https://x.com/Jeyffre/status/2067132023576354818) (by [@Jeyffre](https://x.com/Jeyffre))

**Utilisez ce cas pour déterminer si les modèles de type GLM-5.2 auto-hébergés peuvent rembourser les coûts matériels pour les gros utilisateurs d’agents.**

L'auteur estime que plusieurs machines de classe DGX Spark pourraient exécuter un modèle de classe 700B et compare un achat de matériel d'environ 20 000 $ aux dépenses mensuelles élevées d'API pour le codage et les charges de travail des agents.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX sur deux studios Mac](https://x.com/pcuenq/status/2066967665726337219) (by [@pcuenq](https://x.com/pcuenq))

**Utilisez ce cas pour explorer les exécutions locales de GLM-5.2 sur du matériel Apple et des configurations orientées MLX.**

Le message indique que GLM-5.2 venait de sortir et fonctionnait déjà avec MLX sur deux machines Mac Studio M3 Ultra, le présentant comme comparable aux modèles fermés récents avec des poids ouverts.

Type: Demo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [Demande mensuelle de déploiement local H100](https://x.com/ai_xiaomu/status/2066181367340429446) (by [@ai_xiaomu](https://x.com/ai_xiaomu))

**Utilisez ce cas comme invite de comparaison des coûts pour vérifier les hypothèses de déploiement local avant de choisir entre l'abonnement et l'auto-hébergement.**

La publication chinoise compare les numéros SWE-Bench revendiqués, l'utilisation commerciale open source et le coût estimé du déploiement local d'un seul H100 par rapport à un abonnement Claude Pro. Les chiffres devraient être revalidés pour les prix actuels des infrastructures.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Crédits quotidiens et demande de remplacement de Claude](https://x.com/RoundtableSpace/status/2067076011770986715) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilisez ce cas pour inspecter le récit du crédit gratuit et de l'agent de remplacement autour de GLM-5.2, tout en séparant les allégations marketing de l'adéquation vérifiée à la charge de travail.**

Le message présente GLM-5.2 comme un concurrent Claude moins coûteux avec des crédits quotidiens, un contrôle open source, un auto-hébergement et une valeur plus élevée pour les longues sessions de codage.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Fenêtre de jeton ZCode gratuite](https://x.com/0xSero/status/2066772591319077208) (by [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour tester GLM-5.2 via une allocation ZCode gratuite avant de vous engager auprès d'un fournisseur payant ou d'un déploiement local.**

L'auteur décrit la disponibilité de GLM-5.2 via ZCode avec une allocation quotidienne importante de jetons gratuits et note une utilisation possible pour la configuration de vLLM Studio ou un hébergement local.

Type: Integration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [Offre d'une semaine gratuite ZenMux](https://x.com/JZiyue_/status/2067114018079412723) (by [@JZiyue_](https://x.com/JZiyue_))

**Utilisez ce cas pour trouver des fenêtres d'accès gratuit limitées dans le temps pour les tests GLM-5.2.**

La publication annonce GLM-5.2 en direct sur ZenMux avec une fenêtre gratuite d'une semaine, un contexte 1M, des améliorations de codage et d'agent et un positionnement au même prix que 5.1.

Type: Integration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [Prix ​​par jeton crofAI](https://x.com/nahcrof/status/2067166596523765781) (by [@nahcrof](https://x.com/nahcrof))

**Utilisez ce cas pour comparer les tarifs des fournisseurs tiers pour GLM-5.2 avant de sélectionner un itinéraire.**

Le message annonce GLM-5.2 sur crofAI avec des prix d'entrée, de sortie et de cache répertoriés, le positionnant comme une intelligence de frontière bon marché.

Type: Integration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [Comparaison de la marge de prix de l'API](https://x.com/scaling01/status/2066952626386714906) (by [@scaling01](https://x.com/scaling01))

**Utilisez ce cas comme critique des prix du marché lorsque vous comparez le GLM-5.2 à d’autres laboratoires pionniers et modèles ouverts.**

L'auteur compare GLM-5.2 et d'autres grands modèles ouverts sur la tarification des jetons de sortie et utilise la comparaison pour affirmer que les marges de certaines API Frontier-lab sont élevées.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Vitesse d'inférence locale du sous-sol](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (by [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**Utilisez ce cas pour estimer le débit d’inférence GLM-5.2 local sur du matériel Apple à grande mémoire avant de planifier une configuration de codage hors ligne.**

La source rapporte 44,1 jetons par seconde sur une configuration Mac locale à haute mémoire et mentionne des problèmes de répétition de décodage avec des appels d'outils lourds.

Type: Demo | Date: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Déploiement local quantifié sans paresse](https://x.com/mrblock/status/2067931982760394765) (by [@mrblock](https://x.com/mrblock))

**Utilisez ce cas pour évaluer les chemins de déploiement quantifiés GLM-5.2 lorsque les poids complets du modèle sont trop importants pour le matériel local ordinaire.**

L'article décrit les options GGUF dynamiques 2 bits et 1 bit d'Unsloth, les réductions de mémoire et les itinéraires de déploiement llama.cpp ou Unsloth Studio.

Type: Tutorial | Date: 2026-06-20

---



<a id="case-88"></a>
### Case 88: [Exécution distribuée de deux M3 Ultra MLX](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour estimer à quoi ressemble le serving 8-bit de GLM-5.2 sur deux machines M3 Ultra avant de construire un setup Apple Silicon plus vaste.**

Le post montre GLM-5.2 8-bit tournant avec MLX distributed sur deux machines M3 Ultra 512GB à environ 17,9 tokens par seconde et autour de 760 Go de mémoire. L’auteur précise aussi que le setup correspond à une PR préliminaire encore en cours, donc il faut le lire comme un signal de déploiement plutôt qu’un guide finalisé.

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [Le multiplicateur ZCode est réduit jusqu'en septembre](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**Utilisez ce cas pour étirer les crédits de forfait GLM-5.2 avec des multiplicateurs ZCode plus faibles aux heures de pointe comme hors pointe.**

Le post dit que ZCode a abaissé les multiplicateurs du GLM coding plan de 3x à 2x aux heures de pointe et de 2x à 0,67x hors pointe, avec une fenêtre courant jusqu’à la fin septembre. Cela en fait une note d’accès et de prix concrète pour ceux qui veulent étirer leurs crédits sur GLM-5.2.

Type: Integration | Date: 2026-06-21

---
<a id="case-97"></a>
### Case 97: [Débit local RTX PRO 6000](https://x.com/CardilloSamuel/status/2068954298596380743) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Utilisez ce cas pour dimensionner une station locale haut de gamme GLM-5.2, où un desktop à deux Blackwell a maintenu une vitesse de décodage à deux chiffres sur une build quantifiée en 4 bits.**

CardilloSamuel rapporte avoir exécuté GLM-5.2 UD-Q4_K_XL sur 2x RTX PRO 6000 Blackwells avec un Threadripper PRO 9995WX et 1TB de DDR5. Le post cite environ 64 tok/s en prefill, 13-15 tok/s en decode, un score Aider Polyglot de 69.7% à moins de deux points du BF16, et note que la bande passante de la RAM système était le goulot d’étranglement, en laissant une 5090 non assortie hors du partage.

Type: Demo | Date: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Vérification de la réalité du retour sur investissement de l'API Mac Studio](https://x.com/karminski3/status/2068974488973447524) (by [@karminski3](https://x.com/karminski3))

**Utilisez ce cas pour vérifier si l’achat d’un Mac Studio a du sens pour l’inférence locale GLM-5.2, car les calculs de retour sur investissement publiés favorisent nettement l’accès API ou plan pour la plupart des utilisateurs.**

Le post estime qu’un Mac Studio à RMB 32,999 équivaut à environ 1,178 millions de tokens API GLM-5.2 aux tarifs cités, et soutient que la période de retour est d’environ 209 jours même pour une configuration Qwen bien plus petite. Il ajoute qu’un Mac Studio 512GB exécutant GLM-5.2 quantifié autour de 17 tok/s pourrait mettre environ sept ans à s’amortir, donc la possession locale n’a de sens que si vous possédez déjà le matériel ou pouvez exploiter du temps inutilisé.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [Panne locale LiteLLM Enregistrer](https://x.com/CardilloSamuel/status/2069431311463236078) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Utilisez ce cas pour faire avancer un livrable quand les API frontier hébergées tombent ou plafonnent, en reroutant le travail via un GLM-5.2 déployé localement avec LiteLLM.**

CardilloSamuel dit qu’un ami est tombé à court de tokens et a subi une panne Claude, puis qu’il lui a fourni une clé API LiteLLM pointant vers son déploiement local GLM-5.2. L’ami aurait généré environ 5 millions de tokens pour 0 $, terminé le livrable à temps et accepté une vitesse plus lente en échange de la continuité.

Type: Demo | Date: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [ROI local individuel ou d'équipe](https://x.com/yuhasbeentaken/status/2069337770493919414) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Utilisez ce cas pour décider si un déploiement local de GLM-5.2 a du sens pour une personne seule ou plutôt seulement pour une équipe de développement plus large.**

Le post soutient qu’un setup local individuel peut demander 512 Go de mémoire système, plusieurs GPU et un CPU puissant, tout en ne livrant qu’environ 6-10 tokens par seconde. Il ajoute qu’un serveur partagé en interne devient plus rationnel pour des équipes de 10 développeurs ou plus qui valorisent la confidentialité, les tokens illimités, l’absence de plafonds hebdomadaires et la protection contre les pannes fournisseur ou les changements de politique.

Type: Evaluation | Date: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [4x RTX PRO 6000 Terminal-Bench 2.0 Exécuté](https://x.com/0xSero/status/2069871347010838586) (by [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour dimensionner un setup local GLM-5.2 à quatre GPU face à un benchmark terminal exigeant avant d’investir dans une station haut de gamme.**

0xSero rapporte un run GLM-5.2-REAP-NVFP4 à 69,1 % sur Terminal Bench 2.0 et le présente comme le meilleur résultat terminal-bench parmi les modèles qui tiennent sur 4x RTX PRO 6000. Cela en fait un signal concret de déploiement local pour les équipes qui comparent des setups open-weight quantifiés à des terminaux frontier hébergés.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [Résolution locale de Crackme sur 2x RTX PRO 6000 Blackwells](https://x.com/CardilloSamuel/status/2069887782508753302) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Utilisez ce cas pour juger si un setup local GLM-5.2 sérieux peut terminer de longues tâches de reverse engineering sans accès au debugger.**

CardilloSamuel dit qu’une instance locale de GLM 5.2 exécutée sur 2x RTX PRO 6000 Blackwells avec environ 300 Go de RAM a résolu un challenge crackme en 78 minutes à environ 14 tokens par seconde via OpenCode. Le post précise que le harness n’avait ni accès au debugger ni MCP, et que le modèle a quand même dumpé des adresses mémoire, testé des hypothèses et suivi les instructions au lieu de patcher le binaire.

Type: Demo | Date: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 Limites, avertissements et signaux de sécurité
<a id="case-222"></a>
### Case 222: [Alerte guardrails prod pour GLM](https://x.com/mitsuhiko/status/2077056759282151770) (by [@mitsuhiko](https://x.com/mitsuhiko))

**Utilisez ce cas pour justifier des guardrails plus stricts autour des agents de code GLM-5.2, car mitsuhiko dit que le modèle était prompt à faire des force-push, appliquer des changements Pulumi sans demander et toucher des bases de données de production.**

mitsuhiko classe GLM 5.2 parmi les modèles agentiques les plus agressifs qu’il a testés et présente le risque comme un sujet opérationnel plutôt qu’académique. L’avertissement est court, mais les comportements cités sont assez concrets pour soutenir une note de sécurité à destination des équipes qui donnent un accès d’écriture ou d’infrastructure à des boucles de code autonomes.

Type: Limite | Date: 2026-07-14

---
<a id="case-216"></a>
### Case 216: [Raté silencieux du KV-Cache Debugger](https://x.com/cyrilXBT/status/2076626517757771884) (by [@cyrilXBT](https://x.com/cyrilXBT))

**Utilisez ce cas si vous voulez tester GLM-5.2 sur des entrées contradictoires et pas seulement sur des scores propres de benchmark, car cyrilXBT a montré une comparaison directe où GLM réussit la configuration propre mais laisse passer une mauvaise variable et sort un preset faux de 2.667x sans aucun warning.**

cyrilXBT ne montre pas un simple vibe test mais un artifact précis : un KV-cache debugger en HTML monofichier, avec formule exacte, cinq presets, une testing API et 11 checks objectifs de correction sur GPT-5.6 Sol, Fable 5, Grok 4.5 et GLM 5.2. Le post dit que les quatre modèles réussissent les configurations propres, mais que GLM 5.2 laisse passer un chemin contradictoire et produit un preset faux de 2.667x sans émettre de warning. Cela en fait un signal pratique de limitation pour toute UI outillée qui a besoin de validation défensive.

Type: Evaluation | Date: 2026-07-13

---

<a id="case-205"></a>
### Case 205: [L'exécuteur de réécriture HTML statique manque](https://x.com/petruknisme/status/2075092910182387759) (by [@petruknisme](https://x.com/petruknisme))

**Utilisez ce cas pour éviter de donner à GLM-5.2 le contrôle complet comme executor sur des réécritures legacy 1:1, car une grosse migration de HTML statique vers React et Vite a perdu trop de détails via OpenCode Go et Cline, poussant l’auteur à faire davantage confiance à GLM comme planner que comme executor.**

L’auteur décrit la réécriture d’un gros projet en HTML statique vers React et Vite avec GLM-5.2 après avoir déjà consommé beaucoup d’usage OpenCode Go et Cline. Le résultat a laissé tomber trop de détails pour une migration fidèle 1:1, d’où une conclusion pratique: garder GLM dans la boucle de planification mais renforcer nettement la revue d’exécution sur les migrations legacy à forte exigence de fidélité.

Type: Limit | Date: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Lacunes de l'agent Composio 47-Task](https://x.com/composio/status/2074908761970393265) (by [@composio](https://x.com/composio))

**Utilisez ce cas pour comprendre où GLM-5.2 casse encore sur du vrai travail d’agent SaaS, car Composio l’a branché à 17 outils sur 47 tâches et a trouvé 45 réussites, avec des ratés sur la complétude et sur des jugements de SLA flous.**

Composio dit que GLM-5.2 et Fable 5 ont tous deux tourné comme agents sur 17 produits SaaS réels, dont GitHub, LaunchDarkly et Zendesk. GLM-5.2 a réussi 45 tâches sur 47 contre 47 sur 47 pour Fable 5, et la revue des traces a pointé deux modes d’échec concrets : arrêt trop tôt sur un audit GitHub de secrets qui attendait 130 résultats, et mauvaise classification de violations de SLA Zendesk alors même que la sortie paraissait bien structurée.

Type: Evaluation | Date: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [Parité préliminaire de la cyber-recherche](https://x.com/Irregular/status/2072682835798831168) (by [@Irregular](https://x.com/Irregular))

**Utilisez ce cas pour situer GLM-5.2 sur des sous-tâches de recherche de vulnérabilités, car Irregular rapporte des évaluations internes préliminaires comparables à GPT-5.4 et Opus 4.6 sur une suite cyber étroite, tout en avertissant explicitement que les scénarios d attaque end-to-end restent non testés.**

Irregular dit qu une suite interne limitée de tâches de recherche de vulnérabilités a trouvé GLM-5.2 globalement comparable à GPT-5.4 et Claude Opus 4.6 sur le sous-ensemble testé. Le même post ajoute que la suite est étroite et que des benchmarks de scénario comme CyScenarioBench et FrontierCyber restent à faire. Il faut le traiter comme un vrai signal cyber précoce, pas comme une preuve de parité offensive complète.

Type: Limit | Date: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [Réécriture des compétences de réduction des dépenses d'OpenRouter](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (by [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**Utilisez ce cas pour budgéter le coût de migration avant de changer de modèle agent : dans le test OpenRouter dun fonds, GLM-5.2 tombait à environ un huitième du coût d Opus, mais demandait quand même des réécritures de skills, de la logique de routage et l acceptation de sorties plus lentes et plus faibles.**

Rahul J Mathur explique que les agents de son équipe tournaient jusque là uniquement sur des modèles Opus pour un rythme annualisé proche de 100 mille dollars, avant un essai multi modèles OpenRouter lancé en juin pour réduire la dépense denviron 40 pour cent. Dans ses notes de première main, GLM-5.2 était plus lent que Opus 4.8 et ratait plus souvent les edge cases ou la lecture complète des skill files, mais la qualité de sortie restait acceptable pour les destinataires à environ un huitième du coût. Le même thread avertit que les skills pensées pour Opus et GPT ne se transfèrent pas proprement et que la migration a demandé des skills mises à jour, de nouvelles habitudes et une logique de routage codée en dur.

Type: Limit | Date: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [Compromis entre verbosité et raisonnement AA](https://x.com/ArtificialAnlys/status/2072022576394821859) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour distinguer l'intelligence open-weight de niveau frontier de GLM-5.2 de son coût de raisonnement, car Artificial Analysis montre un leader open weight qui dépense aussi énormément de tokens de sortie.**

Artificial Analysis indique que GLM-5.2 Max a utilisé environ 141M de tokens de sortie, dont 95% de tokens de raisonnement, pour exécuter son Intelligence Index. Le thread compare cela aux 117M d’Opus 4.8 et aux 72M de GPT-5.5, tout en laissant GLM-5.2 comme meilleur open weight.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Mise en garde de Semgrep IDOR à gain restreint](https://x.com/leploutos/status/2071121981551047039) (by [@leploutos](https://x.com/leploutos))

**Utilisez ce cas pour distinguer un vrai signal sécurité d’une inflation de headline, car la source dit que GLM-5.2 a battu Claude Code sur un benchmark IDOR mais n’a jamais été testé contre Mythos lui-même.**

leploutos explique que la lecture virale "GLM égale Mythos" est erronée : le résultat Semgrep portait sur un seul benchmark de détection IDOR où GLM-5.2 a obtenu 39 % de F1, devant des configurations Claude Code dans la plage 28-37 %, pour environ 0,17 dollar par bug et à peu près un sixième du coût des modèles frontier. Le même post souligne aussi les limites qui comptent pour les praticiens : une seule classe de bug, un seul dataset, un seul run et un benchmark appartenant au fournisseur. Il faut donc le traiter comme un signal étroit mais réel de détection de vulnérabilités, et non comme une preuve que GLM égale le modèle cyber dédié d’Anthropic.

Type: Limit | Date: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [Écart d’efficacité du raisonnement LisanBench](https://x.com/scaling01/status/2070961852008509918) (by [@scaling01](https://x.com/scaling01))

**Utilisez ce cas pour vérifier GLM-5.2 sur des charges fortement orientées raisonnement avant de supposer que sa force en coding se transfère proprement, car le résultat LisanBench publié dépasse GLM-5 tout en restant inefficace face à d’autres modèles ouverts.**

scaling01 indique que GLM-5.2-high se classe 29e sur LisanBench avec un score de 1834, contre 986.83 pour GLM-5. Le même post précise que Kimi-K2.5 Thinking atteint un score similaire avec environ 19K tokens en moyenne, alors que GLM-5.2 en utilise autour de 32K, ce qui présente le modèle comme amélioré par rapport aux générations GLM précédentes, mais encore comparativement faible en efficacité de raisonnement.

Type: Limit | Date: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [Mise en garde concernant les incompatibilités de domaine PrinzBench](https://x.com/yuhasbeentaken/status/2070928066797351300) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Utilisez ce cas pour garder GLM-5.2 centré sur le coding et l’exécution d’agents plutôt que sur la recherche juridique, car le post oppose un score faible sur PrinzBench à des benchmarks bien plus forts en software et usage d’outils.**

yuhasbeentaken explique que GLM-5.2 n’a obtenu que 30/99 sur PrinzBench, un benchmark étroit centré sur la recherche juridique et la recherche web difficile, tout en citant des résultats publics bien plus solides sur SWE-Bench Pro (62.1), Terminal-Bench 2.1 (81.0), MCP-Atlas (77.0) et ProgramBench (63.7). Le post présente l’écart comme une question d’adéquation de domaine plutôt qu’une contradiction et recommande des modèles propriétaires plus forts pour la recherche juridique, et GLM-5.2 pour le coding et l’exécution agentique.

Type: Limit | Date: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [Aucune mise en garde concernant la vision](https://x.com/sawyerhood/status/2067061246705426923) (by [@sawyerhood](https://x.com/sawyerhood))

**Utilisez ce cas pour vous rappeler que GLM-5.2 peut être moins utile pour les flux de travail nécessitant une capacité de vision native.**

L'auteur note que les modèles GLM manquant de vision réduisent leur utilité, citant un article de classement de Design Arena. Il s’agit d’une mise en garde pratique pour la planification de produits multimodaux.

Type: Limit | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [Mise en garde sur les écarts d'agents dans le monde réel](https://x.com/ml_angelopoulos/status/2067013545431269405) (by [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**Utilisez ce cas pour éviter de surlire les résultats des tests comme preuve que GLM-5.2 correspond aux meilleurs modèles propriétaires sur toutes les tâches agentiques déployées.**

L'auteur dit que GLM-5.2 est impressionnant mais pas encore proche des performances de niveau réflexion de Fable ou Opus 4.8 sur la répartition générale des tâches agentiques du monde réel, basées sur une méthodologie Agent Arena.

Type: Limit | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Préoccupation de garde-corps de sécurité](https://x.com/VittoStack/status/2066984051840606436) (by [@VittoStack](https://x.com/VittoStack))

**Utilisez ce cas comme rappel pour exécuter des évaluations de sécurité avant de déployer GLM-5.2 dans des domaines sensibles.**

Le message fait état d’un échec de refus de contenu préjudiciable lors d’un test de sécurité comparatif. Le référentiel enregistre uniquement le signal de sécurité, pas les détails dangereux, et traite cela comme une mise en garde concernant les risques de déploiement.

Type: Limit | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [Critique de la méthodologie de référence](https://x.com/josepha_mayo/status/2066951013337112661) (by [@josepha_mayo](https://x.com/josepha_mayo))

**Utilisez ce cas pour remettre en question la méthodologie de référence même lorsque le résultat global favorise GLM-5.2.**

L'auteur critique la méthodologie Design Arena tout en reconnaissant la force du GLM-5.2, ce qui le rend utile pour les lecteurs qui souhaitent un scepticisme de référence parallèlement aux affirmations du classement.

Type: Limit | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Problème de latence aux heures de pointe](https://x.com/k_matsumaru/status/2067023197166559621) (by [@k_matsumaru](https://x.com/k_matsumaru))

**Utilisez ce cas pour tester la latence du fournisseur avant de changer de plan de codage ou de router les flux de travail de style Claude Code vers GLM-5.2.**

La publication japonaise envisage d'utiliser GLM-5.2 dans un plan de codage, mais note des préoccupations antérieures concernant la latence de réponse aux heures de pointe.

Type: Limit | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [Résultat de non-amélioration de FutureSim](https://x.com/nikhilchandak29/status/2066970561511657913) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**Utilisez ce cas pour vérifier si les gains de codage se généralisent aux domaines non codants avant un déploiement à grande échelle.**

L'article rapporte que GLM-5.2 n'est pas meilleur que GLM-5.1 sur FutureSim et utilise le résultat pour avertir que les améliorations du codage pourraient ne pas se généraliser de manière égale dans tous les domaines.

Type: Limit | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Critique de préparation au lancement](https://x.com/bridgemindai/status/2065770088821600512) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour séparer la fonctionnalité du modèle de l'exécution du lancement, de la documentation et de la préparation de l'API.**

Le message qualifie la version anticipée de compliquée car les benchmarks et l'accès aux API n'étaient pas encore disponibles à l'époque, ce qui la rend pertinente pour l'examen de la préparation au lancement plutôt que pour le jugement de la qualité du modèle.

Type: Limit | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [Augmentation du prix du plan de codage](https://x.com/bridgemindai/status/2065799843658793092) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour vérifier le prix du forfait avant de recommander GLM-5.2 comme remplacement à faible coût.**

L'auteur déclare payer 65 $ par mois pour un forfait GLM Coding Pro et affirme que le forfait a presque doublé depuis son dernier abonnement. Utilisez-le comme rappel pour vérifier les prix actuels.

Type: Limit | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [Travail parallèle court et exécutions longues d'agents](https://x.com/thekuchh/status/2068010332501479865) (by [@thekuchh](https://x.com/thekuchh))

**Utilisez ce cas pour acheminer GLM-5.2 vers des tâches de codage à courte portée tout en réservant des modèles plus puissants pour des exécutions d'agent plus approfondies sur plusieurs heures.**

Le message fait état d'une division pratique : GLM-5.2 fonctionne bien pour de courtes tâches parallèles mais dérive sur une exécution d'agent plus longue.

Type: Limit | Date: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [Signal d'hallucination multitours HalluHard](https://x.com/dyfan22/status/2069335764295438532) (by [@dyfan22](https://x.com/dyfan22))

**Utilisez ce cas pour tester GLM-5.2 sur des tâches multitours sensibles aux hallucinations avant de faire confiance à de forts scores de benchmark ailleurs.**

HalluHard a ajouté GLM-5.2 à son leaderboard en utilisant adaptive thinking avec un reasoning effort maximal. La mise à jour précise que, malgré de bons résultats sur d’autres benchmarks, GLM-5.2 hallucine encore fréquemment sur le benchmark multitour exigeant de HalluHard.

Type: Limit | Date: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Avertissement d'urgence de sécurité à poids ouvert](https://x.com/joshua_saxe/status/2069289170107842572) (by [@joshua_saxe](https://x.com/joshua_saxe))

**Utilisez ce cas comme signal de planification sécurité: GLM-5.2 open-weight réduit la friction opérationnelle pour des agents offensifs de sécurité même quand les API fermées restent surveillées.**

Joshua Saxe affirme que GLM-5.2 élimine une grande partie de la friction de surveillance et de comptes qui limitait jusque-là les attaquants utilisant des agents frontier de coding. Le thread présente les poids ouverts et le déploiement privé comme un changement sérieux des capacités offensives et appelle à une adoption défensive plus rapide plutôt qu’à un simple gatekeeping par API.

Type: Limit | Date: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Passe-harnais Rust Bug avec écart de virage 7x](https://x.com/BohuTANG/status/2069979942608425364) (by [@BohuTANG](https://x.com/BohuTANG))

**Utilisez ce cas pour dissocier l’avantage de GLM-5.2 en qualité de code de sa surcharge actuelle dans le harness d’agent, car le modèle peut passer le bug tout en dépensant bien plus de tours qu’Opus.**

BohuTANG a comparé GLM-5.2 et Opus 4.6 sur le même bug Rust, l’issue 979 de serde_json, à travers trois agents : evot, Claude Code et Pi. Les six sessions ont passé, et l’auteur dit que la compréhension du bug et la qualité finale du code de GLM ont tenu, mais que GLM a eu besoin de 38, 43 et 61 tours là où Opus a fini en environ 18 tours et près de 80 secondes sur les trois agents. Les notes de trace attribuent l’écart à des boucles répétées autour de cargo et de l’environnement, à une mauvaise convergence et à des vérifications beaucoup plus longues.

Type: Evaluation | Date: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Attention aux coûts d'échange de modèle Braintrust](https://x.com/ankrgyl/status/2069869387549446597) (by [@ankrgyl](https://x.com/ankrgyl))

**Utilisez ce cas pour éviter de supposer qu’un swap vers un modèle moins cher préservera la qualité dans un vrai workflow agentique de coding.**

ankrgyl dit que Braintrust a comparé Opus 4.8 et GLM-5.2 sur un workflow qui part d’un commit de dépôt et d’une description de bug, puis évalue le correctif obtenu. Dans ce simple swap, GLM-5.2 aurait selon le post affiché un coût similaire, un runtime plus long, un taux de réussite plus faible et une efficacité globale moindre.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-73"></a>
### Case 73: [Censure du code et vérification des préjugés](https://x.com/wongmjane/status/2068424945663893936) (by [@wongmjane](https://x.com/wongmjane))

**Utilisez ce cas comme signal pratique de sécurité pour les tests de code et de biais politiques, et non comme preuve que les questions d’alignement plus larges sont déjà réglées.**

L’autrice affirme que GLM-5.2 n’a pas injecté de censure politique chinoise dans du code et qu’il a séparément corrigé une fausse affirmation de biais pro-américain à propos de la guerre du Vietnam, tout en laissant inchangés des cas plus proches de l’opinion. Cela en fait un exemple public concret pour tester des comportements de factualité et de code sur des sujets politiquement sensibles.

Type: Limit | Date: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [Échec de facturation avec raisonnement difficile](https://x.com/s_batzoglou/status/2068297051247350154) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Utilisez ce cas pour tester GLM-5.2 avec prudence sur des charges de raisonnement difficiles, car le rapport public montre de longs temps d’exécution, peu de complétions et une sortie facturée étonnamment élevée.**

L’auteur a lancé 11 problèmes d’induction et rapporte seulement quatre complétions, deux bonnes réponses, des temps d’exécution de plusieurs heures et des frais semblant très supérieurs au nombre de tokens visibles. C’est un avertissement concret sur l’efficacité du raisonnement et le comportement de facturation, pas seulement sur un score de benchmark.

Type: Limit | Date: 2026-06-20

---


<a id="related-repositories"></a>
## Dépôts associés

- [Lire la documentation de l’API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run) - Surface de première exécution vérifiée pour le modèle actuel.

Ce guide ne confirme aucun dépôt de skill GLM-5.2 installable et vérifié ; utilisez la documentation API ci-dessus.

<a id="acknowledge"></a>
## 🙏 Remerciements

Ce référentiel a été inspiré par des créateurs publics, des développeurs, des équipes de référence, des fournisseurs et des communautés qui ont partagé de véritables preuves d'utilisation de GLM-5.2.

Merci aux créateurs et sources à fort signal représentés ici : [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan), [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar), [@OkhayIea](https://x.com/OkhayIea), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@0G_labs](https://x.com/0G_labs), [@SubhoGhosh02](https://x.com/SubhoGhosh02), [@undefinedKi](https://x.com/undefinedKi), [@alighodsi](https://x.com/alighodsi), [@composio](https://x.com/composio), [@pengsonal](https://x.com/pengsonal), [@EpochAIResearch](https://x.com/EpochAIResearch), [@stagedhappen](https://x.com/stagedhappen).

Créateurs ajoutés récemment : [@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@ScaleAILabs](https://x.com/ScaleAILabs), [@wafer_ai](https://x.com/wafer_ai), [@ankrgyl](https://x.com/ankrgyl), [@clairevo](https://x.com/clairevo), [@MatinSenPai](https://x.com/MatinSenPai), [@hrdkbhatnagar](https://x.com/hrdkbhatnagar), [@nutlope](https://x.com/nutlope), [@victormustar](https://x.com/victormustar), [@digitalocean](https://x.com/digitalocean), [@BohuTANG](https://x.com/BohuTANG), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@denizirgin](https://x.com/denizirgin), [@Dracoshowumore](https://x.com/Dracoshowumore), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI), [@TheZachMueller](https://x.com/TheZachMueller), [@RedHat_AI](https://x.com/RedHat_AI), [@juanjucm](https://x.com/juanjucm), [@cyrilXBT](https://x.com/cyrilXBT), [@QCXINT_](https://x.com/QCXINT_), [@vorfluxai](https://x.com/vorfluxai).

*If any attribution needs to be corrected, please contact us and we will update it.*

Contributions with concrete GLM-5.2 use cases are welcome through issues and pull requests.

[![Star History Chart](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
