def babble_sort(elements, key):
    target_list = [element[key] for element in elements]
    sorted_list = []
    size = len(target_list)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if target_list[j] > target_list[j+1]:
                target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
                swapped = True
        if not swapped:
            break
    for element in target_list:
        for dct in elements:
            if dct[key] == element:
                sorted_list.append(dct)
    return sorted_list


elements = [
    {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]
sorted_list = babble_sort(elements, key='transaction_amount')
print(sorted_list)