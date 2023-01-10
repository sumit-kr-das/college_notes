SET SERVEROUTPUT ON;

DECLARE
    str VARCHAR(15);
BEGIN
    str:= '&Enter_a_word';
    IF str='sumit' THEN
        DBMS_OUTPUT.PUT_LINE('This is sumit');
    ELSIF str='snehasis' THEN
        DBMS_OUTPUT.PUT_LINE('This is snehasis');
    ELSE
        DBMS_OUTPUT.PUT_LINE('sorry');
    END IF;
END;
/