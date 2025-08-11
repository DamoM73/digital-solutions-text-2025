-- First need to remove all invoice items to prevent conflict with invoice table
DELETE FROM invoice_items
WHERE InvoiceId IN (
  SELECT InvoiceId
  FROM invoices
  WHERE CustomerId IN (
    SELECT CustomerId
    FROM customers
    WHERE Country = 'Brazil'
  )
);