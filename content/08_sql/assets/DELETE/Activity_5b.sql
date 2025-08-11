-- Then need to delete invoices to void conflict with customer table
DELETE FROM invoices
WHERE CustomerId IN (
  SELECT CustomerId
  FROM customers
  WHERE Country = 'Brazil'
);