import pandas as pd
from src.reporting import build_markdown_report

def test_report_contains_key_sections():
    df = pd.DataFrame({"amount": [10, 20], "dept": ["IT", "Sales"]})
    filtered = df[df["dept"] == "IT"]

    report = build_markdown_report(df, filtered, "dept")

    assert "# InsightDash Report" in report
    assert "Filter column: dept" in report
    assert "Rows shown: 1 of 2" in report
    assert "## Missing Values (filtered)" in report