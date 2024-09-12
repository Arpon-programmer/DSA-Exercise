list = [['A', 'B', 'C', 'D', 'E', 'F'],['G', 'H', 'I'],['J', 'K','ab']]
len_list = []
for i in list:
    len_list.append(len(i))

print(list[len_list.index(min(len_list))])