# 🍞 Plate 2 Plate – Food Waste Reduction & Redistribution Platform

### Business Data Management – Assignment 1

**Plate 2 Plate** is a database-driven food surplus management and redistribution platform designed to help organize, analyze, and redistribute surplus food from bakeries to NGOs.

The project integrates **PostgreSQL, Supabase, SQL analytics, Python data analysis, data visualization, and a web-based frontend** into one Business Data Management solution.

> **Note:** The current repository focuses on database management, analytics, visualization, and frontend database integration. AI/ML-based prediction is considered a future enhancement rather than a currently implemented feature.

---

## 👥 Team

**Team Name:** Plate2Plate  
**Group:** 2

| Student | Register Number |
|---|---|
| Nanthitha. P | CB.BU.P2ASB25114 |
| Navaneeth Krishnan M | CB.BU.P2ASB25117 |
| Varshini Balaji | CB.BU.P2ASB24193 |

---

# 📌 1. Project Overview

Food businesses such as bakeries may have surplus food that remains unsold at the end of the day. At the same time, NGOs and community organizations may require food for redistribution.

Plate 2 Plate provides a structured database and web interface to manage and analyze information related to:

- Food products
- Food categories
- Food surplus
- Food waste
- Bakeries
- NGOs
- Donations
- Donation and pickup status

The system uses **PostgreSQL through Supabase** as the database layer, **Python** for data preprocessing and analysis, and **HTML, CSS, and JavaScript** for the frontend.

---

# 🎯 2. Problem Statement

Food wastage can occur when surplus food is not identified, tracked, or redistributed efficiently.

Businesses may need better visibility into:

- Daily surplus quantities
- Food waste levels
- Product-level waste
- Category-level surplus
- Bakery-level performance
- Donation availability
- Donation quantities
- NGO distribution
- Pickup status

Plate 2 Plate addresses these requirements by combining a relational database, SQL analysis, Python analytics, visualization, and a web-based interface.

---

# 🎯 3. Project Objectives

The main objectives are to:

1. Design a relational database for food surplus and waste management.
2. Store bakery, food, NGO, and donation information.
3. Analyze food surplus and waste using SQL.
4. Demonstrate SQL concepts such as `JOIN`, `GROUP BY`, `HAVING`, subqueries, CTEs, and window functions.
5. Connect Python with the PostgreSQL database.
6. Perform data preprocessing and feature engineering.
7. Generate business-oriented analytical results.
8. Create visualizations for food surplus and waste analysis.
9. Develop a web interface for viewing database information.
10. Connect the frontend to Supabase.
11. Apply Row Level Security (RLS) for database access.
12. Maintain and document the project using GitHub.

---

# 🛠️ 4. Technology Stack

| Component | Technology |
|---|---|
| Database | PostgreSQL |
| Database Platform | Supabase |
| Frontend | HTML5 |
| Styling | CSS3 |
| Client-side Programming | JavaScript |
| Database Connectivity | psycopg2 |
| Data Analysis | Python, Pandas |
| Visualization | Matplotlib |
| Environment Variables | python-dotenv |
| Version Control | Git & GitHub |

---

# 🏗️ 5. System Architecture

```text
                         USER
                           │
                           ▼
                  HTML / CSS / JavaScript
                           │
                           ▼
                Supabase JavaScript Client
                           │
                           ▼
                       SUPABASE
                           │
                           ▼
                     PostgreSQL
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     FOOD WASTE        BAKERIES           NGOs
          │                                 │
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                     DONATIONS
```

### Overall Data and Analysis Workflow

```text
Database Design
       ↓
PostgreSQL / Supabase
       ↓
Data Exploration
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
SQL Analysis
       ↓
Python Analysis
       ↓
Visualization
       ↓
Web Application
       ↓
User Interface
```

---

# 🗄️ 6. Database Design

The project uses a PostgreSQL relational database hosted through Supabase.

The major database tables are:

- `food_waste`
- `bakeries`
- `food_category`
- `ngos`
- `donations`

---

## 6.1 Food Waste Table

