import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

df = pd.read_csv("data/btc_usd.csv")

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO price_data (ts, price) VALUES (%s, %s)",
        (row['ts'], row['price'])
    )

conn.commit()
cur.close()
conn.close()
print("Data ingested into price_data table.")
