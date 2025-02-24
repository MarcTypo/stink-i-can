# Write a program that asks the user to enter an integer greater 
# than 0, then asks whether the user wants to determine 
# the sum or the product of all numbers 
# between 1 and the entered integer, inclusive.

def calculate_product(num): 
    total = 1 
    for i in range (1, num + 1):
        total *= i 
    return total

def calculate_sum(num):
    total = 0
    for i in range (1, num + 1):
        total += i
    return total 
    

num = int(input(f'Enter a number greater than 0.  '))
choice = input(f'Enter "s" to compute the sum, or "p" to compute the product. "')


if choice == 's' or choice  == 'sum':
    print(calculate_sum(num))
elif choice  == 'p' or choice == 'product':
    print(calculate_product(num))
else:
    print(f'You did not reply with p/s.')







    
    




