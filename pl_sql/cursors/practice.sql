declare
    cursor cur_var is
    select salary from worker
    for update;

    num int;
begin 
    for a in cur_var loop
        