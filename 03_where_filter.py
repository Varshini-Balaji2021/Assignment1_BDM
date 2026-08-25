import os
import psycopg2
from dotenv import load_dotenv

# Load database credentials
load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

print("Connected to database successfully!")
print("=" * 70)
print("WHERE FILTERS ON food_waste")
print("=" * 70)

# Filter 1: Exact string match on Food Category
print("\n1. Filter: Food Category = 'Bread'")
cursor.execute("""
    SELECT "Bakery Name", "Product Name", "Food Category", "Daily Surplus Quantity"
    FROM food_waste
    WHERE "Food Category" = 'Bread'
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Filter 2: Numeric comparison (> threshold)
print("\n2. Filter: Average Daily Waste > 10")
cursor.execute("""
    SELECT "Bakery Name", "Product Name", "Average Daily Waste"
    FROM food_waste
    WHERE "Average Daily Waste" > 10
    ORDER BY "Average Daily Waste" DESC
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Filter 3: Multiple conditions using AND & OR
print("\n3. Filter: Surplus Quantity > 50 AND Price < 50")
cursor.execute("""
    SELECT "Product Name", "Food Category", "Daily Surplus Quantity", "Original Price"
    FROM food_waste
    WHERE "Daily Surplus Quantity" > 50 AND "Original Price" < 50
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(f"  {row}")

# Close connection
cursor.close()
connection.close()

print("\n" + "=" * 70)
print("Database connection closed. WHERE filters completed.")
print("=" * 70)