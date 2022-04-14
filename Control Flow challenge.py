# Large power
import telnetlib


def power_number(base, exponent):
    number = base ** exponent
    if number > 5000:
        return True
    else:
        return False
    
print(power_number(10, 3))

# Over Budget
def budget_check(budget, food_bill, electricity_bill, internet_bill, rent):
    spending = food_bill + electricity_bill + internet_bill + rent
    if spending > budget:
        return True
    else:
        return False
    
print(budget_check(500, 100, 100, 200, 0))

# Twice As Large
def comparison(num1, num2):
    if num1 > (num2 * 2):
        return True
    else:
        return False
    
print(comparison(1, 0))

# Divisible By Ten
def ten_division(num):
    if num % 10 == 0:
        return True
    else:
        return False
    
print(ten_division(11))

# Not Sum To Ten
def ten_total(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False
    
print(ten_total(2, 8))

# In Range
def in_range(num1, num2, num3):
    if num1 >= num2 and num1 <= num3:
        return True
    else:
        return False
    
print(in_range(3, 1, 2))

# Same Name
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
    
print(same_name("Long", "Long"))

# Always False
def contradiction(num):
    if num > 0 and num < 0:
        return True
    else:
        return False
    
print(contradiction(-1))

# Movie Review
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating <= 9:
        return "This one was fun."
    else:
        return "Outstanding!"
    
print(movie_review(10))

# Max Number
def max_number(num1, num2, num3):
    if num1 == num2 or num1 == num2 or num2 == num3:
        return "It's a tie!"
    elif num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
print(max_number(2, 3, 5))