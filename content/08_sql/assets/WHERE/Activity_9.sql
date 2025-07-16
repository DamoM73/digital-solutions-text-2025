SELECT *
FROM country
WHERE CountryName IS NULL 
OR Continent IS NULL 
OR Region IS NULL
OR Area IS NULL
OR IndepenYear IS NULL
OR Population IS NULL
OR LifeExp IS NULL
OR GNP IS NULL
OR Government IS NULL
OR Capital IS NULL