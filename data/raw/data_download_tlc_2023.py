import os
import requests
import polars as pl

# Create a local directory to save the files
os.makedirs("./raw_parquet_files", exist_ok=True)

months = [f"{i+1:02d}" for i in range(12)]
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-{}.parquet"
all_dfs = []

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

for month in months:
    file_name = f"yellow_tripdata_2023-{month}.parquet"
    local_path = os.path.join("./raw_parquet_files", file_name)
    url = base_url.format(month)

    if not os.path.exists(local_path):
        response = session.get(url, stream=True)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else: continue
    all_dfs.append(pl.read_parquet(local_path))

# Concatenating dataframes
full_2023_df = pl.concat(all_dfs, how="diagonal_relaxed")

sample_df = full_2023_df.sample(fraction=0.05, seed = 42)

sample_df.write_csv("sampled_data.csv")