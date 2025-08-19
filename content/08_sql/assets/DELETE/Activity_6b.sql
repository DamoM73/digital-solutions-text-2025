-- Remove invoice_items with those tracks
DELETE FROM invoice_items
WHERE TrackId IN (
  SELECT TrackId
  FROM tracks
  WHERE AlbumId IN (
    SELECT AlbumId
    FROM albums
    WHERE ArtistId = (
      SELECT ArtistId
      FROM artists
      WHERE Name = 'Queen'
    )
  )
);