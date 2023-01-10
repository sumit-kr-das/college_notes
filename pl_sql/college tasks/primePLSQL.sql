set serveroutput on;
DECLARE
	p number :=&EnterNumber;
	flag int:=0;
	
BEGIN
    	flag:=isPrime(p);
	if flag=0 then
		dbms_output.put_line('Prime');
	else
		dbms_output.put_line('Not Prime');
	end if;
END;
/