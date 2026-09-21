CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY,
    bakery_id TEXT,
    ngo_id INTEGER,
    product_name TEXT,
    quantity_donated NUMERIC,
    donation_date DATE,
    pickup_status TEXT
);

INSERT INTO donations
(bakery_id, ngo_id, product_name, quantity_donated, donation_date, pickup_status)
VALUES
('B0001', 1, 'Pineapple Pastry', 10, '2026-08-20', 'Completed'),
('B0002', 2, 'Veg Pizza', 5, '2026-08-20', 'Completed'),
('B0003', 1, 'Muffin', 12, '2026-08-21', 'Pending'),
('B0004', 4, 'Veg Puff', 8, '2026-08-21', 'Completed'),
('B0005', 5, 'Brown Bread', 15, '2026-08-22', 'Pending'),
('B0006', 6, 'Pineapple Pastry', 6, '2026-08-22', 'Completed'),
('B0007', 3, 'Pineapple Pastry', 10, '2026-08-23', 'Pending'),
('B0008', 2, 'Pav Buns', 8, '2026-08-23', 'Completed'),
('B0009', 1, 'Veg Sandwich', 7, '2026-08-24', 'Pending'),
('B0010', 6, 'Chocolate Cookies', 5, '2026-08-24', 'Completed');
