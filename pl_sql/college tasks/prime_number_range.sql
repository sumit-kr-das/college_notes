set serveroutput on
declare
    temp number := 0;
    starting number := &enter_starting_number;
    ending number := &enter_ending_number;
    i int;
    j int;
begin
    for j in starting..ending loop
        temp := 0;
        for i in 2..j-1 loop
            if mod(j,i) = 0 then
                temp := temp + 1;
            end if;
        end loop;
        if temp=0 then
            DBMS_OUTPUT.PUT_LINE('Number is prime '||j);
        else
            DBMS_OUTPUT.PUT_LINE('Number is not prime '||j);
        end if;
    end loop;
end;
/