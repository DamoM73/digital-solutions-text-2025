SELECT AlbumId
FROM tracks
GROUP BY AlbumId
HAVING SUM(Milliseconds)/1000 > 3600