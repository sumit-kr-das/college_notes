# Python program to
# demonstrate binary tree implementation
# using list

# class node represents a single node
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# constract a tree


class ConstructTree:
    # build a node
    def buildTree(self):
        # input a number from user
        rootData = int(input())
        # if user enter -1 the return Nonde
        if rootData == -1:
            return None
        # creation of root node
        root = Node(rootData)
        # make a new left node
        root.left = self.buildTree()
        # make a new right node
        root.right = self.buildTree()
        return root
    def preOrder(self, root):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)


if __name__ == "__main__":
    construct = ConstructTree()
    root = construct.buildTree()
    construct.preOrder(root)
