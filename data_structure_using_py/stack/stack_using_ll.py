class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        itr = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(itr != None):
                print(itr.data, end = "")
                itr = itr.next
                if(itr != None):
                    print(" -> ", end = "")
            return


st = Stack()
st.push(5)
st.push(4)
st.push(3)
st.push(2)
st.push(1)
print("All the elements inside a stack: ")
st.display()
print()
st.pop()
print("After pop: ")
st.display()
print()
print("After peek: ")
peekData = st.peek()
print(peekData)