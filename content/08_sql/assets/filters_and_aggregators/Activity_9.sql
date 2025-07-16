SELECT CoName, MIN(CurPrice)
FROM company
WHERE (Risk = "Medium" OR Risk = "Low")
AND Exchange = "NYSE"