The `food_waste` table contains information related to food products, availability, sales, surplus, and waste.

The dataset includes fields related to:

- Bakery ID
- Bakery Name
- Branch Name
- City
- Food Category
- Product Name
- Quantity Available
- Unit
- Original Price
- Discounted Price
- Manufacturing Date
- Expiry / Best Before Date
- Pickup Time
- Closing Time
- Availability Status
- Daily Surplus Quantity
- Average Daily Sales
- Average Daily Waste
- Donation Availability
- Pickup Option
- Store Type
- Last Updated

---

## 6.2 Bakeries Table

The `bakeries` table stores information about participating bakeries.

It contains information such as:

- Bakery ID
- Bakery Name
- Branch Name
- City
- Address
- Contact Number
- Store Type

---

## 6.3 Food Category

Food categories classify products and support category-level analysis.

Category analysis is used for:

- Product counts
- Average waste
- Total surplus
- Average price
- Category ranking

---

## 6.4 NGOs Table

The `ngos` table stores information about organizations that can receive surplus food.

It contains:

- NGO ID
- NGO Name
- City
- Food Categories Accepted
- Pickup Availability
- Contact Number

---

## 6.5 Donations Table

The `donations` table records food donations from bakeries to NGOs.

It contains:

- Donation ID
- Bakery ID
- NGO ID
- Product Name
- Quantity Donated
- Donation Date
- Pickup Status

---

# 🔗 7. Database Relationships

The main logical relationships represented by the project are:

```text
                    BAKERIES
                       │
                       ▼
                  FOOD WASTE


                    BAKERIES
                       │
                       ▼
                   DONATIONS
                       │
                       ▼
                      NGOs
```

The ER diagram provides the visual representation of the database entities and their relationships.

## ER Diagram

![Plate 2 Plate ER Diagram](assets/Plate%202%20Plate%20ER%20Diagram.png)

> **Database note:** The ER diagram represents the intended logical relationships. The SQL schema should be treated as the authoritative source for which relationships are physically enforced through primary keys and foreign keys.

---

# 🔄 8. System User Flow

The system user flow shows how users interact with the Plate 2 Plate interface and how the frontend connects to the database.

![Plate 2 Plate User Flow](assets/Plate%202%20Plate%20%E2%80%94%20System%20User%20Flow.png)

---

# 💻 9. Web Application

The project contains a browser-based frontend developed using:

- HTML
- CSS
- JavaScript
- Supabase JavaScript Client

The interface contains the following sections:

### 🏠 Home

Introduces the Plate 2 Plate project and provides navigation.

### 🔄 User Flow

Displays the system user-flow diagram.

### 🗂️ ER Diagram

Displays the database Entity Relationship Diagram.

### 📈 Visualization

Displays analytical food surplus information.

### 🍞 Surplus Food

Displays surplus-food records retrieved from the `food_waste` table.

### 🏪 Bakeries

Displays bakery information retrieved from the database.

### 🤝 NGOs

Displays NGO information.

### 🎁 Donations

Displays donation records and pickup status.

---

# 🔌 10. Supabase Integration

The frontend uses the Supabase JavaScript client to retrieve information from the PostgreSQL database.

The current frontend retrieves data from:

```text
food_waste
bakeries
ngos
donations
```

The JavaScript application provides functionality for:

- Testing database connectivity
- Loading surplus food
- Loading bakery records
- Loading NGO records
- Loading donation records
- Loading dashboard statistics
- Displaying database connection status

This allows the website to display information stored in the Supabase database.

---

# 🔐 11. Row Level Security

Row Level Security (RLS) is configured for the main frontend-accessed tables:

```text
food_waste
bakeries
ngos
donations
```

The current configuration provides the read access required by the frontend.

The RLS configuration is available at:

```text
supabase/database/enable_rls.sql
```

### Security Note

The frontend may use a Supabase publishable/anonymous key as intended by Supabase's client-side architecture. **Database passwords, service-role keys, private API keys, and other secrets must never be placed in frontend code or committed to GitHub.**

The `.gitignore` file excludes `.env` files from version control.

