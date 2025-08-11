DELETE FROM results
WHERE stnumb IN (
  SELECT stnumb
  FROM student
  WHERE born < '2000-01-01'
);
