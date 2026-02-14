import streamlit as st
import pandas as pd
from pathlib import Path

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

st.subheader("Data preview")
st.dataframe(df, width="stretch")

st.subheader("Filter")

filter_col = st.selectbox("Choose a column", df.columns)

col = df[filter_col]
col_no_na = col.dropna()

if pd.api.types.is_numeric_dtype(col_no_na):
    min_val = float(col_no_na.min())
    max_val = float(col_no_na.max())

    low, high = st.slider(
        f"Select range for {filter_col}",
        min_value=min_val,
        max_value=max_val,
        value=(min_val, max_val)
    )

    filtered_df = df[(df[filter_col] >= low) & (df[filter_col] <= high)]
else:
    unique_vals = sorted(col_no_na.astype(str).unique().tolist())

    selected_vals = st.multiselect(
        f"Select values for {filter_col}",
        options=unique_vals,
        default=unique_vals
    )

    if selected_vals:
        filtered_df = df[df[filter_col].astype(str).isin(selected_vals)]
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
