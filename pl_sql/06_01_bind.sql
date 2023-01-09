-- syntax
-- VARIABLE variable_name DATATYPE;
SET SERVEROUTPUT ON;

VARIABLE v_bind VARCHAR2(10);
EXEC :v_bind := 'sumit';
-- PRINT :v_bind;

-- second way to initialized the bind variable
BEGIN
    :v_bind:='snehasis';
    DBMS_OUTPUT.PUT_LINE(:v_bind);
END;
/