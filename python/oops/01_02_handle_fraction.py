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

n1 = Fraction(2,4)
n2 = Fraction(3,5)

print(n1)
print(n2)
print(n1+n2)