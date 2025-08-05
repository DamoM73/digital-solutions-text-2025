UPDATE tracks
SET UnitPrice = UnitPrice + 0.20
WHERE GenreId = (
  SELECT GenreId FROM genres
  WHERE Name = 'Rock'
);
