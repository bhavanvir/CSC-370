-- Retrieve in descending order of labour force size
-- all counties that had unemployment rates over 10%
-- in the 2008 census.
-- Hint: Unemployment rate = unemployment / labour force
-- 1.1 marks: <9 operators
-- 1.0 marks: <10 operators
-- 1.0 marks: <15 operators
-- 0.8 marks: correct answer

SELECT DISTINCT c.name, s.abbr, l.labour_force, l.unemployed / l.labour_force * 100 AS "Unemployment Rate"
FROM county c, countylabourstats l, state s
WHERE c.fips = l.county AND l.unemployed / l.labour_force > 0.1 AND l.year = 2008
ORDER BY l.labour_force DESC;