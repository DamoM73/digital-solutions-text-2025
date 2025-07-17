SELECT albums.Title AS "Album", artists.Name AS "Artist"
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId
ORDER BY artists.Name