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
    
print(larger_list([20, 40, 50, 38], [13, 26, 70, 45]))

# More Than N
def more_than_n(lst, item, n):
    count = lst.count(item)
    if count > n:
        return True
    else:
        return False
    
print(more_than_n([2, 4, 2, 6, 1, 2, 9], 2, 3))

# Combine Sort
def combine_sort(lst1, lst2):
    lst_new = lst1 + lst2   
    return sorted(lst_new)

print(combine_sort([4, 6, 2, 83, 82, 37, 19, 37, 30], [94, 1048, 82394823, 8305, 2, 734, 234]))

# Every Three Numbers
def every_three_numbers(start):
    return list(range(start, 101, 3))

print(every_three_numbers(99))

# Remove Middle
def remove_middle(lst, start, end):
    lst = lst[:start] + lst[end + 1:]
    return lst

print(remove_middle([1, 4, 6, 3, 7, 2, 7, 2, 7], 2, 5))

# More Frequent Item
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2
    
print(more_frequent_item([2, 2, 2, 2, 5, 5, 5, 5], 2, 5))

# Double Index
def double_index(lst, index):
    if (index + 1) > len(lst):
        return lst
    else:
        lst_new = lst[:index]
        remaining_lst = lst[index + 1:]
        lst_new.append(lst[index] * 2)
        new_new_lst = lst_new + remaining_lst
        return new_new_lst

print(double_index([3, 8, -10, 12], 2))

# Middle Item
def middle_element(lst):
    half_len = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        return ((lst[half_len] + lst[half_len - 1]) / 2) 
    else:
        return (round(lst[half_len]))
    
print(middle_element([5, 2, -10, -4, 4, 5, 6, 7]))