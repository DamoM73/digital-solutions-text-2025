SELECT tracks.Name AS "Track", albums.Title AS "Album", genres.Name AS "Genre", tracks.Composer, tracks.Milliseconds / 1000 AS "Length", tracks.UnitPrice
FROM tracks
JOIN albums ON tracks.AlbumId = albums.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
JOIN artists ON albums.ArtistId = artists.ArtistId
WHERE artists.Name = "Def Leppard"