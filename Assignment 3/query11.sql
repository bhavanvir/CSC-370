-- Retrieve alphabetically the states that had
-- over 100 counties with unemployment rates above 6.0%
-- in 2008.
-- Hint: Unemployment rate = unemployed / labour force
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer

SELECT DISTINCT s.abbr FROM county c, countylabourstats l, state s
WHERE c.fips = l.county AND c.state = s.id AND l.unemployed / l.labour_force > 0.06 AND l.year = 2008
GROUP BY c.state 
HAVING COUNT(c.state) > 100
ORDER BY s.abbr;