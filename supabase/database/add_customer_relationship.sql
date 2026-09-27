-- ============================================================
-- PLATE 2 PLATE
-- ADD CUSTOMER RELATIONSHIP TO EXISTING DONATIONS TABLE
-- ============================================================
-- Run this once in Supabase SQL Editor if donations already exists.

ALTER TABLE public.donations
ADD COLUMN IF NOT EXISTS customer_id INTEGER;

ALTER TABLE public.donations
DROP CONSTRAINT IF EXISTS donations_customer_fk;

ALTER TABLE public.donations
ADD CONSTRAINT donations_customer_fk
FOREIGN KEY (customer_id)
REFERENCES public.customers(customer_id);

-- Verify
SELECT
    d.donation_id,
    d.customer_id,
    c.customer_name,
    d.product_name,
    d.quantity_donated,
    d.pickup_status
FROM public.donations d
LEFT JOIN public.customers c
    ON d.customer_id = c.customer_id
LIMIT 15;
