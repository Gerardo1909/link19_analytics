# Análisis y Reestructuración de LinkedIn — Gerardo Toboso
> Generado: 2026-06-30 | Basado en datos reales del periodo Jul 2025 – Jun 2026

---

## 1. Diagnóstico: Qué dicen los datos

### Lo que funciona

| Señal | Dato | Implicancia |
|-------|------|-------------|
| Mejor tema | `bigdata` → 4855 imp. promedio | El contenido técnico profundo > contenido genérico |
| Segundo mejor | `pymc` → 4077 imp. promedio | Tu diferenciador estadístico tiene audiencia real |
| Mayor eng. rate | Post PySpark/Airflow → 2.62% | Mostrar proyectos reales > posts teóricos |
| Mejor día | Miércoles (2.8x vs domingo) | Publicar lunes–miércoles maximiza alcance |
| Mejor mes | Marzo (13 posts, 1095 imp/post) | Consistencia sostenida → resultados exponenciales |
| Follower spike | 2025-12-10: +92 en un día | Probablemente por un post de proyecto concreto |

> ⚠️ **Advertencia metodológica (leer antes de tratar esto como ley).** Son 50 posts y los rankings de tema están dominados por **un solo outlier**: el post de DuckDB (11274 imp.). `bigdata` son 3 posts con avg 4855, pero quitando DuckDB los otros 2 promedian ~1645. Lo mismo con `python` (5 posts, inflado por el mismo post). Conclusión real: *"bigdata es tu mejor tema"* en verdad dice *"un post se viralizó"* — es varianza, no una propiedad del tema. Tratá los rankings de tema y el "mejor día" como **señales débiles a re-medir con más volumen**, no como verdad establecida. Lo que sí es robusto: el formato que genera engagement (ver §4.1) y los gaps de abajo.

### Gaps críticos

| Problema | Dato | Consecuencia |
|----------|------|--------------|
| `fintech` topic tiene bajo rendimiento | 816 imp. promedio (vs 4855 bigdata) | El nicho fintech no aparece en el **contenido**, solo en el perfil |
| 40% de audiencia es Entry Level | Seniority demográfico | Estás atrayendo learners, no hiring managers ni peers |
| Engagement rate general bajo | 0.01 promedio | Posts informativos, poca fricción, poca conversación |
| Junio 2026: caída libre | 32 imp. promedio, 1 post | La consistencia se rompió justo antes de este análisis |

### El problema central

Tu perfil dice "fintech" pero tu contenido habla de data engineering general. Los reclutadores de fintech que buscan un Senior DE especializado no tienen forma de conectar los puntos. **El nicho tiene que aparecer tanto en el perfil como en el contenido.**

---

## 2. Top 5 Perfiles de Referencia en Fintech + Data Engineering

Estos perfiles fueron seleccionados por su posicionamiento claro en el cruce entre fintech y data engineering, con alta presencia y engagement en LinkedIn.

---

