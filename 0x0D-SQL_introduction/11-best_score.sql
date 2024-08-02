-- List all records with a score >= 10 from second_table of the database hbtn_0c_0
-- Display both the score and the name, ordered by score (top first)
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
