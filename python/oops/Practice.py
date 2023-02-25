class Node:
    def _init_(self,value):
        self.data = value 
        self.next = None #whenever node is created, in address part new node will hold null.

class LinkedList:
    #constractor
    def _init_(self):
        self.head = None
        self.n = 0 #counter to count number of nodes in the linkedlist

    #magic method to find length of linkedlist
    def _len_(self):
        return self.n

    def insert_head(self,value): #method to insert new node in the linked list
        new_node = Node(value) #creating new node
        new_node.next = self.head #creating link with new node, using linked list's head
        self.n = self.n+1 #whenever new node is connect, the counter of node will be incremented
    
    def _str_(self):
        curr = self.head #curr is pointer, pointing to head of linked list
        
        result = ''
        
        while curr !=None:
            result = result + str(curr.data) + '->' #this while loop will print every value of node in the linked list
            curr = curr.next #.next of every node already holding the address of next node
        return result[:-2]
    
    
L = LinkedList()
L.insert_head(4)
L.insert_head(5)
L.insert_head(6)
L.insert_head(8)
L.insert_head(9)
L.insert_head(10)
print(L)