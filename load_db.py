import pandas as pd
from sqlalchemy import create_engine


def load_database(
    filename: str = "transformed_sales.csv",
    database: str = "sales.db",
    table: str = "sales",
    idx: bool = False,
) -> None:
    df = pd.read_csv(filename)

    engine = create_engine("sqlite:///" + database)

    df.to_sql(table, engine, if_exists="replace", index=idx)
    print("Data uploaded to the database: " + database)


if __name__ == "__main__":
    load_database()
