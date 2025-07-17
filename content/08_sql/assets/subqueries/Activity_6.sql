SELECT owner
FROM repair
WHERE id_numb IN (
	SELECT id_numb
	FROM technicians
	WHERE name = "Carrol"
	)