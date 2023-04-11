class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
    def print(self):
        if self.head is None:
            raise Exception("Linked list is empty")
            return
        itr = self.head
        temp = ''
        while itr:
            temp += str(itr.data) + ' --> '
            itr = itr.next
        print(temp)

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_beginning(5)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)

    ll.print()