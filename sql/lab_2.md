#### Query 1: For creating s table where s_no is primary key:(master table) 
```sql
$ create table s(s_no number(5) primary key , s_name varchar(20),city varchar(20),status char(1));
```

#### Query 2: For creating p table where p_no is primary key:(master table)
```sql
$ create table p(p_no number(5) primary key , p_name varchar(20),color varchar(40),weight number(10));
```

#### Query 3: creating sp table where sp is child table of 's' and 'p'
```sql
$ create table sp(s_no number(5) , p_no number(5) references p(p_no), qty number(5));
```
```sql
$ alter table sp add foreign key(s_no) references s(s_no);
```

#### Query 4 : for create user level constants(use for data restrictions)
- User can not enter any city except durgapur, asansol, burdwan
```sql
$ alter table s add(constraints ss_c check(city in('Burdwan','Durgapur', 'Asansol')));
```

##### ```check``` is keyward for set the user level constant 
- constraints is the keyword for creating the constant who will store the restrictions details in the constant name ss_c
- ss_c is the constant name(variable name) for this restriction
<br/>
#### Query 5 : User shound have to enter quantity between 10 to 100

```sql
$ alter table sp add constraints sp_c check (qty between 10 and 100);
``` 

- sp_c is the constant name for this restriction
#### Query 5 : s_name should not null from the s table
```sql
$ alter table s add constraints s_c check (s_name is Not Null);
```

- s_c is the constant name for this restriction

#### Query 6: p_name should be unique of p table

```sql
$ alter table p add constraints p_c UNIQUE(p_name);
```

#### query 7: For inserting multiple values  =>
```sql
$ insert into s(table_name) values (&s_no , '&s_name', '&city', '&status');
```

```
Enter for value s_no : 
Enter for value s_name :
Enter for value city :
Enter for value statys :
```

```sql
$ / 
```

#### Query 8 : show the swevice provider name where city is Durgaupr
```sql
$ Select s_name from s where city='Durgapur' ;
```

#### Query 9: show the product name where weight less than 100 and weight is greater than 200 and color ='Grey'
```sql 
$ select p_name from p where weight > 100 and weight <200 and color ='Grey';
```

#### Qyery 10 :(Delete all the Red color product)
```sql
$ delete from p where color ='Red';
```

#### Query 11 : (Name shoud start with a or A)
```sql
$ select s_name from s where s_name like 'a%' or  s_name like '%A' ;
```

#### Query 12 : Show the supplier names that as 4 letters
```sql
$ select s_name from s where length (s_name)=4 ;
```
