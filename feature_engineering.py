import pandas as pd
import os

# ============================================================
# 1. LOAD CLEAN DATA
# ============================================================

input_path = "results/eda/food_waste_clean.csv"

df = pd.read_csv(input_path)

print("=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

print("\nOriginal shape:")
print(df.shape)


# ============================================================
# 2. CONVERT NUMERICAL COLUMNS
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
# 3. WASTE RATE
# ============================================================

df["Waste Rate"] = (
    df["Average Daily Waste"]
    / df["Average Daily Sales"].replace(0, pd.NA)
) * 100


# ============================================================
# 4. SURPLUS RATE
# ============================================================

df["Surplus Rate"] = (
    df["Daily Surplus Quantity"]
    / df["Quantity Available"].replace(0, pd.NA)
) * 100


# ============================================================
# 5. WASTE TO SURPLUS RATIO
# ============================================================

df["Waste to Surplus Ratio"] = (
    df["Average Daily Waste"]
    / df["Daily Surplus Quantity"].replace(0, pd.NA)
)


# ============================================================
# 6. SALES TO AVAILABLE QUANTITY RATIO
# ============================================================

df["Sales Utilization Rate"] = (
    df["Average Daily Sales"]
    / df["Quantity Available"].replace(0, pd.NA)
) * 100


# ============================================================
# 7. DONATION AVAILABILITY AS NUMERIC FEATURE
# ============================================================

df["Donation Available Flag"] = (
    df["Donation Available (Yes/No)"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        "yes": 1,
        "no": 0
    })
)


# ============================================================
# 8. WASTE LEVEL CATEGORY
# ============================================================

df["Waste Level"] = pd.cut(
    df["Waste Rate"],
    bins=[-float("inf"), 10, 25, float("inf")],
    labels=["Low", "Medium", "High"]
)


# ============================================================
# 9. SURPLUS LEVEL CATEGORY
# ============================================================

df["Surplus Level"] = pd.cut(
    df["Daily Surplus Quantity"],
    bins=[-float("inf"), 10, 25, float("inf")],
    labels=["Low", "Medium", "High"]
)


# ============================================================
# 10. DISPLAY NEW FEATURES
# ============================================================

new_features = [
    "Waste Rate",
    "Surplus Rate",
    "Waste to Surplus Ratio",
    "Sales Utilization Rate",
    "Donation Available Flag",
    "Waste Level",
    "Surplus Level"
]

print("\nNew Features:")
print(new_features)

print("\nFeature-engineered data:")
print(df[new_features].head())


# ============================================================
# 11. CHECK MISSING VALUES CREATED
# ============================================================

print("\nMissing values after feature engineering:")

print(
    df[new_features].isnull().sum()
)


# ============================================================
# 12. SAVE FEATURE-ENGINEERED DATA
# ============================================================

os.makedirs("results/eda", exist_ok=True)

output_path = "results/eda/food_waste_features.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nFeature-engineered dataset saved to:")
print(output_path)


# ============================================================
# 13. SUMMARY
# ============================================================

print("\nFinal dataset shape:")
print(df.shape)

print("\nFeature engineering completed successfully.")