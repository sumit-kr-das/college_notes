/* Q.Find the employees  
   who's salary is more than
   the average salary earned by all employees */

USE ORG;
SELECT * FROM worker;

SELECT AVG(salary) FROM worker; -- 506250.0000

SELECT * 
FROM worker
WHERE salary > (SELECT AVG(salary) FROM worker);

SELECT w.*
FROM worker w
JOIN (SELECT AVG(salary) sal FROM worker) avg_sal
ON w.salary > avg_sal.sal;

/*
	TYPES OF SUBQUERY: 
		A. SCALAR SUBQUERY => always returns one row one column
        B. MULTIPLE ROW SUBQUERY
        C. CORRELATED SUBQUERY
*/

-- A. SCALAR SUBQUERY
SELECT AVG(salary) FROM worker;

-- B. MULTIPLE ROW SUBQUERY
-- TYPES OF MULTIPLE ROW SUBQUERY:
-- B.1 SUBQUERY WHICH RETURNS MULTIPLE COLUMNS & MULTIPLE ROWS
-- B.2 SUBQUERY WHICH RETURNS ONLY 1 COLUMN & 1 ROW

-- Q. FIND THE EMPLOYEES WHO EARNS THE HEIGHEST SALARY IN EACH DEPARTMENT

-- SALARY IN EACH DEPARTMENT
SELECT department, MAX(salary)
FROM worker
GROUP BY department;

-- B.1 SUBQUERY WHICH RETURNS MULTIPLE COLUMNS & MULTIPLE ROWS

SELECT * 
FROM worker 
WHERE (department, salary) in (
	SELECT department, MAX(salary)
	FROM worker
	GROUP BY department
);

-- B.2 SUBQUERY WHICH RETURNS ONLY 1 COLUMN & 1 ROW

-- Q. FIND THE DEPARTMENT WHO DO NOT HAVE ANY EMPLOYEES

SELECT * 
FROM department 
WHERE department_name NOT IN (SELECT DISTINCT department_name FROM employee);

-- C. CORRELATED SUBQUERY
-- SUBQUERY WHICH IS RELATED TO THE OUTER QUERY

-- Q. FIND THE EMPLOYEES IN EACH DEPARTMENT WHO EARN MORE THAN THE AVERAGE 
-- SALARY IN THAT DEPARTMENT

SELECT * 
FROM worker w1
WHERE salary > (
	SELECT AVG(salary) 
	FROM worker w2
	WHERE W2.department = W1.department );




