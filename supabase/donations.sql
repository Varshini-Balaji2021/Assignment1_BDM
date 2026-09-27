CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY,
    bakery_id TEXT,
    ngo_id INTEGER,
    customer_id INTEGER,
    product_name TEXT,
    quantity_donated NUMERIC,
    donation_date DATE,
    pickup_status TEXT,
    CONSTRAINT donations_customer_fk FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO donations
(bakery_id, ngo_id, customer_id, product_name, quantity_donated, donation_date, pickup_status)
VALUES
('B0001', 1, NULL, 'Pineapple Pastry', 10, '2026-08-20', 'Completed'),
('B0002', 2, NULL, 'Veg Pizza', 5, '2026-08-20', 'Completed'),
('B0003', 1, NULL, 'Muffin', 12, '2026-08-21', 'Pending'),
('B0004', 4, NULL, 'Veg Puff', 8, '2026-08-21', 'Completed'),
('B0005', 5, NULL, 'Brown Bread', 15, '2026-08-22', 'Pending'),
('B0006', 6, NULL, 'Pineapple Pastry', 6, '2026-08-22', 'Completed'),
('B0007', 3, NULL, 'Pineapple Pastry', 10, '2026-08-23', 'Pending'),
('B0008', 2, NULL, 'Pav Buns', 8, '2026-08-23', 'Completed'),
('B0009', 1, NULL, 'Veg Sandwich', 7, '2026-08-24', 'Pending'),
('B0010', 6, NULL, 'Chocolate Cookies', 5, '2026-08-24', 'Completed');
