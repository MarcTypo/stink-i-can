'''
Write a program that prompts the user for two positive numbers (floating-point), 
then prints the results of the following operations on those two numbers: 
addition, subtraction, product, quotient, floor quotient, remainder, and power. 
Do not worry about validating the input.
'''


def prompt(message):
    print(f'==> {message}')

prompt('Enter a postive number.  ')
number1 = float(input())

prompt('Enter another positive number. ')
number2 = float(input())


prompt(f'{number1} + {number2} = {number1 + number2}')
prompt(f'{number1} - {number2} = {number1 - number2}')
prompt(f'{number1} * {number2} = {number1 * number2}')
prompt(f'{number1} // {number2} = {number1 // number2}')
prompt(f'{number1} % {number2} = {number1 % number2}')
prompt(f'{number1} ** {number2} = {number1 ** number2}')


