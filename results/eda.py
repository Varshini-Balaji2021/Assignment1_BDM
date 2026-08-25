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

print("\nFood Waste Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ============================================================
# 3. BASIC DATA INFORMATION
# ============================================================

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescriptive Statistics:")
print(df.describe())


# ============================================================
# 4. CLOSE CONNECTION
# ============================================================

connection.close()

print("\nDatabase connection closed.")