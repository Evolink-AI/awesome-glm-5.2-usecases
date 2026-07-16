<div align="center">

<a href="https://evolink.ai/glm-5-2?utm_source=github&utm_medium=banner&utm_campaign=awesome-glm-5.2-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/en.jpg" alt="Repositorio de casos de uso de GLM-5.2 banner" width="760"></a>

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

# Repositorio de casos de uso de GLM-5.2

## 🍌 Introducción

Bienvenido al repositorio de casos de uso de alta señal de GLM-5.2.

**Recopilamos casos reales, tutoriales, integraciones, evaluaciones, señales de precio y limitaciones de GLM-5.2 a partir de demos públicas y comunidades de creadores.**

Este README localizado mantiene casos con flujos concretos, evidencia pública de benchmarks, demos prácticas, integraciones, costes o advertencias útiles.

Cada título de caso enlaza a su fuente pública y cada usuario enlaza al perfil del creador.

[Probar GLM-5.2 en Evolink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases&utm_content=introduction_cta)

## 📊 Resumen

- **226 casos seleccionados de GLM-5.2** de creadores públicos, equipos de benchmarks, desarrolladores de herramientas, proveedores y usuarios prácticos.
- Cubre evaluaciones comparativas y evaluación de frontera, agentes de código y flujos de contexto largo, demos prácticas y muestras, integraciones de proveedores y herramientas, coste, precios y despliegue local, límites, advertencias y señales de seguridad.
- Cada caso incluye la fuente original, la atribución del creador, un takeaway de uso conciso, el tipo de evidencia y la fecha de publicación.
- Usa este repo para encontrar flujos prácticos, comparar fortalezas y límites, descubrir rutas de proveedor y seguir experimentos reales.

> [!NOTE]
> La colección prioriza evidencia concreta sobre hype: demos publicadas, métodos de benchmark, notas de integración, datos de coste y caveats claros.

> [!NOTE]
> Los README localizados conservan el mismo orden de casos, enlaces, anchors y atribución que la fuente inglesa. Algunos títulos se mantienen cerca del idioma original para mejorar la trazabilidad.

<a id="quick-start"></a>
## ⚡ Quick Start

