import polars as pl
from sodapy import Socrata

# --- YOUR CREDENTIALS ---
DOMAIN = "data.cityofnewyork.us"
DATASET_ID = "4b4i-vvec"
APP_TOKEN = "your_app_token"
KEY_ID = "your_key_id"         # This is the "Key ID"
KEY_SECRET = "your_key_secret" # This is the "Key Secret"

# Initialize the client
# username = Key ID, password = Key Secret
client = Socrata(
    DOMAIN, 
    APP_TOKEN, 
    username=KEY_ID, 
    password=KEY_SECRET,
    timeout = 600
)

count_res = client.get(DATASET_ID, select = "COUNT(*)")
total_rows = int(count_res[0]['COUNT'])

CHUNK_SIZE = 50000 
SAMPLE_RATE = 0.05

samples = []

for offset in range(0, total_rows, CHUNK_SIZE):
    # Fetch chunk
    results = client.get(DATASET_ID, limit=CHUNK_SIZE, offset=offset)
    
    # Convert list of dicts to Polars DataFrame
    chunk_pl = pl.DataFrame(results)
    
    # Perform 5% sampling on this chunk
    sampled_chunk = chunk_pl.sample(fraction=SAMPLE_RATE, seed=42)
    
    # Store the sample
    samples.append(sampled_chunk)
    print(f"Collected sample from offset {offset}")

# 4. Vertically stack (concat) all sampled chunks
final_df = pl.concat(samples, how = 'diagonal_relaxed')

print(f"\nSampling Finished.")
print(f"Final sampled rows: {final_df.height}")
print(final_df.head())

client.close()

final_df.write_csv("sampled_data.csv")

