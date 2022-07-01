-- Retrieve by life expectancy all
-- counties that have no industry data
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

SELECT *
FROM county AS c 
    LEFT JOIN countyindustries AS i ON c.fips = i.county
WHERE i.county IS NULL
ORDER BY c.life_expectancy;