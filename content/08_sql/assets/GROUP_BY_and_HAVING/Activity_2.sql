SELECT memberid, COUNT(movienumber)
FROM movies_onhire
GROUP BY memberid