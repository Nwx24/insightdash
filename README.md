# InsightDash

InsightDash is a Python + Streamlit CSV dashboard. Upload a CSV (or use sample data), apply smart filters, visualize filtered results, and export both the filtered data and a generated report.

## Features
- Upload any CSV (or use the included sample dataset)
- Smart filtering
  - Numeric columns -> range slider
  - Text/categorical columns -> multi-select
- Filtered preview with row counts
- Charting on filtered data
- Export
  - Download filtered CSV
  - Download Markdown report (summary stats + missing values)
- Automated tests for core logic (filtering + reporting)

## Tech Stack
- Python
- Streamlit
- pandas
- matplotlib
- tabulate
- pytest

## Project Structure
```text
insightdash/
  app.py
  requirements.txt
  README.md
  data/
    sample.csv
  src/
    __init__.py
    filtering.py
    reporting.py
  tests/
    test_filtering.py
    test_reporting.py
```

## Run Locally (Windows)
```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## How to Use
1. Open the app in your browser (Streamlit launches it automatically)
2. Upload a CSV from the sidebar (or use the sample dataset)
3. Choose a column to filter and apply filters
4. View the filtered table + chart
5. Download `filtered.csv` and/or `report.md`

## Run Tests
```bat
pytest
```

## What I Learned
- Building a data dashboard with Streamlit (UI + reruns)
- Using pandas to filter datasets and generate summary statistics
- Debugging common issues (paths, column names, data types)
- Writing testable code by separating logic from UI
- Using pytest to validate filtering/report generation behavior

## Future Improvements
- Multiple filters at once (filter by more than one column)
- Data cleaning controls (type conversion, handling bad numeric values)
- Export HTML/PDF reports
- More chart types and better aggregations (group-by summaries)
