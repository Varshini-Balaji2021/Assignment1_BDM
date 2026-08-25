import pandas as pd
import os

# ============================================================
# 1. LOAD FEATURE-ENGINEERED DATA
# ============================================================

input_path = "results/eda/food_waste_features.csv"

df = pd.read_csv(input_path)

print("=" * 70)
print("DEEPER BUSINESS ANALYSIS")
print("=" * 70)

print("\nDataset shape:")
print(df.shape)


# ============================================================
# 2. TOP BAKERIES BY SURPLUS
# ============================================================

print("\n" + "=" * 70)
print("TOP BAKERIES BY SURPLUS")
print("=" * 70)

bakery_surplus = (
    df.groupby("Bakery ID")["Daily Surplus Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(bakery_surplus.head(10))


# ============================================================
# 3. TOP BAKERIES BY WASTE
# ============================================================

print("\n" + "=" * 70)
print("TOP BAKERIES BY WASTE")
print("=" * 70)

bakery_waste = (
    df.groupby("Bakery ID")["Average Daily Waste"]
    .sum()
    .sort_values(ascending=False)
)

print(bakery_waste.head(10))


# ============================================================
# 4. FOOD CATEGORY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("FOOD CATEGORY ANALYSIS")
print("=" * 70)

category_analysis = (
    df.groupby("Food Category")
    .agg(
        total_surplus=("Daily Surplus Quantity", "sum"),
        total_waste=("Average Daily Waste", "sum"),
        average_sales=("Average Daily Sales", "mean"),
        average_waste_rate=("Waste Rate", "mean")
    )
    .sort_values(
        "total_surplus",
        ascending=False
    )
)

print(category_analysis)


# ============================================================
# 5. HIGH-WASTE PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("TOP 10 HIGH-WASTE PRODUCTS")
print("=" * 70)

high_waste_products = (
    df[
        [
            "Product Name",
            "Food Category",
            "Average Daily Waste",
            "Waste Rate"
        ]
    ]
    .sort_values(
        "Average Daily Waste",
        ascending=False
    )
    .head(10)
)

print(high_waste_products)


# ============================================================
# 6. HIGH-SURPLUS PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("TOP 10 HIGH-SURPLUS PRODUCTS")
print("=" * 70)

high_surplus_products = (
    df[
        [
            "Product Name",
            "Food Category",
            "Daily Surplus Quantity",
            "Surplus Rate"
        ]
    ]
    .sort_values(
        "Daily Surplus Quantity",
        ascending=False
    )
    .head(10)
)

print(high_surplus_products)


# ============================================================
# 7. DONATION AVAILABILITY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("DONATION AVAILABILITY ANALYSIS")
print("=" * 70)

donation_analysis = (
    df.groupby("Donation Available (Yes/No)")
    .agg(
        products=("Product Name", "count"),
        total_surplus=("Daily Surplus Quantity", "sum"),
        total_waste=("Average Daily Waste", "sum"),
        average_waste_rate=("Waste Rate", "mean")
    )
)

print(donation_analysis)


# ============================================================
# 8. WASTE LEVEL ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("WASTE LEVEL ANALYSIS")
print("=" * 70)

waste_level = (
    df.groupby("Waste Level", observed=True)
    .agg(
        products=("Product Name", "count"),
        total_surplus=("Daily Surplus Quantity", "sum"),
        total_waste=("Average Daily Waste", "sum")
    )
)

print(waste_level)


# ============================================================
# 9. SURPLUS LEVEL ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("SURPLUS LEVEL ANALYSIS")
print("=" * 70)

surplus_level = (
    df.groupby("Surplus Level", observed=True)
    .agg(
        products=("Product Name", "count"),
        total_surplus=("Daily Surplus Quantity", "sum"),
        total_waste=("Average Daily Waste", "sum")
    )
)

print(surplus_level)


# ============================================================
# 10. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("CORRELATION ANALYSIS")
print("=" * 70)

correlation_columns = [
    "Quantity Available",
    "Daily Surplus Quantity",
    "Average Daily Sales",
    "Average Daily Waste",
    "Waste Rate",
    "Surplus Rate"
]

correlation = df[correlation_columns].corr()

print(correlation)


# ============================================================
# 11. SAVE RESULTS
# ============================================================

os.makedirs("results/eda", exist_ok=True)

category_analysis.to_csv(
    "results/eda/category_analysis.csv"
)

high_waste_products.to_csv(
    "results/eda/high_waste_products.csv",
    index=False
)

high_surplus_products.to_csv(
    "results/eda/high_surplus_products.csv",
    index=False
)

donation_analysis.to_csv(
    "results/eda/donation_availability_analysis.csv"
)

waste_level.to_csv(
    "results/eda/waste_level_analysis.csv"
)

surplus_level.to_csv(
    "results/eda/surplus_level_analysis.csv"
)

correlation.to_csv(
    "results/eda/correlation_matrix.csv"
)


# ============================================================
# 12. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED")
print("=" * 70)

print("""
Results saved under:

results/eda/

The analysis identifies:
- Highest-surplus bakeries
- Highest-waste bakeries
- High-surplus food categories
- High-waste products
- Donation availability patterns
- Waste and surplus levels
- Relationships between numerical variables
""")