SELECT Country, COUNT(CustomerId)
FROM customers
GROUP BY Country
HAVING COUNT(CustomerId) > 1