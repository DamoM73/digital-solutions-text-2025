-- Remove the tracks
DELETE FROM tracks
WHERE AlbumId IN (
  SELECT AlbumId
  FROM albums
  WHERE ArtistId = (
    SELECT ArtistId
    FROM artists
    WHERE Name = 'Queen'
  )
);