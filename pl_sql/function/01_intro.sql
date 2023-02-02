CREATE OR REPLACE FUNCTION aria_circle(radius NUMBER)
RETURN NUMBER IS
pi CONSTANT NUMBER(5,3) := 3.14;
area NUMBER(20,5);
BEGIN
    area := pi*(radius*radius);
    RETURN area;
END;
/