---

# 📊 12. SQL Analysis

The project demonstrates SQL concepts relevant to Business Data Management.

### Basic SQL

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`

### Aggregate Functions

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

### Relational Operations

- `JOIN`
- `INNER JOIN`
- `LEFT JOIN`
- `GROUP BY`
- `HAVING`

### Advanced SQL

- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- `RANK()`

---

# 📈 13. Business Analysis

The SQL and Python analysis supports business questions such as:

### Bakery Analysis

- Which bakeries have higher surplus?
- What is the total quantity donated by bakery?
- What is the waste level associated with bakery food records?
- Which bakeries have high surplus quantities?

### NGO Analysis

- How much food does each NGO receive?
- How many donations does each NGO receive?
- Which NGOs receive quantities above a defined threshold?

### Donation Analysis

- What is the total quantity donated?
- What is the distribution of pickup status?
- Which bakeries contribute donations?
- Which NGOs receive donations?

### Food Waste Analysis

- What is the food waste by category?
- What is the food surplus by category?
- Which products have higher waste?
- Which products have higher surplus?
- How does waste vary across locations?

---

# 🐍 14. Python Data Analysis

Python is used for database exploration, preprocessing, feature engineering, business analysis, and visualization.

The analytical workflow includes:

1. Database connection
2. Data loading
3. Table exploration
4. Missing-value checking
5. Duplicate checking
6. Data cleaning
7. Data preprocessing
8. Feature engineering
9. Business analysis
10. Visualization

---

# ⚙️ 15. Data Preprocessing

The preprocessing stage includes:

- Loading food-waste data
- Checking dataset dimensions
- Checking duplicate records
- Checking missing values
- Converting numerical fields
- Checking negative values
- Cleaning the dataset
- Saving processed data for further analysis

---

# 🧮 16. Feature Engineering

The project derives additional analytical features from the food-waste dataset.

### Waste Rate

Measures waste relative to available food.

### Surplus Rate

Measures surplus relative to available food.

### Waste to Surplus Ratio

Compares waste quantity with surplus quantity.

### Sales Utilization Rate

Measures the proportion of available food represented by sales.

### Donation Available Flag

Converts donation availability into an analytical indicator.

### Waste Level

Categorizes waste into:

```text
Low
Medium
High
```

### Surplus Level

Categorizes surplus into:

```text
Low
Medium
High
```

---

# 📈 17. Data Visualization

The project includes visual analysis of food surplus.

## Food Surplus by Category

![Food Surplus Visualization](assets/food_surplus_chart.png)

The visualization provides a category-level view of surplus food quantities.

Additional visualization outputs are available in the `results/` directory.

---

# 📁 18. Repository Structure

```text
Assignment1_BDM/
│
├── assets/
│   ├── Plate 2 Plate logo.png
│   ├── Plate 2 Plate — System User Flow.png
│   ├── Plate 2 Plate ER Diagram.png
│   └── food_surplus_chart.png
│
├── results/
│   ├── eda.py
│   ├── results.py
│   ├── visualization.py
│   └── surplus_by_category.png
│
├── supabase/
│   ├── bakeries.sql
│   ├── donations.sql
│   ├── food_category.sql
│   ├── food_waste.sql
│   ├── joins.sql
│   ├── ngos.sql
│   ├── plate2plate_queries.sql
│   │
│   └── database/
│       └── enable_rls.sql
│
├── 1_explore_tables.py
├── business_analysis.py
├── deeper_analysis.py
├── feature_engineering.py
├── joins.py
├── preprocessing.py
├── test_connection.py
│
├── index.html
├── script.js
├── style.css
├── .gitignore
└── README.md
```

---

# 📄 19. Important Files

| File | Purpose |
|---|---|
| `index.html` | Main website interface |
| `style.css` | Website styling |
| `script.js` | Frontend logic and Supabase integration |
| `preprocessing.py` | Data cleaning and preprocessing |
| `feature_engineering.py` | Derived analytical features |
| `business_analysis.py` | Business-oriented analysis |
| `deeper_analysis.py` | Additional analysis |
| `joins.py` | SQL JOIN analysis |
| `test_connection.py` | Database connection testing |
| `supabase/food_waste.sql` | Food waste database structure/data |
| `supabase/bakeries.sql` | Bakery database structure/data |
| `supabase/ngos.sql` | NGO database structure/data |
| `supabase/donations.sql` | Donation database structure/data |
| `supabase/food_category.sql` | Category-level SQL analysis |
| `supabase/joins.sql` | JOIN-based SQL analysis |
| `supabase/plate2plate_queries.sql` | Business analysis queries |
| `supabase/database/enable_rls.sql` | Row Level Security configuration |

---

# 🚀 20. Installation and Setup

## Step 1 – Clone the Repository

```bash
git clone https://github.com/Varshini-Balaji2021/Assignment1_BDM.git
cd Assignment1_BDM
```

## Step 2 – Create a Python Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

## Step 3 – Install Dependencies

```bash
pip install psycopg2-binary pandas matplotlib python-dotenv
```

---

# 🔑 21. Environment Variables

Create a `.env` file in the project root for database credentials used by Python.

Example:

```env
DATABASE_URL=your_supabase_postgresql_connection_string
```

Do not commit the `.env` file to GitHub.

The repository `.gitignore` excludes:

```text
.env
.venv/
__pycache__/
*.csv
```

---

# 🐍 22. Running the Python Analysis

Example:

```bash
python 1_explore_tables.py
```

Other analysis scripts include:

```bash
python preprocessing.py
python feature_engineering.py
python business_analysis.py
python deeper_analysis.py
python joins.py
```

---

# 🌐 23. Running the Website

The frontend can be opened using a local development server.

For example, using VS Code Live Server:

```text
index.html
```

The frontend loads the Supabase JavaScript client and retrieves data from the configured Supabase database.

---

# 🔄 24. End-to-End Project Workflow

```text
              DATA SOURCES
                   │
                   ▼
          PostgreSQL / Supabase
                   │
                   ▼
            Data Exploration
                   │
                   ▼
          Data Preprocessing
                   │
                   ▼
          Feature Engineering
                   │
                   ▼
             SQL Analysis
                   │
                   ▼
           Python Analysis
                   │
                   ▼
             Visualization
                   │
                   ▼
            Web Application
                   │
                   ▼
              User Interface
