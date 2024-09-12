class Tree_Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def remove_child(self,child):
        for cld in self.children:
            if cld == child and child.parent == cld.parent and child.data == cld.data:
                self.children.remove(cld)
                cld.parent = None
                break
    def get_level(self):
        if self.parent:
            return self.parent.get_level() + 1
        else:
            return 0

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
def build_location_tree():
    glo_bal=Tree_Node('Global')
    india=Tree_Node('India')
    gujarat=Tree_Node('Gujarat')
    karnataka = Tree_Node('Karnataka')
    ahmedabad=Tree_Node('Ahmedabad')
    baroda=Tree_Node('Baroda')
    bangluru=Tree_Node('Bangluru')
    mysore=Tree_Node('Mysore')
    usa=Tree_Node('USA')
    new_jersey=Tree_Node('New Jersey')
    princeton=Tree_Node('Princeton')
    trenton=Tree_Node('Trenton')
    california=Tree_Node('California')
    san_francisco=Tree_Node('San Francisco')
    mountain_view=Tree_Node('Mountain View')
    palo_alto=Tree_Node('Palo Alto')

    glo_bal.add_child(india)
    india.add_child(gujarat)
    india.add_child(karnataka)
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)

    glo_bal.add_child(usa)
    usa.add_child(new_jersey)
    usa.add_child(california)
    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)
    california.add_child(san_francisco)
    california.add_child(mountain_view)
    california.add_child(palo_alto)
    return glo_bal

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(level=3)