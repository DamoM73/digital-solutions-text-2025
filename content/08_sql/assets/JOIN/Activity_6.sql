SELECT tracks.Name AS "Track"
FROM tracks
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE genres.Name LIKE "%Metal%"