-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

SELECT T.name, T.2010, T.population AS '2019', T.abbr, ABS(T.Percentage) AS 'Loss (%)'
FROM(
    SELECT *, (T.population - LAG(T.population, 1) OVER (PARTITION BY T.fips)) / LAG(T.population, 1) OVER (PARTITION BY T.fips) * 100 AS 'Percentage', LAG(T.population, 1) OVER (PARTITION BY T.fips) AS '2010'
    FROM(
        SELECT * FROM county c 
        JOIN state s ON s.id = c.state 
        JOIN countypopulation p ON p.county = c.fips
        WHERE p.year IN (2010, 2019)
    ) AS T
    ORDER BY Percentage ASC
) AS T
WHERE T.Percentage = (SELECT(MIN(T.Percentage)))
LIMIT 1 OFFSET 1;