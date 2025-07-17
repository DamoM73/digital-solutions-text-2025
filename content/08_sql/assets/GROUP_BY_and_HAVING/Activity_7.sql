SELECT Risk, CoName, MIN(CurPrice)
FROM company
WHERE Exchange = "NYSE"
GROUP BY Risk
