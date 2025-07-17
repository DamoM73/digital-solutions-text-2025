SELECT stname
FROM student
WHERE stnumb IN (
	SELECT stnumb
	FROM results
	WHERE percent > 50
	AND subjnumb IN (
		SELECT subjnumb
		FROM subject
		WHERE subjname = "language"
		)
	)