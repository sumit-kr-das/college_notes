-- MULTIPLICATION TABLE
SET SERVEROUTPUT ON;

DECLARE
    temp NUMBER := 0;
    mul NUMBER := 0;
BEGIN
    LOOP
        temp := temp+1;
        mul := temp*19;
        DBMS_OUTPUT.PUT_LINE('19 * '||temp||' = '||mul);
        EXIT WHEN temp >= 10;
    END LOOP;
END;
/
