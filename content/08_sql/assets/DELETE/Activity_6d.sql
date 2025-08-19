-- Remove the albums
DELETE FROM albums
WHERE ArtistId = (
  SELECT ArtistId
  FROM artists
  WHERE Name = 'Queen'
);