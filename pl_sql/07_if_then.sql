SET SERVEROUTPUT ON;

DECLARE
    n NUMBER(10) := 10;
BEGIN
    IF n >= 5 THEN
        DBMS_OUTPUT.PUT_LINE('TRUE');
    END IF;
        DBMS_OUTPUT.PUT_LINE('OUTSIDE OF THE LOOP');
END;
/