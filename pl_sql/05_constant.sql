-- syntax
-- constant_name CONSTANT datatype(dw) := value;
-- * We must initialized a constant at its declaration 

set serveroutput on;
declare
    val_pi constant number(7,6) := 3.141592;
    my_weight constant number(7,2) not null default 40.35;
begin
    dbms_output.put_line(val_pi);
    dbms_output.put_line(my_weight);
end;
/