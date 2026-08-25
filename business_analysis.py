import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)

print("=" * 70)
print("BAKERY FOOD WASTE BUSINESS ANALYSIS")
print("=" * 70)


# ============================================================
# 2. LOAD FOOD WASTE DATA
# ============================================================

food_waste_query = """
SELECT
    "Bakery ID",
    "Product Name",
    "Food Category",
    "Quantity Available",
    "Daily Surplus Quantity",
    "Average Daily Sales",
    "Average Daily Waste",
    "Donation Available (Yes/No)",
    "City"
FROM food_waste;
"""

food_waste = pd.read_sql(food_waste_query, connection)


# ============================================================
# 3. LOAD DONATION DATA
# ============================================================

donation_query = """
SELECT
    donation_id,
    bakery_id,
    ngo_id,
    quantity_donated,
    pickup_status
FROM donations;
"""

donations = pd.read_sql(donation_query, connection)


# ============================================================
# 4. TOTAL SURPLUS
# ============================================================

total_surplus = food_waste["Daily Surplus Quantity"].sum()

print("\n1. TOTAL FOOD SURPLUS")
print("-" * 50)
print(f"Total surplus quantity: {total_surplus}")


# ============================================================
# 5. TOTAL WASTE
# ============================================================

total_waste = food_waste["Average Daily Waste"].sum()

print("\n2. TOTAL RECORDED DAILY WASTE")
print("-" * 50)
print(f"Total average daily waste: {total_waste}")


# ============================================================
# 6. TOTAL DONATIONS
# ============================================================

total_donations = donations["quantity_donated"].sum()

print("\n3. TOTAL FOOD DONATED")
print("-" * 50)
print(f"Total quantity donated: {total_donations}")


# ============================================================
# 7. DONATION RATE
# ============================================================

if total_surplus > 0:
    donation_rate = (total_donations / total_surplus) * 100
else:
    donation_rate = 0

print("\n4. DONATION-TO-SURPLUS RATIO")
print("-" * 50)
print(f"Donation rate: {donation_rate:.2f}%")


# ============================================================
# 8. TOP FOOD CATEGORY BY SURPLUS
# ============================================================

category_surplus = (
    food_waste
    .groupby("Food Category")["Daily Surplus Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n5. HIGHEST-SURPLUS FOOD CATEGORY")
print("-" * 50)

print(
    f"{category_surplus.index[0]}: "
    f"{category_surplus.iloc[0]} units"
)


# ============================================================
# 9. TOP WASTING FOOD CATEGORY
# ============================================================

category_waste = (
    food_waste
    .groupby("Food Category")["Average Daily Waste"]
    .mean()
    .sort_values(ascending=False)
)

print("\n6. HIGHEST-WASTE FOOD CATEGORY")
print("-" * 50)

print(
    f"{category_waste.index[0]}: "
    f"{category_waste.iloc[0]:.2f} average waste"
)


# ============================================================
# 10. BAKERIES WITH HIGH SURPLUS
# ============================================================

bakery_surplus = (
    food_waste
    .groupby("Bakery ID")["Daily Surplus Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n7. TOP 10 BAKERIES BY SURPLUS")
print("-" * 50)

print(bakery_surplus.head(10))


# ============================================================
# 11. DONATION STATUS
# ============================================================

donation_status = donations.groupby(
    "pickup_status"
)["quantity_donated"].agg(
    ["count", "sum"]
)

print("\n8. DONATION STATUS ANALYSIS")
print("-" * 50)

print(donation_status)


# ============================================================
# 12. BUSINESS RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 70)
print("BUSINESS RECOMMENDATIONS")
print("=" * 70)

print("""
1. Focus donation efforts on food categories generating the highest surplus.

2. Bakeries with consistently high surplus should be prioritized for
   NGO partnerships and scheduled pickups.

3. High-waste categories should be monitored to improve inventory planning.

4. Bakeries should increase the conversion of surplus food into donations.

5. Donation pickup performance should be monitored to reduce food loss
   between surplus generation and NGO collection.
""")


# ============================================================
# 13. CLOSE CONNECTION
# ============================================================

connection.close()

print("\nDatabase connection closed.")
print("Business analysis completed.")