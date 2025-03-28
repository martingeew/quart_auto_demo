import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
from datetime import datetime
from dotenv import load_dotenv
import os
import seaborn as sns
import plotly.express as px

# Set pandas parameters
pd.set_option("display.max_colwidth", 1000)

# Load environment variables from .env file
load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")
if FRED_API_KEY is None:
    raise ValueError("FRED_API_KEY environment variable not set")


# Search for state indicators
fred = Fred(api_key=FRED_API_KEY)
results = fred.search("GDPNOW", limit=10, order_by="popularity", sort_order="desc")

# Retrieve data
data = fred.get_series("GDPNOW", observation_start="2010-01-01")



df = data.to_frame(name="Ggdpnow")
# Save raw data as csv
timestamp = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"gdpnow_data_{timestamp}.csv"
df.to_csv(f"data/raw/gdpnow_data_{timestamp}.csv")
print(f"Raw data saved to {csv_filename}")

# Create the Plotly figure
fig = px.line(
    df,
    x=df.index,
    y=df.columns[0],
    title="US GDP Nowcast (Seasonally Adjusted Annual Rate)",
    labels={"index": "Date", "y": "Value"},
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="",
    yaxis_title="",
    template="plotly_dark",
    width=700,
    height=400,
    plot_bgcolor="#282a36",
    paper_bgcolor="#282a36",
),

fig.update_traces(line=dict(width=3.5))

fig.show()

# Create a seaborn time series plot with a white grid theme using an ax object
sns.set_theme(style="whitegrid")  # White grid background
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df, x=df.index, y="Ggdpnow", linewidth=2.5, color="blue", ax=ax)

# Customize the plot
ax.set_title("US GDP Nowcast (Seasonally Adjusted Annual Rate)", fontsize=16)
ax.set_xlabel("", fontsize=12)
ax.set_ylabel("", fontsize=12)
ax.grid(visible=True, linestyle="--", alpha=0.6)
ax.spines["left"].set_color("none")
ax.spines["bottom"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
# Add a horizontal line at y=0
ax.axhline(0, color="gray", linestyle="--", linewidth=1.5, alpha=0.8)

# Show the plot
plt.tight_layout()
plt.show()
