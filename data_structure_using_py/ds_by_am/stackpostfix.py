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

'''s=stack(10)
s.push(12)
s.push(10)
s.push(23)
s.display()
print(s.pop()'''



postfix=""
s=stack(50)
infix="K+L-M*N+(O^P)*W/U/V*T+Q"
operators=['(',')','+','-','*','/','%','^']
preced={'^':3,'*':2,'/':2,'%':2,'+':1,'-':1}
for ch in infix:
            if ch.isalpha():
                        postfix += ch
            elif ch in operators:
                        if ch=='(':
                                    s.push(ch)
                        elif s.peek()== None or s.peek()=='(':
                                    s.push(ch)
                        elif ch==')':
                                    while s.peek()!='(':
                                                postfix += s.pop()
                                    s.pop()
                        elif preced[ch] > preced[s.peek()]:
                                    s.push(ch)
                        elif preced[ch] < preced[s.peek()]:
                                    while s.peek()!='(' and preced[ch] < preced[s.peek()]:
                                          postfix += s.pop()
                                    if s.peek()!='(' and preced[ch] == preced[s.peek()]:       
                                    
                                          postfix += s.pop()
                                    s.push(ch)
                        elif preced[ch] == preced[s.peek()]and ch == '^':
                                    s.push(ch)
                        elif preced[ch] == preced[s.peek()]and ch != '^':
                                      
                                    while s.peek()!= None and preced[ch] == preced[s.peek()]:
                                         postfix += s.pop()
                                    s.push(ch)
            print("{:>3}   {:<25} {}".format(ch,str(s),postfix))
while s.peek()!=None:
      postfix += s.pop()
print(postfix)






























