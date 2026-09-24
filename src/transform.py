import pandas as pd


def transform(input_path: str, output_path: str):

    df = pd.read_parquet(input_path)

    df = df.drop_duplicates()

    df = df.dropna()

    df["tpep_pickup_datetime"] = pd.to_datetime(
        df["tpep_pickup_datetime"]
    )

    df["tpep_dropoff_datetime"] = pd.to_datetime(
        df["tpep_dropoff_datetime"]
    )

    df = df[df["trip_distance"] > 0]

    df = df[df["fare_amount"] > 0]

    df["trip_duration"] = (
        df["tpep_dropoff_datetime"]
        - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    df["pickup_year"] = df["tpep_pickup_datetime"].dt.year
    df["pickup_month"] = df["tpep_pickup_datetime"].dt.month
    df["pickup_day"] = df["tpep_pickup_datetime"].dt.day
    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour

    df.to_parquet(output_path, index=False)

    print("Transform Complete")

    return output_path