# Sum Values
def sum_values(my_dictionary):
    total = 0
    for values in my_dictionary.values():
        total += values
    return total

print(sum_values({10:1, 100:2, 1000:3}))

# Even Keys
def sum_even_keys(my_dictionary):
    total = 0
    for keys in my_dictionary.keys():
        if keys % 2 == 0:
            total += my_dictionary[keys]
    return total

print(sum_even_keys({1:5, 2:2, 3:3}))

# Add Ten
def add_ten(my_dictionary):
    for keys in my_dictionary.keys():
        my_dictionary[keys] += 10
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))

# Values That Are Keys
def values_that_are_keys(my_dictionary):
    values_keys = []
    for keys in my_dictionary.keys():
        for values in my_dictionary.values():
            if keys == values:
                values_keys.append(keys)
    return values_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))

# Largest Value
def max_key(my_dictionary):
    largest_value = float("-inf")
    largest_key = 1
    for keys, values in my_dictionary.items():
        if values > largest_value:
            largest_value = values
            largest_key = keys
    return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))

# Word Length
def word_length_dictionary(words):
    new_dict = {}
    for item in words:
        new_dict[item] = len(item)
    return new_dict

print(word_length_dictionary(["apple", "dog", "cat"]))

# Frequency Count (Used Solution)
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))

# Unique Values
def unique_values(my_dictionary):
    new_list = []
    total = 0
    for value in my_dictionary.values():
        if value not in new_list:
            new_list.append(value)
            total += 1
    return total

print(unique_values({0:3, 1:1, 4:1, 5:3}))

# Count First Letter
def count_first_letter(names):
    letters = {}
    for key, value in names.items():
        if key[0] not in letters:
            letters[key[0]] = 0
        letters[key[0]] += len(value)
    return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))