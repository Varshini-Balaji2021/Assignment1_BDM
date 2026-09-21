/* Number of records by food category */

SELECT 
    "Food Category", 
    COUNT(*) AS total_records 
FROM food_waste 
GROUP BY "Food Category" 
ORDER BY total_records DESC; 

/* Waste by food category */

SELECT 
    "Food Category", 
    COUNT(*) AS products, 
    ROUND(AVG("Average Daily Waste"), 2) AS average_waste, 
    SUM("Daily Surplus Quantity") AS total_surplus 
FROM food_waste 
GROUP BY "Food Category" 
ORDER BY total_surplus DESC; 

/* Waste by city */

SELECT 
    "City", 
    COUNT(*) AS records, 
    ROUND(AVG("Average Daily Waste"), 2) AS average_waste, 
    SUM("Daily Surplus Quantity") AS total_surplus 
FROM food_waste 
GROUP BY "City" 
ORDER BY total_surplus DESC; 

/* GROUP BY with multiple calculations */

SELECT 
    "Food Category", 
    COUNT(*) AS products, 
    ROUND(AVG("Original Price"), 2) AS average_price, 
    MIN("Original Price") AS cheapest, 
    MAX("Original Price") AS highest, 
    SUM("Daily Surplus Quantity") AS total_surplus 
FROM food_waste 
GROUP BY "Food Category" 
ORDER BY total_surplus DESC; 

-- HAVING

SELECT 
    "Food Category", 
    COUNT(*) AS products, 
    ROUND(AVG("Average Daily Waste"), 2) AS average_waste 
FROM food_waste 
GROUP BY "Food Category" 
HAVING AVG("Average Daily Waste") > 10 
ORDER BY average_waste DESC; 

-- SUBQUERY

SELECT 
    "Bakery Name", 
    "Product Name", 
    "Average Daily Waste" 
FROM food_waste 
WHERE "Average Daily Waste" > 
      ( 
          SELECT AVG("Average Daily Waste") 
          FROM food_waste 
      ) 
ORDER BY "Average Daily Waste" DESC; 

-- CTE

WITH category_waste AS ( 
    SELECT 
        "Food Category", 
        AVG("Average Daily Waste") AS avg_waste, 
        SUM("Daily Surplus Quantity") AS total_surplus 
    FROM food_waste 
    GROUP BY "Food Category" 
) 
SELECT * 
FROM category_waste 
ORDER BY avg_waste DESC; 

-- WINDOW FUNCTION

SELECT 
    "Food Category", 
    "Product Name", 
    "Average Daily Waste", 
    RANK() OVER ( 
        PARTITION BY "Food Category" 
        ORDER BY "Average Daily Waste" DESC 
    ) AS waste_rank 
FROM food_waste; 

WITH ranked_food AS ( 
    SELECT 
        "Food Category", 
        "Product Name", 
        "Average Daily Waste", 
        RANK() OVER ( 
            PARTITION BY "Food Category" 
            ORDER BY "Average Daily Waste" DESC 
        ) AS waste_rank 
    FROM food_waste 
) 
SELECT * 
FROM ranked_food 
WHERE waste_rank <= 3 
ORDER BY "Food Category", waste_rank;
