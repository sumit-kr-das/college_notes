class Employee:
    def __init__(self, emp_name, salary, position):
        self.emp_name = emp_name
        self.salary = salary
        self.position = position

    def info(self):
        print('Info of the Employee is', self.emp_name, self.salary, self.position)

    # operator overloading
    def __add__(self, other):
        return self.salary + other.salary

e1 = Employee('Sumit',1000000,'SDE')
e2 = Employee('Snehasis', 2000000,'SDE')

e1.info()
e2.info()

total_sal = e1+e2
print(total_sal)