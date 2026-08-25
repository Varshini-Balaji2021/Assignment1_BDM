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

print("Database connected successfully!")


# ============================================================
# 2. LOAD DATA
# ============================================================

query = """
SELECT *
FROM food_waste;
"""

df = pd.read_sql(query, connection)

print("\nOriginal shape:")
print(df.shape)


# ============================================================
# 3. CHECK DUPLICATES
# ============================================================

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\nMissing values:")
print(df.isnull().sum())


# ============================================================
# 5. REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)


# ============================================================
# 6. NUMERICAL COLUMNS
# ============================================================

numeric_columns = [
    "Quantity Available",
    "Daily Surplus Quantity",
    "Average Daily Sales",
    "Average Daily Waste"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# 7. CHECK NEGATIVE VALUES
# ============================================================

print("\nNegative values:")

for column in numeric_columns:
    print(
        column,
        (df[column] < 0).sum()
    )


# ============================================================
# 8. SAVE CLEAN DATA
# ============================================================

os.makedirs("results/eda", exist_ok=True)

df.to_csv(
    "results/eda/food_waste_clean.csv",
    index=False
)

print("\nClean dataset saved:")
print("results/eda/food_waste_clean.csv")


# ============================================================
# 9. CLOSE CONNECTION
# ============================================================

connection.close()

print("\nDatabase connection closed.")
print("Preprocessing completed.")