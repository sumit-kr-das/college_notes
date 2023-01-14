class School:
    name = "Dr B C Roy Engineering College"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # Instance Methods
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # Class Methods
    @classmethod
    def schoolName(cls):
        return cls.name
    # Static Methood
    @staticmethod
    def info():
        print("This is MCA Department")

student1 = School(45,55,69)
student2 = School(55,88,96)

print(student1.avg())
print(School.schoolName())
School.info()