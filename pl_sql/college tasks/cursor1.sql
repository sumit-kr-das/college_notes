set serveroutput on;
declare
 a s1.id%type;
 b s1.marks%type;
 cursor c1 is select * from s1 order by marks desc;
 c number;
begin
 open c1; 
 c:=&position;
 loop
     fetch c1 into a,b;
     Exit When c1%notfound;
     if(c1%rowcount=c) then
     
		dbms_output.put_line(c1%rowcount||' '||a||' '||b);
     end if;
     EXIT WHEN c1%rowcount=c;
 end loop;
 close c1; 
end;
/