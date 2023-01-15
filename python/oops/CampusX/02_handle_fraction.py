class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.deno = d

    def __str__(self):
        return "{}/{}".format(self.num,self.deno)

    def __add__(self, other):
        temp_num = self.num * other.deno + other.num * self.deno
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_num,temp_deno)

    def __sub__(self, other):
        temp_num = self.num * other.deno - self.deno * other.num
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_num, temp_deno)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_num, temp_deno)

    def __truediv__(self, other):
        temp_num = self.num * other.deno
        temp_deno = self.deno * other.num
        return "{}/{}".format(temp_num, temp_deno)



n1 = Fraction(2,4)
n2 = Fraction(3,5)

print(n1)
print(n2)
print("Addition: ",n1+n2)
print("Subtraction: ",n1-n2)
print("Multiplication: ",n1*n2)
print("Division: ",n1/n2)