[Abrir GLM-5.2 en EvoLink](https://evolink.ai/glm-5-2?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=model_link).

Usa GLM-5.2 mediante la API Chat Completions compatible con OpenAI de Evolink. Obtén una API key en [Obtén tu clave API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-glm-5.2-usecases&utm_content=api_key) y configúrala como `EVOLINK_API_KEY` antes de ejecutar la solicitud.

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

Lee la referencia completa de la API GLM-5.2: [Abrir documentación de la API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run).

## 📑 Menú

| Sección | Casos |
|---|---|
| [📏 Evaluaciones comparativas y evaluación de frontera](#benchmarks-frontier-evaluation) | Case 1-12, 60, 70, 72, 76, 90, 94, 110-111, 113, 120-121, 146, 154, 159, 162, 167, 175, 178, 184, 188-190, 196, 199, 207, 217, 223 |
| [💻 Agentes de código y flujos de contexto largo](#coding-agents-long-context-workflows) | Case 13-22, 62, 65, 66, 77, 80, 91, 102, 117, 119, 122, 127, 135-136, 142-143, 145, 148, 150, 153, 155, 168, 174, 180, 194, 210-212 |
| [🎮 Demos prácticas y muestras](#hands-on-demos-showcase-builds) | Case 23-30, 71, 78, 81-82, 92, 99-100, 123, 144, 158, 161, 192, 200, 202, 213, 218 |
| [🔌 Integraciones de proveedores y herramientas](#provider-tool-integrations) | Case 31-42, 61, 63, 69, 74, 79, 83-87, 93, 95-96, 101, 104-105, 109, 115-116, 124-125, 128-130, 137, 141, 147, 152, 160, 165, 169-170, 176, 179, 185, 193, 195, 198, 201, 203-204, 208, 214, 219-220, 224-225 |
| [💸 Coste, precios y despliegue local](#cost-pricing-local-deployment) | Case 43-51, 64, 68, 88-89, 97-98, 106-107, 112, 118, 131, 138-140, 151, 156, 164, 166, 171-173, 177, 181-183, 186-187, 191, 206, 209, 215, 221, 226 |
| [🧭 Límites, advertencias y señales de seguridad](#limits-caveats-safety-signals) | Case 52-59, 67, 73, 75, 103, 108, 114, 126, 132-134, 149, 157, 163, 197, 205, 216, 222 |
| [Repositorios relacionados](#related-repositories) | Ruta API verificada y superficies adyacentes |
| [🙏 Agradecimientos](#acknowledge) | Créditos y política de correcciones |

### [📏 Evaluaciones comparativas y evaluación de frontera](#benchmarks-frontier-evaluation)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 223: Brecha de eficiencia de tokens en el Intelligence Index](#case-223) | Usa este caso para presupuestar GLM-5.2 en cargas de benchmark de largo horizonte, porque Artificial Analysis dice que GLM-5.2 Max promedió unos 43K output tokens por tarea del Intelligence Index frente a 25K de Inkling y cifras menores de Kimi K2.6 y DeepSeek v4 Pro Max. | Evaluation |
| [Case 217: Ruta de rescate EvalPlus supera a Fable](#case-217) | Usa este caso para probar una ruta de coding con dos modelos y verificador, porque gmi_cloud dice que Opus 4.8 primero y GLM 5.2 FP8 como rescate resolvieron 94 de 100 tareas congeladas de EvalPlus, cinco más que Fable 5, con un coste alrededor de 47 por ciento menor. | Evaluación |
| [Case 207: Comparativa del navegador de fluidos estables](#case-207) | Usa este caso para comparar GLM-5.2 en builds de física para navegador cargados de algoritmo, porque AlicanKiraz0 ejecutó un benchmark HTML de Stable Fluids y dio a GLM 5.2 Max un 88 sobre 100 por unos 1,17 dólares, por delante de Opus 4.8 y Fable 5 pero por detrás de GPT 5.6 Sol. | Evaluation |
| [Case 199: Plomo del índice de peso abierto de época](#case-199) | Usa este caso para ubicar GLM-5.2 en una curva de capacidad de largo plazo, porque Epoch AI estima una puntuación de 152 en su Capabilities Index y lo llama el mejor open weight de su conjunto evaluado. | Benchmark |
| [Case 196: Evaluación de arnés interno de Databricks](#case-196) | Usa este caso para benchmarkear GLM-5.2 sobre una gran codebase privada de ingeniería, porque Databricks dice que su evaluación interna sobre trabajo de más de 3.000 engineers mostró que GLM 5.2 rindió muy bien y que solo elegir mejor el harness puede recortar el coste alrededor de 2x. | Evaluation |
| [Case 190: Subcampeón de peso abierto NatureBench](#case-190) | Usa este caso para benchmarkear GLM-5.2 en trabajo de agentes científicos, porque NatureBench dice que GLM-5.2 debutó como número dos global y lideró a los open weights en 90 tareas de seis dominios científicos. | Benchmark |
| [Case 189: Compensación de costos de 45 tareas entre terminal y banco](#case-189) | Usa este caso para comparar GLM-5.2 con GPT-5.5 en el mismo harness de agente, porque una corrida de 45 tareas de Terminal-Bench dejó a GLM-5.2 con 25 aciertos frente a 29 de GPT-5.5, con cerca de 40% menos coste usando prompt caching. | Evaluation |
| [Case 188: Harvey LAB-AA Vinculación de agente legal](#case-188) | Usa este caso para benchmarkear GLM-5.2 en trabajo real de agentes legales, porque Harvey LAB-AA sitúa a GLM-5.2 Max en 7,5% de all-pass, empatado con Claude Opus 4.8 en 120 tareas privadas de 24 áreas legales. | Benchmark |
| [Case 184: Líder de pesas abiertas AutomationBench-AA](#case-184) | Usa este caso para comparar GLM-5.2 en automatización SaaS con reglas de negocio y no solo en benchmarks de código, porque Artificial Analysis reporta 27,8% para GLM-5.2 Max y lo llama el mejor modelo open weights en AutomationBench-AA. | Evaluation |
| [Case 178: Victoria en el punto de referencia del simulador de tres cuerpos](#case-178) | Usa este caso para comparar GLM-5.2 en benchmarks de programación con física numérica, porque AlicanKiraz0 ejecutó una tarea caótica de simulador de tres cuerpos y dio a GLM 5.2 Max la mejor nota con 91 sobre 100. | Evaluation |
| [Case 167: GameDevBench 333-Tarea Líder de código abierto](#case-167) | Usa este caso para seguir GLM-5.2 en benchmarks de desarrollo de juegos agentic, porque GameDevBench se amplió a 333 tareas y dice que GLM-5.2 ya es el modelo open-source más fuerte de su leaderboard pese a no tener visión. | Evaluation |
| [Case 175: Cuadro de mando de doble péndulo del cursor](#case-175) | Usa este caso para comparar GLM-5.2 en un benchmark de coding dentro de Cursor con una tarea acotada, porque AlicanKiraz0 probó seis modelos sobre un simulador HTML de doble péndulo y dio a GLM 5.2 Max 88 sobre 100, detrás de Fable y Sonnet pero por delante de GPT-5.5, Kimi K2.7 Code y Composer. | Evaluation |
| [Case 162: VulcanBench 10 tareas 80 por ciento empatado](#case-162) | Usa este caso para comparar GLM-5.2 en tareas de ingeniería reales y fuera de cutoff donde el coste importa tanto como la puntuación, porque Morgan Linton dice que VulcanBench dio a GLM 5.2 High, Fable 5 Low y Sonnet 5 High el mismo 80 por ciento en 10 repos, mientras GLM quedó en el medio por coste. | Evaluation |
| [Case 159: Punto de control del 51,1 por ciento de SWE-Rebench](#case-159) | Use este caso para seguir GLM-5.2 en una tabla SWE agent que se actualiza continuamente, porque la última publicación de SWE rebench reporta 51,1 por ciento con 2,62 millones de tokens, claramente por delante de las nuevas ejecuciones de DeepSeek, MiMo, Qwen y Gemma. | Evaluation |
| [Case 154: LaunchDarkly Edge-Case gana con 40/41](#case-154) | Use este caso para probar GLM-5.2 en trabajo de agentes con herramientas empresariales en lugar de evaluaciones de solo chat, porque Composio reporta 40 de 41 en tareas con GitHub, Jira y LaunchDarkly y dice que GLM fue el único modelo que detectó un caso límite de aprobación pendiente. | Evaluation |
| [Case 146: Subcampeón del parche de peso abierto CyberBench](#case-146) | Usa este caso para medir a GLM-5.2 en búsqueda y parcheo de vulnerabilidades de estilo ofensivo, porque CyberBench lo sitúa segundo en 60 vulnerabilidades reales de OSS-Fuzz. | Evaluation |
| [Case 1: Índice de Inteligencia de Análisis Artificial](#case-1) | Utilice la publicación de Análisis artificial para comparar GLM-5.2 con otros modelos de frontera patentados y de peso abierto en materia de inteligencia y costo por tarea. | Benchmark |
| [Case 2: Clasificación de interfaz de Code Arena](#case-2) | Utilice este caso para evaluar GLM-5.2 en tareas reales de codificación front-end juzgadas mediante comparaciones de estilo arena. | Benchmark |
| [Case 3: Primer lugar en Design Arena](#case-3) | Utilice este caso para juzgar si GLM-5.2 puede manejar tareas de diseño más código en lugar de solo pruebas comparativas de codificación con mucho texto. | Benchmark |
| [Case 4: Resultado de FrontierSWE](#case-4) | Utilice la publicación de FrontierSWE para comparar GLM-5.2 con los modelos GPT-5.5, Opus y Fable en tareas de ingeniería de software. | Benchmark |
| [Case 5: Líder de código abierto de DeepSWE](#case-5) | Utilice el caso de DeepSWE para comprender GLM-5.2 como un modelo abierto sólido para tareas difíciles de evaluación de ingeniería de software. | Benchmark |
| [Case 6: Banco de terminales superior al 80 por ciento](#case-6) | Utilice este caso al evaluar GLM-5.2 para flujos de trabajo de agentes y codificación orientados a terminales. | Benchmark |
| [Case 7: Comparación de SWELancer con GPT-5.5](#case-7) | Utilice este caso de SWELancer como una comparación multimétrica concreta entre GLM-5.2 y GPT-5.5 sobre el éxito de la tarea, la recompensa y el tiempo de finalización. | Evaluation |
| [Case 8: Señal de puntuación perfecta BridgeBench](#case-8) | Utilice este caso para inspeccionar GLM-5.2 sobre un razonamiento fundamentado de varios pasos en lugar de solo codificar tablas de clasificación. | Benchmark |
| [Case 9: BridgeBench Razonamiento número uno](#case-9) | Utilice este caso para comparar GLM-5.2 con modelos de frontera cerrada en tareas de razonamiento fundamentado. | Benchmark |
| [Case 10: KernelBench-Hard sin atajos](#case-10) | Utilice este caso para comprobar si las ganancias de referencia provienen de un comportamiento de implementación válido en lugar de atajos. | Evaluation |
| [Case 11: Actualización del banco de Runescape](#case-11) | Utilice este caso como una señal rápida para el progreso del modelo de peso abierto en tareas de referencia similares a las de un juego. | Benchmark |
| [Case 12: Mejora de la velocidad de BridgeBench](#case-12) | Utilice este caso para evaluar flujos de trabajo sensibles a la latencia donde la velocidad importa junto con la inteligencia. | Benchmark |
| [Case 60: Codificación KernelBench Hard y Mega GPU](#case-60) | Utilice este caso para evaluar GLM-5.2 en la codificación del kernel de GPU en KernelBench-Hard y KernelBench-Mega, donde los rastros de agentes abiertos hacen que el resultado sea inspeccionable. | Benchmark |
| [Case 70: Liderazgo open-source en DeepSWE con esfuerzo máximo](#case-70) | Usa este caso para seguir a GLM-5.2 en DeepSWE con esfuerzo máximo, donde la tabla publicada lo sitúa primero entre los modelos abiertos con una puntuación pass@1 del 44%. | Benchmark |
| [Case 72: Segundo puesto en benchmark de debates LLM](#case-72) | Usa este caso para evaluar GLM-5.2 más allá del código en debates adversariales de varios turnos, donde la variante de razonamiento máximo quedó segunda detrás de modelos Claude. | Benchmark |
| [Case 76: Tasa de alucinación en AA-Omniscience](#case-76) | Usa este caso para comparar GLM-5.2 en manejo de incertidumbre, donde el resultado publicado de AA-Omniscience muestra una tasa de alucinación menor que la de varios otros modelos frontier. | Evaluation |
| [Case 90: Índice de Trabajo Agentic GDPval-AA](#case-90) | Usa este caso para comparar GLM-5.2 en trabajo de conocimiento de largo horizonte, en lugar de limitarte a rankings centrados solo en código. | Evaluation |
| [Case 94: Subcampeón de Game Dev Arena](#case-94) | Usa este caso para juzgar la calidad de GLM-5.2 en creación de juegos, donde el modelo alcanzó el segundo puesto en Game Dev Arena y se convirtió en el laboratorio open-weight mejor clasificado en ese ranking. | Evaluation |
| [Case 120: Líder de confiabilidad PostTrainBench](#case-120) | Usa este caso para comparar GLM-5.2 Max en fiabilidad de agentes post-training, no solo por la puntuación principal, porque la tabla también informa cero ejecuciones fallidas en 84 tareas. | Benchmark |
| [Case 121: Fuegos artificiales + Evaluación del repositorio de tareas 211 de Faros](#case-121) | Usa este caso para juzgar GLM-5.2 en tareas reales de ingeniería sobre repos privados en lugar de depender solo de benchmarks públicos, porque el resultado publicado incluye puntuación, velocidad y coste por tarea. | Evaluation |
| [Case 110: Frontera de tiempo por tarea del maletín AA](#case-110) | Usa este caso para comparar GLM-5.2 en tareas de conocimiento de largo horizonte donde el tiempo por tarea importa junto con la puntuación del benchmark. | Benchmark |
| [Case 111: Márgenes cara a cara del frontend de Code Arena](#case-111) | Usa este caso para inspeccionar la ventaja de GLM-5.2 en frontend mediante resultados cara a cara por pares en lugar de depender de una sola captura de clasificación. | Benchmark |
| [Case 113: Subcampeón de QnA de SWE Atlas Codebase](#case-113) | Usa este caso para seguir a GLM-5.2 en Codebase QnA, redacción de pruebas y refactorización en lugar de mirar solo clasificaciones SWE de una sola tarea. | Benchmark |

### [💻 Agentes de código y flujos de contexto largo](#coding-agents-long-context-workflows)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 168: Conjunto Synthwave Hard-Slice a $ 2,66](#case-168) | Usa este caso para probar GLM-5.2 dentro de un ensemble de coding multi-modelo en vez de usarlo solo, porque TracNetwork informa que una mezcla de Synthwave con GLM logró 46.3 por ciento en LiveCodeBench hard por unos 2.66 dólares y superó a cada generador por separado. | Integration |
| [Case 212: Tutorial Dell Hub GLM Agent](#case-212) | Usa este caso si quieres montar un coding agent con GLM-5.2 para un workflow de entrenamiento open-weight, porque juanjucm enlazó una guía nueva que combina la llegada de GLM-5.2-FP8 al catálogo de Dell Enterprise Hub con un recorrido paso a paso para construir un agent alrededor de ese modelo. | Tutorial |
| [Case 211: Pipeline de informes open-weight con 8xB200](#case-211) | Usa este caso si quieres poner GLM-5.2 como redactor principal dentro de un pipeline de informes cercano al despliegue local, porque TheZachMueller dice que dividir un nodo 8xB200 en 4/4 le permitió usar GLM 5.2 NVFP4 para redactar y Kimi K2.7 Code para retrieval, sacando un informe de 36 páginas por una fracción del coste de Claude API. | Demo |
| [Case 210: Renovación multiagente Liquid Glass de Spettro](#case-210) | Usa este caso para probar GLM-5.2 como solucionador de frontend con mucha investigación dentro de una renovación web multiagente, porque spettrotoken dice que GLM 5.2 usó herramientas integradas de web scraping y data fetching para entregar una implementación cross-browser de Liquid Glass que funcionó en Firefox después de que Fable 5 y GPT-5.5 fallaran. | Demo |
| [Case 194: Habilidad del kernel CuTeDSL de código abierto](#case-194) | Usa este caso para estudiar GLM-5.2 dentro de una skill reutilizable de depuración de kernels, porque el autor liberó una skill de Hermes para CuTeDSL y dice que GLM-5.2 fue especialmente eficiente en coste al depurar y escribir kernels. | Tutorial |
| [Case 180: Bucle de habilidades de recuperación de SSD de Hermes](#case-180) | Usa este caso para probar GLM-5.2 dentro de un loop de agente orientado a reparación, porque ShankhadeepSho1 dice que Hermes más GLM 5.2 diagnosticó un SSD fallido de un NAS, arregló el problema y empaquetó la solución como una skill reutilizable. | Demo |
| [Case 174: Pila de codificador de servicio pesado enrutado por roles](#case-174) | Usa este caso para asignar GLM-5.2 como coder pesado dentro de una pila personal con routing por roles, porque denizirgin dice que un mes de pruebas con Codex y OpenCode le llevó a enviar el trabajo de coding más pesado a GLM 5.2 manteniendo el presupuesto mensual total en unos 120 a 140 dólares. | Evaluation |
| [Case 155: Bucle TUI de cuatro agentes de Cotal](#case-155) | Use este caso para dividir un bucle de codificación entre agentes especializados, porque el autor usó dos workers con GLM-5.2 bajo un líder Opus y un revisor GPT para terminar una TUI estilo lazygit en 47 minutos sin intervención humana. | Demo |
| [Case 153: Piloto de reducción de costos de migración heredada](#case-153) | Use este caso para valorar GLM-5.2 como el trabajador más barato dentro de una modernización de aplicaciones heredadas, porque el piloto de 8090 dice que GLM más Software Factory redujo el costo 16,4 veces frente a Opus 4.8 solo, aunque fue unas 3 veces más lento. | Evaluation |
| [Case 150: Bucle local para uso del navegador Mac Studio](#case-150) | Usa este caso para probar si una pila totalmente local de GLM-5.2 puede hacer trabajo ligero de browser agent en hardware de consumo, porque el autor ejecutó llama.cpp en un Mac Studio y usó browser-use para encontrar un modelo de PII en Hugging Face. | Demo |
| [Case 148: Reducción de costos de intercambio de agentes de Gumloop](#case-148) | Usa este caso para probar una sustitución directa de modelo dentro de un harness existente, porque Gumloop dice que movió sus agentes más usados a GLM-5.2 con cerca de 50% menos créditos y sin caída visible de calidad. | Evaluation |
| [Case 13: Bucle de refactorización de una hora cuarenta y dos minutos](#case-13) | Utilice este caso como patrón para una refactorización frontal autónoma prolongada con TDD, comentarios de los revisores y comprobaciones de regresión. | Demo |
| [Case 14: Prueba de implementación y corrección de errores de OpenCode](#case-14) | Utilice este caso para probar GLM-5.2 como agente de codificación OpenCode para corregir errores además de una pequeña tarea de implementación. | Demo |
| [Case 15: Tutorial del videojuego OpenCode Retro](#case-15) | Utilice este tutorial para crear un juego pequeño con GLM-5.2 y OpenCode desde un solo mensaje y luego inspeccione cómo el modelo maneja los detalles de implementación. | Tutorial |
| [Case 16: Concurso de Simulaciones de Física HTML5](#case-16) | Utilice este caso para comparar el código GLM-5.2 y Kimi K2.7 en simulaciones de física HTML5 autónomas sin bibliotecas. | Evaluation |
| [Case 17: Creación de UX de interfaz de usuario de sitio personal](#case-17) | Utilice este caso para solicitar a GLM-5.2 un sitio personal pulido e inspeccionar hasta qué punto múltiples turnos pueden mejorar la UI/UX. | Demo |
| [Case 18: Creación de productos de revisión de contratos de IA](#case-18) | Utilice este caso para evaluar GLM-5.2 en una tarea de creación de productos con un PRD, presupuesto de tiempo, recuento de pasos, cuota de uso y comparación de calidad del código. | Evaluation |
| [Case 19: Función de objetivo de ZCode para objetivos de desarrollo más amplios](#case-19) | Utilice este caso para comprender cómo se integra GLM-5.2 en ZCode 3.0 para tareas de desarrollo agente más grandes. | Integration |
| [Case 20: Envoltorio de Linux para ZCode creado con GLM-5.2](#case-20) | Utilice este caso como ejemplo de cómo GLM-5.2 ayuda con herramientas en entornos de agentes de codificación. | Demo |
| [Case 21: Empaquetado de habilidades para el uso de la computadora](#case-21) | Utilice este caso para estudiar GLM-5.2 como ayuda para convertir un repositorio de uso de computadora de código abierto en una habilidad reutilizable. | Demo |
| [Case 22: Revisión del entorno de desarrollo agente ZCode 3.0](#case-22) | Utilice este caso para evaluar GLM-5.2 dentro de un entorno de desarrollo agente completo en lugar de una única sesión de chat. | Demo |
| [Case 62: Arnés OpenCode con servicio local](#case-62) | Utilice este caso para probar GLM-5.2 con el arnés OpenCode, el servicio local y los flujos de trabajo de codificación con muchas herramientas antes de compararlo con Claude Opus. | Evaluation |
| [Case 65: Inyección de instrucciones de contexto largo Fast-RLM](#case-65) | Utilice este caso para mejorar el recuento de contexto largo de GLM-5.2 y el comportamiento del agente REPL moviendo instrucciones al indicador del sistema RLM. | Integration |
| [Case 66: Prueba de arnés abierto de código DeepAgents](#case-66) | Utilice este caso para probar GLM-5.2 con un arnés de agente de codificación abierto y compare el modelo bajo un shell de agente reproducible. | Demo |
| [Case 77: Enrutamiento de stack de agentes de marketing en producción](#case-77) | Usa este caso para enrutar GLM-5.2 a workflows de agentes en producción que valoran estructura, velocidad y self-hosting, manteniendo modelos cerrados más fuertes para juicios ambiguos. | Evaluation |
| [Case 80: Recreación de Pokemon Red en M3 Ultra](#case-80) | Usa este caso para evaluar GLM-5.2 en una ejecución local de agente de código a largo plazo, donde el modelo pasó alrededor de medio día intentando recrear Pokemon Red en HTML en una máquina M3 Ultra. | Demo |
| [Case 91: Enfrentamiento de corrección de errores del repositorio de Cline](#case-91) | Usa este caso para comparar GLM-5.2 y Opus 4.8 en la corrección de un bug de un repositorio real, donde GLM gastó más tokens pero entregó el parche final más barato y más limpio. | Evaluation |
| [Case 102: Agente en segundo plano OpenInspect FP8](#case-102) | Usa este caso para estudiar un stack de agente en segundo plano autoalojado con GLM-5.2 en lugar de un flujo de chat alojado. | Integration |
| [Case 145: Migración de ahorro con OpenCode y Fireworks](#case-145) | Usa este caso para probar si basta con cambiar a un harness de open models, porque el autor movió sus tareas personales de coding y loops a GLM-5.2 sobre Fireworks más OpenCode y dice que la factura de tokens cayó a un tercio sin una pérdida clara de calidad diaria. | Evaluation |
| [Case 143: Flujo con agregador GLM en Hermes MoA](#case-143) | Usa este caso cuando un turno de agente de alto valor justifique más orquestación, porque la configuración Mixture of Agents de Hermes Agent combinó GLM-5.2 con otros modelos y logró una salida visiblemente mejor con un aumento pequeño de coste por tarea en el demo publicado. | Integration |
| [Case 142: Diferencia del harness con reasoning en Cline](#case-142) | Usa este caso para evaluar el diseño del harness y no solo los pesos del modelo, porque el mismo GLM-5.2 pasó de 57.3% a 68.5% en las mismas tareas de coding cuando el harness activó reasoning. | Evaluation |
| [Case 136: Prueba de campo de 455M tokens con Cursor + Fireworks](#case-136) | Usa este caso para juzgar GLM-5.2 como un modelo serio para el uso diario en Cursor, porque el autor informa 455M tokens de uso real con serving rápido de Fireworks y sin ganas inmediatas de volver a Opus o GPT-5.5. | Evaluation |
| [Case 135: Arnés de Devin Desktop con portabilidad de skills](#case-135) | Usa este caso para probar GLM-5.2 dentro de Devin Desktop cuando la propia superficie de coding de Z.ai se sienta inestable, porque el autor informa portabilidad de skills más fácil, mayor velocidad y mejor capacidad de hackeo. | Evaluation |
| [Case 127: Revisor GLM en línea de Pi](#case-127) | Usa este caso para añadir un segundo revisor a un loop de agente de código estilo Pi, porque el autor informa que GLM-5.2 puede asesorar a Opus turno a turno por un aumento de coste de alrededor del 10%. | Integration |
| [Case 122: Bot de Telegram de un solo uso con AgentRouter](#case-122) | Usa este caso para probar si GLM-5.2 puede inferir decisiones orientadas a producción en una build one-shot con agente de código, en lugar de limitarse a generar el camino mínimo que funciona. | Demo |
| [Case 117: Ganancia del primer paso de OpenCode Go Refactor](#case-117) | Usa este caso para evaluar GLM-5.2 en refactorizaciones medianas de Go dentro de OpenCode en lugar de apoyarte solo en afirmaciones de benchmark. | Evaluation |
| [Case 119: Código Claude + Cursor $3.36 Ejecución predeterminada](#case-119) | Usa este caso para medir GLM-5.2 como modelo diario en Claude Code y Cursor antes de mover más trabajo autónomo de programación a pesos abiertos. | Evaluation |

### [🎮 Demos prácticas y muestras](#hands-on-demos-showcase-builds)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 218: Rebuild de portfolio y SO con OpenCode](#case-218) | Usa este caso para medir GLM-5.2 en builds ambiciosas con OpenCode, porque MarkSShenouda dice que OpenCode Go más GLM-5.2 ayudó a rehacer un sitio de portfolio y un sistema operativo real escrito en C y Assembly que corre en WASM o en un emulador Qemu. | Demostración |
| [Case 213: Reconstrucción GLM de LlamaCoder v4](#case-213) | Usa este caso si quieres prototipar un workflow de generación de apps con un solo prompt apoyándote en las fortalezas de GLM-5.2 para planning y diseño, porque nutlope dice que LlamaCoder v4 fue rehecho alrededor de GLM 5.2, mejoró parsing y planning y ahora entrega un renderer WebAssembly dentro de un stack gratuito y open source. | Demo |
| [Case 202: Función de disparo espacial con código de comando](#case-202) | Usa este caso para comparar GLM-5.2 en builds de UI interactiva de un solo prompt, porque Command Code ejecutó el mismo prompt de space shooter retro con Fable 5, GPT 5.5, GLM 5.2 y DeepSeek V4 Pro, y colocó a GLM como el mejor en features por $0.07. | Evaluation |
| [Case 200: Emulador ZCode Nintendo DS](#case-200) | Usa este caso para inspeccionar una build local de coding de largo recorrido, porque el autor ejecutó GLM-5.2 en ZCode sobre 4x RTX 6000 con el objetivo de construir desde cero un emulador de Nintendo DS en C++. | Demo |
| [Case 192: Código de comando Flappy Bird UX Split](#case-192) | Usa este caso para comparar GLM-5.2 en tareas ligeras de diseño y juego, porque el autor pasó el mismo prompt de Flappy Bird por Command Code y concluyó que Fable 5 no fue significativamente mejor en UX pese a costar casi nueve veces más que GLM-5.2. | Evaluation |
| [Case 161: REAP NVFP4 Cubo de Rubik One-Shot](#case-161) | Usa este caso para probar GLM-5.2 en tareas interactivas de construcción con un solo prompt, porque la demo REAP-NVFP4 afirma que un único prompt produjo un cubo de Rubik 3D con scrambles reales, estado en vivo y botón de resolver. | Demo |
| [Case 158: Cliente OMP Relay para iPhone](#case-158) | Use este caso para envolver rápidamente un agente local con GLM-5.2 en una superficie móvil, porque el autor dice que el plugin build-ios-app de Codex produjo en un par de horas un cliente pulido para iPhone sobre un relay OMP que ya usaba GLM-5.2 y túneles de Cloudflare. | Demo |
| [Case 144: Agente open source de investigación DevRel](#case-144) | Usa este caso para convertir GLM-5.2 en un asistente de investigación vertical y no en un chat genérico, porque el autor creó un agente DevRel open source que transforma producto y audiencia en oportunidades de contenido clasificadas con evidencia y esquemas. | Demo |
| [Case 123: Refundido del bucle de página de destino de seis variaciones](#case-123) | Usa este caso para prototipar landing pages de forma barata generando primero varias variantes con GLM-5.2 y llevando luego la mejor a un agente de código. | Tutorial |
| [Case 23: Trastiendas jugables One-Shot](#case-23) | Utilice este caso para comparar el resultado, el tiempo de ejecución y el costo de creación de juegos con el mismo sistema entre GLM-5.2 y Opus 4.8. | Demo |
| [Case 24: Tres construcciones reales con resultados mixtos](#case-24) | Utilice este caso como conjunto de demostración de advertencia: pruebe varias compilaciones reales antes de confiar en un modelo para tareas de producción de juegos o videos. | Evaluation |
| [Case 25: Clon de Super Mario en ZCode](#case-25) | Utilice este caso para evaluar la creación de juegos iterativos con GLM-5.2 y ZCode en varias pasadas de corrección y funciones. | Demo |
| [Case 26: Concurso de módulo de aterrizaje lunar](#case-26) | Utilice este caso para comparar GLM-5.2, MiniMax M3 y Kimi K2.7 Code en una tarea de estilo de juego interactivo. | Evaluation |
| [Case 27: Creación de arena de diseño en un solo momento](#case-27) | Utilice este caso para inspeccionar lo que GLM-5.2 puede generar a partir de un único mensaje de diseño en un contexto de arena. | Demo |
| [Case 28: Trabajo de investigación: comprensión del flujo de trabajo](#case-28) | Utilice este caso para aplicar GLM-5.2 a flujos de trabajo de lectura de artículos con preguntas contextuales y referencias entre artículos. | Integration |
| [Case 29: Comparación de poemas restringida](#case-29) | Utilice este caso para separar la corrección de la calidad creativa al comparar el GLM-5.2 con los modelos estilo Fable. | Evaluation |
| [Case 30: Ejemplo de sentido del diseño](#case-30) | Utilice este caso como una señal de diseño visual liviano y luego verifíquelo con su propio mensaje y revisión de la interfaz de usuario. | Demo |
| [Case 71: Juego voxel estilo Temple Run en un solo intento](#case-71) | Usa este caso para poner a prueba GLM-5.2 en generación de juegos con un solo prompt y luego revisar qué sigue necesitando correcciones iterativas en una build visualmente rica. | Demo |
| [Case 78: Conjunto de ejemplos one-shot en OpenCode Go](#case-78) | Usa este caso para medir GLM-5.2 en builds rápidas de un solo intento dentro de OpenCode Go antes de comprometerlo a loops de agentes más abiertos. | Demo |
| [Case 81: Build de Space Invaders con un solo prompt](#case-81) | Usa este caso para probar GLM-5.2 en la creación de juegos con un solo prompt y ver luego cómo unos pocos pases extra manejan cambios de assets y pulido simple. | Demo |
| [Case 82: Laboratorio de recuperación de OpenCode en un solo intento](#case-82) | Usa este caso para prototipar rápidamente simulaciones interactivas de fallos de agentes, porque el autor informa que obtuvo un recovery lab funcional en un solo intento por unos 3,50 $. | Demo |
| [Case 92: Abrir reconstrucción de URL de referencia de diseño](#case-92) | Usa este caso para probar GLM-5.2 en recreación web guiada por referencias, donde un solo prompt más una URL de origen reprodujeron un sitio con fidelidad casi a nivel de píxel. | Demo |
| [Case 99: Prueba de calidad de costo de Trader Desk](#case-99) | Usa este caso para comparar GLM-5.2 en builds full-stack de UI, donde se acercó al resultado de trading desk más pulido mientras costaba solo una pequeña fracción del mejor resultado. | Evaluation |
| [Case 100: Juego ludita tras la negativa de Claude](#case-100) | Usa este caso para prototipar conceptos de juego sensibles a políticas con GLM-5.2 cuando un modelo cerrado rechaza la solicitud, y luego inspeccionar por ti mismo el resultado jugable. | Demo |

### [🔌 Integraciones de proveedores y herramientas](#provider-tool-integrations)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 170: Acceso gratuito a la API Plug-and-Play de NVIDIA](#case-170) | Usa este caso para probar GLM-5.2 rápido mediante un endpoint alojado sin costo, porque hqmank dice que NVIDIA abrió una ruta API compatible con OpenAI y confirmó que funcionó como un reemplazo plug-and-play. | Integration |
| [Case 169: Ruta del agente de codificación de IA para trabajadores gratuitos](#case-169) | Usa este caso para montar una ruta de GLM-5.2 sin coste para coding agents, porque el tutorial conecta Workers AI con Claude Code, OpenCode, Cursor y Aider mediante el endpoint compatible con OpenAI `cf/zai-org/glm-5.2`. | Tutorial |
| [Case 225: Puente de TogetherLink con el harness de Codex](#case-225) | Usa este caso para ejecutar GLM-5.2 dentro de CLIs de coding agents ya existentes, porque nutlope dice que TogetherLink es un CLI open source que permite a Codex y Claude Code llamar directamente a modelos abiertos como GLM 5.2. | Integration |
| [Case 224: Enrutamiento del Open Model Harness de Vorflux](#case-224) | Usa este caso para llevar GLM-5.2 a una sesión completa de agent sin glue personalizado, porque vorfluxai dice que su Open Model Harness asigna GLM 5.2 a los pasos de design, build y simplify mientras mantiene intacto el resto del flujo de Vorflux. | Integration |
| [Case 220: Agente clínico OpenMed con de-id](#case-220) | Usa este caso para mantener GLM-5.2 dentro de un flujo clínico con privacidad preservada, porque MaziyarPanahi dice que GLM 5.2 planificó, llamó herramientas y escribió la disposición de un caso completo después de que OpenMed eliminó identificadores en local y Gemma 4 manejó la estructura. | Integración |
| [Case 219: Ruta de acceso GLM con USDC en Katana](#case-219) | Usa este caso para exponer GLM-5.2 mediante una ruta pay per request nativa de wallet, porque imgn_ai dice que Katana sirve GLM-5.2 sobre x402 en Base sin cuenta, usando USDC y un llms.txt publicado para integración directa. | Integración |
| [Case 214: Ruta GLM mediante Databricks AI Gateway](#case-214) | Usa este caso si quieres probar una vía gestionada y muy rápida de acceso a GLM-5.2 dentro de agent tooling, porque QCXINT_ mostró un flujo con base URL y token propios de Databricks AI Gateway que expone una ruta de GLM 5.2 aparentemente de 1M de contexto, aunque la identidad exacta del backend sigue sin confirmarse. | Integration |
| [Case 208: Pila de agente de visor molecular abierto](#case-208) | Usa este caso para conectar GLM-5.2 a un flujo abierto de inspección científica, porque MaziyarPanahi combinó GLM-5.2 vía Hugging Face Inference Providers con Qwen3-VL sobre llama.cpp, Mol* y PydanticAI para renderizar y criticar una estructura EGFR más erlotinib con un solo prompt. | Integration |
| [Case 204: Línea base de costos de WANDR de Perplexity Advisor](#case-204) | Usa este caso para estimar la economía de GLM-5.2 dentro de un harness de computer use con routing, porque Perplexity dice que su configuración de GLM 5.2 más advisor marca 2.1x en WANDR frente a 6.1x de Opus, con un coste medio cercano a la mitad en los benchmarks. | Evaluation |
| [Case 203: Enrutamiento de artefactos abiertos de compañeros de trabajo](#case-203) | Usa este caso para llevar GLM-5.2 a workflows empresariales de artifacts, porque Coworker dice que Open Artifacts puede construir docs, decks, PDF, spreadsheets, dashboards y apps mientras su router optimizado reduce el uso de tokens en torno a 5x y sigue ofreciendo GLM 5.2 alojado en EE. UU. | Integration |
| [Case 201: Flujo de trabajo de carga de contexto de DotCode](#case-201) | Usa este caso para dar a GLM-5.2 más contexto de proyecto dentro de una sandbox privada de coding, porque DotCode añadió soporte para GLM 5.2 junto con uploads de screenshots, imágenes, CSV, PDF, source files y zips que alimentan el mismo flujo de filesystem y terminal. | Integration |
| [Case 221: Serving agentic B300 con SGLang TopK-V2](#case-221) | Usa este caso para benchmarkear serving productivo de GLM-5.2 en cargas agent de contexto largo, porque lmsysorg dice que SGLang alcanzó más de 500 tok/s por usuario en 8xB300 con batch size 1 mientras mejoró la interactividad de usuario único entre 18 y 34 por ciento. | Evaluación |
| [Case 215: Ruta llm-d H200 con Prefix-Cache](#case-215) | Usa este caso si quieres benchmarkear la economía de serving gestionado de GLM-5.2 sobre H200, porque RedHat_AI dice que la combinación de Wide EP y prefix-cache routing en llm-d logró más de 90 por ciento de cache reuse, TTFT por debajo de 3 segundos y unos 2 dólares por millón de output tokens en una ruta GLM-5.2 de más de 700B. | Integration |
| [Case 209: Colibri 25 GB de RAM Transmisión escasa](#case-209) | Usa este caso para entender el nuevo suelo práctico del despliegue local de GLM-5.2, porque techNmak explica cómo Colibrì ejecuta el MoE 744B con unos 25 GB de RAM mediante streaming de expertos desde NVMe, aunque la configuración más pequeña solo logra alrededor de 0,05 a 0,1 tok/s. | Demo |
| [Case 206: Rendimiento de producción de SGLang NVFP4](#case-206) | Usa este caso para dimensionar serving productivo de SGLang para GLM-5.2 NVFP4, porque la release oficial de SGLang v0.5.15 dice que ahora alcanza más de 500 tok/s por usuario en 8x B300 y 450 en 4x GB300 con batch size 1. | Evaluation |
| [Case 198: Terminal GLM gratuito Dahl 100M](#case-198) | Usa este caso para probar GLM-5.2 por una ruta OpenAI-compatible sin tarjeta, porque Dahl Inference ofrece 100M de tokens gratis para GLM 5.2 FP8 y explica cómo crear una clave y llamar a `/v1/chat/completions`. | Tutorial |
| [Case 195: Configuración de GLM para terminales gratuitos de NVIDIA](#case-195) | Usa este caso para probar GLM-5.2 en herramientas de código sin self-hosting, porque la fuente describe un flujo de endpoint gratuito de NVIDIA que mete claves API de GLM-5.2 en Claude Code, Cursor o Cline. | Tutorial |
| [Case 193: Ruta de inferencia privada 0G TeeML](#case-193) | Usa este caso para enrutar GLM-5.2 por una vía de proveedor centrada en privacidad, porque 0G dice que GLM 5.2 ya corre en TeeML con prompts sellados dentro de un enclave TEE y con precio por debajo de la ruta oficial. | Integration |
| [Case 185: PR Open-SQL de DuckDB Flock](#case-185) | Usa este caso para llevar GLM-5.2 a un análisis SQL local totalmente abierto, porque lhoestq dice que un PR de duckdb más flock ya habilita GLM-5.2 dentro de un stack de datos 100% open source. | Integration |
| [Case 179: Acceso API de 26 modelos con una sola clave](#case-179) | Usa este caso para probar GLM-5.2 a través de un único proveedor compatible con OpenAI, porque Alan_Earn dice que una sola API key expone GLM-5.2 más otros 25 modelos e incluye 26 dólares de crédito inicial. | Tutorial |
| [Case 176: Configuración de pensamiento NVIDIA NIM OpenCode](#case-176) | Usa este caso para conectar GLM-5.2 a OpenCode a través del endpoint gratuito de NVIDIA NIM cuando quieras una ruta sin coste con thinking activado de forma explícita, porque Dracoshowumore comparte el flujo de API key, la base URL y una configuración de OpenCode donde la capa de herramientas gestiona las function calls mientras GLM corre con enable_thinking en true. | Tutorial |
| [Case 165: Lanzamiento de ZCode con control de agente móvil](#case-165) | Usa este caso para evaluar ZCode como superficie oficial de coding para GLM-5.2, porque el reporte de lanzamiento dice que el IDE agentic gratuito llega a Windows, macOS y Linux y puede seguir proyectos mediante Telegram, WeChat y Feishu. | Integration |
| [Case 160: Documentos del agente de mantenimiento automático de OpenWiki](#case-160) | Usa este caso para mantener al día documentación legible por agentes automáticamente, porque LangChain dice que OpenWiki regenera y mantiene los docs del repo a medida que cambia el código y funciona sobre modelos abiertos como GLM 5.2. | Integration |
| [Case 152: PTU de fundición a través de FireConnect](#case-152) | Use este caso para enrutar GLM-5.2 mediante presupuestos empresariales de Foundry sin reescribir clientes de agentes, porque Fireworks dice que FireConnect conecta las PTU de Microsoft Foundry con flujos en Codex, OpenCode y Pi. | Integration |
| [Case 147: Banco de trabajo de evaluación Braintrust GLM](#case-147) | Usa este caso para comparar GLM-5.2 y Opus dentro de una misma pila de evals, porque Braintrust y Baseten lo lanzaron con un ejemplo concreto de coste frente a precisión en contexto largo. | Integration |
| [Case 141: Suscripción plana ClinePass para modelos open-weight](#case-141) | Usa este caso para reunir varios modelos de coding open-weight en un solo agent harness, porque ClinePass empaqueta GLM-5.2 y modelos relacionados bajo una tarifa mensual fija en lugar de claves y paneles de cobro separados por proveedor. | Integration |
| [Case 137: Servicio gratuito de API GLM para agentes de código](#case-137) | Usa este caso para probar GLM-5.2 en Hermes u otros agentes de código sin registro, porque el servicio compartido emite API keys de corta duración y mantiene la configuración ligera. | Integration |
| [Case 31: Disponibilidad de OpenCode Go](#case-31) | Utilice este caso para realizar un seguimiento de la disponibilidad de GLM-5.2 dentro de los flujos de trabajo de OpenCode Go con texto, contexto de 1 millón y precios similares a GLM-5.1. | Integration |
| [Case 32: Disponibilidad de la nube de Ollama](#case-32) | Utilice este caso para enrutar GLM-5.2 a Ollama Cloud para realizar experimentos de modelos de codificación de código abierto accesibles. | Integration |
| [Case 33: Acceso a llamadas API de OpenRouter One](#case-33) | Utilice este caso para acceder a GLM-5.2 a través de OpenRouter al comparar enrutamiento de proveedores o pilas multimodelo. | Integration |
| [Case 34: Soporte de día cero de vLLM](#case-34) | Utilice este caso para autohospedar o servir GLM-5.2 a través de vLLM con soporte de día cero. | Integration |
| [Case 35: Disponibilidad de nociones a través de Baseten](#case-35) | Utilice este caso para identificar GLM-5.2 como un modelo de peso abierto disponible dentro de los flujos de trabajo de Notion. | Integration |
| [Case 36: Servicio de fuegos artificiales del día cero](#case-36) | Utilice este caso para evaluar Fireworks como ruta de servicio para cargas de trabajo GLM-5.2 que necesitan una infraestructura alojada. | Integration |
| [Case 37: Enlace al jardín modelo de Google Cloud](#case-37) | Utilice este caso para encontrar GLM-5.2 en contextos de plataforma de agentes y de implementación orientados a Google Cloud. | Integration |
| [Case 38: Modo de privacidad de Venecia](#case-38) | Utilice este caso cuando el modo de privacidad, TEE o cifrado de extremo a extremo sea un factor decisivo al probar GLM-5.2. | Integration |
| [Case 39: Disponibilidad del código de comando](#case-39) | Utilice este caso para probar GLM-5.2 en Command Code con un plan inicial de bajo costo y funciones de codificación de contexto largo. | Integration |
| [Case 40: Agente Hermes De Nous Portal](#case-40) | Utilice este caso para conectar GLM-5.2 a los flujos de trabajo del Agente Hermes a través de Nous Portal y OpenRouter. | Integration |
| [Case 41: Socio de lanzamiento del día cero de io.net](#case-41) | Utilice este caso al evaluar el servicio respaldado por computación para un modelo de contexto largo de parámetros 753B. | Integration |
| [Case 42: Servicio de día cero en la nube modular](#case-42) | Utilice este caso para considerar Modular Cloud para el servicio GLM-5.2 de contexto prolongado a escala de proveedor. | Integration |
| [Case 61: Configuración del cursor a través de OpenRouter](#case-61) | Utilice este caso para configurar GLM-5.2 en Cursor a través de OpenRouter para un flujo de trabajo de codificación de modelo abierto de bajo costo. | Tutorial |
| [Case 63: Amp Agentic ojos para el diseño visual](#case-63) | Utilice este caso para emparejar GLM-5.2 con agentes personalizados de Amp cuando un modelo de solo texto necesite soporte de revisión visual para tareas de diseño. | Integration |
| [Case 69: Baseten sirve un millón de contextos más rápido](#case-69) | Utilice este caso para enrutar GLM-5.2 a través de Baseten cuando la velocidad de servicio de contexto largo sea importante para Factory Droid, OpenCode y arneses de codificación. | Integration |
| [Case 74: Subagentes QA de Browser Use para diseño web](#case-74) | Usa este caso para combinar GLM-5.2 con subagentes multimodales de QA de Browser Use v2 cuando un modelo solo de texto necesita inspección visual y correcciones iterativas de sitios web. | Integration |
| [Case 79: Tokens gratis diarios en el IDE oficial ZCode](#case-79) | Usa este caso para acceder a GLM-5.2 a través de ZCode cuando quieras un IDE oficial de programación gratuito con grandes asignaciones diarias de tokens y un flujo parecido a Cursor. | Tutorial |
| [Case 83: Configuración de Cursor mediante Fireworks](#case-83) | Usa este caso para conectar GLM-5.2 a Cursor mediante Fireworks con una configuración mínima compatible con OpenAI y sin código cliente personalizado. | Tutorial |
| [Case 84: Soporte del proveedor ZAI en VulcanBench](#case-84) | Usa este caso para ejecutar GLM-5.2 en un harness abierto de benchmark con soporte de primer nivel para el proveedor ZAI y una ruta dedicada de API key. | Integration |
| [Case 85: Variantes de razonamiento High/Max en OpenCode](#case-85) | Usa este caso para acceder a las variantes de razonamiento High y Max de GLM-5.2 dentro de OpenCode, al tiempo que obtienes un manejo más fiable del límite de pasos. | Integration |
| [Case 86: Selección del endpoint de código de Z.ai](#case-86) | Usa este caso para enrutar el tráfico de coding plan de GLM-5.2 al endpoint de Z.ai optimizado para código en lugar de la ruta genérica de API. | Tutorial |
| [Case 87: Configuración gratuita de la API GLM-5.2 en ZenMux](#case-87) | Usa este caso para obtener una API key y una base URL gratuitas de GLM-5.2, y luego conectarlas a Claude, Cursor, Hermes y herramientas similares. | Tutorial |
| [Case 93: Noumena ncode GLM predeterminado](#case-93) | Usa este caso para enrutar GLM-5.2 a entornos de agentes tipo ncode y Noumena con endpoints separados estándar y de contexto 1M, además de soporte como modelo por defecto. | Integration |
| [Case 101: Inicio rápido del arnés Baseten + Droid](#case-101) | Usa este caso para poner GLM-5.2 en marcha rápidamente mediante Baseten y el harness Droid, con un flujo corto de configuración que también puedes reutilizar en otros IDEs. | Tutorial |
| [Case 104: Flujo de trabajo de API GLM compatible con OpenAI](#case-104) | Usa este caso para construir en Python un cliente GLM-5.2 compatible con OpenAI con control de razonamiento, tool calling, recuperación de contexto largo y seguimiento de costes. | Tutorial |
| [Case 105: Zona de pruebas de búsqueda de API del agente de perplejidad](#case-105) | Usa este caso para conectar GLM-5.2 a la Agent API de Perplexity cuando quieras agentes en sandbox con búsqueda detrás de una sola llamada API. | Integration |
| [Case 109: API GLM de Baseten a 280 TPS](#case-109) | Usa este caso cuando importe la latencia del proveedor: Baseten afirma un serving de GLM-5.2 muy rápido con time-to-first-token subsegundo y alto throughput de decodificación. | Integration |
| [Case 128: Configuración de OpenCode de IA para trabajadores de Cloudflare](#case-128) | Usa este caso para ejecutar GLM-5.2 a través de Cloudflare Workers AI cuando quieras una ruta gratuita compatible con OpenAI para agentes de código sin aprovisionar tu propio host del modelo. | Tutorial |
| [Case 129: Cliente de navegador de configuración cero Puter.js](#case-129) | Usa este caso para probar GLM-5.2 en un prototipo solo de navegador antes de tocar API keys, facturación o configuración de backend. | Tutorial |
| [Case 130: Acceso unificado a terminales de SiliconFlow](#case-130) | Usa este caso para situar GLM-5.2 dentro de una pila multimodelo más amplia, porque la publicación describe un único endpoint compatible con OpenAI de SiliconFlow que cubre modelos chinos y occidentales con crédito de prueba gratis. | Integration |
| [Case 124: Creador de sitios web HuggingChat para HF Space](#case-124) | Usa este caso para probar GLM-5.2 en un flujo casi gratuito de sitio personal, desde la investigación en HuggingChat hasta el despliegue estático en Hugging Face Spaces. | Tutorial |
| [Case 125: Disponibilidad del motor de inferencia DigitalOcean](#case-125) | Usa este caso para enrutar GLM-5.2 por infraestructura gestionada cuando quieras acceso oficial del proveedor sin autoalojar tú mismo el modelo de 1M de contexto. | Integration |
| [Case 115: Código de comando Nivel rápido 120-250 Tok/S](#case-115) | Usa este caso para acceder a una variante más rápida de GLM-5.2 en Command Code cuando la velocidad de programación de largo horizonte importe más que solo el precio de entrada mínimo. | Integration |
| [Case 116: API rápida GLM-5.2 de Vercel AI Gateway](#case-116) | Usa este caso para enrutar GLM-5.2 Fast por Vercel AI Gateway cuando necesites velocidad sin servidor más precios explícitos por token. | Integration |
| [Case 95: Código Claude a través de Baseten](#case-95) | Usa este caso para ejecutar GLM-5.2 dentro de Claude Code mediante una clave de Baseten, una base URL personalizada y remapeo de modelos en `~/.claude/settings.json`. | Tutorial |
| [Case 96: Valor predeterminado del agente Deepsec Pi](#case-96) | Usa este caso para probar GLM-5.2 en un harness de seguridad, donde `deepsec` lo convirtió en el modelo por defecto para Pi agent y reportó resultados competitivos en evaluaciones. | Integration |

### [💸 Coste, precios y despliegue local](#cost-pricing-local-deployment)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 226: Triaje de historiales en Mac Studio con Bonsai](#case-226) | Usa este caso para mantener local un historial clínico largo mientras GLM-5.2 razona sobre él, porque MaziyarPanahi dice que GLM 5.2 hizo triage de un historial de paciente de tres años a través de Bonsai 27B en un Mac Studio y detectó un riesgo de contraste enterrado 17 meses atrás. | Demo |
| [Case 191: Laboratorio local LiteLLM construido por Hermes](#case-191) | Usa este caso para arrancar un laboratorio local de inferencia con GLM-5.2 como agente de código, porque la fuente dice que Hermes Agent más GLM-5.2 conectaron LiteLLM, Postgres, Prometheus y Grafana alrededor de una configuración con M3 Ultra. | Integration |
| [Case 187: Sim dual de drones sin conexión M5 Max](#case-187) | Usa este caso para estimar qué puede hacer un agente GLM-5.2 sobre Apple Silicon funcionando totalmente offline, porque XavierLocalAI reporta una instalación 753B escribiendo un simulador de aterrizaje en droneship a 26 tok/s sobre dos máquinas M5 Max de 128 GB. | Demo |
| [Case 186: 5x Arnés de producción de chispas DGX](#case-186) | Usa este caso para juzgar si una configuración de cinco nodos DGX Spark basta para trabajo productivo con GLM-5.2, porque thatcofffeeguy reporta unos 13,9 tok/s en un solo stream con 400K de contexto y 19,9 tok/s agregados en tres lanes dentro de un harness en vivo. | Demo |
| [Case 183: Punto de control M3 Ultra ds4-eval Q4](#case-183) | Usa este caso para benchmarkear una instalación de GLM-5.2 sobre Apple Silicon en una sola máquina con ds4-eval, porque ivanfioravanti reporta una ejecución q4 de unos 16 tok/s, con 76 de 92 pruebas superadas en 8 horas y 53 minutos sobre una M3 Ultra de 512 GB. | Evaluation |
| [Case 182: Guía de construcción de 4x RTX PRO 6000](#case-182) | Usa este caso para dimensionar una build local seria de GLM-5.2-594B, porque QingQ77 comparte una guía completa de hardware y operación basada en cuatro RTX PRO 6000, APIs expuestas vía opencode y una VM sandbox para trabajo con agentes. | Tutorial |
| [Case 181: Ejecución de QuantTrio en cuatro DGX Spark](#case-181) | Usa este caso para estimar lo que puede hacer un clúster DGX Spark de cuatro nodos con GLM-5.2 QuantTrio, porque Tech2Wild reporta 200K de contexto, 30 tok/s en un solo stream y 60,5 tok/s de throughput agregado con seis solicitudes concurrentes. | Demo |
| [Case 177: Ejecución de vídeo único M3 Ultra de 4 bits](#case-177) | Usa este caso para estimar la viabilidad de GLM-5.2 en una sola máquina Apple Silicon, porque ivanfioravanti muestra una ejecución 4-bit en un M3 Ultra de 512GB a unos 16 tok/s y la compara con un vídeo de ds4-eval en q2 cerca de 17 tok/s. | Demo |
| [Case 173: Servicio de nodo AMD MI355X 2626 Tok/s](#case-173) | Usa este caso para dimensionar inferencia GLM-5.2 de alto rendimiento sobre hardware AMD, porque wafer_ai dice que MI355X alcanzó 2626 tok/s por nodo y 213 tok/s en flujo único con un coste superior a 2 veces menos que Blackwell. | Demo |
| [Case 172: Vercel Gateway 287 Tok/s sin servidor](#case-172) | Usa este caso para estimar la latencia real de GLM-5.2 para usuarios a través de un gateway serverless, porque wafer_ai dice que su ruta GLM 5.2 Fast alcanzó 287 tokens por segundo en Vercel AI Gateway y no solo dentro de un harness de benchmark. | Demo |
| [Case 171: Implementación de RTX PRO 6000 con un clic](#case-171) | Usa este caso para estimar el suelo de un despliegue alojado y aislado de GLM-5.2, porque XciD_ dice que GLM-5.2-NVFP4 ya puede desplegarse con un clic en Inference Endpoints sobre 8x RTX PRO 6000 por 22 dólares la hora. | Integration |
| [Case 166: 744B completo en 5x ASUS GX10](#case-166) | Usa este caso para dimensionar un despliegue extremo de GLM-5.2 en home lab, porque el autor dice que el modelo completo de 744B ya corre con full context en 5 cajas ASUS GX10 y ya está conectado a un causal harness para cargas reales. | Demo |
| [Case 164: Intercambio de ruta de agente en la pila de China](#case-164) | Usa este caso para enrutar GLM-5.2 a la capa agent de una pila mixta cuando la presión de costes pesa más que la calidad máxima, porque el autor dice que cambiar Sonnet por GLM-5.2 redujo 5x el coste de entrada de ese slot con una caída de calidad de alrededor del 3 por ciento dentro de una migración de 30 días. | Evaluation |
| [Case 156: Piso de hardware local 744B](#case-156) | Use este caso para dimensionar con realismo los planes locales de GLM-5.2, porque la fuente dice que incluso las versiones cuantizadas siguen rondando 239 GB en 2 bits y 466 GB en 4 bits, lo que convierte 256 GB o más de RAM o VRAM en un piso práctico. | Limit |
| [Case 151: Puerto local NVFP4 Rust a 140 Tok/s](#case-151) | Usa este caso para medir lo que una instalación local afinada de GLM-5.2 puede hacer en trabajo real de coding, porque el autor informa de NVFP4 a 140 tok/s y de una migración completa de Python a Rust terminada en minutos. | Evaluation |
| [Case 140: Puesta en marcha dual-stack guiada por agentes en B300 x2](#case-140) | Usa este caso para dimensionar un despliegue autoalojado serio de GLM-5.2, porque el hilo muestra a analistas levantando inferencia NVFP4 sobre B300 bare-metal en vLLM y SGLang en menos de un día. | Evaluation |
| [Case 139: Aceleración de prefill en oMLX M3 Ultra](#case-139) | Usa este caso para volver a comprobar la viabilidad local en Apple silicon tras trabajo reciente de kernels, porque la velocidad de prefill reportada para GLM-5.2 en un M3 Ultra 512GB casi se duplicó sin un colapso obvio de calidad en pruebas rápidas. | Evaluation |
| [Case 138: Explosión de crédito de registro de 20M tokens](#case-138) | Usa este caso para evaluar si los créditos de registro bastan para una prueba real de GLM-5.2, porque la publicación afirma que las cuentas nuevas reciben 20M tokens gratis, sin tarjeta y con acceso completo compatible con OpenAI. | Integration |
| [Case 131: 4x Runbook GLM local DGX Spark](#case-131) | Usa este caso para medir si un clúster DGX Spark es una ruta local realista para GLM-5.2, porque la guía recopilada conecta coste de hardware, topología de clúster y comandos de vLLM con un objetivo GLM de contexto 1M. | Tutorial |
| [Case 43: Comparación de costos de tokens de salida](#case-43) | Utilice este caso para comparar la economía del token de salida GLM-5.2 con los modelos estilo Opus, Fable y GPT-5.5. | Evaluation |
| [Case 44: ROI del hardware local cercano a la frontera](#case-44) | Utilice este caso para razonar sobre si los modelos autohospedados tipo GLM-5.2 pueden compensar los costos de hardware para los usuarios intensivos de agentes. | Evaluation |
| [Case 45: MLX en dos estudios Mac](#case-45) | Utilice este caso para explorar ejecuciones locales de GLM-5.2 en hardware de Apple y configuraciones orientadas a MLX. | Demo |
| [Case 46: Reclamo de implementación local mensual H100](#case-46) | Utilice este caso como indicador de comparación de costos para verificar los supuestos de implementación local antes de elegir entre suscripción y autohospedaje. | Evaluation |
| [Case 47: Créditos diarios y reclamo de reemplazo de Claude](#case-47) | Utilice este caso para inspeccionar la narrativa del crédito gratuito y del agente de reemplazo en torno a GLM-5.2, mientras separa las afirmaciones de marketing de la adecuación de la carga de trabajo verificada. | Evaluation |
| [Case 48: Ventana de token ZCode gratuita](#case-48) | Utilice este caso para probar GLM-5.2 a través de una asignación gratuita de ZCode antes de comprometerse con un proveedor pago o una implementación local. | Integration |
| [Case 49: Oferta de semana gratuita de ZenMux](#case-49) | Utilice este caso para encontrar ventanas de acceso gratuito con límites de tiempo para las pruebas de GLM-5.2. | Integration |
| [Case 50: Precios por token de crofAI](#case-50) | Utilice este caso para comparar los precios de proveedores externos para GLM-5.2 antes de seleccionar una ruta. | Integration |
| [Case 51: Comparación de margen de precio API](#case-51) | Utilice este caso como crítica de precios de mercado al comparar GLM-5.2 con otros laboratorios de vanguardia y modelos abiertos. | Evaluation |
| [Case 64: Velocidad de inferencia local del sótano](#case-64) | Utilice este caso para estimar el rendimiento de inferencia local de GLM-5.2 en hardware Apple de gran memoria antes de planificar una configuración de codificación fuera de línea. | Demo |
| [Case 68: Implementación local cuantificada sin pereza](#case-68) | Utilice este caso para evaluar las rutas de implementación cuantificadas de GLM-5.2 cuando los pesos del modelo completo sean demasiado grandes para el hardware local normal. | Tutorial |
| [Case 88: Ejecución distribuida de MLX en dos M3 Ultra](#case-88) | Usa este caso para estimar cómo es servir GLM-5.2 en 8 bits a través de dos máquinas M3 Ultra antes de construir una configuración mayor sobre Apple silicon. | Demo |
| [Case 89: Reducción del multiplicador de ZCode hasta septiembre](#case-89) | Usa este caso para estirar los créditos del plan de GLM-5.2 con multiplicadores más bajos de ZCode tanto en horas pico como fuera de pico. | Integration |
| [Case 97: Rendimiento local RTX PRO 6000](#case-97) | Usa este caso para dimensionar una estación local de alta gama para GLM-5.2, donde un escritorio con dos Blackwell mantuvo velocidad de decodificación de dos dígitos en una build cuantizada a 4 bits. | Demo |
| [Case 98: Verificación de la realidad del ROI de la API de Mac Studio](#case-98) | Usa este caso para validar si tiene sentido comprar un Mac Studio para inferencia local de GLM-5.2, porque las cuentas de amortización publicadas favorecen claramente el acceso por API o plan para la mayoría de usuarios. | Evaluation |
| [Case 106: Ahorro de interrupción local de LiteLLM](#case-106) | Usa este caso para mantener avanzando un entregable cuando las APIs frontier alojadas fallen o queden limitadas, redirigiendo el trabajo mediante un GLM-5.2 desplegado localmente con LiteLLM. | Demo |
| [Case 107: ROI individual versus equipo local](#case-107) | Usa este caso para decidir si un despliegue local de GLM-5.2 tiene sentido para una persona individual o más bien solo para un equipo de desarrollo más grande. | Evaluation |
| [Case 112: Ejecución de Terminal-Bench 2.0 en cuatro RTX PRO 6000](#case-112) | Usa este caso para dimensionar una configuración local de GLM-5.2 con cuatro GPU frente a un benchmark duro de terminal antes de comprometerte con una workstation de alta gama. | Evaluation |
| [Case 118: Crackme local resuelto en 2x RTX PRO 6000 Blackwells](#case-118) | Usa este caso para juzgar si una configuración local seria de GLM-5.2 puede terminar tareas largas de ingeniería inversa sin acceso a depurador. | Demo |

### [🧭 Límites, advertencias y señales de seguridad](#limits-caveats-safety-signals)

| Caso | Enfoque | Tipo |
|---|---|---|
| [Case 222: Advertencia de guardrails para GLM en prod](#case-222) | Usa este caso para justificar guardrails más estrictos alrededor de agentes de coding con GLM-5.2, porque mitsuhiko dice que el modelo mostraba ganas de hacer force-push, aplicar cambios de Pulumi sin preguntar y tocar bases de datos de producción. | Límite |
| [Case 216: Fallo silencioso del KV-Cache Debugger](#case-216) | Usa este caso si quieres probar GLM-5.2 frente a entradas contradictorias y no solo frente a números de benchmark en limpio, porque cyrilXBT mostró una comparación directa en la que GLM acertó la configuración limpia pero omitió una variable mala y devolvió un preset 2.667x incorrecto sin ninguna advertencia. | Evaluation |
| [Case 205: Errores del ejecutor de reescritura de HTML estático](#case-205) | Usa este caso para evitar dar a GLM-5.2 control total como executor en reescrituras legacy 1:1, porque una migración grande de HTML estático a React y Vite perdió demasiados detalles usando OpenCode Go y Cline, y llevó al autor a confiar más en GLM como planner que como executor. | Limit |
| [Case 197: Composio 47-Brechas del agente de tareas](#case-197) | Usa este caso para entender dónde GLM-5.2 todavía falla en trabajo real de agentes SaaS, porque Composio lo conectó a 17 herramientas en 47 tareas y encontró 45 aciertos, con fallos en chequeos de completitud y en juicios difusos sobre SLA. | Evaluation |
| [Case 163: Paridad preliminar de la investigación cibernética](#case-163) | Usa este caso para medir GLM-5.2 en subtareas de investigación de vulnerabilidades, porque Irregular reporta evaluaciones internas tempranas comparables a GPT-5.4 y Opus 4.6 en una suite cyber estrecha, advirtiendo al mismo tiempo que los escenarios de ataque end-to-end siguen sin probarse. | Limit |
| [Case 157: Reescritura de habilidades de reducción de gastos de OpenRouter](#case-157) | Use este caso para presupuestar el costo de migración antes de cambiar de modelo agente, porque la prueba con OpenRouter de un fondo situó GLM-5.2 en alrededor de un octavo del costo de Opus, pero aun así necesitó reescrituras de skills, lógica de enrutamiento y aceptar salidas más lentas y más débiles. | Limit |
| [Case 149: AA Verbosidad y compensación de razonamiento](#case-149) | Usa este caso para separar la inteligencia open-weight de nivel frontier de GLM-5.2 de su coste de razonamiento, porque Artificial Analysis muestra un líder abierto que también gasta demasiados tokens de salida. | Evaluation |
| [Case 134: Advertencia sobre la estrecha victoria de Semgrep en IDOR](#case-134) | Usa este caso para separar una señal de seguridad real de la exageración del titular, porque la fuente dice que GLM-5.2 superó a Claude Code en un benchmark de IDOR pero nunca se probó contra Mythos. | Limit |
| [Case 132: Brecha de eficiencia de razonamiento de LisanBench](#case-132) | Usa este caso para revisar GLM-5.2 en cargas con mucho razonamiento antes de asumir que su fortaleza en coding se traslada de forma limpia, porque el resultado publicado de LisanBench mejora a GLM-5 pero sigue siendo ineficiente frente a otros modelos abiertos. | Limit |
| [Case 133: Advertencia sobre discrepancia en el dominio de PrinzBench](#case-133) | Usa este caso para mantener GLM-5.2 centrado en coding y ejecución de agentes en lugar de investigación legal, porque la publicación contrasta una puntuación floja en PrinzBench con benchmarks mucho más fuertes de software y uso de herramientas. | Limit |
| [Case 52: Sin advertencia de visión](#case-52) | Utilice este caso para recordar que GLM-5.2 puede ser menos útil para flujos de trabajo que requieren capacidad de visión nativa. | Limit |
| [Case 53: Advertencia sobre la brecha de agentes en el mundo real](#case-53) | Utilice este caso para evitar una lectura excesiva de los resultados de los puntos de referencia como prueba de que GLM-5.2 coincide con los mejores modelos propietarios en todas las tareas agentes implementadas. | Limit |
| [Case 54: Preocupación por la barandilla de seguridad](#case-54) | Utilice este caso como recordatorio para realizar evaluaciones de seguridad antes de implementar GLM-5.2 en dominios confidenciales. | Limit |
| [Case 55: Crítica de la metodología de referencia](#case-55) | Utilice este caso para cuestionar la metodología de referencia incluso cuando el resultado principal favorezca a GLM-5.2. | Limit |
| [Case 56: Preocupación por la latencia en horas pico](#case-56) | Utilice este caso para probar la latencia del proveedor antes de cambiar los planes de codificación o enrutar los flujos de trabajo estilo Claude Code a GLM-5.2. | Limit |
| [Case 57: Resultado de no mejora de FutureSim](#case-57) | Utilice este caso para comprobar si las ganancias de codificación se generalizan a dominios que no son de codificación antes de una implementación amplia. | Limit |
| [Case 58: Crítica de preparación para el lanzamiento](#case-58) | Utilice este caso para separar la capacidad del modelo de la ejecución del lanzamiento, la documentación y la preparación de la API. | Limit |
| [Case 59: Aumento del precio del plan de codificación](#case-59) | Utilice este caso para verificar el precio del plan antes de recomendar GLM-5.2 como reemplazo de bajo costo. | Limit |
| [Case 67: Trabajo paralelo corto versus tiradas largas de agentes](#case-67) | Utilice este caso para dirigir GLM-5.2 hacia tareas de codificación limitadas cortas y, al mismo tiempo, reservar modelos más potentes para ejecuciones de agentes más profundas de varias horas. | Limit |
| [Case 103: Señal de alucinación multivuelta HalluHard](#case-103) | Usa este caso para probar GLM-5.2 en tareas multiturno sensibles a las alucinaciones antes de confiar en puntuaciones fuertes de benchmark en otros frentes. | Limit |
| [Case 108: Advertencia de emergencia de seguridad de peso abierto](#case-108) | Usa este caso como señal para planificar seguridad: GLM-5.2 open-weight reduce la fricción operativa para agentes ofensivos de seguridad incluso cuando las APIs cerradas siguen monitorizadas. | Limit |
| [Case 126: Pase de arnés Rust Bug con espacio de giro de 7x](#case-126) | Usa este caso para separar la ventaja de GLM-5.2 en calidad de código de su sobrecarga actual en el harness de agentes, porque puede resolver el bug gastando muchas más vueltas que Opus. | Evaluation |
| [Case 114: Advertencia sobre el costo de intercambio de modelos de Braintrust](#case-114) | Usa este caso para evitar asumir que cambiar a un modelo más barato conservará la calidad en un flujo real de programación con agentes. | Evaluation |
| [Case 73: Comprobación de censura en código y sesgo](#case-73) | Usa este caso como una señal práctica de seguridad para pruebas de código y sesgo político, no como prueba de que las preocupaciones de alineación más amplias ya estén resueltas. | Limit |
| [Case 75: Fallo de facturación en razonamiento difícil](#case-75) | Usa este caso para probar GLM-5.2 con cuidado en cargas de razonamiento difíciles, porque el informe público muestra tiempos largos, baja finalización y una facturación inesperadamente alta. | Limit |

<a id="benchmarks-frontier-evaluation"></a>
## 📏 Evaluaciones comparativas y evaluación de frontera
---
<a id="case-223"></a>
### Case 223: [Brecha de eficiencia de tokens en el Intelligence Index](https://x.com/ArtificialAnlys/status/2077466596528832678) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para presupuestar GLM-5.2 en cargas de benchmark de largo horizonte, porque Artificial Analysis dice que GLM-5.2 Max promedió unos 43K output tokens por tarea del Intelligence Index frente a 25K de Inkling y cifras menores de Kimi K2.6 y DeepSeek v4 Pro Max.**

Artificial Analysis aísla el uso de output tokens en lugar de fijarse solo en la puntuación del leaderboard y sitúa a GLM-5.2 en el lado caro del grupo open-weight para la misma familia de benchmarks. La publicación compara 25K output tokens medios de Inkling frente a 43K de GLM-5.2 Max, 38K de Kimi K2.6 y 37K de DeepSeek v4 Pro Max, así que funciona como una nota práctica de eficiencia para equipos a los que ya les gusta la calidad de GLM pero necesitan prever el consumo de tokens de los agent loops.

Type: Evaluation | Date: 2026-07-15

---
<a id="case-217"></a>
### Case 217: [Ruta de rescate EvalPlus supera a Fable](https://x.com/gmi_cloud/status/2077124979397947824) (by [@gmi_cloud](https://x.com/gmi_cloud))

**Usa este caso para probar una ruta de coding con dos modelos y verificador, porque gmi_cloud dice que Opus 4.8 primero y GLM 5.2 FP8 como rescate resolvieron 94 de 100 tareas congeladas de EvalPlus, cinco más que Fable 5, con un coste alrededor de 47 por ciento menor.**

gmi_cloud dice que el stack ejecutó 50 tareas de HumanEval+ y 50 de MBPP+, llamó a GLM 5.2 FP8 solo cuando Opus falló el verificador y aun así superó a cada modelo individual en tasa de acierto. El hilo también deja claro el trade-off: la combinación usó 85,4 por ciento más tokens que Fable 5, pero costó 0,4251 dólares frente a 0,8033, con GLM rescatando cuatro de los diez fallos de Opus.

Tipo: Evaluación | Fecha: 2026-07-14

---
<a id="case-207"></a>
### Case 207: [Comparativa del navegador de fluidos estables](https://x.com/AlicanKiraz0/status/2075639232169705781) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Usa este caso para comparar GLM-5.2 en builds de física para navegador cargados de algoritmo, porque AlicanKiraz0 ejecutó un benchmark HTML de Stable Fluids y dio a GLM 5.2 Max un 88 sobre 100 por unos 1,17 dólares, por delante de Opus 4.8 y Fable 5 pero por detrás de GPT 5.6 Sol.**

El benchmark pide a cada modelo un único archivo HTML autocontenido que implemente stable fluids de Jos Stam con advección semi-Lagrangiana, difusión iterativa, proyección de presión, informe en vivo de divergencia e inyección interactiva de pintura y velocidad. AlicanKiraz0 dice que GLM 5.2 Max alcanzó 88 sobre 100, por delante de Opus 4.8 con 86 y Fable 5 con 81, manteniéndose mucho más barato, así que sirve como evaluación de ingeniería sobre corrección numérica y rendimiento en navegador en tiempo real, no como una comparación frontend basada en gustos.

Type: Evaluation | Date: 2026-07-10

<a id="case-199"></a>
### Case 199: [Plomo del índice de peso abierto de época](https://x.com/EpochAIResearch/status/2074894535558300103) (by [@EpochAIResearch](https://x.com/EpochAIResearch))

**Usa este caso para ubicar GLM-5.2 en una curva de capacidad de largo plazo, porque Epoch AI estima una puntuación de 152 en su Capabilities Index y lo llama el mejor open weight de su conjunto evaluado.**

Epoch AI dice que GLM-5.2 obtuvo una puntuación estimada de 152 en el Epoch Capabilities Index, y que es la más alta entre los modelos open weight que han evaluado. Eso convierte el post en una referencia útil cuando necesitas una señal única de posicionamiento de capacidades y no solo un leaderboard estrecho de coding.

Type: Benchmark | Date: 2026-07-08

---
<a id="case-196"></a>
### Case 196: [Evaluación de arnés interno de Databricks](https://x.com/alighodsi/status/2074996561306955958) (by [@alighodsi](https://x.com/alighodsi))

**Usa este caso para benchmarkear GLM-5.2 sobre una gran codebase privada de ingeniería, porque Databricks dice que su evaluación interna sobre trabajo de más de 3.000 engineers mostró que GLM 5.2 rindió muy bien y que solo elegir mejor el harness puede recortar el coste alrededor de 2x.**

Ali Ghodsi dice que Databricks ejecutó una evaluación amplia sobre sus propias tareas, codebase e infraestructura, abarcando a más de 3.000 software engineers, tres hyperscalers y muchos lenguajes. El post afirma que GLM 5.2 rindió extremadamente bien y que escoger el harness correcto para el mismo modelo puede reducir el coste alrededor de 2x, con Omnigent delante para multiplexar modelos y harnesses según la tarea.

Type: Evaluation | Date: 2026-07-08

---
<a id="case-190"></a>
### Case 190: [Subcampeón de peso abierto NatureBench](https://x.com/OkhayIea/status/2074498200262889837) (by [@OkhayIea](https://x.com/OkhayIea))

**Usa este caso para benchmarkear GLM-5.2 en trabajo de agentes científicos, porque NatureBench dice que GLM-5.2 debutó como número dos global y lideró a los open weights en 90 tareas de seis dominios científicos.**

NatureBench pregunta si un agente de código puede descubrir un método que supere el SOTA publicado de artículos reales de la familia Nature en 90 tareas y seis dominios científicos, sin búsqueda web. La actualización dice que GLM-5.2 debutó como número dos global, solo detrás de Claude Opus 4.7, y lideró el campo open weight. Eso lo convierte en un benchmark concreto para workflows de agentes científicos, no solo para generación de código normal.

Type: Benchmark | Date: 2026-07-07

---
<a id="case-189"></a>
### Case 189: [Compensación de costos de 45 tareas entre terminal y banco](https://x.com/Aiswarya_Sankar/status/2074554064856314219) (by [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar))

**Usa este caso para comparar GLM-5.2 con GPT-5.5 en el mismo harness de agente, porque una corrida de 45 tareas de Terminal-Bench dejó a GLM-5.2 con 25 aciertos frente a 29 de GPT-5.5, con cerca de 40% menos coste usando prompt caching.**

La nota del benchmark dice que el equipo ejecutó GPT-5.5 y GLM-5.2 sobre 45 tareas de Terminal-Bench con el mismo agente, los mismos prompts, la misma evaluación y el mismo harness, cambiando solo el modelo. GLM resolvió 25 de 45 frente a 29 de 45 de GPT-5.5, pero costó alrededor de 40% menos con prompt caching. Eso lo convierte en un checkpoint concreto de precio frente a éxito, no en una preferencia vaga de workflow.

Type: Evaluation | Date: 2026-07-07

---
<a id="case-188"></a>
### Case 188: [Harvey LAB-AA Vinculación de agente legal](https://x.com/ArtificialAnlys/status/2074541975186165887) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para benchmarkear GLM-5.2 en trabajo real de agentes legales, porque Harvey LAB-AA sitúa a GLM-5.2 Max en 7,5% de all-pass, empatado con Claude Opus 4.8 en 120 tareas privadas de 24 áreas legales.**

Artificial Analysis dice que Harvey LAB-AA evalúa trabajo jurídico real en 120 tareas privadas de 24 áreas de práctica y califica las salidas con rúbricas binarias. En el lanzamiento, GLM-5.2 Max alcanza 7,5% de all-pass y 91,0% de criteria-pass, empatado con Claude Opus 4.8 y costando por tarea apenas alrededor del 6% de Claude Fable 5. Por eso funciona tanto como benchmark de dominio frontier como señal de eficiencia de coste.

Type: Benchmark | Date: 2026-07-07

---
<a id="case-184"></a>
### Case 184: [Líder de pesas abiertas AutomationBench-AA](https://x.com/ArtificialAnlys/status/2074194764510208230) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para comparar GLM-5.2 en automatización SaaS con reglas de negocio y no solo en benchmarks de código, porque Artificial Analysis reporta 27,8% para GLM-5.2 Max y lo llama el mejor modelo open weights en AutomationBench-AA.**

Artificial Analysis dice que AutomationBench-AA ejecuta 657 tareas privadas de workflow sobre 40 aplicaciones SaaS simuladas y las evalúa con casi 12.000 assertions de objetivos y guardrails. El post de lanzamiento sitúa a GLM-5.2 Max en 27,8%, como líder entre los open weights, pero también aclara que sigue detrás de modelos cerrados más fuertes y que incurre en bastantes más violaciones de guardrails por tarea, así que funciona tanto como señal de capacidad como de limitación para automatización empresarial con agentes.

Type: Evaluation | Date: 2026-07-06

---
<a id="case-178"></a>
### Case 178: [Victoria en el punto de referencia del simulador de tres cuerpos](https://x.com/AlicanKiraz0/status/2073823792543998170) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Usa este caso para comparar GLM-5.2 en benchmarks de programación con física numérica, porque AlicanKiraz0 ejecutó una tarea caótica de simulador de tres cuerpos y dio a GLM 5.2 Max la mejor nota con 91 sobre 100.**

El benchmark combina física de tres cuerpos, RK4 real, estabilidad en encuentros cercanos, gráficos de conservación en vivo y controles interactivos. El hilo dice que GLM 5.2 Max destacó por usar estado en Float64Array, reutilizar buffers de RK4, aplicar Plummer softening y subpasos adaptativos, por lo que se trata de una evaluación concreta de calidad de ingeniería y no de una simple captura de ranking.

Type: Evaluation | Date: 2026-07-05

---
<a id="case-167"></a>
### Case 167: [GameDevBench 333-Tarea Líder de código abierto](https://x.com/iamwaynechi/status/2073081777091182633) (by [@iamwaynechi](https://x.com/iamwaynechi))

**Usa este caso para seguir GLM-5.2 en benchmarks de desarrollo de juegos agentic, porque GameDevBench se amplió a 333 tareas y dice que GLM-5.2 ya es el modelo open-source más fuerte de su leaderboard pese a no tener visión.**

iamwaynechi dice que GameDevBench triplicó su tamaño hasta 333 tareas, actualizó el paper y añadió GLM-5.2 y Opus 4.8 al leaderboard. La publicación dice que Opus lidera por poco, mientras GLM-5.2 queda como el open-source más fuerte, lo que lo convierte en una señal útil para workflows de construcción de juegos agentic y no solo para coding de texto.

Type: Evaluation | Date: 2026-07-03

---

<a id="case-175"></a>
### Case 175: [Cuadro de mando de doble péndulo del cursor](https://x.com/AlicanKiraz0/status/2073386918813778143) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Usa este caso para comparar GLM-5.2 en un benchmark de coding dentro de Cursor con una tarea acotada, porque AlicanKiraz0 probó seis modelos sobre un simulador HTML de doble péndulo y dio a GLM 5.2 Max 88 sobre 100, detrás de Fable y Sonnet pero por delante de GPT-5.5, Kimi K2.7 Code y Composer.**

AlicanKiraz0 comparó seis modelos dentro de Cursor sobre una única tarea de simulador HTML de doble péndulo y publicó tanto la puntuación total como las debilidades de cada modelo. Describe la ejecución de GLM 5.2 Max como visualmente fuerte y didáctica, pero menos refinada que Fable o Sonnet en la arquitectura de rendimiento, con riesgo extra de allocation en el wrapper RK4 y una ruta menos robusta al redimensionar el trail buffer. Eso lo convierte en una evaluación comparativa concreta y no en un juicio de gusto vago.

Type: Evaluation | Date: 2026-07-04

<a id="case-162"></a>
### Case 162: [VulcanBench 10 tareas 80 por ciento empatado](https://x.com/morganlinton/status/2072689409011679642) (by [@morganlinton](https://x.com/morganlinton))

**Usa este caso para comparar GLM-5.2 en tareas de ingeniería reales y fuera de cutoff donde el coste importa tanto como la puntuación, porque Morgan Linton dice que VulcanBench dio a GLM 5.2 High, Fable 5 Low y Sonnet 5 High el mismo 80 por ciento en 10 repos, mientras GLM quedó en el medio por coste.**

Morgan Linton dice que el benchmark usó 10 tareas de ingeniería reales de proyectos como Flask, aiohttp y sqlglot, todas descritas como post-training-cutoff. Fable 5 Low, GLM 5.2 High y Sonnet 5 High obtuvieron 80 por ciento, con costes reportados de 2,27, 8,41 y 15,81 dólares respectivamente. Es un punto de control útil de precio frente a calidad en tres vías.

Type: Evaluation | Date: 2026-07-02

---

<a id="case-159"></a>
### Case 159: [Punto de control del 51,1 por ciento de SWE-Rebench](https://x.com/ibragim_bad/status/2072318238407483593) (by [@ibragim_bad](https://x.com/ibragim_bad))

**Use este caso para seguir GLM-5.2 en una tabla SWE agent que se actualiza continuamente, porque la última publicación de SWE rebench reporta 51,1 por ciento con 2,62 millones de tokens, claramente por delante de las nuevas ejecuciones de DeepSeek, MiMo, Qwen y Gemma.**

ibragim_bad dice que la última actualización de SWE rebench añade GLM-5.2 junto con varios modelos abiertos nuevos. Las cifras publicadas muestran a GLM en 51,1 por ciento usando 2,62 millones de tokens, frente a DeepSeek V4 Pro en 42,7 por ciento, MiMo V2.5 Pro en 42,4 por ciento, y puntuaciones aún menores para Qwen y Gemma, lo que lo convierte en un checkpoint público concreto del leaderboard.

Type: Evaluation | Date: 2026-07-01

---

<a id="case-154"></a>
### Case 154: [LaunchDarkly Edge-Case gana con 40/41](https://x.com/composio/status/2072355937415827950) (by [@composio](https://x.com/composio))

**Use este caso para probar GLM-5.2 en trabajo de agentes con herramientas empresariales en lugar de evaluaciones de solo chat, porque Composio reporta 40 de 41 en tareas con GitHub, Jira y LaunchDarkly y dice que GLM fue el único modelo que detectó un caso límite de aprobación pendiente.**

Composio probó GLM-5.2 contra Claude Opus 4.8 y GPT-5.5 en 41 tareas agenticas que usan herramientas reales como GitHub, Jira y LaunchDarkly. GLM obtuvo 40 de 41, mientras que Opus y GPT obtuvieron 39 cada uno. En una tarea de LaunchDarkly, GLM revisó las aprobaciones pendientes antes de marcar una flag como obsoleta, mientras que los otros dos modelos se quedaron en el estado encendido o apagado.

Type: Evaluation | Date: 2026-07-01

---


<a id="case-146"></a>
### Case 146: [Subcampeón del parche de peso abierto CyberBench](https://x.com/ValsAI/status/2072099011398627639) (by [@ValsAI](https://x.com/ValsAI))

**Usa este caso para medir a GLM-5.2 en búsqueda y parcheo de vulnerabilidades de estilo ofensivo, porque CyberBench lo sitúa segundo en 60 vulnerabilidades reales de OSS-Fuzz.**

ValsAI explica que CyberBench añade dos tareas: enviar una PoC que rompa solo el build vulnerable y parchear el código sin romper el comportamiento. En 60 vulnerabilidades de memoria de OSS-Fuzz, GPT-5.5 lideró y GLM 5.2 fue una de las referencias open-weight más fuertes.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-1"></a>
### Case 1: [Índice de Inteligencia de Análisis Artificial](https://x.com/ArtificialAnlys/status/2067135640249209175) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilice la publicación de Análisis artificial para comparar GLM-5.2 con otros modelos de frontera patentados y de peso abierto en materia de inteligencia y costo por tarea.**

Artificial Analysis informó que GLM-5.2 es el modelo líder en ponderaciones abiertas en su Índice de Inteligencia, con una puntuación de 51 y una posición en la frontera de Pareto en inteligencia versus costo por tarea. La publicación también registra el tamaño del modelo, la ventana de contexto, los precios y la disponibilidad del proveedor.

Type: Benchmark | Date: 2026-06-17

---

<a id="case-2"></a>
### Case 2: [Clasificación de interfaz de Code Arena](https://x.com/arena/status/2066957802741043641) (by [@arena](https://x.com/arena))

**Utilice este caso para evaluar GLM-5.2 en tareas reales de codificación front-end juzgadas mediante comparaciones de estilo arena.**

La cuenta de Arena informó que GLM-5.2 Max ocupa el segundo lugar en Code Arena Frontend, por delante de otros modelos abiertos y cerca de la entrada de la frontera superior. La publicación es especialmente útil para casos de uso de front-end, React, HTML, juegos, simulación y diseño basado en referencias.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-3"></a>
### Case 3: [Primer lugar en Design Arena](https://x.com/Designarena/status/2066940737011560652) (by [@Designarena](https://x.com/Designarena))

**Utilice este caso para juzgar si GLM-5.2 puede manejar tareas de diseño más código en lugar de solo pruebas comparativas de codificación con mucho texto.**

Design Arena informó que GLM-5.2 alcanzó el primer lugar con una puntuación Elo de 1360, lo que destaca un salto en el rendimiento del código de diseño para un modelo de peso abierto. Trátelo como una señal de referencia de diseño, no como un sustituto de la revisión de la interfaz de usuario específica del proyecto.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-4"></a>
### Case 4: [Resultado de FrontierSWE](https://x.com/ProximalHQ/status/2066939701026787583) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Utilice la publicación de FrontierSWE para comparar GLM-5.2 con los modelos GPT-5.5, Opus y Fable en tareas de ingeniería de software.**

La publicación informa que GLM-5.2 ocupa el tercer lugar en FrontierSWE y lo enmarca como uno de los primeros modelos de peso abierto que reduce la brecha con los mejores modelos propietarios en trabajos de ingeniería de implementación pesada.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-5"></a>
### Case 5: [Líder de código abierto de DeepSWE](https://x.com/AiBattle_/status/2066938378512126024) (by [@AiBattle_](https://x.com/AiBattle_))

**Utilice el caso de DeepSWE para comprender GLM-5.2 como un modelo abierto sólido para tareas difíciles de evaluación de ingeniería de software.**

AiBattle informó una puntuación DeepSWE del 46,2 % para GLM-5.2 y la describió como la puntuación más alta para un modelo de código abierto en ese contexto de referencia.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-6"></a>
### Case 6: [Banco de terminales superior al 80 por ciento](https://x.com/cline/status/2066951439793242193) (by [@cline](https://x.com/cline))

**Utilice este caso al evaluar GLM-5.2 para flujos de trabajo de agentes y codificación orientados a terminales.**

Cline destacó GLM-5.2 como el primer modelo de peso abierto que superó el 80 % en Terminal-Bench y lo posicionó como una opción de nivel de frontera para un desarrollo accesible basado en herramientas.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-7"></a>
### Case 7: [Comparación de SWELancer con GPT-5.5](https://x.com/gosrum/status/2067153091842203676) (by [@gosrum](https://x.com/gosrum))

**Utilice este caso de SWELancer como una comparación multimétrica concreta entre GLM-5.2 y GPT-5.5 sobre el éxito de la tarea, la recompensa y el tiempo de finalización.**

El autor compartió una actualización de referencia japonesa en la que GLM-5.2 superó inesperadamente a GPT-5.5 en los últimos resultados de SWELancer en términos de éxito de la tarea, recompensa obtenida y tiempo para completarla, con dos tareas inaccesibles excluidas.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-8"></a>
### Case 8: [Señal de puntuación perfecta BridgeBench](https://x.com/bridgemindai/status/2065874542321426819) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para inspeccionar GLM-5.2 sobre un razonamiento fundamentado de varios pasos en lugar de solo codificar tablas de clasificación.**

BridgeMind informó que el GLM-5.2 fue el primer modelo en recibir una puntuación perfecta en el benchmark BridgeBench BS, lo que lo convierte en una fuente útil para afirmaciones de evaluación con mucho razonamiento.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-9"></a>
### Case 9: [BridgeBench Razonamiento número uno](https://x.com/bridgebench/status/2066123398816624743) (by [@bridgebench](https://x.com/bridgebench))

**Utilice este caso para comparar GLM-5.2 con modelos de frontera cerrada en tareas de razonamiento fundamentado.**

BridgeBench informó que GLM-5.2 ocupó el puesto número uno en un punto de referencia de razonamiento y superó a Claude Fable 5 en ese contexto de medición.

Type: Benchmark | Date: 2026-06-14

---

<a id="case-10"></a>
### Case 10: [KernelBench-Hard sin atajos](https://x.com/elliotarledge/status/2065735912370417760) (by [@elliotarledge](https://x.com/elliotarledge))

**Utilice este caso para comprobar si las ganancias de referencia provienen de un comportamiento de implementación válido en lugar de atajos.**

La publicación de KernelBench-Hard dice que el resultado interesante no fue solo la puntuación, sino que GLM-5.2 dejó de usar un acceso directo inapropiado en un problema GEMM fp8, lo que lo hace relevante para la integridad del benchmark.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-11"></a>
### Case 11: [Actualización del banco de Runescape](https://x.com/maxbittker/status/2066985743197577433) (by [@maxbittker](https://x.com/maxbittker))

**Utilice este caso como una señal rápida para el progreso del modelo de peso abierto en tareas de referencia similares a las de un juego.**

La publicación informa que GLM-5.2 obtiene una puntuación mejor que los modelos propietarios recientes en Runescape, y utiliza ese resultado para enmarcar la rapidez con la que se está poniendo al día la capacidad de frontera de código abierto.

Type: Benchmark | Date: 2026-06-16

---

<a id="case-12"></a>
### Case 12: [Mejora de la velocidad de BridgeBench](https://x.com/bridgebench/status/2065845045752648159) (by [@bridgebench](https://x.com/bridgebench))

**Utilice este caso para evaluar flujos de trabajo sensibles a la latencia donde la velocidad importa junto con la inteligencia.**

BridgeBench informó que GLM-5.2 es tres veces más rápido que GLM-5.1 y cuarto en su punto de referencia de velocidad, lo que lo hace relevante para flujos de trabajo donde la velocidad de iteración afecta la usabilidad.

Type: Benchmark | Date: 2026-06-13

---

<a id="case-60"></a>
### Case 60: [Codificación KernelBench Hard y Mega GPU](https://x.com/elliotarledge/status/2068177175640240323) (by [@elliotarledge](https://x.com/elliotarledge))

**Utilice este caso para evaluar GLM-5.2 en la codificación del kernel de GPU en KernelBench-Hard y KernelBench-Mega, donde los rastros de agentes abiertos hacen que el resultado sea inspeccionable.**

La actualización de KernelBench informa pruebas H100, B200 y RTX PRO 6000, seguimientos de agentes de código abierto y GLM-5.2 como el modelo abierto superior en la comparación.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-70"></a>
### Case 70: [Liderazgo open-source en DeepSWE con esfuerzo máximo](https://x.com/datacurve/status/2068473057107476680) (by [@datacurve](https://x.com/datacurve))

**Usa este caso para seguir a GLM-5.2 en DeepSWE con esfuerzo máximo, donde la tabla publicada lo sitúa primero entre los modelos abiertos con una puntuación pass@1 del 44%.**

DataCurve compartió una actualización de la tabla de DeepSWE que muestra a GLM-5.2 con 44% pass@1 y 17 puntos por delante de Kimi K2.7 Code entre los modelos abiertos. Tómalo como una actualización de benchmark, no como prueba de que todos los workflows reales de agentes ya estén resueltos.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-72"></a>
### Case 72: [Segundo puesto en benchmark de debates LLM](https://x.com/LechMazur/status/2068428300460974279) (by [@LechMazur](https://x.com/LechMazur))

**Usa este caso para evaluar GLM-5.2 más allá del código en debates adversariales de varios turnos, donde la variante de razonamiento máximo quedó segunda detrás de modelos Claude.**

Lech Mazur compartió un resultado del LLM Debate Benchmark que sitúa a GLM-5.2 Max en segundo lugar. El benchmark mide debates adversariales de varios turnos sobre temas amplios, por lo que funciona como una señal de razonamiento fuera de los leaderboards de código habituales.

Type: Benchmark | Date: 2026-06-20

---

<a id="case-76"></a>
### Case 76: [Tasa de alucinación en AA-Omniscience](https://x.com/yuhasbeentaken/status/2068259921519423855) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Usa este caso para comparar GLM-5.2 en manejo de incertidumbre, donde el resultado publicado de AA-Omniscience muestra una tasa de alucinación menor que la de varios otros modelos frontier.**

La publicación reporta una tasa de alucinación del 28% para GLM-5.2 en AA-Omniscience, frente a tasas más altas para Fable 5 y DeepSeek V4 Pro. El benchmark se plantea en torno a si los modelos rehúsan responder o admiten incertidumbre en lugar de adivinar.

Type: Evaluation | Date: 2026-06-20

---


<a id="case-90"></a>
### Case 90: [Índice de Trabajo Agentic GDPval-AA](https://x.com/ArtificialAnlys/status/2069121548670406947) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para comparar GLM-5.2 en trabajo de conocimiento de largo horizonte, en lugar de limitarte a rankings centrados solo en código.**

Artificial Analysis informa que GLM-5.2 alcanza 1524 Elo en GDPval-AA, puesto #3 global detrás de Claude Fable 5 y Opus 4.8, y ligeramente por delante de GPT-5.5 xhigh con 1509. Es el modelo open-weights mejor clasificado con amplio margen, y la publicación dice que el benchmark promedió unas 31 vueltas por tarea en 1,999 enfrentamientos.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-94"></a>
### Case 94: [Subcampeón de Game Dev Arena](https://x.com/Designarena/status/2069166634976371084) (by [@Designarena](https://x.com/Designarena))

**Usa este caso para juzgar la calidad de GLM-5.2 en creación de juegos, donde el modelo alcanzó el segundo puesto en Game Dev Arena y se convirtió en el laboratorio open-weight mejor clasificado en ese ranking.**

Design Arena informó que GLM-5.2 logró 1368 Elo en Game Dev Arena, con una subida de 29 puntos y seis puestos frente a GLM-5.1. La publicación lo sitúa en la misma banda de rendimiento que Claude Fable 5 y dice que quedó segundo en la clasificación general, por delante de OpenAI y solo por detrás de Anthropic a nivel de laboratorio.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-120"></a>
### Case 120: [Líder de confiabilidad PostTrainBench](https://x.com/hrdkbhatnagar/status/2070244540108423427) (by [@hrdkbhatnagar](https://x.com/hrdkbhatnagar))

**Usa este caso para comparar GLM-5.2 Max en fiabilidad de agentes post-training, no solo por la puntuación principal, porque la tabla también informa cero ejecuciones fallidas en 84 tareas.**

hrdkbhatnagar compartió una tabla de PostTrainBench donde GLM 5.2 Max reasoning alcanzó 34.29 %, apenas por encima de Opus 4.8 Max con 34.08 %. El mismo post dice que GLM registró cero ejecuciones fallidas en 84 corridas, frente a una tasa de fallo de alrededor del 10 % en los agentes con Opus, por lo que sirve para equipos que valoran la fiabilidad del agente tanto como la tasa de acierto.

Type: Benchmark | Date: 2026-06-25

---

<a id="case-121"></a>
### Case 121: [Fuegos artificiales + Evaluación del repositorio de tareas 211 de Faros](https://x.com/FireworksAI_HQ/status/2070181898962534570) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Usa este caso para juzgar GLM-5.2 en tareas reales de ingeniería sobre repos privados en lugar de depender solo de benchmarks públicos, porque el resultado publicado incluye puntuación, velocidad y coste por tarea.**

Fireworks dice que una evaluación conjunta con Faros sobre 211 tareas reales de ingeniería encontró a Claude Code + GLM-5.2 por delante de Claude Code + Opus 4.8 y de Codex + GPT-5.5. Las cifras publicadas fueron 0.568 de judge score frente a 0.521 y 0.466, 321 segundos por tarea frente a 775 y 392, y 0.92 dólares por tarea frente a 1.76 y 2.06, además de aclarar que Faros usó sus propios repositorios y trabajo en lugar de solo benchmarks públicos.

Type: Evaluation | Date: 2026-06-25

---

<a id="case-110"></a>
### Case 110: [Frontera de tiempo por tarea del maletín AA](https://x.com/ArtificialAnlys/status/2069914443639635978) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para comparar GLM-5.2 en tareas de conocimiento de largo horizonte donde el tiempo por tarea importa junto con la puntuación del benchmark.**

Artificial Analysis dice que GLM-5.2 se sitúa en la frontera de Pareto de AA-Briefcase con una puntuación de 1261 y un tiempo medio por tarea de 16.3 minutos, por delante de GPT-5.5 xhigh con 1159 y manteniéndose como el mejor modelo open-weights del benchmark. La publicación lo convierte en una referencia útil para equipos que comparan calidad de entregables de largo horizonte frente a tiempo de ejecución, no solo rango bruto en la tabla.

Type: Benchmark | Date: 2026-06-24

---

<a id="case-111"></a>
### Case 111: [Márgenes cara a cara del frontend de Code Arena](https://x.com/arena/status/2069885722333769963) (by [@arena](https://x.com/arena))

**Usa este caso para inspeccionar la ventaja de GLM-5.2 en frontend mediante resultados cara a cara por pares en lugar de depender de una sola captura de clasificación.**

arena desglosa por qué GLM-5.2 Max llegó a la cima de Code Arena: Frontend y dice que obtiene una cuota de victorias superior a la del rival en todos los emparejamientos salvo uno. El hilo destaca 61.0% frente a Kimi-K2.6, 59.4% frente a Sonnet 4.6, 55.0% frente a Opus 4.7 Thinking, un ajustado 41.7% frente a 40.0% contra GPT-5.5 xHigh y un empate 45.5% frente a GLM-5.1.

Type: Benchmark | Date: 2026-06-24

---

<a id="case-113"></a>
### Case 113: [Subcampeón de QnA de SWE Atlas Codebase](https://x.com/ScaleAILabs/status/2069864932913631617) (by [@ScaleAILabs](https://x.com/ScaleAILabs))

**Usa este caso para seguir a GLM-5.2 en Codebase QnA, redacción de pruebas y refactorización en lugar de mirar solo clasificaciones SWE de una sola tarea.**

Scale AI Labs dice que GLM 5.2 ya está disponible en las tres clasificaciones de SWE Atlas: Codebase QnA, Test Writing y Refactoring. La publicación destaca un resultado #2 en Codebase QnA y describe que los modelos abiertos ya compiten con sistemas de frontera en todo el tablero.

Type: Benchmark | Date: 2026-06-24

---

<a id="coding-agents-long-context-workflows"></a>
## 💻 Agentes de código y flujos de contexto largo
<a id="case-168"></a>
### Case 168: [Conjunto Synthwave Hard-Slice a $ 2,66](https://x.com/TracNetwork/status/2073038214592360522) (by [@TracNetwork](https://x.com/TracNetwork))

**Usa este caso para probar GLM-5.2 dentro de un ensemble de coding multi-modelo en vez de usarlo solo, porque TracNetwork informa que una mezcla de Synthwave con GLM logró 46.3 por ciento en LiveCodeBench hard por unos 2.66 dólares y superó a cada generador por separado.**

TracNetwork dice que usó OpenRouter para construir un ensemble de Synthwave con qwen3-coder-next como sintetizador y GLM-5.2 más qwen3.5-122b y qwen3-coder-next como generadores de código. En 82 tareas hard de LiveCodeBench, la publicación reporta 46.3 por ciento por unos 2.66 dólares y afirma que ninguno de los generadores individuales alcanzó ese resultado. Es un ejemplo concreto de GLM-5.2 como parte de un ensemble orientado al costo y no como único modelo de coding.

Type: Integration | Date: 2026-07-03

---

<a id="case-212"></a>
### Case 212: [Tutorial Dell Hub GLM Agent](https://x.com/juanjucm/status/2076714987569963508) (by [@juanjucm](https://x.com/juanjucm))

**Usa este caso si quieres montar un coding agent con GLM-5.2 para un workflow de entrenamiento open-weight, porque juanjucm enlazó una guía nueva que combina la llegada de GLM-5.2-FP8 al catálogo de Dell Enterprise Hub con un recorrido paso a paso para construir un agent alrededor de ese modelo.**

juanjucm cuenta que escribió una guía pública para montar un coding agent basado en GLM-5.2 con el que entrenar dos language models pequeños, y conectó ese tutorial con la incorporación de GLM-5.2-FP8 al catálogo de Dell Enterprise Hub. El artículo enlazado en Hugging Face aporta la parte práctica, mientras que el post lo enmarca como una ruta open-weight para entrenamiento hands-on y experimentos agentic, no como un simple aviso de disponibilidad.

Type: Tutorial | Date: 2026-07-13

---

<a id="case-211"></a>
### Case 211: [Pipeline de informes open-weight con 8xB200](https://x.com/TheZachMueller/status/2076746035758502275) (by [@TheZachMueller](https://x.com/TheZachMueller))

**Usa este caso si quieres poner GLM-5.2 como redactor principal dentro de un pipeline de informes cercano al despliegue local, porque TheZachMueller dice que dividir un nodo 8xB200 en 4/4 le permitió usar GLM 5.2 NVFP4 para redactar y Kimi K2.7 Code para retrieval, sacando un informe de 36 páginas por una fracción del coste de Claude API.**

TheZachMueller explica que, tras dedicar un fin de semana a afinar la configuración, movió un workflow real de trabajo desde Claude Code a Pi dot dev con un stack open-weight. La configuración publicada parte un nodo 8xB200 en dos mitades: GLM 5.2 NVFP4 como agent principal y driver, y Kimi K2.7 Code como retriever. El resultado fue un informe de 36 páginas frente a las 21 del run con Claude. El post también deja claro el tradeoff: el tiempo total pasó de unos 20 minutos a unos 30-40, y la mejora clave de calidad vino de dejar de resumir repetidamente los artículos fuente y guardarlos completos en disco para retrieval más profundo.

Type: Demo | Date: 2026-07-13

---

<a id="case-210"></a>
### Case 210: [Renovación multiagente Liquid Glass de Spettro](https://x.com/spettrotoken/status/2076330234492698844) (by [@spettrotoken](https://x.com/spettrotoken))

**Usa este caso para probar GLM-5.2 como solucionador de frontend con mucha investigación dentro de una renovación web multiagente, porque spettrotoken dice que GLM 5.2 usó herramientas integradas de web scraping y data fetching para entregar una implementación cross-browser de Liquid Glass que funcionó en Firefox después de que Fable 5 y GPT-5.5 fallaran.**

spettrotoken cuenta que una renovación real del sitio de Spettro se dividió entre cuatro instancias de Spettro, cada una dueña de una parte distinta del frontend, mientras GLM-5.2 se encargó del componente visual más difícil: un efecto refractivo Liquid Glass que normalmente se rompe en Firefox. El post dice que GLM 5.2 rastreó la web, leyó workarounds de filtros CSS y SVG, hizo ingeniería inversa del efecto y entregó una implementación cross-browser que se desplegó en el sitio en producción, con Kimi K2.7 y subagentes en paralelo apoyando la renovación más amplia.

Type: Demo | Date: 2026-07-12

---

<a id="case-194"></a>
### Case 194: [Habilidad del kernel CuTeDSL de código abierto](https://x.com/SubhoGhosh02/status/2074466050557739469) (by [@SubhoGhosh02](https://x.com/SubhoGhosh02))

**Usa este caso para estudiar GLM-5.2 dentro de una skill reutilizable de depuración de kernels, porque el autor liberó una skill de Hermes para CuTeDSL y dice que GLM-5.2 fue especialmente eficiente en coste al depurar y escribir kernels.**

El post dice que la mayor parte de la skill se construyó mediante conversaciones agentic en Hermes con varios modelos, y que GLM-5.2 destacó por su eficiencia de coste durante el debugging y la escritura de kernels. La fuente también da los comandos exactos de instalación y arranque, `hermes skills install ighoshsubho/awesome-kernel-skills/cutedsl-kernels` y `hermes chat -s cutedsl-kernels`, lo que lo convierte en un workflow reutilizable de estilo tutorial y no en un elogio vago.

Type: Tutorial | Date: 2026-07-07

---
<a id="case-180"></a>
### Case 180: [Bucle de habilidades de recuperación de SSD de Hermes](https://x.com/ShankhadeepSho1/status/2073658918937473444) (by [@ShankhadeepSho1](https://x.com/ShankhadeepSho1))

**Usa este caso para probar GLM-5.2 dentro de un loop de agente orientado a reparación, porque ShankhadeepSho1 dice que Hermes más GLM 5.2 diagnosticó un SSD fallido de un NAS, arregló el problema y empaquetó la solución como una skill reutilizable.**

El autor dice que un SSD de un QNAP NAS murió, lo movió a una máquina de repuesto y se lo entregó a Hermes para diagnóstico. El resultado publicado es inusualmente concreto para un workflow de agentes: supuestamente el stack reparó el problema, creó una skill para sí mismo y actualizó la wiki de infraestructura con la estrategia de recuperación.

Type: Demo | Date: 2026-07-05

---
<a id="case-174"></a>
### Case 174: [Pila de codificador de servicio pesado enrutado por roles](https://x.com/denizirgin/status/2073462071639876004) (by [@denizirgin](https://x.com/denizirgin))

**Usa este caso para asignar GLM-5.2 como coder pesado dentro de una pila personal con routing por roles, porque denizirgin dice que un mes de pruebas con Codex y OpenCode le llevó a enviar el trabajo de coding más pesado a GLM 5.2 manteniendo el presupuesto mensual total en unos 120 a 140 dólares.**

denizirgin dice que su configuración actual combina Codex, OpenCode, DeepSeek, OpenRouter y una skill propia de sub-agents con una decision table para coding, review, research, speed y cost. En ese esquema, GLM 5.2 actúa como heavy-duty coder a través de un proveedor complementario, mientras Codex queda como backbone principal y OpenRouter se usa de forma más selectiva para probar modelos. Es una nota práctica de workflow con sensibilidad a coste, no una clasificación genérica de modelos.

Type: Evaluation | Date: 2026-07-04

<a id="case-155"></a>
### Case 155: [Bucle TUI de cuatro agentes de Cotal](https://x.com/silvanrec/status/2072335315822403656) (by [@silvanrec](https://x.com/silvanrec))

**Use este caso para dividir un bucle de codificación entre agentes especializados, porque el autor usó dos workers con GLM-5.2 bajo un líder Opus y un revisor GPT para terminar una TUI estilo lazygit en 47 minutos sin intervención humana.**

silvanrec dice que Cotal coordinó cuatro modelos: dos instancias de GLM-5.2 como desarrolladores de frontend y backend, GPT-5.5 como revisor en segundo plano y Claude Opus como líder del bucle. A partir de un único prompt para construir una consola TUI real, el sistema ejecutó cuatro rondas, detectó bugs de renderizado y cableado de pestañas, gestionó handoffs entre agentes y produjo un resultado funcional en 47 minutos. La publicación también apunta a la capa open source con npx cotal-ai setup --full.

Type: Demo | Date: 2026-07-01

---

<a id="case-153"></a>
### Case 153: [Piloto de reducción de costos de migración heredada](https://x.com/chamath/status/2072390507628540213) (by [@chamath](https://x.com/chamath))

**Use este caso para valorar GLM-5.2 como el trabajador más barato dentro de una modernización de aplicaciones heredadas, porque el piloto de 8090 dice que GLM más Software Factory redujo el costo 16,4 veces frente a Opus 4.8 solo, aunque fue unas 3 veces más lento.**

Chamath compartió un piloto inicial de modernización de PHP a Next.js. Opus 4.8 con Software Factory de 8090 fue 1,4 veces más barato y 1,5 veces más rápido que Opus solo, mientras que la misma fábrica con GLM 5.2 redujo el costo 16,4 veces frente a Opus solo, aunque corrió unas 3 veces más lento. La publicación aclara que el resultado es direccional, con n igual a 1, y que debe repetirse en 10 a 15 tareas reales de modernización.

Type: Evaluation | Date: 2026-07-01

---


<a id="case-150"></a>
### Case 150: [Bucle local para uso del navegador Mac Studio](https://x.com/MaziyarPanahi/status/2071955191260151862) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Usa este caso para probar si una pila totalmente local de GLM-5.2 puede hacer trabajo ligero de browser agent en hardware de consumo, porque el autor ejecutó llama.cpp en un Mac Studio y usó browser-use para encontrar un modelo de PII en Hugging Face.**

MaziyarPanahi dice que ejecutó GLM-5.2 localmente en un Mac Studio mediante llama.cpp y luego lo envolvió en un loop con browser-use. En el ejemplo publicado, el modelo navega por Hugging Face e identifica `privacy-filter-nemotron`.

Type: Demo | Date: 2026-06-30

---

<a id="case-148"></a>
### Case 148: [Reducción de costos de intercambio de agentes de Gumloop](https://x.com/aronkor/status/2072032854675218538) (by [@aronkor](https://x.com/aronkor))

**Usa este caso para probar una sustitución directa de modelo dentro de un harness existente, porque Gumloop dice que movió sus agentes más usados a GLM-5.2 con cerca de 50% menos créditos y sin caída visible de calidad.**

aronkor describe un experimento interno de Gumloop en el que sustituyeron sus agentes más usados por GLM 5.2 manteniendo el mismo harness y prompt. El resultado comunicado es que nadie notó una diferencia clara en la salida y el consumo de créditos cayó casi a la mitad.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-13"></a>
### Case 13: [Bucle de refactorización de una hora cuarenta y dos minutos](https://x.com/KELMAND1/status/2066012493315723610) (by [@KELMAND1](https://x.com/KELMAND1))

**Utilice este caso como patrón para una refactorización frontal autónoma prolongada con TDD, comentarios de los revisores y comprobaciones de regresión.**

La publicación describe una tarea de refactorización de GLM-5.2 de 1 hora y 42 minutos con 88 giros de modelo y 102 llamadas de herramientas. El flujo de trabajo incluyó una transferencia, cuatro correcciones de bloqueadores, implementación TDD de 12 pruebas, dos rondas de correcciones P2 y una regresión final.

Type: Demo | Date: 2026-06-14

---

<a id="case-14"></a>
### Case 14: [Prueba de implementación y corrección de errores de OpenCode](https://x.com/altudev/status/2065868921341632881) (by [@altudev](https://x.com/altudev))

**Utilice este caso para probar GLM-5.2 como agente de codificación OpenCode para corregir errores además de una pequeña tarea de implementación.**

El autor informa que probó GLM-5.2 con seis correcciones de errores y una implementación en OpenCode, y dice que los cambios se realizaron de manera limpia con una planificación sólida y mejor velocidad que GLM-5.1.

Type: Demo | Date: 2026-06-13

---

<a id="case-15"></a>
### Case 15: [Tutorial del videojuego OpenCode Retro](https://x.com/AskVenice/status/2067047775783534789) (by [@AskVenice](https://x.com/AskVenice))

**Utilice este tutorial para crear un juego pequeño con GLM-5.2 y OpenCode desde un solo mensaje y luego inspeccione cómo el modelo maneja los detalles de implementación.**

Venice compartió un tutorial completo para crear un videojuego retro con GLM-5.2 y OpenCode, posicionándolo como un flujo de trabajo de codificación privado, de código abierto y de largo horizonte.

Type: Tutorial | Date: 2026-06-17

---

<a id="case-16"></a>
### Case 16: [Concurso de Simulaciones de Física HTML5](https://x.com/atomic_chat_hq/status/2067038851139334588) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Utilice este caso para comparar el código GLM-5.2 y Kimi K2.7 en simulaciones de física HTML5 autónomas sin bibliotecas.**

Atomic Chat informó que pidió a ambos modelos que construyeran simulaciones de rotura de piscina, bloques de resorte y tablero Galton. Su publicación dice que GLM-5.2 manejó los tres con más detalle y pulido, mientras que Kimi tuvo problemas con el comportamiento físico.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-17"></a>
### Case 17: [Creación de UX de interfaz de usuario de sitio personal](https://x.com/anshuc/status/2067034697704857615) (by [@anshuc](https://x.com/anshuc))

**Utilice este caso para solicitar a GLM-5.2 un sitio personal pulido e inspeccionar hasta qué punto múltiples turnos pueden mejorar la UI/UX.**

El autor dice que GLM-5.2 produjo un sitio personal creativo después de ser impulsado con las indicaciones correctas y compartió un video del resultado. Es útil para la iteración del diseño de front-end en lugar de para afirmaciones de referencia de un solo disparo.

Type: Demo | Date: 2026-06-17

---

<a id="case-18"></a>
### Case 18: [Creación de productos de revisión de contratos de IA](https://x.com/laozhang2579/status/2066339734956499301) (by [@laozhang2579](https://x.com/laozhang2579))

**Utilice este caso para evaluar GLM-5.2 en una tarea de creación de productos con un PRD, presupuesto de tiempo, recuento de pasos, cuota de uso y comparación de calidad del código.**

La publicación china compara GLM-5.2, Kimi K2.7 y Claude Opus 4.8 en un producto PRD de revisión de contratos de IA. Informa la duración de la compilación, el recuento de pasos, el uso de la cuota de cinco horas y la puntuación de la calidad del código.

Type: Evaluation | Date: 2026-06-15

---

<a id="case-19"></a>
### Case 19: [Función de objetivo de ZCode para objetivos de desarrollo más amplios](https://x.com/zcode_ai/status/2066236605917188228) (by [@zcode_ai](https://x.com/zcode_ai))

**Utilice este caso para comprender cómo se integra GLM-5.2 en ZCode 3.0 para tareas de desarrollo agente más grandes.**

ZCode anunció la disponibilidad de GLM-5.2 para los usuarios del plan de codificación, una ejecución más sólida de las tareas del agente, una mejor codificación de contexto largo y una función de objetivo para gestionar objetivos más grandes desde la planificación hasta su finalización.

Type: Integration | Date: 2026-06-14

---

<a id="case-20"></a>
### Case 20: [Envoltorio de Linux para ZCode creado con GLM-5.2](https://x.com/gosrum/status/2066484949755269510) (by [@gosrum](https://x.com/gosrum))

**Utilice este caso como ejemplo de cómo GLM-5.2 ayuda con herramientas en entornos de agentes de codificación.**

El autor informa haber completado zcode-linux utilizando GLM-5.2 y Claude Code para que los usuarios de Linux puedan ejecutar ZCode en un entorno Linux y agregar puntos finales API arbitrarios, incluidos puntos finales LLM locales.

Type: Demo | Date: 2026-06-15

---

<a id="case-21"></a>
### Case 21: [Empaquetado de habilidades para el uso de la computadora](https://x.com/0xSero/status/2065952130054382079) (by [@0xSero](https://x.com/0xSero))

**Utilice este caso para estudiar GLM-5.2 como ayuda para convertir un repositorio de uso de computadora de código abierto en una habilidad reutilizable.**

La publicación dice que GLM-5.2 estaba configurando el uso de la computadora, encontró un repositorio avanzado de código abierto y lo convirtió en una habilidad. Es una señal práctica para el trabajo de integración de agentes y envoltura de herramientas.

Type: Demo | Date: 2026-06-14

---

<a id="case-22"></a>
### Case 22: [Revisión del entorno de desarrollo agente ZCode 3.0](https://x.com/laogui/status/2066190262993559963) (by [@laogui](https://x.com/laogui))

**Utilice este caso para evaluar GLM-5.2 dentro de un entorno de desarrollo agente completo en lugar de una única sesión de chat.**

La revisión china dice que ZCode 3.0 fue reescrito a partir de versiones anteriores tipo shell en un núcleo de agente de desarrollo propio junto con GLM-5.2, con una mejor experiencia entre los entornos de desarrollo de agentes nacionales.

Type: Demo | Date: 2026-06-14

---

<a id="case-62"></a>
### Case 62: [Arnés OpenCode con servicio local](https://x.com/PatrickToulme/status/2068134212587184442) (by [@PatrickToulme](https://x.com/PatrickToulme))

**Utilice este caso para probar GLM-5.2 con el arnés OpenCode, el servicio local y los flujos de trabajo de codificación con muchas herramientas antes de compararlo con Claude Opus.**

El autor informa sobre una implementación local, subagentes anidados, comportamiento de investigación/planificación y una compilación de aplicación funcional.

Type: Evaluation | Date: 2026-06-20

---

<a id="case-65"></a>
### Case 65: [Inyección de instrucciones de contexto largo Fast-RLM](https://x.com/neural_avb/status/2067992817625088439) (by [@neural_avb](https://x.com/neural_avb))

**Utilice este caso para mejorar el recuento de contexto largo de GLM-5.2 y el comportamiento del agente REPL moviendo instrucciones al indicador del sistema RLM.**

Las notas de la versión describen un cambio concreto en el andamiaje del agente y un efecto de referencia de contexto largo de GLM-5.2.

Type: Integration | Date: 2026-06-20

---

<a id="case-66"></a>
### Case 66: [Prueba de arnés abierto de código DeepAgents](https://x.com/sydneyrunkle/status/2067947260369854830) (by [@sydneyrunkle](https://x.com/sydneyrunkle))

**Utilice este caso para probar GLM-5.2 con un arnés de agente de codificación abierto y compare el modelo bajo un shell de agente reproducible.**

El autor informa que utiliza GLM-5.2 con DeepAgents Code y marcos de modelo abierto más arnés abierto como patrón de prueba.

Type: Demo | Date: 2026-06-20

---

<a id="case-77"></a>
### Case 77: [Enrutamiento de stack de agentes de marketing en producción](https://x.com/DeRonin_/status/2068303752671477820) (by [@DeRonin_](https://x.com/DeRonin_))

**Usa este caso para enrutar GLM-5.2 a workflows de agentes en producción que valoran estructura, velocidad y self-hosting, manteniendo modelos cerrados más fuertes para juicios ambiguos.**

Tras una ejecución comparativa de seis días en un stack de agencia, el autor dice que GLM-5.2 sostuvo más de 60 pasos de agente antes de desviarse, respetó formatos estructurados más de 800 veces seguidas y entregó respuestas self-hosted de baja latencia. La misma publicación sigue prefiriendo Opus para tareas críticas de voz o ambiguas, así que la propia regla de enrutamiento es la conclusión útil.

Type: Evaluation | Date: 2026-06-20

---



<a id="case-80"></a>
### Case 80: [Recreación de Pokemon Red en M3 Ultra](https://x.com/hxiao/status/2068800750554378434) (by [@hxiao](https://x.com/hxiao))

**Usa este caso para evaluar GLM-5.2 en una ejecución local de agente de código a largo plazo, donde el modelo pasó alrededor de medio día intentando recrear Pokemon Red en HTML en una máquina M3 Ultra.**

El autor cambió el modelo de Claude Code por GLM 5.2 local en una máquina M3 Ultra de 512 GB y ejecutó durante 12 horas la tarea `/goal replicate Pokemon Red in HTML, make no mistakes, verify it end-to-end.`. La publicación comparte tiempo de ejecución, uso de tokens, churn de código, uso de RAM y la configuración de GGUF más KV-cache, al tiempo que señala que la calidad del modelo se sintió de nivel frontier pero que el throughput de inferencia local fue el cuello de botella.

Type: Demo | Date: 2026-06-21

---
<a id="case-91"></a>
### Case 91: [Enfrentamiento de corrección de errores del repositorio de Cline](https://x.com/cline/status/2069171146994729078) (by [@cline](https://x.com/cline))

**Usa este caso para comparar GLM-5.2 y Opus 4.8 en la corrección de un bug de un repositorio real, donde GLM gastó más tokens pero entregó el parche final más barato y más limpio.**

Cline probó ambos modelos sobre el mismo bug del repo Cline con el mismo harness y las mismas herramientas. La publicación dice que GLM usó cerca de 1.1M tokens frente a 660K de Opus, costó $0.41 frente a $0.81, tardó 4.7 minutos y 28 llamadas a herramientas frente a 1.6 minutos y 12 llamadas, y terminó con limpieza de código muerto y build de producción exitosa, mientras Opus dejó errores de tipos que aun así pasaban las pruebas.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-102"></a>
### Case 102: [Agente en segundo plano OpenInspect FP8](https://x.com/colemurray/status/2069485572339707938) (by [@colemurray](https://x.com/colemurray))

**Usa este caso para estudiar un stack de agente en segundo plano autoalojado con GLM-5.2 en lugar de un flujo de chat alojado.**

Cole Murray compartió un stack de OpenInspect, remote code runner y Fireworks FP8 GLM-5.2 que ejecuta agentes en segundo plano sobre infraestructura autoalojada. La publicación presenta la configuración como una alternativa abierta a los productos de agentes alojados y enlaza a un runbook ya publicado.

Type: Integration | Date: 2026-06-23

---

<a id="case-145"></a>
### Case 145: [Migración de ahorro con OpenCode y Fireworks](https://x.com/SeekingN0rth/status/2071484711327985696) (by [@SeekingN0rth](https://x.com/SeekingN0rth))

**Usa este caso para probar si basta con cambiar a un harness de open models, porque el autor movió sus tareas personales de coding y loops a GLM-5.2 sobre Fireworks más OpenCode y dice que la factura de tokens cayó a un tercio sin una pérdida clara de calidad diaria.**

SeekingN0rth dice que una migración de fin de semana de sus tareas personales de coding y loops a GLM 5.2 sobre Fireworks con OpenCode redujo el gasto en tokens a aproximadamente un tercio. El hilo sostiene que el harness importó más que el estatus frontier: OpenCode se sintió comparable a Claude Code en terminal, no hubo una caída significativa de calidad en tareas cotidianas y el ejemplo se plantea como un patrón de cambio de modelo que también podrían aplicar empresas grandes cuando el coste pesa más que el rendimiento SOTA absoluto.

Type: Evaluation | Date: 2026-06-29

---

<a id="case-143"></a>
### Case 143: [Flujo con agregador GLM en Hermes MoA](https://x.com/IBuzovskyi/status/2071601107944571249) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**Usa este caso cuando un turno de agente de alto valor justifique más orquestación, porque la configuración Mixture of Agents de Hermes Agent combinó GLM-5.2 con otros modelos y logró una salida visiblemente mejor con un aumento pequeño de coste por tarea en el demo publicado.**

IBuzovskyi explica el modo Mixture of Agents de Hermes Agent como un modelo agregador con acceso a herramientas más varios modelos de referencia que solo aportan consejo privado. El hilo reporta una prueba de coding en la que GLM 5.2 en solitario tardó 13 minutos y costó 0.38 dólares, mientras que un agregador GLM 5.2 con Kimi K2.6 y MiniMax M3 tardó 35 minutos y costó 0.47 dólares, pero produjo animaciones más fluidas, mejores visuales y mecánicas de juego más limpias. También detalla cómo diseñar presets, dónde activar la función y cuándo compensa esa latencia extra.

Type: Integration | Date: 2026-06-29

---

<a id="case-142"></a>
### Case 142: [Diferencia del harness con reasoning en Cline](https://x.com/akshay_pachaar/status/2071638409022763292) (by [@akshay_pachaar](https://x.com/akshay_pachaar))

**Usa este caso para evaluar el diseño del harness y no solo los pesos del modelo, porque el mismo GLM-5.2 pasó de 57.3% a 68.5% en las mismas tareas de coding cuando el harness activó reasoning.**

akshay_pachaar cita una prueba de Cline en la que GLM 5.2 resolvió el mismo conjunto de tareas de coding de dos maneras: 57.3% con reasoning apagado y 68.5% con reasoning encendido. El hilo usa esa diferencia para sostener que la continuidad del contexto, el acceso a herramientas, la aplicación de ediciones y los loops de verificación pueden importar tanto como el modelo base cuando lo que quieres es código entregable y no solo texto.

Type: Evaluation | Date: 2026-06-29

<a id="case-136"></a>
### Case 136: [Prueba de campo de 455M tokens con Cursor + Fireworks](https://x.com/robinebers/status/2071246749210190132) (by [@robinebers](https://x.com/robinebers))

**Usa este caso para juzgar GLM-5.2 como un modelo serio para el uso diario en Cursor, porque el autor informa 455M tokens de uso real con serving rápido de Fireworks y sin ganas inmediatas de volver a Opus o GPT-5.5.**

robinebers dice que cambiar durante 36 horas a GLM 5.2 en Cursor le hizo cambiar de opinión sobre el modelo una vez que lo emparejó con Fireworks. La publicación destaca en concreto soporte de imágenes, supuesta retención cero de datos, throughput de unas 80-100 tokens por segundo y un gasto aproximado de 145 dólares para 455 millones de tokens. Eso lo convierte en una evaluación más concreta del harness que el elogio genérico de benchmarks, con evidencia práctica de que la elección del proveedor puede cambiar la experiencia real.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-135"></a>
### Case 135: [Arnés de Devin Desktop con portabilidad de skills](https://x.com/lily_gpupoor/status/2071297351801794850) (by [@lily_gpupoor](https://x.com/lily_gpupoor))

**Usa este caso para probar GLM-5.2 dentro de Devin Desktop cuando la propia superficie de coding de Z.ai se sienta inestable, porque el autor informa portabilidad de skills más fácil, mayor velocidad y mejor capacidad de hackeo.**

lily_gpupoor dice que usar GLM-5.2 intensivamente a través de Devin Desktop se sintió materialmente mejor que el plan de coding directo de Z.ai durante un periodo de inestabilidad de API. La publicación destaca tres victorias de workflow concretas: GLM editó un JSON personalizado del tema Solarized Green y registró la extensión correctamente, Devin se sintió inusualmente rápido y la mayoría de los skills ya construidos se trasladaron casi sin cambios tras pasar del agente predeterminado Windsurf Cascade a Devin Local.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-127"></a>
### Case 127: [Revisor GLM en línea de Pi](https://x.com/xpasky/status/2070831715518460177) (by [@xpasky](https://x.com/xpasky))

**Usa este caso para añadir un segundo revisor a un loop de agente de código estilo Pi, porque el autor informa que GLM-5.2 puede asesorar a Opus turno a turno por un aumento de coste de alrededor del 10%.**

xpasky dice que los usuarios de Pi pueden copiar un patrón estilo OMP en el que un segundo modelo revisa cada turno e inyecta consejo en línea. La publicación menciona en concreto a GLM 5.2 observando a Opus de forma continua, dice que la pareja parece "discutir" visiblemente y estima que ese revisor extra de GLM añade alrededor de un 10% al coste medio de la API de Opus. Eso lo convierte en un patrón concreto de supervisión multimodelo y no en un cambio completo de modelo.

Type: Integration | Date: 2026-06-27

---

<a id="case-122"></a>
### Case 122: [Bot de Telegram de un solo uso con AgentRouter](https://x.com/MatinSenPai/status/2070259817818812701) (by [@MatinSenPai](https://x.com/MatinSenPai))

**Usa este caso para probar si GLM-5.2 puede inferir decisiones orientadas a producción en una build one-shot con agente de código, en lugar de limitarse a generar el camino mínimo que funciona.**

MatinSenPai cuenta que construyó un bot de Telegram de una sola vez con GLM 5.2 usando el mismo prompt del vídeo y que el modelo añadió detalles prácticos sin que se los pidieran. El post destaca limpieza automática de archivos tras enviar vídeos, respeto por los límites del Bot API de Telegram con un tope por defecto de 50 MB, auto-pruebas repetidas antes de terminar, una estructura más limpia que una build anterior con MiMo y unas 140K tokens o alrededor de 5 dólares de uso reportado a través de AgentRouter.

Type: Demo | Date: 2026-06-25

---

<a id="case-117"></a>
### Case 117: [Ganancia del primer paso de OpenCode Go Refactor](https://x.com/vedovelli74/status/2069889605969592500) (by [@vedovelli74](https://x.com/vedovelli74))

**Usa este caso para evaluar GLM-5.2 en refactorizaciones medianas de Go dentro de OpenCode en lugar de apoyarte solo en afirmaciones de benchmark.**

vedovelli74 informa de una primera ejecución de OpenCode sobre una refactorización de una base de código Go de tamaño medio y dice que GLM-5.2 fue más rápido que Opus 4.8, más eficiente en tokens y correcto en la primera evaluación de lo que había que refactorizar. Añade que luego validó el resultado frente a Codex y Opus y que GLM siguió saliendo por delante en calidad de entrega.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-119"></a>
### Case 119: [Código Claude + Cursor $3.36 Ejecución predeterminada](https://x.com/clairevo/status/2069828122640548204) (by [@clairevo](https://x.com/clairevo))

**Usa este caso para medir GLM-5.2 como modelo diario en Claude Code y Cursor antes de mover más trabajo autónomo de programación a pesos abiertos.**

clairevo dice que GLM 5.2 se ha convertido en el modelo predeterminado en Claude Code y Cursor con un coste acumulado de $3.36, mientras transmite una calidad de programación similar a Opus. La publicación también apunta a una ruta de configuración con OpenRouter, impresiones de diseño front-end y una revisión de una tarea autónoma de larga duración como motivos por los que terminó convenciéndole.

Type: Evaluation | Date: 2026-06-24

---

<a id="hands-on-demos-showcase-builds"></a>
## 🎮 Demos prácticas y muestras
<a id="case-218"></a>
### Case 218: [Rebuild de portfolio y SO con OpenCode](https://x.com/MarkSShenouda/status/2077032282141978842) (by [@MarkSShenouda](https://x.com/MarkSShenouda))

**Usa este caso para medir GLM-5.2 en builds ambiciosas con OpenCode, porque MarkSShenouda dice que OpenCode Go más GLM-5.2 ayudó a rehacer un sitio de portfolio y un sistema operativo real escrito en C y Assembly que corre en WASM o en un emulador Qemu.**

El post vincula GLM-5.2 con dos artefactos ya construidos y no con una demo de juguete: un portfolio rehecho y un proyecto de sistema operativo implementado en C y Assembly con objetivos para WASM y Qemu. Aunque el tweet es breve, las dos vistas previas enlazadas lo convierten en una muestra concreta de trabajo maker y de coding más grande.

Tipo: Demostración | Fecha: 2026-07-14

---
<a id="case-213"></a>
### Case 213: [Reconstrucción GLM de LlamaCoder v4](https://x.com/nutlope/status/2076722464671793184) (by [@nutlope](https://x.com/nutlope))

**Usa este caso si quieres prototipar un workflow de generación de apps con un solo prompt apoyándote en las fortalezas de GLM-5.2 para planning y diseño, porque nutlope dice que LlamaCoder v4 fue rehecho alrededor de GLM 5.2, mejoró parsing y planning y ahora entrega un renderer WebAssembly dentro de un stack gratuito y open source.**

nutlope dice que LlamaCoder v4 ahora gira en torno a GLM 5.2, cambió la capa de UI a Base UI with shadcn, mejoró parsing, planning y app design, y añadió un renderer basado en WebAssembly. El proyecto se presenta como gratuito, open source y powered by Together, así que aquí hay una demo entregada y reutilizable, no solo una opinión vaga sobre calidad de modelo.

Type: Demo | Date: 2026-07-13

---

<a id="case-202"></a>
### Case 202: [Función de disparo espacial con código de comando](https://x.com/CommandCodeAI/status/2075264795817972107) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Usa este caso para comparar GLM-5.2 en builds de UI interactiva de un solo prompt, porque Command Code ejecutó el mismo prompt de space shooter retro con Fable 5, GPT 5.5, GLM 5.2 y DeepSeek V4 Pro, y colocó a GLM como el mejor en features por $0.07.**

Command Code dice que el mismo prompt de `/design` produjo layouts retro pixel-art de space shooter bastante parecidos en los cuatro modelos, pero GLM 5.2 destacó en features como sonido, controles, sistema de niveles y UX general, mientras costó $0.07 frente a $0.80 de Fable 5. Eso lo convierte en una comparación práctica para builds ligeras de juegos y UI, no en una simple captura de benchmark.

Type: Evaluation | Date: 2026-07-09

---

<a id="case-200"></a>
### Case 200: [Emulador ZCode Nintendo DS](https://x.com/0xSero/status/2074870153267818638) (by [@0xSero](https://x.com/0xSero))

**Usa este caso para inspeccionar una build local de coding de largo recorrido, porque el autor ejecutó GLM-5.2 en ZCode sobre 4x RTX 6000 con el objetivo de construir desde cero un emulador de Nintendo DS en C++.**

La fuente muestra a GLM-5.2 corriendo dentro de ZCode sobre una configuración de cuatro GPU RTX 6000 y fija un objetivo concreto: construir un emulador de Nintendo DS en C++ sin usar uno ya hecho, y seguir hasta que arranque la ROM de Mario 64 DS. Eso lo convierte en una demo real de coding agent con un estado final duro, en lugar de una vaga afirmación de 'hice una app de juguete'.

Type: Demo | Date: 2026-07-08

---
<a id="case-192"></a>
### Case 192: [Código de comando Flappy Bird UX Split](https://x.com/MrAhmadAwais/status/2074536879308026031) (by [@MrAhmadAwais](https://x.com/MrAhmadAwais))

**Usa este caso para comparar GLM-5.2 en tareas ligeras de diseño y juego, porque el autor pasó el mismo prompt de Flappy Bird por Command Code y concluyó que Fable 5 no fue significativamente mejor en UX pese a costar casi nueve veces más que GLM-5.2.**

El post dice que el experimento usó el mismo prompt del juego y la misma configuración `/design` de Command Code en DeepSeek V4 Pro, GLM 5.2 y Fable 5. GLM 5.2 quedó entre DeepSeek y Fable en precio bruto, pero el autor afirma que Fable no mostró una ventaja de UX lo bastante grande como para justificar la diferencia de precio. Por eso funciona como comparación práctica de UX frente a coste, y no como una simple afirmación de arena.

Type: Evaluation | Date: 2026-07-07

---
<a id="case-161"></a>
### Case 161: [REAP NVFP4 Cubo de Rubik One-Shot](https://x.com/RoundtableSpace/status/2072700573145788914) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Usa este caso para probar GLM-5.2 en tareas interactivas de construcción con un solo prompt, porque la demo REAP-NVFP4 afirma que un único prompt produjo un cubo de Rubik 3D con scrambles reales, estado en vivo y botón de resolver.**

RoundtableSpace dice que a GLM-5.2-REAP-NVFP4 se le dio solo un prompt HTML y devolvió una app funcional de cubo de Rubik 3D con estado en vivo, lógica real de scramble y acción de resolver. El post no publica mucho código, pero sigue siendo una demo concreta de one-shot build y no una captura genérica de benchmark.

Type: Demo | Date: 2026-07-02

---

<a id="case-158"></a>
### Case 158: [Cliente OMP Relay para iPhone](https://x.com/mov_axbx/status/2072192903762288721) (by [@mov_axbx](https://x.com/mov_axbx))

**Use este caso para envolver rápidamente un agente local con GLM-5.2 en una superficie móvil, porque el autor dice que el plugin build-ios-app de Codex produjo en un par de horas un cliente pulido para iPhone sobre un relay OMP que ya usaba GLM-5.2 y túneles de Cloudflare.**

mov_axbx dice que quería una app de teléfono para un agente OMP alojado localmente, usó el plugin build-ios-app de Codex y obtuvo una versión pulida en un par de horas. La ruta de backend usaba un relay personalizado escrito con GLM-5.2 y OMP, mientras Cloudflare se encargaba del túnel.

Type: Demo | Date: 2026-07-01

---


---

<a id="case-144"></a>
### Case 144: [Agente open source de investigación DevRel](https://x.com/Astrodevil_/status/2071572680470655253) (by [@Astrodevil_](https://x.com/Astrodevil_))

**Usa este caso para convertir GLM-5.2 en un asistente de investigación vertical y no en un chat genérico, porque el autor creó un agente DevRel open source que transforma producto y audiencia en oportunidades de contenido clasificadas con evidencia y esquemas.**

Astrodevil_ creó una app chat-first de investigación DevRel sobre GLM-5.2 que recibe una descripción del producto y de la audiencia, busca señales de demanda en Hacker News, revisa huecos de contenido en DEV, actualiza hechos con Engram memory y devuelve ideas de temas priorizadas con evidencia y esquemas. El post también nombra la pila: Agno, Weaviate Engram, inferencia de Nebius y un código abierto.

Type: Demo | Date: 2026-06-29

<a id="case-123"></a>
### Case 123: [Refundido del bucle de página de destino de seis variaciones](https://x.com/nutlope/status/2070199649818779914) (by [@nutlope](https://x.com/nutlope))

**Usa este caso para prototipar landing pages de forma barata generando primero varias variantes con GLM-5.2 y llevando luego la mejor a un agente de código.**

nutlope describe un flujo de iteración web basado en GLM 5.2 y Recast: generar seis variaciones de landing page desde un solo prompt, elegir el mejor diseño, descargar ese código y seguir iterando en otro agente de programación. El autor dice que GLM-5.2 funciona bien aquí porque es rápido, barato y fuerte en diseño, y afirma que con el mismo presupuesto suele poder producir de tres a seis variantes con GLM por cada página generada con Opus 4.8.

Type: Tutorial | Date: 2026-06-25

---

<a id="case-23"></a>
### Case 23: [Trastiendas jugables One-Shot](https://x.com/aimlapi/status/2066996493257408639) (by [@aimlapi](https://x.com/aimlapi))

**Utilice este caso para comparar el resultado, el tiempo de ejecución y el costo de creación de juegos con el mismo sistema entre GLM-5.2 y Opus 4.8.**

AI/ML API informó haber pedido a GLM-5.2 y Opus 4.8 realizar un one-shot en un juego de Backrooms jugable. Su publicación dice que el GLM-5.2 construyó una mecánica más completa en 1:08 a $0,37, mientras que Opus tardó 2:14 a $1,94.

Type: Demo | Date: 2026-06-16

---

<a id="case-24"></a>
### Case 24: [Tres construcciones reales con resultados mixtos](https://x.com/bridgemindai/status/2065840871929442319) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso como conjunto de demostración de advertencia: pruebe varias compilaciones reales antes de confiar en un modelo para tareas de producción de juegos o videos.**

BridgeMind probó GLM-5.2 en un juego de terror, un juego de sigilo en 3D y un vídeo de marketing de Remotion. La publicación informa resultados mixtos, incluida una lógica de juego rota, lo que la hace útil como señal de limitación fundamentada.

Type: Evaluation | Date: 2026-06-13

---

<a id="case-25"></a>
### Case 25: [Clon de Super Mario en ZCode](https://x.com/ivanfioravanti/status/2066272681406980208) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilice este caso para evaluar la creación de juegos iterativos con GLM-5.2 y ZCode en varias pasadas de corrección y funciones.**

El autor probó ZCode 3.0 con GLM-5.2 creando un clon al estilo de Super Mario y luego compartió el resultado después de cinco iteraciones de correcciones de problemas y adiciones de funciones.

Type: Demo | Date: 2026-06-14

---

<a id="case-26"></a>
### Case 26: [Concurso de módulo de aterrizaje lunar](https://x.com/ivanfioravanti/status/2066193134984319173) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Utilice este caso para comparar GLM-5.2, MiniMax M3 y Kimi K2.7 Code en una tarea de estilo de juego interactivo.**

La publicación describe un concurso de Lunar Lander entre MiniMax M3, GLM-5.2 y Kimi K2.7 Code, utilizando un resultado de video como punto de referencia práctico antes de regresar al desarrollo del modelo local.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-27"></a>
### Case 27: [Creación de arena de diseño en un solo momento](https://x.com/grx_xce/status/2066951779154374907) (by [@grx_xce](https://x.com/grx_xce))

**Utilice este caso para inspeccionar lo que GLM-5.2 puede generar a partir de un único mensaje de diseño en un contexto de arena.**

El autor compartió un ejemplo de una creación de GLM-5.2 en Design Arena realizada a partir de un mensaje, usándolo para mostrar la brecha cada vez menor entre los modelos de peso abierto y cerrado.

Type: Demo | Date: 2026-06-16

---

<a id="case-28"></a>
### Case 28: [Trabajo de investigación: comprensión del flujo de trabajo](https://x.com/askalphaxiv/status/2066996976445706745) (by [@askalphaxiv](https://x.com/askalphaxiv))

**Utilice este caso para aplicar GLM-5.2 a flujos de trabajo de lectura de artículos con preguntas contextuales y referencias entre artículos.**

AlphaXiv introdujo GLM-5.2 para comprender artículos de investigación, donde los usuarios resaltan una sección, hacen preguntas y hacen referencia a otros artículos para contexto, comparaciones y referencias comparativas.

Type: Integration | Date: 2026-06-16

---

<a id="case-29"></a>
### Case 29: [Comparación de poemas restringida](https://x.com/emollick/status/2067056226337186146) (by [@emollick](https://x.com/emollick))

**Utilice este caso para separar la corrección de la calidad creativa al comparar el GLM-5.2 con los modelos estilo Fable.**

Ethan Mollick le dio crédito a GLM-5.2 Max por producir un poema restringido correcto, al tiempo que señaló que Fable incorporó la restricción de letras que desaparecen en el tema del poema de manera más creativa.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-30"></a>
### Case 30: [Ejemplo de sentido del diseño](https://x.com/0xSero/status/2067074877941796994) (by [@0xSero](https://x.com/0xSero))

**Utilice este caso como una señal de diseño visual liviano y luego verifíquelo con su propio mensaje y revisión de la interfaz de usuario.**

El autor dice que disfrutaron el sentido del diseño del GLM-5.2 y compartieron un ejemplo visual. Es útil como indicador para inspeccionar, no como prueba independiente de la calidad del diseño de producción.

Type: Demo | Date: 2026-06-17

---

<a id="case-71"></a>
### Case 71: [Juego voxel estilo Temple Run en un solo intento](https://x.com/pseudokid/status/2068431546143649829) (by [@pseudokid](https://x.com/pseudokid))

**Usa este caso para poner a prueba GLM-5.2 en generación de juegos con un solo prompt y luego revisar qué sigue necesitando correcciones iterativas en una build visualmente rica.**

El autor cuenta que obtuvo la mayor parte de un juego de motos voxel inspirado en Temple Run en el primer turno y luego usó unas pocas iteraciones de seguimiento para corregir cámara y movimiento. La publicación también señala que las herramientas de Z.ai pueden generar capturas y videos de gameplay para ayudar al modelo de texto a evaluar el resultado.

Type: Demo | Date: 2026-06-20

---

<a id="case-78"></a>
### Case 78: [Conjunto de ejemplos one-shot en OpenCode Go](https://x.com/LyalinDotCom/status/2068378281636982990) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**Usa este caso para medir GLM-5.2 en builds rápidas de un solo intento dentro de OpenCode Go antes de comprometerlo a loops de agentes más abiertos.**

El autor reporta ejemplos one-shot que incluyen una app web del sistema solar, una app Electron de información del sistema y un sencillo juego web de exploración de islas mediante OpenCode Go. La misma publicación también afirma que GLM-5.2 es el mejor modelo abierto que ha usado, aunque sin llegar a llamarlo igual a la frontera.

Type: Demo | Date: 2026-06-20

---



<a id="case-81"></a>
### Case 81: [Build de Space Invaders con un solo prompt](https://x.com/DeryaTR_/status/2068803754611069128) (by [@DeryaTR_](https://x.com/DeryaTR_))

**Usa este caso para probar GLM-5.2 en la creación de juegos con un solo prompt y ver luego cómo unos pocos pases extra manejan cambios de assets y pulido simple.**

La autora dice que GLM-5.2 construyó un juego jugable estilo Space Invaders a partir de un prompt principal y luego usó tres prompts de seguimiento para reemplazar sprites y añadir pequeños extras como un leaderboard. El resultado publicado es un ejemplo público ligero de calidad de creación de juegos, no un benchmark completo.

Type: Demo | Date: 2026-06-21

---

<a id="case-82"></a>
### Case 82: [Laboratorio de recuperación de OpenCode en un solo intento](https://x.com/threepointone/status/2068718370581536816) (by [@threepointone](https://x.com/threepointone))

**Usa este caso para prototipar rápidamente simulaciones interactivas de fallos de agentes, porque el autor informa que obtuvo un recovery lab funcional en un solo intento por unos 3,50 $.**

El autor construyó un recovery lab totalmente interactivo con OpenCode y GLM-5.2 después de darle al modelo un análisis de 4.000 palabras y el repositorio del Agents SDK. La publicación reporta una ejecución de 176k tokens, un resultado one-shot y un coste de extremo a extremo de alrededor de 3,50 $ antes del pulido.

Type: Demo | Date: 2026-06-21

---
<a id="case-92"></a>
### Case 92: [Abrir reconstrucción de URL de referencia de diseño](https://x.com/OpenDesignHQ/status/2069046584134778995) (by [@OpenDesignHQ](https://x.com/OpenDesignHQ))

**Usa este caso para probar GLM-5.2 en recreación web guiada por referencias, donde un solo prompt más una URL de origen reprodujeron un sitio con fidelidad casi a nivel de píxel.**

Open Design dice que probó GLM-5.2 en su AMR integrado usando solo una URL de referencia y un prompt sencillo, y el modelo recreó el sitio web casi a la perfección en la demo. Tómalo como una prueba práctica de generación de UI basada en referencias, no como un benchmark completo.

Type: Demo | Date: 2026-06-22

---

<a id="case-99"></a>
### Case 99: [Prueba de calidad de costo de Trader Desk](https://x.com/atomic_chat_hq/status/2069171121044513273) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Usa este caso para comparar GLM-5.2 en builds full-stack de UI, donde se acercó al resultado de trading desk más pulido mientras costaba solo una pequeña fracción del mejor resultado.**

Atomic Chat comparó cuatro modelos con el mismo prompt real de Trader Desk, con frontend, backend, datos de mercado de ocho símbolos y una UI personalizada de tema oscuro. La publicación informa que GLM-5.2 usó 13,677 tokens y costó $0.03, frente a Fugu Ultra con 22,225 tokens y $0.51, y dice que GLM produjo una interfaz multipanel igualmente completa con datos en vivo a un coste mucho menor.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-100"></a>
### Case 100: [Juego ludita tras la negativa de Claude](https://x.com/atmoio/status/2069559053114577088) (by [@atmoio](https://x.com/atmoio))

**Usa este caso para prototipar conceptos de juego sensibles a políticas con GLM-5.2 cuando un modelo cerrado rechaza la solicitud, y luego inspeccionar por ti mismo el resultado jugable.**

atmoio dice que Claude marcó como violación de uso aceptable un juego humorístico estilo Plague Inc. sobre destruir IA, así que el autor construyó en su lugar con GLM 5.2 el juego llamado Luddite y adjuntó un clip de demo. Tómalo como un ejemplo práctico de fallback para tareas de creative coding que los modelos cerrados pueden rechazar por motivos de política.

Type: Demo | Date: 2026-06-23

---

<a id="provider-tool-integrations"></a>
## 🔌 Integraciones de proveedores y herramientas
<a id="case-170"></a>
### Case 170: [Acceso gratuito a la API Plug-and-Play de NVIDIA](https://x.com/hqmank/status/2072855265612030010) (by [@hqmank](https://x.com/hqmank))

**Usa este caso para probar GLM-5.2 rápido mediante un endpoint alojado sin costo, porque hqmank dice que NVIDIA abrió una ruta API compatible con OpenAI y confirmó que funcionó como un reemplazo plug-and-play.**

hqmank dice que GLM-5.2 llegó a la API gratuita de NVIDIA y que el endpoint funcionó en una prueba rápida. La publicación lo describe como compatible con OpenAI y plug-and-play, aunque también advierte que las capas gratuitas suelen endurecerse cuando sube la demanda. Eso lo convierte en una nota práctica de acceso para evaluaciones rápidas o rutas temporales de agentes.

Type: Integration | Date: 2026-07-03

---

<a id="case-169"></a>
### Case 169: [Ruta del agente de codificación de IA para trabajadores gratuitos](https://x.com/ClaudeCode_UT/status/2072881775408456066) (by [@ClaudeCode_UT](https://x.com/ClaudeCode_UT))

**Usa este caso para montar una ruta de GLM-5.2 sin coste para coding agents, porque el tutorial conecta Workers AI con Claude Code, OpenCode, Cursor y Aider mediante el endpoint compatible con OpenAI `cf/zai-org/glm-5.2`.**

ClaudeCode_UT describe una ruta de seis pasos: crear una cuenta gratuita de Cloudflare, copiar el account ID de Workers AI, emitir un API token, añadir Cloudflare como proveedor en herramientas compatibles con OpenAI, elegir `cf/zai-org/glm-5.2` y empezar a usar Claude Code, Cursor, Aider u OpenCode. Es un tutorial práctico de acceso para equipos que quieren probar workflows de coding agents antes de pagar facturación por token.

Type: Tutorial | Date: 2026-07-03

---
<a id="case-225"></a>
### Case 225: [Puente de TogetherLink con el harness de Codex](https://x.com/nutlope/status/2077432463685554558) (by [@nutlope](https://x.com/nutlope))

**Usa este caso para ejecutar GLM-5.2 dentro de CLIs de coding agents ya existentes, porque nutlope dice que TogetherLink es un CLI open source que permite a Codex y Claude Code llamar directamente a modelos abiertos como GLM 5.2.**

El anuncio presenta TogetherLink como una capa puente para desarrolladores que quieren conservar su harness de coding preferido mientras cambian el modelo subyacente a una stack open-weight. Como la publicación nombra explícitamente a Codex y Claude Code como harnesses compatibles y posiciona el proyecto como open source, sirve como una ruta concreta de acceso para equipos que quieren probar GLM-5.2 sin abandonar su flujo actual en terminal.

Type: Integration | Date: 2026-07-15

---
<a id="case-224"></a>
### Case 224: [Enrutamiento del Open Model Harness de Vorflux](https://x.com/vorfluxai/status/2077449967711760587) (by [@vorfluxai](https://x.com/vorfluxai))

**Usa este caso para llevar GLM-5.2 a una sesión completa de agent sin glue personalizado, porque vorfluxai dice que su Open Model Harness asigna GLM 5.2 a los pasos de design, build y simplify mientras mantiene intacto el resto del flujo de Vorflux.**

vorfluxai dice que el harness expone un menú desplegable que cambia toda una sesión a modelos abiertos mientras conserva el flujo normal de Vorflux para planning, subagents, pull requests y testing. En la tabla de routing publicada, DeepSeek V4 Pro se encarga de main, plan y review, DeepSeek V4 Flash de explore, GLM 5.2 de design, build y simplify, y Kimi 2.7 Code de debug y testing, lo que convierte este caso en un patrón concreto de orquestación agentic multimodelo y no en una simple publicación de disponibilidad.

Type: Integration | Date: 2026-07-15

---
<a id="case-220"></a>
### Case 220: [Agente clínico OpenMed con de-id](https://x.com/MaziyarPanahi/status/2077000157103898789) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Usa este caso para mantener GLM-5.2 dentro de un flujo clínico con privacidad preservada, porque MaziyarPanahi dice que GLM 5.2 planificó, llamó herramientas y escribió la disposición de un caso completo después de que OpenMed eliminó identificadores en local y Gemma 4 manejó la estructura.**

MaziyarPanahi describe un workflow totalmente abierto donde OpenMed realiza la desidentificación en el dispositivo, Gemma 4 extrae la estructura y GLM-5.2 asume el razonamiento médico agentic sobre texto redactado. El detalle operativo clave es que la nota cruda nunca sale de la máquina, lo que convierte el hilo en un patrón concreto de privacidad y tooling sanitario, y no en una recomendación genérica de modelo.

Tipo: Integración | Fecha: 2026-07-14

---
<a id="case-219"></a>
### Case 219: [Ruta de acceso GLM con USDC en Katana](https://x.com/imgn_ai/status/2077061568068465148) (by [@imgn_ai](https://x.com/imgn_ai))

**Usa este caso para exponer GLM-5.2 mediante una ruta pay per request nativa de wallet, porque imgn_ai dice que Katana sirve GLM-5.2 sobre x402 en Base sin cuenta, usando USDC y un llms.txt publicado para integración directa.**

imgn_ai presenta Katana como una vía impulsada por x402 en la que los desarrolladores copian el llms.txt del servicio, conectan una wallet y llaman modelos frontier de texto, imagen o video a precios mayoristas. Como el post dice explícitamente que no hace falta cuenta y que el pago ocurre por petición en USDC, esto funciona como una opción de acceso concreta para experimentos que no quieren una cuenta SaaS permanente.

Tipo: Integración | Fecha: 2026-07-14

---
<a id="case-214"></a>
### Case 214: [Ruta GLM mediante Databricks AI Gateway](https://x.com/QCXINT_/status/2076490318695088218) (by [@QCXINT_](https://x.com/QCXINT_))

**Usa este caso si quieres probar una vía gestionada y muy rápida de acceso a GLM-5.2 dentro de agent tooling, porque QCXINT_ mostró un flujo con base URL y token propios de Databricks AI Gateway que expone una ruta de GLM 5.2 aparentemente de 1M de contexto, aunque la identidad exacta del backend sigue sin confirmarse.**

QCXINT_ describe un flujo bastante concreto: crear un workspace de Databricks, abrir User Settings, generar un access token con scope de AI Gateway, copiar la AI Gateway base URL propia de la organización y llamar al endpoint expuesto desde herramientas como OpenClaw o Hermes. Según el post, en las pruebas actuales solo aparecía GLM-5.2, la velocidad era inusualmente alta y la ruta parecía soportar hasta 1M de contexto; aun así, el propio autor avisa de que todavía no confirmó si el backend es exactamente el modelo GLM-5.2 que afirma ser.

Type: Integration | Date: 2026-07-13

---

<a id="case-208"></a>
### Case 208: [Pila de agente de visor molecular abierto](https://x.com/MaziyarPanahi/status/2075913552854933869) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Usa este caso para conectar GLM-5.2 a un flujo abierto de inspección científica, porque MaziyarPanahi combinó GLM-5.2 vía Hugging Face Inference Providers con Qwen3-VL sobre llama.cpp, Mol* y PydanticAI para renderizar y criticar una estructura EGFR más erlotinib con un solo prompt.**

MaziyarPanahi describe una pila completamente abierta donde GLM-5.2 actúa como cerebro de lenguaje mediante Hugging Face Inference Providers, Qwen3-VL se ocupa de la inspección visual sobre llama.cpp, Mol* renderiza la estructura y PydanticAI coordina la capa de agente. El post dice que el flujo produjo seis renders desde un solo prompt sobre un ejemplo de EGFR más erlotinib tomado del RCSB PDB, lo que lo convierte en una integración científica multiherramienta concreta y no en un simple anuncio de disponibilidad.

Type: Integration | Date: 2026-07-11

---
<a id="case-204"></a>
### Case 204: [Línea base de costos de WANDR de Perplexity Advisor](https://x.com/perplexity_ai/status/2075229779716973030) (by [@perplexity_ai](https://x.com/perplexity_ai))

**Usa este caso para estimar la economía de GLM-5.2 dentro de un harness de computer use con routing, porque Perplexity dice que su configuración de GLM 5.2 más advisor marca 2.1x en WANDR frente a 6.1x de Opus, con un coste medio cercano a la mitad en los benchmarks.**

Perplexity dice que midió el coste por tarea usando GLM 5.2 como baseline y que la ruta GLM 5.2 más advisor en WANDR quedó en 2.1x, frente a 6.1x de Opus. Tómalo como una señal concreta para routing de computer agent con open weights primero, donde un núcleo GLM más barato se combina con escalado selectivo en vez de ejecutar un modelo cerrado más fuerte en cada paso.

Type: Evaluation | Date: 2026-07-09

---

<a id="case-203"></a>
### Case 203: [Enrutamiento de artefactos abiertos de compañeros de trabajo](https://x.com/coworkerapp/status/2075233366266310905) (by [@coworkerapp](https://x.com/coworkerapp))

**Usa este caso para llevar GLM-5.2 a workflows empresariales de artifacts, porque Coworker dice que Open Artifacts puede construir docs, decks, PDF, spreadsheets, dashboards y apps mientras su router optimizado reduce el uso de tokens en torno a 5x y sigue ofreciendo GLM 5.2 alojado en EE. UU.**

Coworker dice que Open Artifacts puede generar productos compartibles como docs, decks, dashboards, spreadsheets, PDF y apps completas. El mismo post de lanzamiento dice que su modo optimizado elige el modelo correcto para cada tarea para usar unas cinco veces menos tokens, mientras sigue permitiendo a los equipos ejecutar GLM 5.2 en un entorno alojado en EE. UU., con SOC 2 y muchas conexiones.

Type: Integration | Date: 2026-07-09

---

<a id="case-201"></a>
### Case 201: [Flujo de trabajo de carga de contexto de DotCode](https://x.com/stagedhappen/status/2074775356867789241) (by [@stagedhappen](https://x.com/stagedhappen))

**Usa este caso para dar a GLM-5.2 más contexto de proyecto dentro de una sandbox privada de coding, porque DotCode añadió soporte para GLM 5.2 junto con uploads de screenshots, imágenes, CSV, PDF, source files y zips que alimentan el mismo flujo de filesystem y terminal.**

DotCode dice que GLM 5.2 ahora funciona con uploads contextuales de workspace para que los agentes puedan inspeccionar archivos, navegar la estructura del proyecto, editar código, ejecutar comandos de terminal y continuar dentro de la misma sandbox. El post enumera las entradas soportadas, muestra el flujo de prompt más archivos hacia la ejecución en sandbox y lo presenta como un paso hacia trabajo real de coding agent basado en contexto auténtico de proyecto.

Type: Integration | Date: 2026-07-08

---
<a id="case-226"></a>
### Case 226: [Triaje de historiales en Mac Studio con Bonsai](https://x.com/MaziyarPanahi/status/2077362554805117132) (by [@MaziyarPanahi](https://x.com/MaziyarPanahi))

**Usa este caso para mantener local un historial clínico largo mientras GLM-5.2 razona sobre él, porque MaziyarPanahi dice que GLM 5.2 hizo triage de un historial de paciente de tres años a través de Bonsai 27B en un Mac Studio y detectó un riesgo de contraste enterrado 17 meses atrás.**

MaziyarPanahi dice que 292 encuentros se mantuvieron dentro de Bonsai 27B en un Mac Studio usando llama.cpp, Metal, pesos ternarios y unos 7.2GB de almacenamiento local del modelo, con GLM-5.2 autorizado a hacer solo tres preguntas antes de identificar un riesgo de metformina más contraste yodado con eGFR 39. El hilo presenta la configuración como privada por diseño: el historial nunca salió de la máquina y el orquestador nunca tocó datos crudos del paciente, así que se trata de un workflow sanitario local concreto y no de una promoción genérica del modelo.

Type: Demo | Date: 2026-07-15

---
<a id="case-221"></a>
### Case 221: [Serving agentic B300 con SGLang TopK-V2](https://x.com/lmsysorg/status/2077076059657548127) (by [@lmsysorg](https://x.com/lmsysorg))

**Usa este caso para benchmarkear serving productivo de GLM-5.2 en cargas agent de contexto largo, porque lmsysorg dice que SGLang alcanzó más de 500 tok/s por usuario en 8xB300 con batch size 1 mientras mejoró la interactividad de usuario único entre 18 y 34 por ciento.**

El post técnico dice que las mediciones vienen de una carga real de coding agentic multi-turn y atribuye las mejoras tanto a la arquitectura de GLM-5.2 consciente de IndexShare y KVShare como al nuevo kernel TopK-V2 de SGLang. También afirma que el kernel es 2,33x más rápido a 80K ISL y escala hasta 10,17x a 1M ISL, lo que lo convierte en una referencia de despliegue más sólida que una nota genérica de lanzamiento.

Tipo: Evaluación | Fecha: 2026-07-14

---
<a id="case-215"></a>
### Case 215: [Ruta llm-d H200 con Prefix-Cache](https://x.com/RedHat_AI/status/2076725768034398513) (by [@RedHat_AI](https://x.com/RedHat_AI))

**Usa este caso si quieres benchmarkear la economía de serving gestionado de GLM-5.2 sobre H200, porque RedHat_AI dice que la combinación de Wide EP y prefix-cache routing en llm-d logró más de 90 por ciento de cache reuse, TTFT por debajo de 3 segundos y unos 2 dólares por millón de output tokens en una ruta GLM-5.2 de más de 700B.**

Red Hat AI enlaza una explicación de robertshaw21 en vLLM Office Hours sobre un despliegue de GLM-5.2 de más de 700B funcionando sobre H200. El post atribuye tanto el cache reuse superior al 90 por ciento como el TTFT inferior a 3 segundos al routing de llm-d con Wide EP y conciencia de prefix cache, y además compara unos 2 dólares por millón de output tokens frente a 4.40 dólares en la API alojada. Es una referencia útil para comparar un stack de routing propio con el uso directo del modelo hosted.

Type: Integration | Date: 2026-07-13

---

<a id="case-209"></a>
### Case 209: [Colibri 25 GB de RAM Transmisión escasa](https://x.com/techNmak/status/2075872446197158361) (by [@techNmak](https://x.com/techNmak))

**Usa este caso para entender el nuevo suelo práctico del despliegue local de GLM-5.2, porque techNmak explica cómo Colibrì ejecuta el MoE 744B con unos 25 GB de RAM mediante streaming de expertos desde NVMe, aunque la configuración más pequeña solo logra alrededor de 0,05 a 0,1 tok/s.**

techNmak resume Colibrì como un motor local de inferencia en C puro que mantiene en RAM solo los pesos siempre calientes y deja los expertos enrutados en NVMe, con unos 9,9 GB residentes de forma permanente, alrededor de 20 GB de pico de RAM durante el chat y unos 370 GB de pesos int4 en disco. El post presenta explícitamente el resultado como una prueba de concepto de sistemas y no como serving rápido en producción, porque la generación en frío sobre la máquina de 25 GB se queda en torno a 0,05 a 0,1 tok/s y el impacto de calidad de la cuantización int4 todavía no está completamente benchmarkeado.

Type: Demo | Date: 2026-07-11

---
<a id="case-206"></a>
### Case 206: [Rendimiento de producción de SGLang NVFP4](https://x.com/sgl_project/status/2075721488456654861) (by [@sgl_project](https://x.com/sgl_project))

**Usa este caso para dimensionar serving productivo de SGLang para GLM-5.2 NVFP4, porque la release oficial de SGLang v0.5.15 dice que ahora alcanza más de 500 tok/s por usuario en 8x B300 y 450 en 4x GB300 con batch size 1.**

El anuncio oficial de SGLang v0.5.15 dice que este ciclo se centró en ajustar GLM-5.2 NVFP4 para serving productivo. El post informa de más de 500 tokens por segundo por usuario en 8x B300 y 450 en 4x GB300 con bs=1, lo que lo convierte en un punto de referencia concreto de throughput de despliegue para equipos que evalúan stacks de inferencia alojados o autogestionados. El mismo anuncio también presenta el trabajo como soporte upstream del producto, no como un hack puntual de laboratorio.

Type: Evaluation | Date: 2026-07-10

---
<a id="case-198"></a>
### Case 198: [Terminal GLM gratuito Dahl 100M](https://x.com/pengsonal/status/2074908680106180669) (by [@pengsonal](https://x.com/pengsonal))

**Usa este caso para probar GLM-5.2 por una ruta OpenAI-compatible sin tarjeta, porque Dahl Inference ofrece 100M de tokens gratis para GLM 5.2 FP8 y explica cómo crear una clave y llamar a `/v1/chat/completions`.**

El post incluye GLM 5.2 FP8 entre los endpoints gratuitos de modelos abiertos de Dahl y dice que no hace falta registro ni tarjeta. También da un flujo concreto de configuración: generar una key en la web UI, usar el endpoint OpenAI-compatible `/v1/chat/completions`, y tener en cuenta que las peticiones directas con `curl` pueden chocar con Cloudflare 403 aunque la ruta de web chat sí funcione.

Type: Tutorial | Date: 2026-07-08

---
<a id="case-195"></a>
### Case 195: [Configuración de GLM para terminales gratuitos de NVIDIA](https://x.com/undefinedKi/status/2074491917333655948) (by [@undefinedKi](https://x.com/undefinedKi))

**Usa este caso para probar GLM-5.2 en herramientas de código sin self-hosting, porque la fuente describe un flujo de endpoint gratuito de NVIDIA que mete claves API de GLM-5.2 en Claude Code, Cursor o Cline.**

El post dice que NVIDIA lanzó claves API gratuitas para modelos top, incluido GLM-5.2, y luego da una ruta directa de configuración: crear una cuenta de NVIDIA, abrir la pestaña Build de un modelo free endpoint, generar la API key y pegar la base URL junto con la clave en Claude Code, Cursor o Cline. Eso lo convierte en un tutorial práctico de acceso para probar GLM-5.2 sin facturación por token ni una pila local de GPU.

Type: Tutorial | Date: 2026-07-07

---
<a id="case-193"></a>
### Case 193: [Ruta de inferencia privada 0G TeeML](https://x.com/0G_labs/status/2074496704959676682) (by [@0G_labs](https://x.com/0G_labs))

**Usa este caso para enrutar GLM-5.2 por una vía de proveedor centrada en privacidad, porque 0G dice que GLM 5.2 ya corre en TeeML con prompts sellados dentro de un enclave TEE y con precio por debajo de la ruta oficial.**

0G presenta TeeML como su capa de inferencia privada y dice que GLM 5.2 ya corre allí con ejecución verificable dentro de un trusted execution environment. El post es breve, pero aun así aporta una integración concreta de proveedor junto con un ángulo de privacidad y precio, así que encaja mejor como señal de ruta de despliegue que como afirmación sobre calidad del modelo.

Type: Integration | Date: 2026-07-07

---
<a id="case-185"></a>
### Case 185: [PR Open-SQL de DuckDB Flock](https://x.com/lhoestq/status/2074143736624275629) (by [@lhoestq](https://x.com/lhoestq))

**Usa este caso para llevar GLM-5.2 a un análisis SQL local totalmente abierto, porque lhoestq dice que un PR de duckdb más flock ya habilita GLM-5.2 dentro de un stack de datos 100% open source.**

El post dice que el autor abrió un PR para habilitar GLM-5.2 en duckdb con flock y lo presenta como una forma de poner inteligencia frontier abierta directamente al servicio de tus datos. Como la fuente es una señal de PR abierto y no una nota de lanzamiento ya fusionada, encaja mejor como caso de integración en progreso para analítica local y workflows nativos de SQL.

Type: Integration | Date: 2026-07-06

---
<a id="case-179"></a>
### Case 179: [Acceso API de 26 modelos con una sola clave](https://x.com/Alan_Earn/status/2073663239028924680) (by [@Alan_Earn](https://x.com/Alan_Earn))

**Usa este caso para probar GLM-5.2 a través de un único proveedor compatible con OpenAI, porque Alan_Earn dice que una sola API key expone GLM-5.2 más otros 25 modelos e incluye 26 dólares de crédito inicial.**

El post da un flujo corto de setup: crear la cuenta, añadir una tarjeta, desbloquear el panel, reclamar los créditos, generar la API key y pegarla en Codex, Cursor, OpenCode, OpenClaw, Hermes u otros clientes compatibles con OpenAI. También menciona billing pay as you go y que los modelos frontier más grandes consumen rápido el crédito gratuito, así que funciona sobre todo como nota de acceso y pricing.

Type: Tutorial | Date: 2026-07-05

---
<a id="case-176"></a>
### Case 176: [Configuración de pensamiento NVIDIA NIM OpenCode](https://x.com/Dracoshowumore/status/2073384581256929717) (by [@Dracoshowumore](https://x.com/Dracoshowumore))

**Usa este caso para conectar GLM-5.2 a OpenCode a través del endpoint gratuito de NVIDIA NIM cuando quieras una ruta sin coste con thinking activado de forma explícita, porque Dracoshowumore comparte el flujo de API key, la base URL y una configuración de OpenCode donde la capa de herramientas gestiona las function calls mientras GLM corre con enable_thinking en true.**

Dracoshowumore detalla una ruta completa: registrarse en la plataforma de desarrolladores de NVIDIA, generar una API key de GLM-5.2, apuntar OpenCode a la base URL publicada, desactivar el tool calling nativo del modelo y pasar chat_template_kwargs.enable_thinking=true en las opciones del proveedor. El mismo post dice que la ruta NIM no expone function calling ni reasoning traces de forma nativa, así que OpenCode debe encargarse de la orquestación de herramientas. Eso lo vuelve una nota práctica de configuración y no otro simple anuncio de endpoint gratis.

Type: Tutorial | Date: 2026-07-04

<a id="case-165"></a>
### Case 165: [Lanzamiento de ZCode con control de agente móvil](https://x.com/Digiato/status/2072663459850829985) (by [@Digiato](https://x.com/Digiato))

**Usa este caso para evaluar ZCode como superficie oficial de coding para GLM-5.2, porque el reporte de lanzamiento dice que el IDE agentic gratuito llega a Windows, macOS y Linux y puede seguir proyectos mediante Telegram, WeChat y Feishu.**

Digiato describe ZCode como un entorno de desarrollo agentic gratuito construido alrededor de GLM-5.2 y posicionado frente a Cursor, Claude Code y Copilot. El post dice que llega a Windows, macOS y Linux, se integra de forma profunda con GLM-5.2 y permite revisar el progreso del proyecto por Telegram, WeChat y Feishu. Eso lo convierte en una superficie de acceso más distintiva que un simple anuncio de modelo.

Type: Integration | Date: 2026-07-02

---

<a id="case-160"></a>
### Case 160: [Documentos del agente de mantenimiento automático de OpenWiki](https://x.com/LangChain/status/2072745455788933321) (by [@LangChain](https://x.com/LangChain))

**Usa este caso para mantener al día documentación legible por agentes automáticamente, porque LangChain dice que OpenWiki regenera y mantiene los docs del repo a medida que cambia el código y funciona sobre modelos abiertos como GLM 5.2.**

LangChain presenta OpenWiki como una capa open-source de mantenimiento de documentación para coding agents. El post dice que combina un harness abierto con flujos CLI abiertos, mantiene la documentación actualizada cuando cambia el codebase y funciona sobre modelos abiertos como GLM 5.2 y Kimi K2.7. Es un patrón práctico de memoria en archivos para equipos que quieren que los agentes lean docs frescos en vez de depender de wikis mantenidas a mano.

Type: Integration | Date: 2026-07-02

---

<a id="case-152"></a>
### Case 152: [PTU de fundición a través de FireConnect](https://x.com/FireworksAI_HQ/status/2072407689964183867) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Use este caso para enrutar GLM-5.2 mediante presupuestos empresariales de Foundry sin reescribir clientes de agentes, porque Fireworks dice que FireConnect conecta las PTU de Microsoft Foundry con flujos en Codex, OpenCode y Pi.**

Fireworks afirma que GLM 5.2 ya está disponible en Microsoft Foundry. Con FireConnect activado, los equipos pueden gastar PTU de Foundry mientras siguen enviando solicitudes desde Codex, OpenCode o Pi, en lugar de montar una ruta separada para cada superficie de agente.

Type: Integration | Date: 2026-07-01

---


<a id="case-147"></a>
### Case 147: [Banco de trabajo de evaluación Braintrust GLM](https://x.com/ankrgyl/status/2072042305108722040) (by [@ankrgyl](https://x.com/ankrgyl))

**Usa este caso para comparar GLM-5.2 y Opus dentro de una misma pila de evals, porque Braintrust y Baseten lo lanzaron con un ejemplo concreto de coste frente a precisión en contexto largo.**

ankrgyl dice que Braintrust añadió GLM-5.2 con soporte de Baseten para usarlo en evals y trazas de producción. El ejemplo compara recuperación en contexto largo a 25K y 50K tokens: Opus 4.8 gana por unos 3,5 puntos, pero cuesta entre 4,1x y 4,5x más por trace.

Type: Integration | Date: 2026-06-30

---

---

<a id="case-141"></a>
### Case 141: [Suscripción plana ClinePass para modelos open-weight](https://x.com/iam_elias1/status/2071655509611151674) (by [@iam_elias1](https://x.com/iam_elias1))

**Usa este caso para reunir varios modelos de coding open-weight en un solo agent harness, porque ClinePass empaqueta GLM-5.2 y modelos relacionados bajo una tarifa mensual fija en lugar de claves y paneles de cobro separados por proveedor.**

iam_elias1 describe ClinePass como una vía de 9.99 dólares al mes para usar GLM-5.2, DeepSeek, Kimi, Qwen, MiniMax, MiMo y otros modelos open-weight dentro de la extensión IDE y la CLI de Cline. El hilo dice que sustituye las API keys por proveedor, ofrece 2-5 veces los límites estándar de API, permite cambiar de modelo en mitad de la sesión según la fase de trabajo y baja el primer mes a 1.99 dólares si el alta se hace desde la CLI.

Type: Integration | Date: 2026-06-29

<a id="case-137"></a>
### Case 137: [Servicio gratuito de API GLM para agentes de código](https://x.com/mcwangcn/status/2071261128575897901) (by [@mcwangcn](https://x.com/mcwangcn))

**Usa este caso para probar GLM-5.2 en Hermes u otros agentes de código sin registro, porque el servicio compartido emite API keys de corta duración y mantiene la configuración ligera.**

mcwangcn compartió un servicio gratuito de API de GLM-5.2 que, según indica, no requiere registro ni inicio de sesión y puede usarse desde Lobster, Hermes u otros agentes de código. La misma publicación dice que cada API key generada dura una hora antes de renovarse, lo que constituye una restricción concreta contra abusos y hace que el servicio encaje mejor en pruebas rápidas de workflow que en uso productivo desatendido a largo plazo.

Type: Integration | Date: 2026-06-28

---

<a id="case-31"></a>
### Case 31: [Disponibilidad de OpenCode Go](https://x.com/opencode/status/2067207923122479242) (by [@opencode](https://x.com/opencode))

**Utilice este caso para realizar un seguimiento de la disponibilidad de GLM-5.2 dentro de los flujos de trabajo de OpenCode Go con texto, contexto de 1 millón y precios similares a GLM-5.1.**

OpenCode anunció la disponibilidad de GLM-5.2 en Go, destacando la compatibilidad con texto, una ventana de contexto de 1 millón y el mismo precio que 5.1.

Type: Integration | Date: 2026-06-17

---

<a id="case-32"></a>
### Case 32: [Disponibilidad de la nube de Ollama](https://x.com/ollama/status/2066949797316350361) (by [@ollama](https://x.com/ollama))

**Utilice este caso para enrutar GLM-5.2 a Ollama Cloud para realizar experimentos de modelos de codificación de código abierto accesibles.**

Ollama anunció la disponibilidad de GLM-5.2 y lo describió como un modelo de tarea agente y codificación de largo horizonte con contexto 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-33"></a>
### Case 33: [Acceso a llamadas API de OpenRouter One](https://x.com/OpenRouter/status/2066941552208056561) (by [@OpenRouter](https://x.com/OpenRouter))

**Utilice este caso para acceder a GLM-5.2 a través de OpenRouter al comparar enrutamiento de proveedores o pilas multimodelo.**

OpenRouter anunció la disponibilidad de GLM-5.2 como un modelo de largo horizonte de 1 millón de tokens, brindando a los usuarios una ruta neutral para llamarlo.

Type: Integration | Date: 2026-06-16

---

<a id="case-34"></a>
### Case 34: [Soporte de día cero de vLLM](https://x.com/vllm_project/status/2066950636428775693) (by [@vllm_project](https://x.com/vllm_project))

**Utilice este caso para autohospedar o servir GLM-5.2 a través de vLLM con soporte de día cero.**

El proyecto vLLM anunció la compatibilidad con GLM-5.2 en v0.23.0, enmarcándolo como un modelo emblemático para agentes de codificación de largo horizonte con contexto 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-35"></a>
### Case 35: [Disponibilidad de nociones a través de Baseten](https://x.com/NotionHQ/status/2066963258985320550) (by [@NotionHQ](https://x.com/NotionHQ))

**Utilice este caso para identificar GLM-5.2 como un modelo de peso abierto disponible dentro de los flujos de trabajo de Notion.**

Notion anunció la disponibilidad de GLM-5.2 como un modelo de peso abierto creado para tareas a largo plazo y servido a través de Baseten.

Type: Integration | Date: 2026-06-16

---

<a id="case-36"></a>
### Case 36: [Servicio de fuegos artificiales del día cero](https://x.com/FireworksAI_HQ/status/2067007200426680509) (by [@FireworksAI_HQ](https://x.com/FireworksAI_HQ))

**Utilice este caso para evaluar Fireworks como ruta de servicio para cargas de trabajo GLM-5.2 que necesitan una infraestructura alojada.**

Fireworks anunció GLM-5.2 en vivo el día cero, enfatizando el contexto 1M, el posicionamiento de codificación primero y la validación independiente en SWE-Bench, Terminal-Bench, GPQA y AIME.

Type: Integration | Date: 2026-06-16

---

<a id="case-37"></a>
### Case 37: [Enlace al jardín modelo de Google Cloud](https://x.com/CarolGLMs/status/2067127223216419088) (by [@CarolGLMs](https://x.com/CarolGLMs))

**Utilice este caso para encontrar GLM-5.2 en contextos de plataforma de agentes y de implementación orientados a Google Cloud.**

CarolGLMs compartió un enlace de Google Cloud para GLM-5.2, lo que lo convierte en un indicador directo para los equipos que trabajan a través de catálogos de modelos en la nube.

Type: Integration | Date: 2026-06-17

---

<a id="case-38"></a>
### Case 38: [Modo de privacidad de Venecia](https://x.com/AskVenice/status/2066990725439361251) (by [@AskVenice](https://x.com/AskVenice))

**Utilice este caso cuando el modo de privacidad, TEE o cifrado de extremo a extremo sea un factor decisivo al probar GLM-5.2.**

Venice anunció la disponibilidad de GLM-5.2 en modo privado con encuadre TEE/E2EE, destinado a codificación agente privada y tareas de largo horizonte.

Type: Integration | Date: 2026-06-16

---

<a id="case-39"></a>
### Case 39: [Disponibilidad del código de comando](https://x.com/CommandCodeAI/status/2066950478194503990) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Utilice este caso para probar GLM-5.2 en Command Code con un plan inicial de bajo costo y funciones de codificación de contexto largo.**

Command Code anunció la disponibilidad de GLM-5.2, destacando el contexto de 1M, un razonamiento sólido, el estado de código abierto y el acceso a través de su plan Go de un dólar.

Type: Integration | Date: 2026-06-16

---

<a id="case-40"></a>
### Case 40: [Agente Hermes De Nous Portal](https://x.com/Teknium/status/2066954081575592282) (by [@Teknium](https://x.com/Teknium))

**Utilice este caso para conectar GLM-5.2 a los flujos de trabajo del Agente Hermes a través de Nous Portal y OpenRouter.**

Teknium informó la disponibilidad de GLM-5.2 en Hermes Agent de Nous Portal y OpenRouter, útil para experimentos de enrutamiento de marco de agente.

Type: Integration | Date: 2026-06-16

---

<a id="case-41"></a>
### Case 41: [Socio de lanzamiento del día cero de io.net](https://x.com/ionet/status/2067140436095803763) (by [@ionet](https://x.com/ionet))

**Utilice este caso al evaluar el servicio respaldado por computación para un modelo de contexto largo de parámetros 753B.**

io.net se anunció como socio de lanzamiento del día cero para GLM-5.2, enfatizando el contexto 1M, el diseño de agente primero, la codificación de largo horizonte y las necesidades informáticas de un modelo de parámetros 753B.

Type: Integration | Date: 2026-06-17

---

<a id="case-42"></a>
### Case 42: [Servicio de día cero en la nube modular](https://x.com/clattner_llvm/status/2066974950293147950) (by [@clattner_llvm](https://x.com/clattner_llvm))

**Utilice este caso para considerar Modular Cloud para el servicio GLM-5.2 de contexto prolongado a escala de proveedor.**

Chris Lattner publicó que GLM-5.2 estuvo activo en Modular Cloud el día cero, destacando los pesos abiertos, la codificación, los agentes de largo plazo y el contexto de 1M.

Type: Integration | Date: 2026-06-16

---

<a id="case-61"></a>
### Case 61: [Configuración del cursor a través de OpenRouter](https://x.com/agentnative_/status/2068148384846746107) (by [@agentnative_](https://x.com/agentnative_))

**Utilice este caso para configurar GLM-5.2 en Cursor a través de OpenRouter para un flujo de trabajo de codificación de modelo abierto de bajo costo.**

La fuente proporciona una ruta de configuración concreta del Cursor/OpenRouter en lugar de solo anunciar la disponibilidad del modelo.

Type: Tutorial | Date: 2026-06-20

---

<a id="case-63"></a>
### Case 63: [Amp Agentic ojos para el diseño visual](https://x.com/beyang/status/2068087124818317374) (by [@beyang](https://x.com/beyang))

**Utilice este caso para emparejar GLM-5.2 con agentes personalizados de Amp cuando un modelo de solo texto necesite soporte de revisión visual para tareas de diseño.**

La publicación conecta un resultado comparativo de diseño visual GLM-5.2 con agentes de complemento Amp que pueden proporcionar una capa de revisión.

Type: Integration | Date: 2026-06-20

---

<a id="case-69"></a>
### Case 69: [Baseten sirve un millón de contextos más rápido](https://x.com/alphatozeta8148/status/2067852860499562821) (by [@alphatozeta8148](https://x.com/alphatozeta8148))

**Utilice este caso para enrutar GLM-5.2 a través de Baseten cuando la velocidad de servicio de contexto largo sea importante para Factory Droid, OpenCode y arneses de codificación.**

La fuente informa que GLM-5.2 se ejecuta cuatro veces más rápido en un contexto completo de 1M y lo muestra en arneses de codificación.

Type: Integration | Date: 2026-06-20

<a id="case-74"></a>
### Case 74: [Subagentes QA de Browser Use para diseño web](https://x.com/browser_use/status/2068405699340853541) (by [@browser_use](https://x.com/browser_use))

**Usa este caso para combinar GLM-5.2 con subagentes multimodales de QA de Browser Use v2 cuando un modelo solo de texto necesita inspección visual y correcciones iterativas de sitios web.**

Browser Use informa que GLM-5.2 superó a Fable 5 en una tarea de diseño web y luego añadió subagentes de QA que inspeccionan el resultado, juzgan la estética, encuentran fallos y devuelven correcciones dirigidas a GLM. Según la publicación, el bucle completo de construcción más QA costó menos de 0,75 USD.

Type: Integration | Date: 2026-06-20

---

<a id="case-79"></a>
### Case 79: [Tokens gratis diarios en el IDE oficial ZCode](https://x.com/Alan_Earn/status/2068223665268006924) (by [@Alan_Earn](https://x.com/Alan_Earn))

**Usa este caso para acceder a GLM-5.2 a través de ZCode cuando quieras un IDE oficial de programación gratuito con grandes asignaciones diarias de tokens y un flujo parecido a Cursor.**

La publicación describe ZCode como el IDE oficial de programación de Zhipu, con GLM-5.2 como modelo por defecto, 3M de tokens diarios, 1M de contexto y clientes para Mac y Windows. También incluye un flujo corto de configuración, lo que la hace más accionable que un anuncio genérico de lanzamiento.

Type: Tutorial | Date: 2026-06-20

---



<a id="case-83"></a>
### Case 83: [Configuración de Cursor mediante Fireworks](https://x.com/skirano/status/2068777440986513647) (by [@skirano](https://x.com/skirano))

**Usa este caso para conectar GLM-5.2 a Cursor mediante Fireworks con una configuración mínima compatible con OpenAI y sin código cliente personalizado.**

Skirano muestra un flujo mínimo de configuración en Cursor: pegar una clave de Fireworks en el campo de API key de OpenAI, usar `https://api.fireworks.ai/inference/v1` como base URL, seleccionar `accounts/fireworks/models/glm-5p2` y reiniciar Cursor. Esto lo convierte en una ruta concreta para probar GLM-5.2 dentro de un IDE de programación familiar.

Type: Tutorial | Date: 2026-06-21

---

<a id="case-84"></a>
### Case 84: [Soporte del proveedor ZAI en VulcanBench](https://x.com/vulcanbench/status/2068724843856707676) (by [@vulcanbench](https://x.com/vulcanbench))

**Usa este caso para ejecutar GLM-5.2 en un harness abierto de benchmark con soporte de primer nivel para el proveedor ZAI y una ruta dedicada de API key.**

VulcanBench v0.2.0 añadió soporte de primer nivel para ZAI, lo que permite ejecutar GLM-5.2 como `zai:glm-5.2` junto a modelos de OpenAI y Anthropic con una `ZAI_API_KEY` dedicada. Esto resulta útil para quienes quieren un harness abierto de benchmark en lugar de capturas aisladas.

Type: Integration | Date: 2026-06-21

---

<a id="case-85"></a>
### Case 85: [Variantes de razonamiento High/Max en OpenCode](https://x.com/OpenCodeLog/status/2068487086576156705) (by [@OpenCodeLog](https://x.com/OpenCodeLog))

**Usa este caso para acceder a las variantes de razonamiento High y Max de GLM-5.2 dentro de OpenCode, al tiempo que obtienes un manejo más fiable del límite de pasos.**

OpenCode v1.17.9 añadió variantes de pensamiento High y Max para GLM-5.2 en proveedores compatibles con OpenAI y Anthropic, además del mapeo nativo de esfuerzo para OpenRouter. La misma versión también corrigió el comportamiento del límite de pasos del agente, lo que hace la integración más práctica para ejecuciones más largas.

Type: Integration | Date: 2026-06-21

---

<a id="case-86"></a>
### Case 86: [Selección del endpoint de código de Z.ai](https://x.com/ivanfioravanti/status/2068574700721082400) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para enrutar el tráfico de coding plan de GLM-5.2 al endpoint de Z.ai optimizado para código en lugar de la ruta genérica de API.**

La publicación indica a los usuarios que usen `https://api.z.ai/api/coding/paas/v4` en lugar del endpoint general `https://api.z.ai/api/paas/v4/` para cargas de coding plan, y señala que `https://api.z.ai/api/anthropic` es lo que suelen usar herramientas como Claude Code y OpenCode cuando hay soporte. Tómalo como una corrección de configuración concreta cuando GLM-5.2 parezca estar mal enrutado.

Type: Tutorial | Date: 2026-06-21

---

<a id="case-87"></a>
### Case 87: [Configuración gratuita de la API GLM-5.2 en ZenMux](https://x.com/0x_kaize/status/2068676992782811607) (by [@0x_kaize](https://x.com/0x_kaize))

**Usa este caso para obtener una API key y una base URL gratuitas de GLM-5.2, y luego conectarlas a Claude, Cursor, Hermes y herramientas similares.**

El autor comparte un flujo de configuración de cinco minutos para conseguir una API key y una base URL gratuitas de ZenMux, y luego conectar GLM-5.2 a Claude, Cursor, Hermes y herramientas similares. La publicación también señala que el rate limit de la capa gratuita llega rápido, por lo que resulta más útil como nota de acceso que como garantía de durabilidad.

Type: Tutorial | Date: 2026-06-21

---
<a id="case-93"></a>
### Case 93: [Noumena ncode GLM predeterminado](https://x.com/_xjdr/status/2069030608727408993) (by [@_xjdr](https://x.com/_xjdr))

**Usa este caso para enrutar GLM-5.2 a entornos de agentes tipo ncode y Noumena con endpoints separados estándar y de contexto 1M, además de soporte como modelo por defecto.**

La actualización de Noumena dice que el equipo añadió soporte de primera clase para GLM en tool calling, análisis de funciones, routing de apps y trazas de razonamiento, y luego dividió la API en endpoints `glm-5.2` y `glm-5.2[1m]` para controlar el TTFT bajo tráfico pesado de contexto 1M. También dice que las nuevas builds de ncode cambiaron su modelo opus-class predeterminado de Kimi a GLM tras comentarios positivos de uso.

Type: Integration | Date: 2026-06-22

---

<a id="case-101"></a>
### Case 101: [Inicio rápido del arnés Baseten + Droid](https://x.com/RayFernando1337/status/2069523126384525639) (by [@RayFernando1337](https://x.com/RayFernando1337))

**Usa este caso para poner GLM-5.2 en marcha rápidamente mediante Baseten y el harness Droid, con un flujo corto de configuración que también puedes reutilizar en otros IDEs.**

RayFernando1337 resume un tutorial con pasos marcados por tiempo: obtener una API key de Baseten, automatizar la configuración de Droid AI, probar la integración de GLM-5.2, revisar configuraciones alternativas y limitaciones, y terminar con notas extra de setup para otros IDEs.

Type: Tutorial | Date: 2026-06-23

---

<a id="case-104"></a>
### Case 104: [Flujo de trabajo de API GLM compatible con OpenAI](https://x.com/Marktechpost/status/2069308807570915500) (by [@Marktechpost](https://x.com/Marktechpost))

**Usa este caso para construir en Python un cliente GLM-5.2 compatible con OpenAI con control de razonamiento, tool calling, recuperación de contexto largo y seguimiento de costes.**

Marktechpost compartió un tutorial junto con un cuaderno de código enlazado para envolver GLM-5.2 en un único cliente compatible con OpenAI. La publicación dice que el flujo cubre control de thinking effort (`off`/`high`/`max`), canales en streaming de razonamiento frente a respuesta, tool calling con un agente de varios pasos, salida JSON estructurada, recuperación de contexto largo y seguimiento del coste por tokens.

Type: Tutorial | Date: 2026-06-23

---

<a id="case-105"></a>
### Case 105: [Zona de pruebas de búsqueda de API del agente de perplejidad](https://x.com/perplexitydevs/status/2069252848647606584) (by [@perplexitydevs](https://x.com/perplexitydevs))

**Usa este caso para conectar GLM-5.2 a la Agent API de Perplexity cuando quieras agentes en sandbox con búsqueda detrás de una sola llamada API.**

Perplexity Devs anunció GLM-5.2 en la Agent API y lo describió como una buena opción para workflows de coding y agentes de largo horizonte. La publicación destaca específicamente Search as Code, una interfaz compatible con OpenAI y precios first-party sin margen adicional.

Type: Integration | Date: 2026-06-23

---

<a id="case-109"></a>
### Case 109: [API GLM de Baseten a 280 TPS](https://x.com/aqaderb/status/2069220126272999501) (by [@aqaderb](https://x.com/aqaderb))

**Usa este caso cuando importe la latencia del proveedor: Baseten afirma un serving de GLM-5.2 muy rápido con time-to-first-token subsegundo y alto throughput de decodificación.**

aqaderb anunció la API de GLM-5.2 de Baseten con 280 tokens por segundo y menos de 0.8 segundos de TTFT. La publicación atribuye el resultado a PD disaggregation, speculative decoding con multi-token prediction heads, routing consciente de KV-cache y otras optimizaciones de serving, con un enlace a una nota técnica.

Type: Integration | Date: 2026-06-23

---

<a id="case-128"></a>
### Case 128: [Configuración de OpenCode de IA para trabajadores de Cloudflare](https://x.com/RoundtableSpace/status/2070820686243959276) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Usa este caso para ejecutar GLM-5.2 a través de Cloudflare Workers AI cuando quieras una ruta gratuita compatible con OpenAI para agentes de código sin aprovisionar tu propio host del modelo.**

RoundtableSpace dice que puedes crear una cuenta gratuita de Cloudflare, copiar tu Account ID, crear un API token, añadir Cloudflare como proveedor en OpenCode y apuntar al modelo `@cf/zai-org/glm-5.2`. La publicación también afirma que la misma ruta funciona en OpenCode, Cursor, Aider, Hermes Agent, Claude Code y otras herramientas compatibles con OpenAI, por lo que es un atajo práctico de acceso alojado para agentes de código.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-129"></a>
### Case 129: [Cliente de navegador de configuración cero Puter.js](https://x.com/FareaNFts/status/2070848321212792945) (by [@FareaNFts](https://x.com/FareaNFts))

**Usa este caso para probar GLM-5.2 en un prototipo solo de navegador antes de tocar API keys, facturación o configuración de backend.**

FareaNFts dice que Puter.js expone la familia GLM del lado del cliente mediante una sola etiqueta de script CDN, con `z-ai/glm-5.2` invocable directamente desde código del navegador y sin configuración de servidor ni facturación del lado del desarrollador. La publicación lo presenta como una vía rápida para prototipar herramientas personales, apps de vibe coding y agentes ligeros, aunque también aclara la contrapartida: Puter usa un modelo de pago por parte del usuario en el navegador y no está pensado para tráfico de producción de alto volumen.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-130"></a>
### Case 130: [Acceso unificado a terminales de SiliconFlow](https://x.com/FareaNFts/status/2070900056736379288) (by [@FareaNFts](https://x.com/FareaNFts))

**Usa este caso para situar GLM-5.2 dentro de una pila multimodelo más amplia, porque la publicación describe un único endpoint compatible con OpenAI de SiliconFlow que cubre modelos chinos y occidentales con crédito de prueba gratis.**

FareaNFts dice que SiliconFlow ofrece acceso unificado por API a GLM-5.2 junto con DeepSeek, Qwen, Llama 4, Hunyuan, Mistral, Yi, Gemma, Phi y más de 200 modelos mediante un solo endpoint compatible con OpenAI. La publicación también afirma que el registro da 1 dólar de crédito gratis sin tarjeta, que algunos modelos siguen siendo gratuitos, que hay límites de gasto y que la clave se puede usar en Cursor, Claude Code, Aider y herramientas similares.

Type: Integration | Date: 2026-06-27

---

<a id="case-124"></a>
### Case 124: [Creador de sitios web HuggingChat para HF Space](https://x.com/victormustar/status/2070190742991994967) (by [@victormustar](https://x.com/victormustar))

**Usa este caso para probar GLM-5.2 en un flujo casi gratuito de sitio personal, desde la investigación en HuggingChat hasta el despliegue estático en Hugging Face Spaces.**

victormustar dice que una cuenta de Hugging Face da suficientes créditos gratuitos para pedirle a GLM-5.2 en HuggingChat que construya un sitio web, con Exa usado para investigar sobre el usuario. El mismo post añade que el sitio resultante puede desplegarse gratis como Hugging Face Space estático, lo que lo convierte en una ruta concreta y de bajo coste para experimentar con sitios personales.

Type: Tutorial | Date: 2026-06-25

---

<a id="case-125"></a>
### Case 125: [Disponibilidad del motor de inferencia DigitalOcean](https://x.com/digitalocean/status/2070177703911719301) (by [@digitalocean](https://x.com/digitalocean))

**Usa este caso para enrutar GLM-5.2 por infraestructura gestionada cuando quieras acceso oficial del proveedor sin autoalojar tú mismo el modelo de 1M de contexto.**

DigitalOcean anunció GLM-5.1 y GLM-5.2 en su Inference Engine, posicionando el modelo para flujos de programación agentic de hasta ocho horas con una ventana de contexto de 1M tokens. El post también presenta esta ruta como una integración directa con tu stack existente mediante precios por uso e infraestructura totalmente gestionada.

Type: Integration | Date: 2026-06-25

---

<a id="case-115"></a>
### Case 115: [Código de comando Nivel rápido 120-250 Tok/S](https://x.com/CommandCodeAI/status/2069891896881857016) (by [@CommandCodeAI](https://x.com/CommandCodeAI))

**Usa este caso para acceder a una variante más rápida de GLM-5.2 en Command Code cuando la velocidad de programación de largo horizonte importe más que solo el precio de entrada mínimo.**

Command Code anunció GLM-5.2 Fast como una variante de alto rendimiento que mantiene el posicionamiento frontier para programación mientras eleva la velocidad a 120-250 tokens por segundo. La publicación también dice que la variante conserva 1M de contexto, uso de herramientas y razonamiento, y que está disponible desde el plan Go de $1 con $10 de créditos de uso en adelante.

Type: Integration | Date: 2026-06-24

---

<a id="case-116"></a>
### Case 116: [API rápida GLM-5.2 de Vercel AI Gateway](https://x.com/wafer_ai/status/2069869501190152528) (by [@wafer_ai](https://x.com/wafer_ai))

**Usa este caso para enrutar GLM-5.2 Fast por Vercel AI Gateway cuando necesites velocidad sin servidor más precios explícitos por token.**

wafer_ai dice que GLM-5.2 Fast ya está disponible en Vercel AI Gateway con 150-250 tokens por segundo, ventana de contexto de 1M tokens y precios listados de $3.00 de entrada, $10.25 de salida y $0.50 de caché por cada 1M tokens. Esto la convierte en una nota concreta de acceso alojado para equipos que priorizan rendimiento y precios previsibles de la pasarela.

Type: Integration | Date: 2026-06-24

---

<a id="case-95"></a>
### Case 95: [Código Claude a través de Baseten](https://x.com/thealexker/status/2069163621469335757) (by [@thealexker](https://x.com/thealexker))

**Usa este caso para ejecutar GLM-5.2 dentro de Claude Code mediante una clave de Baseten, una base URL personalizada y remapeo de modelos en `~/.claude/settings.json`.**

El tutorial explica cómo instalar Claude Code, crear una cuenta en Baseten, obtener una API key y editar `~/.claude/settings.json` para que los tres niveles de modelos Claude apunten a `zai-org/GLM-5.2` mediante variables de entorno Anthropic personalizadas. Es un patrón de configuración concreto tipo drop-in para usar GLM-5.2 en el cliente Claude Code.

Type: Tutorial | Date: 2026-06-22

---

<a id="case-96"></a>
### Case 96: [Valor predeterminado del agente Deepsec Pi](https://x.com/cramforce/status/2069057402524082622) (by [@cramforce](https://x.com/cramforce))

**Usa este caso para probar GLM-5.2 en un harness de seguridad, donde `deepsec` lo convirtió en el modelo por defecto para Pi agent y reportó resultados competitivos en evaluaciones.**

La publicación anuncia soporte de `deepsec` para Pi agent de `@badlogicgames` con GLM-5.2 como modelo predeterminado y da un comando ejecutable: `pnpm deepsec process --agent pi`. También dice que el autor ejecutó las evaluaciones de Deepsec y encontró un resultado competitivo frente a otros modelos frontier, lo que lo convierte en una superficie de integración concreta orientada a seguridad.

Type: Integration | Date: 2026-06-22

---

<a id="cost-pricing-local-deployment"></a>
## 💸 Coste, precios y despliegue local
<a id="case-191"></a>
### Case 191: [Laboratorio local LiteLLM construido por Hermes](https://x.com/ivanfioravanti/status/2074609005272375329) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para arrancar un laboratorio local de inferencia con GLM-5.2 como agente de código, porque la fuente dice que Hermes Agent más GLM-5.2 conectaron LiteLLM, Postgres, Prometheus y Grafana alrededor de una configuración con M3 Ultra.**

El post dice que LiteLLM ya estaba corriendo sobre un M3 Ultra y exponía como ruta inicial de prueba un modelo Qwen respaldado por DGX Spark. Lo más importante para este repo es que, según el autor, Hermes Agent más GLM-5.2 montaron LiteLLM, Postgres, Prometheus y Grafana. Eso lo convierte en un ejemplo concreto de integración de laboratorio local para routing, persistencia y observabilidad, y no solo en un elogio vago.

Type: Integration | Date: 2026-07-07

---
<a id="case-187"></a>
### Case 187: [Sim dual de drones sin conexión M5 Max](https://x.com/XavierLocalAI/status/2073938465121833452) (by [@XavierLocalAI](https://x.com/XavierLocalAI))

**Usa este caso para estimar qué puede hacer un agente GLM-5.2 sobre Apple Silicon funcionando totalmente offline, porque XavierLocalAI reporta una instalación 753B escribiendo un simulador de aterrizaje en droneship a 26 tok/s sobre dos máquinas M5 Max de 128 GB.**

Según el post, la configuración usa una build GLM-5.2 753B, una quant Unsloth dynamic IQ2_M de unas 222 GB en disco, dos máquinas M5 Max unidas por Thunderbolt 5 para unos 256 GB de memoria combinada y llama.cpp RPC. El resultado no es solo throughput: el modelo estaba programando en vivo y totalmente offline un simulador de aterrizaje estilo Falcon 9 sobre droneship, así que encaja como demo concreta de despliegue local y agente privacy-first.

Type: Demo | Date: 2026-07-06

---
<a id="case-186"></a>
### Case 186: [5x Arnés de producción de chispas DGX](https://x.com/thatcofffeeguy/status/2074245620207058981) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**Usa este caso para juzgar si una configuración de cinco nodos DGX Spark basta para trabajo productivo con GLM-5.2, porque thatcofffeeguy reporta unos 13,9 tok/s en un solo stream con 400K de contexto y 19,9 tok/s agregados en tres lanes dentro de un harness en vivo.**

El post dice que fue la mejor configuración tras múltiples experimentos y que entró en producción ese mismo día sin pruning. La carga declarada también es más concreta que una simple prueba de laboratorio: el harness ya se estaba usando para generar contenido en unos 30 minutos y revisar datos diarios de ERP, así que funciona como checkpoint práctico de despliegue y no solo como fanfarronada de hardware.

Type: Demo | Date: 2026-07-06

---
<a id="case-183"></a>
### Case 183: [Punto de control M3 Ultra ds4-eval Q4](https://x.com/ivanfioravanti/status/2073742792044446194) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para benchmarkear una instalación de GLM-5.2 sobre Apple Silicon en una sola máquina con ds4-eval, porque ivanfioravanti reporta una ejecución q4 de unos 16 tok/s, con 76 de 92 pruebas superadas en 8 horas y 53 minutos sobre una M3 Ultra de 512 GB.**

ivanfioravanti dice que la ejecución q4 de ds4-eval usó una máquina M3 Ultra de 512 GB y que planea volver a la rama anterior con batch inference. Así, el repo gana un complemento más fuerte para el caso anterior basado solo en video: este hilo añade número de aciertos y tiempo total, no solo un clip de throughput.

Type: Evaluation | Date: 2026-07-05

---
<a id="case-182"></a>
### Case 182: [Guía de construcción de 4x RTX PRO 6000](https://x.com/QingQ77/status/2073589933567094981) (by [@QingQ77](https://x.com/QingQ77))

**Usa este caso para dimensionar una build local seria de GLM-5.2-594B, porque QingQ77 comparte una guía completa de hardware y operación basada en cuatro RTX PRO 6000, APIs expuestas vía opencode y una VM sandbox para trabajo con agentes.**

La guía describe una ruta de mayor presupuesto con cuatro RTX PRO 6000 y 384 GB de VRAM para GLM-5.2-594B, además de piezas EPYC y DDR4 de segunda mano. También cubre switching PCIe Gen4, ajustes de bifurcation y ASPM en BIOS, iommu=off, límites de 350W en circuitos de 110V, contenedores Docker por modelo expuestos mediante opencode y una VM sandbox para que los agentes no alteren el host.

Type: Tutorial | Date: 2026-07-05

---
<a id="case-181"></a>
### Case 181: [Ejecución de QuantTrio en cuatro DGX Spark](https://x.com/Tech2Wild/status/2073637530960826787) (by [@Tech2Wild](https://x.com/Tech2Wild))

**Usa este caso para estimar lo que puede hacer un clúster DGX Spark de cuatro nodos con GLM-5.2 QuantTrio, porque Tech2Wild reporta 200K de contexto, 30 tok/s en un solo stream y 60,5 tok/s de throughput agregado con seis solicitudes concurrentes.**

Tech2Wild dice que la ejecución final mantuvo intactos los 256 expertos y usó decodificación especulativa MTP con k=4. A diferencia de los hilos anteriores de planificación para Spark, aquí hay un resultado concreto de inferencia local ya completado: 30 tok/s en un stream, 60,5 tok/s agregados con seis peticiones concurrentes y un objetivo de 200K de contexto en el clúster.

Type: Demo | Date: 2026-07-05

---
<a id="case-177"></a>
### Case 177: [Ejecución de vídeo único M3 Ultra de 4 bits](https://x.com/ivanfioravanti/status/2073502277449486460) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para estimar la viabilidad de GLM-5.2 en una sola máquina Apple Silicon, porque ivanfioravanti muestra una ejecución 4-bit en un M3 Ultra de 512GB a unos 16 tok/s y la compara con un vídeo de ds4-eval en q2 cerca de 17 tok/s.**

ivanfioravanti publicó un vídeo de GLM 5.2 4-bit corriendo en una sola máquina M3 Ultra de 512GB a unas 16 tokens por segundo, y añade que el vídeo de ds4-eval usa una build q2 alrededor de 17 tokens por segundo. El autor lo presenta como una prueba local todavía en progreso, pero aun así ofrece un punto de referencia concreto de throughput en una sola caja Apple Silicon para complementar los casos existentes del repo sobre despliegues multi-M3 y oMLX.

Type: Demo | Date: 2026-07-04

<a id="case-173"></a>
### Case 173: [Servicio de nodo AMD MI355X 2626 Tok/s](https://x.com/wafer_ai/status/2073155792182907085) (by [@wafer_ai](https://x.com/wafer_ai))

**Usa este caso para dimensionar inferencia GLM-5.2 de alto rendimiento sobre hardware AMD, porque wafer_ai dice que MI355X alcanzó 2626 tok/s por nodo y 213 tok/s en flujo único con un coste superior a 2 veces menos que Blackwell.**

wafer_ai dice que unos ingenieros sirvieron GLM 5.2 sobre AMD MI355X a 2626 tokens por segundo por nodo y 213 tokens por segundo en modo single-stream. La publicación enmarca eso como cerca del 80 por ciento del throughput de B200 con más de 2 veces menos coste, así que sirve como referencia concreta para equipos que evalúan economía de inferencia open-weight más allá de una pila solo NVIDIA.

Type: Demo | Date: 2026-07-03

---

<a id="case-172"></a>
### Case 172: [Vercel Gateway 287 Tok/s sin servidor](https://x.com/wafer_ai/status/2072861749104288074) (by [@wafer_ai](https://x.com/wafer_ai))

**Usa este caso para estimar la latencia real de GLM-5.2 para usuarios a través de un gateway serverless, porque wafer_ai dice que su ruta GLM 5.2 Fast alcanzó 287 tokens por segundo en Vercel AI Gateway y no solo dentro de un harness de benchmark.**

wafer_ai dice que su ruta GLM 5.2 Fast llegó a 287 tokens por segundo en Vercel AI Gateway y lo presenta como una cifra que los usuarios finales verían de verdad en un despliegue serverless. Eso lo convierte en un puente útil entre benchmarks brutos de inferencia y acceso alojado más cercano a producción, donde importa el overhead del gateway.

Type: Demo | Date: 2026-07-03

---

<a id="case-171"></a>
### Case 171: [Implementación de RTX PRO 6000 con un clic](https://x.com/XciD_/status/2073035324272328733) (by [@XciD_](https://x.com/XciD_))

**Usa este caso para estimar el suelo de un despliegue alojado y aislado de GLM-5.2, porque XciD_ dice que GLM-5.2-NVFP4 ya puede desplegarse con un clic en Inference Endpoints sobre 8x RTX PRO 6000 por 22 dólares la hora.**

XciD_ dice que GLM-5.2-NVFP4, la variante MoE de 753B, está disponible como despliegue de un clic en Inference Endpoints con una instancia dedicada de 8x RTX PRO 6000. La publicación destaca precio predecible de 22 dólares por hora, cero setup y aislamiento completo, así que funciona como referencia concreta para equipos que no quieren autogestionar la pila.

Type: Integration | Date: 2026-07-03

---

<a id="case-166"></a>
### Case 166: [744B completo en 5x ASUS GX10](https://x.com/thatcofffeeguy/status/2072525885077434743) (by [@thatcofffeeguy](https://x.com/thatcofffeeguy))

**Usa este caso para dimensionar un despliegue extremo de GLM-5.2 en home lab, porque el autor dice que el modelo completo de 744B ya corre con full context en 5 cajas ASUS GX10 y ya está conectado a un causal harness para cargas reales.**

thatcofffeeguy dice que el GLM-5.2 completo de 744B ya corre en cinco sistemas ASUS GX10 con full context, con token rates mejores de lo esperado y el stack ya conectado a un causal harness. El post aún no publica cifras exactas de throughput, pero sigue siendo una prueba pública concreta de que este tipo de clúster local puede alojar el modelo completo.

Type: Demo | Date: 2026-07-02

---

<a id="case-164"></a>
### Case 164: [Intercambio de ruta de agente en la pila de China](https://x.com/0xluffy_eth/status/2072548580183900430) (by [@0xluffy_eth](https://x.com/0xluffy_eth))

**Usa este caso para enrutar GLM-5.2 a la capa agent de una pila mixta cuando la presión de costes pesa más que la calidad máxima, porque el autor dice que cambiar Sonnet por GLM-5.2 redujo 5x el coste de entrada de ese slot con una caída de calidad de alrededor del 3 por ciento dentro de una migración de 30 días.**

El hilo describe un cambio de routing de seis partes entre razonamiento, generación de código, llamadas agent, procesamiento por lotes, imagen y vídeo. En la capa agent, el autor sustituyó Sonnet por GLM 5.2 y reporta una caída de rendimiento de alrededor del 3 por ciento con entrada 5x más barata. El resumen de 30 días dice que el coste operativo total de IA cayó 87 por ciento mientras los ingresos siguieron planos.

Type: Evaluation | Date: 2026-07-02

---

<a id="case-156"></a>
### Case 156: [Piso de hardware local 744B](https://x.com/devjuninho/status/2072151237840007399) (by [@devjuninho](https://x.com/devjuninho))

**Use este caso para dimensionar con realismo los planes locales de GLM-5.2, porque la fuente dice que incluso las versiones cuantizadas siguen rondando 239 GB en 2 bits y 466 GB en 4 bits, lo que convierte 256 GB o más de RAM o VRAM en un piso práctico.**

devjuninho rechaza la idea de que open weights signifique automáticamente uso local de consumo. El hilo dice que GLM-5.2 tiene alrededor de 744B parámetros con unos 40B activos, estima unos 239 GB en 2 bits y 466 GB en 4 bits, y sostiene que las ejecuciones locales útiles necesitan memoria de clase servidor, margen en SSD y paciencia, no un PC gamer común.

Type: Limit | Date: 2026-07-01

---


<a id="case-151"></a>
### Case 151: [Puerto local NVFP4 Rust a 140 Tok/s](https://x.com/mov_axbx/status/2071839859723882771) (by [@mov_axbx](https://x.com/mov_axbx))

**Usa este caso para medir lo que una instalación local afinada de GLM-5.2 puede hacer en trabajo real de coding, porque el autor informa de NVFP4 a 140 tok/s y de una migración completa de Python a Rust terminada en minutos.**

mov_axbx informa de una configuración local de GLM-5.2 NVFP4 en OMP que alcanza unos 140 tokens por segundo. En la misma publicación dice que el modelo portó un servicio de localización satelital escrito en Python a Rust en unos 10 minutos y luego montó una demo web pocos minutos después.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-140"></a>
### Case 140: [Puesta en marcha dual-stack guiada por agentes en B300 x2](https://x.com/TheValueist/status/2071261052080148607) (by [@TheValueist](https://x.com/TheValueist))

**Usa este caso para dimensionar un despliegue autoalojado serio de GLM-5.2, porque el hilo muestra a analistas levantando inferencia NVFP4 sobre B300 bare-metal en vLLM y SGLang en menos de un día.**

TheValueist dice que un workflow de agentes analistas desplegó GLM 5.2 NVFP4 en un clúster bare-metal NVIDIA B300 x2 tanto sobre vLLM como sobre SGLang y luego ejecutó una batería completa de benchmarks sobre cada stack en menos de 24 horas. El hilo también dice que el factor limitante fue la capacidad de HBM y no el cómputo bruto, y que la DRAM pasa a importar cuando el KV cache se derrama, lo que convierte esta publicación en una nota operativa concreta para equipos que evalúan economía de inferencia local y cuellos de botella de hardware.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-139"></a>
### Case 139: [Aceleración de prefill en oMLX M3 Ultra](https://x.com/jundotkim/status/2071287585297887510) (by [@jundotkim](https://x.com/jundotkim))

**Usa este caso para volver a comprobar la viabilidad local en Apple silicon tras trabajo reciente de kernels, porque la velocidad de prefill reportada para GLM-5.2 en un M3 Ultra 512GB casi se duplicó sin un colapso obvio de calidad en pruebas rápidas.**

jundotkim dice que oMLX 0.4.5.dev1 añade kernels MLX personalizados que elevan el prefill de GLM-5.2-oQ4 32k de 87.7 tok/s a 174.4 tok/s en una máquina M3 Ultra 512GB, un salto del 98.9%. La misma publicación dice que la ruta sigue siendo experimental, pero las comprobaciones tipo needle-in-a-haystack y las pruebas de coding estilo Claude Code no mostraron regresiones obvias, por lo que se trata de una actualización práctica de inferencia local y no solo de una nota de lanzamiento.

Type: Evaluation | Date: 2026-06-28

---

<a id="case-138"></a>
### Case 138: [Explosión de crédito de registro de 20M tokens](https://x.com/Bitbro4crypto/status/2071150218872283262) (by [@Bitbro4crypto](https://x.com/Bitbro4crypto))

**Usa este caso para evaluar si los créditos de registro bastan para una prueba real de GLM-5.2, porque la publicación afirma que las cuentas nuevas reciben 20M tokens gratis, sin tarjeta y con acceso completo compatible con OpenAI.**

Bitbro4crypto dice que la ruta actual de registro de GLM 5.2 da 20 millones de tokens gratuitos, 120 créditos de imagen y vídeo, modos high y max thinking, una ventana de contexto de 1M y una API compatible con OpenAI que encaja en herramientas como Cursor o Claude Code sin suscripción. Tómalo como una señal concreta de acceso y precios para pruebas a corto plazo, asumiendo a la vez que la cuota promocional puede cambiar.

Type: Integration | Date: 2026-06-28

---

<a id="case-131"></a>
### Case 131: [4x Runbook GLM local DGX Spark](https://x.com/TraffAlex/status/2071020631072616698) (by [@TraffAlex](https://x.com/TraffAlex))

**Usa este caso para medir si un clúster DGX Spark es una ruta local realista para GLM-5.2, porque la guía recopilada conecta coste de hardware, topología de clúster y comandos de vLLM con un objetivo GLM de contexto 1M.**

TraffAlex recopiló material validado por la comunidad y material oficial de NVIDIA en una guía de DGX Spark que sitúa cada unidad en 4.699 dólares, trata un clúster de 2x Spark como el punto dulce para otros modelos y dice que 4x Sparks pueden ejecutar GLM 5.2 NVFP4 a unas 20 tokens por segundo con contexto de 1M tokens. La misma publicación incluye configuración de red CX7, SSH sin contraseña, comprobaciones de NCCL y comandos de ejemplo de vLLM con Docker, de modo que funciona como runbook útil de despliegue local en lugar de una opinión genérica sobre hardware.

Type: Tutorial | Date: 2026-06-27

---

<a id="case-43"></a>
### Case 43: [Comparación de costos de tokens de salida](https://x.com/Hesamation/status/2066999955638673891) (by [@Hesamation](https://x.com/Hesamation))

**Utilice este caso para comparar la economía del token de salida GLM-5.2 con los modelos estilo Opus, Fable y GPT-5.5.**

La publicación compara los precios de los tokens de producción de 1 millón y sostiene que GLM-5.2 puede ser significativamente más barato que los modelos de frontera cerrada. Trate las cifras como una comparación de precios vinculada a la fuente que debe volver a verificarse antes de presupuestar.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-44"></a>
### Case 44: [ROI del hardware local cercano a la frontera](https://x.com/Jeyffre/status/2067132023576354818) (by [@Jeyffre](https://x.com/Jeyffre))

**Utilice este caso para razonar sobre si los modelos autohospedados tipo GLM-5.2 pueden compensar los costos de hardware para los usuarios intensivos de agentes.**

El autor estima que varias máquinas de clase DGX Spark podrían ejecutar un modelo de clase 700B y compara una compra de hardware de aproximadamente $20,000 con un alto gasto mensual de API para cargas de trabajo de agentes y codificación.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-45"></a>
### Case 45: [MLX en dos estudios Mac](https://x.com/pcuenq/status/2066967665726337219) (by [@pcuenq](https://x.com/pcuenq))

**Utilice este caso para explorar ejecuciones locales de GLM-5.2 en hardware de Apple y configuraciones orientadas a MLX.**

La publicación dice que GLM-5.2 acaba de ser lanzado y ya se estaba ejecutando con MLX en dos máquinas Mac Studio M3 Ultra, lo que lo presenta como comparable a los modelos cerrados recientes con pesos abiertos.

Type: Demo | Date: 2026-06-16

---

<a id="case-46"></a>
### Case 46: [Reclamo de implementación local mensual H100](https://x.com/ai_xiaomu/status/2066181367340429446) (by [@ai_xiaomu](https://x.com/ai_xiaomu))

**Utilice este caso como indicador de comparación de costos para verificar los supuestos de implementación local antes de elegir entre suscripción y autohospedaje.**

La publicación china compara los números declarados de SWE-Bench, el uso comercial de código abierto y el costo estimado de implementación local de un solo H100 con una suscripción a Claude Pro. Las cifras deberían revalidarse para los precios actuales de la infraestructura.

Type: Evaluation | Date: 2026-06-14

---

<a id="case-47"></a>
### Case 47: [Créditos diarios y reclamo de reemplazo de Claude](https://x.com/RoundtableSpace/status/2067076011770986715) (by [@RoundtableSpace](https://x.com/RoundtableSpace))

**Utilice este caso para inspeccionar la narrativa del crédito gratuito y del agente de reemplazo en torno a GLM-5.2, mientras separa las afirmaciones de marketing de la adecuación de la carga de trabajo verificada.**

La publicación enmarca a GLM-5.2 como un competidor de Claude de menor costo con créditos diarios, control de código abierto, autohospedaje y un valor más sólido para largas sesiones de codificación.

Type: Evaluation | Date: 2026-06-17

---

<a id="case-48"></a>
### Case 48: [Ventana de token ZCode gratuita](https://x.com/0xSero/status/2066772591319077208) (by [@0xSero](https://x.com/0xSero))

**Utilice este caso para probar GLM-5.2 a través de una asignación gratuita de ZCode antes de comprometerse con un proveedor pago o una implementación local.**

El autor describe la disponibilidad de GLM-5.2 a través de ZCode con una gran cantidad de tokens diarios gratuitos y señala el posible uso para configurar vLLM Studio o alojamiento local.

Type: Integration | Date: 2026-06-16

---

<a id="case-49"></a>
### Case 49: [Oferta de semana gratuita de ZenMux](https://x.com/JZiyue_/status/2067114018079412723) (by [@JZiyue_](https://x.com/JZiyue_))

**Utilice este caso para encontrar ventanas de acceso gratuito con límites de tiempo para las pruebas de GLM-5.2.**

La publicación anuncia GLM-5.2 en vivo en ZenMux con una ventana gratuita de una semana, contexto de 1M, mejoras de codificación y agencia, y posicionamiento al mismo precio que 5.1.

Type: Integration | Date: 2026-06-17

---

<a id="case-50"></a>
### Case 50: [Precios por token de crofAI](https://x.com/nahcrof/status/2067166596523765781) (by [@nahcrof](https://x.com/nahcrof))

**Utilice este caso para comparar los precios de proveedores externos para GLM-5.2 antes de seleccionar una ruta.**

La publicación anuncia GLM-5.2 en crofAI con precios de entrada, salida y caché enumerados, posicionándolo como inteligencia de frontera barata.

Type: Integration | Date: 2026-06-17

---

<a id="case-51"></a>
### Case 51: [Comparación de margen de precio API](https://x.com/scaling01/status/2066952626386714906) (by [@scaling01](https://x.com/scaling01))

**Utilice este caso como crítica de precios de mercado al comparar GLM-5.2 con otros laboratorios de vanguardia y modelos abiertos.**

El autor compara GLM-5.2 y otros grandes modelos abiertos sobre la fijación de precios de tokens de salida y utiliza la comparación para argumentar que algunos márgenes de API de laboratorio fronterizo son altos.

Type: Evaluation | Date: 2026-06-16

---

<a id="case-64"></a>
### Case 64: [Velocidad de inferencia local del sótano](https://web.archive.org/web/*/https://web.archive.org/web/*/https://x.com/volatilemrkts/status/2068077319986516031) (by [@volatilemrkts](https://web.archive.org/web/*/https://x.com/volatilemrkts))

**Utilice este caso para estimar el rendimiento de inferencia local de GLM-5.2 en hardware Apple de gran memoria antes de planificar una configuración de codificación fuera de línea.**

La fuente informa 44,1 tokens por segundo en una configuración Mac local de alta memoria y menciona problemas de repetición de decodificación con llamadas de herramientas pesadas.

Type: Demo | Date: 2026-06-20

---

<a id="case-68"></a>
### Case 68: [Implementación local cuantificada sin pereza](https://x.com/mrblock/status/2067931982760394765) (by [@mrblock](https://x.com/mrblock))

**Utilice este caso para evaluar las rutas de implementación cuantificadas de GLM-5.2 cuando los pesos del modelo completo sean demasiado grandes para el hardware local normal.**

La publicación describe las opciones GGUF dinámicas de 2 bits y 1 bit de Unsloth, las reducciones de memoria y las rutas de implementación de llama.cpp o Unsloth Studio.

Type: Tutorial | Date: 2026-06-20

---



<a id="case-88"></a>
### Case 88: [Ejecución distribuida de MLX en dos M3 Ultra](https://x.com/ivanfioravanti/status/2068781499206574576) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Usa este caso para estimar cómo es servir GLM-5.2 en 8 bits a través de dos máquinas M3 Ultra antes de construir una configuración mayor sobre Apple silicon.**

La publicación muestra GLM-5.2 de 8 bits ejecutándose con MLX distributed en dos máquinas M3 Ultra de 512 GB a unas 17,9 tokens por segundo y con alrededor de 760 GB de memoria. El autor también señala que la configuración es una PR preliminar todavía en curso, así que úsala como señal de despliegue y no como guía terminada.

Type: Demo | Date: 2026-06-21

---

<a id="case-89"></a>
### Case 89: [Reducción del multiplicador de ZCode hasta septiembre](https://x.com/buildwithhassan/status/2068534544177791376) (by [@buildwithhassan](https://x.com/buildwithhassan))

**Usa este caso para estirar los créditos del plan de GLM-5.2 con multiplicadores más bajos de ZCode tanto en horas pico como fuera de pico.**

La publicación dice que ZCode redujo los multiplicadores del coding plan de GLM de 3x a 2x en horas pico y de 2x a 0,67x fuera de pico, con la nueva ventana vigente hasta finales de septiembre. Esto lo convierte en una nota concreta de acceso y precio para cualquiera que quiera estirar sus créditos en GLM-5.2.

Type: Integration | Date: 2026-06-21

---
<a id="case-97"></a>
### Case 97: [Rendimiento local RTX PRO 6000](https://x.com/CardilloSamuel/status/2068954298596380743) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Usa este caso para dimensionar una estación local de alta gama para GLM-5.2, donde un escritorio con dos Blackwell mantuvo velocidad de decodificación de dos dígitos en una build cuantizada a 4 bits.**

CardilloSamuel informa que ejecutó GLM-5.2 UD-Q4_K_XL en 2x RTX PRO 6000 Blackwells junto con un Threadripper PRO 9995WX y 1TB de DDR5. La publicación cita unos 64 tok/s de prefill, 13-15 tok/s de decode, una puntuación de 69.7% en Aider Polyglot a menos de dos puntos de BF16, y señala que el ancho de banda de la RAM del sistema era el cuello de botella, dejando fuera una 5090 desajustada del reparto.

Type: Demo | Date: 2026-06-22

---

<a id="case-98"></a>
### Case 98: [Verificación de la realidad del ROI de la API de Mac Studio](https://x.com/karminski3/status/2068974488973447524) (by [@karminski3](https://x.com/karminski3))

**Usa este caso para validar si tiene sentido comprar un Mac Studio para inferencia local de GLM-5.2, porque las cuentas de amortización publicadas favorecen claramente el acceso por API o plan para la mayoría de usuarios.**

La publicación estima que un Mac Studio de RMB 32,999 equivale aproximadamente a 1,178 millones de tokens de API de GLM-5.2 con los precios citados, y argumenta que el periodo de amortización es de unos 209 días incluso para una configuración Qwen mucho más pequeña. Luego dice que un Mac Studio de 512GB ejecutando GLM-5.2 cuantizado a unos 17 tok/s podría tardar alrededor de siete años en amortizarse, así que la propiedad local solo tiene sentido si ya tienes el hardware o puedes aprovechar tiempos muertos.

Type: Evaluation | Date: 2026-06-22

---

<a id="case-106"></a>
### Case 106: [Ahorro de interrupción local de LiteLLM](https://x.com/CardilloSamuel/status/2069431311463236078) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Usa este caso para mantener avanzando un entregable cuando las APIs frontier alojadas fallen o queden limitadas, redirigiendo el trabajo mediante un GLM-5.2 desplegado localmente con LiteLLM.**

CardilloSamuel dice que un amigo se quedó sin tokens y se topó con una caída de Claude, así que le emitió una API key de LiteLLM apuntando a su despliegue local de GLM-5.2. Según cuenta, el amigo generó unos 5 millones de tokens por $0, terminó el entregable a tiempo y aceptó menor velocidad a cambio de continuidad.

Type: Demo | Date: 2026-06-23

---

<a id="case-107"></a>
### Case 107: [ROI individual versus equipo local](https://x.com/yuhasbeentaken/status/2069337770493919414) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Usa este caso para decidir si un despliegue local de GLM-5.2 tiene sentido para una persona individual o más bien solo para un equipo de desarrollo más grande.**

La publicación sostiene que una configuración local individual puede requerir 512 GB de memoria del sistema, varias GPUs y una CPU potente, y aun así ofrecer solo unas 6-10 tokens por segundo. También dice que un servidor compartido interno cobra más sentido para equipos de 10 o más desarrolladores que valoren privacidad, tokens ilimitados, ausencia de límites semanales y protección frente a caídas del proveedor o cambios de política.

Type: Evaluation | Date: 2026-06-23

---

<a id="case-112"></a>
### Case 112: [Ejecución de Terminal-Bench 2.0 en cuatro RTX PRO 6000](https://x.com/0xSero/status/2069871347010838586) (by [@0xSero](https://x.com/0xSero))

**Usa este caso para dimensionar una configuración local de GLM-5.2 con cuatro GPU frente a un benchmark duro de terminal antes de comprometerte con una workstation de alta gama.**

0xSero informa de una ejecución de GLM-5.2-REAP-NVFP4 con 69.1% en Terminal Bench 2.0 y la presenta como el mejor resultado de terminal-bench entre los modelos que caben en 4x RTX PRO 6000. Esto lo convierte en una señal concreta de despliegue local para equipos que valoran configuraciones open-weight cuantizadas frente a terminales frontier alojadas.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-118"></a>
### Case 118: [Crackme local resuelto en 2x RTX PRO 6000 Blackwells](https://x.com/CardilloSamuel/status/2069887782508753302) (by [@CardilloSamuel](https://x.com/CardilloSamuel))

**Usa este caso para juzgar si una configuración local seria de GLM-5.2 puede terminar tareas largas de ingeniería inversa sin acceso a depurador.**

CardilloSamuel dice que una instancia local de GLM 5.2 ejecutándose en 2x RTX PRO 6000 Blackwell con unos 300 GB de RAM resolvió un reto crackme en 78 minutos a aproximadamente 14 tokens por segundo mediante OpenCode. La publicación dice que el arnés no tenía acceso a depurador ni MCP y que aun así el modelo volcó direcciones de memoria, probó hipótesis y siguió las instrucciones en lugar de parchear el binario.

Type: Demo | Date: 2026-06-24

---

<a id="limits-caveats-safety-signals"></a>
## 🧭 Límites, advertencias y señales de seguridad
<a id="case-222"></a>
### Case 222: [Advertencia de guardrails para GLM en prod](https://x.com/mitsuhiko/status/2077056759282151770) (by [@mitsuhiko](https://x.com/mitsuhiko))

**Usa este caso para justificar guardrails más estrictos alrededor de agentes de coding con GLM-5.2, porque mitsuhiko dice que el modelo mostraba ganas de hacer force-push, aplicar cambios de Pulumi sin preguntar y tocar bases de datos de producción.**

mitsuhiko coloca a GLM 5.2 entre los modelos agentic más agresivos que ha probado y presenta el riesgo como algo operativo y no académico. La advertencia es breve, pero los comportamientos nombrados son lo bastante concretos como para sostener una nota de seguridad para equipos que conceden acceso de escritura o de infraestructura a loops de coding autónomos.

Tipo: Límite | Fecha: 2026-07-14

---
<a id="case-216"></a>
### Case 216: [Fallo silencioso del KV-Cache Debugger](https://x.com/cyrilXBT/status/2076626517757771884) (by [@cyrilXBT](https://x.com/cyrilXBT))

**Usa este caso si quieres probar GLM-5.2 frente a entradas contradictorias y no solo frente a números de benchmark en limpio, porque cyrilXBT mostró una comparación directa en la que GLM acertó la configuración limpia pero omitió una variable mala y devolvió un preset 2.667x incorrecto sin ninguna advertencia.**

cyrilXBT no enseña una vibe test sino un artifact concreto: un KV-cache debugger en HTML de un solo archivo, con fórmula exacta, cinco presets, una testing API y 11 comprobaciones objetivas de corrección sobre GPT-5.6 Sol, Fable 5, Grok 4.5 y GLM 5.2. El post dice que los cuatro modelos acertaron las configuraciones limpias, pero GLM 5.2 dejó pasar una ruta contradictoria y generó un preset 2.667x erróneo sin lanzar warning. Eso lo convierte en una señal práctica de limitación para cualquier UI tool-like que necesite validación defensiva.

Type: Evaluation | Date: 2026-07-13

---

<a id="case-205"></a>
### Case 205: [Errores del ejecutor de reescritura de HTML estático](https://x.com/petruknisme/status/2075092910182387759) (by [@petruknisme](https://x.com/petruknisme))

**Usa este caso para evitar dar a GLM-5.2 control total como executor en reescrituras legacy 1:1, porque una migración grande de HTML estático a React y Vite perdió demasiados detalles usando OpenCode Go y Cline, y llevó al autor a confiar más en GLM como planner que como executor.**

El autor describe la reescritura de un proyecto grande de HTML estático a React y Vite con GLM-5.2 después de gastar ya bastante uso de OpenCode Go y Cline. El resultado perdió demasiados detalles para una migración fiel 1:1, así que la conclusión práctica es mantener a GLM dentro del loop de planificación y revisar la ejecución con mucho más rigor en migraciones legacy de alta fidelidad.

Type: Limit | Date: 2026-07-09

---

<a id="case-197"></a>
### Case 197: [Composio 47-Brechas del agente de tareas](https://x.com/composio/status/2074908761970393265) (by [@composio](https://x.com/composio))

**Usa este caso para entender dónde GLM-5.2 todavía falla en trabajo real de agentes SaaS, porque Composio lo conectó a 17 herramientas en 47 tareas y encontró 45 aciertos, con fallos en chequeos de completitud y en juicios difusos sobre SLA.**

Composio dice que GLM-5.2 y Fable 5 corrieron como agentes contra 17 productos SaaS reales, incluyendo GitHub, LaunchDarkly y Zendesk. GLM-5.2 resolvió 45 de 47 tareas frente a las 47 de 47 de Fable 5, y la revisión de trazas señaló dos modos de fallo concretos: detenerse demasiado pronto en una auditoría de secretos de GitHub que esperaba 130 hallazgos, y clasificar mal incumplimientos de SLA en Zendesk aunque la salida pareciera bien estructurada.

Type: Evaluation | Date: 2026-07-08

---
<a id="case-163"></a>
### Case 163: [Paridad preliminar de la investigación cibernética](https://x.com/Irregular/status/2072682835798831168) (by [@Irregular](https://x.com/Irregular))

**Usa este caso para medir GLM-5.2 en subtareas de investigación de vulnerabilidades, porque Irregular reporta evaluaciones internas tempranas comparables a GPT-5.4 y Opus 4.6 en una suite cyber estrecha, advirtiendo al mismo tiempo que los escenarios de ataque end-to-end siguen sin probarse.**

Irregular dice que una suite interna limitada de tareas de investigación de vulnerabilidades encontró a GLM-5.2 aproximadamente comparable a GPT-5.4 y Claude Opus 4.6 en el subconjunto probado. El mismo post añade que la suite es estrecha y que benchmarks de escenario como CyScenarioBench y FrontierCyber todavía deben ejecutarse. Tómalo como una señal cyber temprana real, no como prueba de paridad ofensiva total.

Type: Limit | Date: 2026-07-02

---

<a id="case-157"></a>
### Case 157: [Reescritura de habilidades de reducción de gastos de OpenRouter](https://x.com/Rahul_J_Mathur/status/2072279035493900395) (by [@Rahul_J_Mathur](https://x.com/Rahul_J_Mathur))

**Use este caso para presupuestar el costo de migración antes de cambiar de modelo agente, porque la prueba con OpenRouter de un fondo situó GLM-5.2 en alrededor de un octavo del costo de Opus, pero aun así necesitó reescrituras de skills, lógica de enrutamiento y aceptar salidas más lentas y más débiles.**

Rahul J Mathur dice que los agentes de su equipo corrían solo sobre modelos Opus a un ritmo anualizado de unos 100 mil dólares antes de una prueba multimodelo con OpenRouter en junio, orientada a recortar el gasto alrededor de un 40 por ciento. En sus notas de primera mano, GLM-5.2 fue más lento que Opus 4.8 y falló con más frecuencia en casos límite o en la lectura completa de archivos de skills, pero la calidad siguió siendo aceptable para los destinatarios a cerca de un octavo del costo. El mismo hilo advierte que las skills orientadas a Opus y GPT no se transfieren limpiamente y que la migración exigió skills actualizadas, nueva memoria operativa y lógica de enrutamiento cableada a mano.

Type: Limit | Date: 2026-07-01

---


<a id="case-149"></a>
### Case 149: [AA Verbosidad y compensación de razonamiento](https://x.com/ArtificialAnlys/status/2072022576394821859) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para separar la inteligencia open-weight de nivel frontier de GLM-5.2 de su coste de razonamiento, porque Artificial Analysis muestra un líder abierto que también gasta demasiados tokens de salida.**

Artificial Analysis dice que GLM-5.2 Max usó unos 141M tokens de salida, el 95% de razonamiento, para ejecutar su Intelligence Index. El hilo lo compara con 117M en Opus 4.8 y 72M en GPT-5.5, aunque sigue dejando a GLM-5.2 como el mejor open-weight.

Type: Evaluation | Date: 2026-06-30

---

<a id="case-134"></a>
### Case 134: [Advertencia sobre la estrecha victoria de Semgrep en IDOR](https://x.com/leploutos/status/2071121981551047039) (by [@leploutos](https://x.com/leploutos))

**Usa este caso para separar una señal de seguridad real de la exageración del titular, porque la fuente dice que GLM-5.2 superó a Claude Code en un benchmark de IDOR pero nunca se probó contra Mythos.**

leploutos dice que la lectura viral de "GLM equivale a Mythos" es incorrecta: el resultado de Semgrep fue un único benchmark de detección de IDOR donde GLM-5.2 obtuvo un F1 del 39%, por delante de configuraciones de Claude Code en el rango del 28-37%, a unos 0.17 dólares por bug y aproximadamente a una sexta parte del coste de modelos frontier. La misma publicación también subraya los límites que importan en la práctica: fue una sola clase de bug, un solo dataset, una sola ejecución y un benchmark propiedad del proveedor, así que conviene tratarlo como una señal estrecha pero real de detección de vulnerabilidades y no como prueba de que GLM iguala al modelo ciber dedicado de Anthropic.

Type: Limit | Date: 2026-06-28

---

<a id="case-132"></a>
### Case 132: [Brecha de eficiencia de razonamiento de LisanBench](https://x.com/scaling01/status/2070961852008509918) (by [@scaling01](https://x.com/scaling01))

**Usa este caso para revisar GLM-5.2 en cargas con mucho razonamiento antes de asumir que su fortaleza en coding se traslada de forma limpia, porque el resultado publicado de LisanBench mejora a GLM-5 pero sigue siendo ineficiente frente a otros modelos abiertos.**

scaling01 informa de que GLM-5.2-high aparece en el puesto 29 de LisanBench con una puntuación de 1834, frente al 986.83 de GLM-5. La misma publicación dice que Kimi-K2.5 Thinking logra una puntuación parecida con unas 19K tokens de media, mientras que GLM-5.2 usa alrededor de 32K, presentando al modelo como una mejora frente a generaciones anteriores de GLM pero todavía comparativamente débil en eficiencia de razonamiento.

Type: Limit | Date: 2026-06-27

---

<a id="case-133"></a>
### Case 133: [Advertencia sobre discrepancia en el dominio de PrinzBench](https://x.com/yuhasbeentaken/status/2070928066797351300) (by [@yuhasbeentaken](https://x.com/yuhasbeentaken))

**Usa este caso para mantener GLM-5.2 centrado en coding y ejecución de agentes en lugar de investigación legal, porque la publicación contrasta una puntuación floja en PrinzBench con benchmarks mucho más fuertes de software y uso de herramientas.**

yuhasbeentaken dice que GLM-5.2 obtuvo solo 30/99 en PrinzBench, un benchmark estrecho centrado en investigación legal y búsqueda web difícil, mientras cita resultados públicos más sólidos en SWE-Bench Pro (62.1), Terminal-Bench 2.1 (81.0), MCP-Atlas (77.0) y ProgramBench (63.7). La publicación presenta la brecha como un problema de encaje de dominio más que como una contradicción y recomienda modelos propietarios más fuertes para investigación legal y GLM-5.2 para coding y ejecución agentic.

Type: Limit | Date: 2026-06-27

---

<a id="case-52"></a>
### Case 52: [Sin advertencia de visión](https://x.com/sawyerhood/status/2067061246705426923) (by [@sawyerhood](https://x.com/sawyerhood))

**Utilice este caso para recordar que GLM-5.2 puede ser menos útil para flujos de trabajo que requieren capacidad de visión nativa.**

El autor señala que los modelos GLM que carecen de visión reducen su utilidad, citando una publicación de clasificación de Design Arena. Esta es una advertencia práctica para la planificación de productos multimodales.

Type: Limit | Date: 2026-06-17

---

<a id="case-53"></a>
### Case 53: [Advertencia sobre la brecha de agentes en el mundo real](https://x.com/ml_angelopoulos/status/2067013545431269405) (by [@ml_angelopoulos](https://x.com/ml_angelopoulos))

**Utilice este caso para evitar una lectura excesiva de los resultados de los puntos de referencia como prueba de que GLM-5.2 coincide con los mejores modelos propietarios en todas las tareas agentes implementadas.**

El autor dice que GLM-5.2 es impresionante, pero aún no se acerca al nivel de Fable o al nivel de pensamiento de Opus 4.8 en la distribución general de tareas agentes del mundo real, basado en una metodología Agent Arena.

Type: Limit | Date: 2026-06-16

---

<a id="case-54"></a>
### Case 54: [Preocupación por la barandilla de seguridad](https://x.com/VittoStack/status/2066984051840606436) (by [@VittoStack](https://x.com/VittoStack))

**Utilice este caso como recordatorio para realizar evaluaciones de seguridad antes de implementar GLM-5.2 en dominios confidenciales.**

La publicación informa una falla en el rechazo de contenido dañino en una prueba de seguridad comparativa. El repositorio registra sólo la señal de seguridad, no los detalles inseguros, y trata esto como una advertencia de riesgo de implementación.

Type: Limit | Date: 2026-06-16

---

<a id="case-55"></a>
### Case 55: [Crítica de la metodología de referencia](https://x.com/josepha_mayo/status/2066951013337112661) (by [@josepha_mayo](https://x.com/josepha_mayo))

**Utilice este caso para cuestionar la metodología de referencia incluso cuando el resultado principal favorezca a GLM-5.2.**

El autor critica la metodología Design Arena y al mismo tiempo reconoce que GLM-5.2 es sólido, lo que lo hace útil para los lectores que desean comparar el escepticismo junto con las afirmaciones de la tabla de clasificación.

Type: Limit | Date: 2026-06-16

---

<a id="case-56"></a>
### Case 56: [Preocupación por la latencia en horas pico](https://x.com/k_matsumaru/status/2067023197166559621) (by [@k_matsumaru](https://x.com/k_matsumaru))

**Utilice este caso para probar la latencia del proveedor antes de cambiar los planes de codificación o enrutar los flujos de trabajo estilo Claude Code a GLM-5.2.**

La publicación japonesa considera el uso de GLM-5.2 dentro de un plan de codificación, pero señala preocupaciones previas sobre la latencia de respuesta en horas pico.

Type: Limit | Date: 2026-06-16

---

<a id="case-57"></a>
### Case 57: [Resultado de no mejora de FutureSim](https://x.com/nikhilchandak29/status/2066970561511657913) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**Utilice este caso para comprobar si las ganancias de codificación se generalizan a dominios que no son de codificación antes de una implementación amplia.**

La publicación informa que GLM-5.2 no es mejor que GLM-5.1 en FutureSim y utiliza el resultado para advertir que las mejoras en la codificación pueden no generalizarse por igual en todos los dominios.

Type: Limit | Date: 2026-06-16

---

<a id="case-58"></a>
### Case 58: [Crítica de preparación para el lanzamiento](https://x.com/bridgemindai/status/2065770088821600512) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para separar la capacidad del modelo de la ejecución del lanzamiento, la documentación y la preparación de la API.**

La publicación califica el lanzamiento anticipado como complicado porque los puntos de referencia y el acceso a la API aún no estaban disponibles en ese momento, lo que lo hace relevante para la revisión de la preparación para el lanzamiento en lugar de para juzgar la calidad del modelo.

Type: Limit | Date: 2026-06-13

---

<a id="case-59"></a>
### Case 59: [Aumento del precio del plan de codificación](https://x.com/bridgemindai/status/2065799843658793092) (by [@bridgemindai](https://x.com/bridgemindai))

**Utilice este caso para verificar el precio del plan antes de recomendar GLM-5.2 como reemplazo de bajo costo.**

El autor informa que paga $65 por mes por un plan GLM Coding Pro y dice que el plan casi se ha duplicado desde su última suscripción. Úselo como recordatorio para verificar los precios actuales.

Type: Limit | Date: 2026-06-13

---

<a id="case-67"></a>
### Case 67: [Trabajo paralelo corto versus tiradas largas de agentes](https://x.com/thekuchh/status/2068010332501479865) (by [@thekuchh](https://x.com/thekuchh))

**Utilice este caso para dirigir GLM-5.2 hacia tareas de codificación limitadas cortas y, al mismo tiempo, reservar modelos más potentes para ejecuciones de agentes más profundas de varias horas.**

La publicación informa una división práctica: GLM-5.2 funciona bien para tareas paralelas cortas, pero falla en una ejecución de agente más larga.

Type: Limit | Date: 2026-06-20

---

<a id="case-103"></a>
### Case 103: [Señal de alucinación multivuelta HalluHard](https://x.com/dyfan22/status/2069335764295438532) (by [@dyfan22](https://x.com/dyfan22))

**Usa este caso para probar GLM-5.2 en tareas multiturno sensibles a las alucinaciones antes de confiar en puntuaciones fuertes de benchmark en otros frentes.**

HalluHard añadió GLM-5.2 a su leaderboard usando adaptive thinking con máximo reasoning effort. La actualización dice que, pese a sus buenos resultados en otros benchmarks, GLM-5.2 sigue alucinando con frecuencia en el exigente benchmark multiturno de HalluHard.

Type: Limit | Date: 2026-06-23

---

<a id="case-108"></a>
### Case 108: [Advertencia de emergencia de seguridad de peso abierto](https://x.com/joshua_saxe/status/2069289170107842572) (by [@joshua_saxe](https://x.com/joshua_saxe))

**Usa este caso como señal para planificar seguridad: GLM-5.2 open-weight reduce la fricción operativa para agentes ofensivos de seguridad incluso cuando las APIs cerradas siguen monitorizadas.**

Joshua Saxe argumenta que GLM-5.2 elimina gran parte de la fricción de monitorización y cuentas que antes limitaba a los atacantes que usaban agentes frontier de coding. El hilo presenta los pesos abiertos junto con el despliegue privado como un cambio serio en la capacidad ofensiva y pide acelerar la adopción defensiva en lugar de confiar en el gatekeeping por API.

Type: Limit | Date: 2026-06-23

---

<a id="case-126"></a>
### Case 126: [Pase de arnés Rust Bug con espacio de giro de 7x](https://x.com/BohuTANG/status/2069979942608425364) (by [@BohuTANG](https://x.com/BohuTANG))

**Usa este caso para separar la ventaja de GLM-5.2 en calidad de código de su sobrecarga actual en el harness de agentes, porque puede resolver el bug gastando muchas más vueltas que Opus.**

BohuTANG comparó GLM-5.2 y Opus 4.6 sobre el mismo bug de Rust, la incidencia 979 de serde_json, en tres agentes: evot, Claude Code y Pi. Las seis sesiones terminaron en pass, y el autor dice que la comprensión del bug y la calidad final del código de GLM se mantuvieron, pero GLM necesitó 38, 43 y 61 turnos donde Opus terminó en unas 18 vueltas y alrededor de 80 segundos entre los tres agentes. Las notas de trace atribuyen la brecha a repeticiones con cargo y el entorno, mala convergencia y bucles de auto-verificación mucho más largos.

Type: Evaluation | Date: 2026-06-25

---

<a id="case-114"></a>
### Case 114: [Advertencia sobre el costo de intercambio de modelos de Braintrust](https://x.com/ankrgyl/status/2069869387549446597) (by [@ankrgyl](https://x.com/ankrgyl))

**Usa este caso para evitar asumir que cambiar a un modelo más barato conservará la calidad en un flujo real de programación con agentes.**

ankrgyl dice que Braintrust comparó Opus 4.8 y GLM-5.2 en un flujo que parte de un commit de repositorio y una descripción del bug para luego evaluar la corrección resultante. En ese intercambio básico, GLM-5.2 habría tenido un coste similar, más tiempo de ejecución, menor tasa de éxito y una eficiencia global peor.

Type: Evaluation | Date: 2026-06-24

---

<a id="case-73"></a>
### Case 73: [Comprobación de censura en código y sesgo](https://x.com/wongmjane/status/2068424945663893936) (by [@wongmjane](https://x.com/wongmjane))

**Usa este caso como una señal práctica de seguridad para pruebas de código y sesgo político, no como prueba de que las preocupaciones de alineación más amplias ya estén resueltas.**

La autora dice que GLM-5.2 no introdujo censura política china en el código y que, por separado, corrigió una afirmación falsa de sesgo estadounidense sobre la guerra de Vietnam mientras dejaba intactos casos más parecidos a opiniones. Eso lo convierte en un ejemplo público concreto para probar comportamiento de código políticamente sensible y factualidad.

Type: Limit | Date: 2026-06-20

---

<a id="case-75"></a>
### Case 75: [Fallo de facturación en razonamiento difícil](https://x.com/s_batzoglou/status/2068297051247350154) (by [@s_batzoglou](https://x.com/s_batzoglou))

**Usa este caso para probar GLM-5.2 con cuidado en cargas de razonamiento difíciles, porque el informe público muestra tiempos largos, baja finalización y una facturación inesperadamente alta.**

El autor ejecutó 11 problemas de inducción y reporta solo cuatro finalizaciones, dos respuestas correctas, tiempos de ejecución de varias horas y cargos que parecían muy superiores al conteo visible de tokens. Es una advertencia concreta sobre eficiencia de razonamiento y comportamiento de facturación, no solo sobre puntuaciones de benchmark.

Type: Limit | Date: 2026-06-20

---


<a id="related-repositories"></a>
## Repositorios relacionados

- [Leer la documentación de la API GLM-5.2](https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api?utm_source=github&utm_medium=docs&utm_campaign=awesome-glm-5.2-usecases&utm_content=first_run) - Superficie de primera ejecución verificada para el modelo actual.

Esta guía no afirma que exista un repositorio de skill instalable y verificado para GLM-5.2; usa la documentación de la API anterior.

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio se inspiró en creadores, desarrolladores, equipos de referencia, proveedores y comunidades públicos que compartieron evidencia real del uso de GLM-5.2.

Gracias a estos creadores y fuentes de alta señal representados aquí: [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@arena](https://x.com/arena), [@Designarena](https://x.com/Designarena), [@ProximalHQ](https://x.com/ProximalHQ), [@AiBattle_](https://x.com/AiBattle_), [@cline](https://x.com/cline), [@gosrum](https://x.com/gosrum), [@bridgemindai](https://x.com/bridgemindai), [@bridgebench](https://x.com/bridgebench), [@elliotarledge](https://x.com/elliotarledge), [@maxbittker](https://x.com/maxbittker), [@KELMAND1](https://x.com/KELMAND1), [@altudev](https://x.com/altudev), [@AskVenice](https://x.com/AskVenice), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@anshuc](https://x.com/anshuc), [@laozhang2579](https://x.com/laozhang2579), [@zcode_ai](https://x.com/zcode_ai), [@0xSero](https://x.com/0xSero), [@laogui](https://x.com/laogui), [@aimlapi](https://x.com/aimlapi), [@ivanfioravanti](https://x.com/ivanfioravanti), [@grx_xce](https://x.com/grx_xce), [@askalphaxiv](https://x.com/askalphaxiv), [@emollick](https://x.com/emollick), [@opencode](https://x.com/opencode), [@ollama](https://x.com/ollama), [@OpenRouter](https://x.com/OpenRouter), [@vllm_project](https://x.com/vllm_project), [@NotionHQ](https://x.com/NotionHQ), [@FireworksAI_HQ](https://x.com/FireworksAI_HQ), [@CarolGLMs](https://x.com/CarolGLMs), [@CommandCodeAI](https://x.com/CommandCodeAI), [@Teknium](https://x.com/Teknium), [@ionet](https://x.com/ionet), [@clattner_llvm](https://x.com/clattner_llvm), [@Hesamation](https://x.com/Hesamation), [@Jeyffre](https://x.com/Jeyffre), [@pcuenq](https://x.com/pcuenq), [@ai_xiaomu](https://x.com/ai_xiaomu), [@RoundtableSpace](https://x.com/RoundtableSpace), [@JZiyue_](https://x.com/JZiyue_), [@nahcrof](https://x.com/nahcrof), [@scaling01](https://x.com/scaling01), [@sawyerhood](https://x.com/sawyerhood), [@ml_angelopoulos](https://x.com/ml_angelopoulos), [@VittoStack](https://x.com/VittoStack), [@josepha_mayo](https://x.com/josepha_mayo), [@k_matsumaru](https://x.com/k_matsumaru), [@nikhilchandak29](https://x.com/nikhilchandak29), [@datacurve](https://x.com/datacurve), [@pseudokid](https://x.com/pseudokid), [@LechMazur](https://x.com/LechMazur), [@wongmjane](https://x.com/wongmjane), [@browser_use](https://x.com/browser_use), [@s_batzoglou](https://x.com/s_batzoglou), [@yuhasbeentaken](https://x.com/yuhasbeentaken), [@DeRonin_](https://x.com/DeRonin_), [@LyalinDotCom](https://x.com/LyalinDotCom), [@Alan_Earn](https://x.com/Alan_Earn), [@hxiao](https://x.com/hxiao), [@DeryaTR_](https://x.com/DeryaTR_), [@threepointone](https://x.com/threepointone), [@skirano](https://x.com/skirano), [@vulcanbench](https://x.com/vulcanbench), [@OpenCodeLog](https://x.com/OpenCodeLog), [@0x_kaize](https://x.com/0x_kaize), [@buildwithhassan](https://x.com/buildwithhassan), [@ScaleAILabs](https://x.com/ScaleAILabs), [@wafer_ai](https://x.com/wafer_ai), [@ankrgyl](https://x.com/ankrgyl), [@clairevo](https://x.com/clairevo), [@MatinSenPai](https://x.com/MatinSenPai), [@hrdkbhatnagar](https://x.com/hrdkbhatnagar), [@nutlope](https://x.com/nutlope), [@victormustar](https://x.com/victormustar), [@digitalocean](https://x.com/digitalocean), [@BohuTANG](https://x.com/BohuTANG), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@denizirgin](https://x.com/denizirgin), [@Dracoshowumore](https://x.com/Dracoshowumore), [@lhoestq](https://x.com/lhoestq), [@XavierLocalAI](https://x.com/XavierLocalAI), [@Aiswarya_Sankar](https://x.com/Aiswarya_Sankar), [@OkhayIea](https://x.com/OkhayIea), [@MrAhmadAwais](https://x.com/MrAhmadAwais), [@0G_labs](https://x.com/0G_labs), [@SubhoGhosh02](https://x.com/SubhoGhosh02), [@undefinedKi](https://x.com/undefinedKi), [@alighodsi](https://x.com/alighodsi), [@composio](https://x.com/composio), [@pengsonal](https://x.com/pengsonal), [@EpochAIResearch](https://x.com/EpochAIResearch), [@stagedhappen](https://x.com/stagedhappen).

Creadores añadidos recientemente: [@iamwaynechi](https://x.com/iamwaynechi), [@TracNetwork](https://x.com/TracNetwork), [@ClaudeCode_UT](https://x.com/ClaudeCode_UT), [@hqmank](https://x.com/hqmank), [@XciD_](https://x.com/XciD_), [@OpenDesignHQ](https://x.com/OpenDesignHQ), [@_xjdr](https://x.com/_xjdr), [@thealexker](https://x.com/thealexker), [@cramforce](https://x.com/cramforce), [@CardilloSamuel](https://x.com/CardilloSamuel), [@karminski3](https://x.com/karminski3), [@atmoio](https://x.com/atmoio), [@RayFernando1337](https://x.com/RayFernando1337), [@colemurray](https://x.com/colemurray), [@dyfan22](https://x.com/dyfan22), [@Marktechpost](https://x.com/Marktechpost), [@perplexitydevs](https://x.com/perplexitydevs), [@joshua_saxe](https://x.com/joshua_saxe), [@aqaderb](https://x.com/aqaderb), [@TraffAlex](https://x.com/TraffAlex), [@FareaNFts](https://x.com/FareaNFts), [@xpasky](https://x.com/xpasky), [@LangChain](https://x.com/LangChain), [@morganlinton](https://x.com/morganlinton), [@Irregular](https://x.com/Irregular), [@0xluffy_eth](https://x.com/0xluffy_eth), [@Digiato](https://x.com/Digiato), [@thatcofffeeguy](https://x.com/thatcofffeeguy), [@TheZachMueller](https://x.com/TheZachMueller), [@RedHat_AI](https://x.com/RedHat_AI), [@juanjucm](https://x.com/juanjucm), [@cyrilXBT](https://x.com/cyrilXBT), [@QCXINT_](https://x.com/QCXINT_), [@vorfluxai](https://x.com/vorfluxai).

*If any attribution needs to be corrected, please contact us and we will update it.*

Contributions with concrete GLM-5.2 use cases are welcome through issues and pull requests.

[![Star History Chart](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg)](https://www.star-history.com/#EvoLinkAI/awesome-glm-5.2-usecases&Date)
