#file reading,input validation, schema checks
import os
import pandas as pd
from .config import CSV_PATH

REQUIRED_COLUMNS = {
    "order_id",
    "customer",
    "product",
    "quantity",
    "price",
    "order_date"
}

def extract_csv():
    """
    Extracts and validates CSV input from upstream batch export.
    """

    ##file existence check
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV not found at {CSV_PATH}")

    ##file size check
    if os.path.getsize(CSV_PATH) == 0:
        raise ValueError("CSV file is empty")

    ##read csv
    df = pd.read_csv(CSV_PATH)

    #row check
    if df.empty:
        raise ValueError("CSV contains no rows")
    
    ##schema validation
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df

if __name__ == "__main__":
    df = extract_csv()
    print(df.head())

