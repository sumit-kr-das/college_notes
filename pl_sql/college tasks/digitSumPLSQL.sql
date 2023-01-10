set serveroutput on;
DECLARE
	p number :=&EnterNumber;
	s number :=0;
BEGIN
    	s:=isDigitSum(p);
	dbms_output.put_line('Sum of the digits of number='||s);
END;
/