-- DATA MODIFICATION LANGUAGE(DML)

CREATE DATABASE TEMP;

USE Temp;

CREATE TABLE Customer(
	id INTEGER PRIMARY KEY,
    cname VARCHAR(255),
    gender CHAR(2),
    city VARCHAR(20),
    pincode INTEGER
);

DESC Customer;

INSERT INTO Customer
	(id, cname, gender, city,pincode) VALUES
		(1,'Sumit Kumar Das','M','Guskara',713128),
        (2,'Dipali Das','F','Guskara',713128),
        (3,'Snehasis Das','M','Burdwan',451236),
        (4,'Pritam Raha','M','Durgapur',562325),
        (5,'Ankita Saha','F','Kalkata',100001),
        (6,'Priti Pal','F','Kalkata',458708);
        
SELECT * FROM CUSTOMER;

-- QUERY: PDATE THE TABLE NAME WHOSE NAME IS 'Priti Pal'
UPDATE CUSTOMER 
SET city='Delhi'
WHERE id=6;

-- UPDATE MULTIPLE ROWS
UPDATE CUSTOMER
SET pincode=100001;
-- ERROR 
-- 00:01:28 UPDATE CUSTOMER SET pincode=100001	
-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  
-- To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.000 sec

-- SOLUTION 1
-- Go to Edit --> Preferences => Click "SQL Editor" tab and uncheck "Safe Updates" check box

-- SOLUTION 2
SET SQL_SAFE_UPDATES=0;

-- DELETE A SPECIFIC RECORD
DELETE FROM CUSTOMER
WHERE ID = 1;

-- DELETE THE WHOLE RECORD
DELETE FROM CUSTOMER;

INSERT INTO Customer
	(id, cname, gender, city,pincode) VALUES
		(7,'Riya Hati','F','Kalakata',NULL);

CREATE TABLE ORDER_DETAILS(
	Order_id INTEGER PRIMARY KEY,
    Delevary_date DATE,
    Cust_id INT,
    FOREIGN KEY(Cust_id) REFERENCES CUSTOMER(id) ON DELETE CASCADE
);

DROP TABLE ORDER_DETAILS;

INSERT INTO Order_details
	(Order_id,Delevary_date,Cust_id) VALUES
		(1,'2019-03-11',4);
        
INSERT INTO Order_details
	(Order_id,Delevary_date,Cust_id) VALUES
		(2,'2019-04-11',4);
        
SELECT * FROM ORDER_DETAILS;

DELETE FROM CUSTOMER WHERE id=4;

-- REPLACE
-- IF DATA IS ALREADY PRESENT THEN IT WILL BE REPLACED
-- & IF DATA IS NOT PRESENT THE IT WILL BE INSERTED

REPLACE INTO CUSTOMER
	(id,cname,city) VALUES
		(123, 'CODE HELP','DELHI');
        
-- USING ID REPLACE
INSERT INTO CUSTOMER
SET id=1200, cname='SUMIT',city='guskara';
        
SELECT * FROM CUSTOMER;

-- REPLACE WITH WHERE
-- SET NULL EVERYTHING WITHOUT id, cname, gender WHERE ID=1
REPLACE INTO CUSTOMER (id,cname,city) 
SELECT id, cname, gender
FROM CUSTOMER 
WHERE id=1;