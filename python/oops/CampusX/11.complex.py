class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i
    def __str__(self):
        return "{} + {}i".format(self.real,self.imag)
    def __add__(self,other):
        temp_real = self.real + other.real
        temp_imag = self.imag + other.imag
        return "{} + {}i".format(temp_real,temp_imag)
    def __sub__(self,other):
        temp_real = self.real - other.real
        temp_imag = self.imag - other.imag
        return "{} + {}i".format(temp_real,temp_imag)
    def __mul__(self,other):
        res = complex(self.real, self.imag) * complex(other.real, other.imag)
        temp_real = res.real
        temp_imag = res.imag
        return "{} + {}i".format(temp_real,temp_imag)
    def __eq__(self,other):
        if(self.real == other.real and self.imag == other.imag):
            return True
        else:
            return False

n1 = Complex(2,5)
n2 = Complex(4,3)

print("Given two complex numbers are:")
print(n1)
print(n2)
print()

print("Addition",n1+n2)
print("Subtraction",n1-n2)
print("Multiplication",n1*n2)
print("Equality",n1==n2)