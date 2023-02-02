set serveroutput on;
DECLARE
    n number := & enter_no;
    temp number :=0 ;
    rem number;
    m number;
BEGIN
    m :=n;
    while n>0
    loop
    rem := mod(n,10);
    temp := (temp*10)+rem;
    n := trunc(n/10);
    end loop;
    if (m=temp) then
    dbms_output.put_line('Palindrome');
    else
    dbms_output.put_line('Not Palindrome');
    end if;
END;