<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases"><img src="images/en.jpg" alt="Repositorio de casos de uso de GLM-5.2 banner" width="760"></a>

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

# Repositorio de casos de uso de GLM-5.2

## 🍌 Introducción

Bienvenido al repositorio de casos de uso de alta señal de GLM-5.2.

**Recopilamos casos reales, tutoriales, integraciones, evaluaciones, señales de precio y limitaciones de GLM-5.2 a partir de demos públicas y comunidades de creadores.**

Este README localizado mantiene casos con flujos concretos, evidencia pública de benchmarks, demos prácticas, integraciones, costes o advertencias útiles.

Cada título de caso enlaza a su fuente pública y cada usuario enlaza al perfil del creador.

[Probar GLM-5.2 en Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases)

## 📊 Resumen

- **109 casos seleccionados de GLM-5.2** de creadores públicos, equipos de benchmarks, desarrolladores de herramientas, proveedores y usuarios prácticos.
- Cubre evaluaciones comparativas y evaluación de frontera, agentes de código y flujos de contexto largo, demos prácticas y muestras, integraciones de proveedores y herramientas, coste, precios y despliegue local, límites, advertencias y señales de seguridad.
- Cada caso incluye la fuente original, la atribución del creador, un takeaway de uso conciso, el tipo de evidencia y la fecha de publicación.
- Usa este repo para encontrar flujos prácticos, comparar fortalezas y límites, descubrir rutas de proveedor y seguir experimentos reales.

> [!NOTE]
> La colección prioriza evidencia concreta sobre hype: demos publicadas, métodos de benchmark, notas de integración, datos de coste y caveats claros.

> [!NOTE]
> Los README localizados conservan el mismo orden de casos, enlaces, anchors y atribución que la fuente inglesa. Algunos títulos se mantienen cerca del idioma original para mejorar la trazabilidad.

<a id="-quick-api-access"></a>
## ⚡ Acceso rápido a la API

Usa GLM-5.2 mediante la API Chat Completions compatible con OpenAI de Evolink. Obtén una API key en [Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases) y configúrala como `EVOLINK_API_KEY` antes de ejecutar la solicitud.

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

Lee la referencia completa de la API GLM-5.2: [Abrir documentación de la API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api).

## 📑 Menú

