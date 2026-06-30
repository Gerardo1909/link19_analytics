# Plan de Acción — Volverse "el data engineer que las empresas quieren contratar"
> Gerardo Toboso · Generado 2026-06-30
> Objetivo personal: **sostener trabajo y atraer ofertas** (no ser influencer). LinkedIn como activo de carrera, no como canal de creador.

---

## 0. La regla mental que cambia todo

No estás construyendo una audiencia. Estás construyendo **evidencia pública de que sos contratable**, dejada en un lugar donde recruiters y managers buscan.

Eso cambia las prioridades respecto a un influencer:
- No necesitás postear todos los días. Necesitás **consistencia sostenible** (que no abandones a los 3 meses, como pasó con Junio).
- No perseguís viralidad (alcance). Perseguís **que la persona correcta vea 2-3 pruebas de competencia** y guarde tu nombre.
- Tu mejor "contenido" no es un post: es tu **perfil + un historial de posts de proyecto que demuestran cómo pensás**. El post es el anzuelo; el perfil es el cierre.

> Métrica de éxito real (no likes): **(a)** recruiters relevantes que te escriben al DM, **(b)** managers que comentan tus posts de proyecto, **(c)** que cuando alguien googlea "Gerardo Toboso data engineer" encuentre un perfil coherente. Likes e impresiones son ruido para tu objetivo.

---

## 1. Roadmap de 90 días (lo concreto)

### Semana 1 — Arreglar el perfil (one-time, alto impacto)
Esto rinde más que 3 meses de posts. Hacelo primero.

