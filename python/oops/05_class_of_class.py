class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop() # way to accessing the inner class

    def show(self):
        print("Details of the student is",self.name, self.roll)
        self.lap.show();

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.ram = '8GB'
        def show(self):
            print("Laptop specs is ", self.brand, self.cpu, self.ram)

stu1 = Student('Sumit',51)
stu2 = Student('Snehasis',12)

stu1.show();
stu2.show();

# stu1.lap.brand()