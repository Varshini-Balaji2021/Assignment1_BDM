import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

print("Connected to database successfully!")
print("=" * 70)
print("TABLE: food_waste")
print("=" * 70)

# Total Row Count
cursor.execute('SELECT COUNT(*) FROM food_waste;')
row_count = cursor.fetchone()[0]
print(f"Total Rows: {row_count}\n")

# Column Names and Data Types
cursor.execute("""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = 'public' AND table_name = 'food_waste'
    ORDER BY ordinal_position;
""")
print("Columns in food_waste:")
for col_name, data_type in cursor.fetchall():
    print(f" - {col_name} ({data_type})")

# First 5 Sample Rows
cursor.execute('SELECT * FROM food_waste LIMIT 5;')
sample_rows = cursor.fetchall()

print("\nFirst 5 Rows:")
for row in sample_rows:
    print(row)

cursor.close()
connection.close()

print("\n" + "=" * 70)
print("Database connection closed. Table exploration complete.")
print("=" * 70)