# InsightDash 🕸️

InsightDash is a Python + Streamlit CSV dashboard. Upload a CSV (or use sample data), apply smart filters, visualize results, and export both the filtered data and a generated report.

## What it does
- Loads a CSV (upload or included sample)
- Smart filtering:
  - Numeric columns → range slider
  - Text/categorical columns → multi-select
- Shows filtered preview + row counts
- Charts filtered data
- Exports:
  - Filtered CSV download
  - Markdown report download (summary stats + missing values)

## Tech
- Python
- Streamlit
- pandas
- matplotlib
- tabulate

## Run locally (Windows)
```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

How to use

1. Upload a CSV from the sidebar (or use the sample dataset)

2. Choose a column to filter and apply filters

3. View the filtered table + chart

4. Download filtered.csv and report.md