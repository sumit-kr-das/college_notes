create or replace FUNCTION isDigitSum(x IN number)  
RETURN number 
IS
    	z number:=0; 
BEGIN 
   while x!=0 
	LOOP
	   r:=mod(x,10);
	   z:=z+r;
	   x:=x/10;
	END LOOP
   RETURN z; 
END; 
/