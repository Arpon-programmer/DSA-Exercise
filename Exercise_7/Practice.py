class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def search(self, data):
        if data == self.data:
            return "It's here..."
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return "It's not here..."
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return "It's not here..."
    def in_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        # base
        elements.append(self.data)
        # right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = ["John", "Mary", "David", "Emily", "Michael"]
    BST = build_tree(elements)
    print(BST.search('Mary'))
    print(BST.in_order_traversal())