#Programmatically determine whether 42 lies between 10 and 100, inclusive. 
# Do the same for the values 100 and 101.




def check_number(num):
    return num in range(10,101)



print(check_number(42))
print(check_number(100))
print(check_number(101))
