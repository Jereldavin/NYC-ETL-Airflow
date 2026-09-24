import pandas as pd


def extract(input_path: str, output_path: str):

    df = pd.read_parquet(input_path)

    df.to_parquet(output_path, index=False)

    print("Extract Complete")

    return output_path