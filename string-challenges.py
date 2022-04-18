# Count Letters
def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    counter = 0
    characters = []
    for letter in word:
        if letter in letters and letter not in characters:
            counter += 1
            characters.append(letter)
    return counter

print(unique_english_letters("mississippi"))

# Count X
def count_char_x(word, x):
    counter = 0
    for letter in word:
        if letter == x:
            counter += 1
    return counter

print(count_char_x("mississippi", "m"))

# Count Multi X (Solution used)
def count_multi_char_x(word, x):
    splits = word.split(x)
    return(len(splits) - 1)

print(count_multi_char_x("mississippi", "iss"))

# Substring Between
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    if start_index != -1 and end_index != -1:
        return word[start_index + 1: end_index]
    else:
        return word
    
print(substring_between_letters("apple", "p", "e"))

# X Length
def x_length_words(sentence, x):
    splits = sentence.split()
    for word in splits:
        if len(word) < x:
            return False
    return True

print(x_length_words("i like apples", 2))

# Check Name
def check_for_name(sentence, name):
    splits = sentence.split()
    for word in splits:
        title_word = word.title()
        if title_word == name:
            return True
    return False

print(check_for_name("My name is Jamie", "Jamie"))

# Every Other Letter
def every_other_letter(word):
    new_string = []
    for letter in range(0, len(word), 2):
        new_string.append(word[letter])
    combined_new_string = "".join(new_string)
    return combined_new_string

print(every_other_letter("Codecademy"))

# Reverse
def reverse_string(word):
    new_string = ""
    for letter in range(-1, -len(word) - 1, -1):
        new_string += word[letter]
    return new_string

print(reverse_string("Codecademy"))

# Make Spoonerism
def make_spoonerism(word1, word2):
    first_character1 = word1[0]
    first_character2 = word2[0]
    remaining_characters1 = word1[1:]
    remaining_characters2 = word2[1:]
    spoonerism = first_character2 + remaining_characters1 + " " + first_character1 + remaining_characters2
    return spoonerism

# Add Exclamation
def add_exclamation(word):
    if len(word) < 20:
        for letter in range(20 - len(word)):
            word += "!"
    else:
        return word
    return word

print(add_exclamation("Codecademy"))
