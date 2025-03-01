#Welcome User 
#Ask for number 
#ask for second number 
#ask for 
# print operaion 


def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)

    except ValueError:
        return True 
    
    return False


prompt('Welcome to the Calculator. Please enter your first number')

prompt("What's your first number?")
number1 = input()

while invalid_number(number1):
    prompt('That does not look like a valid number.')
    number1 = input()

prompt('What is your second number? ')
number2 = input()

while invalid_number(number2):
    prompt('That does not look like a valid number.')
    number2 = input()

prompt('What operation would you like to perform?\n' 
       'Select 1) Add 2) Subtract 3) Multiply 4) Divide ')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must chose 1, 2, 3, or 4. ')
    operation = input()



match operation:

    case '1': #addition 
        output = int(number1) + int(number2)

    case '2': #subtract
        output = int(number1) - int(number2)

    case '3': #multiply
        output = int(number1) * int(number2)

    case '4': #divide 
        output =  int(number1) / int(number2)


print(f'The result is {output}')    






