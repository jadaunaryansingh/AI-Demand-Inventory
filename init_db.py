import pandas as pd
import sqlite3

df = pd.read_csv('data/sales.csv')

conn = sqlite3.connect('forecast.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        store INTEGER NOT NULL,
        dept INTEGER NOT NULL,
        date TEXT NOT NULL,
        weekly_sales REAL NOT NULL,
        isholiday INTEGER NOT NULL
    )
""")

if 'isholiday' in df.columns:
    df['isholiday'] = df['isholiday'].astype(int)
df.to_sql('sales', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Database initialized successfully!")
print(f"Loaded {len(df)} records into sales table")
