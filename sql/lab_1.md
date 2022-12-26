#### Query 1: Create a new user
```sql
    $ create user USER_NAME identified by PASSWORD;
```


#### Query 2: Give all permissions for the created user
##### [you should be connected into your system account]
```sql
    $ grant all privileges to USER_NAME;
```


#### Query 3: Show all the tables
```sql
    $ select * from tab;
```


#### Query 4: Show Date from system
```sql
    $ select sysdate from dual;
```


#### Query 5: Calculate some arithmetic operation using sql
```sql
    $ select 2*3-4+6 from dual;
```


#### Query 6: Create a student table
```sql
    $ create table student(roll number(4),name varchar2(30),address varchar2(50),dob date,marks number(5,2));
```


#### Query 7: insert data into the student table
```sql
    $ insert into student values(1,'ayesha','durgapur','20-oct-01',89.75);
```


#### Query 8: Show the student table
```sql
    $ select * from student;
```


#### Query 8: Show the structure of the student table
```sql
    $ desc student;
```


#### Query 9: Select roll no, and student name from the student table
```sql
    $ select name, roll from student;
```


#### Query 10: Select name and roll whose name is sumit from student table
```sql
    $ select name, roll from student where name='sumit';
```


#### Query 11: Select name and roll whose marks is greater than 100 from student table
```sql
    $ select name, roll from student where marks<100;
```
