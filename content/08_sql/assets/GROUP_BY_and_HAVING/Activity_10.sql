SELECT BillingCountry, SUM(Total)
FROM invoices
GROUP BY BillingCountry
HAVING SUM(Total) > 100
ORDER BY BillingCountry