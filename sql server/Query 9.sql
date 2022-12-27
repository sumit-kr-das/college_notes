CREATE DATABASE ABC;
USE ABC;

CREATE TABLE DEPT1(
	ID INT PRIMARY KEY,
    NAME VARCHAR(255),
    ROLE VARCHAR(255)
);

CREATE TABLE DEPT2(
	ID INT PRIMARY KEY,
    NAME VARCHAR(255),
    ROLE VARCHAR(255)
);

INSERT INTO DEPT1
	(ID,NAME,ROLE) VALUES
		(1,'A','engineer'),
        (2,'B','salesman'),
        (3,'C','engineer'),
        (4,'D','manager'),
        (5,'E','salesman');
        
SELECT * FROM DEPT1;

INSERT INTO DEPT2
	(ID,NAME,ROLE) VALUES
		(3,'C','manager'),
        (6,'F','marketing'),
        (7,'G','salesman');
        
INSERT INTO DEPT2
	(ID,NAME,ROLE) VALUES
		(1,'A','engineer');
        
DELETE FROM DEPT2 WHERE id=1;
        
-- SET OPERATORS

-- LIST OUT ALL THE EMPLOYEES IN THE COMPANY
SELECT * FROM DEPT1
UNION
SELECT * FROM DEPT2;


        
        