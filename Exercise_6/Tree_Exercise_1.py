class Tree_Node:
    def __init__(self,name,designation):
        self.data = {
            'name':name,
            'designation':designation
        }
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
    def print_tree(self,demand):
        spaces=' '*self.get_level()*3
        prefix=spaces+'|__' if self.parent else ''
        if demand.lower() in ['name', 'designation']:
            print(prefix+self.data[demand])
        elif demand.lower()=='both':
            print(f"{prefix}{self.data['name']} ({self.data['designation']})")
        for cld in self.children:
            cld.print_tree(demand)
def build_management_tree():
    ceo=Tree_Node('Nilupul','CEO')
    cto=Tree_Node('Chinmay','CTO')
    infrastructure_head=Tree_Node('Vishwa','Infrastructure Head')
    cloud_manager=Tree_Node('Dhaval','Cloud Manager')
    app_manager=Tree_Node('Abhijit','App Manager')
    application_head=Tree_Node('Aamir','Application Head')
    hr_head=Tree_Node('Gels','HR_Head')
    recruitment_manager=Tree_Node('Peter','Recruitment Manager')
    policy_manager=Tree_Node('Waqas','Policy Manager')

    ceo.add_child(cto)
    ceo.add_child(hr_head)
    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)
    cto.add_child(infrastructure_head)
    cto.add_child(application_head)
    infrastructure_head.add_child(cloud_manager)
    infrastructure_head.add_child(app_manager)
    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy