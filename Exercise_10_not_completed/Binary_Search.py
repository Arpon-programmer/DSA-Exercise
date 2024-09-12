import random


def linear_seacrh(element_list, element_to_find):
    for element in element_list:
        if element == element_to_find:
            return element_list.index(element)

def binary_search(element_list, element_to_find):
    element_list_1 = sorted(element_list) # Will be used for binary operations
    element_list_2 = sorted(element_list) # Will be used to represent target index
    
    if element_to_find >= element_list_2[0] and element_to_find <= element_list_2[-1]:
        def binary_operations(element_list_1, element_to_find):
            middle = len(element_list_1) // 2
            
            if element_list_1[middle] == element_to_find:
                return element_list_2.index(element_to_find)
            
            elif element_list_1[middle] < element_to_find:
                element_list_1 = element_list_1[middle+1:]
                return binary_operations(element_list_1, element_to_find)
            
            else:
                element_list_1 = element_list_1[:middle]
                return binary_operations(element_list_1, element_to_find)
            
        return binary_operations(element_list_1, element_to_find)
    
    else:
        return None

element_list = [100,200,300,400,500,600,700,800,900]
element_to_find = 400

print(f'Linear Search: {linear_seacrh(element_list, element_to_find)}')
print(f'Binary Search: {binary_search(element_list, element_to_find)}')