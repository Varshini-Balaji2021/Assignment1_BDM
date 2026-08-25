import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


# ============================================================
# 1. HAVING — BAKERIES DONATING MORE THAN 15 UNITS
# ============================================================

print("=" * 70)
print("BAKERIES DONATING MORE THAN 15 UNITS")
print("=" * 70)

cursor.execute("""
    SELECT
        b."Bakery Name",
        b."City",
        SUM(d.quantity_donated) AS total_donated
    FROM bakeries b
    JOIN donations d
        ON b."Bakery ID" = d.bakery_id
    GROUP BY
        b."Bakery Name",
        b."City"
    HAVING SUM(d.quantity_donated) > 15
    ORDER BY total_donated DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# 2. HAVING — NGOs RECEIVING MORE THAN 10 UNITS
# ============================================================

print("\n" + "=" * 70)
print("NGOs RECEIVING MORE THAN 10 UNITS")
print("=" * 70)

cursor.execute("""
    SELECT
        n.ngo_name,
        n.city,
        SUM(d.quantity_donated) AS total_received
    FROM ngos n
    JOIN donations d
        ON n.ngo_id = d.ngo_id
    GROUP BY
        n.ngo_name,
        n.city
    HAVING SUM(d.quantity_donated) > 10
    ORDER BY total_received DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# 3. SUBQUERY — BAKERIES ABOVE AVERAGE SURPLUS
# ============================================================

print("\n" + "=" * 70)
print("BAKERIES WITH ABOVE-AVERAGE DAILY SURPLUS")
print("=" * 70)

cursor.execute("""
    SELECT
        b."Bakery Name",
        b."City",
        f."Daily Surplus Quantity"
    FROM food_waste f
    JOIN bakeries b
        ON f."Bakery ID" = b."Bakery ID"
    WHERE f."Daily Surplus Quantity" >
          (
              SELECT AVG("Daily Surplus Quantity")
              FROM food_waste
          )
    ORDER BY f."Daily Surplus Quantity" DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nDone — connection closed.")