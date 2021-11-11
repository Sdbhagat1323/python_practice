# Count occurrences of an element in a list


lst = [15, 6, 7, 10, 12, 20,6, 10, 28, 10]
x = 10
y = 6

def count_occurrence(list, element):
    """
        takes two argument list and element which count is need to calculated
    """
    count = 0
    for item in list:
        if element == item:
            count += 1
    return count

# print(count_occurrence(lst, y))

# using count method,

def count_x(list, element):
    """
        using predifined functions to count the occurance.
    """
    num = list.count(element)
    return num

print(count_x(lst, x))