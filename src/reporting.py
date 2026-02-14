from datetime import datetime
import pandas as pd

def build_markdown_report(df: pd.DataFrame, filtered_df: pd.DataFrame, filter_col: str) -> str:
    """Return a Markdown report for the filtered dataset."""
    lines: list[str] = []

    lines.append("# InsightDash Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Filter column: {filter_col}")
    lines.append(f"Rows shown: {len(filtered_df)} of {len(df)}")
    lines.append("")

    numeric_cols = [
        c for c in filtered_df.columns
        if pd.api.types.is_numeric_dtype(filtered_df[c])
    ]

    lines.append("## Numeric Summary (filtered)")
    lines.append("")
    if numeric_cols:
        summary = filtered_df[numeric_cols].describe().T
        lines.append(summary.to_markdown())
    else:
        lines.append("_No numeric columns availavle._")
    lines.append("")

    lines.append("## Missing Values (filtered)")
    lines.append("")
    missing = filtered_df.isna().sum().to_frame("missing_count")
    lines.append(missing.to_markdown())
    lines.append("")

    return "\n".join(lines)