# Append Size
def append_size(lst):
    lst.append(len(lst))
    return lst

print(append_size(["burgers", "salad", "cheeze"]))

# Append Sum
def append_sum(lst):
    i = 0
    while i <= 2:
        lst.append(lst[-2] + lst[-1])
        i += 1
    return lst

print(append_sum([1, 2, 3]))

# Larger List
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]
    
print(larger_list([20, 40, 50], [13, 26, 70, 45]))
