# Plate 2 Plate

Food Waste Reduction & Redistribution Platform

## Business Data Management – Capstone Project

Plate 2 Plate is a database-driven solution designed to reduce food waste by efficiently tracking surplus food from bakeries and redistributing it to NGOs and community organizations. The platform combines PostgreSQL, Supabase, SQL analytics, Python, FastAPI, and a web front end to manage food surplus, donation flow, and business insights.

---

## Team

Team Name: Plate2Plate  


- Nanthitha. P – CB.BU.P2ASB25114
- Navaneeth Krishnan M – CB.BU.P2ASB25117
- Varshini Balaji – CB.BU.P2ASB24193

---

## Project Overview

Food businesses often face surplus food at the end of the day, while NGOs and community groups may need food for redistribution. Plate 2 Plate helps manage this flow by keeping track of:

- Food products and categories
- Bakery surplus data
- Food waste and donation records
- NGO availability and pickup status
- Business-level analysis for decision making

The system uses:
- PostgreSQL database hosted on Supabase
- FastAPI backend
- Python for analysis and preprocessing
- HTML, CSS, and JavaScript for the frontend
- SQL queries for database analysis and reporting

---

## Problem Statement

Food wastage often happens because surplus inventory is not tracked effectively or redistributed on time. Businesses need better visibility into:

- Daily surplus food quantity
- Food waste levels
- Category-wise waste and surplus
- Bakery-wise performance
- Donation availability
- NGO distribution support
- Pickup and donation status
=======
- Product-level waste
- Category-level surplus
- Bakery-level surplus
- Donation quantities
- NGO distribution
- Pickup status

Plate 2 Plate addresses this by combining a structured database, analytical queries, and a user-friendly web interface.

---

## Objectives

The project aims to:

1. Design a relational database for surplus food management
2. Store data for bakeries, products, NGOs, donations, and waste
3. Use SQL for analysis and reporting
4. Perform data preprocessing and feature engineering using Python
5. Generate analytical insights from business data
6. Connect the frontend with a FastAPI backend
7. Display live results through a browser-based interface
8. Implement secure database access using environment variables and local configuration
9. Maintain the project using Git and GitHub

---

## Technology Stack

- Database: PostgreSQL
- Cloud Database Platform: Supabase
- Backend: FastAPI
- Server: Uvicorn
- Frontend: HTML, CSS, JavaScript
- Data Analysis: Python, Pandas
- Visualization: Matplotlib
- Database Connector: psycopg2
- Environment Variables: python-dotenv
- Version Control: Git, GitHub

---

## Application Workflow

User
  ↓
Frontend (HTML/CSS/JavaScript)
  ↓
FastAPI Backend
  ↓
Supabase PostgreSQL
  ↓
Business Analysis & Reporting
  ↓
Web Dashboard / API Responses

The analysis includes:

## 11.1 Total Surplus

Total daily surplus quantity available across food-waste records.

## 11.2 Total Waste

Total average daily waste across the food-waste records.

## 11.3 Total Donated

Total quantity recorded in the donations table.

## 11.4 Donation-to-Surplus Ratio

Calculated as:

(Total Donated / Total Surplus) × 100


## 11.5 Highest Surplus Category

Identifies the food category with the highest total daily surplus.

## 11.6 Highest Waste Category

Identifies the food category with the highest average daily waste.

## 11.7 Top Bakeries by Surplus

Ranks bakery IDs according to total daily surplus.

## 11.8 Food Category Analysis

Provides category-level:

- Total surplus
- Total waste
- Average daily sales

## 11.9 High-Waste Products

Identifies products with comparatively high average daily waste.

## 11.10 High-Surplus Products

Identifies products with comparatively high daily surplus.

---

## Database Design

The project uses a relational PostgreSQL schema with tables such as:

- bakeries
- food_category
- food_waste
- ngos
- donations

The main relationships connect:
- Bakeries to food waste records
- Bakeries to donations
- NGOs to donations
- Food categories to food items and surplus records

---

## Key Features

- Surplus food tracking
- Bakery and NGO record management
- Food donation history
- Donation status monitoring
- KPI-based business analysis
- Category-level surplus and waste insights
- Data visualization for food surplus trends
- API-based integration between frontend and database

---

## API Endpoints

The backend exposes API endpoints to retrieve and analyze database data, including:

