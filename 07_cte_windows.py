# =====================================================================
# cte_window.py
# CTE and Window Function examples
# =====================================================================

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


# --- 1. CTE — total surplus by bakery -------------------------------

print("=" * 70)
print("TOTAL SURPLUS BY BAKERY")
print("=" * 70)

cursor.execute("""
    WITH bakery_surplus AS (
        SELECT
            "Bakery ID",
            SUM("Daily Surplus Quantity") AS total_surplus
        FROM food_waste
        GROUP BY "Bakery ID"
    )
    SELECT
        b."Bakery Name",
        b."City",
        bs.total_surplus
    FROM bakery_surplus bs
    JOIN bakeries b
        ON b."Bakery ID" = bs."Bakery ID"
    ORDER BY bs.total_surplus DESC;
""")

for row in cursor.fetchall():
    print(row)


# --- 2. RANK — bakeries by total surplus ----------------------------

print("\n" + "=" * 70)
print("BAKERIES RANKED BY SURPLUS")
print("=" * 70)

cursor.execute("""
    SELECT
        "Bakery Name",
        "City",
        total_surplus,
        RANK() OVER (
            ORDER BY total_surplus DESC
        ) AS surplus_rank
    FROM (
        SELECT
            b."Bakery Name",
            b."City",
            SUM(f."Daily Surplus Quantity") AS total_surplus
        FROM food_waste f
        JOIN bakeries b
            ON f."Bakery ID" = b."Bakery ID"
        GROUP BY
            b."Bakery Name",
            b."City"
    ) AS bakery_data
    ORDER BY surplus_rank;
""")

for row in cursor.fetchall():
    print(row)


# --- 3. ROW_NUMBER — donations -------------------------------------

print("\n" + "=" * 70)
print("DONATIONS NUMBERED BY QUANTITY")
print("=" * 70)

cursor.execute("""
    SELECT
        donation_id,
        bakery_id,
        ngo_id,
        quantity_donated,
        ROW_NUMBER() OVER (
            ORDER BY quantity_donated DESC
        ) AS donation_rank
    FROM donations
    ORDER BY donation_rank;
""")

for row in cursor.fetchall():
    print(row)


# --- clean up --------------------------------------------------------

cursor.close()
connection.close()

print("\nDone — connection closed.")