-- Script lists number of records with the same score
SELECT score, count(score) FROM second_table GROUP BY number ORDER BY number ASC;
