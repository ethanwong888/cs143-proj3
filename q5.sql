SELECT COUNT(DISTINCT awardYear) FROM Laureate l INNER JOIN NobelPrize n ON l.lid = n.lid WHERE lName IS NULL AND gender IS NULL;
