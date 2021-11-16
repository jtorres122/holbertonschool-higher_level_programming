-- Script lists number of records with the same score
SELECT score,count(score) as number FROM second_table ORDER BY number ASC;
