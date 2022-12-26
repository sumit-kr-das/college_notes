import math;
a=int(input())
b=int(input())
c=int(input())
D=((b*b)-4*a*c)

if(D>=0) :
     r1=(-b + (math.sqrt(D))/(2 * a))
     r2=(-b + (math.sqrt(D))/(2 * a))
     print("Root Real and unqual", r1,r2)
elif(D>0) :
    r1=(-b + (math.sqrt(D))/(2 * a))
    r2=r1;
    print("Root Real and Equal", r1,r2)    
else :
    print("Complex root")
