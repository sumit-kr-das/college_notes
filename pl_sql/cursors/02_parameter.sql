SET SERVEROUTPUT ON;

DECLARE
    v_name VARCHAR2(30);
    CURSOR new_cursor(params_id VARCHAR2) IS
    SELECT first_name from worker 
    WHERE worker_id = params_id;
BEGIN
    OPEN new_cursor(1);
    LOOP 
        FETCH new_cursor INTO v_name;
        EXIT WHEN new_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_name);
    END LOOP;
    CLOSE new_cursor;
END;
/
