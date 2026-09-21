-- create bakery

CREATE TABLE bakeries (
    "Bakery ID" TEXT PRIMARY KEY,
    "Bakery Name" TEXT,
    "Branch Name" TEXT,
    "City" TEXT,
    "Address" TEXT,
    "Contact Number" TEXT,
    "Store Type" TEXT
);

INSERT INTO bakeries
SELECT DISTINCT
    "Bakery ID",
    "Bakery Name",
    "Branch Name",
    "City",
    "Address",
    "Contact Number",
    "Store Type (Bakery/Cafe/Restaurant)"
FROM food_waste;

SELECT *
FROM bakeries
LIMIT 10;
