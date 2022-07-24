-- Retrieve the state with the median number of
-- employees in 'Education Services'
-- 1.1 marks: < 10 operators
-- 1.0 marks: < 11 operators
-- 0.8 marks: correct answer

SELECT s.abbr,
    SUM(
        (SELECT SUM(r.employees) FROM countyindustries r 
        JOIN industry i ON r.industry = i.id
        WHERE i.name = 'Educational Services' AND r.county = c.fips)
    ) AS TotalEmployees
FROM state s
JOIN county c ON s.id = c.state
GROUP BY s.abbr
ORDER BY TotalEmployees ASC
LIMIT 1 OFFSET 25;