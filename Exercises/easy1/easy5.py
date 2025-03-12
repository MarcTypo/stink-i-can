#Create a simple tip calculator. 
# The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

bill = float(input('What is the bill? ' ))
tip = float(input('What is the tip percentage? ' ))/100

total = bill + (tip * bill )

print(f'The tips:${tip:.2f}')
print(f'The toal is ${total:.2f}')



