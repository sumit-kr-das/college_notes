-- TABLE STRUCTURE
-- CUSTOMER(C_NO, C_NAME, C_ADDRESS)
-- TRUCK(T_NO, DRIVER_NAME)
-- PACKET(P_NO, C_NO, T_NO, WEIGHT, DESTINATION)

CREATE DATABASE GROUPA;
USE GROUPA;

CREATE TABLE CUSTOMER(
	C_NO INT PRIMARY KEY,
    C_NAME VARCHAR(255),
    C_ADDRESS VARCHAR(255)
);

CREATE TABLE TRUCK(
	T_NO INT PRIMARY KEY,
    DRIVER_NAME VARCHAR(255)
);

CREATE TABLE PACKET(
	P_NO INT PRIMARY KEY, 
    C_NO INT,
    T_NO INT,
    WEIGHT INT,
    DESTINATION VARCHAR(255),
    FOREIGN KEY (C_NO) REFERENCES CUSTOMER(C_NO) ON DELETE CASCADE,
    FOREIGN KEY (T_NO) REFERENCES TRUCK(T_NO) ON DELETE CASCADE
);

DESC PACKET;

INSERT INTO CUSTOMER
	(C_NO, C_NAME, C_ADDRESS) VALUES
		(1, 'Raja','Guskara'),
        (2, 'Sumit','Bombay'),
        (3, 'King','Dubai'),
        (4, 'Shoyeb','Kalkata'),
        (5, 'Kazi','Londan');
        
INSERT INTO CUSTOMER
	(C_NO, C_NAME, C_ADDRESS) VALUES
		(8, 'Shoyeb','Kashmir');
        
SELECT * FROM PACKET;

INSERT INTO TRUCK
	(T_NO, DRIVER_NAME) VALUES
		(101, 'Sukanta'),
        (102, 'Krisnha'),
        (103, 'Chottu'),
        (104, 'Modhu');
        
INSERT INTO PACKET
	(P_NO, C_NO, T_NO, WEIGHT, DESTINATION) VALUES
		(1, 1, 101, 4, 'Guskara'),
        (2, 2, 102, 1, 'Bombay'),
        (3, 6, 103, 2, 'Kashmir'),
        (4, 3, 102, 5, 'Dubai'),
        (5, 5, 103, 8, 'London');
        
INSERT INTO PACKET
	(P_NO, C_NO, T_NO, WEIGHT, DESTINATION) VALUES
		(8, 8, 104, 1, 'Kashmir'),
        (9, 8, 104, 1, 'Kashmir'),
        (10, 7, 104, 1, 'Guskara');

SELECT * FROM CUSTOMER;

-- Q: NAME OF CUSTOMERS, WHO HAVE SENT AT LIST ONE PACKET OF WEIGHT MORE THAN 1KG TO BOMBAY
SELECT C.C_NAME, P.WEIGHT, P.DESTINATION
FROM CUSTOMER AS C, PACKET AS P
WHERE P.C_NO=C.C_NO AND P.WEIGHT>1 AND P.DESTINATION='Bombay';

-- Q. NAME OF THE ALL CUATOMERS WHOSE PACKETS WERE DELIVERED A DRIVER WHOSE NAME IS RAJA
SELECT C.C_NAME, T.DRIVER_NAME
FROM CUSTOMER AS C, TRUCK AS T, PACKET AS P
WHERE P.C_NO = C.C_NO AND P.T_NO = T.T_NO AND T.DRIVER_NAME='Krisnha';

-- Q. NAME OF ALL CUSTOMERS WHOSE TOTAL(INDIVIDUAL) SHIPMENTS ARE LESS THAN ONE KG
-- ANS BY PREM SANIA
SELECT * FROM (
SELECT C.C_NAME, SUM(P.WEIGHT) SUM_IS
FROM customer C, PACKET P
WHERE C.C_NO = P.C_NO
GROUP BY C.C_NAME)WHERE SUM_IS < 3;
-- ANS BY SUMIT ROUNAK
SELECT C.C_NAME, SUM(P.WEIGHT)
FROM CUSTOMER C, PACKET P
WHERE C.C_NO = P.C_NO
GROUP BY C.C_NAME
HAVING SUM(P.WEIGHT) < 3;