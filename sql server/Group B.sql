CREATE DATABASE groupb;
USE groupb;

-- TABLE STRUCTURE PCA1 GROUP B [2009]
-- HOTEL(H_NO, NAME, ADDRESS)
-- ROOM (R_NO, R_TYPE, H_NO, PRICE)
-- GUEST(G_NO, G_NAME, G_ADDRESS)
-- BOOKING (H_NO, G_NO, R_NO, NO_OF_DAYS) [Booking ( Hno,Gno,Rno,Dt_from,Dt_to )]

CREATE TABLE hotel(
	h_no INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(10)
);

INSERT INTO hotel 
	(h_no, name, address) VALUES
		(1, 'Taj','Kalkata'),
        (2, 'Matara','Durgapur'),
        (3, 'Hotel Dubai','Dubai'),
        (4, 'Oyo','Durgapur'),
        (5, 'Fantasy','Kashmir');
        
SELECT * FROM hotel;

CREATE TABLE room(
	r_no INT PRIMARY KEY,
    r_type VARCHAR(255),
    h_no INT,
    price INT,
    FOREIGN KEY(h_no) REFERENCES hotel(h_no) ON DELETE CASCADE
);

INSERT INTO room
	(r_no,r_type,h_no,price) VALUES
		(1,'Delux',1,1200),
        (2,'Delux',2,600),
        (3,'Delux',3,3800),
        (4,'Delux',4,900),
        (5,'Delux',5,1100);
        
INSERT INTO room
	(r_no,r_type,h_no,price) VALUES
		(6,'Delux',1,700),
        (8,'Delux',1,1800),
        (7,'Delux',2,6400);
        
SELECT * FROM room;

CREATE TABLE guest(
	g_no INT PRIMARY KEY,
    g_name VARCHAR(255),
    g_address VARCHAR(255)
);

INSERT INTO guest
	(g_no,g_name,g_address) VALUES
		(101,'Sumit Das','Delhi'),
        (102,'Snehasis Das','Kalakata'),
        (103,'Dipali Das','Guskara'),
        (104,'Debsishu Pal','Hydrabad'),
        (105,'Falguni Chak','Durgapur');
        
INSERT INTO guest
	(g_no,g_name,g_address) VALUES
		(106,'Ayan Dahara','Khana Jn'),
        (107,'Rounak Mukherjee','Banglore');
        
select * from guest;

CREATE TABLE booking(
	h_no INT,
    g_no INT,
    r_no INT,
    no_of_days INT,
    FOREIGN KEY(h_no) REFERENCES hotel(h_no) ON DELETE CASCADE,
    FOREIGN KEY(g_no) REFERENCES guest(g_no) ON DELETE CASCADE,
    FOREIGN KEY(r_no) REFERENCES room(r_no) ON DELETE CASCADE
);

INSERT INTO booking
	(h_no,g_no,r_no,no_of_days) VALUES
		(1,101,1,4),
        (2,102,2,1),
        (3,103,3,3),
        (4,104,4,2),
        (5,105,5,5);
        
INSERT INTO booking
	(h_no,g_no,r_no,no_of_days) VALUES
		(1,106,1,4),
        (1,107,2,1);

SELECT * FROM BOOKING;

-- Q1: FIND THE NAME OF ALL GUESTS WHO ARE STAYING IN HOTELS
--     EITHER IN KALKATA OR CHANNAI [ Relational Calculus ]

SELECT g.g_name,h.address 
FROM guest as g, hotel as h, booking as b
where h.h_no = b.h_no AND b.g_no = g.g_no 
and address IN('Durgapur','Dubai');

-- Q2: FIND THE TOTAL NO OF GUESTS IN TAJ HOTEL [ Tuple Relational Calculus ]
SELECT *
FROM booking AS b,hotel AS h;

SELECT b.g_no,COUNT(*) 
FROM booking AS b,hotel AS h
WHERE b.h_no = h.h_no
AND h.name = 'Taj';

-- Q2: LIST THE NUMBER OF ROOMS IN EACH HOTEL [ Domain Relational Calculus ]

SELECT h.name,COUNT(r.h_no)
FROM room AS r, hotel AS h
WHERE r.h_no = h.h_no
GROUP BY r.h_no;


-- Q3:  Find the room with the maximum price. [ SQL ]

SELECT price FROM room r1
WHERE 0 = (SELECT COUNT(distinct price) FROM room r2
WHERE r2.price > r1.price);

select * FROM ROOM;

-- Q4: Find the hotel with 2nd maximum no. of rooms. ( SQL )

SELECT name FROM hotel r1
WHERE 0 = (SELECT COUNT(distinct price) FROM room r2
WHERE r2.price > r1.price);
