-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

WITH T AS (
	SELECT c.state, SUM(p.population) AS 'Population' FROM countypopulation p
    JOIN county c ON p.county = c.fips
    JOIN state s ON c.state = s.id
    WHERE p.year = 2019
    GROUP BY c.state
)
SELECT s.abbr, i.name, SUM(r.payroll) AS 'Total Payrolls', ((SUM(r.employees) / T.Population) * 100) AS `% of Population` FROM countyindustries r
JOIN county c ON r.county = c.fips
JOIN state s ON c.state = s.id
JOIN industry i ON r.industry = i.id
JOIN T ON T.state = c.state
WHERE s.id != 49
GROUP BY c.state, r.industry
HAVING `% of Population` >= 7.5
ORDER BY `Total Payrolls` DESC;