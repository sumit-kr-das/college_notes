class stack:
    def __init__(self, Maxsize):
        self.top = -1
        self.MS = Maxsize
        self.arr = [None]*Maxsize

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.MS-1

    def push(self, ele):
        if self.isFull():
            print("Full")
        else:
            self.top += 1
            self.arr[self.top] = ele

    def pop(self):
        if self.isEmpty():
            print("empty")
        else:
            ele = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return ele

    def peek(self):
        return (self.arr[self.top])



s = stack(10)

operators = ['(', ')', '+', '-', '*', '/', '%', '^']
exp = "ABC*+"
for i in exp:
    if i.isalpha():
        s.push(i)
    elif i in operators:
        A = s.pop()
        B = s.pop()
        EXP = "("+B+i+A+")"

        print(EXP)
        s.push(str(EXP))

