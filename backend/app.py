from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from dotenv import load_dotenv

import os
import psycopg2
import pandas as pd


# ============================================================
# 1. LOAD ENVIRONMENT
# ============================================================

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


# ============================================================
# 2. FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Plate 2 Plate",
    description="Food Waste Reduction Business Analysis API",
    version="1.0"
)


# ============================================================
# 3. CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# 4. FRONTEND FILES
# ============================================================

# Serve assets folder
if os.path.exists("assets"):
    app.mount(
        "/assets",
        StaticFiles(directory="assets"),
        name="assets"
    )


@app.get("/")
def serve_frontend():
    return FileResponse("index.html")


@app.get("/style.css")
def serve_css():
    return FileResponse("style.css")


@app.get("/script.js")
def serve_script():
    return FileResponse("script.js")


# ============================================================
# 5. DATABASE CONNECTION
# ============================================================

def get_connection():

    if not DATABASE_URL:
        raise Exception(
            "DATABASE_URL is missing from .env"
        )

    return psycopg2.connect(
        DATABASE_URL
    )


# ============================================================
# 6. HELPER - CONVERT DATABASE DATA TO JSON
# ============================================================

def clean_records(df):

    if df.empty:
        return []

    # Replace NaN / NaT with None
    df = df.where(
        pd.notnull(df),
        None
    )

    records = df.to_dict(
        orient="records"
    )

    return records


# ============================================================
# 7. API STATUS
# ============================================================

@app.get("/api")
def api_status():

    return {
        "message": "Plate 2 Plate API is running"
    }


# ============================================================
# 8. DATABASE CONNECTION TEST
# ============================================================

