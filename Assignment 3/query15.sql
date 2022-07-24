-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer

SELECT 
    (SUM(MoreFemales = 'TRUE') / (SUM(MoreFemales = 'FALSE') + SUM(MoreFemales = 'TRUE'))) AS 'Fraction'
FROM(
    SELECT a.county,
    CASE WHEN a.population > b.population THEN 'TRUE' ELSE 'FALSE' END AS 'MoreFemales'
    FROM genderbreakdown a
    JOIN genderbreakdown b ON a.county = b.county
    WHERE a.gender = 'female'
    AND b.gender = 'male'
) AS T;