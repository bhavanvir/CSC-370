-- Retrieve alphabetically all states
-- with at least one hundred counties.
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

SELECT s.abbr FROM state s
WHERE (
    SELECT COUNT(*) FROM county c WHERE c.state = s.id
) >= 100
ORDER BY s.abbr ASC;