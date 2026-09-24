from datetime import datetime

import sys
sys.path.append('/opt/airflow')

from airflow.sdk import dag, task

from src.extract import extract
from src.transform import transform
from src.load import load


RAW_PATH = "/opt/airflow/data/raw/raw.parquet"

PROCESSED_PATH = "/opt/airflow/data/processed/clean.parquet"

SOURCE_PATH = "/opt/airflow/data/raw/nyc.parquet"


@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "taxi"],
)
def taxi_etl():

    @task
    def extract_task():

        return extract(
            SOURCE_PATH,
            RAW_PATH,
        )

    @task
    def transform_task(raw_path):

        return transform(
            raw_path,
            PROCESSED_PATH,
        )

    @task
    def load_task(processed_path):

        load(processed_path)

    raw = extract_task()

    clean = transform_task(raw)

    load_task(clean)


taxi_etl()
