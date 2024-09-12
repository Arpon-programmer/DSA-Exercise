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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root

if __name__ == '__main__':
    numbers = [151, 160, 158, 162, 147, 145, 153, 156, 155, 148, 146, 159, 161, 152, 163, 150, 144, 157, 149, 164, 154]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(158))