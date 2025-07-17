SELECT qualification
FROM experience
WHERE (id_numb, type) IN (
  SELECT id_numb, type
  FROM repair
  WHERE owner = "James"
)