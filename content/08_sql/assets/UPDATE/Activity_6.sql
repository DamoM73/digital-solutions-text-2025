UPDATE holdings
SET PurPrice = PurPrice * 0.9
WHERE PurDate = (
  SELECT MAX(PurDate)
  FROM holdings
);
