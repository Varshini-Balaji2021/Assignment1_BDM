import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

print("Connected to database successfully!")
print("=" * 70)
print("AGGREGATE FUNCTIONS ON food_waste")
print("=" * 70)

# Total records
cursor.execute('SELECT COUNT(*) FROM food_waste;')
print(f"Total Records: {cursor.fetchone()[0]}")

# Total Surplus Quantity
cursor.execute('SELECT SUM("Daily Surplus Quantity") FROM food_waste;')
print(f"Total Daily Surplus Quantity: {cursor.fetchone()[0]}")

# Average Daily Waste
cursor.execute('SELECT ROUND(AVG("Average Daily Waste"), 2) FROM food_waste;')
print(f"Average Daily Waste: {cursor.fetchone()[0]}")

# Min & Max Price
cursor.execute('SELECT MIN("Original Price"), MAX("Original Price") FROM food_waste;')
min_p, max_p = cursor.fetchone()
print(f"Minimum Price: {min_p} | Maximum Price: {max_p}")

cursor.close()
connection.close()

print("\n" + "=" * 70)
print("Database connection closed. Aggregates completed.")
print("=" * 70)