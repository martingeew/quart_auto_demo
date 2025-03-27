import ffn
from datetime import datetime

# Step 1: Retrieve data using ffn
data = ffn.get("nvda,msft,googl,amzn,aapl,meta", start="2023-01-01")

# Step 2: Rebase data
data_rebase = data.rebase()

# Step 3: Save pandas dataframe as csv and the plot as a PNG
timestamp = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"stock_data_{timestamp}.csv"
data_rebase.to_csv(f"data/stock_data_{timestamp}.csv")

print(f"Data saved to {csv_filename}")
