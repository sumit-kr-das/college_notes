set serveroutput on;

declare
    cursor cur_var is
    select first_name, last_name
    from worker
    where worker_id > 2;
begin
    for temp in cur_var loop
        dbms_output.put_line(temp.first_name ||' '|| temp.last_name);
    end loop;
end;
/