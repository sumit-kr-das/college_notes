CREATE DATABASE AMAZON_EMP;
USE AMAZON_EMP;

CREATE TABLE EMPLOYEE(
	id INT PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    age INT,
    email_id VARCHAR(255) UNIQUE,
    phone_no INT UNIQUE,
    CITY VARCHAR(255)
);

CREATE TABLE CLIENT(
	id INT PRIMARY KEY,
	f_name VARCHAR(255),
    l_name VARCHAR(255),
    age INT,
    email_id VARCHAR(255) UNIQUE,
    phone_no INT UNIQUE,
    CITY VARCHAR(255),
    emp_id INT,
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEE(id) ON DELETE SET NULL
);

CREATE TABLE PROJECT(
	id INT PRIMARY KEY,
    emp_id INT,
    name VARCHAR(255),
    start_date DATE,
    client_id INT,
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEE(id) ON DELETE SET NULL,
    FOREIGN KEY(client_id) REFERENCES CLIENT(id) ON DELETE SET NULL
);

INSERT INTO EMPLOYEE
	(id, f_name, l_name, age,email_id, phone_no, CITY) VALUES
		(1,'sumit','das',23,'sumit@gmail.com',1234,'kalkata'),
        (2,'shehasis','pal',24,'snehasis@gmail.com',3455,'guskara'),
        (3,'dipali','das',35,'dipali@gmail.com',865,'ramchandra pur'),
        (4,'susmita','roy',24,'susmita@gmail.com',9564,'guskara'),
        (5,'rounak','mukherjee',22,'rounak@gmail.com',7797,'burdwan');
        
INSERT INTO EMPLOYEE
	(id, f_name, l_name, age,email_id, phone_no, CITY) VALUES
		(6,'Pabitra','Dey',23,'pd@gmail.com',1004,'guskara');
        
SELECT * FROM EMPLOYEE;

INSERT INTO CLIENT
	(id, f_name, l_name, age,email_id, phone_no, CITY,emp_id) VALUES
		(1,'mr','pal',23,'pal@gmail.com',9705,'landan',3),
        (2,'max','worner',55,'max@gmail.com',1785,'dc',3),
        (3,'pratap','singh',35,'singh@gmail.com',9485,'landan',1),
        (4,'peter','parker',23,'parker@gmail.com',5785,'england',5),
        (5,'sushant','aggargal',63,'sushant@gmail.com',9785,'mumbai',2);
        
INSERT INTO CLIENT
	(id, f_name, l_name, age,email_id, phone_no, CITY,emp_id) VALUES
		(7,'Prakash','Das',45,'pprakash@gmail.com',9105,'landan',6);
        
SELECT * FROM PROJECT;

INSERT INTO PROJECT
	(id, emp_id, name, start_date, client_id) VALUES
		(1, 1, 'A', '2021-04-21',3),
        (2, 2, 'B', '2021-03-12',1),
        (3, 3, 'C', '2021-01-16',5),
        (4, 3, 'D', '2021-04-26',2),
        (5, 3, 'E', '2021-05-21',4);
        
INSERT INTO PROJECT
	(id, emp_id, name, start_date, client_id) VALUES
		(6, 2, 'A', '2021-12-15',3);