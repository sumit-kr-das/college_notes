class PyCharm:
    def execute(self):
        print('Compiled')
        print('Running')

class VsCode:
    def execute(self):
        print('Spell Check')
        print('Auto Suggestion')
        print('Compiled')
        print('Running')


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()
newIde = VsCode()

laptop1 = Laptop()
laptop1.code(newIde)