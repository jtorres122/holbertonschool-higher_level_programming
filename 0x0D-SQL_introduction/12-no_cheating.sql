-- Script updates the score of Bob to 10
SELECT name FROM second_table WHERE name='Bob' UPDATE second_table REPLACE(score, 10);
