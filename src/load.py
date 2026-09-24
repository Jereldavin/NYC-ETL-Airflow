import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    'postgresql+psycopg2://airflow:airflow@postgres:5432/airflow'
)


def load(processed_path: str):

    df = pd.read_parquet(processed_path)

    df.to_sql(
        "taxi_trip",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )

    print("Load Complete")