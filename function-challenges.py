# Tenth Power
def tenth_power(num):
    return num ** 10

print(tenth_power(2))

# Square Root
def square_root(num):
    return num ** 0.5

print(square_root(16))

# Win Percentage
def win_percentage(wins, loses):
    return (wins / (wins + loses)) * 100

print(win_percentage(5, 5))

# Average
def average(num1, num2):
    return (num1 + num2) / 2

print(average(1, 100))

# Remainder
def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)

print(remainder(15, 14))

# First Three Multiples
def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3

print(first_three_multiples(10))

# Tip
def tip(total, percentage):
    return (total * percentage) / 100

print(tip(10, 25))

# Bond, James Bond
def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))

# Dog Years
def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))

# All Operations
def lots_of_math(a, b, c, d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return(((a + b) * (c - d)) % a)
    
print(lots_of_math(1, 2, 3, 4)) 