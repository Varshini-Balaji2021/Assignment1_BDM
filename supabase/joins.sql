-- JOIN DONATIONS & BAKERIES

SELECT
    d.donation_id,
    b."Bakery Name",
    b."City",
    d.product_name,
    d.quantity_donated,
    d.pickup_status
FROM donations d
INNER JOIN bakeries b
    ON b."Bakery ID" = d.bakery_id;

-- DONATIONS, BAKERIES AND NGO

SELECT
    d.donation_id,
    b."Bakery Name",
    b."City",
    d.product_name,
    d.quantity_donated,
    n.ngo_name,
    d.pickup_status
FROM donations d
INNER JOIN bakeries b
    ON b."Bakery ID" = d.bakery_id
INNER JOIN ngos n
    ON n.ngo_id = d.ngo_id;

-- LEFT JOIN

SELECT
    b."Bakery ID",
    b."Bakery Name",
    b."City",
    COUNT(d.donation_id) AS donation_count
FROM bakeries b
LEFT JOIN donations d
    ON b."Bakery ID" = d.bakery_id
GROUP BY
    b."Bakery ID",
    b."Bakery Name",
    b."City"
ORDER BY donation_count ASC;
