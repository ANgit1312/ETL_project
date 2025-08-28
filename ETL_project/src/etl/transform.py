import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans dataframe: removes nulls, enforces correct data types.
    """
    if df.empty:
        return df

    df = df.dropna()

    # Convert 'price' to float if present
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0)

    # Standardize column names to lowercase
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df
