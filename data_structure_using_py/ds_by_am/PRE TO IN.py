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
exp="-+P*QCD"
P=2;Q=3;C=1;D=9
exp_r=exp[::-1]
print(exp_r)
for i in exp_r:
           if i.isalpha():
                         s.push(i)
           elif i in operators:
                         A=s.pop()
                         B=s.pop()
                         EXP="("+A+i+B+")"
                         
                         
                         print(EXP)
                         s.push(str(EXP)) 


#obj=stack(len(exp))
            


























