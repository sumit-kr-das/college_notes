create or replace FUNCTION findMax(x IN number, y IN number)  
RETURN number 
IS
    z number; 
BEGIN 
   IF x > y THEN 
      z:= x; 
   ELSE 
      Z:= y; 
   END IF;  
   RETURN z; 
END; 
/