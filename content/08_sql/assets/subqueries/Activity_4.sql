SELECT stname
FROM student
WHERE stnumb IN (
	SELECT stnumb
	FROM results
	WHERE subjnumb IN (
		SELECT subjnumb
		FROM subject
		WHERE subjname = "science"
		)
	)
	