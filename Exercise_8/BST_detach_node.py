class BinarySeacrhTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySeacrhTreeNode(data)
        if self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySeacrhTreeNode(data)
    def find_min(self):
        return self.left.find_min() if self.left else self.data
    def find_max(self):
        return self.right.find_max() if self.right else self.data
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
    def remove_child(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.remove_child(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.remove_child(val)
        else: # val == self.data
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            elif self.right is None and self.left is None:
                return None
            else: # self.right and self.left
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.remove_child(min_val)
        return self
def build_tree(elements):
    root = BinarySeacrhTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = [i for i in range(234,321)]
    root = build_tree(elements)
    print('In',root.in_order_traversal())
    print('Pre',root.pre_order_traversal())
    print('Post',root.post_order_traversal())
    root.remove_child(242)
    root.remove_child(300)
    print('In',root.in_order_traversal())
    print('Pre',root.pre_order_traversal())
    print('Post',root.post_order_traversal())
    print(root.find_min())
    print(root.find_max())