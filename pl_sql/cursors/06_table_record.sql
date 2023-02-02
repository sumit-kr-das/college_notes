set serveroutput on;
declare 
    v_emp worker%rowtype;
begin
    select * into v_emp from worker
    where worker_id = 2;
    dbms_output.put_line(v_emp.first_name||' '||v_emp.last_name);
    dbms_output.put_line(v_emp.salary);
end;
/