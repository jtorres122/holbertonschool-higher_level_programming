-- Script displays the avg temperature by city ordered by temp
SELECT city, AVG(value) AS avg_temp FROM temperatures
ORDER BY avg_temp DESC
GROUP BY city;
