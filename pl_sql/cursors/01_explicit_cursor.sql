SET SERVEROUTPUT ON;

DECLARE
    v_name VARCHAR2(30);
    -- DECLARE THE CURSOR
    CURSOR my_cursor IS
    SELECT first_name FROM worker
    WHERE worker_id < 5;
BEGIN
    OPEN my_cursor;
    LOOP 
        FETCH my_cursor INTO v_name;
        DBMS_OUTPUT.PUT_LINE(v_name);
        EXIT WHEN my_cursor%NOTFOUND;
    END LOOP;
    CLOSE my_cursor;
END;
/

