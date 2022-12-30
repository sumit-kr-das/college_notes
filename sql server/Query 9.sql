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
        (3,'C','manager'),
        (4,'D','salesman'),
        (5,'E','engineer');

INSERT INTO DEPT2
	(ID,NAME,ROLE) VALUES
		(3,'C','manager'),
        (6,'F','marketing'),
        (7,'G','salesman');
        
SELECT * FROM DEPT1;
SELECT * FROM DEPT2;

-- SET OPERATORS

-- LIST OUT ALL THE EMPLOYEES IN THE COMPANY
SELECT * FROM DEPT1
UNION
SELECT * FROM DEPT2;

-- LIST OUT ALL THE EMPLOYEES IN ALL DEPERMENTS WHO WORK AS SALESMAN
SELECT *  FROM DEPT1 WHERE ROLE='salesman'
UNION 
SELECT *  FROM DEPT2 WHERE ROLE='salesman';

-- LIST OUT ALL THE EMPLOYEES WHO WORK FOR BOTH THE DEPERMENTS [USING INTERSECTION]
SELECT DEPT1.* FROM DEPT1 INNER JOIN DEPT2 USING(ID);

-- LIST OUT ALL THE EMPLOYEES WORKING IN DEPT1 BUT NOT IN DEPT2 [USING MINUS]
SELECT DEPT1.* FROM DEPT1 LEFT JOIN DEPT2 USING(ID)
WHERE DEPT2.ID IS NULL;
        