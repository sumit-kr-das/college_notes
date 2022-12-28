-- [2012][2015]
-- Employee (emp_name, street, city)
-- Works (emp_name, co_name, salary)
-- Company (co_name, city)
-- Managers (emp_name, manager_name)

-- Write the following queries in terms of Relational Algebraic expressions :
-- (i) Find the names of the employees who live in the 
-- same city of the company for which they work for [2015]
-- (ii) Find the name of the city where employee X works.

-- Write the following queries in terms of SQL :
-- (i) Find the names and cities for all employees who work for the company XYZ
-- (ii) Find the names of employees who earns 
-- Rs. 25,000, Rs. 23,000, or Rs. 21,000 as salary
-- (iii) Find the names of the employees whose names are 
-- exactly 7 character length and the third letter is "S".
-- Write the following queries in terms of Tuple Relational Calculus expressions :
-- (i) Find the names of all employees who work for IBM
-- (ii) Find the names of all employees who earn more than every employee of TCS .

-- (ii) FIND THE NAME OF THE ALL EMPLOYEES WHO DO NOT WORK FOR 'ABC' COMPANY [2015]
-- (iii) FIND THE COMPANY THAT HAS MOST EMPLOYEES [2015]
-- (iv) FIND THE NAME OF ALL EMPLOYEES WHO WORK FOR "ABC" COMPANY AND EARN MORE THAN 10,000 [2015]

-- [2013]
-- Loan : {cust_id, name, amount} 
-- Deposit : {cust_id, name, branch, balance} 

--  a) Represent the following using relational algebra : 
--  i) Names of customers having both loan & deposit accounts. 
--  ii) Names of customers having loan account, but no deposit account. 
--  iii) Find the branch name where customers having loan account and deposit accounts. Do not use 
-- standard natural join operator. 
--  b) Using tuple calculus, find the names of customers 
-- having deposit account in ‘xyz’ branch having 
-- balance > 7500. 

-- [2011]
-- Hotel (Hno, Name, Address) 
-- Room (Rno, Rtype, Hno, Price) 
-- Booking (Hno, Gno, Rno, DC from, DC to) 
-- Guest (Gno, GName, GAddress) 
--  a) Find the names of all guests who are staying in hotels 
-- either in Kolkata or Chennai. [ relational calculus ] 
-- b) Find the total number of guests in Hotel Taj. [Tuple 
-- Relational Calculus] 
--  c) List the number of rooms in each hotel. [ Domain 
-- Relational Calculus] 
--  d) Find the room with the maximum price. (SQL) 
--  e) Find the hotel with 2nd maximum no. of rooms. (SQL) 
