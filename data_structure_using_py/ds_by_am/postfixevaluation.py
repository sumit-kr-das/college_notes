class stack:
            def __init__(self,Maxsize):
                        self.top=-1
                        self.MS=Maxsize
                        self.arr=[None]*Maxsize
            def isEmpty(self):
                        return self.top==-1
            def isFull(self):
                        return self.top==self.MS-1
            def push(self,ele):
                        if self.isFull():
                                    print("Full")
                        else:
                                    self.top+=1
                                    self.arr[self.top]=ele
            def pop(self):
                        if self.isEmpty():
                                    print("empty")
                        else:
                                    ele=self.arr[self.top]
                                    self.arr[self.top]=None
                                    self.top-=1
                                    return ele
            def peek(self):
                        return(self.arr[self.top])
            def __str__(self):
                        data=[]
                        for i in range(self.top+1):
                                    data.append(self.arr[i])
                        return str(data)
                        '''if self.isEmpty():
                                    print("empty")
                        else:
                                    for i in range(self.top+1):
                                                print(self.arr[i])'''

s=stack(10)
'''
s.push(12)
s.push(10)
s.push(23)
s.display()
print(s.pop()'''

operators=['(',')','+','-','*','/','%','^']
exp="PQC*+D-"
P=200;Q=300;C=100;D=900
for i in exp:
           if i.isalpha():
                         s.push(i)
           elif i in operators:
                         A=s.pop()
                         B=s.pop()
                         print(B," ",A)
                         if i=="+":
                                     val = eval(B)+eval(A)
                         elif i=="-":
                                     val = eval(B)-eval(A)
                         elif i=="*":
                                     val = eval(B)*eval(A)
                         elif i=="/":
                                     val = eval(B)/eval(A)
                         elif i=="%":
                                     val = eval(B)%eval(A)
                         elif i=="^":
                                     val = eval(B)**eval(A)
                         
                         print(val)
                         s.push(str(val)) 


#obj=stack(len(exp))
            


























