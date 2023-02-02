set serveroutput on;
declare
    var_n varchar2(30);
    cursor cur_sor(params varchar2 := 4) is
    select first_name from worker
    where worker_id > params;
begin
    open cur_sor;
    loop
        fetch cur_sor into var_n;
        exit when cur_sor%NOTFOUND;
        dbms_output.put_line(var_n);
    end loop;
    close cur_sor;
end;
/