# finding the length of differnt list

l1 = [12, 35, 9, 56, 24]
l2 = [1, 2, 3]

def findLength(list):
    count = 0
    for element in list:
        count += 1
    return count

print(findLength(l2))
print(len(l1))