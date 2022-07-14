-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

SELECT s.abbr, i.name, SUM(r.payroll) AS 'Total Payroll', (SUM(r.employees) / SUM(p.population) * 100) AS '% of Population' FROM countypopulation p
JOIN county c ON p.county = c.fips
JOIN state s ON c.state = s.id
JOIN countyindustries r ON p.county = r.county
JOIN industry i ON r.industry = i.id
WHERE year = 2019 AND s.id != 49
GROUP BY c.state, r.industry
HAVING SUM(r.employees) / SUM(p.population) * 100 >= 7.5
ORDER BY SUM(r.payroll) DESC;