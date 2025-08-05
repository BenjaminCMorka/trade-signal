from src.signal import generate_signals
import psycopg2

def test_signal_generation():
    generate_signals()
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM signals")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    assert count > 0
