import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT ts, signal_type, price FROM signals ORDER BY ts ASC")
signals = cur.fetchall()

balance = 100000  # start capitl
position = 0      # num of units
entry_price = None

for ts, sig, price in signals:
    if sig == "BUY" and balance >= price:
        position += balance / price
        entry_price = price
        balance = 0
        print("{} BUY at {}".format(ts, price))

    elif sig == "SELL" and position > 0:
        # only sell if profitable
        if price > entry_price:
            balance = position * price
            position = 0
            print("{} SELL at {} (PROFIT)".format(ts, price))
        else:
            print("{} SELL signal ignored (not profitable)".format(ts))

# final val if holding
final_value = balance + (position * (signals[-1][2] if position > 0 else 0))
print("Final Portfolio Value: {:.2f}".format(final_value))

cur.close()
conn.close()
