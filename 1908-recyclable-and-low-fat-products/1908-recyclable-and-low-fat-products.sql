# Write your MySQL query statement below
SELECT product_id FROM Products WHERE product_id NOT IN (SELECT product_id FROM Products WHERE low_fats = 'N' OR recyclable = 'N');