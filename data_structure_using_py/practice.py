class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        istr = ''
        while itr:
            istr+=str(itr.data)+' -> '
            itr = itr.next
        print(istr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(8)
    ll.print()