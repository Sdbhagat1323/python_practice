# | Uncommon elements in Lists of List
# Difficulty Level : Medium

from types import resolve_bases


test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

def uncommon_list(list1, list2):
    """
        achieving the task of finding uncommon two list, in which each element
        is in itself a list. This is also a useful utility as this kind of task 
        can come in life of programmer if he is in the world of development.
        Lets discuss some ways to achieve this task.
    """
    rest_list = []
    for element in test_list1:
        if element not in list2:
            rest_list.append(element)

    for element in test_list2:
        if element not in list1:
            rest_list.append(element)
    return rest_list

# print(uncommon_list(test_list1, test_list2))
# use map function

ex_list = [13, 14, 15, 16]
newlist = list(map(lambda x: str(x) + "th", ex_list))
# print(newlist)

def uncommon_element(list1, list2):
    """
         achieving the task of finding uncommon two list, in which each element
        is in itself a list. This is also a useful utility as this kind of task 
        can come in life of programmer if he is in the world of development.
        Lets discuss some ways to achieve this task.

    """
    uncommon_list = set(map(tuple, list1)) ^ set(map(tuple, list2))
    converted_list = list(map(list, uncommon_list))

    return converted_list

print(uncommon_element(test_list1, test_list2))