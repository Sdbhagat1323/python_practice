#Python program to find smallest number in a list

list1 = [10, 20, 4, 6, 7, 1]

def find_small(list):
    """
        take list argument and return smallest element in list.
    """
    tem = list[0]
    for element in list:
        if element <= tem:
            tem = element

    return "The smallest element is {}".format(tem)

# print(find_small(list1))

def find_small2(list):
    """
        take list argument and return smallest element in list.
    """
    element = min(list)
    return "the smallest element in list is {}".format(element)

print(find_small2(list1))


def find_small3(list):
    """
        take list argument and return smallest element in list.
    """

    sorted_list = sorted(list)
    return "the smallest element in list is {}".format(sorted_list[0])

print(find_small3(list1))
