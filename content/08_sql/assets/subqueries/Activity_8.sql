SELECT rate
FROM devices
WHERE type IN (
	SELECT type
	FROM repair
	WHERE owner = "Byrne"
	)