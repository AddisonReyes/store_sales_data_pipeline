import random
from typing import Dict, List

import pandas as pd
from faker import Faker

fake = Faker("en_US")

products: List[str] = ["Laptop", "Mouse", "Keyboard", "Screen", "Webcam"]
regions: List[str] = ["North", "South", "East", "West"]


def generate_data(
    n: int = 1000, filename: str = "sales_raw.csv", idx: bool = False
) -> None:
    sales: List[Dict] = []
    for i in range(n):
        date = fake.date_time_between(start_date="-90d", end_date="now")
        sale: dict = {
            "sale_id": i + 1,
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "client_id": random.randint(1, 200),
            "product": random.choice(products),
            "quantity": random.randint(1, 6),
            "unit_price": round(random.uniform(10, 1600), 2),
            "region": random.choice(regions),
        }

        sales.append(sale)
    df = pd.DataFrame(sales)
    df.to_csv(filename, index=idx)
    print("Data generated successfully: " + filename)


if __name__ == "__main__":
    generate_data()
