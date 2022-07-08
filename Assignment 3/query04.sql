-- Retrieve alphabetically all states in which
-- every county has a name not found anywhere else
-- in the US
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer

SELECT abbr FROM state
WHERE id NOT IN (
    SELECT a.state FROM county a, county b
    WHERE a.fips <> b.fips AND a.name = b.name
)
ORDER BY abbr;