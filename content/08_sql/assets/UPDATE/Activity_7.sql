UPDATE customers
SET SupportRepId = (
  SELECT EmployeeId FROM employees
  WHERE FirstName = 'Jane' AND LastName = 'Peacock'
)
WHERE Country = 'Brazil';
