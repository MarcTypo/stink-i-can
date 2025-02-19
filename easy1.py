#Write a function that takes one integer argument and returns 
# True when the number's absolute value is odd, False otherwise.

def absolute_value(num):
    if abs(num) % 2 != 0:
        return True 
    return False 



print(absolute_value(1))
print(absolute_value(2))
print(absolute_value(-2))
print(absolute_value(-3))

