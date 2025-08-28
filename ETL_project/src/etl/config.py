import os
from dotenv import load_dotenv

# Load environment variables (if .env file exists)
load_dotenv()

DB_URI = os.getenv("DB_URI", "postgresql://etl_user:etl_pass@localhost:5432/etl_db")

# Data sources
CSV_PATH = os.getenv("CSV_PATH", "data/sales.csv")
API_URL = os.getenv("API_URL", "https://fakestoreapi.com/products")
