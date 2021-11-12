# List product excluding duplicates

list1 = [10, 20,100, 4, 4]

def get_uniques(list):
    """
        take list as an argument and return unique list.
    """
    res = []
    for item in list:
        if item not in res:
            res.append(item)

    return "the uniques element in list are {}".format(res)

print(get_uniques(list1))


def get_uniques_method_two(list):
    """
        take list argument and return unque list.
    """
    res = []
    [res.append(x) for x in list if x not in res]

    return "the uniques element in list are {}".format(res)
