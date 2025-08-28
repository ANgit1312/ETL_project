import pandas as pd
import requests
from faker import Faker
from .config import CSV_PATH, API_URL

fake = Faker()

def ingest_csv(path: str = CSV_PATH) -> pd.DataFrame:
    """
    Reads sales data from CSV file.
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise RuntimeError(f"CSV ingestion failed: {e}")

def ingest_api(url: str = API_URL) -> pd.DataFrame:
    """
    Fetches product data from REST API.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return pd.DataFrame(resp.json())
    except Exception as e:
        raise RuntimeError(f"API ingestion failed: {e}")

def ingest_stream(n: int = 10) -> pd.DataFrame:
    """
    Simulates streaming sales transactions.
    """
    try:
        data = [
            {"customer": fake.name(), "amount": fake.random_int(100, 1000)}
            for _ in range(n)
        ]
        return pd.DataFrame(data)
    except Exception as e:
        raise RuntimeError(f"Stream ingestion failed: {e}")
