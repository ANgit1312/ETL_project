from sqlalchemy import create_engine
import pandas as pd
from .config import DB_URI

def load_to_db(df: pd.DataFrame, table_name: str):
    """
    Loads DataFrame into PostgreSQL table.
    If table exists, appends data.
    """
    if df.empty:
        print(f"⚠️ Skipping load: {table_name} is empty.")
        return

    try:
        engine = create_engine(DB_URI)
        with engine.begin() as conn:  # ensures transactions
            df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"✅ Loaded {len(df)} rows into '{table_name}'")
    except Exception as e:
        raise RuntimeError(f"DB load failed for {table_name}: {e}")
