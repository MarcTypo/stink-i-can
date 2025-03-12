# Given a number and a list, determine whether the number is included in the list.


numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

#Solution 1
def check_numbers(lst , target):
    return target in lst


#Solution 2 
def check_numbers(lst , target):
    for element in lst: 
        if element == target:
            return True
    return False 



print(check_numbers(numbers, number1))

print(check_numbers(numbers, number2))

