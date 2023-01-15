class Person:
    def __init__(self):
        # __name is called private attribute
        self.__name = "Sumit Kumar Das"
        self.__age = 22
        self.__address = "Guskara"

    def getInfo(self):
        print(f"Name of the person is {self.__name} & Age is {self.__age} & Address is {self.__address}")

    def setInfo(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

per1 = Person()
per1.getInfo()
per1.setInfo("Snehasis Das", 18, "Kalkata")
per1.getInfo()