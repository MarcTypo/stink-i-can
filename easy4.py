#Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet


def calculate_area(side1,side2):
    return side1 * side2 

def square_meters_feet(area_in_meters):
    return area_in_meters * square_feet

length = float(input(f'Please enter the length of the room in meters:'))
width = float(input(f'Please enter the width of the room in meters:'))
square_feet = 10.7639
area_in_meters = calculate_area(length,width)
area_in_sqfeet = square_meters_feet(area_in_meters)


print(f'The length of your room is: {length} meters')
print(f'The width of your room is: {width} meters')
print(f'The area of your room in meters is: {area_in_meters} square meters')
print(f'The area of your room in square meters is:{square_meters_feet(area_in_meters)} square feet.')






    
