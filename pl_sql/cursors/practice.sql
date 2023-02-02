set serveroutput on
DECLARE
    CURSOR cur_var IS
    SELECT first_name, last_name FROM worker
    WHERE worker_id < 3;
BEGIN
    FOR L_IDX IN cur_var LOOP
        DBMS_OUTPUT.PUT_LINE(L_IDX.first_name||' '||L_IDX.last_name);
    END LOOP;
END;
/