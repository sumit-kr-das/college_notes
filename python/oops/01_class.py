class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Now the config is", self.ram, self.cpu)

com1 = Computer('i5',16)
com2 = Computer('Ryzen 5', 8)

# other way to calling constractor 
# Computer.config(com1)

com1.config()
com2.config()