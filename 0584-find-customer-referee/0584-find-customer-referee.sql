# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id IS NULL OR referee_id NOT IN (2);