-- Anchored Datatype [%TYPE]
-- => Datatype which you assign to a variable basrd on a datatype object

set serveroutput on;
declare
    -- variable_name db_name.attribute_name%TYPE;
    worker_name worker.first_name%TYPE;
begin
    select first_name into worker_name from worker
    where worker_id = 1;
    dbms_output.put_line(worker_name);
end;
/