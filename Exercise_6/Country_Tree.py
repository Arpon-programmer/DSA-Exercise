class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        for cld in self.children:
            if cld == child and child.parent == cld.parent and child.data == cld.data:
                self.children.remove(cld)
                cld.parent = None
                break

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|---' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for cld in self.children:
                cld.print_tree()


def tree_builder():
    root = TreeNode('Country')
    india = TreeNode('India')
    bangladesh = TreeNode('Bangladesh')
    pakistan = TreeNode('Pakistan')
    usa = TreeNode('USA')
    canada = TreeNode('Canada')
    root.add_child(india)
    root.add_child(bangladesh)
    root.add_child(pakistan)
    root.add_child(usa)
    root.add_child(canada)

    delhi = TreeNode('Delhi')
    mumbai = TreeNode('Mumbai')
    chennai = TreeNode('Chennai')
    kolkata = TreeNode('Kolkata')
    bengaluru = TreeNode('Bengaluru')
    india.add_child(delhi)
    india.add_child(mumbai)
    india.add_child(chennai)
    india.add_child(kolkata)
    india.add_child(bengaluru)

    # Add sub-cities to Indian cities
    delhi.add_child(TreeNode('South Delhi'))
    delhi.add_child(TreeNode('North Delhi'))
    delhi.add_child(TreeNode('East Delhi'))
    delhi.add_child(TreeNode('West Delhi'))
    delhi.add_child(TreeNode('Central Delhi'))

    mumbai.add_child(TreeNode('Juhu'))
    mumbai.add_child(TreeNode('Bandra'))
    mumbai.add_child(TreeNode('Andheri'))
    mumbai.add_child(TreeNode('Dadar'))
    mumbai.add_child(TreeNode('Colaba'))

    chennai.add_child(TreeNode('T Nagar'))
    chennai.add_child(TreeNode('Adyar'))
    chennai.add_child(TreeNode('Velachery'))
    chennai.add_child(TreeNode('Anna Nagar'))
    chennai.add_child(TreeNode('Mylapore'))

    kolkata.add_child(TreeNode('Salt Lake'))
    kolkata.add_child(TreeNode('Park Street'))
    kolkata.add_child(TreeNode('Howrah'))
    kolkata.add_child(TreeNode('Dumdum'))
    kolkata.add_child(TreeNode('Behala'))

    bengaluru.add_child(TreeNode('Whitefield'))
    bengaluru.add_child(TreeNode('Koramangala'))
    bengaluru.add_child(TreeNode('Indiranagar'))
    bengaluru.add_child(TreeNode('MG Road'))
    bengaluru.add_child(TreeNode('Jayanagar'))

    dhaka = TreeNode('Dhaka')
    sylhet = TreeNode('Sylhet')
    rajshahi = TreeNode('Rajshahi')
    barisal = TreeNode('Barisal')
    chittagong = TreeNode('Chittagong')
    bangladesh.add_child(dhaka)
    bangladesh.add_child(sylhet)
    bangladesh.add_child(rajshahi)
    bangladesh.add_child(barisal)
    bangladesh.add_child(chittagong)

    # Add sub-cities to Bangladeshi cities
    dhaka.add_child(TreeNode('Gulshan'))
    dhaka.add_child(TreeNode('Dhanmondi'))
    dhaka.add_child(TreeNode('Banani'))
    dhaka.add_child(TreeNode('Mirpur'))
    dhaka.add_child(TreeNode('Uttara'))

    sylhet.add_child(TreeNode('Zindabazar'))
    sylhet.add_child(TreeNode('Ambarkhana'))
    sylhet.add_child(TreeNode('Kumarpara'))
    sylhet.add_child(TreeNode('Mirabazar'))
    sylhet.add_child(TreeNode('Shibganj'))

    rajshahi.add_child(TreeNode('Shaheb Bazar'))
    rajshahi.add_child(TreeNode('Talaimari'))
    rajshahi.add_child(TreeNode('Uposhahar'))
    rajshahi.add_child(TreeNode('Kazla'))
    rajshahi.add_child(TreeNode('Padma Residential Area'))

    barisal.add_child(TreeNode('Band Road'))
    barisal.add_child(TreeNode('Hospital Road'))
    barisal.add_child(TreeNode('Cox\'s Bazar Road'))
    barisal.add_child(TreeNode('Alekhanda'))
    barisal.add_child(TreeNode('Chak Bazar'))

    chittagong.add_child(TreeNode('Agrabad'))
    chittagong.add_child(TreeNode('GEC'))
    chittagong.add_child(TreeNode('Pahartali'))
    chittagong.add_child(TreeNode('Chawkbazar'))
    chittagong.add_child(TreeNode('Khulshi'))

    lahsore = TreeNode('Lahsore')
    islamabad = TreeNode('Islamabad')
    karachi = TreeNode('Karachi')
    quetta = TreeNode('Quetta')
    peshawar = TreeNode('Peshawar')
    pakistan.add_child(lahsore)
    pakistan.add_child(islamabad)
    pakistan.add_child(karachi)
    pakistan.add_child(quetta)
    pakistan.add_child(peshawar)

    # Add sub-cities to Pakistani cities
    lahsore.add_child(TreeNode('Gulberg'))
    lahsore.add_child(TreeNode('Model Town'))
    lahsore.add_child(TreeNode('DHA'))
    lahsore.add_child(TreeNode('Cantt'))
    lahsore.add_child(TreeNode('Johar Town'))

    islamabad.add_child(TreeNode('F-6'))
    islamabad.add_child(TreeNode('F-7'))
    islamabad.add_child(TreeNode('G-6'))
    islamabad.add_child(TreeNode('G-7'))
    islamabad.add_child(TreeNode('I-8'))

    karachi.add_child(TreeNode('Clifton'))
    karachi.add_child(TreeNode('Gulshan-e-Iqbal'))
    karachi.add_child(TreeNode('Korangi'))
    karachi.add_child(TreeNode('Lyari'))
    karachi.add_child(TreeNode('Malir'))

    quetta.add_child(TreeNode('Quetta Cantt'))
    quetta.add_child(TreeNode('Satellite Town'))
    quetta.add_child(TreeNode('Sariab Road'))
    quetta.add_child(TreeNode('Jinnah Town'))
    quetta.add_child(TreeNode('Hanna Lake'))

    peshawar.add_child(TreeNode('University Town'))
    peshawar.add_child(TreeNode('Hayatabad'))
    peshawar.add_child(TreeNode('Saddar'))
    peshawar.add_child(TreeNode('Kohat Road'))
    peshawar.add_child(TreeNode('Dabgari Gardens'))

    california = TreeNode('California')
    texas = TreeNode('Texas')
    florida = TreeNode('Florida')
    new_york = TreeNode('New York')
    washington = TreeNode('Washington')
    usa.add_child(california)
    usa.add_child(texas)
    usa.add_child(florida)
    usa.add_child(new_york)
    usa.add_child(washington)

    # Add sub-cities to US states
    california.add_child(TreeNode('Los Angeles'))
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('San Diego'))
    california.add_child(TreeNode('Sacramento'))
    california.add_child(TreeNode('San Jose'))

    texas.add_child(TreeNode('Houston'))
    texas.add_child(TreeNode('Dallas'))
    texas.add_child(TreeNode('Austin'))
    texas.add_child(TreeNode('San Antonio'))
    texas.add_child(TreeNode('Fort Worth'))

    florida.add_child(TreeNode('Miami'))
    florida.add_child(TreeNode('Orlando'))
    florida.add_child(TreeNode('Tampa'))
    florida.add_child(TreeNode('Jacksonville'))
    florida.add_child(TreeNode('Tallahassee'))

    new_york.add_child(TreeNode('New York City'))
    new_york.add_child(TreeNode('Buffalo'))
    new_york.add_child(TreeNode('Rochester'))
    new_york.add_child(TreeNode('Albany'))
    new_york.add_child(TreeNode('Syracuse'))

    washington.add_child(TreeNode('Seattle'))
    washington.add_child(TreeNode('Spokane'))
    washington.add_child(TreeNode('Tacoma'))
    washington.add_child(TreeNode('Vancouver'))
    washington.add_child(TreeNode('Bellevue'))

    ottawa = TreeNode('Ottawa')
    toronto = TreeNode('Toronto')
    vancouver = TreeNode('Vancouver')
    montreal = TreeNode('Montreal')
    quebec = TreeNode('Quebec')
    canada.add_child(ottawa)
    canada.add_child(toronto)
    canada.add_child(vancouver)
    canada.add_child(montreal)
    canada.add_child(quebec)

    # Add sub-cities to Canadian cities
    ottawa.add_child(TreeNode('Kanata'))
    ottawa.add_child(TreeNode('Nepean'))
    ottawa.add_child(TreeNode('Orleans'))
    ottawa.add_child(TreeNode('Barrhaven'))
    ottawa.add_child(TreeNode('The Glebe'))

    toronto.add_child(TreeNode('Scarborough'))
    toronto.add_child(TreeNode('North York'))
    toronto.add_child(TreeNode('Etobicoke'))
    toronto.add_child(TreeNode('Downtown Toronto'))
    toronto.add_child(TreeNode('York'))

    vancouver.add_child(TreeNode('Kitsilano'))
    vancouver.add_child(TreeNode('Richmond'))
    vancouver.add_child(TreeNode('Burnaby'))
    vancouver.add_child(TreeNode('Surrey'))
    vancouver.add_child(TreeNode('West End'))

    montreal.add_child(TreeNode('Plateau Mont-Royal'))
    montreal.add_child(TreeNode('Old Montreal'))
    montreal.add_child(TreeNode('Downtown Montreal'))
    montreal.add_child(TreeNode('Outremont'))
    montreal.add_child(TreeNode('Westmount'))

    quebec.add_child(TreeNode('Old Quebec'))
    quebec.add_child(TreeNode('Sainte-Foy'))
    quebec.add_child(TreeNode('Charlesbourg'))
    quebec.add_child(TreeNode('Limoilou'))
    quebec.add_child(TreeNode('Beauport'))
    return root
if __name__ == '__main__':
    root = tree_builder()
    root.print_tree()