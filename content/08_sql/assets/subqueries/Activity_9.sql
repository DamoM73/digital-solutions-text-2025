SELECT owner
FROM repair
WHERE type IN (
	SELECT type
	FROM devices
	WHERE priority = "H"
	)