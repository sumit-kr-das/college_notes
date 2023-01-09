set serveroutput on;
declare
    v_salary number(8) := 12000;
    a int;
    b int;  
    c int;
begin
    a:=&a;
    b:=&b;
    c:=a+b;
    dbms_output.put_line('sum '||c);
    dbms_output.put_line('Salary of the employee is '|| v_salary);
end;
/