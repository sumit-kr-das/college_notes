set serveroutput on;
DECLARE
    CURSOR cur_var(params number) IS
    select first_name, last_name from worker
    where worker_id < params;
BEGIN
    for L_IDX in cur_var(5) loop
        DBMS_OUTPUT.PUT_LINE(L_IDX.first_name||' '||L_IDX.last_name);
    end loop;
end;
/