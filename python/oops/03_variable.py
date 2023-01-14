# In OOPs there are two different types of variable in py
# a. instance variable
# b. static variable or class variable

class Car:
    weels = 4
    def __init__(self):
        self.mil = 10;
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8;

Car.weels = 5

print("Features of the cars", c1.weels, c1.mil, c1.com)
print("Features of the cars", c2.weels, c2.mil, c2.com)