@app.get("/api/connection")
def test_connection():

    connection = None

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1"
        )

        result = cursor.fetchone()

        cursor.close()

        return {
            "connected": True,
            "message":
                "Supabase PostgreSQL connected successfully",
            "result": result[0]
        }

    except Exception as error:

        return {
            "connected": False,
            "message":
                "Database connection failed",
            "error": str(error)
        }

    finally:

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
        SELECT *
        FROM food_waste
        ORDER BY "Daily Surplus Quantity" DESC;
        """

        df = pd.read_sql(
            query,
            connection
        )

        return clean_records(df)

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

        return clean_records(df)

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 11. NGOs
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

        return clean_records(df)

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

        return clean_records(df)

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }

    finally:

        if connection:
            connection.close()


# ============================================================
# 13. COMPLETE BUSINESS ANALYSIS
# ============================================================

@app.get("/api/business-analysis")
def business_analysis():

    connection = None

    try:

        connection = get_connection()

        # ====================================================
        # LOAD FOOD WASTE DATA
        # ====================================================

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

        food_waste = pd.read_sql(
            food_waste_query,
            connection
        )


        # ====================================================
        # LOAD DONATIONS
        # ====================================================

        donation_query = """
        SELECT
            donation_id,
            bakery_id,
            ngo_id,
            quantity_donated,
            pickup_status
        FROM donations;
        """

        donations = pd.read_sql(
            donation_query,
            connection
        )


        # ====================================================
        # BASIC METRICS
        # ====================================================

        total_surplus = (
            food_waste[
                "Daily Surplus Quantity"
            ]
            .fillna(0)
            .sum()
        )

        total_waste = (
            food_waste[
                "Average Daily Waste"
            ]
            .fillna(0)
            .sum()
        )

        total_donated = (
            donations[
                "quantity_donated"
            ]
            .fillna(0)
            .sum()
        )


        # ====================================================
        # DONATION-TO-SURPLUS RATIO
        # ====================================================

        if total_surplus > 0:

            donation_rate = (
                total_donated
                / total_surplus
            ) * 100

        else:

            donation_rate = 0


        # ====================================================
        # FOOD CATEGORY ANALYSIS
        # ====================================================

        category_analysis = (

            food_waste
            .groupby("Food Category")
            .agg(

                total_surplus=(
                    "Daily Surplus Quantity",
                    "sum"
                ),

                total_waste=(
                    "Average Daily Waste",
                    "sum"
                ),

                average_sales=(
                    "Average Daily Sales",
                    "mean"
                )

            )
            .sort_values(
                "total_surplus",
                ascending=False
            )
        )


        category_records = []

        for category, row in category_analysis.iterrows():

            category_records.append({

                "category":
                    str(category),

                "total_surplus":
                    float(
                        row["total_surplus"]
                    ),

                "total_waste":
                    float(
                        row["total_waste"]
                    ),

                "average_sales":
                    round(
                        float(
                            row["average_sales"]
                        ),
                        2
                    )

            })


        # ====================================================
        # HIGHEST SURPLUS CATEGORY
        # ====================================================

        if len(category_analysis) > 0:

            highest_surplus_category = (
                str(
                    category_analysis.index[0]
                )
            )

        else:

            highest_surplus_category = "N/A"


        # ====================================================
        # HIGHEST WASTE CATEGORY
        # ====================================================

        category_waste = (

            food_waste
            .groupby("Food Category")
            ["Average Daily Waste"]
            .mean()
            .sort_values(
                ascending=False
            )
        )

        if len(category_waste) > 0:

            highest_waste_category = (
                str(
                    category_waste.index[0]
                )
            )

        else:

            highest_waste_category = "N/A"


        # ====================================================
        # TOP BAKERIES BY SURPLUS
        # ====================================================

        bakery_surplus = (

            food_waste
            .groupby("Bakery ID")
            ["Daily Surplus Quantity"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        top_bakeries = []

        for bakery_id, value in (
            bakery_surplus
            .head(10)
            .items()
        ):

            top_bakeries.append({

                "bakery_id":
                    str(bakery_id),

                "surplus_quantity":
                    float(value)

            })


        # ====================================================
        # HIGH-WASTE PRODUCTS
        # ====================================================

        high_waste = (

            food_waste[
                [
                    "Product Name",
                    "Food Category",
                    "Average Daily Waste"
                ]
            ]
            .sort_values(
                "Average Daily Waste",
                ascending=False
            )
            .head(10)
        )

        high_waste_products = []

        for _, row in high_waste.iterrows():

            high_waste_products.append({

                "product":
                    str(row["Product Name"]),

                "category":
                    str(row["Food Category"]),

                "waste":
                    float(
                        row[
                            "Average Daily Waste"
                        ]
                    )

            })


        # ====================================================
        # HIGH-SURPLUS PRODUCTS
        # ====================================================

        high_surplus = (

            food_waste[
                [
                    "Product Name",
                    "Food Category",
                    "Daily Surplus Quantity"
                ]
            ]
            .sort_values(
                "Daily Surplus Quantity",
                ascending=False
            )
            .head(10)
        )

        high_surplus_products = []

        for _, row in high_surplus.iterrows():

            high_surplus_products.append({

                "product":
                    str(row["Product Name"]),

                "category":
                    str(row["Food Category"]),

                "surplus":
                    float(
                        row[
                            "Daily Surplus Quantity"
                        ]
                    )

            })


        # ====================================================
        # DONATION AVAILABILITY
        # ====================================================

        donation_analysis = (

            food_waste
            .groupby(
                "Donation Available (Yes/No)"
            )
            .agg(

                products=(
                    "Product Name",
                    "count"
                ),

                total_surplus=(
                    "Daily Surplus Quantity",
                    "sum"
                ),

                total_waste=(
                    "Average Daily Waste",
                    "sum"
                )

            )
        )

        donation_availability = []

        for status, row in (
            donation_analysis.iterrows()
        ):

            donation_availability.append({

                "status":
                    str(status),

                "products":
                    int(row["products"]),

                "total_surplus":
                    float(
                        row["total_surplus"]
                    ),

                "total_waste":
                    float(
                        row["total_waste"]
                    )

            })


        # ====================================================
        # RETURN ONE COMPLETE BUSINESS ANALYSIS
        # ====================================================

        return {

            "success": True,

            "metrics": {

                "total_surplus":
                    round(
                        float(total_surplus),
                        2
                    ),

                "total_waste":
                    round(
                        float(total_waste),
                        2
                    ),

                "total_donations":
                    round(
                        float(total_donated),
                        2
                    ),

                "donation_rate":
                    round(
                        float(donation_rate),
                        2
                    )

            },

            "key_findings": {

                "highest_surplus_category":
                    highest_surplus_category,

                "highest_waste_category":
                    highest_waste_category

            },

            "top_bakeries":
                top_bakeries,

            "category_analysis":
                category_records,

            "high_waste_products":
                high_waste_products,

            "high_surplus_products":
                high_surplus_products,

            "donation_availability":
                donation_availability

        }


    except Exception as error:

        return {

            "success": False,

            "error": str(error)

        }


    finally:

        if connection:
            connection.close()