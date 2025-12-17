from .extract import extract_csv
from .transform import transform_sales
from .load import load

def run_pipeline():
    raw_df = extract_csv()
    clean_df = transform_sales(raw_df)
    load(clean_df, "sales")

if __name__ == "__main__":
    run_pipeline()
