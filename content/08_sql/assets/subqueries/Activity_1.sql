SELECT percent
FROM results
WHERE stnumb IN (
	SELECT stnumb
	FROM student
	WHERE grade = 7
	)