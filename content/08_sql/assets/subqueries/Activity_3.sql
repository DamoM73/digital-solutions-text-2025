SELECT subjname
FROM subject
WHERE subjnumb IN (
	SELECT subjnumb
	FROM results
	WHERE percent > 90
	)