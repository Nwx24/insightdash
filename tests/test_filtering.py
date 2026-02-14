import pandas as pd
from src.filtering import is_numeric_series, filter_numeric_range, filter_by_values

def test_is_numeric_series_true():
    s = pd.Series([1, 2, 3, None])
    assert is_numeric_series(s) is True

def test_is_numeric_series_false():
    s = pd.Series(["a", "b", None])
    assert is_numeric_series(s) is False

def test_filter_numeric_range():
    df = pd.DataFrame({"amount": [10, 20, 30]})
    out = filter_numeric_range(df, "amount", 15, 30)
    assert out["amount"].tolist() == [20, 30]

def test_filter_by_values():
    df = pd.DataFrame({"dept": ["IT", "Sales", "IT"]})
    out = filter_by_values(df, "dept", ["IT"])
    assert out["dept"].tolist() == ["IT", "IT"]

def test_filter_by_values_empty_selection():
    df = pd.DataFrame({"dept": ["IT", "Sales"]})
    out = filter_by_values(df, "debt", [])
    assert len(out) == 0