- /api
- /api/connection
- /api/surplus
- /api/bakeries
- /api/ngos
- /api/donations
- /api/business-analysis

These endpoints are consumed by the frontend JavaScript to display data dynamically.

---

## Business Insights Included

The platform generates analytical insights such as:

- Total surplus quantity
- Total waste
- Total donated amount/quantity
- Donation-to-surplus ratio
- Highest surplus category
- Highest waste category
- Top bakeries by surplus
- Category-wise surplus and waste summary
- High-waste and high-surplus products
- Donation availability analysis

---

## Data Analysis and SQL

The project includes SQL-based analysis using operations such as:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- JOIN
- Subqueries
- CTEs
- Aggregations
- Window functions

Python is used for:
- Data cleaning
- Missing value checks
- Duplicate checking
- Feature engineering
- Business analysis
- Visualization

---

## Repository Structure

```text
Assignment1_BDM/
│
├── assets/
│   ├── food_surplus_chart.png
│   ├── Plate 2 Plate ER Diagram.png
│   ├── Plate 2 Plate — System User Flow.png
│   └── Plate 2 Plate logo.png
│
├── backend/
│   └── app.py
│
├── results/
│   ├── eda.py
│   ├── results.py
│   ├── visualization.py
│   └── ...
│
├── supabase/
│   ├── bakeries.sql
│   ├── donations.sql
│   ├── food_category.sql
│   ├── food_waste.sql
│   ├── joins.sql
│   ├── ngos.sql
│   ├── plate2plate_queries.sql
│   └── database/
│
├── index.html
├── script.js
├── style.css
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

> Note: The .env file contains local configuration and should not be committed to GitHub.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Varshini-Balaji2021/Assignment1_BDM.git
cd Assignment1_BDM
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn psycopg2-binary pandas matplotlib python-dotenv
```

---

## Environment Variables

Create a .env file in the project root and add your Supabase PostgreSQL connection string:

```env
DATABASE_URL=your_supabase_connection_string_here
```

Do not expose sensitive credentials publicly or commit them to GitHub.

---

## Running the Project

From the project root, start the backend:

```powershell
uvicorn backend.app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/
```

You can also test the API endpoints directly in the browser:

```text
http://127.0.0.1:8000/api/connection
http://127.0.0.1:8000/api/business-analysis
```

---

## Future Enhancements


Possible improvements for the system include:


              SUPABASE POSTGRESQL
                       │
                       ▼
                 FastAPI Backend
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Surplus        Bakeries         NGOs
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                   Donations
                       │
                       ▼
              Business Analysis
                       │
                       ▼
                  JavaScript
                       │
                       ▼
                  index.html
                       │
                       ▼
                 User Interface
```

---

# 📌 24. Key Project Outcomes

### Database Management

A relational PostgreSQL database is used to organize food waste, surplus, bakery, NGO, and donation information.

### SQL Analytics

The project demonstrates aggregation, joins, grouping, filtering, subqueries, CTEs, and window functions.

### Python Analytics

Python and Pandas are used for preprocessing, feature engineering, business analysis, and visualization.

### FastAPI Integration

FastAPI provides the backend layer connecting the website with the Supabase PostgreSQL database.

### Business Insights

The website displays live metrics and business analysis covering surplus, waste, donations, categories, bakeries, and products. The separate Donation Availability insight has been removed to keep the dashboard focused on actual donation activity and core business metrics.

### Data Visualization

Food surplus information is represented visually to support analysis.

### Security

Database credentials remain in the local `.env` configuration and should not be committed to GitHub.

### Version Control

The project is maintained using Git and GitHub.

---

# 🔮 25. Future Enhancements

The current system can be extended with:
- User authentication
- Bakery and NGO login
- Admin dashboard
- Donation request workflow
- Search and filtering features
- Real-time updates
- Predictive waste forecasting
- Advanced BI dashboard
- Geographic matching between surplus food and receiving NGOs

---

## Project Repository

GitHub:
https://github.com/Varshini-Balaji2021/Assignment1_BDM

---

## Conclusion

Plate 2 Plate is a Business Data Management solution that brings together relational database design, SQL analytics, Python-based analysis, FastAPI integration, and a web-application interface to tackle the challenge of food surplus and food waste reduction.

The project demonstrates how data management and analytics can support sustainability, community support, and efficient food redistribution.
