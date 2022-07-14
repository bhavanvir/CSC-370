-- Out of those counties with at least 25000 residents,
-- retrieve the pair from the same state
-- that had the absolute closest
-- population in 2018
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

WITH T AS(
    SELECT * FROM countypopulation
    JOIN county ON county = fips
    WHERE population >= 25000 AND year = 2018
)
SELECT p2.name, p2.population, p1.name, p1.population FROM T p1
JOIN T p2 ON p1.county <> p2.county AND p1.state = p2.state
ORDER BY ABS(p1.population - p2.population)
LIMIT 1;