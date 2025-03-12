# Build a program that displays when the user will retire and how many years she has to work till retirement.

'''
Ask for current age 
retirement age 

calculate retirement year 
how much years left 
'''
import datetime
def prompt(message):
    print(f'==> {message}')
            

def calculate_retirement_age(current, retirement):
     retirement_year = (retirement - current_age) + current_year 
     return (f"It's {current_year}. You will retire in {retirement_year} \n"
     f'You only have {retirement - current_age} to go. ')



prompt('What is your age?')
current_age = int(input())


prompt('At what age would you like to retire?')
retirement_age = int(input())

current_year = datetime.datetime.now().year 

print(calculate_retirement_age(current_age , retirement_age))





