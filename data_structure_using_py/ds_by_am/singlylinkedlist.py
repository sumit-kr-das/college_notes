class Node:
    def __init__(self, dv=None):
        self.data = dv
        self.next = None
    '''def isEmpty(self):
          return'''

    def append(self, dv):
        if self.data == None:
            self.data = dv
            return
        temp = self

        while temp.next != None:

            temp = temp.next

        newnode = Node(dv)
        temp.next = newnode

    # to give the string representation of the object
    def __str__(self):
        items = []
        if self.data == None:
            return str([])
        temp = self
        items.append(temp.data)
        while temp.next != None:
            temp = temp.next
            items.append(temp.data)
        return str(items)

    def length(self):
        count = 1
        temp = self
        while temp.next != None:
            count = count+1
            temp = temp.next
        return count

    # insertion at the beginning
    def insert_at_beg(self, dv):
        if self.data == None:
            self.data = dv
        else:
            newnode = Node(dv)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            self.next = newnode

    # insertion after a node,key-->after value,dv-->insert value
    def insert_after_a_node(self, dv, key):
        if self.data == None:
            return
        temp = self
        while temp.next != None:
            if temp.data == key:
                newnode = Node(dv)
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next
            # self.append(dv)
        return

    # insert at any position
    def insert_at_any_position(self, dv, pos):
        if pos == 1:
            self.insert_at_beg(dv)
        elif pos < 1:
            print("position is negative")
            return
        elif pos > self.length():
            print("out of length")
            return
        else:
            count = 1
            temp = self
            # print("count",self.count())
            while count < pos-1:
                temp = temp.next
                count += 1
            newnode = Node(dv)
            newnode.next = temp.next
            temp.next = newnode
        return

    def insert_before_a_node(self, dv, key):  # insert before a node
        if self.data == None:
            return
        if self.data == key:
            self.insert_at_beg(dv)
            return
        temp = self
        while temp.next.data != key:
            temp = temp.next
            if temp.next == None:
                return
            newnode = Node(dv)
            newnode.next = temp.next
            temp.next = newnode
            return

    def insert_at_last(self, dv):  # insert at the end
        if self.data == None:
            self.data = dv
        temp = self
        while temp.next != None:
            temp = temp.next
        newnode = Node(dv)
        temp.next = newnode
        newnode.next = None
        return
### ------------------------------------------------------------deletion-------------------------------------------------------------------------------------###

    def delete_at_the_beg(self):  # delete at the beginning
        if self.data == None:
            return
        if self.next == None:
            self.data = None
            return
        else:
            self.data = self.next.data
            self.next = self.next.next
            return

    def delete_at_the_last(self):  # delete at the last
        if self.data == None:
            return
        if self.length() == 1:
            self.data = None
            return
        temp = self
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return

    def delete_after_a_node(self, key):  # delete after a node
        if self.data == None or self.data == key:
            return
        if self.next == None:
            return
        temp = self
        while temp.data != key:
            if temp.next == None:
                return
            temp = temp.next
        if temp.next == None:
            return
        temp.next = temp.next.next

    def delete_before_a_node(self, key):  # delete before a node
        if self.data == None or self.data == key:
            return
        if self.next == None:
            return
        if self.next.data == key:
            self.delete_at_the_beg()
        temp = self
        while temp.next.next.data != key:
            if temp.next.next.next == None:
                return
            temp = temp.next
        temp.next = temp.next.next

    def delete_at_any_pos(self, pos):  # delete at any position
        if self.data == None:
            return
        if pos < 1:
            return
        if pos > self.length():
            return
        if pos == 1:
            self.delete_at_the_beg()
            return
        if pos == self.length():
            self.delete_at_the_last()
            return
        count = 1
        temp = self
        while count < pos-1:
            temp = temp.next
            count += 1
        temp.next = temp.next.next

    def delete_particular_node(self, key):  # delete a particular node
        if self.data == None:
            return
        if self.data == key:
            self.delete_at_the_beg()
            return
        temp = self
        while temp.next.data != key:
            if temp.next.next == None:
                print(key, "not found")
                return
            temp = temp.next
        temp.next = temp.next.next

### -----------------------------------------------------------creating linked list------------------------------------------------------------------------###


sll = Node()
sll.append(10)
print(sll)
sll.append(20)
print(sll)

sll.append(30)
print(sll)
sll.insert_at_beg(50)
print("after insert in beginning:", sll)
sll.insert_at_any_position(200, 3)
print("insert at any position:", sll)
sll.insert_after_a_node(90, 50)
print("insert after a node:", sll)
sll.insert_after_a_node(190, 90)
print("insert after a node:", sll)
sll.insert_before_a_node(180, 190)
print("insert before a node:", sll)
sll.insert_at_last(500)
print("insert at the end of the list:", sll)
sll.delete_at_the_beg()
print("after deleting the 1st node:", sll)
sll.delete_at_the_last()
print("after deleting the last node:", sll)
sll.delete_after_a_node(10)
print("after a specific node:", sll)
sll.delete_before_a_node(10)
print("delete before a node:", sll)
sll.delete_at_any_pos(2)
print("delete at any position:", sll)
sll.delete_particular_node(1000)
print("delete particular node", sll)
