# Find sum and average of List in Python


l1 = [4, 5, 1, 2, 9, 7, 10, 8]


def average(l1):
    """
        take list argument and return average value
    """
    length_of_list = len(l1)
    avg = sum(l1)/ length_of_list

    return "The average value is {}".format(avg)

def average_method_2(l1):
    """
        take list argument and return average value
    """
    length_of_list = len(l1)
    count = 0
    for i in l1:
        count += i
    avg = count/length_of_list
    return "The avarage value is {}".format(avg)


print(average(l1))
print(average_method_2(l1))
