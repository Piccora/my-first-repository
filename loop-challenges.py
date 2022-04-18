# Divisble By Ten
def divisible_by_ten(nums):
    i = 0
    for items in nums:
        if items % 10 == 0:
            i += 1
    return i

print(print(divisible_by_ten([20, 25, 30, 35, 40])))

# Greetings
def add_greetings(names):
    lst_names = []
    for items in names:
        lst_names.append("Hello, " + items)
    return lst_names
    
print(add_greetings(["Owen", "Max", "Sophie"]))

# Delete Starting Even Numbers (Used solution)
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

# Odd Indices
def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Exponents
def exponents(bases, powers):
    lst_answer = []
    for items1 in bases:
        for items2 in powers:
            lst_answer.append(items1 ** items2)
    return lst_answer

print(exponents([2, 3, 4], [1, 2, 3]))

# Larger Sum
def larger_sum(lst1, lst2):
    total1 = 0
    total2 = 0
    for items1 in lst1:
        total1 += items1
    for items2 in lst2:
        total2 += items2
    if total1 >= total2:
        return lst1
    else:
        return lst2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Over 9000
def over_nine_thousand(lst):
    total = 0
    for items in lst:
        total += items
        if total > 9000:
            break
    return total

print(over_nine_thousand([8000, 900, 120, 5000]))

# Max Num
def max_num(nums):
    maximum = nums[0]
    for items in nums:
        if items > maximum:
            maximum = items
    return maximum

print(max_num([50, -10, 0, 75, 20]))

# Same Values
def same_values(lst1, lst2):
    matching_indices = []
    i = 0
    for items in lst1:
        if lst1[i] == lst2[i]:
            matching_indices.append(i)
        i += 1
    return matching_indices

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Reversed List
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[-int(index) - 1]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))