```

---

# 📌 25. Key Project Outcomes

### Database Management
A relational PostgreSQL database is used to organize food waste, surplus, bakery, NGO, and donation information.

### SQL Analytics
The project demonstrates aggregation, joins, grouping, filtering, subqueries, CTEs, and window functions.

### Python Analytics
Python is used for preprocessing, feature engineering, business analysis, and visualization.

### Web Integration
The frontend retrieves and displays database information through Supabase.

### Data Visualization
Food surplus information is represented visually to support analysis.

### Security
Row Level Security is configured for the tables accessed by the frontend.

### Version Control
The project is maintained using Git and GitHub.

---

# 🔮 26. Future Enhancements

The current system can be extended with:

- User authentication
- Bakery login
- NGO login
- Admin dashboard
- Donation request functionality
- Advanced search and filtering
- Location-based bakery and NGO matching
- Real-time donation updates
- Automated surplus notifications
- Food-waste prediction models
- Machine-learning based surplus prediction
- Advanced business intelligence dashboards

---

# 👥 27. Team Members

### Plate2Plate – Group 2

**Nanthitha. P**  
CB.BU.P2ASB25114

**Navaneeth Krishnan M**  
CB.BU.P2ASB25117

**Varshini Balaji**  
CB.BU.P2ASB24193

---

# 🔗 28. Project Repository

GitHub Repository:

https://github.com/Varshini-Balaji2021/Assignment1_BDM

---

# 🍞 Plate 2 Plate

### Reducing Food Waste. Feeding Communities.

**Plate 2 Plate** integrates **relational database design, SQL analytics, Python data analysis, visualization, Supabase, and a web-based interface** into a Business Data Management project focused on food surplus and redistribution.
