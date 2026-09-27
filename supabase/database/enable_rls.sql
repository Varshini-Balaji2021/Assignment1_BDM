-- Allow the website to READ the four Plate 2 Plate tables

ALTER TABLE public.food_waste ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bakeries ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.ngos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.donations ENABLE ROW LEVEL SECURITY;


CREATE POLICY "Allow public read food waste"
ON public.food_waste
FOR SELECT
TO anon
USING (true);


CREATE POLICY "Allow public read bakeries"
ON public.bakeries
FOR SELECT
TO anon
USING (true);


CREATE POLICY "Allow public read ngos"
ON public.ngos
FOR SELECT
TO anon
USING (true);


CREATE POLICY "Allow public read donations"
ON public.donations
FOR SELECT
TO anon
USING (true);



SELECT * FROM public.ngos LIMIT 10;

SELECT * FROM public.food_waste LIMIT 5;

SELECT * FROM public.donations LIMIT 5;
