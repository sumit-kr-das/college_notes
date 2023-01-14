# a = 10;
# b = 20
# print(a+b)
# print(int.__add__(a,b))

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other_self):
        m1 = self.m1 + other_self.m1
        m2 = self.m2 + other_self.m2
        s3 = Student(m1,m2)
        return s3

s1 = Student(50,56)
s2 = Student(54,78)

s3 = s1+s2       # -> Student.__add__(s1,s2)

print(s3.m1)