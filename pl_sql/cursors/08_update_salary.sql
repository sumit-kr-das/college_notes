declare 
    cursor std is
    select salary from worker
    for update;

    inc number;
begin
    for a in std loop
    if a.salary > 300000 then 
        inc := .15;
    else
        inc := .10;
    end if;
    update worker set salary = salary+salary*inc where current of std;
    end loop;
end;
/