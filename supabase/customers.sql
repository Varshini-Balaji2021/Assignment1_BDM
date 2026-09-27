-- ============================================================
-- PLATE 2 PLATE
-- CUSTOMERS TABLE
-- ============================================================

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    preferred_food_category TEXT,
    preferred_pickup_option TEXT
);

-- ============================================================
-- CUSTOMER DATA
-- ============================================================

INSERT INTO customers
(customer_id, customer_name, city, preferred_food_category, preferred_pickup_option)
VALUES
(1, 'Arun Kumar', 'Chennai', 'Bakery', 'Self'),
(2, 'Priya Sharma', 'Coimbatore', 'Cake', 'Delivery'),
(3, 'Rahul Menon', 'Bengaluru', 'Pastry', 'Self'),
(4, 'Sneha R', 'Hyderabad', 'Snack', 'Delivery'),
(5, 'Karthik S', 'Pune', 'Bread', 'Self'),
(6, 'Ananya Iyer', 'Mumbai', 'Dessert', 'Delivery'),
(7, 'Vijay Raj', 'Chennai', 'Pizza', 'Self'),
(8, 'Meena Devi', 'Coimbatore', 'Cookies', 'Delivery'),
(9, 'Naveen Kumar', 'Bengaluru', 'Buns', 'Self'),
(10, 'Divya S', 'Hyderabad', 'Savory', 'Delivery');