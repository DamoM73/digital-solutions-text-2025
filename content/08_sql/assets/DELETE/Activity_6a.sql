-- Remove from playlist_track first
DELETE FROM playlist_track
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