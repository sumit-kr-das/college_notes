set SERVEROUTPUT on
declare
    n number;
    s number:=0;
    r number;
    len number;
    m number;
begin
    for a in 1..500 loop
        m:=a;
        n:=a;
        len:=length(to_char(n));
        s:=0;
        while(n>0) loop
            r:=mod(n,10);
            s:=s+power(r,len);
            n:=trunc(n/10);
        end loop;
        
        if m=s then
            dbms_output.put_line('a='||to_char(a));
        end if;
    end loop;
end;
/