- [ ] **Headline** → Versión A o C del análisis de reestructuración. Número concreto adentro.
- [ ] **About** → reordenar: primeros 150 chars con métrica (22M calls *o* "cierre de hipotecas 30→7 días"). Ya tenés el contenido, solo cambiás el orden.
- [ ] **Título en Figure** → de "Fullstack Software Engineer" a algo con "Data" / "Backend & Data Infrastructure". Preserva la verdad, mejora la búsqueda.
- [ ] **Featured section** → fijá tu post de PySpark (#8) y el de Causalito (#9) con links a GitHub. Es lo primero que ve un recruiter que llega a tu perfil.
- [ ] **Skills** → asegurate que estén en orden de prioridad de búsqueda: AWS, Python, Data Engineering, Airflow, PySpark, Serverless arriba. PyMC/Bayesian como diferenciador.
- [ ] **"Open to work"** (modo privado, solo recruiters) → si estás abierto a ofertas, activalo. No es visible públicamente y te mete en los filtros de recruiters.

### Semanas 2-12 — Ritmo de contenido sostenible
- **Meta realista: 2 posts/semana.** No 3, no 4. Dos que sostengas 3 meses le ganan a cinco que abandonás en tres semanas. Subís a 3 solo si los 2 ya son automáticos.
- **Día**: miércoles fijo el principal, el segundo lunes o viernes. (Re-medís a los 2-3 meses con tus datos.)
- **Mezcla por semana**:
  - **Post A — Proyecto / trabajo real** (tu formato ganador, §4.1 del análisis): proyecto propio o algo de tu día laboral anonimizado → decisión de arquitectura → por qué X sobre Y → número → pregunta. Repo o link en el **primer comentario**, no en el post.
  - **Post B — Reflexión técnica corta o "build in public"**: una decisión, un error que corregiste, una herramienta que probaste. Más liviano, genera conversación.
- **Regla de oro de engagement**: respondé **todos** los comentarios de tus posts en la primera hora. Para tu objetivo, una conversación de calidad con un manager en los comentarios vale más que 500 impresiones.

---

## 2. El motor de contenido (de dónde sale el material para no secarte)

El problema #1 de sostenerlo es "no sé qué postear". Solución: **no inventes temas, capturá lo que ya hacés.** Tres fuentes, en orden de facilidad:

### Fuente 1 — Tu propio trabajo (la mina principal, anonimizada)
Cada semana, en tu trabajo de Figure / Bayes, pasan cosas posteables. Quitando nombres de clientes, datos internos y números confidenciales, contá el **patrón técnico y la decisión**, no el caso específico.

> **Ritual semanal (15 min, viernes):** abrí una nota titulada "posteable". Cuando durante la semana resuelvas algo, anotá una línea: *"esta semana decidí X en vez de Y porque Z"*. El viernes elegís una y la convertís en post. Sin la nota, el viernes no te acordás de nada.

**Qué SÍ se puede contar (con privacidad):**
- El *tipo* de problema: "un pipeline event-driven que reprocesaba eventos duplicados".
- La decisión de arquitectura y el trade-off: "elegí idempotencia con dedup keys en vez de locking".
- El resultado en términos genéricos o porcentuales: "bajó el reprocesamiento ~40%".
- La lección transferible.

**Qué NO:**
- Nombres de clientes, montos reales, datos de usuarios, secretos, capturas de código propietario, nada que viole tu contrato. Ante la duda, generalizá. Reemplazá "Figure" por "una fintech de mortgage en US" si hace falta.

> Plantilla lista: *"Esta semana me crucé con [tipo de problema, sin nombres]. La reacción default era [solución obvia]. Elegí [tu decisión] porque [trade-off]. Resultado: [métrica genérica]. ¿Vos cómo lo resolverías?"* — eso es un post #8 en 6 líneas.

### Fuente 2 — Tus proyectos personales (ya tenés varios)
Causalito, el web scraper de hoteles, el pipeline de PySpark, **y este mismo repo de analytics de LinkedIn**. Cada uno da 2-3 posts:
- Uno de arquitectura/decisión.
- Uno de un detalle técnico puntual ("cómo testée la calidad de retrieval sin llamar al LLM").
- Uno de "qué aprendí / qué haría distinto".

> Acción concreta esta semana: el pipeline de analytics de LinkedIn (este repo) es un post "build in public" perfecto — analizaste tus propios datos para mejorar tu perfil. Meta-narrativa que funciona (`buildinpublic` ya te rindió 952 imp.).

### Fuente 3 — Reaccionar a la industria (el relleno, no la base)
Cuando no tengas material propio, comentá algo del mercado **con tu ángulo técnico**, no repitiendo la noticia. Para esto necesitás estar informado — ver §3.

> Importante: esta fuente es la *menos* valiosa para tu objetivo. Un recruiter no te contrata por tu opinión sobre la noticia de OpenAI; te contrata por la evidencia de que construís sistemas. Usá la Fuente 3 como máximo 1 de cada 4 posts.

---

## 3. Mantenerte informado (rutina de input, 20 min/día)

No para "tener de qué postear", sino para **no quedarte atrás del mercado** y poder hablar el idioma actual en entrevistas. Seguí estas fuentes:

**Newsletters (las que valen para Data Eng / fintech):**
- **Data Engineering Weekly** (Ananth Packkildurai) — el estándar del nicho.
- **Seattle Data Guy** / **Start Data Engineering** — práctico, orientado a carrera.
- **The Pragmatic Engineer** (Gergely Orosz) — para entender el mercado laboral tech y qué valoran los hiring managers.
- **Blog de tu propio stack**: AWS Big Data Blog, dbt Developer Blog.

**Para seguir en LinkedIn (no para copiar, para calibrar):**
- Zach Wilson, Andreas Kretz, Darshil Parmar (del análisis). Mirá *qué formato* usan, no el tema.

**Comunidades donde están los que contratan:**
- Locales: comunidades de data de Argentina/LATAM (Data Engineering en español, meetups de AWS UG Buenos Aires).
- Foros: r/dataengineering para pulso de mercado.

> Ritual: 20 min a la mañana. Leés, y si algo te dispara una idea técnica, va a la nota "posteable". El input alimenta el output sin esfuerzo extra.

---

## 4. Dónde profundizar conocimientos (alineación con el mercado HOY)

Esto es lo que más mueve la aguja para "ser contratable", más que cualquier post. Sugerencias fuertes, priorizadas según tu perfil actual (sos fuerte en AWS serverless + Bayesian, te falta cierta caja de herramientas que el mercado 2026 da por sentada).

### 🔴 Prioridad alta — lo que el mercado pide y vos tenés flojo o no visible

1. **Orquestación moderna y formatos de tabla abiertos.** Tenés Airflow, pero el mercado se movió. Profundizá en:
   - **dbt** (lo mencionás pero no lo demostrás en proyectos) — es prácticamente un requisito en job posts de analytics engineering / DE.
   - **Tablas abiertas: Apache Iceberg / Delta Lake** — el tema caliente 2025-2026. Saber por qué un lakehouse con Iceberg reemplaza al warehouse clásico te pone en la conversación senior.
   - Un orquestador moderno como complemento mental a Airflow: **Dagster** o **Prefect** (entender el modelo asset-based).

2. **Streaming / datos en tiempo real.** Ya hacés event-driven con DynamoDB Streams + SQS — eso es oro. Capitalizalo aprendiendo **Kafka / Kinesis** y patrones de **CDC (Change Data Capture)**. Para fintech (pagos, fraude) el real-time es *el* diferenciador. Es tu camino natural de especialización.

3. **Demostrar el lado "Data Platform / Reliability", no solo "Backend".** El mercado valora hoy el **Data Quality / Observability** como disciplina: contratos de datos, tests de datos (Great Expectations / dbt tests), lineage. Vos ya pensás así (lo del detector bayesiano de anomalías es exactamente esto) — solo te falta nombrarlo con el vocabulario que buscan los recruiters.

### 🟡 Prioridad media — diferenciadores que ya tenés y conviene afilar

4. **Tu cruce Bayesian + Data Engineering es tu foso.** Casi nadie lo tiene. No lo abandones por seguir la corriente. Convertilo en una narrativa: *"data quality probabilístico"*, *"uncertainty-aware pipelines"*. Es exactamente lo que te hace memorable vs. otros 500 DEs con el mismo stack de AWS.

5. **MLOps / LLMOps aplicado.** Causalito ya te mete acá. Profundizá en **evaluación de sistemas RAG** y **observabilidad de LLMs** (el "confidence engine" que armaste es justo lo que la industria está descubriendo que necesita). Esto cruza tu fortaleza estadística con el tema más demandado del momento.

### 🟢 Prioridad baja — completar el perfil, no urgente

6. **Infra as Code (Terraform).** Si vas a roles senior de plataforma, lo van a esperar. No es urgente pero suma.
7. **Un cloud secundario conceptualmente** (GCP BigQuery / Snowflake): no para dominarlo, sino para no quedar pegado a "solo AWS" en filtros.

> **Cómo aprender Y postear a la vez (mata dos pájaros):** elegí UN tema de prioridad alta (sugerencia: **Iceberg** o **streaming con Kafka/CDC**), armá un proyecto chico end-to-end, y documentá el proceso en 3-4 posts ("build in public"). Aprendés algo que el mercado pide *y* generás evidencia pública de que lo sabés. Es el mejor ROI de tu tiempo.

---

## 5. Checklist de mantenimiento (para que no se caiga como en Junio)

**Diario (20 min):** leer 1-2 newsletters/feeds → si surge idea, a la nota "posteable".

**Semanal (~1h total):**
- [ ] Viernes: elegir 2 ideas de la nota "posteable" y escribir los posts de la semana siguiente.
- [ ] Programar 2 posts (miércoles + lunes/viernes).
- [ ] Responder todos los comentarios pendientes de la semana.
- [ ] Comentar con sustancia en 3-5 posts de gente del nicho (managers, peers) — esto te pone en su radar más que postear.

**Mensual (~30 min):**
- [ ] Mirar tus métricas: ¿qué post tuvo más *engagement* (no impresiones)? Replicar ese formato.
- [ ] ¿Algún recruiter/manager escribió o comentó? Esa es tu métrica real.
- [ ] Actualizar perfil si hubo logro nuevo en el trabajo.

**Trimestral:**
- [ ] Re-correr este pipeline de analytics y comparar: ¿subió el % de audiencia Senior/Manager? ¿bajó el % Entry? Esa es la prueba de que la estrategia funciona.
- [ ] Ajustar día/hora con datos nuevos (ya no con los 50 posts actuales).

---

## 6. Lo que NO tenés que hacer (para vos específicamente)

- ❌ No postees diario. Te quemás y abandonás (ya pasó). 2/semana sostenibles.
- ❌ No persigas viralidad ni likes. No es tu objetivo. Un post de 800 impresiones que te trae un DM de un recruiter > un post de 11k que no trae nada.
- ❌ No te vuelvas "creador de contenido genérico de carrera" (motivación, tips de productividad). Atrae a la audiencia equivocada (entry-level). Quedate en lo técnico-profundo.
- ❌ No abandones tu diferenciador bayesiano para parecerte más al DE promedio. Es al revés: es tu ventaja.
- ❌ No copies el formato exacto de los influencers. Tomá la estructura, poné tu sustancia técnica real.

---

## 7. Si tuvieras que hacer solo 5 cosas

1. **Arreglar el perfil esta semana** (headline + primeros 150 chars del About + Featured). Mayor ROI de todo el plan.
2. **Activar "Open to work" en modo recruiter** si buscás ofertas.
3. **Nota "posteable" + 2 posts/semana de proyecto/trabajo anonimizado.** Sostener > intensidad.
4. **Aprender Iceberg o streaming/CDC con un proyecto chico, y documentarlo en posts.** Mercado + evidencia a la vez.
5. **Responder comentarios y comentar a managers del nicho.** La conversación es lo que convierte en oferta, no el post.

---

*Basado en: `linkedin_report.md` (analytics reales), `linkedin_restructure_analysis.md` (reestructuración corregida), y los componentes actuales del perfil en `/linkedin_structure`.*
