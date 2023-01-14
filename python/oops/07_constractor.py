class A:
    def __init__(self):
        print("Constractor of class A called")
    def features1(self):
        print('Feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')

class B(A):
    def __init__(self):
        super().__init__()
        print("Constractor of class B called")
    def features3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')

a1 = B()
