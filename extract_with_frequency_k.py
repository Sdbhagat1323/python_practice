# Extract elements with Frequency greater than K

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3

def extract_element(list, k):
    """
        take two parameters and return the one list as per k values.
    """
    res = dict((i, list.count(i)) for i in list)
    k_dic = []
    [k_dic.append(key) for key, value in res.items() if value >= K]
    return "the key which values greater than k are {}".format(k_dic)

print(extract_element(test_list, K))
    