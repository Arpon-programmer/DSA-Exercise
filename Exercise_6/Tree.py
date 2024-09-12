# ট্রি নোডের ক্লাস
class TreeNode:
    def __init__(self, data):
        # ট্রি নোডের ডেটা
        self.data = data
        # ট্রি নোডের চাইল্ড নোডগুলির লিস্ট
        self.children = []
        # ট্রি নোডের প্যারেন্ট নোড
        self.parent = None

    def add_child(self, child):
        # চাইল্ড নোডকে প্যারেন্ট নোডে যোগ করে
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        # চাইল্ড নোডকে প্যারেন্ট থেকে অপসারণ করে
        for cld in self.children:
            if cld.data == child.data:
                self.children.remove(cld)
                cld.parent = None
                break

    def get_level(self):
        # ট্রি নোডের লেভেল (রুট থেকে নোডের দূরত্ব) পরিচালনা করে
        level = 0
        if self.parent:
            return self.parent.get_level() + 1
        else:
            return 0

    def print_tree(self):
        # ট্রি নোডের সব উপাদানকে প্রিন্ট করে
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

# ট্রি নোডের উদাহরণ তৈরি করে রিটার্ন করে
def build_node():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    mac = TreeNode('MacBook')
    surface = TreeNode("Surface")
    thinkpad = TreeNode("Thinkpad")

    laptop.add_child(mac)
    laptop.add_child(surface)
    laptop.add_child(thinkpad)

    cellphone = TreeNode("Cell Phone")
    iphone = TreeNode("iPhone")
    google_pixel = TreeNode("Google Pixel")
    vivo = TreeNode("Vivo")

    cellphone.add_child(iphone)
    cellphone.add_child(google_pixel)
    cellphone.add_child(vivo)

    tv = TreeNode("TV")
    samsung = TreeNode("Samsung")
    lg = TreeNode("LG")

    tv.add_child(samsung)
    tv.add_child(lg)

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    #laptop.remove_child(mac)  # চাইল্ড নোডকে অপসারণের জন্য এই লাইনটি আনকমেন্ট করুন
    return root

# প্রধান ফাংশন
if __name__ == '__main__':
    root = build_node()
    root.print_tree()