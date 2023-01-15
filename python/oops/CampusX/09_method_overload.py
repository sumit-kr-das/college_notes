# Method overloading is not exist in python, but we can do this using default argument
class Geometry:
    def area(self, radius):
        return 3.14 * radius * radius

    def area(self, length, bredth):
        return length * bredth

obj = Geometry()

print(obj.area(3, 4))