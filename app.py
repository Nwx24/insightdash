import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
from src.filtering import is_numeric_series, filter_numeric_range, filter_by_values
from src.reporting import build_markdown_report

st.set_page_config(page_title="InsightDash", layout="wide", page_icon="🕸️")
st.title("InsightDash")

SAMPLE_PATH = Path("data/sample.csv")

st.sidebar.header("Data Source")

uploaded = st.sidebar.file_uploader("Upload a CSV", type=["csv"])

@st.cache_data
def load_csv(file) -> pd.DataFrame:
    """Load CSV into a DataFrame. Cached so it doesn't re-read on ever rereun."""
    return pd.read_csv(file)

if uploaded is not None:
    df = load_csv(uploaded)
    st.success(f"Loaded uploaded file: {uploaded.name}")

else:
    df = load_csv(SAMPLE_PATH)
    st.info("Using sample.csv (upload a CSV in the sidebar to replace it)")

filtered_df = df.copy()

# Optional: normalize headers for messy CSVs
# df.columns = df.columns.str.strip().str.lower()

st.subheader("Data")

with st.expander("Data preview (click to expand)", expanded=False):
    st.dataframe(df, width="stretch")

st.subheader("Filter")

filter_col = st.selectbox("Choose a column", df.columns)

col = df[filter_col]
col_no_na = col.dropna()

if is_numeric_series(col):
    min_val = float(col_no_na.min())
    max_val = float(col_no_na.max())

    low, high = st.slider(
        f"Select range for {filter_col}",
        min_value=min_val,
        max_value=max_val,
        value=(min_val, max_val)
    )

    filtered_df = filter_numeric_range(df, filter_col, low, high)
else:
    unique_vals = sorted(col_no_na.astype(str).unique().tolist())

    selected_vals = st.multiselect(
        f"Select values for {filter_col}",
        options=unique_vals,
        default=unique_vals
    )

    if selected_vals:
        filtered_df = filter_by_values(df, filter_col, selected_vals)
    else:
        filtered_df = df.iloc[0:0]  # empty (0 rows)

st.subheader("Filtered preview")
st.caption(f"Showing {len(filtered_df)} of {len(df)} rows")
st.dataframe(filtered_df, width="stretch")

st.subheader("Export")
csv_bytes = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered CSV",
    data=csv_bytes,
    file_name="filtered.csv",
    mime="text/csv"
)

st.subheader("Chart (filtered data)")

# Find numeric columns in the filtered data
numeric_cols = [
    c for c in filtered_df.columns
    if pd.api.types.is_numeric_dtype(filtered_df[c])
]

if numeric_cols:
    chart_col = st.selectbox("Choose a numeric column to chart", numeric_cols)

    st.write(f"Charting: {chart_col}")
    group_by_canidates = [
        c for c in filtered_df.columns
        if not pd.api.types.is_numeric_dtype(filtered_df[c])
    ]

    group_col = st.selectbox("Group by (optional)", ["(no grouping)"] + group_by_canidates)

    if group_col == "(no grouping)":
        st.bar_chart(filtered_df[chart_col])
    else:
        grouped = (
            filtered_df.groupby(group_col)[chart_col]
            .sum()
            .sort_values(ascending=False)
        )
        st.bar_chart(grouped)

st.subheader("Report")

report_md = build_markdown_report(df, filtered_df, filter_col)

st.download_button(
    label = "Download report (Markdown)",
    data=report_md.encode("utf-8"),
    file_name="report.md",
    mime="text/markdown"
)

with st.expander("Preview report"):
    st.markdown(report_md)