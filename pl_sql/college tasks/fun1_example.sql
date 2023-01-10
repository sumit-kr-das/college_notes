set serveroutput on;
DECLARE 
   a number; 
   b number; 
   c number; 

BEGIN 
   a:= &a; 
   b:= &b;  
   c := findMax(a, b); 
   dbms_output.put_line(' Maximum is ' || c); 
END; 
/ 