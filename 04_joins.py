# =====================================================================
# join.py
# Run JOIN queries from Python
# =====================================================================

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


# --- 1. INNER JOIN — donations + bakeries ----------------------------

print("=" * 70)
print("DONATIONS WITH BAKERY DETAILS")
print("=" * 70)

cursor.execute("""
    SELECT
        d.donation_id,
        b."Bakery Name",
        b."City",
        d.quantity_donated,
        d.pickup_status
    FROM donations d
    INNER JOIN bakeries b
        ON b."Bakery ID" = d.bakery_id
    ORDER BY d.quantity_donated DESC
    LIMIT 10;
""")

for row in cursor.fetchall():
    print(row)


# --- 2. LEFT JOIN — bakeries with donations --------------------------

print("\n" + "=" * 70)
print("BAKERIES WITH THEIR DONATIONS")
print("=" * 70)

cursor.execute("""
    SELECT
        b."Bakery Name",
        b."City",
        COUNT(d.donation_id) AS total_donations
    FROM bakeries b
    LEFT JOIN donations d
        ON b."Bakery ID" = d.bakery_id
    GROUP BY
        b."Bakery Name",
        b."City"
    ORDER BY total_donations DESC;
""")

for row in cursor.fetchall():
    print(row)


# --- clean up --------------------------------------------------------

cursor.close()
connection.close()

print("\nDone — connection closed.")