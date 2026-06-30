# link19_analytics

**Dejo de adivinar qué postear en LinkedIn. Ahora lo decido con datos.**

Un pipeline ETL en Python que toma el export crudo de LinkedIn Analytics (Excel), lo transforma en datos limpios y genera un reporte con recomendaciones accionables: qué día postear, qué temas funcionan, quién es mi audiencia y qué posts merecen un análisis más profundo.

## El problema

LinkedIn te da un Excel con datos desordenados: hojas con formatos distintos, dos tablas pegadas lado a lado, porcentajes como strings, fechas en formato americano. Analizarlo a mano es tedioso y lo terminás haciendo una vez y nunca más. Mientras tanto, seguís posteando por intuición.

## La solución

Un comando. Un reporte.

```bash
uv run python src/pipeline.py
```

El pipeline:

1. **Extrae** cada hoja del Excel y la normaliza en un CSV limpio
2. **Transforma** los datos: parsea fechas, calcula engagement rates, extrae temas de las URLs, agrega métricas temporales
3. **Analiza** patrones: mejor día de la semana, mejor mes, temas que más traccionan, crecimiento de followers, composición demográfica de la audiencia
4. **Genera** un reporte Markdown con recomendaciones concretas y los top posts listos para análisis de texto con un LLM

## Qué descubrí con mis propios datos

| Hallazgo | Dato |
|----------|------|
| Mejor día para postear | Miércoles (2.8x vs domingo) |
| Mejor mes | Marzo (1095 impressions/día promedio) |
| Tema top | `bigdata` — 4855 impressions promedio |
| Audiencia principal | Data Engineers (10%), Entry level (40%) |
| Followers ganados en 365 días | 1,785 (4.89/día) |
| Posts analizados | 50 |

## Estructura

```
data/
  raw/               # Excel descargado de LinkedIn (input)
  processed/          # CSVs limpios generados por el pipeline
  output/             # Reporte final (.md)
src/
  extract.py          # Excel → CSVs
  transform.py        # Limpieza + feature engineering
  analyze.py          # Análisis estadístico + recomendaciones
  report.py           # Generación del reporte Markdown
  pipeline.py         # Orquestador
```

## Cómo usarlo

**Requisitos**: Python 3.11+ y [uv](https://docs.astral.sh/uv/)

```bash
# 1. Instalar dependencias
uv sync

# 2. Dejar el Excel de LinkedIn en data/raw/
#    (LinkedIn > Analytics > Export)

# 3. Ejecutar
uv run python src/pipeline.py

# 4. Revisar el reporte
cat data/output/linkedin_report.md
```

## Stack

Solo dos dependencias: **pandas** y **openpyxl**. Nada más. El análisis más potente no viene de librerías complejas sino de hacerle las preguntas correctas a datos limpios.

## Próximos pasos

- Integrar texto de los posts top para análisis NLP con un LLM
- Correlación entre frecuencia de posting y crecimiento de followers
- Comparación entre períodos (quarter vs quarter)
