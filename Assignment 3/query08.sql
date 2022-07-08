-- Retrieve the fifteen counties with the largest 2016 vote imbalance,
-- with their vote counts and states, restricted to counties with at least 10000 votes
-- Hint: Use pq to measure variance/imbalance in this question,
-- where p is the probability of voting democrat and q, republican.
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <15 operators
-- 0.8 marks: correct answer

SELECT c.name, s.abbr, e.dem, e.gop, e.total_votes FROM county c
JOIN electionresult e ON c.fips = e.county
JOIN state s ON s.id = c.state
WHERE e.year = 2016 AND e.total_votes >= 10000
ORDER BY (e.dem / e.total_votes) * (e.gop / e.total_votes)
LIMIT 15;
