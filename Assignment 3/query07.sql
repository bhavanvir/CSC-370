-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

SELECT c.name, a.population AS '2010', b.population AS '2019', s.abbr, (((a.population-b.population) / a.population) * 100) AS 'Loss (%)' FROM countypopulation a
LEFT JOIN countypopulation b ON a.county = b.county
JOIN county c ON a.county = c.fips
JOIN state s ON c.state = s.id
WHERE a.year = 2010 AND b.year = 2019 
ORDER BY `Loss (%)` DESC
LIMIT 1;