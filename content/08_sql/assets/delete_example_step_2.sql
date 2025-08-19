DELETE FROM movie
WHERE dirnumb IN (
	SELECT dirnumb
	FROM director
	WHERE dirname = "Gibson, Mel"
	)