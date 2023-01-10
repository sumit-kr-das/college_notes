create or replace FUNCTION isPrime(x IN number)
RETURN number
IS
	i int ;
	flag int:=0;
	
BEGIN
	for i in 2..(x+1)
	LOOP
	 if mod(x,i)=0 then
		flag:=1;
	 	exit;
	 end if;
	END LOOP;
	return flag;
END;
/