class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        itr = self.head
        llstr = ''
        while itr:
            llstr = llstr+str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    def insert_multiple_val(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1;
            itr = itr.next
        return count
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index !")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    def insert_at(self, index_at, data):
        if index_at<0 or index_at>self.get_length():
            raise Exception("Invalid index")
        if index_at == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index_at - 1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.insert_at_begining(3)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    
    # ll.insert_multiple_val(['sumit','snehasis','dipali'])
    # ll.print()
    # print(ll.get_length())
    # ll.remove_at(2)
    # ll.print()
    # ll.insert_at(0,"shoyeb")
    # ll.insert_at(2,"pritam")
    ll.print()
