from .ingest import ingest_csv, ingest_api, ingest_stream
from .transform import clean_data
from .load import load_to_db

def run_pipeline():
    """
    End-to-end ETL pipeline: Ingest → Transform → Load
    """
    print(" Starting ETL pipeline...")

    # Step 1: Ingest
    csv_data = ingest_csv()
    api_data = ingest_api()
    stream_data = ingest_stream(10)

    # Step 2: Transform
    csv_data = clean_data(csv_data)
    api_data = clean_data(api_data)
    stream_data = clean_data(stream_data)

    # Step 3: Load
    load_to_db(csv_data, "csv_sales")
    load_to_db(api_data, "api_products")
    load_to_db(stream_data, "stream_sales")

    print(" ETL pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()
