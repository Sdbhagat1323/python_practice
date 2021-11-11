# Maximum of two numbers in Python

a = 2
b = 4
c = 6


def findMaxNum(first_number, second_number):
    """
        takes two arrguments and return maximum number.
    """
    if first_number > second_number:
        return first_number
    elif first_number < second_number:
        return second_number
    else:
        return "they are equal.."

# print(findMaxNum(a, b))

def methodTwo(first_number, second_number):
    """
         takes two arrguments and return maximum number.
    
    """
    max_num = max(first_number, second_number)
    return max_num


# print(methodTwo(a, b))

a = 2
b = 10
c = 6

def methodThree(first_number, second_number, third_number):
    """
        takes three arrguments and return maximum number.
    
    """
    if (first_number > second_number) and ( first_number > third_number ):
        return first_number
    elif (second_number > first_number) or ( second_number > third_number):
        return second_number
    else:
        return third_number


print(methodThree(a,b,c))