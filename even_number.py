# Python program to print all even numbers in a range
start = 2
end = 10

def even_range(start, end):
    """
        Print all even numbers from given list using for loop
    
    """
    list = []
    for item in range(start, end+1):
        if item % 2 == 0:
            list.append(item)
    return list

print(even_range(start, end))

def odd_range(start, end):
    """
        Print all even numbers from given list using for loop
    """
    list = []
    for item in range(start, end+1):
        if item % 2 != 0:
            list.append(item)
    return list

print(odd_range(start, end))