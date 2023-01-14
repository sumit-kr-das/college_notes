class A:
    def features1(self):
        print('Feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')

class B(A):
    def features3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')

class C(B):
    def features5(self):
        print('Feature 5 is working')
    def feature6(self):
        print('Feature 6 is working')

student1 = C();
student2 = C();

student1.features1()
student1.features3()