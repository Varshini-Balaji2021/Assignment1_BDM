import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to Supabase PostgreSQL
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# ============================================================
# 1. TOTAL DONATIONS BY BAKERY
# ============================================================

print("=" * 70)
print("TOTAL DONATIONS BY BAKERY")
print("=" * 70)

cursor.execute("""
    SELECT
        b."Bakery Name",
        b."City",
        COUNT(d.donation_id) AS total_donations,
        SUM(d.quantity_donated) AS total_food_donated
    FROM bakeries b
    LEFT JOIN donations d
        ON b."Bakery ID" = d.bakery_id
    GROUP BY
        b."Bakery Name",
        b."City"
    ORDER BY total_food_donated DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# 2. TOTAL FOOD RECEIVED BY NGO
# ============================================================

print("\n" + "=" * 70)
print("TOTAL FOOD RECEIVED BY NGO")
print("=" * 70)

cursor.execute("""
    SELECT
        n.ngo_name,
        n.city,
        COUNT(d.donation_id) AS donations_received,
        SUM(d.quantity_donated) AS total_food_received
    FROM ngos n
    LEFT JOIN donations d
        ON n.ngo_id = d.ngo_id
    GROUP BY
        n.ngo_name,
        n.city
    ORDER BY total_food_received DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# 3. DONATION STATUS ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("DONATION STATUS ANALYSIS")
print("=" * 70)

cursor.execute("""
    SELECT
        d.pickup_status,
        COUNT(*) AS number_of_donations,
        SUM(d.quantity_donated) AS total_quantity
    FROM donations d
    GROUP BY d.pickup_status
    ORDER BY number_of_donations DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nDone — connection closed.")