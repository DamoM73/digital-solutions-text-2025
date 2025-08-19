DELETE FROM movies_onhire
WHERE movienumber IN (
	SELECT movienumb
	FROM movie
	WHERE dirnumb IN (
		SELECT dirnumb
		FROM director
		WHERE dirname = "Gibson, Mel"
		)	
	)