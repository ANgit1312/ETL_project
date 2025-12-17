from sqlalchemy import create_engine
import pandas as pd
from .config import DB_URI

engine = create_engine(DB_URI)

def load(df: pd.DataFrame, table_name: str):
    """
    Loads cleaned data into PostgreSQL.
    """
    if df.empty:
        raise ValueError("Attempted to load empty DataFrame")

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )
