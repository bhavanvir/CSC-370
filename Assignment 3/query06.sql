-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'coal', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

WITH T1 AS(
    SELECT T.fips, T.n AS name, T.abbr, T.snow, r.employees
    FROM(
        SELECT c.fips, c.name AS n, s.abbr, c.snow FROM county c
        JOIN state s ON s.id = c.state
        WHERE c.name LIKE '%iron%' OR c.name LIKE '%coal%' OR c.name LIKE '%mineral%'
    ) AS T
    JOIN countyindustries r ON r.county = T.fips
    JOIN industry i ON r.industry = i.id
    WHERE i.id = 19
), T2 AS(
    SELECT c.fips, c.name, s.abbr, c.snow, NULL AS employees FROM county c
    JOIN state s ON s.id = c.state
    WHERE c.name LIKE '%iron%' OR c.name LIKE '%coal%' OR c.name LIKE '%mineral%'
)
SELECT T.name, T.abbr, T.employees
FROM(
    SELECT T2.name, T2.abbr, T2.snow, T2.employees FROM T2
    WHERE T2.fips NOT IN (SELECT T1.fips FROM T1)
    UNION
    SELECT T1.name, T1.abbr, T1.snow, T1.employees FROM T1
) AS T
ORDER BY T.snow; 