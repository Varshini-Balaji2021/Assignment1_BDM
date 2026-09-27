# ============================================================
# PLATE 2 PLATE
# FASTAPI BACKEND
# SUPABASE POSTGRESQL + BUSINESS ANALYSIS
# ============================================================

from pathlib import Path
import os

import pandas as pd
import psycopg2

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


# ============================================================
# 1. PATHS AND ENVIRONMENT
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL was not found in the project-root .env file."
    )


# ============================================================
# 2. FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Plate 2 Plate API",
    description="Food waste reduction and redistribution platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# 3. STATIC FILES (Mounted once properly)
# ============================================================

ASSETS_DIR = BASE_DIR / "assets"

if ASSETS_DIR.exists():
    app.mount(
        "/assets",
        StaticFiles(directory=str(ASSETS_DIR)),
        name="assets"
    )
else:
    # Fallback to backend/assets if it's placed locally inside backend
    LOCAL_ASSETS_DIR = Path(__file__).resolve().parent / "assets"
    if LOCAL_ASSETS_DIR.exists():
        app.mount(
            "/assets",
            StaticFiles(directory=str(LOCAL_ASSETS_DIR)),
            name="assets"
        )


# ============================================================
# 4. DATABASE CONNECTION
# ============================================================

def get_connection():
    return psycopg2.connect(DATABASE_URL)


# ============================================================
# 5. HOME PAGE & FRONTEND ASSET ROUTES
# ============================================================

@app.get("/")
def home():

    index_file = BASE_DIR / "index.html"

    if not index_file.exists():
        # Fallback check locally
        index_file = Path(__file__).resolve().parent / "index.html"

    if not index_file.exists():
        return {
            "message": "Plate 2 Plate API is running",
            "error": "index.html not found"
        }

    return FileResponse(index_file)


@app.get("/style.css")
def serve_css():

    css_file = BASE_DIR / "style.css"
    if not css_file.exists():
        css_file = Path(__file__).resolve().parent / "style.css"

    if not css_file.exists():
        return {
            "error": "style.css not found"
        }

    return FileResponse(css_file)


@app.get("/script.js")
def serve_javascript():

    js_file = BASE_DIR / "script.js"
    if not js_file.exists():
        js_file = Path(__file__).resolve().parent / "script.js"

    if not js_file.exists():
        return {
            "error": "script.js not found"
        }

    return FileResponse(js_file)


# ============================================================
# 6. API STATUS & HEALTH
# ============================================================

@app.get("/api")
def api_home():

    return {
        "success": True,
        "message": "Plate 2 Plate API is running"
    }


# ============================================================
# 7. DATABASE CONNECTION TEST
# ============================================================

@app.get("/api/connection")
def test_connection():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 1;")

        result = cursor.fetchone()

        return {
            "connected": True,
            "message": "Supabase PostgreSQL connected successfully",
            "result": result[0]
        }

    except Exception as error:

        return {
            "connected": False,
            "message": "Database connection failed",
            "error": str(error)
        }

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ============================================================
# 8. LIVE DATABASE STATS (FOR VIVA / PROOF)
# ============================================================

