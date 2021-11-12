input_list = [1, 2, 2, 5,3,3,3, 8, 4, 4, 8]

def count_unique(list):
    """
        take list argument and return the unique value of each element.


    """
    list1 = []
    
    for item in list:
        if item not in list1:
            list1.append(item)
    return "the unique values in list is {}".format(len(list1))

print(count_unique(input_list)) 


# using counter module

from collections import Counter

def count_unique_method_two(list):
    """
        take one arguemant and use collection from counter to calculate the unqie values
    
    """
    value = Counter(list).keys()
    return len(value)

print(count_unique_method_two(input_list))


# to get how many time each element occurce

def count_occurance(list):
    """
        take list argument and return a dictionay to with the key value pair of the item occure in list.    
    
    """
    count_dic = Counter(list)
    return count_dic 

print(count_occurance(input_list))


# rewrite the counter for calculating the occurance.


def count_occurance_method_two(list):
    """
         take list argument and return a dictionay to with the key value pair of the item occure in list.    
    
    """
    count_dic = dict((i, list.count(i)) for i in list)

    return count_dic

# print(dict((i, input_list.count(i)) for i in input_list))

print(count_occurance_method_two(input_list))













