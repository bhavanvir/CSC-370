-- Retrieve alphabetically the names of industries that
-- employ at least five million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT i.name FROM industry i
WHERE (
    SELECT SUM(r.employees) FROM countyindustries r 
    JOIN county c ON r.county = c.fips
    JOIN state s ON c.state = s.id
    WHERE r.industry = i.id AND s.abbr != 'CA'
) >= 5000000
ORDER BY i.name ASC;