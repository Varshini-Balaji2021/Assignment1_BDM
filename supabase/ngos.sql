CREATE TABLE ngos (
    ngo_id SERIAL PRIMARY KEY,
    ngo_name TEXT,
    city TEXT,
    food_categories_accepted TEXT,
    pickup_available TEXT,
    contact_number TEXT
);

INSERT INTO ngos
(ngo_name, city, food_categories_accepted, pickup_available, contact_number)
VALUES
('Food For All Chennai', 'Chennai', 'Bread, Bakery, Cake, Snack', 'Yes', '+91 9000000001'),
('Coimbatore Food Relief', 'Coimbatore', 'Bread, Pastry, Snacks', 'Yes', '+91 9000000002'),
('Bengaluru Food Rescue', 'Bengaluru', 'Bakery, Dessert, Bread', 'Yes', '+91 9000000003'),
('Hyderabad Food Foundation', 'Hyderabad', 'Cake, Pizza, Snack', 'No', '+91 9000000004'),
('Pune Food Bank', 'Pune', 'Bread, Cookies, Buns', 'Yes', '+91 9000000005'),
('Mumbai Food Aid', 'Mumbai', 'Bakery, Pastry, Savory', 'Yes', '+91 9000000006');

SELECT *
FROM ngos;
