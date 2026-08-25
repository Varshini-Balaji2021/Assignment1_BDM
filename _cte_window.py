import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


# ============================================================
# 1. CTE — TOTAL SURPLUS BY BAKERY
# ============================================================

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


# ============================================================
# 2. CTE + HAVING — HIGH SURPLUS BAKERIES
# ============================================================

print("\n" + "=" * 70)
print("HIGH SURPLUS BAKERIES")
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
    WHERE bs.total_surplus > 30
    ORDER BY bs.total_surplus DESC;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# 3. RANK — RANK BAKERIES BY SURPLUS
# ============================================================

print("\n" + "=" * 70)
print("BAKERIES RANKED BY TOTAL SURPLUS")
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


# ============================================================
# 4. RANK — TOP BAKERIES WITHIN EACH CITY
# ============================================================

print("\n" + "=" * 70)
print("BAKERIES RANKED WITHIN EACH CITY")
print("=" * 70)

cursor.execute("""
    SELECT
        "Bakery Name",
        "City",
        total_surplus,
        RANK() OVER (
            PARTITION BY "City"
            ORDER BY total_surplus DESC
        ) AS city_rank
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
    ORDER BY
        "City",
        city_rank;
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nDone — connection closed.")