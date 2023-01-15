class Customer:
    def __init__(self, name):
        self.name = name

def Greet(customer):
    customer.name = "Sumit"
    print(customer.name)


cus = Customer("Snehasis")

print(cus.name);

Greet(cus)

print(cus.name);