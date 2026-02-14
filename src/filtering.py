import pandas as pd

def is_numeric_series(s: pd.Series) -> bool:
    """True if series is numeric dtype after dropping missing values."""
    s2 = s.dropna()
    if s2.empty:
        return False
    return pd.api.types.is_numeric_dtype(s2)

def filter_numeric_range(df: pd.DataFrame, col:  str, low: float, high: float) -> pd.DataFrame:
    """Keep rows where df[col] is between low and high inclusive."""
    return df[(df[col] >= low) & (df[col] <= high)]

def filter_by_values(df: pd.DataFrame, col: str, selected_vals: list[str]) -> pd.DataFrame:
    """Keep rows where df[col] (as string) is in selected_vals."""
    if not selected_vals:
        return df.iloc[0:0] # empty but keep columns
    return df[df[col].astype(str).isin(selected_vals)]