@app.get("/api/database-stats")
def get_database_stats():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM food_waste;")
        food_waste_rows = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM bakeries;")
        bakeries_rows = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM ngos;")
        ngos_rows = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM donations;")
        donations_rows = cursor.fetchone()[0]

        return {
            "success": True,
            "row_counts": {
                "food_waste": food_waste_rows,
                "bakeries": bakeries_rows,
                "ngos": ngos_rows,
                "donations": donations_rows
            }
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# ============================================================
# 9. SURPLUS FOOD
# ============================================================

@app.get("/api/surplus")
def get_surplus_food():

    connection = None

    try:

        connection = get_connection()

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
        FROM food_waste
        ORDER BY "Daily Surplus Quantity" DESC;
        """

        df = pd.read_sql(
            query,
            connection
        )

        df = df.where(
            pd.notnull(df),
            None
        )

        return df.to_dict(
            orient="records"
        )

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 10. BAKERIES
# ============================================================

@app.get("/api/bakeries")
def get_bakeries():

    connection = None

    try:

        connection = get_connection()

        df = pd.read_sql(
            "SELECT * FROM bakeries;",
            connection
        )

        df = df.where(
            pd.notnull(df),
            None
        )

        return df.to_dict(
            orient="records"
        )

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 11. NGOS
# ============================================================

@app.get("/api/ngos")
def get_ngos():

    connection = None

    try:

        connection = get_connection()

        df = pd.read_sql(
            "SELECT * FROM ngos;",
            connection
        )

        df = df.where(
            pd.notnull(df),
            None
        )

        return df.to_dict(
            orient="records"
        )

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 12. DONATIONS
# ============================================================

@app.get("/api/donations")
def get_donations():

    connection = None

    try:

        connection = get_connection()

        df = pd.read_sql(
            "SELECT * FROM donations;",
            connection
        )

        df = df.where(
            pd.notnull(df),
            None
        )

        return df.to_dict(
            orient="records"
        )

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 13. CUSTOMERS
# ============================================================

@app.get("/api/customers")
def get_customers():

    connection = None

    try:

        connection = get_connection()

        query = """
        SELECT
            customer_id,
            customer_name,
            city,
            preferred_food_category,
            preferred_pickup_option
        FROM customers
        ORDER BY customer_id
        LIMIT 10;
        """

        df = pd.read_sql(
            query,
            connection
        )

        df = df.where(
            pd.notnull(df),
            None
        )

        return df.to_dict(
            orient="records"
        )

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 14. BUSINESS ANALYSIS
# ============================================================

@app.get("/api/business-analysis")
def business_analysis():

    connection = None

    try:

        connection = get_connection()

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

        df = pd.read_sql(
            food_waste_query,
            connection
        )

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
            ).fillna(0)

        df["Product Name"] = (
            df["Product Name"]
            .fillna("Unknown Product")
            .astype(str)
            .str.strip()
        )

        df["Food Category"] = (
            df["Food Category"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
        )

        total_surplus = df["Daily Surplus Quantity"].sum()
        total_waste = df["Average Daily Waste"].sum()

        donation_query = """
        SELECT
            COALESCE(SUM(quantity_donated), 0)
            AS total_donations
        FROM donations;
        """

        donation_df = pd.read_sql(
            donation_query,
            connection
        )

        total_donations = float(
            donation_df.iloc[0]["total_donations"]
        )

        donation_rate = (
            (total_donations / total_surplus) * 100
            if total_surplus > 0
            else 0
        )

        category_surplus = (
            df.groupby("Food Category")
            ["Daily Surplus Quantity"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_surplus_category = (
            str(category_surplus.index[0])
            if not category_surplus.empty
            else "N/A"
        )

        category_waste = (
            df.groupby("Food Category")
            ["Average Daily Waste"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_waste_category = (
            str(category_waste.index[0])
            if not category_waste.empty
            else "N/A"
        )

        bakery_surplus = (
            df.groupby("Bakery ID")
            ["Daily Surplus Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        top_bakeries = [
            {
                "bakery_id": str(b_id),
                "total_surplus": float(surplus)
            }
            for b_id, surplus
            in bakery_surplus.items()
        ]

        category_analysis = (
            df.groupby("Food Category")
            .agg(
                total_surplus=("Daily Surplus Quantity", "sum"),
                total_waste=("Average Daily Waste", "sum"),
                average_sales=("Average Daily Sales", "mean")
            )
            .sort_values("total_surplus", ascending=False)
        )

        category_records = [
            {
                "category": str(category),
                "total_surplus": float(row["total_surplus"]),
                "total_waste": float(row["total_waste"]),
                "average_sales": round(float(row["average_sales"]), 2)
            }
            for category, row in category_analysis.iterrows()
        ]

        high_waste_products = (
            df.groupby(["Product Name", "Food Category"], as_index=False)
            .agg(total_waste=("Average Daily Waste", "sum"))
            .sort_values("total_waste", ascending=False)
            .head(10)
        )

        high_waste_records = [
            {
                "product": str(row["Product Name"]),
                "category": str(row["Food Category"]),
                "waste": float(row["total_waste"])
            }
            for _, row in high_waste_products.iterrows()
        ]

        high_surplus_products = (
            df.groupby(["Product Name", "Food Category"], as_index=False)
            .agg(total_surplus=("Daily Surplus Quantity", "sum"))
            .sort_values("total_surplus", ascending=False)
            .head(10)
        )

        high_surplus_records = [
            {
                "product": str(row["Product Name"]),
                "category": str(row["Food Category"]),
                "surplus": float(row["total_surplus"])
            }
            for _, row in high_surplus_products.iterrows()
        ]

        return {
            "success": True,
            "metrics": {
                "total_surplus": round(float(total_surplus), 2),
                "total_waste": round(float(total_waste), 2),
                "total_donations": round(float(total_donations), 2),
                "donation_rate": round(float(donation_rate), 2)
            },
            "key_findings": {
                "highest_surplus_category": highest_surplus_category,
                "highest_waste_category": highest_waste_category
            },
            "top_bakeries": top_bakeries,
            "category_analysis": category_records,
            "high_waste_products": high_waste_records,
            "high_surplus_products": high_surplus_records
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }

    finally:
        if connection:
            connection.close()