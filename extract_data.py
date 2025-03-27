import ffn
from datetime import datetime

# Step 1: Retrieve data using ffn
data = ffn.get("nvda,msft,googl,amzn,aapl,meta", start="2023-01-01")

# Step 2: Rebase data
data_rebase = data.rebase()

# Step 3: Save raw data as csv
timestamp = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"stock_data_{timestamp}.csv"
data.to_csv(f"data/raw/stock_data_{timestamp}.csv")

print(f"Raw data saved to {csv_filename}")

# Step 4: Save processed data as csv
timestamp = datetime.now().strftime("%Y-%m-%d")
processed_csv_filename = f"stock_data_{timestamp}.csv"
data_rebase.to_csv(f"data/processed/stock_data_rebased_{timestamp}.csv")

print(f"Processed data saved to {processed_csv_filename}")
