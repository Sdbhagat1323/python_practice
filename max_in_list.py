# Python program to find largest number in a list


list1 = [10, 20,100, 4]

def find_max(list):
    """
        take one list argument and return maximun in list.
    
    """
    tem = list[0]
    for element in list:
        if element > tem:
            tem = element

    return "the maximum number is {}".format(tem)

print(find_max(list1))