import pandas as pd

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and standardizes sales data.
    Applies only data-quality transformations.
    """

    ## Normalizing column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    ##  Removing duplicate rows
    df = df.drop_duplicates()

    ##  Enforcing data types
    df["order_id"] = df["order_id"].astype(int)
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    ##  Removing rows with invalid critical values
    df = df.dropna(subset=["order_id", "product", "price", "order_date"])
    df = df[df["price"] >= 0]
    df = df[df["quantity"] > 0]

    ## Adding technical metadata (allowed)
    df["ingestion_timestamp"] = pd.Timestamp.utcnow()

    return df
