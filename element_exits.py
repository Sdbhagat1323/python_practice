l1 = [12, 35, 9, 56, 24]

def ifExists(list, element):
    """
        take two arguments one is list and second is element to be found
    """
    for item in list:
        if element == item:
            return True
        else:
            return False

                
print(ifExists(l1, 55))