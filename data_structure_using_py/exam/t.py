class Stack:
    def __init__(self,maxsize):
        self.Top=-1
        self.MS=maxsize
        self.arr=[None]*maxsize
        
    def isempty(self):
        return self.Top==-1
    def isfull(self):
        return self.Top==self.MS-1
    def push(self,ele):
        if self.isfull():
            print("full")
        else:
            self.Top+=1
            self.arr[self.Top]=ele
    def pop(self):
        if self.isempty():
            print("empty")
        else:
            ele=self.arr[self.Top]
            self.Top-=1
            return ele
    def peek(self):
        if not self.isempty():
            return(self.arr[self.Top])

def evaluate(str):
    stack = Stack(10000)
    for i in range(len(str)-1, -1, -1):
        if str[i].isdigit():
            stack.push(int(str[i]))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if str[i] == "+":
                result = operand1 + operand2
            elif str[i] == "-":
                result = operand1 - operand2
            elif str[i] == "*":
                result = operand1 * operand2
            elif str[i] == "/":
                if operand2==0 :
                    print("Divide by zero")
                else:    
                    result = operand1 / operand2
            elif str[i] == "%":
                result = operand1 % operand2
            elif str[i] == "^":
                result = operand1 ^ operand2
                
            stack.push(result)
    return stack.pop()
    
str = "%*/*90-/50+23^1251520"
print(evaluate(str))