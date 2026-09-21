CREATE TABLE food_waste (
    "Bakery ID" TEXT PRIMARY KEY,
    "Bakery Name" TEXT,
    "Branch Name" TEXT,
    "City" TEXT,
    "Address" TEXT,
    "Contact Number" TEXT,
    "Food Category" TEXT,
    "Product Name" TEXT,
    "Quantity Available" NUMERIC,
    "Unit (pcs/kg)" TEXT,
    "Original Price" NUMERIC(10,2),
    "Discounted Price" NUMERIC(10,2),
    "Manufacturing Date" DATE,
    "Expiry Date / Best Before" DATE,
    "Pickup Time" TIME,
    "Closing Time" TIME,
    "Availability Status" TEXT,
    "Daily Surplus Quantity" NUMERIC,
    "Average Daily Sales" NUMERIC,
    "Average Daily Waste" NUMERIC,
    "Donation Available (Yes/No)" TEXT,
    "Pickup Option (Self/Delivery)" TEXT,
    "Store Type (Bakery/Cafe/Restaurant)" TEXT,
    "Last Updated" TIMESTAMP
);

SELECT * FROM food_waste LIMIT 10;

SELECT
    "Bakery ID",
    "Bakery Name",
    "City",
    "Food Category",
    "Product Name",
    "Quantity Available"
FROM food_waste
LIMIT 20;

SELECT
    "Bakery Name",
    "City",
    "Product Name",
    "Quantity Available",
    "Daily Surplus Quantity"
FROM food_waste
WHERE "Availability Status" = 'Available';

SELECT
    "Bakery Name",
    "City",
    "Product Name",
    "Daily Surplus Quantity"
FROM food_waste
WHERE "Donation Available (Yes/No)" = 'Yes';

SELECT
    "Bakery Name",
    "Product Name",
    "Daily Surplus Quantity"
FROM food_waste
WHERE "Daily Surplus Quantity" > 20
ORDER BY "Daily Surplus Quantity" DESC;

SELECT
    "Bakery Name",
    "Product Name",
    "Quantity Available",
    "Daily Surplus Quantity",
    "Average Daily Waste"
FROM food_waste
ORDER BY "Average Daily Waste" DESC;

SELECT
    "Bakery Name",
    "Product Name",
    "Average Daily Waste"
FROM food_waste
ORDER BY "Average Daily Waste" DESC
LIMIT 10;
