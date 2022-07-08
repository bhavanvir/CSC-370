-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

SELECT s.abbr, i.name FROM county c 
JOIN countyindustries r ON r.county = c.fips
JOIN state s ON s.id = c.state
JOIN industry i ON r.industry = i.id
