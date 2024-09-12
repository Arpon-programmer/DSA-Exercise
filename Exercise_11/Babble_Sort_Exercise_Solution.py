def babble_sort(elements, key):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                elements[j+1][key], elements[j][key] = elements[j][key], elements[j+1][key]
                swapped = True
            if not swapped:
                break

elements = [
    {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]
babble_sort(elements, key='name')
print(elements)