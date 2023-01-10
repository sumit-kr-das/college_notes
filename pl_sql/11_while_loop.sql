SET SERVEROUTPUT ON;

DECLARE
    ter BOOLEAN:=TRUE;
    temp NUMBER:=0;
    ans NUMBER:=0;
BEGIN
    WHILE ter LOOP
        temp:=temp+1;
        ans:=temp*19;
        DBMS_OUTPUT.PUT_LINE('19 * '||temp||' = '||ans);
        IF temp>=10 THEN
            ter:=FALSE;
        END IF;
    END LOOP;
END;
/