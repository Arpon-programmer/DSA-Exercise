class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        elif self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def remove_child(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.remove_child(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove_child(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.remove_child(min_val)
        return self
    def search(self,data):
        if data == self.data:
            return f"{data} is present in this BinarySearchTree."
        elif self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return f"{data} is not present in this BinarySearchTree."
        else:
            if self.right:
                return self.right.search(data)
            else:
                return f"{data} is not present in this BinarySearchTree."
    def find_max(self):
        return self.right.find_max() if self.right else self.data
    def find_min(self):
        return self.left.find_min() if self.left else self.data
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = [86,58765,464,224,6,3454,46346,32,3466,35564]
    root = build_tree(elements)
    print('Max',root.find_max())
    print('Min',root.find_min())
    print(root.search(32))
    print(root.search(100))
    print('In',root.in_order_traversal())
    print('Pre',root.pre_order_traversal())
    print('Post',root.post_order_traversal())
    root.remove_child(86)
    root.remove_child(464)
    root.remove_child(3466)
    print('In', root.in_order_traversal())
    print('Pre', root.pre_order_traversal())
    print('Post', root.post_order_traversal())