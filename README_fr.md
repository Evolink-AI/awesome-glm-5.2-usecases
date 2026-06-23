<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="Dépôt de cas d’usage GLM-5.2 banner" width="760"></a>

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

# Dépôt de cas d’usage GLM-5.2

## 🍌 Introduction

Bienvenue dans le dépôt de cas d’usage à forte valeur de GLM-5.2.

**Nous collectons des cas réels, tutoriels, intégrations, évaluations, signaux de prix et limites de GLM-5.2 depuis des démos publiques et des communautés de créateurs.**

Ce README localisé se concentre sur les cas avec workflows concrets, preuves publiques de benchmarks, démos pratiques, intégrations, coûts ou limites utiles.

Chaque titre de cas renvoie à sa source publique et chaque auteur renvoie au profil du créateur.

[Essayer GLM-5.2 sur Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 Vue d’ensemble

- **99 cas GLM-5.2 sélectionnés** provenant de créateurs publics, équipes de benchmark, développeurs d’outils, fournisseurs et utilisateurs de terrain.
- Couvre les évaluations comparatives et l’évaluation des modèles de pointe, les agents de code et les flux de travail à long contexte, les démos pratiques et exemples, les intégrations fournisseurs et outils, les coûts, les prix et le déploiement local, ainsi que les limites, avertissements et signaux de sécurité.
- Chaque cas inclut la source d’origine, l’attribution du créateur, un takeaway d’usage concis, le type de preuve et la date de publication.
- Utilisez ce repo pour trouver des workflows pratiques, comparer les forces et limites, découvrir des routes fournisseur et suivre des expériences réelles.

> [!NOTE]
> La collection privilégie les preuves concrètes au hype: démos publiées, méthodes de benchmark, notes d’intégration, données de coût et limites explicites.

> [!NOTE]
> Les README localisés conservent le même ordre de cas, les mêmes liens, anchors et attributions que la source anglaise. Certains titres restent proches de la langue source pour préserver la traçabilité.

<a id="-quick-api-access"></a>
## ⚡ Accès rapide à l’API

Utilisez GLM-5.2 via l’API Chat Completions compatible OpenAI d’Evolink. Obtenez une API key sur [Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases), puis définissez-la comme `EVOLINK_API_KEY` avant d’exécuter la requête.

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

Référence complète de l’API GLM-5.2 : [Ouvrir la documentation API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api).

## 📑 Menu

| Section | Cas |
|---|---|
| [📏 Évaluations comparatives et modèles de pointe](#benchmarks-frontier-evaluation) | Cas 1-12, 60, 70, 72, 76, 90, 94 |
| [💻 Agents de code et flux de travail à long contexte](#coding-agents-long-context-workflows) | Cas 13-22, 62, 65, 66, 77, 80, 91 |
| [🎮 Démos pratiques et exemples](#hands-on-demos-showcase-builds) | Cas 23-30, 71, 78, 81-82, 92, 99 |
| [🔌 Intégrations fournisseurs et outils](#provider-tool-integrations) | Cas 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96 |
| [💸 Coût, prix et déploiement local](#cost-pricing-local-deployment) | Cas 43-51, 64, 68, 88-89, 97-98 |
| [🧭 Limites, avertissements et signaux de sécurité](#limits-caveats-safety-signals) | Cas 52-59, 67, 73, 75 |
| [🙏 Remerciements](#acknowledge) | Crédits et politique de correction |

### [📏 Évaluations comparatives et modèles de pointe](#benchmarks-frontier-evaluation)

| Cas | Point clé | Type |
|---|---|---|
| [Artificial Analysis Intelligence Index](#case-1) | Utilisez la publication d'analyse artificielle pour comparer le GLM-5.2 à d'autres modèles frontières ouverts et propriétaires en termes d'intelligence et de coût par tâche. | Benchmark |
| [Code Arena Frontend Ranking](#case-2) | Utilisez ce cas pour évaluer GLM-5.2 sur de véritables tâches de codage front-end jugées par des comparaisons de type arène. | Benchmark |
| [Design Arena First Place](#case-3) | Utilisez ce cas pour juger si GLM-5.2 peut gérer des tâches de conception plus code plutôt que uniquement des tests de codage contenant beaucoup de texte. | Benchmark |
| [FrontierSWE Result](#case-4) | Utilisez la publication FrontierSWE pour comparer GLM-5.2 aux modèles de style GPT-5.5, Opus et Fable sur les tâches d'ingénierie logicielle. | Benchmark |
| [DeepSWE Open-Source Lead](#case-5) | Utilisez le cas DeepSWE pour comprendre GLM-5.2 comme un modèle ouvert solide pour les tâches difficiles d'évaluation de génie logiciel. | Benchmark |
| [Terminal-Bench Over 80 Percent](#case-6) | Utilisez ce cas lors de l’évaluation de GLM-5.2 pour le codage orienté terminal et les flux de travail d’agent. | Benchmark |
| [Comparaison SWELancer avec GPT-5.5](#case-7) | Utilisez ce cas SWELancer comme comparaison multimétrique concrète entre GLM-5.2 et GPT-5.5 sur la réussite des tâches, la récompense et le temps d'achèvement. | Évaluation |
| [BridgeBench Perfect Score Signal](#case-8) | Utilisez ce cas pour inspecter GLM-5.2 sur la base d'un raisonnement en plusieurs étapes plutôt que de coder uniquement des classements. | Benchmark |
| [BridgeBench Reasoning Number One](#case-9) | Utilisez ce cas pour comparer GLM-5.2 avec des modèles à frontières fermées sur des tâches de raisonnement fondées. | Benchmark |
| [KernelBench-Hard Without Shortcutting](#case-10) | Utilisez ce cas pour vérifier si les gains de référence proviennent d'un comportement d'implémentation valide plutôt que d'un raccourci. | Évaluation |
| [Runescape Bench Catch-Up](#case-11) | Utilisez ce cas comme un signal rapide pour la progression du modèle à poids ouvert sur des tâches de référence de type jeu. | Benchmark |
| [BridgeBench Speed Improvement](#case-12) | Utilisez ce cas pour évaluer les flux de travail sensibles à la latence où la vitesse compte aux côtés de l'intelligence. | Benchmark |
| [KernelBench Hard et Mega GPU Codage](#case-60) | Utilisez ce cas pour évaluer GLM-5.2 sur le codage du noyau GPU sur KernelBench-Hard et KernelBench-Mega, où les traces d'agent ouvertes rendent le résultat inspectable. | Benchmark |
| [DeepSWE Max-Effort Open-Source Lead](#case-70) | Utilisez ce cas pour suivre GLM-5.2 sur DeepSWE en mode effort maximal, où le leaderboard publié le place premier parmi les modèles ouverts avec un score de 44 % pass@1. | Benchmark |
| [LLM Debate Benchmark Runner-Up](#case-72) | Utilisez ce cas pour évaluer GLM-5.2 au-delà du code sur des débats adversariaux multi-tours, où la variante max-reasoning a pris la deuxième place derrière les modèles Claude. | Benchmark |
| [AA-Omniscience Hallucination Rate](#case-76) | Utilisez ce cas pour comparer GLM-5.2 sur la gestion de l’incertitude, où le résultat AA-Omniscience publié montre un taux d’hallucination plus faible que plusieurs autres modèles frontier. | Évaluation |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, plutôt que sur des classements limités au code. | Évaluation |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | Utilisez ce cas pour juger GLM-5.2 sur la qualité de création de jeux, où le modèle a atteint la deuxième place sur Game Dev Arena et est devenu le meilleur labo open-weight de ce classement. | Évaluation |

### [💻 Agents de code et flux de travail à long contexte](#coding-agents-long-context-workflows)

| Cas | Point clé | Type |
|---|---|---|
| [One Hour Forty Two Minute Refactor Loop](#case-13) | Utilisez ce cas comme modèle pour une longue refactorisation frontale autonome avec TDD, les commentaires des réviseurs et les contrôles de régression. | Démo |
| [OpenCode Bug Fix And Implementation Test](#case-14) | Utilisez ce cas pour tester GLM-5.2 en tant qu'agent de codage OpenCode pour les corrections de bogues ainsi qu'une petite tâche d'implémentation. | Démo |
| [OpenCode Retro Video Game Walkthrough](#case-15) | Utilisez cette procédure pas à pas pour créer un petit jeu avec GLM-5.2 et OpenCode à partir d'une seule invite, puis inspectez la manière dont le modèle gère les détails d'implémentation. | Tutoriel |
| [HTML5 Physics Simulations Contest](#case-16) | Utilisez ce cas pour comparer le code GLM-5.2 et Kimi K2.7 sur des simulations physiques HTML5 autonomes sans bibliothèques. | Évaluation |
| [Personal Site UI UX Build](#case-17) | Utilisez ce cas pour demander à GLM-5.2 un site personnel soigné et inspecter dans quelle mesure plusieurs tours peuvent améliorer l'UI/UX. | Démo |
| [AI Contract Review Product Build](#case-18) | Utilisez ce cas pour évaluer GLM-5.2 sur une tâche de création de produit avec un PRD, un budget temps, un nombre d'étapes, un quota d'utilisation et une comparaison de la qualité du code. | Évaluation |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | Utilisez ce cas pour comprendre comment GLM-5.2 est intégré dans ZCode 3.0 pour des tâches de développement agent plus importantes. | Intégration |
| [Wrapper Linux pour ZCode construit avec GLM-5.2](#case-20) | Utilisez ce cas comme exemple d'aide de GLM-5.2 avec des outils autour des environnements d'agent de codage. | Démo |
| [Computer Use Skill Packaging](#case-21) | Utilisez ce cas pour étudier GLM-5.2 en tant qu'aide pour transformer un dépôt informatique open source en une compétence réutilisable. | Démo |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | Utilisez ce cas pour évaluer GLM-5.2 dans un environnement de développement agent complet plutôt que dans une seule session de discussion. | Démo |
| [Harnais OpenCode avec service local](#case-62) | Utilisez ce cas pour tester GLM-5.2 avec l'exploitation OpenCode, le service local et les workflows de codage gourmands en outils avant de le comparer avec Claude Opus. | Évaluation |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | Utilisez ce cas pour améliorer le comptage de contextes longs GLM-5.2 et le comportement de l'agent REPL en déplaçant les instructions dans l'invite système RLM. | Intégration |
| [DeepAgents Code Open Harness Trial](#case-66) | Utilisez ce cas pour essayer GLM-5.2 avec un faisceau d'agents de codage ouvert et comparez le modèle sous un shell d'agent reproductible. | Démo |
| [Production Marketing Agent Stack Routing](#case-77) | Utilisez ce cas pour orienter GLM-5.2 vers des workflows d’agents en production qui valorisent structure, vitesse et self-hosting, tout en gardant des modèles fermés plus forts pour les jugements ambigus. | Évaluation |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | Utilisez ce cas pour comparer GLM-5.2 et Opus 4.8 sur un vrai bug de dépôt, où GLM a consommé plus de tokens mais a produit le patch final le moins cher et le plus propre. | Évaluation |

### [🎮 Démos pratiques et exemples](#hands-on-demos-showcase-builds)

| Cas | Point clé | Type |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | Utilisez ce cas pour comparer le résultat, la durée d'exécution et le coût de la création de jeux avec la même invite entre GLM-5.2 et Opus 4.8. | Démo |
| [Trois constructions réelles avec des résultats mitigés](#case-24) | Utilisez ce cas comme un ensemble de démonstration d'avertissement : testez plusieurs versions réelles avant de faire confiance à un modèle pour des tâches de production de jeux ou de vidéos. | Évaluation |
| [Super Mario Clone In ZCode](#case-25) | Utilisez ce cas pour évaluer la création de jeux itérative avec GLM-5.2 et ZCode sur plusieurs passes de correctifs et de fonctionnalités. | Démo |
| [Lunar Lander Contest](#case-26) | Utilisez ce cas pour comparer les codes GLM-5.2, MiniMax M3 et Kimi K2.7 sur une tâche de style jeu interactif. | Évaluation |
| [One-Prompt Design Arena Creation](#case-27) | Utilisez ce cas pour inspecter ce que GLM-5.2 peut générer à partir d'une seule invite de conception dans un contexte d'arène. | Démo |
| [Document de recherche Comprendre le flux de travail](#case-28) | Utilisez ce cas pour appliquer GLM-5.2 aux flux de travail de lecture papier avec des questions contextuelles et des références croisées. | Intégration |
| [Constrained Poem Comparison](#case-29) | Utilisez ce cas pour séparer l'exactitude de la qualité créative lorsque vous comparez GLM-5.2 avec les modèles de style Fable. | Évaluation |
| [Design Sense Example](#case-30) | Utilisez ce cas comme signal de conception visuelle léger, puis vérifiez avec votre propre invite et examen de l'interface utilisateur. | Démo |
| [Temple Run Voxel Game One-Shot](#case-71) | Utilisez ce cas pour stress-tester GLM-5.2 sur la génération de jeu en un seul prompt, puis examiner ce qui nécessite encore des corrections itératives dans un build visuellement riche. | Démo |
| [OpenCode Go One-Shot Example Set](#case-78) | Utilisez ce cas pour benchmarker GLM-5.2 sur des builds one-shot rapides dans OpenCode Go avant de l’engager dans des boucles d’agents plus ouvertes. | Démo |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | Utilisez ce cas pour tester GLM-5.2 sur une recréation web pilotée par référence, où un prompt plus une URL source ont reproduit un site avec une fidélité presque pixel-perfect. | Démo |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | Utilisez ce cas pour comparer GLM-5.2 sur des builds UI full-stack, où il s’est rapproché du résultat Trader Desk le plus soigné tout en ne coûtant qu’une petite fraction du meilleur résultat. | Évaluation |

### [🔌 Intégrations fournisseurs et outils](#provider-tool-integrations)

| Cas | Point clé | Type |
|---|---|---|
| [OpenCode Go Availability](#case-31) | Utilisez ce cas pour suivre la disponibilité de GLM-5.2 dans les workflows OpenCode Go avec du texte, un contexte 1M et une tarification de type GLM-5.1. | Intégration |
| [Ollama Cloud Availability](#case-32) | Utilisez ce cas pour acheminer GLM-5.2 vers Ollama Cloud pour des expériences de modèle de codage open source accessibles. | Intégration |
| [OpenRouter One API Call Access](#case-33) | Utilisez ce cas pour accéder à GLM-5.2 via OpenRouter lors de la comparaison du routage de fournisseur ou des piles multimodèles. | Intégration |
| [vLLM Day-Zero Support](#case-34) | Utilisez ce cas pour auto-héberger ou servir GLM-5.2 via vLLM avec une prise en charge jour zéro. | Intégration |
| [Notion Availability Via Baseten](#case-35) | Utilisez ce cas pour identifier GLM-5.2 en tant que modèle à poids ouvert disponible dans les flux de travail Notion. | Intégration |
| [Fireworks Day-Zero Serving](#case-36) | Utilisez ce cas pour évaluer Fireworks en tant que route de diffusion pour les charges de travail GLM-5.2 nécessitant une infrastructure hébergée. | Intégration |
| [Lien vers le jardin modèle Google Cloud](#case-37) | Utilisez ce cas pour trouver GLM-5.2 dans des contextes de déploiement orientés Google Cloud et de plate-forme d'agent. | Intégration |
| [Venice Privacy Mode](#case-38) | Utilisez ce cas lorsque le mode de confidentialité, TEE ou le chiffrement de bout en bout est un facteur décisif pour essayer GLM-5.2. | Intégration |
| [Command Code Availability](#case-39) | Utilisez ce cas pour essayer GLM-5.2 dans Command Code avec un plan d’entrée à faible coût et des fonctionnalités de codage à contexte long. | Intégration |
| [Agent Hermès du portail Nous](#case-40) | Utilisez ce cas pour connecter GLM-5.2 aux flux de travail Hermes Agent via Nous Portal et OpenRouter. | Intégration |
| [io.net Day-Zero Launch Partner](#case-41) | Utilisez ce cas lors de l'évaluation de la diffusion basée sur le calcul pour un modèle à contexte long avec paramètres 753 B. | Intégration |
| [Modular Cloud Day-Zero Serving](#case-42) | Utilisez ce cas pour envisager Modular Cloud pour le service GLM-5.2 à contexte long à l'échelle du fournisseur. | Intégration |
| [Cursor Setup Through OpenRouter](#case-61) | Utilisez ce cas pour configurer GLM-5.2 dans Cursor via OpenRouter pour un flux de travail de codage en modèle ouvert à faible coût. | Tutoriel |
| [Amp Agentic Eyes For Visual Design](#case-63) | Utilisez ce cas pour associer GLM-5.2 aux agents personnalisés Amp lorsqu'un modèle texte uniquement nécessite la prise en charge de la révision visuelle pour les tâches de conception. | Intégration |
| [Baseten Faster One-Million-Context Serving](#case-69) | Utilisez ce cas pour acheminer GLM-5.2 via Baseten lorsque la vitesse de diffusion dans un contexte long est importante pour Factory Droid, OpenCode et les faisceaux de codage. | Intégration |
| [Browser Use QA Subagents For Web Design](#case-74) | Utilisez ce cas pour associer GLM-5.2 à des sous-agents QA multimodaux Browser Use v2 lorsqu’un modèle purement textuel a besoin d’inspection visuelle et de corrections itératives de site web. | Intégration |
| [ZCode Official IDE Daily Free Tokens](#case-79) | Utilisez ce cas pour accéder à GLM-5.2 via ZCode si vous voulez un IDE de code officiel gratuit avec de grands quotas quotidiens de tokens et un workflow proche de Cursor. | Tutoriel |
| [Case 93: Noumena ncode GLM Default](#case-93) | Utilisez ce cas pour acheminer GLM-5.2 vers des environnements d’agents type ncode et Noumena avec des endpoints standard et 1M contexte séparés, plus un support de modèle par défaut. | Intégration |
| [Case 95: Claude Code Through Baseten](#case-95) | Utilisez ce cas pour exécuter GLM-5.2 dans Claude Code via une clé Baseten, une base URL personnalisée et un remapping de modèle dans `~/.claude/settings.json`. | Tutoriel |
| [Case 96: Deepsec Pi Agent Default](#case-96) | Utilisez ce cas pour tester GLM-5.2 dans un harness de sécurité, où `deepsec` en a fait le modèle par défaut pour Pi agent et a rapporté des résultats d’évaluation compétitifs. | Intégration |

### [💸 Coût, prix et déploiement local](#cost-pricing-local-deployment)

| Cas | Point clé | Type |
|---|---|---|
| [Output Token Cost Comparison](#case-43) | Utilisez ce cas pour comparer l'économie des jetons de sortie GLM-5.2 avec les modèles de style Opus, Fable et GPT-5.5. | Évaluation |
| [Local Near-Frontier Hardware ROI](#case-44) | Utilisez ce cas pour déterminer si les modèles de type GLM-5.2 auto-hébergés peuvent rembourser les coûts matériels pour les gros utilisateurs d’agents. | Évaluation |
| [MLX On Two Mac Studios](#case-45) | Utilisez ce cas pour explorer les exécutions locales de GLM-5.2 sur du matériel Apple et des configurations orientées MLX. | Démo |
| [H100 Monthly Local Deployment Claim](#case-46) | Utilisez ce cas comme invite de comparaison des coûts pour vérifier les hypothèses de déploiement local avant de choisir entre l'abonnement et l'auto-hébergement. | Évaluation |
| [Daily Credits And Claude Replacement Claim](#case-47) | Utilisez ce cas pour inspecter le récit du crédit gratuit et de l'agent de remplacement autour de GLM-5.2, tout en séparant les allégations marketing de l'adéquation vérifiée à la charge de travail. | Évaluation |
| [Free ZCode Token Window](#case-48) | Utilisez ce cas pour tester GLM-5.2 via une allocation ZCode gratuite avant de vous engager auprès d'un fournisseur payant ou d'un déploiement local. | Intégration |
| [ZenMux Free Week Offer](#case-49) | Utilisez ce cas pour trouver des fenêtres d'accès gratuit limitées dans le temps pour les tests GLM-5.2. | Intégration |
| [Prix ​​par jeton crofAI](#case-50) | Utilisez ce cas pour comparer les tarifs des fournisseurs tiers pour GLM-5.2 avant de sélectionner un itinéraire. | Intégration |
| [API Price Margin Comparison](#case-51) | Utilisez ce cas comme critique des prix du marché lorsque vous comparez le GLM-5.2 à d’autres laboratoires pionniers et modèles ouverts. | Évaluation |
| [Basement Local Inference Speed](#case-64) | Utilisez ce cas pour estimer le débit d’inférence GLM-5.2 local sur du matériel Apple à grande mémoire avant de planifier une configuration de codage hors ligne. | Démo |
| [Unsloth Quantized Local Deployment](#case-68) | Utilisez ce cas pour évaluer les chemins de déploiement quantifiés GLM-5.2 lorsque les poids complets du modèle sont trop importants pour le matériel local ordinaire. | Tutoriel |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | Utilisez ce cas pour dimensionner une station locale haut de gamme GLM-5.2, où un desktop à deux Blackwell a maintenu une vitesse de décodage à deux chiffres sur une build quantifiée en 4 bits. | Démo |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | Utilisez ce cas pour vérifier si l’achat d’un Mac Studio a du sens pour l’inférence locale GLM-5.2, car les calculs de retour sur investissement publiés favorisent nettement l’accès API ou plan pour la plupart des utilisateurs. | Évaluation |

### [🧭 Limites, avertissements et signaux de sécurité](#limits-caveats-safety-signals)

| Cas | Point clé | Type |
|---|---|---|
| [No Vision Caveat](#case-52) | Utilisez ce cas pour vous rappeler que GLM-5.2 peut être moins utile pour les flux de travail nécessitant une capacité de vision native. | Limite |
| [Mise en garde sur les écarts d'agents dans le monde réel](#case-53) | Utilisez ce cas pour éviter de surlire les résultats des tests comme preuve que GLM-5.2 correspond aux meilleurs modèles propriétaires sur toutes les tâches agentiques déployées. | Limite |
| [Safety Guardrail Concern](#case-54) | Utilisez ce cas comme rappel pour exécuter des évaluations de sécurité avant de déployer GLM-5.2 dans des domaines sensibles. | Limite |
| [Critique de la méthodologie de référence](#case-55) | Utilisez ce cas pour remettre en question la méthodologie de référence même lorsque le résultat global favorise GLM-5.2. | Limite |
| [Peak-Time Latency Concern](#case-56) | Utilisez ce cas pour tester la latence du fournisseur avant de changer de plan de codage ou de router les flux de travail de style Claude Code vers GLM-5.2. | Limite |
| [FutureSim Non-Improvement Result](#case-57) | Utilisez ce cas pour vérifier si les gains de codage se généralisent aux domaines non codants avant un déploiement à grande échelle. | Limite |
| [Launch Readiness Critique](#case-58) | Utilisez ce cas pour séparer la fonctionnalité du modèle de l'exécution du lancement, de la documentation et de la préparation de l'API. | Limite |
| [Augmentation du prix du plan de codage](#case-59) | Utilisez ce cas pour vérifier le prix du forfait avant de recommander GLM-5.2 comme remplacement à faible coût. | Limite |
| [Travail parallèle court et exécutions longues d'agents](#case-67) | Utilisez ce cas pour acheminer GLM-5.2 vers des tâches de codage à courte portée tout en réservant des modèles plus puissants pour des exécutions d'agent plus approfondies sur plusieurs heures. | Limite |
| [Code Censorship And Bias Check](#case-73) | Utilisez ce cas comme signal pratique de sécurité pour les tests de code et de biais politiques, et non comme preuve que les questions d’alignement plus larges sont déjà réglées. | Limite |
| [Hard Reasoning Billing Failure](#case-75) | Utilisez ce cas pour tester GLM-5.2 avec prudence sur des charges de raisonnement difficiles, car le rapport public montre de longs temps d’exécution, peu de complétions et une sortie facturée étonnamment élevée. | Limite |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 Évaluations comparatives et modèles de pointe

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez la publication d'analyse artificielle pour comparer le GLM-5.2 à d'autres modèles frontières ouverts et propriétaires en termes d'intelligence et de coût par tâche.**

L'analyse artificielle a signalé GLM-5.2 comme le principal modèle à pondérations ouvertes sur son indice d'intelligence, avec un score de 51 et une position frontière de Pareto sur l'intelligence par rapport au coût par tâche. La publication enregistre également la taille du modèle, la fenêtre contextuelle, les prix et la disponibilité du fournisseur.

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (par [@arena](https://x.com/arena))

**Utilisez ce cas pour évaluer GLM-5.2 sur de véritables tâches de codage front-end jugées par des comparaisons de type arène.**

Le compte Arena a rapporté que GLM-5.2 Max se classait deuxième dans Code Arena Frontend, devant les autres modèles ouverts et proche de la première entrée frontière. Cet article est particulièrement utile pour les cas d'utilisation du front-end, de React, du HTML, des jeux, de la simulation et de la conception basée sur des références.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (par [@Designarena](https://x.com/Designarena))

**Utilisez ce cas pour juger si GLM-5.2 peut gérer des tâches de conception plus code plutôt que uniquement des tests de codage contenant beaucoup de texte.**

Design Arena a rapporté que GLM-5.2 avait atteint la première place avec un score Elo de 1 360, soulignant une augmentation des performances du code de conception pour un modèle à poids ouverts. Traitez-le comme un signal de référence en matière de conception, et non comme un substitut à l'examen de l'interface utilisateur spécifique au projet.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (par [@ProximalHQ](https://x.com/ProximalHQ))

**Utilisez la publication FrontierSWE pour comparer GLM-5.2 aux modèles de style GPT-5.5, Opus et Fable sur les tâches d'ingénierie logicielle.**

L'article rapporte que GLM-5.2 se classe troisième sur FrontierSWE et le présente comme l'un des premiers modèles à poids ouvert à réduire l'écart avec les meilleurs modèles propriétaires sur les travaux d'ingénierie lourds de mise en œuvre.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (par [@AiBattle_](https://x.com/AiBattle_))

**Utilisez le cas DeepSWE pour comprendre GLM-5.2 comme un modèle ouvert solide pour les tâches difficiles d'évaluation de génie logiciel.**

AiBattle a rapporté un score DeepSWE de 46,2 % pour GLM-5.2 et l'a décrit comme le score le plus élevé pour un modèle open source dans ce contexte de référence.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (par [@cline](https://x.com/cline))

**Utilisez ce cas lors de l’évaluation de GLM-5.2 pour le codage orienté terminal et les flux de travail d’agent.**

Cline a souligné GLM-5.2 comme le premier modèle à poids ouvert à franchir 80 % sur Terminal-Bench et l'a positionné comme une option de pointe pour un développement basé sur des outils accessibles.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [Comparaison SWELancer avec GPT-5.5](https://x.com/gosrum/status/2067153091842203676) (par [@gosrum](https://x.com/gosrum))

**Utilisez ce cas SWELancer comme comparaison multimétrique concrète entre GLM-5.2 et GPT-5.5 sur la réussite des tâches, la récompense et le temps d'achèvement.**

L'auteur a partagé une mise à jour de référence japonaise dans laquelle GLM-5.2 a mené de manière inattendue GPT-5.5 sur les derniers résultats de SWELancer en termes de réussite des tâches, de récompense gagnée et de temps d'exécution, avec deux tâches inaccessibles exclues.

Type: Évaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (par [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour inspecter GLM-5.2 sur la base d'un raisonnement en plusieurs étapes plutôt que de coder uniquement des classements.**

BridgeMind a signalé GLM-5.2 comme le premier modèle à recevoir un score parfait sur le benchmark BridgeBench BS, ce qui en fait une source utile pour les affirmations d'évaluation lourdes de raisonnement.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (par [@bridgebench](https://x.com/bridgebench))

**Utilisez ce cas pour comparer GLM-5.2 avec des modèles à frontières fermées sur des tâches de raisonnement fondées.**

BridgeBench a rapporté que GLM-5.2 avait pris la première place dans un test de raisonnement et battu Claude Fable 5 dans ce contexte de mesure.

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (par [@elliotarledge](https://x.com/elliotarledge))

**Utilisez ce cas pour vérifier si les gains de référence proviennent d'un comportement d'implémentation valide plutôt que d'un raccourci.**

L'article de KernelBench-Hard indique que le résultat intéressant n'était pas seulement le score, mais que GLM-5.2 a cessé d'utiliser un raccourci inapproprié sur un problème GEMM fp8, ce qui le rend pertinent pour l'intégrité du benchmark.

Type: Évaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (par [@maxbittker](https://x.com/maxbittker))

**Utilisez ce cas comme un signal rapide pour la progression du modèle à poids ouvert sur des tâches de référence de type jeu.**

L'article rapporte que GLM-5.2 obtient de meilleurs résultats que les modèles propriétaires récents sur le banc Runescape, en utilisant ce résultat pour déterminer la rapidité avec laquelle les capacités de pointe open source rattrapent leur retard.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (par [@bridgebench](https://x.com/bridgebench))

**Utilisez ce cas pour évaluer les flux de travail sensibles à la latence où la vitesse compte aux côtés de l'intelligence.**

BridgeBench a signalé que GLM-5.2 est trois fois plus rapide que GLM-5.1 et quatrième sur son benchmark de vitesse, ce qui le rend pertinent pour les flux de travail où la vitesse d'itération affecte la convivialité.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [KernelBench Hard et Mega GPU Codage](https://x.com/elliotarledge/status/2068177175640240323) (par [@elliotarledge](https://x.com/elliotarledge))

**Utilisez ce cas pour évaluer GLM-5.2 sur le codage du noyau GPU sur KernelBench-Hard et KernelBench-Mega, où les traces d'agent ouvertes rendent le résultat inspectable.**

La mise à jour KernelBench signale les tests H100, B200 et RTX PRO 6000, les traces d'agents open source et GLM-5.2 comme le meilleur modèle ouvert de la comparaison.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [DeepSWE Max-Effort Open-Source Lead](https://x.com/datacurve/status/2068473057107476680) (par [@datacurve](https://x.com/datacurve))

**Utilisez ce cas pour suivre GLM-5.2 sur DeepSWE en mode effort maximal, où le leaderboard publié le place premier parmi les modèles ouverts avec un score de 44 % pass@1.**

DataCurve a partagé une mise à jour du leaderboard DeepSWE montrant GLM-5.2 à 44 % pass@1 et 17 points devant Kimi K2.7 Code parmi les modèles ouverts. Considérez cela comme une mise à jour de benchmark, pas comme une preuve que chaque workflow d’agent réel est déjà résolu.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [LLM Debate Benchmark Runner-Up](https://x.com/LechMazur/status/2068428300460974279) (par [@LechMazur](https://x.com/LechMazur))

**Utilisez ce cas pour évaluer GLM-5.2 au-delà du code sur des débats adversariaux multi-tours, où la variante max-reasoning a pris la deuxième place derrière les modèles Claude.**

Lech Mazur a partagé un résultat du LLM Debate Benchmark plaçant GLM-5.2 Max à la deuxième place. Le benchmark mesure des débats adversariaux multi-tours sur des sujets variés, ce qui en fait un signal de raisonnement en dehors des classements de code classiques.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [AA-Omniscience Hallucination Rate](https://x.com/yuhasbeentaken/status/2068259921519423855) (par [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Utilisez ce cas pour comparer GLM-5.2 sur la gestion de l’incertitude, où le résultat AA-Omniscience publié montre un taux d’hallucination plus faible que plusieurs autres modèles frontier.**

Le post rapporte un taux d’hallucination de 28 % pour GLM-5.2 sur AA-Omniscience, contre des taux plus élevés pour Fable 5 et DeepSeek V4 Pro. Le benchmark est présenté autour de la capacité des modèles à refuser ou admettre l’incertitude au lieu de deviner.

Type: Évaluation | Date: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour comparer GLM-5.2 sur du travail de connaissance à long horizon, plutôt que sur des classements limités au code.**

Artificial Analysis rapporte GLM-5.2 à 1524 Elo sur GDPval-AA, #3 au classement général derrière Claude Fable 5 et Opus 4.8, et légèrement devant GPT-5.5 xhigh à 1509. C’est de loin le meilleur modèle open-weights, et le post indique que le benchmark a moyenné environ 31 tours par tâche sur 1,999 matchs.

Type: Évaluation | Date: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (par [@Designarena](https://x.com/Designarena))

**Utilisez ce cas pour juger GLM-5.2 sur la qualité de création de jeux, où le modèle a atteint la deuxième place sur Game Dev Arena et est devenu le meilleur labo open-weight de ce classement.**

Design Arena a rapporté GLM-5.2 à 1368 Elo sur Game Dev Arena, soit un gain de 29 points et de six rangs par rapport à GLM-5.1. Le post le place dans la même bande de performance que Claude Fable 5 et indique qu’il s’est classé deuxième au général, devant OpenAI et derrière Anthropic seulement au niveau des laboratoires.

Type: Évaluation | Date: 2026-06-22

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 Agents de code et flux de travail à long contexte

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (par [@KELMAND1](https://x.com/KELMAND1))

**Utilisez ce cas comme modèle pour une longue refactorisation frontale autonome avec TDD, les commentaires des réviseurs et les contrôles de régression.**

L'article décrit une tâche de refactorisation GLM-5.2 d'une heure et 42 minutes avec 88 tours de modèle et 102 appels d'outils. Le flux de travail comprenait un transfert, quatre correctifs de bloqueurs, la mise en œuvre TDD de 12 tests, deux séries de correctifs P2 et une régression finale.

Type: Démo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (par [@altudev](https://x.com/altudev))

**Utilisez ce cas pour tester GLM-5.2 en tant qu'agent de codage OpenCode pour les corrections de bogues ainsi qu'une petite tâche d'implémentation.**

L'auteur rapporte avoir testé GLM-5.2 avec six corrections de bugs et une implémentation dans OpenCode, affirmant que les modifications se sont déroulées proprement avec une planification solide et une meilleure vitesse que GLM-5.1.

Type: Démo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (par [@AskVenice](https://x.com/AskVenice))

**Utilisez cette procédure pas à pas pour créer un petit jeu avec GLM-5.2 et OpenCode à partir d'une seule invite, puis inspectez la manière dont le modèle gère les détails d'implémentation.**

Venise a partagé une procédure complète pour créer un jeu vidéo rétro avec GLM-5.2 et OpenCode, le positionnant comme un flux de travail de codage privé, open source et à long horizon.

Type: Tutoriel | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (par [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilisez ce cas pour comparer le code GLM-5.2 et Kimi K2.7 sur des simulations physiques HTML5 autonomes sans bibliothèques.**

Atomic Chat a signalé avoir demandé aux deux modèles de créer des simulations de rupture de piscine, de bloc à ressort et de carte Galton. Leur message indique que GLM-5.2 a traité les trois avec plus de détails et de précision, tandis que Kimi avait du mal avec le comportement physique.

Type: Évaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (par [@anshuc](https://x.com/anshuc))

**Utilisez ce cas pour demander à GLM-5.2 un site personnel soigné et inspecter dans quelle mesure plusieurs tours peuvent améliorer l'UI/UX.**

L'auteur affirme que GLM-5.2 a produit un site personnel créatif après avoir été poussé avec la bonne incitation et a partagé une vidéo du résultat. Il est utile pour les itérations de conception frontale plutôt que pour les revendications de référence uniques.

Type: Démo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (par [@laozhang2579](https://x.com/laozhang2579))

**Utilisez ce cas pour évaluer GLM-5.2 sur une tâche de création de produit avec un PRD, un budget temps, un nombre d'étapes, un quota d'utilisation et une comparaison de la qualité du code.**

La publication chinoise compare GLM-5.2, Kimi K2.7 et Claude Opus 4.8 sur un produit PRD d'examen de contrats d'IA. Il indique la durée de la construction, le nombre d'étapes, l'utilisation du quota de cinq heures et l'évaluation de la qualité du code.

Type: Évaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (par [@zcode_ai](https://x.com/zcode_ai))

**Utilisez ce cas pour comprendre comment GLM-5.2 est intégré dans ZCode 3.0 pour des tâches de développement agent plus importantes.**

ZCode a annoncé la disponibilité de GLM-5.2 pour les utilisateurs du plan de codage, une exécution plus forte des tâches d'agent, un meilleur codage à contexte long et une fonctionnalité d'objectif pour gérer des objectifs plus larges, de la planification à l'achèvement.

Type: Intégration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [Wrapper Linux pour ZCode construit avec GLM-5.2](https://x.com/gosrum/status/2066484949755269510) (par [@gosrum](https://x.com/gosrum))

**Utilisez ce cas comme exemple d'aide de GLM-5.2 avec des outils autour des environnements d'agent de codage.**

L'auteur rapporte avoir terminé zcode-linux en utilisant GLM-5.2 et Claude Code afin que les utilisateurs de Linux puissent exécuter ZCode dans un environnement Linux et ajouter des points de terminaison d'API arbitraires, y compris des points de terminaison LLM locaux.

Type: Démo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (par [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour étudier GLM-5.2 en tant qu'aide pour transformer un dépôt informatique open source en une compétence réutilisable.**

Le message indique que GLM-5.2 configurait l'utilisation de l'ordinateur, trouvait un référentiel open source avancé et le convertissait en compétence. Il s’agit d’un signal pratique pour le travail d’emballage d’outils et d’intégration d’agents.

Type: Démo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (par [@laogui](https://x.com/laogui))

**Utilisez ce cas pour évaluer GLM-5.2 dans un environnement de développement agent complet plutôt que dans une seule session de discussion.**

La revue chinoise indique que ZCode 3.0 a été réécrit à partir de versions antérieures de type shell en un noyau d'agent auto-développé associé à GLM-5.2, avec une meilleure expérience parmi les environnements de développement d'agents nationaux.

Type: Démo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [Harnais OpenCode avec service local](https://x.com/PatrickToulme/status/2068134212587184442) (par [@PatrickToulme](https://x.com/PatrickToulme))

**Utilisez ce cas pour tester GLM-5.2 avec l'exploitation OpenCode, le service local et les workflows de codage gourmands en outils avant de le comparer avec Claude Opus.**

L'auteur rapporte un déploiement local, des sous-agents imbriqués, un comportement de recherche/planification et une version d'application fonctionnelle.

Type: Évaluation | Date: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (par [@neural_avb](https://x.com/neural_avb))

**Utilisez ce cas pour améliorer le comptage de contextes longs GLM-5.2 et le comportement de l'agent REPL en déplaçant les instructions dans l'invite système RLM.**

Les notes de version décrivent un changement concret d'échafaudage d'agent et un effet de référence à contexte long GLM-5.2.

Type: Intégration | Date: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (par [@sydneyrunkle](https://x.com/sydneyrunkle))

**Utilisez ce cas pour essayer GLM-5.2 avec un faisceau d'agents de codage ouvert et comparez le modèle sous un shell d'agent reproductible.**

L'auteur rapporte qu'il utilise GLM-5.2 avec DeepAgents Code et cadre un modèle ouvert ainsi qu'un harnais ouvert comme modèle de test.

Type: Démo | Date: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [Production Marketing Agent Stack Routing](https://x.com/DeRonin_/status/2068303752671477820) (par [@DeRonin_](https://x.com/DeRonin_))

**Utilisez ce cas pour orienter GLM-5.2 vers des workflows d’agents en production qui valorisent structure, vitesse et self-hosting, tout en gardant des modèles fermés plus forts pour les jugements ambigus.**

Après six jours de test côte à côte dans un stack d’agence, l’auteur dit que GLM-5.2 a tenu plus de 60 étapes d’agent avant de dériver, a respecté des formats structurés plus de 800 fois de suite et a livré des réponses self-hosted à faible latence. Le même post préfère encore Opus pour les tâches sensibles à la voix ou ambiguës, ce qui fait justement de cette règle de routage le principal enseignement utile.

Type: Évaluation | Date: 2026-06-20

---



<a id="case-80"></a>
### Case 80: [M3 Ultra Pokemon Red Goal Run](https://x.com/hxiao/status/2068800750554378434) (par [@hxiao](https://x.com/hxiao))

**Utilisez ce cas pour évaluer GLM-5.2 sur un run local d’agent de code à long horizon, où le modèle a passé environ une demi-journée à essayer de recréer Pokemon Red en HTML sur une machine M3 Ultra.**

L’auteur a remplacé le modèle de Claude Code par GLM 5.2 en local sur une machine M3 Ultra 512GB et a lancé pendant 12 heures la tâche `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.`. Le post partage la durée d’exécution, l’usage des tokens, le churn de code, l’usage RAM ainsi que le setup GGUF et KV cache, tout en notant que la qualité du modèle semblait de niveau frontier, tandis que le débit d’inférence local restait le goulot d’étranglement.

Type: Démo | Date: 2026-06-21

---
<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (par [@cline](https://x.com/cline))

**Utilisez ce cas pour comparer GLM-5.2 et Opus 4.8 sur un vrai bug de dépôt, où GLM a consommé plus de tokens mais a produit le patch final le moins cher et le plus propre.**

Cline a testé les deux modèles sur le même bug du dépôt Cline avec le même harness et les mêmes outils. Le post indique que GLM a utilisé environ 1.1M tokens contre 660K pour Opus, coûté $0.41 contre $0.81, pris 4.7 minutes et 28 appels d’outils contre 1.6 minute et 12 appels, puis terminé avec nettoyage de code mort et build de production réussie, alors qu’Opus a laissé des erreurs de type qui passaient quand même les tests.

Type: Évaluation | Date: 2026-06-22

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 Démos pratiques et exemples

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (par [@aimlapi](https://x.com/aimlapi))

**Utilisez ce cas pour comparer le résultat, la durée d'exécution et le coût de la création de jeux avec la même invite entre GLM-5.2 et Opus 4.8.**

L'API AI/ML a signalé avoir demandé à GLM-5.2 et Opus 4.8 de créer un jeu Backrooms jouable en une seule fois. Leur message indique que GLM-5.2 a construit une mécanique plus complète en 1:08 à 0,37 $, tandis qu'Opus a pris 2:14 à 1,94 $.

Type: Démo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [Trois constructions réelles avec des résultats mitigés](https://x.com/bridgemindai/status/2065840871929442319) (par [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas comme un ensemble de démonstration d'avertissement : testez plusieurs versions réelles avant de faire confiance à un modèle pour des tâches de production de jeux ou de vidéos.**

BridgeMind a testé GLM-5.2 sur un jeu de maison d'horreur, un jeu d'infiltration 3D et une vidéo marketing Remotion. Le message rapporte des résultats mitigés, y compris une logique de jeu brisée, ce qui le rend utile comme signal de limitation fondé.

Type: Évaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (par [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour évaluer la création de jeux itérative avec GLM-5.2 et ZCode sur plusieurs passes de correctifs et de fonctionnalités.**

L'auteur a testé ZCode 3.0 avec GLM-5.2 en créant un clone de style Super Mario, puis a partagé le résultat après cinq itérations de corrections de problèmes et d'ajouts de fonctionnalités.

Type: Démo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (par [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour comparer les codes GLM-5.2, MiniMax M3 et Kimi K2.7 sur une tâche de style jeu interactif.**

L'article décrit un concours Lunar Lander entre MiniMax M3, GLM-5.2 et Kimi K2.7 Code, en utilisant un résultat vidéo comme référence pratique avant de revenir au développement de modèles locaux.

Type: Évaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (par [@grx_xce](https://x.com/grx_xce))

**Utilisez ce cas pour inspecter ce que GLM-5.2 peut générer à partir d'une seule invite de conception dans un contexte d'arène.**

L'auteur a partagé un exemple de création GLM-5.2 sur Design Arena réalisée à partir d'une seule invite, en l'utilisant pour montrer l'écart réduit entre les modèles à poids ouvert et fermé.

Type: Démo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [Document de recherche Comprendre le flux de travail](https://x.com/askalphaxiv/status/2066996976445706745) (par [@askalphaxiv](https://x.com/askalphaxiv))

**Utilisez ce cas pour appliquer GLM-5.2 aux flux de travail de lecture papier avec des questions contextuelles et des références croisées.**

AlphaXiv a introduit GLM-5.2 pour comprendre les articles de recherche, dans lequel les utilisateurs mettent en évidence une section, posent des questions et référencent d'autres articles pour le contexte, les comparaisons et les références de référence.

Type: Intégration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (par [@emollick](https://x.com/emollick))

**Utilisez ce cas pour séparer l'exactitude de la qualité créative lorsque vous comparez GLM-5.2 avec les modèles de style Fable.**

Ethan Mollick a crédité GLM-5.2 Max pour avoir produit un poème contraint correct, tout en notant que Fable a incorporé la contrainte de lettre disparue dans le thème du poème de manière plus créative.

Type: Évaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (par [@0xSero](https://x.com/0xSero))

**Utilisez ce cas comme signal de conception visuelle léger, puis vérifiez avec votre propre invite et examen de l'interface utilisateur.**

L'auteur dit avoir apprécié le sens de la conception de GLM-5.2 et a partagé un exemple visuel. Il s'agit d'un indicateur utile pour l'inspection, et non d'une preuve autonome de la qualité de la conception de la production.

Type: Démo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Temple Run Voxel Game One-Shot](https://x.com/pseudokid/status/2068431546143649829) (par [@pseudokid](https://x.com/pseudokid))

**Utilisez ce cas pour stress-tester GLM-5.2 sur la génération de jeu en un seul prompt, puis examiner ce qui nécessite encore des corrections itératives dans un build visuellement riche.**

L’auteur explique avoir obtenu dès le premier tour l’essentiel d’un jeu de biker voxel inspiré de Temple Run, puis n’avoir eu besoin que de quelques passes supplémentaires pour corriger la caméra et les mouvements. Le post précise aussi que les outils Z.ai peuvent générer des captures d’écran et des vidéos de gameplay pour aider le modèle textuel à évaluer le résultat.

Type: Démo | Date: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [OpenCode Go One-Shot Example Set](https://x.com/LyalinDotCom/status/2068378281636982990) (par [@LyalinDotCom](https://x.com/LyalinDotCom))

**Utilisez ce cas pour benchmarker GLM-5.2 sur des builds one-shot rapides dans OpenCode Go avant de l’engager dans des boucles d’agents plus ouvertes.**

L’auteur rapporte des exemples one-shot couvrant une web app de système solaire, une application Electron d’informations système et un petit jeu web d’exploration d’île via OpenCode Go. Le même post dit aussi que GLM-5.2 est le meilleur modèle ouvert qu’il ait utilisé, sans pour autant le déclarer au niveau frontier.

Type: Démo | Date: 2026-06-20

---



<a id="case-81"></a>
### Case 81: [Space Invaders One-Prompt Build](https://x.com/DeryaTR_/status/2068803754611069128) (par [@DeryaTR_](https://x.com/DeryaTR_))

**Utilisez ce cas pour tester GLM-5.2 sur la création de jeu en un seul prompt, puis voir comment quelques passes supplémentaires gèrent les remplacements d’assets et un léger polissage.**

L’autrice dit que GLM-5.2 a construit un jeu jouable de type Space Invaders à partir d’un prompt principal, puis a utilisé trois prompts de suivi pour remplacer les sprites et ajouter de petits éléments comme un leaderboard. Le résultat publié est un exemple public léger de qualité de création de jeu, pas un benchmark complet.

Type: Démo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [OpenCode Recovery Lab One-Shot](https://x.com/threepointone/status/2068718370581536816) (par [@threepointone](https://x.com/threepointone))

**Utilisez ce cas pour prototyper rapidement des simulations interactives d’échec d’agent, car l’auteur dit avoir obtenu un recovery lab fonctionnel en one-shot pour environ 3,50 $.**

L’auteur a construit un recovery lab entièrement interactif avec OpenCode et GLM-5.2 après avoir fourni au modèle une analyse de 4 000 mots et le dépôt Agents SDK. Le post mentionne un run de 176k tokens, un résultat one-shot et un coût end-to-end d’environ 3,50 $ avant polissage.

Type: Démo | Date: 2026-06-21

---
<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (par [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**Utilisez ce cas pour tester GLM-5.2 sur une recréation web pilotée par référence, où un prompt plus une URL source ont reproduit un site avec une fidélité presque pixel-perfect.**

Open Design indique avoir testé GLM-5.2 dans son AMR intégré avec seulement une URL de référence et un prompt simple, et le modèle a recréé le site presque parfaitement dans la démo. Considérez cela comme une preuve pratique de génération d’UI fondée sur des références, pas comme un benchmark complet.

Type: Démo | Date: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (par [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilisez ce cas pour comparer GLM-5.2 sur des builds UI full-stack, où il s’est rapproché du résultat Trader Desk le plus soigné tout en ne coûtant qu’une petite fraction du meilleur résultat.**

Atomic Chat a comparé quatre modèles sur le même prompt live Trader Desk avec frontend, backend, données de marché sur huit symboles et UI dark theme personnalisée. Le post rapporte GLM-5.2 à 13,677 tokens et $0.03, contre Fugu Ultra à 22,225 tokens et $0.51, et indique que GLM a produit une interface multi-panneaux tout aussi complète avec données en direct pour un coût bien plus faible.

Type: Évaluation | Date: 2026-06-22

---

<a id="provider-tool-integrations"></a>
## 🔌 Intégrations fournisseurs et outils

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (par [@opencode](https://x.com/opencode))

**Utilisez ce cas pour suivre la disponibilité de GLM-5.2 dans les workflows OpenCode Go avec du texte, un contexte 1M et une tarification de type GLM-5.1.**

OpenCode a annoncé la disponibilité de GLM-5.2 dans Go, mettant en évidence la prise en charge du texte, une fenêtre contextuelle de 1 million et le même prix que la version 5.1.

Type: Intégration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (par [@ollama](https://x.com/ollama))

**Utilisez ce cas pour acheminer GLM-5.2 vers Ollama Cloud pour des expériences de modèle de codage open source accessibles.**

Ollama a annoncé la disponibilité du GLM-5.2, le décrivant comme un modèle de codage et de tâches agentiques à long terme avec un contexte 1M.

Type: Intégration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (par [@OpenRouter](https://x.com/OpenRouter))

**Utilisez ce cas pour accéder à GLM-5.2 via OpenRouter lors de la comparaison du routage de fournisseur ou des piles multimodèles.**

OpenRouter a annoncé la disponibilité du GLM-5.2 en tant que modèle à long terme de 1 million de jetons, offrant aux utilisateurs un chemin indépendant du fournisseur pour l'appeler.

Type: Intégration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (par [@vllm_project](https://x.com/vllm_project))

**Utilisez ce cas pour auto-héberger ou servir GLM-5.2 via vLLM avec une prise en charge jour zéro.**

Le projet vLLM a annoncé la prise en charge de GLM-5.2 dans la version 0.23.0, le présentant comme un modèle phare pour les agents de codage à long horizon avec un contexte 1M.

Type: Intégration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (par [@NotionHQ](https://x.com/NotionHQ))

**Utilisez ce cas pour identifier GLM-5.2 en tant que modèle à poids ouvert disponible dans les flux de travail Notion.**

Notion a annoncé la disponibilité du GLM-5.2 en tant que modèle ouvert conçu pour les tâches à long terme et servi via Baseten.

Type: Intégration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (par [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilisez ce cas pour évaluer Fireworks en tant que route de diffusion pour les charges de travail GLM-5.2 nécessitant une infrastructure hébergée.**

Fireworks a annoncé GLM-5.2 en direct le jour zéro, en mettant l'accent sur le contexte 1M, le positionnement axé sur le codage et la validation indépendante sur SWE-Bench, Terminal-Bench, GPQA et AIME.

Type: Intégration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Lien vers le jardin modèle Google Cloud](https://x.com/CarolGLMs/status/2067127223216419088) (par [@CarolGLMs](https://x.com/CarolGLMs))

**Utilisez ce cas pour trouver GLM-5.2 dans des contextes de déploiement orientés Google Cloud et de plate-forme d'agent.**

CarolGLMs a partagé un lien Google Cloud pour GLM-5.2, ce qui en fait un pointeur direct pour les équipes travaillant via des catalogues de modèles cloud.

Type: Intégration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (par [@AskVenice](https://x.com/AskVenice))

**Utilisez ce cas lorsque le mode de confidentialité, TEE ou le chiffrement de bout en bout est un facteur décisif pour essayer GLM-5.2.**

Venice a annoncé la disponibilité du GLM-5.2 en mode confidentialité avec le cadrage TEE/E2EE, destiné au codage agent privé et aux tâches à long terme.

Type: Intégration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (par [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilisez ce cas pour essayer GLM-5.2 dans Command Code avec un plan d’entrée à faible coût et des fonctionnalités de codage à contexte long.**

Command Code a annoncé la disponibilité du GLM-5.2, en notant le contexte 1M, un raisonnement solide, le statut open source et l'accès via son plan Go à un dollar.

Type: Intégration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Agent Hermès du portail Nous](https://x.com/Teknium/status/2066954081575592282) (par [@Teknium](https://x.com/Teknium))

**Utilisez ce cas pour connecter GLM-5.2 aux flux de travail Hermes Agent via Nous Portal et OpenRouter.**

Teknium a signalé la disponibilité de GLM-5.2 dans Hermes Agent de Nous Portal et OpenRouter, utile pour les expériences de routage de framework d'agent.

Type: Intégration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (par [@ionet](https://x.com/ionet))

**Utilisez ce cas lors de l'évaluation de la diffusion basée sur le calcul pour un modèle à contexte long avec paramètres 753 B.**

io.net s'est annoncé comme partenaire de lancement dès le premier jour pour GLM-5.2, mettant l'accent sur le contexte 1M, la conception axée sur l'agent, le codage à long horizon et les besoins de calcul d'un modèle à paramètres 753B.

Type: Intégration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (par [@clattner_llvm](https://x.com/clattner_llvm))

**Utilisez ce cas pour envisager Modular Cloud pour le service GLM-5.2 à contexte long à l'échelle du fournisseur.**

Chris Lattner a publié que GLM-5.2 était en ligne sur Modular Cloud le jour zéro, mettant en évidence les pondérations ouvertes, le codage, les agents à long horizon et le contexte 1M.

Type: Intégration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (par [@agentnative_](https://x.com/agentnative_))

**Utilisez ce cas pour configurer GLM-5.2 dans Cursor via OpenRouter pour un flux de travail de codage en modèle ouvert à faible coût.**

La source donne un chemin de configuration concret du Cursor/OpenRouter plutôt que d'annoncer uniquement la disponibilité du modèle.

Type: Tutoriel | Date: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (par [@beyang](https://x.com/beyang))

**Utilisez ce cas pour associer GLM-5.2 aux agents personnalisés Amp lorsqu'un modèle texte uniquement nécessite la prise en charge de la révision visuelle pour les tâches de conception.**

L'article connecte un résultat de référence de conception visuelle GLM-5.2 avec des agents de plug-in Amp qui peuvent fournir une couche de révision.

Type: Intégration | Date: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (par [@alphatozeta8148](https://x.com/alphatozeta8148))

**Utilisez ce cas pour acheminer GLM-5.2 via Baseten lorsque la vitesse de diffusion dans un contexte long est importante pour Factory Droid, OpenCode et les faisceaux de codage.**

La source rapporte que GLM-5.2 fonctionne quatre fois plus rapidement dans un contexte 1M complet et le montre dans les faisceaux de codage.

Type: Intégration | Date: 2026-06-20

---

<a id="case-74"></a>
### Case 74: [Browser Use QA Subagents For Web Design](https://x.com/browser_use/status/2068405699340853541) (par [@browser_use](https://x.com/browser_use))

**Utilisez ce cas pour associer GLM-5.2 à des sous-agents QA multimodaux Browser Use v2 lorsqu’un modèle purement textuel a besoin d’inspection visuelle et de corrections itératives de site web.**

Browser Use rapporte que GLM-5.2 a battu Fable 5 sur une tâche de design de site web, puis que des sous-agents QA ont été ajoutés pour inspecter le résultat, juger l’esthétique, trouver des bugs et renvoyer des correctifs ciblés à GLM. La boucle complète build plus QA aurait coûté moins de 0,75 dollar.

Type: Intégration | Date: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [ZCode Official IDE Daily Free Tokens](https://x.com/Alan_Earn/status/2068223665268006924) (par [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan))

**Utilisez ce cas pour accéder à GLM-5.2 via ZCode si vous voulez un IDE de code officiel gratuit avec de grands quotas quotidiens de tokens et un workflow proche de Cursor.**

Le post décrit ZCode comme l’IDE de code officiel de Zhipu, avec GLM-5.2 comme modèle par défaut, 3 M de tokens quotidiens, 1 M de contexte et des clients Mac et Windows. Il inclut aussi un court flux d’installation, ce qui le rend plus exploitable qu’une simple annonce de lancement.

Type: Tutoriel | Date: 2026-06-20

---



<a id="case-83"></a>
### Case 83: [Cursor Setup Through Fireworks](https://x.com/skirano/status/2068777440986513647) (par [@skirano](https://x.com/skirano))

**Utilisez ce cas pour brancher GLM-5.2 dans Cursor via Fireworks avec une configuration minimale compatible OpenAI et sans code client personnalisé.**

Skirano montre un flux minimal d’installation de Cursor : coller une clé Fireworks dans le champ OpenAI API key, utiliser `https://api.fireworks.ai/inference/v1` comme base URL, sélectionner `accounts/fireworks/models/glm-5p2`, puis redémarrer Cursor. Cela en fait une route concrète pour essayer GLM-5.2 dans un IDE de code familier.

Type: Tutoriel | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [VulcanBench ZAI Provider Support](https://x.com/vulcanbench/status/2068724843856707676) (par [@vulcanbench](https://x.com/vulcanbench))

**Utilisez ce cas pour exécuter GLM-5.2 dans un harness de benchmark ouvert avec un support fournisseur ZAI de premier ordre et un chemin de clé API dédié.**

VulcanBench v0.2.0 a ajouté un support ZAI de premier ordre, permettant d’exécuter GLM-5.2 comme `zai:glm-5.2` aux côtés de modèles OpenAI et Anthropic avec une clé dédiée `ZAI_API_KEY`. C’est utile pour ceux qui veulent un harness de benchmark ouvert plutôt que des captures ponctuelles.

Type: Intégration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [OpenCode High/Max Reasoning Variants](https://x.com/OpenCodeLog/status/2068487086576156705) (par [@OpenCodeLog](https://x.com/OpenCodeLog))

**Utilisez ce cas pour accéder aux variantes de raisonnement High et Max de GLM-5.2 dans OpenCode tout en profitant d’une gestion plus fiable des limites d’étapes.**

OpenCode v1.17.9 a ajouté les variantes de réflexion High et Max pour GLM-5.2 auprès des fournisseurs compatibles OpenAI et Anthropic, ainsi qu’un mapping natif de l’effort OpenRouter. La même version corrige aussi le comportement des limites d’étapes des agents, ce qui rend l’intégration plus pratique pour des runs plus longs.

Type: Intégration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Z.ai Coding Endpoint Selection](https://x.com/ivanfioravanti/status/2068574700721082400) (par [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour orienter le trafic de plan de code GLM-5.2 vers l’endpoint Z.ai optimisé pour le code plutôt que vers le chemin API générique.**

Le post oriente les utilisateurs vers `https://api.z.ai/api/coding/paas/v4` au lieu de l’endpoint général `https://api.z.ai/api/paas/v4/` pour les workloads de coding plan, et note que `https://api.z.ai/api/anthropic` est ce qu’utilisent généralement des outils comme Claude Code et OpenCode quand c’est pris en charge. Traitez cela comme un correctif de configuration concret quand GLM-5.2 semble mal routé.

Type: Tutoriel | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [ZenMux Free GLM-5.2 API Setup](https://x.com/0x_kaize/status/2068676992782811607) (par [@0x_kaize](https://x.com/0x_kaize))

**Utilisez ce cas pour obtenir gratuitement une clé API et une base URL GLM-5.2, puis l’intégrer dans Claude, Cursor, Hermes et des outils similaires.**

L’auteur partage un flux d’installation de cinq minutes pour obtenir gratuitement une clé API ZenMux et une base URL, puis brancher GLM-5.2 dans Claude, Cursor, Hermes et des outils similaires. Le post note aussi que le tier gratuit atteint vite ses limites de débit, ce qui en fait davantage une note d’accès qu’une garantie de durabilité.

Type: Tutoriel | Date: 2026-06-21

---
<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (par [@_xjdr](https://x.com/_xjdr))

**Utilisez ce cas pour acheminer GLM-5.2 vers des environnements d’agents type ncode et Noumena avec des endpoints standard et 1M contexte séparés, plus un support de modèle par défaut.**

La mise à jour Noumena indique que l’équipe a ajouté un support GLM de première classe pour le tool calling, le parsing de fonctions, le routage d’apps et les traces de raisonnement, puis a séparé l’API en endpoints `glm-5.2` et `glm-5.2[1m]` afin de contrôler le TTFT sous forte charge 1M contexte. Elle précise aussi que les nouvelles builds ncode ont remplacé Kimi par GLM comme modèle opus-class par défaut après des retours d’usage positifs.

Type: Intégration | Date: 2026-06-22

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (par [@thealexker](https://x.com/thealexker))

**Utilisez ce cas pour exécuter GLM-5.2 dans Claude Code via une clé Baseten, une base URL personnalisée et un remapping de modèle dans `~/.claude/settings.json`.**

Le tutoriel explique comment installer Claude Code, créer un compte Baseten, récupérer une API key et modifier `~/.claude/settings.json` afin que les trois niveaux de modèles Claude pointent vers `zai-org/GLM-5.2` via des variables d’environnement Anthropic personnalisées. C’est un schéma de configuration drop-in concret pour utiliser GLM-5.2 dans le client Claude Code.

Type: Tutoriel | Date: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (par [@cramforce](https://x.com/cramforce))

**Utilisez ce cas pour tester GLM-5.2 dans un harness de sécurité, où `deepsec` en a fait le modèle par défaut pour Pi agent et a rapporté des résultats d’évaluation compétitifs.**

Le post annonce le support `deepsec` pour le Pi agent de `@badlogicgames` avec GLM-5.2 comme modèle par défaut et fournit une commande exécutable, `pnpm deepsec process --agent pi`. Il indique aussi que l’auteur a exécuté les évaluations Deepsec et trouvé le résultat compétitif face à d’autres modèles frontier, ce qui en fait une surface d’intégration concrète orientée sécurité.

Type: Intégration | Date: 2026-06-22

---

<a id="cost-pricing-local-deployment"></a>
## 💸 Coût, prix et déploiement local

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (par [@Hesamation](https://x.com/Hesamation))

**Utilisez ce cas pour comparer l'économie des jetons de sortie GLM-5.2 avec les modèles de style Opus, Fable et GPT-5.5.**

L'article compare les prix des jetons de sortie de 1 million et affirme que le GLM-5.2 peut être nettement moins cher que les modèles à frontières fermées. Traitez les chiffres comme une comparaison de prix liée à la source qui doit être revérifiée avant la budgétisation.

Type: Évaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (par [@Jeyffre](https://x.com/Jeyffre))

**Utilisez ce cas pour déterminer si les modèles de type GLM-5.2 auto-hébergés peuvent rembourser les coûts matériels pour les gros utilisateurs d’agents.**

L'auteur estime que plusieurs machines de classe DGX Spark pourraient exécuter un modèle de classe 700B et compare un achat de matériel d'environ 20 000 $ aux dépenses mensuelles élevées d'API pour le codage et les charges de travail des agents.

Type: Évaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (par [@pcuenq](https://x.com/pcuenq))

**Utilisez ce cas pour explorer les exécutions locales de GLM-5.2 sur du matériel Apple et des configurations orientées MLX.**

Le message indique que GLM-5.2 venait de sortir et fonctionnait déjà avec MLX sur deux machines Mac Studio M3 Ultra, le présentant comme comparable aux modèles fermés récents avec des poids ouverts.

Type: Démo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (par [@ai_xiaomu](https://x.com/ai_xiaomu))

**Utilisez ce cas comme invite de comparaison des coûts pour vérifier les hypothèses de déploiement local avant de choisir entre l'abonnement et l'auto-hébergement.**

La publication chinoise compare les numéros SWE-Bench revendiqués, l'utilisation commerciale open source et le coût estimé du déploiement local d'un seul H100 par rapport à un abonnement Claude Pro. Les chiffres devraient être revalidés pour les prix actuels des infrastructures.

Type: Évaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (par [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilisez ce cas pour inspecter le récit du crédit gratuit et de l'agent de remplacement autour de GLM-5.2, tout en séparant les allégations marketing de l'adéquation vérifiée à la charge de travail.**

Le message présente GLM-5.2 comme un concurrent Claude moins coûteux avec des crédits quotidiens, un contrôle open source, un auto-hébergement et une valeur plus élevée pour les longues sessions de codage.

Type: Évaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (par [@0xSero](https://x.com/0xSero))

**Utilisez ce cas pour tester GLM-5.2 via une allocation ZCode gratuite avant de vous engager auprès d'un fournisseur payant ou d'un déploiement local.**

L'auteur décrit la disponibilité de GLM-5.2 via ZCode avec une allocation quotidienne importante de jetons gratuits et note une utilisation possible pour la configuration de vLLM Studio ou un hébergement local.

Type: Intégration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (par [@JZiyue_](https://x.com/JZiyue_))

**Utilisez ce cas pour trouver des fenêtres d'accès gratuit limitées dans le temps pour les tests GLM-5.2.**

La publication annonce GLM-5.2 en direct sur ZenMux avec une fenêtre gratuite d'une semaine, un contexte 1M, des améliorations de codage et d'agent et un positionnement au même prix que 5.1.

Type: Intégration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [Prix ​​par jeton crofAI](https://x.com/nahcrof/status/2067166596523765781) (par [@nahcrof](https://x.com/nahcrof))

**Utilisez ce cas pour comparer les tarifs des fournisseurs tiers pour GLM-5.2 avant de sélectionner un itinéraire.**

Le message annonce GLM-5.2 sur crofAI avec des prix d'entrée, de sortie et de cache répertoriés, le positionnant comme une intelligence de frontière bon marché.

Type: Intégration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (par [@scaling01](https://x.com/scaling01))

**Utilisez ce cas comme critique des prix du marché lorsque vous comparez le GLM-5.2 à d’autres laboratoires pionniers et modèles ouverts.**

L'auteur compare GLM-5.2 et d'autres grands modèles ouverts sur la tarification des jetons de sortie et utilise la comparaison pour affirmer que les marges de certaines API Frontier-lab sont élevées.

Type: Évaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://x.com/volatilemrkts/status/2068077319986516031) (par [@volatilemrkts](https://x.com/volatilemrkts))

**Utilisez ce cas pour estimer le débit d’inférence GLM-5.2 local sur du matériel Apple à grande mémoire avant de planifier une configuration de codage hors ligne.**

La source rapporte 44,1 jetons par seconde sur une configuration Mac locale à haute mémoire et mentionne des problèmes de répétition de décodage avec des appels d'outils lourds.

Type: Démo | Date: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (par [@mrblock](https://x.com/mrblock))

**Utilisez ce cas pour évaluer les chemins de déploiement quantifiés GLM-5.2 lorsque les poids complets du modèle sont trop importants pour le matériel local ordinaire.**

L'article décrit les options GGUF dynamiques 2 bits et 1 bit d'Unsloth, les réductions de mémoire et les itinéraires de déploiement llama.cpp ou Unsloth Studio.

Type: Tutoriel | Date: 2026-06-20

---



<a id="case-88"></a>
### Case 88: [Two M3 Ultra MLX Distributed Run](https://x.com/ivanfioravanti/status/2068781499206574576) (par [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilisez ce cas pour estimer à quoi ressemble le serving 8-bit de GLM-5.2 sur deux machines M3 Ultra avant de construire un setup Apple Silicon plus vaste.**

Le post montre GLM-5.2 8-bit tournant avec MLX distributed sur deux machines M3 Ultra 512GB à environ 17,9 tokens par seconde et autour de 760 Go de mémoire. L’auteur précise aussi que le setup correspond à une PR préliminaire encore en cours, donc il faut le lire comme un signal de déploiement plutôt qu’un guide finalisé.

Type: Démo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [ZCode Multiplier Cut Through September](https://x.com/buildwithhassan/status/2068534544177791376) (par [@buildwithhassan](https://x.com/buildwithhassan))

**Utilisez ce cas pour étirer les crédits de forfait GLM-5.2 avec des multiplicateurs ZCode plus faibles aux heures de pointe comme hors pointe.**

Le post dit que ZCode a abaissé les multiplicateurs du GLM coding plan de 3x à 2x aux heures de pointe et de 2x à 0,67x hors pointe, avec une fenêtre courant jusqu’à la fin septembre. Cela en fait une note d’accès et de prix concrète pour ceux qui veulent étirer leurs crédits sur GLM-5.2.

Type: Intégration | Date: 2026-06-21

---
<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (par [@CardilloSamuel](https://x.com/CardilloSamuel))

**Utilisez ce cas pour dimensionner une station locale haut de gamme GLM-5.2, où un desktop à deux Blackwell a maintenu une vitesse de décodage à deux chiffres sur une build quantifiée en 4 bits.**

CardilloSamuel rapporte avoir exécuté GLM-5.2 UD-Q4_K_XL sur 2x RTX PRO 6000 Blackwells avec un Threadripper PRO 9995WX et 1TB de DDR5. Le post cite environ 64 tok/s en prefill, 13-15 tok/s en decode, un score Aider Polyglot de 69.7% à moins de deux points du BF16, et note que la bande passante de la RAM système était le goulot d’étranglement, en laissant une 5090 non assortie hors du partage.

Type: Démo | Date: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (par [@karminski3](https://x.com/karminski3))

**Utilisez ce cas pour vérifier si l’achat d’un Mac Studio a du sens pour l’inférence locale GLM-5.2, car les calculs de retour sur investissement publiés favorisent nettement l’accès API ou plan pour la plupart des utilisateurs.**

Le post estime qu’un Mac Studio à RMB 32,999 équivaut à environ 1,178 millions de tokens API GLM-5.2 aux tarifs cités, et soutient que la période de retour est d’environ 209 jours même pour une configuration Qwen bien plus petite. Il ajoute qu’un Mac Studio 512GB exécutant GLM-5.2 quantifié autour de 17 tok/s pourrait mettre environ sept ans à s’amortir, donc la possession locale n’a de sens que si vous possédez déjà le matériel ou pouvez exploiter du temps inutilisé.

Type: Évaluation | Date: 2026-06-22

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 Limites, avertissements et signaux de sécurité

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (par [@sawyerhood](https://x.com/sawyerhood))

**Utilisez ce cas pour vous rappeler que GLM-5.2 peut être moins utile pour les flux de travail nécessitant une capacité de vision native.**

L'auteur note que les modèles GLM manquant de vision réduisent leur utilité, citant un article de classement de Design Arena. Il s’agit d’une mise en garde pratique pour la planification de produits multimodaux.

Type: Limite | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [Mise en garde sur les écarts d'agents dans le monde réel](https://x.com/ml_angelopoulos/status/2067013545431269405) (par [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**Utilisez ce cas pour éviter de surlire les résultats des tests comme preuve que GLM-5.2 correspond aux meilleurs modèles propriétaires sur toutes les tâches agentiques déployées.**

L'auteur dit que GLM-5.2 est impressionnant mais pas encore proche des performances de niveau réflexion de Fable ou Opus 4.8 sur la répartition générale des tâches agentiques du monde réel, basées sur une méthodologie Agent Arena.

Type: Limite | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (par [@VittoStack](https://x.com/VittoStack))

**Utilisez ce cas comme rappel pour exécuter des évaluations de sécurité avant de déployer GLM-5.2 dans des domaines sensibles.**

Le message fait état d’un échec de refus de contenu préjudiciable lors d’un test de sécurité comparatif. Le référentiel enregistre uniquement le signal de sécurité, pas les détails dangereux, et traite cela comme une mise en garde concernant les risques de déploiement.

Type: Limite | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [Critique de la méthodologie de référence](https://x.com/josepha_mayo/status/2066951013337112661) (par [@josepha_mayo](https://x.com/josepha_mayo))

**Utilisez ce cas pour remettre en question la méthodologie de référence même lorsque le résultat global favorise GLM-5.2.**

L'auteur critique la méthodologie Design Arena tout en reconnaissant la force du GLM-5.2, ce qui le rend utile pour les lecteurs qui souhaitent un scepticisme de référence parallèlement aux affirmations du classement.

Type: Limite | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (par [@k_matsumaru](https://x.com/k_matsumaru))

**Utilisez ce cas pour tester la latence du fournisseur avant de changer de plan de codage ou de router les flux de travail de style Claude Code vers GLM-5.2.**

La publication japonaise envisage d'utiliser GLM-5.2 dans un plan de codage, mais note des préoccupations antérieures concernant la latence de réponse aux heures de pointe.

Type: Limite | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (par [@nikhilchandak29](https://x.com/nikhilchandak29))

**Utilisez ce cas pour vérifier si les gains de codage se généralisent aux domaines non codants avant un déploiement à grande échelle.**

L'article rapporte que GLM-5.2 n'est pas meilleur que GLM-5.1 sur FutureSim et utilise le résultat pour avertir que les améliorations du codage pourraient ne pas se généraliser de manière égale dans tous les domaines.

Type: Limite | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (par [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour séparer la fonctionnalité du modèle de l'exécution du lancement, de la documentation et de la préparation de l'API.**

Le message qualifie la version anticipée de compliquée car les benchmarks et l'accès aux API n'étaient pas encore disponibles à l'époque, ce qui la rend pertinente pour l'examen de la préparation au lancement plutôt que pour le jugement de la qualité du modèle.

Type: Limite | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [Augmentation du prix du plan de codage](https://x.com/bridgemindai/status/2065799843658793092) (par [@bridgemindai](https://x.com/bridgemindai))

**Utilisez ce cas pour vérifier le prix du forfait avant de recommander GLM-5.2 comme remplacement à faible coût.**

L'auteur déclare payer 65 $ par mois pour un forfait GLM Coding Pro et affirme que le forfait a presque doublé depuis son dernier abonnement. Utilisez-le comme rappel pour vérifier les prix actuels.

Type: Limite | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [Travail parallèle court et exécutions longues d'agents](https://x.com/thekuchh/status/2068010332501479865) (par [@thekuchh](https://x.com/thekuchh))

**Utilisez ce cas pour acheminer GLM-5.2 vers des tâches de codage à courte portée tout en réservant des modèles plus puissants pour des exécutions d'agent plus approfondies sur plusieurs heures.**

Le message fait état d'une division pratique : GLM-5.2 fonctionne bien pour de courtes tâches parallèles mais dérive sur une exécution d'agent plus longue.

Type: Limite | Date: 2026-06-20

---

<a id="case-73"></a>
### Case 73: [Code Censorship And Bias Check](https://x.com/wongmjane/status/2068424945663893936) (par [@wongmjane](https://x.com/wongmjane))

**Utilisez ce cas comme signal pratique de sécurité pour les tests de code et de biais politiques, et non comme preuve que les questions d’alignement plus larges sont déjà réglées.**

L’autrice affirme que GLM-5.2 n’a pas injecté de censure politique chinoise dans du code et qu’il a séparément corrigé une fausse affirmation de biais pro-américain à propos de la guerre du Vietnam, tout en laissant inchangés des cas plus proches de l’opinion. Cela en fait un exemple public concret pour tester des comportements de factualité et de code sur des sujets politiquement sensibles.

Type: Limite | Date: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [Hard Reasoning Billing Failure](https://x.com/s_batzoglou/status/2068297051247350154) (par [@s_batzoglou](https://x.com/s_batzoglou))

**Utilisez ce cas pour tester GLM-5.2 avec prudence sur des charges de raisonnement difficiles, car le rapport public montre de longs temps d’exécution, peu de complétions et une sortie facturée étonnamment élevée.**

L’auteur a lancé 11 problèmes d’induction et rapporte seulement quatre complétions, deux bonnes réponses, des temps d’exécution de plusieurs heures et des frais semblant très supérieurs au nombre de tokens visibles. C’est un avertissement concret sur l’efficacité du raisonnement et le comportement de facturation, pas seulement sur un score de benchmark.

Type: Limite | Date: 2026-06-20

---


<a id="acknowledge"></a>
## 🙏 Remerciements

Ce référentiel a été inspiré par des créateurs publics, des développeurs, des équipes de référence, des fournisseurs et des communautés qui ont partagé de véritables preuves d'utilisation de GLM-5.2.

Merci aux créateurs et sources à fort signal représentés ici : [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn).

*If any attribution needs to be corrected, please contact us and we will update it.*

Contributions with concrete GLM-5.2 use cases are welcome through issues and pull requests.

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
