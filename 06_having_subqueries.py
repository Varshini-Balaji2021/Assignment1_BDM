# =====================================================================
# having_subqueries.py
# HAVING and SUBQUERY examples
# =====================================================================

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


# --- 1. HAVING — bakeries donating more than 15 units ---------------

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


# --- 2. HAVING — NGOs receiving more than 10 units ------------------

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


# --- 3. SUBQUERY — bakeries with above-average surplus ---------------

print("\n" + "=" * 70)
print("BAKERIES WITH ABOVE-AVERAGE SURPLUS")
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


# --- clean up --------------------------------------------------------

cursor.close()
connection.close()

print("\nDone — connection closed.")