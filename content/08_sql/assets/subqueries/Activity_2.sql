SELECT subjname
FROM subject
WHERE tname IN (
	SELECT tname
	FROM teacher
	WHERE room = "A2"
	)