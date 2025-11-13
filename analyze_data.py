import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine


def analyze_data(
    filename: str = "sales_region.png", database: str = "sales.db"
) -> None:
    engine = create_engine("sqlite:///" + database)

    # Sales by region
    query1 = """
    SELECT region,
        SUM(total_sales) as total_sales,
        COUNT(*) as sales_num
    FROM sales
    GROUP BY region
    ORDER BY total_sales DESC
    """
    sales_by_region = pd.read_sql(query1, engine)
    print("Sales by region:")
    print(sales_by_region)

    # Top products
    query2 = """
    SELECT product,
        SUM(quantity) as units_sold,
        SUM(total_sales) as income
    FROM sales
    GROUP BY product
    ORDER BY income DESC
    """
    top_products = pd.read_sql(query2, engine)
    print("\nTop products:")
    print(top_products)

    plt.figure(figsize=(10, 6))
    plt.bar(sales_by_region["region"], sales_by_region["total_sales"])
    plt.title("Total sales by region")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    print("\nChart saved: " + filename)


if __name__ == "__main__":
    analyze_data()
