# reverse the sorted list

test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

def reverse_sorted_list(list):
    """
        This function takes list arguments and return new revese sorted list.
    """
    for elements in list:
        elements.sort(reverse = True)
    
    return list

print(reverse_sorted_list(test_list))