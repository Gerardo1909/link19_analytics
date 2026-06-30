"""Report: genera el reporte .md final con hallazgos y recomendaciones."""

from pathlib import Path

import pandas as pd


def df_to_md_table(df: pd.DataFrame, max_rows: int = 15) -> str:
    display = df.head(max_rows)
    if isinstance(display.index, pd.Index) and display.index.name:
        display = display.reset_index()
    headers = "| " + " | ".join(str(c) for c in display.columns) + " |"
    separator = "| " + " | ".join("---" for _ in display.columns) + " |"
    rows = []
    for _, row in display.iterrows():
        rows.append("| " + " | ".join(str(v) for v in row.values) + " |")
    return "\n".join([headers, separator] + rows)


def generate_report(findings: dict, output_dir: str | Path) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    discovery = findings["discovery"]
    impressions = discovery.iloc[0].get("Impressions", "N/A")
    members = discovery.iloc[0].get("Members reached", "N/A")

    sections = []

    sections.append("# LinkedIn Analytics Report — Gerardo Toboso")
    sections.append(f"## Periodo: {discovery.iloc[0].get('Overall Performance', 'N/A')}\n")

    sections.append("## Resumen")
    sections.append(f"- **Impressions totales**: {impressions}")
    sections.append(f"- **Members alcanzados**: {members}")
    sections.append(f"- **Followers totales**: {findings['total_followers']}")
    sections.append(f"- **Followers ganados**: {findings['follower_growth']['total_gained']}")
    sections.append(f"- **Posts analizados**: {len(findings['top_posts'])}\n")

    sections.append("## Recomendaciones\n")
    for i, rec in enumerate(findings["recommendations"], 1):
        sections.append(f"{i}. {rec}")
    sections.append("")

    sections.append("## Engagement por Día de la Semana\n")
    sections.append(df_to_md_table(findings["by_day"]))
    sections.append("")

    sections.append("## Engagement por Mes\n")
    sections.append(df_to_md_table(findings["by_month"]))
    sections.append("")

    sections.append("## Top Temas (por impressions promedio, mínimo 2 posts)\n")
    frequent = findings["topics"][findings["topics"]["post_count"] >= 2] if not findings["topics"].empty else findings["topics"]
    if not frequent.empty:
        sections.append(df_to_md_table(frequent))
    else:
        sections.append("No hay temas con 2+ posts.")
    sections.append("")

    sections.append("## Frecuencia de Posting por Mes\n")
    sections.append(df_to_md_table(findings["frequency"]))
    sections.append("")

    sections.append("## Crecimiento de Followers\n")
    fg = findings["follower_growth"]
    sections.append(f"- Promedio diario: **{fg['avg_daily']}**")
    sections.append(f"- Mejor día: **{fg['best_day_date']}** ({fg['best_day_count']} nuevos)")
    sections.append(f"- Racha más larga sin followers: **{fg['longest_zero_streak']} días**\n")

    sections.append("## Demographics\n")
    for category, df in findings["demographics"].items():
        sections.append(f"### {category}\n")
        sections.append(df_to_md_table(df))
        sections.append("")

    sections.append("## Top 10 Posts para Análisis de Texto con LLM\n")
    sections.append("Pegá el texto de estos posts y pasalos a un LLM para análisis de contenido.\n")
    top10 = findings["top_posts"].head(10)
    for i, (_, post) in enumerate(top10.iterrows(), 1):
        sections.append(f"### Post {i}")
        sections.append(f"- **URL**: {post['post_url']}")
        sections.append(f"- **Fecha**: {post['publish_date'].strftime('%Y-%m-%d')}")
        sections.append(f"- **Impressions**: {post['impressions']}")
        sections.append(f"- **Engagements**: {post['engagements']}")
        sections.append(f"- **Engagement Rate**: {post['engagement_rate']:.4f}")
        sections.append(f"- **Temas**: {post['topics']}")
        sections.append(f"- **Texto del post**:\n")
        sections.append("```\n(pegar texto aquí)\n```\n")

    report_path = output_dir / "linkedin_report.md"
    report_path.write_text("\n".join(sections), encoding="utf-8")
    return report_path
