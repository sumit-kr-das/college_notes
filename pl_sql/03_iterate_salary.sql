set serveroutput on;
declare
    v_salary number(10);
begin
    select salary into v_salary from worker
    where worker_id = 2;
    dbms_output.put_line('Id of worker 2 is '|| v_salary);
end;
/

declare
    first_emp_name varchar2(10);
    last_emp_name varchar2(10);
    emp_salary number(10);
begin
    select first_name,last_name,salary into first_emp_name,last_emp_name,emp_salary from worker
    where worker_id=2;
    dbms_output.put_line(first_emp_name||' '||last_emp_name||' salary is '||emp_salary);
end;
/