import pandas as pd
from faker import Faker
import random

# Initialize Faker (used to generate fake but realistic data)
fake = Faker()

def generate_sales_data(num_records: int = 100):
    """
    Simulates batch export from a sales system
    """
    data = []

    for _ in range(num_records):
        record = {
            "order_id": random.randint(100000, 999999),
            "customer": fake.name(),
            "product": random.choice([
                "MacBook Air", "iPhone 15", "iPad Pro",
                "Apple Watch", "AirPods Pro"
            ]),
            "quantity": random.randint(1, 3),
            "price": round(random.uniform(99.99, 1999.99), 2),
            "order_date": fake.date_between(start_date="-30d", end_date="today")
        }
        data.append(record)

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sales_data(50)
    df.to_csv("data/sales.csv", index=False)
    print("sales.csv generated successfully")