### Perfil 1 — Zach Wilson
**URL**: [linkedin.com/in/eczachly](https://www.linkedin.com/in/eczachly)

**Headline actual**:
> "Founder @ DataExpert.io | ADHD | Recovering Big Tech Engineer | 700k+ followers on all platforms"

**Por qué importa para Gerardo**:
- Ex-Airbnb, Facebook y Netflix → su credencial es haber resuelto problemas de datos a escala masiva en producción
- Su contenido no es "teoría de data engineering", es **experiencias concretas** con números reales
- Habla de errores y aprendizajes → engagement altísimo porque genera identificación
- Su audiencia son data engineers que quieren crecer, igual que la tuya

**Qué imitar**:
- Mencionar empresas concretas donde resolviste problemas reales (Figure) con métricas (22M calls/week, 71M registros)
- Posicionarse como alguien que "vivió el problema en producción" no como alguien que "sabe la teoría"
- El headline mezcla identidad profesional + misión clara → no solo el job title

**Headline pattern**: `[Rol actual] | [Misión/Apuesta] | [Prueba social cuantificada]`

---

### Perfil 2 — Andreas Kretz
**URL**: [linkedin.com/in/andreas-kretz](https://de.linkedin.com/in/andreas-kretz)

**Headline actual**:
> "I teach Data Engineering and create data & AI content | 15+ years of experience | 3x LinkedIn Top Voice | 230k+ YouTube subscribers"

**Por qué importa para Gerardo**:
- 3x LinkedIn Top Voice en Data Science & Analytics
- Combina **practitioner** (15+ años en producción) con **educator** (cursos, contenido)
- Su posicionamiento no es "busco trabajo en data engineering", es "soy el recurso de data engineering"
- Eso lo hace deseable para roles donde la empresa quiere a alguien que eleve al equipo

**Qué imitar**:
- Tu rol en Bayes Plurinacional (Technical Lead + instructor de inferencia bayesiana) te da exactamente esta credencial de educator
- Posicionarte como alguien que enseña hace que la gente te siga aunque no estén contratando, y cuando buscan contratar te tienen presente
- La especificidad temporal ("15+ años") da peso. Vos tenés la experiencia en Figure bien cuantificada

**Insight clave**: Andreas usa el headline para posicionarse como **creador**, no como candidato. Eso le da control de la narrativa.

---

### Perfil 3 — Darshil Parmar
**URL**: [linkedin.com/in/darshil-parmar](https://www.linkedin.com/in/darshil-parmar/)

**Headline actual**:
> "Freelance Data Engineer | Founder @DataVidhya | Helping Data Engineers Crack Jobs | 🎥YouTube (181K+)"

**Por qué importa para Gerardo**:
- Su contenido es 100% **proyectos prácticos con AWS** (igual que tu post de PySpark/Airflow que tuvo 2.62% engagement rate, el más alto del período)
- Construyó su audiencia mostrando arquitecturas end-to-end, no hablando de conceptos
- Fintech no es su nicho declarado, pero los proyectos que muestra son directamente applicables a pagos, transacciones, compliance

**Qué imitar**:
- La estructura de sus posts: **Arquitectura → Decisión técnica → Por qué elegí X sobre Y → Resultado medible**
- Tu post de DuckDB (11274 imp.) ya sigue este patrón. Es tu formato ganador. Hay que replicarlo con casos fintech
- Mostrar repos en GitHub linkados en el primer comentario, no en el post → evita penalización del algoritmo

**Insight de contenido**: Darshil convierte cada proyecto personal en contenido. Vos hacés lo mismo (Causalito, web scraper de hoteles, pipeline PySpark) pero no siempre conectás el proyecto con el dolor de negocio fintech.

---

### Perfil 4 — Naufal Samudra
**URL**: [linkedin.com/in/naufal-samudra](https://www.linkedin.com/in/naufal-samudra/)

**Headline actual**:
> "Senior Data Engineer - iFortepay | Airflow | Python | Docker | Data Pipeline Architect"

**Por qué importa para Gerardo**:
- Trabaja en **iFortepay**, una fintech real → exactamente el tipo de rol al que Gerardo apunta
- Su perfil es directo: rol + empresa + stack técnico + función (architect)
- No intenta ser influencer, apunta a ser el candidato ideal para hiring managers de fintech

**Qué imitar**:
- La claridad del stack en el headline: recruiters que hacen búsqueda `"Airflow" AND "Data Engineer" AND "fintech"` lo encuentran inmediatamente
- Vos tenés un stack más potente (AWS Lambda, DynamoDB Streams, PySpark, PyMC) pero menos visible en el headline
- Para el modo "búsqueda pasiva de trabajo", poner el stack en headline > poner filosofía

**Diferencia con Gerardo**: Naufal está posicionado para ser encontrado. Gerardo está posicionado para impresionar una vez que te encuentran. Necesitás ambas cosas.

---

### Perfil 5 — Venkata Krishna Gangavarapu
**URL**: [linkedin.com/in/venkata-krishna-gangavarapu-b79647187](https://www.linkedin.com/in/venkata-krishna-gangavarapu-b79647187/)

**Por qué importa para Gerardo**:
- Senior Data Engineer en una fintech que **procesa 3 billones de transacciones por día**
- Su perfil está completamente orientado a métricas de negocio, no de tecnología
- No habla de "Airflow", habla de "reducción de latencia de 40% en pipelines críticos de pagos"

**Qué imitar**:
- **Traducir el impacto técnico a impacto de negocio**: "22M invocaciones reducidas" → "ahorro de $X por año en AWS"
- Vos tenés los números (22M calls, 71M registros redactados, 160+ escalaciones eliminadas) pero están dentro del About. Ponerlos en el headline o en la primera línea del About es lo que marca la diferencia
- Los recruiters de fintech de US/Europa no leen el About sección completo. Necesitan ver el número en los primeros 300 caracteres

---

## 3. Reestructuración Concreta del Perfil

### 3.1 Header (Headline) — Cambio Prioritario

**Actual**:
> `Data & Cloud Engineer | E2E Fintech Solutions | Building High Impact Infrastructure`

**Problema**: Genérico, no tiene números, no tiene nicho específico dentro de fintech, no es searchable por stack.

**Versión A — Orientada a búsqueda pasiva (para que recruiters te encuentran)**:
> `Data Engineer | AWS Serverless & Pipelines | Fintech (Mortgage · Payments) | Cut 22M redundant API calls/week @ Figure`

**Versión B — Orientada a posicionamiento como referente (para que la audiencia te siga)**:
> `Data Engineer building production-grade fintech infrastructure | AWS · Python · Bayesian Systems | Figure | Bayes Plurinacional`

**Versión C — Híbrida (recomendada)**:
> `Senior Data Engineer | Fintech Infrastructure @ Figure | AWS Serverless · PyMC · Pipelines | –22M API calls/week`

**Por qué Versión C**:
- `Senior` → le habla a los hiring managers, no a entry levels (tu audiencia actual es 40% entry, querés que sea 40% seniors/managers)
- `Fintech Infrastructure @ Figure` → señal de dominio + empresa validada
- Stack explícito → SEO de LinkedIn
- Número concreto en headline → prueba social inmediata antes de que abran el perfil

> ⚠️ **Nota sobre "Senior".** Tu título formal en Figure es `Fullstack Software Engineer · Contract`. A favor de usar "Senior": 2.5 años en Figure + Technical Lead en Bayes + scope real de nivel senior (lideraste remediación de seguridad sobre 71M registros, migración de arquitectura, 99.9% uptime para 200+ clientes). En contra: un recruiter contrasta el "Senior" del headline contra el título "Contract/Fullstack" y los años visibles. **Decisión:** si tu scope respalda el título (y lo respalda), usalo — pero asegurate de que la Experiencia cuente esas responsabilidades de líder, no solo de ejecutor, para que "Senior" no quede huérfano. Si preferís cero fricción, la Versión A (sin "Senior", liderando con el número) es igual de fuerte.

---

### 3.2 About — Ajuste de Estructura (no de contenido)

Tu About actual es **excepcionalmente fuerte**. El problema no es lo que dice sino el orden.

**Regla crítica de LinkedIn 2025**: Los primeros 300 caracteres son lo único visible antes de "ver más". Todo lo que ponés después puede no ser leído nunca.

**Primeros 300 caracteres actuales**:
> "Data is only as good as the infrastructure that supports it. I don't just move data or write Lambdas; I design and fix production-grade, event-driven architectures where uptime, cost-efficiency, and strict data contracts are non-negotiable."

**Problema**: Es una declaración filosófica. No tiene números. No menciona fintech. No captura la atención de alguien que en 5 segundos decide si sigue leyendo.

**Primera línea recomendada** (los primeros 150 caracteres):
> "I cut 22M redundant API calls/week at a US mortgage fintech (Figure). I redacted 71M+ sensitive records from production DynamoDB. I don't just build pipelines — I fix the ones that cost money and wake people up at 3 AM."

> 💡 **Métrica de negocio sin explotar.** Tu Experiencia tiene una línea más fuerte que las técnicas para hablarle a un hiring manager no-técnico: **"reduje el cierre de hipotecas de 30 días a menos de 7"**. Eso es impacto de negocio puro (el patrón Venkata del §2.5). Considerá abrir con ella o sumarla al primer párrafo: *"I helped cut mortgage closing time from 30 days to under 7 at a US fintech."* Un manager entiende eso al instante; "22M API calls" lo entiende un ingeniero. Tené ambas a mano según a quién le hablás.

**Estructura recomendada del About completo**:

```
[PÁRRAFO 1 — Hook con métricas, visible antes de "ver más"]
I cut 22M redundant API calls/week at a US mortgage fintech. I redacted 71M+ sensitive 
records from production DynamoDB. I don't just build pipelines — I fix the ones that 
cost money and wake people up at 3 AM.

[PÁRRAFO 2 — Quién sos y qué hacés diferente]
Hybrid background: Data Science (BSc @ UNSAM) + Systems Engineering + 2+ years building 
production serverless infrastructure for Figure, a US fintech orchestrating 50+ AWS Lambdas 
and 30+ financial APIs (Experian, Plaid, DocuTech).

[PÁRRAFO 3 — Tu diferenciador técnico (Bayesian + Data Engineering)]
What sets me apart: I apply Bayesian and probabilistic thinking to data quality problems — 
not as an academic exercise, but as a production layer (anomaly detection, MLOps pipelines, 
uncertainty quantification). This is the intersection where most Data Engineers don't go.

[PÁRRAFO 4 — Stack concreto]
Core Stack:
• Cloud & Infra: AWS (Lambda, DynamoDB Streams, SQS, API Gateway, S3), Serverless
• Data: Python, PySpark, Airflow, DuckDB, SQL (PostgreSQL), dbt
• Stats: Bayesian Inference (PyMC), Causal Discovery
• Frontend: TypeScript, React (when the data needs a face)

[PÁRRAFO 5 — CTA]
If your fintech platform is struggling with API reliability, AWS cost overruns, or data 
pipelines that break under scale — let's talk.
📫 gerardotoboso1909@gmail.com
```

---

### 3.3 Experiencia — Ajuste de Título en Figure

**Actual**: `Fullstack Software Engineer | Cloud & Serverless Architect`

**Problema**: "Fullstack" te asocia con front/back, no con data engineering. Los recruiters que buscan data engineers en fintech filtran por `"Data Engineer" OR "Data Platform" OR "Backend Engineer"`.

**Sugerencia**: Si podés editar el título (es tu propio perfil):
> `Backend & Data Infrastructure Engineer | Cloud & Serverless Architect`

o

> `Data Platform Engineer | Serverless & Cloud Infrastructure (AWS)`

Esto preserva la verdad (hacés fullstack pero tu core es infra/data) y te posiciona mejor en búsquedas de DE roles.

---

## 4. Estrategia de Contenido Alineada con los Datos

### 4.1 Tu fórmula ganadora — distinguí alcance de engagement

Hay **dos métricas distintas** y no optimizan lo mismo. No las mezcles:

| Post | Impressions | Engagement rate | Qué optimiza |
|------|-------------|-----------------|--------------|
| #1 DuckDB (opinión/comparación) | 11274 | **0.34%** (bajo) | **Alcance** — te ve mucha gente, conversan pocos |
| #8 PySpark (proyecto propio + GitHub) | 2480 | **2.62%** (el más alto) | **Conversación** — menos ojos, pero los correctos comentan |

Tus 4 posts de mayor engagement son **todos de proyecto real**: #8 PySpark (2.62%), #10 scraper (1.80%), #9 Causalito (1.56%), #5 diseño ETL (1.05%). El viral de DuckDB, irónicamente, tuvo de los engagement rates **más bajos**.

**Para tu objetivo (sostener trabajo + atraer ofertas, no ser influencer), priorizá engagement sobre alcance.** El formato a replicar es el **#8/#10: proyecto propio → decisión de arquitectura → por qué elegí X sobre Y → número/resultado → pregunta abierta + repo en el primer comentario.** El formato DuckDB (opinión técnica con benchmark) sirve como complemento ocasional para alcance, no como columna vertebral.

En todos los casos: posts de "hice X, medí Y, aprendí Z" — no posts filosóficos.

### 4.2 Ajuste de temas para audiencia fintech

El problema: `fintech` como hashtag solo tiene 816 imp. promedio, pero tus mejores posts (`bigdata`, `pymc`, `python`) son técnicos generales.

**La solución no es hablar más de fintech. Es contextualizar los temas técnicos dentro de casos fintech.**

| Tema actual (genérico) | Versión fintech-contextualizada |
|------------------------|--------------------------------|
| "DuckDB vs Pandas" | "Cómo auditamos 500K transacciones de pagos localmente con DuckDB sin clusters" |
| "Inferencia bayesiana en producción" | "Detector de fraude probabilístico con PyMC: cómo redujimos falsos positivos en un pipeline de mortgage" |
| "Cuándo NO usar Airflow" | "Pipelines de ingesta financiera event-driven vs batch: la decisión que tomamos en Figure" |
| "RAG architecture" | "Cómo diseñé Causalito para que sea confiable en un dominio financiero regulado" |

### 4.3 Calendario propuesto (basado en datos)

- **Frecuencia**: 3 posts/semana (Marzo fue tu mejor mes con 13 posts → 4.3/semana). Nota: el promedio alto de Marzo está inflado por el post viral; la consistencia ayuda pero el dato no prueba "exponencial". Apuntá a 3/semana sostenibles antes que a picos.
- **Mejor día**: con ~7 posts por día de semana, la ventaja del miércoles es señal débil (y el viral cayó un **lunes**). Probá Miércoles como primera opción, Lunes y Viernes como segundas, y **re-medí con tus propios datos en 2-3 meses** en vez de fijar el día por ahora.
- **Mix por semana**:
  - 1 post técnico profundo (arquitectura, decisión, benchmark) → apunta a `bigdata`, `python`, `aws`
  - 1 post de proyecto o build-in-public → conecta con fintech explícitamente
  - 1 post de opinión/reflexión corta → genera discusión, sube engagement rate

### 4.4 Audiencia objetivo real (vs audiencia actual)

| Dimensión | Ahora (40% Entry) | Objetivo |
|-----------|-------------------|----------|
| Seniority | Entry (40%), Senior (33%) | Senior (45%), Manager (20%), Entry (25%) |
| Industria | IT Services (18%) | Financial Services / Fintech (30%+) |
| Rol | Data Engineer (10%), Data Scientist (5%) | Data Engineer (15%), Engineering Manager (10%) |

**Cómo lograrlo**: Cambiar el lenguaje de los posts de "aquí te enseño X" (atrae entry) a "así resolvimos X en producción con estas limitaciones" (atrae seniors/managers). La diferencia es sutil pero poderosa.

---

## 5. Resumen de Acciones Prioritarias

| Prioridad | Acción | Impacto esperado |
|-----------|--------|-----------------|
| 🔴 Alta | Cambiar headline → Versión C recomendada | SEO + primera impresión |
| 🔴 Alta | Reescribir primeros 300 chars del About con métricas | Retención de lectores |
| 🟡 Media | Ajustar título de Figure a "Data Platform Engineer" o similar | Búsqueda pasiva por recruiters |
| 🟡 Media | Volver a consistencia de 3 posts/semana en miércoles | Recuperar momentum de Marzo |
| 🟡 Media | Contextualizar posts técnicos en casos fintech | Audiencia objetivo + diferenciación |
| 🟢 Baja | Agregar Featured section con tu mejor post (DuckDB) + repo GitHub | Trust signal |
| 🟢 Baja | Crear un post "build in public" del pipeline de analytics de LinkedIn (este repo) | Autenticidad + `buildinpublic` funciona (952 imp.) |

---

## 6. Perfiles de Referencia — Links Directos

| # | Nombre | URL | Por qué seguirlo |
|---|--------|-----|-----------------|
| 1 | Zach Wilson | [linkedin.com/in/eczachly](https://www.linkedin.com/in/eczachly) | Ex Big Tech → educator → misión clara |
| 2 | Andreas Kretz | [linkedin.com/in/andreas-kretz](https://de.linkedin.com/in/andreas-kretz) | 3x Top Voice, combina practitioner + creator |
| 3 | Darshil Parmar | [linkedin.com/in/darshil-parmar](https://www.linkedin.com/in/darshil-parmar/) | Proyectos prácticos AWS → alta conversión |
| 4 | Naufal Samudra | [linkedin.com/in/naufal-samudra](https://www.linkedin.com/in/naufal-samudra/) | DE en fintech real, perfil searchable |
| 5 | Venkata Gangavarapu | [linkedin.com/in/venkata-krishna-gangavarapu-b79647187](https://www.linkedin.com/in/venkata-krishna-gangavarapu-b79647187/) | Métricas de negocio, no de tecnología |

---

## 7. Conclusión

Tu perfil actual tiene el contenido correcto pero el **orden de impacto incorrecto**. Las métricas que más valen (22M calls, 71M registros, 160 escalaciones) están enterradas en el medio del About cuando deberían estar en las primeras 150 caracteres.

Tu contenido ya tiene el formato correcto (posts técnicos con benchmark real) pero le falta **ancla fintech** para que la audiencia correcta te encuentre.

La estrategia del "no reinventar la rueda" es la correcta: Zach Wilson, Andreas Kretz y Darshil Parmar ya demostraron que el contenido técnico profundo con casos reales y números concretos convierte. Solo hay que agregarle el contexto fintech que es tu ventaja competitiva real.

---

*Fuentes: Datos analíticos del pipeline `/data/output/linkedin_report.md` · Búsqueda web LinkedIn creators data engineering 2025-2026 · Perfiles públicos referenciados*
