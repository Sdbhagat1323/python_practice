#swapning first and last elements

l1 = [12, 35, 9, 56, 24]
l2 = [1, 2, 3]
pos1 = 1
pos2 = 3

def swapElements(list_data):
    data = list_data
    data[0], data[-1] = data[-1], data[0]
    new_list = data
    return new_list

def swapMethod2(list):
    start, *middle, end = list
    list = end, *middle, start
    return list

# print(swapElements(l1)) 
# print(swapMethod2(l2)) 

# swap any element in list

def swapAnyElement(list, position1, position2):
    list[position1], list[position2] = list[position2], list[position1]
    new_list = list
    return new_list

print(swapAnyElement(l1, pos1, pos2))



    

