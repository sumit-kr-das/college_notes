class Customer:
    def __init__(self, c_name, c_age, c_add):
        self.name = c_name
        self.age = c_age
        self.add = c_add
    def info(self):
        print(f"Customer Info: {self.name} {self.age} {self.add}")

c1 = Customer("Sumit", 22, "kalkata")
c2 = Customer("Shehasis", 18, "kalkata")
c3 = Customer("Sk Shoyeb", 23, "burdwan")
c4 = Customer("Pritam", 26, "durgapur")

ll = [c1,c2,c3,c4]

for i in ll:
    i.info()