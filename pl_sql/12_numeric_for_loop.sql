SET SERVEROUTPUT ON;
DECLARE
BEGIN
    FOR counter IN 1..10 LOOP
        DBMS_OUTPUT.PUT_LINE(counter);
    END LOOP;
END;
/