'''
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.
'''

def prompt(message):
    print(f'==> {message}')

def area_sq_meters(side1, side2):
    return side1 * side2

while True:
    prompt('Enter the length of the room in meters. ')   #eror handling 
    length = input()

    prompt('Enter the width of the room in meters. ')
    width = input()

    prompt(f'Would you like the measurement type in meters or feet? Entet m/f')
    measurement = input()

    square_meters = area_sq_meters(int(length), int(width))
    square_feet = square_meters * 10.7639


    if measurement == 'meters' or 'm':
        prompt(f'Your room in sqaure metets is {square_meters} square meters.')
    elif measurement == 'feet' or 'f':
        prompt(f'Your room in square feet is {square_feet} square feet. ')

    prompt(f'Do you want to enter another measurement?')
    answer = input()

    if answer and answer[0].lower() != 'n':   #need to work on the looping for asking again 
        break   









