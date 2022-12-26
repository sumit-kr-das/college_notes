#### Query 1: Get the supplier name and city that supply product p1
```sql
    $ select s_name, city 
    from s,p,sp
    where s.s_no and p.p_no = sp.p_no and p_name = "p";
```

#### Query 2: Get the color of the product, supply by Ajay
```sql
    $ select color 
    from s,p,sp
    where s.s_no = sp.s_no and p.p_no = sp.p_no and s_name = "ajay";
```

#### Query 3: Get the supplier name who supply product p1 with quantity < 100
```sql
    $ select s_name 
    from s,p,sp
    where s.s_no = sp.s_no and p.p_no = sp.p_no and p_name = "p" and qty<100;
```

#### Query 4: Increase the product p1 weight of mouse by 10%
```sql
    $ update p
    set weight = weight + ( weight * 10 / 100 )
    where p_name = "mouse";
```