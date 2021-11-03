-- delete the tables if they already exist
DROP TABLE IF EXISTS Affiliation, Place, Laureate, NobelPrize;

-- create all the tables again from scratch
CREATE TABLE Affiliation(aName varchar(500), city varchar(50), aid int);
CREATE TABLE Place(city varchar(50), country varchar(50), PRIMARY KEY(city));
CREATE TABLE Laureate(lid int, fname varchar(99), lName varchar(99), gender varchar(6), 
    createDate date, city varchar(50), PRIMARY KEY(id));
CREATE TABLE NobelPrize(npid int, lid int, awardYear int(4), category varchar(50), sortOrder varchar(1), portion varchar(3), 
    dateAwarded date, prizeStatus varchar(20), motivation varchar(400), prizeAmount int, PRIMARY KEY(pid));

-- load in all the data from their corresponding .del files
LOAD DATA LOCAL INFILE 'Affiliation.del' INTO TABLE Affiliation FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
LOAD DATA LOCAL INFILE 'Place.del' INTO TABLE Place FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
LOAD DATA LOCAL INFILE 'Laureate.del' INTO TABLE Laureate FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
LOAD DATA LOCAL INFILE 'NobelPrize.del' INTO TABLE NobelPrize FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
