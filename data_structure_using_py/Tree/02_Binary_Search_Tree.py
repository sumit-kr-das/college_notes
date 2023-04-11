# Tutorial Link: https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                # you are not a leaf node
                self.left.add_child(data)
            else:
                # you are a leaf node
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                # you are not a leaf node
                self.right.add_child(data)
            else:
                # you are a leaf node
                self.right = BinarySearchTreeNode(data)
    def inorderTraversal(self):
        elements = []
        # visit the left tree
        if self.left:
            elements += self.left.inorderTraversal()
        # visit root node
        elements.append(self.data)
        # visite the right tree
        if self.right:
            elements += self.right.inorderTraversal()
        return elements
    def search(self, data):
        if self.data == data:
            return True
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False;

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    ele = [12,32,1,4,5,6,12,7]
    ele_tree = buildTree(ele)
    print(ele_tree.inorderTraversal())
    print(ele_tree.search(1))
