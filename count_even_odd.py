# Python program to count Even and Odd numbers in a List

list1 = [2, 7, 5, 64, 14]

def count_even_odd(list):
    """
        take one list argument and return number even element and odd elements

    """
    even = 0
    odd = 0

    for element in list:
        if element % 2 == 0:
            even += 1
        else:
            odd += 1
    return "even count is {} and odd count is {}".format(even, odd)

print(count_even_odd(list1))

# using lambda expression

def count_even_odd_method_two(list1):
    """
        Using lambda expression
    """
    odd_count = len(list(filter((lambda x: x%2== 0), list1)))
    even_count = len(list(filter((lambda x: x%2 != 0), list1)))
    return "even count is {} and odd count is {}".format(odd_count, even_count)


print(count_even_odd_method_two(list1))

# using list comprehasion

def count_even_odd_method_three(list):
    """
        using list comprihension
    """
    even_count = len([num for num in list if num%2==1 ])
    odd_count = len([num for num in list if num%2!= 1])
    return "even count is {} and odd count is {}".format(odd_count, even_count)


print(count_even_odd_method_three(list1))









