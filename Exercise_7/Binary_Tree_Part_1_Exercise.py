class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return
        elif self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
    def find_min(self):
        return self.left.find_min() if self.left else self.data
    def find_max(self):
        return self.right.find_max() if self.right else self.data
    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum
        # left_sum = self.left.calculate_sum() if self.left else 0
        # right_sum = self.right.calculate_sum() if self.right else 0
        # return self.data + left_sum + right_sum
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
    def pre_order_traversal(self):
        elements = []
        # base
        elements.append(self.data)
        # left
        if self.left:
            elements += self.left.pre_order_traversal()
        # right
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    def post_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.post_order_traversal()
        # right
        if self.right:
            elements += self.right.post_order_traversal()
        # base
        elements.append(self.data)
        return elements
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    elements = [i for i in range(168,564)]
    BST = build_tree(elements)
    print(BST.find_min())
    print(BST.find_max())
    print(BST.calculate_sum())
    print(BST.in_order_traversal())
    print(BST.pre_order_traversal())
    print(BST.post_order_traversal())