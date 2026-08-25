import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)

print("Database connected successfully!")


# ============================================================
# 2. LOAD FOOD WASTE DATA
# ============================================================

query = """
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

df = pd.read_sql(query, connection)


# ============================================================
# 3. SURPLUS BY FOOD CATEGORY
# ============================================================

category_surplus = (
    df.groupby("Food Category")["Daily Surplus Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Surplus by Food Category:")
print(category_surplus)


plt.figure(figsize=(10, 6))

category_surplus.plot(kind="bar")

plt.title("Total Food Surplus by Category")
plt.xlabel("Food Category")
plt.ylabel("Total Surplus Quantity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("surplus_by_category.png")

plt.show()


# ============================================================
# 4. AVERAGE WASTE BY FOOD CATEGORY
# ============================================================

category_waste = (
    df.groupby("Food Category")["Average Daily Waste"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Daily Waste by Food Category:")
print(category_waste)


plt.figure(figsize=(10, 6))

category_waste.plot(kind="bar")

plt.title("Average Daily Waste by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Average Daily Waste")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("average_waste_by_category.png")

plt.show()


# ============================================================
# 5. SURPLUS VS WASTE
# ============================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Daily Surplus Quantity"],
    df["Average Daily Waste"]
)

plt.title("Daily Surplus vs Average Daily Waste")
plt.xlabel("Daily Surplus Quantity")
plt.ylabel("Average Daily Waste")
plt.tight_layout()

plt.savefig("surplus_vs_waste.png")

plt.show()


# ============================================================
# 6. CLOSE CONNECTION
# ============================================================

connection.close()

print("\nDatabase connection closed.")
print("EDA visualizations completed.")