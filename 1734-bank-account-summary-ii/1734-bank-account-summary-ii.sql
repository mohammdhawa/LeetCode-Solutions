# Write your MySQL query statement below
SELECT u.name, 
SUM(amount) AS balance
FROM Transactions t INNER JOIN Users u
ON t.account = u.account
GROUP BY t.account
HAVING SUM(t.amount) > 10000