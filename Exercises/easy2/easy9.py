# Build a program that randomly generates and prints 
# Teddy's age. To get the age, 
# you should generate a random number between 20 and 100, inclusive.



import random

age = random.randint(20 ,100)

def generate_age(name = 'Teddy'):
    return f'{name} is {age} years old!'

def prompt(message):
    print(f'==> {message}')


prompt('What is your name?')
user_name = input().strip()

if user_name:
    print(generate_age(age))
else: 
    print(generate_age())





