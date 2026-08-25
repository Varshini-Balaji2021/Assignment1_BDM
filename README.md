# BDM Assignment 1 – AI Food Waste Reduction Platform
Idea: Connects restaurants, bakeries, and supermarkets with customers to sell surplus food before it expires
---------------
Team name: Plate2Plate
Presented by: Group 2: 
1.Nanthitha. P (CB.BU.P2ASB25114)
2.Navaneeth Krishnan M (CB.BU.P2ASB25117)
3.Varshini Balaji (CB.BU.P2ASB24193)


## Student Project

This project is developed as part of the Business Data Management (BDM)
assignment.

The project implements a relational database for managing food surplus,
food waste, bakeries, customers, NGOs, and food donations. The database is
created and managed using PostgreSQL through Supabase, while Python is used
to connect to the database and execute SQL queries.

The project demonstrates SQL concepts ranging from basic table exploration
and filtering to advanced concepts such as JOINs, GROUP BY, HAVING,
subqueries, Common Table Expressions (CTEs), and window functions.

---

# 1. Project Overview

Food businesses such as bakeries can generate significant quantities of
surplus food every day. Instead of allowing usable food to become waste,
the surplus can be identified and connected with NGOs for donation.

This project models such a system using a relational database.

The database stores information about:

- Bakeries
- Food categories
- Customers
- NGOs
- Food waste and surplus
- Donations

The project then uses SQL queries to analyse the stored information.

Python is integrated with the PostgreSQL database so that the SQL queries
can be executed programmatically and their results can be displayed.

---

# 2. Project Objectives

The main objectives of the project are:

1. Create and work with a relational database.
2. Store bakery, food, NGO, customer, and donation information.
3. Explore the structure and contents of database tables.
4. Filter records using SQL conditions.
5. Perform calculations using aggregate functions.
6. Combine information from multiple tables using JOINs.
7. Group records for meaningful analysis.
8. Filter grouped results using HAVING.
9. Use subqueries for analytical questions.
10. Use Common Table Expressions (CTEs).
11. Apply window functions such as RANK() and ROW_NUMBER().
12. Connect Python with PostgreSQL.
13. Execute SQL queries from Python.
14. Organise the complete project using Git.
15. Document and maintain the project using GitHub.

---

# 3. Problem Statement

Bakeries may have food items that remain unsold or become surplus at the
end of the day. At the same time, NGOs may require food donations.

A structured database can help track:

- How much food is available
- How much food becomes surplus
- How much food is wasted
- Which bakeries generate surplus
- Which bakeries donate food
- Which NGOs receive donations
- The quantity of food donated
- The status of donations

The purpose of this project is to build a database-based system that
allows these questions to be answered using SQL.

---

# 4. Database Used

The project uses:

**PostgreSQL**

The database is hosted using:

**Supabase**

Python connects to the PostgreSQL database using:

**psycopg2**

Environment variables are managed using:

**python-dotenv**

---

# 5. Database Tables

The project contains the following major tables.

## 5.1 Food Category

The `food_category` table stores information about the different food
categories used in the project.

It helps classify food products into meaningful categories.

---

## 5.2 Bakeries

The `bakeries` table stores bakery-related information.

Important information includes:

- Bakery ID
- Bakery Name
- City

The Bakery ID is used to connect bakery information with food waste and
donation records.

---

## 5.3 Customers

The `customers` table stores customer-related information.

This table represents the customer side of the food business system.

---

## 5.4 NGOs

The `ngos` table stores information about organisations receiving food
donations.

Important information includes:

- NGO ID
- NGO Name
- City

The NGO ID is used to connect NGOs with donation records.

---

## 5.5 Donations

The `donations` table records food donations made by bakeries to NGOs.

Important fields include:

- donation_id
- bakery_id
- ngo_id
- quantity_donated
- pickup_status

This table connects bakeries and NGOs.

---

## 5.6 Food Waste

The `food_waste` table contains information about food products,
availability, surplus, sales, and waste.

Important fields include:

- Bakery ID
- Product Name
- Food Category
- Quantity Available
- Daily Surplus Quantity
- Average Daily Sales
- Average Daily Waste
- Donation Available (Yes/No)

This table is used to analyse food surplus and waste.

---

# 6. Database Relationships

The major relationships in the database are:

```text
                    BAKERIES
                       |
          +------------+------------+
          |                         |
          v                         v
     FOOD_WASTE                  DONATIONS
                                    |
                                    v
                                   NGOS


FOOD_CATEGORY
      |
      v
FOOD_WASTE


CUSTOMERS
