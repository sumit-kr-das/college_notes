SET SERVEROUTPUT ON;

DECLARE
    a NUMBER(10);
BEGIN
    a:= &Enter_a_no;
    IF MOD(a,2)=0 THEN
        DBMS_OUTPUT.PUT_LINE('EVEN');
    ELSE
        DBMS_OUTPUT.PUT_LINE('ODD');
    END IF;
END;
/