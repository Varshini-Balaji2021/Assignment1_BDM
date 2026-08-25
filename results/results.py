import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

# ============================================================
# DATABASE CONNECTION
# ============================================================

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)

print("Database connected successfully!")


# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

os.makedirs("results/sql_results", exist_ok=True)


# ============================================================
# 1. DONATIONS BY BAKERY
# ============================================================

query = """
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
"""

df_bakery = pd.read_sql(query, connection)

df_bakery.to_csv(
    "results/sql_results/donations_by_bakery.csv",
    index=False
)

print("Saved: donations_by_bakery.csv")


# ============================================================
# 2. FOOD RECEIVED BY NGO
# ============================================================

query = """
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
"""

df_ngo = pd.read_sql(query, connection)

df_ngo.to_csv(
    "results/sql_results/food_received_by_ngo.csv",
    index=False
)

print("Saved: food_received_by_ngo.csv")


# ============================================================
# 3. DONATION STATUS
# ============================================================

query = """
SELECT
    pickup_status,
    COUNT(*) AS number_of_donations,
    SUM(quantity_donated) AS total_quantity
FROM donations
GROUP BY pickup_status
ORDER BY number_of_donations DESC;
"""

df_status = pd.read_sql(query, connection)

df_status.to_csv(
    "results/sql_results/donation_status.csv",
    index=False
)

print("Saved: donation_status.csv")


# ============================================================
# 4. HIGH SURPLUS BAKERIES
# ============================================================

query = """
SELECT
    b."Bakery Name",
    b."City",
    SUM(f."Daily Surplus Quantity") AS total_surplus,
    ROUND(AVG(f."Average Daily Waste"), 2) AS average_waste
FROM food_waste f
JOIN bakeries b
    ON f."Bakery ID" = b."Bakery ID"
GROUP BY
    b."Bakery Name",
    b."City"
ORDER BY total_surplus DESC;
"""

df_surplus = pd.read_sql(query, connection)

df_surplus.to_csv(
    "results/sql_results/bakery_surplus.csv",
    index=False
)

print("Saved: bakery_surplus.csv")


# ============================================================
# CLOSE CONNECTION
# ============================================================

connection.close()

print("\nAll SQL results exported successfully.")