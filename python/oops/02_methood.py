class Person:
    def __init__(self):
        self.name = 'sumit';
        self.age = 22;
    def compare(self, other):
        if(self.age == other.age):
            print("Age of the both person is same")
        else:
            print("Age of the other persion is not same")


per1 = Person();
per1.age = 21;
per2 = Person();

per1.compare(per2);