| Sección | Casos |
|---|---|
| [📏 Evaluaciones comparativas y evaluación de frontera](#benchmarks-frontier-evaluation) | Caso 1-12, 60, 70, 72, 76, 90, 94 |
| [💻 Agentes de código y flujos de contexto largo](#coding-agents-long-context-workflows) | Caso 13-22, 62, 65, 66, 77, 80, 91, 102 |
| [🎮 Demos prácticas y muestras](#hands-on-demos-showcase-builds) | Caso 23-30, 71, 78, 81-82, 92, 99-100 |
| [🔌 Integraciones de proveedores y herramientas](#provider-tool-integrations) | Caso 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109 |
| [💸 Coste, precios y despliegue local](#cost-pricing-local-deployment) | Caso 43-51, 64, 68, 88-89, 97-98, 106-107 |
| [🧭 Límites, advertencias y señales de seguridad](#limits-caveats-safety-signals) | Caso 52-59, 67, 73, 75, 103, 108 |
| [🙏 Agradecimientos](#acknowledge) | Créditos y política de correcciones |

### [📏 Evaluaciones comparativas y evaluación de frontera](#benchmarks-frontier-evaluation)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Artificial Analysis Intelligence Index](#case-1) | Utilice la publicación de Análisis artificial para comparar GLM-5.2 con otros modelos de frontera patentados y de peso abierto en materia de inteligencia y costo por tarea. | Referencia |
| [Code Arena Frontend Ranking](#case-2) | Utilice este caso para evaluar GLM-5.2 en tareas reales de codificación front-end juzgadas mediante comparaciones de estilo arena. | Referencia |
| [Design Arena First Place](#case-3) | Utilice este caso para juzgar si GLM-5.2 puede manejar tareas de diseño más código en lugar de solo pruebas comparativas de codificación con mucho texto. | Referencia |
| [FrontierSWE Result](#case-4) | Utilice la publicación de FrontierSWE para comparar GLM-5.2 con los modelos GPT-5.5, Opus y Fable en tareas de ingeniería de software. | Referencia |
| [DeepSWE Open-Source Lead](#case-5) | Utilice el caso de DeepSWE para comprender GLM-5.2 como un modelo abierto sólido para tareas difíciles de evaluación de ingeniería de software. | Referencia |
| [Terminal-Bench Over 80 Percent](#case-6) | Utilice este caso al evaluar GLM-5.2 para flujos de trabajo de agentes y codificación orientados a terminales. | Referencia |
| [Comparación de SWELancer con GPT-5.5](#case-7) | Utilice este caso de SWELancer como una comparación multimétrica concreta entre GLM-5.2 y GPT-5.5 sobre el éxito de la tarea, la recompensa y el tiempo de finalización. | Evaluación |
| [BridgeBench Perfect Score Signal](#case-8) | Utilice este caso para inspeccionar GLM-5.2 sobre un razonamiento fundamentado de varios pasos en lugar de solo codificar tablas de clasificación. | Referencia |
| [BridgeBench Reasoning Number One](#case-9) | Utilice este caso para comparar GLM-5.2 con modelos de frontera cerrada en tareas de razonamiento fundamentado. | Referencia |
| [KernelBench-Hard Without Shortcutting](#case-10) | Utilice este caso para comprobar si las ganancias de referencia provienen de un comportamiento de implementación válido en lugar de atajos. | Evaluación |
| [Runescape Bench Catch-Up](#case-11) | Utilice este caso como una señal rápida para el progreso del modelo de peso abierto en tareas de referencia similares a las de un juego. | Referencia |
| [BridgeBench Speed Improvement](#case-12) | Utilice este caso para evaluar flujos de trabajo sensibles a la latencia donde la velocidad importa junto con la inteligencia. | Referencia |
| [Codificación KernelBench Hard y Mega GPU](#case-60) | Utilice este caso para evaluar GLM-5.2 en la codificación del kernel de GPU en KernelBench-Hard y KernelBench-Mega, donde los rastros de agentes abiertos hacen que el resultado sea inspeccionable. | Referencia |
| [Liderazgo open-source en DeepSWE con esfuerzo máximo](#case-70) | Usa este caso para seguir a GLM-5.2 en DeepSWE con esfuerzo máximo, donde la tabla publicada lo sitúa primero entre los modelos abiertos con una puntuación pass@1 del 44%. | Referencia |
| [Segundo puesto en benchmark de debates LLM](#case-72) | Usa este caso para evaluar GLM-5.2 más allá del código en debates adversariales de varios turnos, donde la variante de razonamiento máximo quedó segunda detrás de modelos Claude. | Referencia |
| [Tasa de alucinación en AA-Omniscience](#case-76) | Usa este caso para comparar GLM-5.2 en manejo de incertidumbre, donde el resultado publicado de AA-Omniscience muestra una tasa de alucinación menor que la de varios otros modelos frontier. | Evaluación |
| [Case 90: GDPval-AA Agentic Work Index](#case-90) | Usa este caso para comparar GLM-5.2 en trabajo de conocimiento de largo horizonte, en lugar de limitarte a rankings centrados solo en código. | Evaluación |
| [Case 94: Game Dev Arena Runner-Up](#case-94) | Usa este caso para juzgar la calidad de GLM-5.2 en creación de juegos, donde el modelo alcanzó el segundo puesto en Game Dev Arena y se convirtió en el laboratorio open-weight mejor clasificado en ese ranking. | Evaluación |

### [💻 Agentes de código y flujos de contexto largo](#coding-agents-long-context-workflows)

| Caso | Enfoque | Tipo |
|---|---|---|
| [One Hour Forty Two Minute Refactor Loop](#case-13) | Utilice este caso como patrón para una refactorización frontal autónoma prolongada con TDD, comentarios de los revisores y comprobaciones de regresión. | Demo |
| [OpenCode Bug Fix And Implementation Test](#case-14) | Utilice este caso para probar GLM-5.2 como agente de codificación OpenCode para corregir errores además de una pequeña tarea de implementación. | Demo |
| [OpenCode Retro Video Game Walkthrough](#case-15) | Utilice este tutorial para crear un juego pequeño con GLM-5.2 y OpenCode desde un solo mensaje y luego inspeccione cómo el modelo maneja los detalles de implementación. | Tutorial |
| [HTML5 Physics Simulations Contest](#case-16) | Utilice este caso para comparar el código GLM-5.2 y Kimi K2.7 en simulaciones de física HTML5 autónomas sin bibliotecas. | Evaluación |
| [Personal Site UI UX Build](#case-17) | Utilice este caso para solicitar a GLM-5.2 un sitio personal pulido e inspeccionar hasta qué punto múltiples turnos pueden mejorar la UI/UX. | Demo |
| [AI Contract Review Product Build](#case-18) | Utilice este caso para evaluar GLM-5.2 en una tarea de creación de productos con un PRD, presupuesto de tiempo, recuento de pasos, cuota de uso y comparación de calidad del código. | Evaluación |
| [ZCode Goal Feature For Larger Development Objectives](#case-19) | Utilice este caso para comprender cómo se integra GLM-5.2 en ZCode 3.0 para tareas de desarrollo agente más grandes. | Integración |
| [Envoltorio de Linux para ZCode creado con GLM-5.2](#case-20) | Utilice este caso como ejemplo de cómo GLM-5.2 ayuda con herramientas en entornos de agentes de codificación. | Demo |
| [Computer Use Skill Packaging](#case-21) | Utilice este caso para estudiar GLM-5.2 como ayuda para convertir un repositorio de uso de computadora de código abierto en una habilidad reutilizable. | Demo |
| [ZCode 3.0 Agentic Development Environment Review](#case-22) | Utilice este caso para evaluar GLM-5.2 dentro de un entorno de desarrollo agente completo en lugar de una única sesión de chat. | Demo |
| [Arnés OpenCode con servicio local](#case-62) | Utilice este caso para probar GLM-5.2 con el arnés OpenCode, el servicio local y los flujos de trabajo de codificación con muchas herramientas antes de compararlo con Claude Opus. | Evaluación |
| [Fast-RLM Long-Context Instruction Injection](#case-65) | Utilice este caso para mejorar el recuento de contexto largo de GLM-5.2 y el comportamiento del agente REPL moviendo instrucciones al indicador del sistema RLM. | Integración |
| [DeepAgents Code Open Harness Trial](#case-66) | Utilice este caso para probar GLM-5.2 con un arnés de agente de codificación abierto y compare el modelo bajo un shell de agente reproducible. | Demo |
| [Enrutamiento de stack de agentes de marketing en producción](#case-77) | Usa este caso para enrutar GLM-5.2 a workflows de agentes en producción que valoran estructura, velocidad y self-hosting, manteniendo modelos cerrados más fuertes para juicios ambiguos. | Evaluación |
| [Case 91: Cline Repo Bug Fix Showdown](#case-91) | Usa este caso para comparar GLM-5.2 y Opus 4.8 en la corrección de un bug de un repositorio real, donde GLM gastó más tokens pero entregó el parche final más barato y más limpio. | Evaluación |
| [Case 102: OpenInspect FP8 Background Agent](#case-102) | Usa este caso para estudiar un stack de agente en segundo plano autoalojado con GLM-5.2 en lugar de un flujo de chat alojado. | Integración |

### [🎮 Demos prácticas y muestras](#hands-on-demos-showcase-builds)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Playable Backrooms One-Shot](#case-23) | Utilice este caso para comparar el resultado, el tiempo de ejecución y el costo de creación de juegos con el mismo sistema entre GLM-5.2 y Opus 4.8. | Demo |
| [Tres construcciones reales con resultados mixtos](#case-24) | Utilice este caso como conjunto de demostración de advertencia: pruebe varias compilaciones reales antes de confiar en un modelo para tareas de producción de juegos o videos. | Evaluación |
| [Super Mario Clone In ZCode](#case-25) | Utilice este caso para evaluar la creación de juegos iterativos con GLM-5.2 y ZCode en varias pasadas de corrección y funciones. | Demo |
| [Lunar Lander Contest](#case-26) | Utilice este caso para comparar GLM-5.2, MiniMax M3 y Kimi K2.7 Code en una tarea de estilo de juego interactivo. | Evaluación |
| [One-Prompt Design Arena Creation](#case-27) | Utilice este caso para inspeccionar lo que GLM-5.2 puede generar a partir de un único mensaje de diseño en un contexto de arena. | Demo |
| [Trabajo de investigación: comprensión del flujo de trabajo](#case-28) | Utilice este caso para aplicar GLM-5.2 a flujos de trabajo de lectura de artículos con preguntas contextuales y referencias entre artículos. | Integración |
| [Constrained Poem Comparison](#case-29) | Utilice este caso para separar la corrección de la calidad creativa al comparar el GLM-5.2 con los modelos estilo Fable. | Evaluación |
| [Design Sense Example](#case-30) | Utilice este caso como una señal de diseño visual liviano y luego verifíquelo con su propio mensaje y revisión de la interfaz de usuario. | Demo |
| [Juego voxel estilo Temple Run en un solo intento](#case-71) | Usa este caso para poner a prueba GLM-5.2 en generación de juegos con un solo prompt y luego revisar qué sigue necesitando correcciones iterativas en una build visualmente rica. | Demo |
| [Conjunto de ejemplos one-shot en OpenCode Go](#case-78) | Usa este caso para medir GLM-5.2 en builds rápidas de un solo intento dentro de OpenCode Go antes de comprometerlo a loops de agentes más abiertos. | Demo |
| [Case 92: Open Design Reference URL Rebuild](#case-92) | Usa este caso para probar GLM-5.2 en recreación web guiada por referencias, donde un solo prompt más una URL de origen reprodujeron un sitio con fidelidad casi a nivel de píxel. | Demo |
| [Case 99: Trader Desk Cost-Quality Test](#case-99) | Usa este caso para comparar GLM-5.2 en builds full-stack de UI, donde se acercó al resultado de trading desk más pulido mientras costaba solo una pequeña fracción del mejor resultado. | Evaluación |
| [Case 100: Luddite Game After Claude Refusal](#case-100) | Usa este caso para prototipar conceptos de juego sensibles a políticas con GLM-5.2 cuando un modelo cerrado rechaza la solicitud, y luego inspeccionar por ti mismo el resultado jugable. | Demo |

### [🔌 Integraciones de proveedores y herramientas](#provider-tool-integrations)

| Caso | Enfoque | Tipo |
|---|---|---|
| [OpenCode Go Availability](#case-31) | Utilice este caso para realizar un seguimiento de la disponibilidad de GLM-5.2 dentro de los flujos de trabajo de OpenCode Go con texto, contexto de 1 millón y precios similares a GLM-5.1. | Integración |
| [Ollama Cloud Availability](#case-32) | Utilice este caso para enrutar GLM-5.2 a Ollama Cloud para realizar experimentos de modelos de codificación de código abierto accesibles. | Integración |
| [OpenRouter One API Call Access](#case-33) | Utilice este caso para acceder a GLM-5.2 a través de OpenRouter al comparar enrutamiento de proveedores o pilas multimodelo. | Integración |
| [vLLM Day-Zero Support](#case-34) | Utilice este caso para autohospedar o servir GLM-5.2 a través de vLLM con soporte de día cero. | Integración |
| [Notion Availability Via Baseten](#case-35) | Utilice este caso para identificar GLM-5.2 como un modelo de peso abierto disponible dentro de los flujos de trabajo de Notion. | Integración |
| [Fireworks Day-Zero Serving](#case-36) | Utilice este caso para evaluar Fireworks como ruta de servicio para cargas de trabajo GLM-5.2 que necesitan una infraestructura alojada. | Integración |
| [Enlace al jardín modelo de Google Cloud](#case-37) | Utilice este caso para encontrar GLM-5.2 en contextos de plataforma de agentes y de implementación orientados a Google Cloud. | Integración |
| [Venice Privacy Mode](#case-38) | Utilice este caso cuando el modo de privacidad, TEE o cifrado de extremo a extremo sea un factor decisivo al probar GLM-5.2. | Integración |
| [Command Code Availability](#case-39) | Utilice este caso para probar GLM-5.2 en Command Code con un plan inicial de bajo costo y funciones de codificación de contexto largo. | Integración |
| [Agente Hermes De Nous Portal](#case-40) | Utilice este caso para conectar GLM-5.2 a los flujos de trabajo del Agente Hermes a través de Nous Portal y OpenRouter. | Integración |
| [io.net Day-Zero Launch Partner](#case-41) | Utilice este caso al evaluar el servicio respaldado por computación para un modelo de contexto largo de parámetros 753B. | Integración |
| [Modular Cloud Day-Zero Serving](#case-42) | Utilice este caso para considerar Modular Cloud para el servicio GLM-5.2 de contexto prolongado a escala de proveedor. | Integración |
| [Cursor Setup Through OpenRouter](#case-61) | Utilice este caso para configurar GLM-5.2 en Cursor a través de OpenRouter para un flujo de trabajo de codificación de modelo abierto de bajo costo. | Tutorial |
| [Amp Agentic Eyes For Visual Design](#case-63) | Utilice este caso para emparejar GLM-5.2 con agentes personalizados de Amp cuando un modelo de solo texto necesite soporte de revisión visual para tareas de diseño. | Integración |
| [Baseten Faster One-Million-Context Serving](#case-69) | Utilice este caso para enrutar GLM-5.2 a través de Baseten cuando la velocidad de servicio de contexto largo sea importante para Factory Droid, OpenCode y arneses de codificación. | Integración |
| [Subagentes QA de Browser Use para diseño web](#case-74) | Usa este caso para combinar GLM-5.2 con subagentes multimodales de QA de Browser Use v2 cuando un modelo solo de texto necesita inspección visual y correcciones iterativas de sitios web. | Integración |
| [Tokens gratis diarios en el IDE oficial ZCode](#case-79) | Usa este caso para acceder a GLM-5.2 a través de ZCode cuando quieras un IDE oficial de programación gratuito con grandes asignaciones diarias de tokens y un flujo parecido a Cursor. | Tutorial |
| [Case 93: Noumena ncode GLM Default](#case-93) | Usa este caso para enrutar GLM-5.2 a entornos de agentes tipo ncode y Noumena con endpoints separados estándar y de contexto 1M, además de soporte como modelo por defecto. | Integración |
| [Case 95: Claude Code Through Baseten](#case-95) | Usa este caso para ejecutar GLM-5.2 dentro de Claude Code mediante una clave de Baseten, una base URL personalizada y remapeo de modelos en `~/.claude/settings.json`. | Tutorial |
| [Case 96: Deepsec Pi Agent Default](#case-96) | Usa este caso para probar GLM-5.2 en un harness de seguridad, donde `deepsec` lo convirtió en el modelo por defecto para Pi agent y reportó resultados competitivos en evaluaciones. | Integración |
| [Case 101: Baseten + Droid Harness Quickstart](#case-101) | Usa este caso para poner GLM-5.2 en marcha rápidamente mediante Baseten y el harness Droid, con un flujo corto de configuración que también puedes reutilizar en otros IDEs. | Tutorial |
| [Case 104: OpenAI-Compatible GLM API Workflow](#case-104) | Usa este caso para construir en Python un cliente GLM-5.2 compatible con OpenAI con control de razonamiento, tool calling, recuperación de contexto largo y seguimiento de costes. | Tutorial |
| [Case 105: Perplexity Agent API Search Sandbox](#case-105) | Usa este caso para conectar GLM-5.2 a la Agent API de Perplexity cuando quieras agentes en sandbox con búsqueda detrás de una sola llamada API. | Integración |
| [Case 109: Baseten 280 TPS GLM API](#case-109) | Usa este caso cuando importe la latencia del proveedor: Baseten afirma un serving de GLM-5.2 muy rápido con time-to-first-token subsegundo y alto throughput de decodificación. | Integración |

### [💸 Coste, precios y despliegue local](#cost-pricing-local-deployment)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Output Token Cost Comparison](#case-43) | Utilice este caso para comparar la economía del token de salida GLM-5.2 con los modelos estilo Opus, Fable y GPT-5.5. | Evaluación |
| [Local Near-Frontier Hardware ROI](#case-44) | Utilice este caso para razonar sobre si los modelos autohospedados tipo GLM-5.2 pueden compensar los costos de hardware para los usuarios intensivos de agentes. | Evaluación |
| [MLX On Two Mac Studios](#case-45) | Utilice este caso para explorar ejecuciones locales de GLM-5.2 en hardware de Apple y configuraciones orientadas a MLX. | Demo |
| [H100 Monthly Local Deployment Claim](#case-46) | Utilice este caso como indicador de comparación de costos para verificar los supuestos de implementación local antes de elegir entre suscripción y autohospedaje. | Evaluación |
| [Daily Credits And Claude Replacement Claim](#case-47) | Utilice este caso para inspeccionar la narrativa del crédito gratuito y del agente de reemplazo en torno a GLM-5.2, mientras separa las afirmaciones de marketing de la adecuación de la carga de trabajo verificada. | Evaluación |
| [Free ZCode Token Window](#case-48) | Utilice este caso para probar GLM-5.2 a través de una asignación gratuita de ZCode antes de comprometerse con un proveedor pago o una implementación local. | Integración |
| [ZenMux Free Week Offer](#case-49) | Utilice este caso para encontrar ventanas de acceso gratuito con límites de tiempo para las pruebas de GLM-5.2. | Integración |
| [Precios por token de crofAI](#case-50) | Utilice este caso para comparar los precios de proveedores externos para GLM-5.2 antes de seleccionar una ruta. | Integración |
| [API Price Margin Comparison](#case-51) | Utilice este caso como crítica de precios de mercado al comparar GLM-5.2 con otros laboratorios de vanguardia y modelos abiertos. | Evaluación |
| [Basement Local Inference Speed](#case-64) | Utilice este caso para estimar el rendimiento de inferencia local de GLM-5.2 en hardware Apple de gran memoria antes de planificar una configuración de codificación fuera de línea. | Demo |
| [Unsloth Quantized Local Deployment](#case-68) | Utilice este caso para evaluar las rutas de implementación cuantificadas de GLM-5.2 cuando los pesos del modelo completo sean demasiado grandes para el hardware local normal. | Tutorial |
| [Case 97: RTX PRO 6000 Local Throughput](#case-97) | Usa este caso para dimensionar una estación local de alta gama para GLM-5.2, donde un escritorio con dos Blackwell mantuvo velocidad de decodificación de dos dígitos en una build cuantizada a 4 bits. | Demo |
| [Case 98: Mac Studio API ROI Reality Check](#case-98) | Usa este caso para validar si tiene sentido comprar un Mac Studio para inferencia local de GLM-5.2, porque las cuentas de amortización publicadas favorecen claramente el acceso por API o plan para la mayoría de usuarios. | Evaluación |
| [Case 106: LiteLLM Local Outage Save](#case-106) | Usa este caso para mantener avanzando un entregable cuando las APIs frontier alojadas fallen o queden limitadas, redirigiendo el trabajo mediante un GLM-5.2 desplegado localmente con LiteLLM. | Demo |
| [Case 107: Individual Versus Team Local ROI](#case-107) | Usa este caso para decidir si un despliegue local de GLM-5.2 tiene sentido para una persona individual o más bien solo para un equipo de desarrollo más grande. | Evaluación |

### [🧭 Límites, advertencias y señales de seguridad](#limits-caveats-safety-signals)

| Caso | Enfoque | Tipo |
|---|---|---|
| [No Vision Caveat](#case-52) | Utilice este caso para recordar que GLM-5.2 puede ser menos útil para flujos de trabajo que requieren capacidad de visión nativa. | Límite |
| [Advertencia sobre la brecha de agentes en el mundo real](#case-53) | Utilice este caso para evitar una lectura excesiva de los resultados de los puntos de referencia como prueba de que GLM-5.2 coincide con los mejores modelos propietarios en todas las tareas agentes implementadas. | Límite |
| [Safety Guardrail Concern](#case-54) | Utilice este caso como recordatorio para realizar evaluaciones de seguridad antes de implementar GLM-5.2 en dominios confidenciales. | Límite |
| [Crítica de la metodología de referencia](#case-55) | Utilice este caso para cuestionar la metodología de referencia incluso cuando el resultado principal favorezca a GLM-5.2. | Límite |
| [Peak-Time Latency Concern](#case-56) | Utilice este caso para probar la latencia del proveedor antes de cambiar los planes de codificación o enrutar los flujos de trabajo estilo Claude Code a GLM-5.2. | Límite |
| [FutureSim Non-Improvement Result](#case-57) | Utilice este caso para comprobar si las ganancias de codificación se generalizan a dominios que no son de codificación antes de una implementación amplia. | Límite |
| [Launch Readiness Critique](#case-58) | Utilice este caso para separar la capacidad del modelo de la ejecución del lanzamiento, la documentación y la preparación de la API. | Límite |
| [Aumento del precio del plan de codificación](#case-59) | Utilice este caso para verificar el precio del plan antes de recomendar GLM-5.2 como reemplazo de bajo costo. | Límite |
| [Trabajo paralelo corto versus tiradas largas de agentes](#case-67) | Utilice este caso para dirigir GLM-5.2 hacia tareas de codificación limitadas cortas y, al mismo tiempo, reservar modelos más potentes para ejecuciones de agentes más profundas de varias horas. | Límite |
| [Comprobación de censura en código y sesgo](#case-73) | Usa este caso como una señal práctica de seguridad para pruebas de código y sesgo político, no como prueba de que las preocupaciones de alineación más amplias ya estén resueltas. | Límite |
| [Fallo de facturación en razonamiento difícil](#case-75) | Usa este caso para probar GLM-5.2 con cuidado en cargas de razonamiento difíciles, porque el informe público muestra tiempos largos, baja finalización y una facturación inesperadamente alta. | Límite |
| [Case 103: HalluHard Multiturn Hallucination Signal](#case-103) | Usa este caso para probar GLM-5.2 en tareas multiturno sensibles a las alucinaciones antes de confiar en puntuaciones fuertes de benchmark en otros frentes. | Límite |
| [Case 108: Open-Weight Security Emergency Warning](#case-108) | Usa este caso como señal para planificar seguridad: GLM-5.2 open-weight reduce la fricción operativa para agentes ofensivos de seguridad incluso cuando las APIs cerradas siguen monitorizadas. | Límite |
<a id="benchmarks-frontier-evaluation"></a>
## 📏 Evaluaciones comparativas y evaluación de frontera

<a id="case-1"></a>
### Case 1: [Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2067135640249209175) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilice la publicación de Análisis artificial para comparar GLM-5.2 con otros modelos de frontera patentados y de peso abierto en materia de inteligencia y costo por tarea.**

Artificial Analysis informó que GLM-5.2 es el modelo líder en ponderaciones abiertas en su Índice de Inteligencia, con una puntuación de 51 y una posición en la frontera de Pareto en inteligencia versus costo por tarea. La publicación también registra el tamaño del modelo, la ventana de contexto, los precios y la disponibilidad del proveedor.

Tipo: Referencia | Fecha: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Code Arena Frontend Ranking](https://x.com/arena/status/2066957802741043641) (por [@arena](https://x.com/arena))

**Utilice este caso para evaluar GLM-5.2 en tareas reales de codificación front-end juzgadas mediante comparaciones de estilo arena.**

La cuenta de Arena informó que GLM-5.2 Max ocupa el segundo lugar en Code Arena Frontend, por delante de otros modelos abiertos y cerca de la entrada de la frontera superior. La publicación es especialmente útil para casos de uso de front-end, React, HTML, juegos, simulación y diseño basado en referencias.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Design Arena First Place](https://x.com/Designarena/status/2066940737011560652) (por [@Designarena](https://x.com/Designarena))

**Utilice este caso para juzgar si GLM-5.2 puede manejar tareas de diseño más código en lugar de solo pruebas comparativas de codificación con mucho texto.**

Design Arena informó que GLM-5.2 alcanzó el primer lugar con una puntuación Elo de 1360, lo que destaca un salto en el rendimiento del código de diseño para un modelo de peso abierto. Trátelo como una señal de referencia de diseño, no como un sustituto de la revisión de la interfaz de usuario específica del proyecto.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [FrontierSWE Result](https://x.com/ProximalHQ/status/2066939701026787583) (por [@ProximalHQ](https://x.com/ProximalHQ))

**Utilice la publicación de FrontierSWE para comparar GLM-5.2 con los modelos GPT-5.5, Opus y Fable en tareas de ingeniería de software.**

La publicación informa que GLM-5.2 ocupa el tercer lugar en FrontierSWE y lo enmarca como uno de los primeros modelos de peso abierto que reduce la brecha con los mejores modelos propietarios en trabajos de ingeniería de implementación pesada.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [DeepSWE Open-Source Lead](https://x.com/AiBattle_/status/2066938378512126024) (por [@AiBattle_](https://x.com/AiBattle_))

**Utilice el caso de DeepSWE para comprender GLM-5.2 como un modelo abierto sólido para tareas difíciles de evaluación de ingeniería de software.**

AiBattle informó una puntuación DeepSWE del 46,2 % para GLM-5.2 y la describió como la puntuación más alta para un modelo de código abierto en ese contexto de referencia.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Terminal-Bench Over 80 Percent](https://x.com/cline/status/2066951439793242193) (por [@cline](https://x.com/cline))

**Utilice este caso al evaluar GLM-5.2 para flujos de trabajo de agentes y codificación orientados a terminales.**

Cline destacó GLM-5.2 como el primer modelo de peso abierto que superó el 80 % en Terminal-Bench y lo posicionó como una opción de nivel de frontera para un desarrollo accesible basado en herramientas.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [Comparación de SWELancer con GPT-5.5](https://x.com/gosrum/status/2067153091842203676) (por [@gosrum](https://x.com/gosrum))

**Utilice este caso de SWELancer como una comparación multimétrica concreta entre GLM-5.2 y GPT-5.5 sobre el éxito de la tarea, la recompensa y el tiempo de finalización.**

El autor compartió una actualización de referencia japonesa en la que GLM-5.2 superó inesperadamente a GPT-5.5 en los últimos resultados de SWELancer en términos de éxito de la tarea, recompensa obtenida y tiempo para completarla, con dos tareas inaccesibles excluidas.

Tipo: Evaluación | Fecha: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [BridgeBench Perfect Score Signal](https://x.com/bridgemindai/status/2065874542321426819) (por [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para inspeccionar GLM-5.2 sobre un razonamiento fundamentado de varios pasos en lugar de solo codificar tablas de clasificación.**

BridgeMind informó que el GLM-5.2 fue el primer modelo en recibir una puntuación perfecta en el benchmark BridgeBench BS, lo que lo convierte en una fuente útil para afirmaciones de evaluación con mucho razonamiento.

Tipo: Referencia | Fecha: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Reasoning Number One](https://x.com/bridgebench/status/2066123398816624743) (por [@bridgebench](https://x.com/bridgebench))

**Utilice este caso para comparar GLM-5.2 con modelos de frontera cerrada en tareas de razonamiento fundamentado.**

BridgeBench informó que GLM-5.2 ocupó el puesto número uno en un punto de referencia de razonamiento y superó a Claude Fable 5 en ese contexto de medición.

Tipo: Referencia | Fecha: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard Without Shortcutting](https://x.com/elliotarledge/status/2065735912370417760) (por [@elliotarledge](https://x.com/elliotarledge))

**Utilice este caso para comprobar si las ganancias de referencia provienen de un comportamiento de implementación válido en lugar de atajos.**

La publicación de KernelBench-Hard dice que el resultado interesante no fue solo la puntuación, sino que GLM-5.2 dejó de usar un acceso directo inapropiado en un problema GEMM fp8, lo que lo hace relevante para la integridad del benchmark.

Tipo: Evaluación | Fecha: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Runescape Bench Catch-Up](https://x.com/maxbittker/status/2066985743197577433) (por [@maxbittker](https://x.com/maxbittker))

**Utilice este caso como una señal rápida para el progreso del modelo de peso abierto en tareas de referencia similares a las de un juego.**

La publicación informa que GLM-5.2 obtiene una puntuación mejor que los modelos propietarios recientes en Runescape, y utiliza ese resultado para enmarcar la rapidez con la que se está poniendo al día la capacidad de frontera de código abierto.

Tipo: Referencia | Fecha: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [BridgeBench Speed Improvement](https://x.com/bridgebench/status/2065845045752648159) (por [@bridgebench](https://x.com/bridgebench))

**Utilice este caso para evaluar flujos de trabajo sensibles a la latencia donde la velocidad importa junto con la inteligencia.**

BridgeBench informó que GLM-5.2 es tres veces más rápido que GLM-5.1 y cuarto en su punto de referencia de velocidad, lo que lo hace relevante para flujos de trabajo donde la velocidad de iteración afecta la usabilidad.

Tipo: Referencia | Fecha: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [Codificación KernelBench Hard y Mega GPU](https://x.com/elliotarledge/status/2068177175640240323) (por [@elliotarledge](https://x.com/elliotarledge))

**Utilice este caso para evaluar GLM-5.2 en la codificación del kernel de GPU en KernelBench-Hard y KernelBench-Mega, donde los rastros de agentes abiertos hacen que el resultado sea inspeccionable.**

La actualización de KernelBench informa pruebas H100, B200 y RTX PRO 6000, seguimientos de agentes de código abierto y GLM-5.2 como el modelo abierto superior en la comparación.

Tipo: Referencia | Fecha: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [Liderazgo open-source en DeepSWE con esfuerzo máximo](https://x.com/datacurve/status/2068473057107476680) (por [@datacurve](https://x.com/datacurve))

**Usa este caso para seguir a GLM-5.2 en DeepSWE con esfuerzo máximo, donde la tabla publicada lo sitúa primero entre los modelos abiertos con una puntuación pass@1 del 44%.**

DataCurve compartió una actualización de la tabla de DeepSWE que muestra a GLM-5.2 con 44% pass@1 y 17 puntos por delante de Kimi K2.7 Code entre los modelos abiertos. Tómalo como una actualización de benchmark, no como prueba de que todos los workflows reales de agentes ya estén resueltos.

Tipo: Referencia | Fecha: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [Segundo puesto en benchmark de debates LLM](https://x.com/LechMazur/status/2068428300460974279) (por [@LechMazur](https://x.com/LechMazur))

**Usa este caso para evaluar GLM-5.2 más allá del código en debates adversariales de varios turnos, donde la variante de razonamiento máximo quedó segunda detrás de modelos Claude.**

Lech Mazur compartió un resultado del LLM Debate Benchmark que sitúa a GLM-5.2 Max en segundo lugar. El benchmark mide debates adversariales de varios turnos sobre temas amplios, por lo que funciona como una señal de razonamiento fuera de los leaderboards de código habituales.

Tipo: Referencia | Fecha: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [Tasa de alucinación en AA-Omniscience](https://x.com/yuhasbeentaken/status/2068259921519423855) (por [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Usa este caso para comparar GLM-5.2 en manejo de incertidumbre, donde el resultado publicado de AA-Omniscience muestra una tasa de alucinación menor que la de varios otros modelos frontier.**

La publicación reporta una tasa de alucinación del 28% para GLM-5.2 en AA-Omniscience, frente a tasas más altas para Fable 5 y DeepSeek V4 Pro. El benchmark se plantea en torno a si los modelos rehúsan responder o admiten incertidumbre en lugar de adivinar.

Tipo: Evaluación | Fecha: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [GDPval-AA Agentic Work Index](https://x.com/ArtificialAnlys/status/2069121548670406947) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para comparar GLM-5.2 en trabajo de conocimiento de largo horizonte, en lugar de limitarte a rankings centrados solo en código.**

Artificial Analysis informa que GLM-5.2 alcanza 1524 Elo en GDPval-AA, puesto #3 global detrás de Claude Fable 5 y Opus 4.8, y ligeramente por delante de GPT-5.5 xhigh con 1509. Es el modelo open-weights mejor clasificado con amplio margen, y la publicación dice que el benchmark promedió unas 31 vueltas por tarea en 1,999 enfrentamientos.

Tipo: Evaluación | Fecha: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Game Dev Arena Runner-Up](https://x.com/Designarena/status/2069166634976371084) (por [@Designarena](https://x.com/Designarena))

**Usa este caso para juzgar la calidad de GLM-5.2 en creación de juegos, donde el modelo alcanzó el segundo puesto en Game Dev Arena y se convirtió en el laboratorio open-weight mejor clasificado en ese ranking.**

Design Arena informó que GLM-5.2 logró 1368 Elo en Game Dev Arena, con una subida de 29 puntos y seis puestos frente a GLM-5.1. La publicación lo sitúa en la misma banda de rendimiento que Claude Fable 5 y dice que quedó segundo en la clasificación general, por delante de OpenAI y solo por detrás de Anthropic a nivel de laboratorio.

Tipo: Evaluación | Fecha: 2026-06-22

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 Agentes de código y flujos de contexto largo

<a id="case-13"></a>
### Case 13: [One Hour Forty Two Minute Refactor Loop](https://x.com/KELMAND1/status/2066012493315723610) (por [@KELMAND1](https://x.com/KELMAND1))

**Utilice este caso como patrón para una refactorización frontal autónoma prolongada con TDD, comentarios de los revisores y comprobaciones de regresión.**

La publicación describe una tarea de refactorización de GLM-5.2 de 1 hora y 42 minutos con 88 giros de modelo y 102 llamadas de herramientas. El flujo de trabajo incluyó una transferencia, cuatro correcciones de bloqueadores, implementación TDD de 12 pruebas, dos rondas de correcciones P2 y una regresión final.

Tipo: Demo | Fecha: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [OpenCode Bug Fix And Implementation Test](https://x.com/altudev/status/2065868921341632881) (por [@altudev](https://x.com/altudev))

**Utilice este caso para probar GLM-5.2 como agente de codificación OpenCode para corregir errores además de una pequeña tarea de implementación.**

El autor informa que probó GLM-5.2 con seis correcciones de errores y una implementación en OpenCode, y dice que los cambios se realizaron de manera limpia con una planificación sólida y mejor velocidad que GLM-5.1.

Tipo: Demo | Fecha: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [OpenCode Retro Video Game Walkthrough](https://x.com/AskVenice/status/2067047775783534789) (por [@AskVenice](https://x.com/AskVenice))

**Utilice este tutorial para crear un juego pequeño con GLM-5.2 y OpenCode desde un solo mensaje y luego inspeccione cómo el modelo maneja los detalles de implementación.**

Venice compartió un tutorial completo para crear un videojuego retro con GLM-5.2 y OpenCode, posicionándolo como un flujo de trabajo de codificación privado, de código abierto y de largo horizonte.

Tipo: Tutorial | Fecha: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [HTML5 Physics Simulations Contest](https://x.com/atomic_chat_hq/status/2067038851139334588) (por [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilice este caso para comparar el código GLM-5.2 y Kimi K2.7 en simulaciones de física HTML5 autónomas sin bibliotecas.**

Atomic Chat informó que pidió a ambos modelos que construyeran simulaciones de rotura de piscina, bloques de resorte y tablero Galton. Su publicación dice que GLM-5.2 manejó los tres con más detalle y pulido, mientras que Kimi tuvo problemas con el comportamiento físico.

Tipo: Evaluación | Fecha: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Personal Site UI UX Build](https://x.com/anshuc/status/2067034697704857615) (por [@anshuc](https://x.com/anshuc))

**Utilice este caso para solicitar a GLM-5.2 un sitio personal pulido e inspeccionar hasta qué punto múltiples turnos pueden mejorar la UI/UX.**

El autor dice que GLM-5.2 produjo un sitio personal creativo después de ser impulsado con las indicaciones correctas y compartió un video del resultado. Es útil para la iteración del diseño de front-end en lugar de para afirmaciones de referencia de un solo disparo.

Tipo: Demo | Fecha: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [AI Contract Review Product Build](https://x.com/laozhang2579/status/2066339734956499301) (por [@laozhang2579](https://x.com/laozhang2579))

**Utilice este caso para evaluar GLM-5.2 en una tarea de creación de productos con un PRD, presupuesto de tiempo, recuento de pasos, cuota de uso y comparación de calidad del código.**

La publicación china compara GLM-5.2, Kimi K2.7 y Claude Opus 4.8 en un producto PRD de revisión de contratos de IA. Informa la duración de la compilación, el recuento de pasos, el uso de la cuota de cinco horas y la puntuación de la calidad del código.

Tipo: Evaluación | Fecha: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [ZCode Goal Feature For Larger Development Objectives](https://x.com/zcode_ai/status/2066236605917188228) (por [@zcode_ai](https://x.com/zcode_ai))

**Utilice este caso para comprender cómo se integra GLM-5.2 en ZCode 3.0 para tareas de desarrollo agente más grandes.**

ZCode anunció la disponibilidad de GLM-5.2 para los usuarios del plan de codificación, una ejecución más sólida de las tareas del agente, una mejor codificación de contexto largo y una función de objetivo para gestionar objetivos más grandes desde la planificación hasta su finalización.

Tipo: Integración | Fecha: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [Envoltorio de Linux para ZCode creado con GLM-5.2](https://x.com/gosrum/status/2066484949755269510) (por [@gosrum](https://x.com/gosrum))

**Utilice este caso como ejemplo de cómo GLM-5.2 ayuda con herramientas en entornos de agentes de codificación.**

El autor informa haber completado zcode-linux utilizando GLM-5.2 y Claude Code para que los usuarios de Linux puedan ejecutar ZCode en un entorno Linux y agregar puntos finales API arbitrarios, incluidos puntos finales LLM locales.

Tipo: Demo | Fecha: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Computer Use Skill Packaging](https://x.com/0xSero/status/2065952130054382079) (por [@0xSero](https://x.com/0xSero))

**Utilice este caso para estudiar GLM-5.2 como ayuda para convertir un repositorio de uso de computadora de código abierto en una habilidad reutilizable.**

La publicación dice que GLM-5.2 estaba configurando el uso de la computadora, encontró un repositorio avanzado de código abierto y lo convirtió en una habilidad. Es una señal práctica para el trabajo de integración de agentes y envoltura de herramientas.

Tipo: Demo | Fecha: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [ZCode 3.0 Agentic Development Environment Review](https://x.com/laogui/status/2066190262993559963) (por [@laogui](https://x.com/laogui))

**Utilice este caso para evaluar GLM-5.2 dentro de un entorno de desarrollo agente completo en lugar de una única sesión de chat.**

La revisión china dice que ZCode 3.0 fue reescrito a partir de versiones anteriores tipo shell en un núcleo de agente de desarrollo propio junto con GLM-5.2, con una mejor experiencia entre los entornos de desarrollo de agentes nacionales.

Tipo: Demo | Fecha: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [Arnés OpenCode con servicio local](https://x.com/PatrickToulme/status/2068134212587184442) (por [@PatrickToulme](https://x.com/PatrickToulme))

**Utilice este caso para probar GLM-5.2 con el arnés OpenCode, el servicio local y los flujos de trabajo de codificación con muchas herramientas antes de compararlo con Claude Opus.**

El autor informa sobre una implementación local, subagentes anidados, comportamiento de investigación/planificación y una compilación de aplicación funcional.

Tipo: Evaluación | Fecha: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Fast-RLM Long-Context Instruction Injection](https://x.com/neural_avb/status/2067992817625088439) (por [@neural_avb](https://x.com/neural_avb))

**Utilice este caso para mejorar el recuento de contexto largo de GLM-5.2 y el comportamiento del agente REPL moviendo instrucciones al indicador del sistema RLM.**

Las notas de la versión describen un cambio concreto en el andamiaje del agente y un efecto de referencia de contexto largo de GLM-5.2.

Tipo: Integración | Fecha: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [DeepAgents Code Open Harness Trial](https://x.com/sydneyrunkle/status/2067947260369854830) (por [@sydneyrunkle](https://x.com/sydneyrunkle))

**Utilice este caso para probar GLM-5.2 con un arnés de agente de codificación abierto y compare el modelo bajo un shell de agente reproducible.**

El autor informa que utiliza GLM-5.2 con DeepAgents Code y marcos de modelo abierto más arnés abierto como patrón de prueba.

Tipo: Demo | Fecha: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [Enrutamiento de stack de agentes de marketing en producción](https://x.com/DeRonin_/status/2068303752671477820) (por [@DeRonin_](https://x.com/DeRonin_))

**Usa este caso para enrutar GLM-5.2 a workflows de agentes en producción que valoran estructura, velocidad y self-hosting, manteniendo modelos cerrados más fuertes para juicios ambiguos.**

Tras una ejecución comparativa de seis días en un stack de agencia, el autor dice que GLM-5.2 sostuvo más de 60 pasos de agente antes de desviarse, respetó formatos estructurados más de 800 veces seguidas y entregó respuestas self-hosted de baja latencia. La misma publicación sigue prefiriendo Opus para tareas críticas de voz o ambiguas, así que la propia regla de enrutamiento es la conclusión útil.

Tipo: Evaluación | Fecha: 2026-06-20

---



<a id="case-80"></a>
### Case 80: [Recreación de Pokemon Red en M3 Ultra](https://x.com/hxiao/status/2068800750554378434) (por [@hxiao](https://x.com/hxiao))

**Usa este caso para evaluar GLM-5.2 en una ejecución local de agente de código a largo plazo, donde el modelo pasó alrededor de medio día intentando recrear Pokemon Red en HTML en una máquina M3 Ultra.**

El autor cambió el modelo de Claude Code por GLM 5.2 local en una máquina M3 Ultra de 512 GB y ejecutó durante 12 horas la tarea `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.`. La publicación comparte tiempo de ejecución, uso de tokens, churn de código, uso de RAM y la configuración de GGUF más KV-cache, al tiempo que señala que la calidad del modelo se sintió de nivel frontier pero que el throughput de inferencia local fue el cuello de botella.

Tipo: Demo | Fecha: 2026-06-21

---
<a id="case-91"></a>
### Case 91: [Cline Repo Bug Fix Showdown](https://x.com/cline/status/2069171146994729078) (por [@cline](https://x.com/cline))

**Usa este caso para comparar GLM-5.2 y Opus 4.8 en la corrección de un bug de un repositorio real, donde GLM gastó más tokens pero entregó el parche final más barato y más limpio.**

Cline probó ambos modelos sobre el mismo bug del repo Cline con el mismo harness y las mismas herramientas. La publicación dice que GLM usó cerca de 1.1M tokens frente a 660K de Opus, costó $0.41 frente a $0.81, tardó 4.7 minutos y 28 llamadas a herramientas frente a 1.6 minutos y 12 llamadas, y terminó con limpieza de código muerto y build de producción exitosa, mientras Opus dejó errores de tipos que aun así pasaban las pruebas.

Tipo: Evaluación | Fecha: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [OpenInspect FP8 Background Agent](https://x.com/colemurray/status/2069485572339707938) (por [@colemurray](https://x.com/colemurray))

**Usa este caso para estudiar un stack de agente en segundo plano autoalojado con GLM-5.2 en lugar de un flujo de chat alojado.**

Cole Murray compartió un stack de OpenInspect, remote code runner y Fireworks FP8 GLM-5.2 que ejecuta agentes en segundo plano sobre infraestructura autoalojada. La publicación presenta la configuración como una alternativa abierta a los productos de agentes alojados y enlaza a un runbook ya publicado.

Tipo: Integración | Fecha: 2026-06-23

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 Demos prácticas y muestras

<a id="case-23"></a>
### Case 23: [Playable Backrooms One-Shot](https://x.com/aimlapi/status/2066996493257408639) (por [@aimlapi](https://x.com/aimlapi))

**Utilice este caso para comparar el resultado, el tiempo de ejecución y el costo de creación de juegos con el mismo sistema entre GLM-5.2 y Opus 4.8.**

AI/ML API informó haber pedido a GLM-5.2 y Opus 4.8 realizar un one-shot en un juego de Backrooms jugable. Su publicación dice que el GLM-5.2 construyó una mecánica más completa en 1:08 a $0,37, mientras que Opus tardó 2:14 a $1,94.

Tipo: Demo | Fecha: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [Tres construcciones reales con resultados mixtos](https://x.com/bridgemindai/status/2065840871929442319) (por [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso como conjunto de demostración de advertencia: pruebe varias compilaciones reales antes de confiar en un modelo para tareas de producción de juegos o videos.**

BridgeMind probó GLM-5.2 en un juego de terror, un juego de sigilo en 3D y un vídeo de marketing de Remotion. La publicación informa resultados mixtos, incluida una lógica de juego rota, lo que la hace útil como señal de limitación fundamentada.

Tipo: Evaluación | Fecha: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Super Mario Clone In ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilice este caso para evaluar la creación de juegos iterativos con GLM-5.2 y ZCode en varias pasadas de corrección y funciones.**

El autor probó ZCode 3.0 con GLM-5.2 creando un clon al estilo de Super Mario y luego compartió el resultado después de cinco iteraciones de correcciones de problemas y adiciones de funciones.

Tipo: Demo | Fecha: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Lunar Lander Contest](https://x.com/ivanfioravanti/status/2066193134984319173) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilice este caso para comparar GLM-5.2, MiniMax M3 y Kimi K2.7 Code en una tarea de estilo de juego interactivo.**

La publicación describe un concurso de Lunar Lander entre MiniMax M3, GLM-5.2 y Kimi K2.7 Code, utilizando un resultado de video como punto de referencia práctico antes de regresar al desarrollo del modelo local.

Tipo: Evaluación | Fecha: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [One-Prompt Design Arena Creation](https://x.com/grx_xce/status/2066951779154374907) (por [@grx_xce](https://x.com/grx_xce))

**Utilice este caso para inspeccionar lo que GLM-5.2 puede generar a partir de un único mensaje de diseño en un contexto de arena.**

El autor compartió un ejemplo de una creación de GLM-5.2 en Design Arena realizada a partir de un mensaje, usándolo para mostrar la brecha cada vez menor entre los modelos de peso abierto y cerrado.

Tipo: Demo | Fecha: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [Trabajo de investigación: comprensión del flujo de trabajo](https://x.com/askalphaxiv/status/2066996976445706745) (por [@askalphaxiv](https://x.com/askalphaxiv))

**Utilice este caso para aplicar GLM-5.2 a flujos de trabajo de lectura de artículos con preguntas contextuales y referencias entre artículos.**

AlphaXiv introdujo GLM-5.2 para comprender artículos de investigación, donde los usuarios resaltan una sección, hacen preguntas y hacen referencia a otros artículos para contexto, comparaciones y referencias comparativas.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Constrained Poem Comparison](https://x.com/emollick/status/2067056226337186146) (por [@emollick](https://x.com/emollick))

**Utilice este caso para separar la corrección de la calidad creativa al comparar el GLM-5.2 con los modelos estilo Fable.**

Ethan Mollick le dio crédito a GLM-5.2 Max por producir un poema restringido correcto, al tiempo que señaló que Fable incorporó la restricción de letras que desaparecen en el tema del poema de manera más creativa.

Tipo: Evaluación | Fecha: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Design Sense Example](https://x.com/0xSero/status/2067074877941796994) (por [@0xSero](https://x.com/0xSero))

**Utilice este caso como una señal de diseño visual liviano y luego verifíquelo con su propio mensaje y revisión de la interfaz de usuario.**

El autor dice que disfrutaron el sentido del diseño del GLM-5.2 y compartieron un ejemplo visual. Es útil como indicador para inspeccionar, no como prueba independiente de la calidad del diseño de producción.

Tipo: Demo | Fecha: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Juego voxel estilo Temple Run en un solo intento](https://x.com/pseudokid/status/2068431546143649829) (por [@pseudokid](https://x.com/pseudokid))

**Usa este caso para poner a prueba GLM-5.2 en generación de juegos con un solo prompt y luego revisar qué sigue necesitando correcciones iterativas en una build visualmente rica.**

El autor cuenta que obtuvo la mayor parte de un juego de motos voxel inspirado en Temple Run en el primer turno y luego usó unas pocas iteraciones de seguimiento para corregir cámara y movimiento. La publicación también señala que las herramientas de Z.ai pueden generar capturas y videos de gameplay para ayudar al modelo de texto a evaluar el resultado.

Tipo: Demo | Fecha: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [Conjunto de ejemplos one-shot en OpenCode Go](https://x.com/LyalinDotCom/status/2068378281636982990) (por [@LyalinDotCom](https://x.com/LyalinDotCom))

**Usa este caso para medir GLM-5.2 en builds rápidas de un solo intento dentro de OpenCode Go antes de comprometerlo a loops de agentes más abiertos.**

El autor reporta ejemplos one-shot que incluyen una app web del sistema solar, una app Electron de información del sistema y un sencillo juego web de exploración de islas mediante OpenCode Go. La misma publicación también afirma que GLM-5.2 es el mejor modelo abierto que ha usado, aunque sin llegar a llamarlo igual a la frontera.

Tipo: Demo | Fecha: 2026-06-20

---



<a id="case-81"></a>
### Case 81: [Build de Space Invaders con un solo prompt](https://x.com/DeryaTR_/status/2068803754611069128) (por [@DeryaTR_](https://x.com/DeryaTR_))

**Usa este caso para probar GLM-5.2 en la creación de juegos con un solo prompt y ver luego cómo unos pocos pases extra manejan cambios de assets y pulido simple.**

La autora dice que GLM-5.2 construyó un juego jugable estilo Space Invaders a partir de un prompt principal y luego usó tres prompts de seguimiento para reemplazar sprites y añadir pequeños extras como un leaderboard. El resultado publicado es un ejemplo público ligero de calidad de creación de juegos, no un benchmark completo.

Tipo: Demo | Fecha: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [Laboratorio de recuperación de OpenCode en un solo intento](https://x.com/threepointone/status/2068718370581536816) (por [@threepointone](https://x.com/threepointone))

**Usa este caso para prototipar rápidamente simulaciones interactivas de fallos de agentes, porque el autor informa que obtuvo un recovery lab funcional en un solo intento por unos 3,50 $.**

El autor construyó un recovery lab totalmente interactivo con OpenCode y GLM-5.2 después de darle al modelo un análisis de 4.000 palabras y el repositorio del Agents SDK. La publicación reporta una ejecución de 176k tokens, un resultado one-shot y un coste de extremo a extremo de alrededor de 3,50 $ antes del pulido.

Tipo: Demo | Fecha: 2026-06-21

---
<a id="case-92"></a>
### Case 92: [Open Design Reference URL Rebuild](https://x.com/OpenDesignHQ/status/2069046584134778995) (por [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**Usa este caso para probar GLM-5.2 en recreación web guiada por referencias, donde un solo prompt más una URL de origen reprodujeron un sitio con fidelidad casi a nivel de píxel.**

Open Design dice que probó GLM-5.2 en su AMR integrado usando solo una URL de referencia y un prompt sencillo, y el modelo recreó el sitio web casi a la perfección en la demo. Tómalo como una prueba práctica de generación de UI basada en referencias, no como un benchmark completo.

Tipo: Demo | Fecha: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Trader Desk Cost-Quality Test](https://x.com/atomic_chat_hq/status/2069171121044513273) (por [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Usa este caso para comparar GLM-5.2 en builds full-stack de UI, donde se acercó al resultado de trading desk más pulido mientras costaba solo una pequeña fracción del mejor resultado.**

Atomic Chat comparó cuatro modelos con el mismo prompt real de Trader Desk, con frontend, backend, datos de mercado de ocho símbolos y una UI personalizada de tema oscuro. La publicación informa que GLM-5.2 usó 13,677 tokens y costó $0.03, frente a Fugu Ultra con 22,225 tokens y $0.51, y dice que GLM produjo una interfaz multipanel igualmente completa con datos en vivo a un coste mucho menor.

Tipo: Evaluación | Fecha: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Luddite Game After Claude Refusal](https://x.com/atmoio/status/2069559053114577088) (por [@atmoio](https://x.com/atmoio))

**Usa este caso para prototipar conceptos de juego sensibles a políticas con GLM-5.2 cuando un modelo cerrado rechaza la solicitud, y luego inspeccionar por ti mismo el resultado jugable.**

atmoio dice que Claude marcó como violación de uso aceptable un juego humorístico estilo Plague Inc. sobre destruir IA, así que el autor construyó en su lugar con GLM 5.2 el juego llamado Luddite y adjuntó un clip de demo. Tómalo como un ejemplo práctico de fallback para tareas de creative coding que los modelos cerrados pueden rechazar por motivos de política.

Tipo: Demo | Fecha: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 Integraciones de proveedores y herramientas

<a id="case-31"></a>
### Case 31: [OpenCode Go Availability](https://x.com/opencode/status/2067207923122479242) (por [@opencode](https://x.com/opencode))

**Utilice este caso para realizar un seguimiento de la disponibilidad de GLM-5.2 dentro de los flujos de trabajo de OpenCode Go con texto, contexto de 1 millón y precios similares a GLM-5.1.**

OpenCode anunció la disponibilidad de GLM-5.2 en Go, destacando la compatibilidad con texto, una ventana de contexto de 1 millón y el mismo precio que 5.1.

Tipo: Integración | Fecha: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Ollama Cloud Availability](https://x.com/ollama/status/2066949797316350361) (por [@ollama](https://x.com/ollama))

**Utilice este caso para enrutar GLM-5.2 a Ollama Cloud para realizar experimentos de modelos de codificación de código abierto accesibles.**

Ollama anunció la disponibilidad de GLM-5.2 y lo describió como un modelo de tarea agente y codificación de largo horizonte con contexto 1M.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [OpenRouter One API Call Access](https://x.com/OpenRouter/status/2066941552208056561) (por [@OpenRouter](https://x.com/OpenRouter))

**Utilice este caso para acceder a GLM-5.2 a través de OpenRouter al comparar enrutamiento de proveedores o pilas multimodelo.**

OpenRouter anunció la disponibilidad de GLM-5.2 como un modelo de largo horizonte de 1 millón de tokens, brindando a los usuarios una ruta neutral para llamarlo.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [vLLM Day-Zero Support](https://x.com/vllm_project/status/2066950636428775693) (por [@vllm_project](https://x.com/vllm_project))

**Utilice este caso para autohospedar o servir GLM-5.2 a través de vLLM con soporte de día cero.**

El proyecto vLLM anunció la compatibilidad con GLM-5.2 en v0.23.0, enmarcándolo como un modelo emblemático para agentes de codificación de largo horizonte con contexto 1M.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Notion Availability Via Baseten](https://x.com/NotionHQ/status/2066963258985320550) (por [@NotionHQ](https://x.com/NotionHQ))

**Utilice este caso para identificar GLM-5.2 como un modelo de peso abierto disponible dentro de los flujos de trabajo de Notion.**

Notion anunció la disponibilidad de GLM-5.2 como un modelo de peso abierto creado para tareas a largo plazo y servido a través de Baseten.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Fireworks Day-Zero Serving](https://x.com/FireworksAI_HQ/status/2067007200426680509) (por [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilice este caso para evaluar Fireworks como ruta de servicio para cargas de trabajo GLM-5.2 que necesitan una infraestructura alojada.**

Fireworks anunció GLM-5.2 en vivo el día cero, enfatizando el contexto 1M, el posicionamiento de codificación primero y la validación independiente en SWE-Bench, Terminal-Bench, GPQA y AIME.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Enlace al jardín modelo de Google Cloud](https://x.com/CarolGLMs/status/2067127223216419088) (por [@CarolGLMs](https://x.com/CarolGLMs))

**Utilice este caso para encontrar GLM-5.2 en contextos de plataforma de agentes y de implementación orientados a Google Cloud.**

CarolGLMs compartió un enlace de Google Cloud para GLM-5.2, lo que lo convierte en un indicador directo para los equipos que trabajan a través de catálogos de modelos en la nube.

Tipo: Integración | Fecha: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Venice Privacy Mode](https://x.com/AskVenice/status/2066990725439361251) (por [@AskVenice](https://x.com/AskVenice))

**Utilice este caso cuando el modo de privacidad, TEE o cifrado de extremo a extremo sea un factor decisivo al probar GLM-5.2.**

Venice anunció la disponibilidad de GLM-5.2 en modo privado con encuadre TEE/E2EE, destinado a codificación agente privada y tareas de largo horizonte.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Command Code Availability](https://x.com/CommandCodeAI/status/2066950478194503990) (por [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilice este caso para probar GLM-5.2 en Command Code con un plan inicial de bajo costo y funciones de codificación de contexto largo.**

Command Code anunció la disponibilidad de GLM-5.2, destacando el contexto de 1M, un razonamiento sólido, el estado de código abierto y el acceso a través de su plan Go de un dólar.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Agente Hermes De Nous Portal](https://x.com/Teknium/status/2066954081575592282) (por [@Teknium](https://x.com/Teknium))

**Utilice este caso para conectar GLM-5.2 a los flujos de trabajo del Agente Hermes a través de Nous Portal y OpenRouter.**

Teknium informó la disponibilidad de GLM-5.2 en Hermes Agent de Nous Portal y OpenRouter, útil para experimentos de enrutamiento de marco de agente.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [io.net Day-Zero Launch Partner](https://x.com/ionet/status/2067140436095803763) (por [@ionet](https://x.com/ionet))

**Utilice este caso al evaluar el servicio respaldado por computación para un modelo de contexto largo de parámetros 753B.**

io.net se anunció como socio de lanzamiento del día cero para GLM-5.2, enfatizando el contexto 1M, el diseño de agente primero, la codificación de largo horizonte y las necesidades informáticas de un modelo de parámetros 753B.

Tipo: Integración | Fecha: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Modular Cloud Day-Zero Serving](https://x.com/clattner_llvm/status/2066974950293147950) (por [@clattner_llvm](https://x.com/clattner_llvm))

**Utilice este caso para considerar Modular Cloud para el servicio GLM-5.2 de contexto prolongado a escala de proveedor.**

Chris Lattner publicó que GLM-5.2 estuvo activo en Modular Cloud el día cero, destacando los pesos abiertos, la codificación, los agentes de largo plazo y el contexto de 1M.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Cursor Setup Through OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (por [@agentnative_](https://x.com/agentnative_))

**Utilice este caso para configurar GLM-5.2 en Cursor a través de OpenRouter para un flujo de trabajo de codificación de modelo abierto de bajo costo.**

La fuente proporciona una ruta de configuración concreta del Cursor/OpenRouter en lugar de solo anunciar la disponibilidad del modelo.

Tipo: Tutorial | Fecha: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic Eyes For Visual Design](https://x.com/beyang/status/2068087124818317374) (por [@beyang](https://x.com/beyang))

**Utilice este caso para emparejar GLM-5.2 con agentes personalizados de Amp cuando un modelo de solo texto necesite soporte de revisión visual para tareas de diseño.**

La publicación conecta un resultado comparativo de diseño visual GLM-5.2 con agentes de complemento Amp que pueden proporcionar una capa de revisión.

Tipo: Integración | Fecha: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten Faster One-Million-Context Serving](https://x.com/alphatozeta8148/status/2067852860499562821) (por [@alphatozeta8148](https://x.com/alphatozeta8148))

**Utilice este caso para enrutar GLM-5.2 a través de Baseten cuando la velocidad de servicio de contexto largo sea importante para Factory Droid, OpenCode y arneses de codificación.**

La fuente informa que GLM-5.2 se ejecuta cuatro veces más rápido en un contexto completo de 1M y lo muestra en arneses de codificación.

Tipo: Integración | Fecha: 2026-06-20

<a id="case-74"></a>
### Case 74: [Subagentes QA de Browser Use para diseño web](https://x.com/browser_use/status/2068405699340853541) (por [@browser_use](https://x.com/browser_use))

**Usa este caso para combinar GLM-5.2 con subagentes multimodales de QA de Browser Use v2 cuando un modelo solo de texto necesita inspección visual y correcciones iterativas de sitios web.**

Browser Use informa que GLM-5.2 superó a Fable 5 en una tarea de diseño web y luego añadió subagentes de QA que inspeccionan el resultado, juzgan la estética, encuentran fallos y devuelven correcciones dirigidas a GLM. Según la publicación, el bucle completo de construcción más QA costó menos de 0,75 USD.

Tipo: Integración | Fecha: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [Tokens gratis diarios en el IDE oficial ZCode](https://x.com/Alan_Earn/status/2068223665268006924) (por [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan))

**Usa este caso para acceder a GLM-5.2 a través de ZCode cuando quieras un IDE oficial de programación gratuito con grandes asignaciones diarias de tokens y un flujo parecido a Cursor.**

La publicación describe ZCode como el IDE oficial de programación de Zhipu, con GLM-5.2 como modelo por defecto, 3M de tokens diarios, 1M de contexto y clientes para Mac y Windows. También incluye un flujo corto de configuración, lo que la hace más accionable que un anuncio genérico de lanzamiento.

Tipo: Tutorial | Fecha: 2026-06-20

---



<a id="case-83"></a>
### Case 83: [Configuración de Cursor mediante Fireworks](https://x.com/skirano/status/2068777440986513647) (por [@skirano](https://x.com/skirano))

**Usa este caso para conectar GLM-5.2 a Cursor mediante Fireworks con una configuración mínima compatible con OpenAI y sin código cliente personalizado.**

Skirano muestra un flujo mínimo de configuración en Cursor: pegar una clave de Fireworks en el campo de API key de OpenAI, usar `https://api.fireworks.ai/inference/v1` como base URL, seleccionar `accounts/fireworks/models/glm-5p2` y reiniciar Cursor. Esto lo convierte en una ruta concreta para probar GLM-5.2 dentro de un IDE de programación familiar.

Tipo: Tutorial | Fecha: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [Soporte del proveedor ZAI en VulcanBench](https://x.com/vulcanbench/status/2068724843856707676) (por [@vulcanbench](https://x.com/vulcanbench))

**Usa este caso para ejecutar GLM-5.2 en un harness abierto de benchmark con soporte de primer nivel para el proveedor ZAI y una ruta dedicada de API key.**

VulcanBench v0.2.0 añadió soporte de primer nivel para ZAI, lo que permite ejecutar GLM-5.2 como `zai:glm-5.2` junto a modelos de OpenAI y Anthropic con una `ZAI_API_KEY` dedicada. Esto resulta útil para quienes quieren un harness abierto de benchmark en lugar de capturas aisladas.

Tipo: Integración | Fecha: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [Variantes de razonamiento High/Max en OpenCode](https://x.com/OpenCodeLog/status/2068487086576156705) (por [@OpenCodeLog](https://x.com/OpenCodeLog))

**Usa este caso para acceder a las variantes de razonamiento High y Max de GLM-5.2 dentro de OpenCode, al tiempo que obtienes un manejo más fiable del límite de pasos.**

OpenCode v1.17.9 añadió variantes de pensamiento High y Max para GLM-5.2 en proveedores compatibles con OpenAI y Anthropic, además del mapeo nativo de esfuerzo para OpenRouter. La misma versión también corrigió el comportamiento del límite de pasos del agente, lo que hace la integración más práctica para ejecuciones más largas.

Tipo: Integración | Fecha: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Selección del endpoint de código de Z.ai](https://x.com/ivanfioravanti/status/2068574700721082400) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para enrutar el tráfico de coding plan de GLM-5.2 al endpoint de Z.ai optimizado para código en lugar de la ruta genérica de API.**

La publicación indica a los usuarios que usen `https://api.z.ai/api/coding/paas/v4` en lugar del endpoint general `https://api.z.ai/api/paas/v4/` para cargas de coding plan, y señala que `https://api.z.ai/api/anthropic` es lo que suelen usar herramientas como Claude Code y OpenCode cuando hay soporte. Tómalo como una corrección de configuración concreta cuando GLM-5.2 parezca estar mal enrutado.

Tipo: Tutorial | Fecha: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [Configuración gratuita de la API GLM-5.2 en ZenMux](https://x.com/0x_kaize/status/2068676992782811607) (por [@0x_kaize](https://x.com/0x_kaize))

**Usa este caso para obtener una API key y una base URL gratuitas de GLM-5.2, y luego conectarlas a Claude, Cursor, Hermes y herramientas similares.**

El autor comparte un flujo de configuración de cinco minutos para conseguir una API key y una base URL gratuitas de ZenMux, y luego conectar GLM-5.2 a Claude, Cursor, Hermes y herramientas similares. La publicación también señala que el rate limit de la capa gratuita llega rápido, por lo que resulta más útil como nota de acceso que como garantía de durabilidad.

Tipo: Tutorial | Fecha: 2026-06-21

---
<a id="case-93"></a>
### Case 93: [Noumena ncode GLM Default](https://x.com/_xjdr/status/2069030608727408993) (por [@_xjdr](https://x.com/_xjdr))

**Usa este caso para enrutar GLM-5.2 a entornos de agentes tipo ncode y Noumena con endpoints separados estándar y de contexto 1M, además de soporte como modelo por defecto.**

La actualización de Noumena dice que el equipo añadió soporte de primera clase para GLM en tool calling, análisis de funciones, routing de apps y trazas de razonamiento, y luego dividió la API en endpoints `glm-5.2` y `glm-5.2[1m]` para controlar el TTFT bajo tráfico pesado de contexto 1M. También dice que las nuevas builds de ncode cambiaron su modelo opus-class predeterminado de Kimi a GLM tras comentarios positivos de uso.

Tipo: Integración | Fecha: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Baseten + Droid Harness Quickstart](https://x.com/RayFernando1337/status/2069523126384525639) (por [@RayFernando1337](https://x.com/RayFernando1337))

**Usa este caso para poner GLM-5.2 en marcha rápidamente mediante Baseten y el harness Droid, con un flujo corto de configuración que también puedes reutilizar en otros IDEs.**

RayFernando1337 resume un tutorial con pasos marcados por tiempo: obtener una API key de Baseten, automatizar la configuración de Droid AI, probar la integración de GLM-5.2, revisar configuraciones alternativas y limitaciones, y terminar con notas extra de setup para otros IDEs.

Tipo: Tutorial | Fecha: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [OpenAI-Compatible GLM API Workflow](https://x.com/Marktechpost/status/2069308807570915500) (por [@Marktechpost](https://x.com/Marktechpost))

**Usa este caso para construir en Python un cliente GLM-5.2 compatible con OpenAI con control de razonamiento, tool calling, recuperación de contexto largo y seguimiento de costes.**

Marktechpost compartió un tutorial junto con un cuaderno de código enlazado para envolver GLM-5.2 en un único cliente compatible con OpenAI. La publicación dice que el flujo cubre control de thinking effort (`off`/`high`/`max`), canales en streaming de razonamiento frente a respuesta, tool calling con un agente de varios pasos, salida JSON estructurada, recuperación de contexto largo y seguimiento del coste por tokens.

Tipo: Tutorial | Fecha: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Perplexity Agent API Search Sandbox](https://x.com/perplexitydevs/status/2069252848647606584) (por [@perplexitydevs](https://x.com/perplexitydevs))

**Usa este caso para conectar GLM-5.2 a la Agent API de Perplexity cuando quieras agentes en sandbox con búsqueda detrás de una sola llamada API.**

Perplexity Devs anunció GLM-5.2 en la Agent API y lo describió como una buena opción para workflows de coding y agentes de largo horizonte. La publicación destaca específicamente Search as Code, una interfaz compatible con OpenAI y precios first-party sin margen adicional.

Tipo: Integración | Fecha: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [Baseten 280 TPS GLM API](https://x.com/aqaderb/status/2069220126272999501) (por [@aqaderb](https://x.com/aqaderb))

**Usa este caso cuando importe la latencia del proveedor: Baseten afirma un serving de GLM-5.2 muy rápido con time-to-first-token subsegundo y alto throughput de decodificación.**

aqaderb anunció la API de GLM-5.2 de Baseten con 280 tokens por segundo y menos de 0.8 segundos de TTFT. La publicación atribuye el resultado a PD disaggregation, speculative decoding con multi-token prediction heads, routing consciente de KV-cache y otras optimizaciones de serving, con un enlace a una nota técnica.

Tipo: Integración | Fecha: 2026-06-23

---

<a id="case-95"></a>
### Case 95: [Claude Code Through Baseten](https://x.com/thealexker/status/2069163621469335757) (por [@thealexker](https://x.com/thealexker))

**Usa este caso para ejecutar GLM-5.2 dentro de Claude Code mediante una clave de Baseten, una base URL personalizada y remapeo de modelos en `~/.claude/settings.json`.**

El tutorial explica cómo instalar Claude Code, crear una cuenta en Baseten, obtener una API key y editar `~/.claude/settings.json` para que los tres niveles de modelos Claude apunten a `zai-org/GLM-5.2` mediante variables de entorno Anthropic personalizadas. Es un patrón de configuración concreto tipo drop-in para usar GLM-5.2 en el cliente Claude Code.

Tipo: Tutorial | Fecha: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Deepsec Pi Agent Default](https://x.com/cramforce/status/2069057402524082622) (por [@cramforce](https://x.com/cramforce))

**Usa este caso para probar GLM-5.2 en un harness de seguridad, donde `deepsec` lo convirtió en el modelo por defecto para Pi agent y reportó resultados competitivos en evaluaciones.**

La publicación anuncia soporte de `deepsec` para Pi agent de `@badlogicgames` con GLM-5.2 como modelo predeterminado y da un comando ejecutable: `pnpm deepsec process --agent pi`. También dice que el autor ejecutó las evaluaciones de Deepsec y encontró un resultado competitivo frente a otros modelos frontier, lo que lo convierte en una superficie de integración concreta orientada a seguridad.

Tipo: Integración | Fecha: 2026-06-22

---

<a id="cost-pricing-local-deployment"></a>
## 💸 Coste, precios y despliegue local

<a id="case-43"></a>
### Case 43: [Output Token Cost Comparison](https://x.com/Hesamation/status/2066999955638673891) (por [@Hesamation](https://x.com/Hesamation))

**Utilice este caso para comparar la economía del token de salida GLM-5.2 con los modelos estilo Opus, Fable y GPT-5.5.**

La publicación compara los precios de los tokens de producción de 1 millón y sostiene que GLM-5.2 puede ser significativamente más barato que los modelos de frontera cerrada. Trate las cifras como una comparación de precios vinculada a la fuente que debe volver a verificarse antes de presupuestar.

Tipo: Evaluación | Fecha: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [Local Near-Frontier Hardware ROI](https://x.com/Jeyffre/status/2067132023576354818) (por [@Jeyffre](https://x.com/Jeyffre))

**Utilice este caso para razonar sobre si los modelos autohospedados tipo GLM-5.2 pueden compensar los costos de hardware para los usuarios intensivos de agentes.**

El autor estima que varias máquinas de clase DGX Spark podrían ejecutar un modelo de clase 700B y compara una compra de hardware de aproximadamente $20,000 con un alto gasto mensual de API para cargas de trabajo de agentes y codificación.

Tipo: Evaluación | Fecha: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX On Two Mac Studios](https://x.com/pcuenq/status/2066967665726337219) (por [@pcuenq](https://x.com/pcuenq))

**Utilice este caso para explorar ejecuciones locales de GLM-5.2 en hardware de Apple y configuraciones orientadas a MLX.**

La publicación dice que GLM-5.2 acaba de ser lanzado y ya se estaba ejecutando con MLX en dos máquinas Mac Studio M3 Ultra, lo que lo presenta como comparable a los modelos cerrados recientes con pesos abiertos.

Tipo: Demo | Fecha: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [H100 Monthly Local Deployment Claim](https://x.com/ai_xiaomu/status/2066181367340429446) (por [@ai_xiaomu](https://x.com/ai_xiaomu))

**Utilice este caso como indicador de comparación de costos para verificar los supuestos de implementación local antes de elegir entre suscripción y autohospedaje.**

La publicación china compara los números declarados de SWE-Bench, el uso comercial de código abierto y el costo estimado de implementación local de un solo H100 con una suscripción a Claude Pro. Las cifras deberían revalidarse para los precios actuales de la infraestructura.

Tipo: Evaluación | Fecha: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Daily Credits And Claude Replacement Claim](https://x.com/RoundtableSpace/status/2067076011770986715) (por [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilice este caso para inspeccionar la narrativa del crédito gratuito y del agente de reemplazo en torno a GLM-5.2, mientras separa las afirmaciones de marketing de la adecuación de la carga de trabajo verificada.**

La publicación enmarca a GLM-5.2 como un competidor de Claude de menor costo con créditos diarios, control de código abierto, autohospedaje y un valor más sólido para largas sesiones de codificación.

Tipo: Evaluación | Fecha: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Free ZCode Token Window](https://x.com/0xSero/status/2066772591319077208) (por [@0xSero](https://x.com/0xSero))

**Utilice este caso para probar GLM-5.2 a través de una asignación gratuita de ZCode antes de comprometerse con un proveedor pago o una implementación local.**

El autor describe la disponibilidad de GLM-5.2 a través de ZCode con una gran cantidad de tokens diarios gratuitos y señala el posible uso para configurar vLLM Studio o alojamiento local.

Tipo: Integración | Fecha: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [ZenMux Free Week Offer](https://x.com/JZiyue_/status/2067114018079412723) (por [@JZiyue_](https://x.com/JZiyue_))

**Utilice este caso para encontrar ventanas de acceso gratuito con límites de tiempo para las pruebas de GLM-5.2.**

La publicación anuncia GLM-5.2 en vivo en ZenMux con una ventana gratuita de una semana, contexto de 1M, mejoras de codificación y agencia, y posicionamiento al mismo precio que 5.1.

Tipo: Integración | Fecha: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [Precios por token de crofAI](https://x.com/nahcrof/status/2067166596523765781) (por [@nahcrof](https://x.com/nahcrof))

**Utilice este caso para comparar los precios de proveedores externos para GLM-5.2 antes de seleccionar una ruta.**

La publicación anuncia GLM-5.2 en crofAI con precios de entrada, salida y caché enumerados, posicionándolo como inteligencia de frontera barata.

Tipo: Integración | Fecha: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [API Price Margin Comparison](https://x.com/scaling01/status/2066952626386714906) (por [@scaling01](https://x.com/scaling01))

**Utilice este caso como crítica de precios de mercado al comparar GLM-5.2 con otros laboratorios de vanguardia y modelos abiertos.**

El autor compara GLM-5.2 y otros grandes modelos abiertos sobre la fijación de precios de tokens de salida y utiliza la comparación para argumentar que algunos márgenes de API de laboratorio fronterizo son altos.

Tipo: Evaluación | Fecha: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Basement Local Inference Speed](https://x.com/volatilemrkts/status/2068077319986516031) (por [@volatilemrkts](https://x.com/volatilemrkts))

**Utilice este caso para estimar el rendimiento de inferencia local de GLM-5.2 en hardware Apple de gran memoria antes de planificar una configuración de codificación fuera de línea.**

La fuente informa 44,1 tokens por segundo en una configuración Mac local de alta memoria y menciona problemas de repetición de decodificación con llamadas de herramientas pesadas.

Tipo: Demo | Fecha: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Unsloth Quantized Local Deployment](https://x.com/mrblock/status/2067931982760394765) (por [@mrblock](https://x.com/mrblock))

**Utilice este caso para evaluar las rutas de implementación cuantificadas de GLM-5.2 cuando los pesos del modelo completo sean demasiado grandes para el hardware local normal.**

La publicación describe las opciones GGUF dinámicas de 2 bits y 1 bit de Unsloth, las reducciones de memoria y las rutas de implementación de llama.cpp o Unsloth Studio.

Tipo: Tutorial | Fecha: 2026-06-20

---



<a id="case-88"></a>
### Case 88: [Ejecución distribuida de MLX en dos M3 Ultra](https://x.com/ivanfioravanti/status/2068781499206574576) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para estimar cómo es servir GLM-5.2 en 8 bits a través de dos máquinas M3 Ultra antes de construir una configuración mayor sobre Apple silicon.**

La publicación muestra GLM-5.2 de 8 bits ejecutándose con MLX distributed en dos máquinas M3 Ultra de 512 GB a unas 17,9 tokens por segundo y con alrededor de 760 GB de memoria. El autor también señala que la configuración es una PR preliminar todavía en curso, así que úsala como señal de despliegue y no como guía terminada.

Tipo: Demo | Fecha: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [Reducción del multiplicador de ZCode hasta septiembre](https://x.com/buildwithhassan/status/2068534544177791376) (por [@buildwithhassan](https://x.com/buildwithhassan))

**Usa este caso para estirar los créditos del plan de GLM-5.2 con multiplicadores más bajos de ZCode tanto en horas pico como fuera de pico.**

La publicación dice que ZCode redujo los multiplicadores del coding plan de GLM de 3x a 2x en horas pico y de 2x a 0,67x fuera de pico, con la nueva ventana vigente hasta finales de septiembre. Esto lo convierte en una nota concreta de acceso y precio para cualquiera que quiera estirar sus créditos en GLM-5.2.

Tipo: Integración | Fecha: 2026-06-21

---
<a id="case-97"></a>
### Case 97: [RTX PRO 6000 Local Throughput](https://x.com/CardilloSamuel/status/2068954298596380743) (por [@CardilloSamuel](https://x.com/CardilloSamuel))

**Usa este caso para dimensionar una estación local de alta gama para GLM-5.2, donde un escritorio con dos Blackwell mantuvo velocidad de decodificación de dos dígitos en una build cuantizada a 4 bits.**

CardilloSamuel informa que ejecutó GLM-5.2 UD-Q4_K_XL en 2x RTX PRO 6000 Blackwells junto con un Threadripper PRO 9995WX y 1TB de DDR5. La publicación cita unos 64 tok/s de prefill, 13-15 tok/s de decode, una puntuación de 69.7% en Aider Polyglot a menos de dos puntos de BF16, y señala que el ancho de banda de la RAM del sistema era el cuello de botella, dejando fuera una 5090 desajustada del reparto.

Tipo: Demo | Fecha: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Mac Studio API ROI Reality Check](https://x.com/karminski3/status/2068974488973447524) (por [@karminski3](https://x.com/karminski3))

**Usa este caso para validar si tiene sentido comprar un Mac Studio para inferencia local de GLM-5.2, porque las cuentas de amortización publicadas favorecen claramente el acceso por API o plan para la mayoría de usuarios.**

La publicación estima que un Mac Studio de RMB 32,999 equivale aproximadamente a 1,178 millones de tokens de API de GLM-5.2 con los precios citados, y argumenta que el periodo de amortización es de unos 209 días incluso para una configuración Qwen mucho más pequeña. Luego dice que un Mac Studio de 512GB ejecutando GLM-5.2 cuantizado a unos 17 tok/s podría tardar alrededor de siete años en amortizarse, así que la propiedad local solo tiene sentido si ya tienes el hardware o puedes aprovechar tiempos muertos.

Tipo: Evaluación | Fecha: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [LiteLLM Local Outage Save](https://x.com/CardilloSamuel/status/2069431311463236078) (por [@CardilloSamuel](https://x.com/CardilloSamuel))

**Usa este caso para mantener avanzando un entregable cuando las APIs frontier alojadas fallen o queden limitadas, redirigiendo el trabajo mediante un GLM-5.2 desplegado localmente con LiteLLM.**

CardilloSamuel dice que un amigo se quedó sin tokens y se topó con una caída de Claude, así que le emitió una API key de LiteLLM apuntando a su despliegue local de GLM-5.2. Según cuenta, el amigo generó unos 5 millones de tokens por $0, terminó el entregable a tiempo y aceptó menor velocidad a cambio de continuidad.

Tipo: Demo | Fecha: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [Individual Versus Team Local ROI](https://x.com/yuhasbeentaken/status/2069337770493919414) (por [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Usa este caso para decidir si un despliegue local de GLM-5.2 tiene sentido para una persona individual o más bien solo para un equipo de desarrollo más grande.**

La publicación sostiene que una configuración local individual puede requerir 512 GB de memoria del sistema, varias GPUs y una CPU potente, y aun así ofrecer solo unas 6-10 tokens por segundo. También dice que un servidor compartido interno cobra más sentido para equipos de 10 o más desarrolladores que valoren privacidad, tokens ilimitados, ausencia de límites semanales y protección frente a caídas del proveedor o cambios de política.

Tipo: Evaluación | Fecha: 2026-06-23

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 Límites, advertencias y señales de seguridad

<a id="case-52"></a>
### Case 52: [No Vision Caveat](https://x.com/sawyerhood/status/2067061246705426923) (por [@sawyerhood](https://x.com/sawyerhood))

**Utilice este caso para recordar que GLM-5.2 puede ser menos útil para flujos de trabajo que requieren capacidad de visión nativa.**

El autor señala que los modelos GLM que carecen de visión reducen su utilidad, citando una publicación de clasificación de Design Arena. Esta es una advertencia práctica para la planificación de productos multimodales.

Tipo: Límite | Fecha: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [Advertencia sobre la brecha de agentes en el mundo real](https://x.com/ml_angelopoulos/status/2067013545431269405) (por [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**Utilice este caso para evitar una lectura excesiva de los resultados de los puntos de referencia como prueba de que GLM-5.2 coincide con los mejores modelos propietarios en todas las tareas agentes implementadas.**

El autor dice que GLM-5.2 es impresionante, pero aún no se acerca al nivel de Fable o al nivel de pensamiento de Opus 4.8 en la distribución general de tareas agentes del mundo real, basado en una metodología Agent Arena.

Tipo: Límite | Fecha: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Safety Guardrail Concern](https://x.com/VittoStack/status/2066984051840606436) (por [@VittoStack](https://x.com/VittoStack))

**Utilice este caso como recordatorio para realizar evaluaciones de seguridad antes de implementar GLM-5.2 en dominios confidenciales.**

La publicación informa una falla en el rechazo de contenido dañino en una prueba de seguridad comparativa. El repositorio registra sólo la señal de seguridad, no los detalles inseguros, y trata esto como una advertencia de riesgo de implementación.

Tipo: Límite | Fecha: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [Crítica de la metodología de referencia](https://x.com/josepha_mayo/status/2066951013337112661) (por [@josepha_mayo](https://x.com/josepha_mayo))

**Utilice este caso para cuestionar la metodología de referencia incluso cuando el resultado principal favorezca a GLM-5.2.**

El autor critica la metodología Design Arena y al mismo tiempo reconoce que GLM-5.2 es sólido, lo que lo hace útil para los lectores que desean comparar el escepticismo junto con las afirmaciones de la tabla de clasificación.

Tipo: Límite | Fecha: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Peak-Time Latency Concern](https://x.com/k_matsumaru/status/2067023197166559621) (por [@k_matsumaru](https://x.com/k_matsumaru))

**Utilice este caso para probar la latencia del proveedor antes de cambiar los planes de codificación o enrutar los flujos de trabajo estilo Claude Code a GLM-5.2.**

La publicación japonesa considera el uso de GLM-5.2 dentro de un plan de codificación, pero señala preocupaciones previas sobre la latencia de respuesta en horas pico.

Tipo: Límite | Fecha: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [FutureSim Non-Improvement Result](https://x.com/nikhilchandak29/status/2066970561511657913) (por [@nikhilchandak29](https://x.com/nikhilchandak29))

**Utilice este caso para comprobar si las ganancias de codificación se generalizan a dominios que no son de codificación antes de una implementación amplia.**

La publicación informa que GLM-5.2 no es mejor que GLM-5.1 en FutureSim y utiliza el resultado para advertir que las mejoras en la codificación pueden no generalizarse por igual en todos los dominios.

Tipo: Límite | Fecha: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Launch Readiness Critique](https://x.com/bridgemindai/status/2065770088821600512) (por [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para separar la capacidad del modelo de la ejecución del lanzamiento, la documentación y la preparación de la API.**

La publicación califica el lanzamiento anticipado como complicado porque los puntos de referencia y el acceso a la API aún no estaban disponibles en ese momento, lo que lo hace relevante para la revisión de la preparación para el lanzamiento en lugar de para juzgar la calidad del modelo.

Tipo: Límite | Fecha: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [Aumento del precio del plan de codificación](https://x.com/bridgemindai/status/2065799843658793092) (por [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para verificar el precio del plan antes de recomendar GLM-5.2 como reemplazo de bajo costo.**

El autor informa que paga $65 por mes por un plan GLM Coding Pro y dice que el plan casi se ha duplicado desde su última suscripción. Úselo como recordatorio para verificar los precios actuales.

Tipo: Límite | Fecha: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [Trabajo paralelo corto versus tiradas largas de agentes](https://x.com/thekuchh/status/2068010332501479865) (por [@thekuchh](https://x.com/thekuchh))

**Utilice este caso para dirigir GLM-5.2 hacia tareas de codificación limitadas cortas y, al mismo tiempo, reservar modelos más potentes para ejecuciones de agentes más profundas de varias horas.**

La publicación informa una división práctica: GLM-5.2 funciona bien para tareas paralelas cortas, pero falla en una ejecución de agente más larga.

Tipo: Límite | Fecha: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [HalluHard Multiturn Hallucination Signal](https://x.com/dyfan22/status/2069335764295438532) (por [@dyfan22](https://x.com/dyfan22))

**Usa este caso para probar GLM-5.2 en tareas multiturno sensibles a las alucinaciones antes de confiar en puntuaciones fuertes de benchmark en otros frentes.**

HalluHard añadió GLM-5.2 a su leaderboard usando adaptive thinking con máximo reasoning effort. La actualización dice que, pese a sus buenos resultados en otros benchmarks, GLM-5.2 sigue alucinando con frecuencia en el exigente benchmark multiturno de HalluHard.

Tipo: Límite | Fecha: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Open-Weight Security Emergency Warning](https://x.com/joshua_saxe/status/2069289170107842572) (por [@joshua_saxe](https://x.com/joshua_saxe))

**Usa este caso como señal para planificar seguridad: GLM-5.2 open-weight reduce la fricción operativa para agentes ofensivos de seguridad incluso cuando las APIs cerradas siguen monitorizadas.**

Joshua Saxe argumenta que GLM-5.2 elimina gran parte de la fricción de monitorización y cuentas que antes limitaba a los atacantes que usaban agentes frontier de coding. El hilo presenta los pesos abiertos junto con el despliegue privado como un cambio serio en la capacidad ofensiva y pide acelerar la adopción defensiva en lugar de confiar en el gatekeeping por API.

Tipo: Límite | Fecha: 2026-06-23

---

<a id="case-73"></a>
### Case 73: [Comprobación de censura en código y sesgo](https://x.com/wongmjane/status/2068424945663893936) (por [@wongmjane](https://x.com/wongmjane))

**Usa este caso como una señal práctica de seguridad para pruebas de código y sesgo político, no como prueba de que las preocupaciones de alineación más amplias ya estén resueltas.**

La autora dice que GLM-5.2 no introdujo censura política china en el código y que, por separado, corrigió una afirmación falsa de sesgo estadounidense sobre la guerra de Vietnam mientras dejaba intactos casos más parecidos a opiniones. Eso lo convierte en un ejemplo público concreto para probar comportamiento de código políticamente sensible y factualidad.

Tipo: Límite | Fecha: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [Fallo de facturación en razonamiento difícil](https://x.com/s_batzoglou/status/2068297051247350154) (por [@s_batzoglou](https://x.com/s_batzoglou))

**Usa este caso para probar GLM-5.2 con cuidado en cargas de razonamiento difíciles, porque el informe público muestra tiempos largos, baja finalización y una facturación inesperadamente alta.**

El autor ejecutó 11 problemas de inducción y reporta solo cuatro finalizaciones, dos respuestas correctas, tiempos de ejecución de varias horas y cargos que parecían muy superiores al conteo visible de tokens. Es una advertencia concreta sobre eficiencia de razonamiento y comportamiento de facturación, no solo sobre puntuaciones de benchmark.

Tipo: Límite | Fecha: 2026-06-20

---


<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio se inspiró en creadores, desarrolladores, equipos de referencia, proveedores y comunidades públicos que compartieron evidencia real del uso de GLM-5.2.

Gracias a estos creadores y fuentes de alta señal representados aquí: [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan).

Creadores añadidos recientemente: [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb).

*If any attribution needs to be corrected, please contact us and we will update it.*

Contributions with concrete GLM-5.2 use cases are welcome through issues and pull requests.

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-glm-5.2-usecases&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
