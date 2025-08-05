import pandas as pd
import numpy as np

def generate_price_data(start_price=29000, minutes=1000, seed=42, output_file="btc_usd.csv"):
    np.random.seed(seed)
    dates = pd.date_range("2025-08-01 00:00:00", periods=minutes, freq="T")

   
    price_changes = np.random.normal(loc=0.1, scale=5, size=minutes)
    prices = start_price + np.cumsum(price_changes)

    df = pd.DataFrame({"ts": dates, "price": prices.round(2)})
    df.to_csv(output_file, index=False)
    print(f"saved {output_file} with {len(df)} rows")

if __name__ == "__main__":
    generate_price_data()
