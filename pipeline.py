import sys
import os

# Ensure the src folder is in the Python search path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(project_root, 'src'))

from extract import extract
from transform import transform
from load import load

# Define data paths
raw_path = os.path.join(project_root, 'data', 'raw', 'nyc.parquet')
staging_dir = os.path.join(project_root, 'data', 'staging')
os.makedirs(staging_dir, exist_ok=True)

extracted_path = os.path.join(staging_dir, 'extracted.parquet')
transformed_path = os.path.join(staging_dir, 'clean.parquet')

print("Starting local pipeline run...")

# 1. Extract
extract(raw_path, extracted_path)

# 2. Transform
transform(extracted_path, transformed_path)

# 3. Load
load(transformed_path)

print("Local pipeline execution completed successfully!")