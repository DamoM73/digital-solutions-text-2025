SELECT name
FROM technicians
WHERE id_numb IN (
	SELECT id_numb
	FROM experience
	WHERE type = "iMac" AND qualification = "N"
	)