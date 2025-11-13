import pandas as pd


def categorize_sale(sale_price: int) -> str:
    if sale_price < 100:
        return "Small"
    elif sale_price < 500:
        return "Medium"
    else:
        return "Big"


def transform_data(
    raw_df: str = "sales_raw.csv",
    transformed_df: str = "transformed_sales.csv",
    idx: bool = False,
) -> None:
    df = pd.read_csv(raw_df)

    df["total_sales"] = df["quantity"] * df["unit_price"]

    df["date"] = pd.to_datetime(df["date"])

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day_name()

    df["sales_category"] = df["total_sales"].apply(categorize_sale)
    df = df.drop_duplicates()

    print(f"Transformations completed: {raw_df} -> {transformed_df}")
    print(df.head())

    df.to_csv(transformed_df, index=idx)


if __name__ == "__main__":
    transform_data()
