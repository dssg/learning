-- Chuckles... --
-- http://xkcd.com/327/ --

-- Drop Table
DROP TABLE project

-- Create Table
CREATE TABLE project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(2000000000),
    type TEXT(2000000000)
)

INSERT INTO project (title, type) VALUES ("Unknown", "Unknown")

INSERT INTO project (title, type) 
    SELECT "City of Chicago Dept. of Transportation - Predicting when Divvy bike share stations will be empty or full" AS title, "Transportation" AS type
UNION SELECT "Chicago Transit Authority - Simulating better bus service", "Transportation"
UNION SELECT "Chicago Police Department , University of Chicago Crime Lab - Predictive analytics of crime", "Public Safety"
UNION SELECT "Cook County Land Bank , Institute for Housing Studies - Abandoned property analytics tool", "Economic Development"
UNION SELECT "Mesa Public Schools - Getting kids into college", "Economic Development"
UNION SELECT "City of Chicago Dept. of Transportation - Predicting when Divvy bike share stations will be empty or full", "Transportation"
UNION SELECT "Lawrence Berkeley National Laboratory - Predicting building energy savings", "Energy"
UNION SELECT "Environmental Defense Fund - Predicting building energy loan performance", "Energy"
UNION SELECT "NorthShore University HealthSystem - Using electronic medical record data to predict better health","Health"
UNION SELECT "Nurse-Family Partnership - Tracking the impact of early childhood health programs","Health"
UNION SELECT "Ushahidi - Smarter crowdsourcing for crisis maps", "Disaster response"
UNION SELECT "Qatar Computing Research Institute - Measuring disaster damage with tweets", "Disaster response"


-- Add a FOREIGN KEY sqlite
DROP TABLE fellow

CREATE TABLE fellow ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT(2000000000),
    last_name TEXT(2000000000),
    id_project INTEGER,
    FOREIGN KEY (id_project) REFERENCES project(id)
)


-- Insert multiple (weird SQlite syntax -- easier in other SQL)
-- http://stackoverflow.com/questions/1609637/is-it-possible-to-insert-multiple-rows-at-a-time-in-an-sqlite-database
INSERT INTO 'fellow' (first_name, last_name, id_project)
    SELECT "Samrachana" AS first_name,"Adhikari" AS last_name, 1 AS id_project
UNION SELECT "Andres","Akle Carranza",1
UNION SELECT "Scott","Alfeld",1
UNION SELECT "Sophia","Alice",1
UNION SELECT "Zahra","Ashktorab",1
UNION SELECT "Jonathan","Auerbach",1
UNION SELECT "Varoon","Bashyakarla",1
UNION SELECT "Jordan","Bates",1
UNION SELECT "John","Brock",1
UNION SELECT "Christopher","Brown",1
UNION SELECT "Giorgio","Cavaggion",1
UNION SELECT "Kyla","Cheung",1
UNION SELECT "Walter","Dempsey",1
UNION SELECT "Sarah","Evans",1
UNION SELECT "Andrea","Fernandez Conde",1
UNION SELECT "Adam","Fishman",1
UNION SELECT "Jette","Henderson",1
UNION SELECT "Kayla","Jacobs",1
UNION SELECT "Kwang-Sung","Jun",1
UNION SELECT "Nathan","Leiby",1
UNION SELECT "Allen","Lin",1
UNION SELECT "Edward","McFowland",1
UNION SELECT "Paul","Meinshausen",1
UNION SELECT "Breanna","Miller",1
UNION SELECT "Evan","Misshula",1
UNION SELECT "Jit","Nandi",1
UNION SELECT "Ahmad","Qamar",1
UNION SELECT "Emily","Rowe",1
UNION SELECT "Nihar","Shah",1
UNION SELECT "Camelia","Simoiu",1
UNION SELECT "Sriram","Somanchi",1
UNION SELECT "Edward","Su",1
UNION SELECT "Vidhur","Vohra",1
UNION SELECT "Joseph","Walsh",1
UNION SELECT "Skyler","Whorton",1
UNION SELECT "Min","Xu",1


--
-- Example queries
--

-- CRUD for a fellow... into the database
-- Create
INSERT INTO fellow (first_name, last_name, id_project) VALUES ("Notorious", "B.I.G.", 1)
-- Read
SELECT * FROM fellow
-- Update
UPDATE fellow SET first_name = "Big Papa" WHERE first_name = "Notorious"
-- Delete
DELETE FROM fellow WHERE first_name = "Nate"

-- Constraints: Cant do this! Invalid id_project (but it's working ... must have setup wrong way :P)
INSERT INTO fellow (first_name, last_name, id_project) VALUES ("Notorious", "B.I.G.", 200)

--     WHERE IN        
SELECT * FROM fellow WHERE first_name IN ("Min", "Nihar")

--     WHERE LIKE
-- Name contains and "A" as first character
SELECT * FROM fellow WHERE first_name LIKE "a%"

-- Name contains and "A" as first character OR "a" as any character
SELECT * FROM fellow WHERE first_name LIKE "a%" OR last_name LIKE "a%"

--     JOIN ( / LEFT / RIGHT / NATURAL / INNER / OUTER) ON
SELECT * FROM fellow JOIN project ON project.id = fellow.id_project

SELECT * FROM fellow JOIN project ON project.id = fellow.id_project

--     UNION
SELECT * FROM fellow WHERE first_name LIKE "a%"
UNION
SELECT * FROM fellow WHERE first_name LIKE "b%"

--     INTERSECTION
SELECT * FROM fellow WHERE first_name LIKE "a%"
INTERSECT
SELECT * FROM fellow WHERE first_name LIKE "%d%"

--     subqueries
SELECT * FROM 
(SELECT * FROM fellow LIMIT 2)
WHERE first_name LIKE "A%"

--     transactions
-- START TRANSACTION;
-- UPDATE  SET balance =   balance -   1000    WHERE   number  =   2;
-- UPDATE  SET balance =   balance +   1000    WHERE   number  =   1;
-- COMMIT;



