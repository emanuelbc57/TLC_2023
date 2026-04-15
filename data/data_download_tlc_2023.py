import os
import requests
import polars as pl

# Create a local directory to save the files
os.makedirs("tlc_data_2023", exist_ok=True)

months = [f"{i:02d}" for i in range(1, 13)]
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-{}.parquet"
all_dfs = []

# Using a session with a User-Agent often bypasses 403 errors
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

for month in months:
    file_name = f"yellow_tripdata_2023-{month}.parquet"
    local_path = os.path.join("tlc_data_2023", file_name)
    url = base_url.format(month)

    # 1. Download if the file doesn't exist locally
    if not os.path.exists(local_path):
        print(f"Downloading month {month}...")
        response = session.get(url, stream=True)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            print(f"❌ Failed to download month {month}. Status: {response.status_code}")
            continue

    # 2. Load from local path
    print(f"✅ Loading month {month}...")
    all_dfs.append(pl.read_parquet(local_path))

# 3. Concatenate
if all_dfs:
    full_2023_df = pl.concat(all_dfs, how="diagonal_relaxed")
    print(f"\nSuccess! Total rows: {len(full_2023_df):,}")
else:
    print("\nNo data was loaded. Check your internet connection or URL.")


sample_df = full_2023_df.sample(fraction=0.01, seed = 42)

sample_df.write_csv("sampled_data.csv")