SELECT DISTINCT country 
FROM Affiliation, Place 
WHERE Affiliation.city = Place.city AND Affiliation.aName = 'CERN';
