-- Plate2Plate BDM: Donation and Food Waste Analysis Queries

-- total donations by bakeries
SELECT
    b."Bakery Name",
    b."City",
    COUNT(d.donation_id) AS total_donations,
    SUM(d.quantity_donated) AS total_food_donated
FROM bakeries b
LEFT JOIN donations d
    ON b."Bakery ID" = d.bakery_id
GROUP BY
    b."Bakery Name",
    b."City"
ORDER BY total_food_donated DESC;

-- total food received by NGO
SELECT
    n.ngo_name,
    n.city,
    COUNT(d.donation_id) AS donations_received,
    SUM(d.quantity_donated) AS total_food_received
FROM ngos n
LEFT JOIN donations d
    ON n.ngo_id = d.ngo_id
GROUP BY
    n.ngo_name,
    n.city
ORDER BY total_food_received DESC;

-- donation status analysis
SELECT
    d.pickup_status,
    COUNT(*) AS number_of_donations,
    SUM(d.quantity_donated) AS total_quantity
FROM donations d
GROUP BY d.pickup_status
ORDER BY number_of_donations DESC;

-- HAVING: subqueries / join + group by + having
SELECT
    b."Bakery Name",
    b."City",
    SUM(d.quantity_donated) AS total_donated
FROM bakeries b
JOIN donations d
    ON b."Bakery ID" = d.bakery_id
GROUP BY
    b."Bakery Name",
    b."City"
HAVING SUM(d.quantity_donated) > 15
ORDER BY total_donated DESC;

-- find NGOs receiving more than 10 units (pcs/kg)
SELECT
    n.ngo_name,
    n.city,
    SUM(d.quantity_donated) AS total_received
FROM ngos n
JOIN donations d
    ON n.ngo_id = d.ngo_id
GROUP BY
    n.ngo_name,
    n.city
HAVING SUM(d.quantity_donated) > 10
ORDER BY total_received DESC;

-- connecting food waste with bakeries
SELECT
    b."Bakery Name",
    b."City",
    f."Product Name",
    f."Food Category",
    f."Daily Surplus Quantity",
    f."Average Daily Waste"
FROM food_waste f
JOIN bakeries b
    ON f."Bakery ID" = b."Bakery ID"
ORDER BY f."Daily Surplus Quantity" DESC;

-- finding high-surplus bakeries
SELECT
    b."Bakery Name",
    b."City",
    SUM(f."Daily Surplus Quantity") AS total_surplus,
    ROUND(AVG(f."Average Daily Waste"), 2) AS average_waste
FROM food_waste f
JOIN bakeries b
    ON f."Bakery ID" = b."Bakery ID"
GROUP BY
    b."Bakery Name",
    b."City"
ORDER BY total_surplus DESC;
