SELECT lName 
FROM Laureate 
GROUP BY COALESCE(lname, lid) 
HAVING COUNT(*) >= 5;
