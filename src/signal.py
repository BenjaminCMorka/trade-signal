import pandas as pd
import psycopg2

def generate_signals():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    df = pd.read_sql("SELECT ts, price FROM price_data ORDER BY ts ASC", conn)

    df['SMA_short'] = df['price'].rolling(window=3).mean()
    df['SMA_long'] = df['price'].rolling(window=5).mean()

    prev_signal = None
    last_signal_ts = None
    cur = conn.cursor()

    for i in range(len(df)):
        if pd.notnull(df.loc[i, 'SMA_short']) and pd.notnull(df.loc[i, 'SMA_long']):
            ts = df.loc[i, 'ts']
            price = df.loc[i, 'price']

            # generate BUY
            if df.loc[i, 'SMA_short'] > df.loc[i, 'SMA_long'] and prev_signal != 'BUY':
                if last_signal_ts != ts:  
                    cur.execute(
                        "INSERT INTO signals (ts, signal_type, price) VALUES (%s, %s, %s)",
                        (ts, 'BUY', price)
                    )
                    prev_signal = 'BUY'
                    last_signal_ts = ts

            # generate SELL
            elif df.loc[i, 'SMA_short'] < df.loc[i, 'SMA_long'] and prev_signal != 'SELL':
                if last_signal_ts != ts:  
                    cur.execute(
                        "INSERT INTO signals (ts, signal_type, price) VALUES (%s, %s, %s)",
                        (ts, 'SELL', price)
                    )
                    prev_signal = 'SELL'
                    last_signal_ts = ts

    conn.commit()
    cur.close()
    conn.close()
    print("Signals generated and stored.")

if __name__ == "__main__":
    generate_signals()
