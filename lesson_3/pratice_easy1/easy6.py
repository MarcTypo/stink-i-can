# Determine whether the name Dino appears in the strings below -- check each string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def check_target(str,target):
    return target in str


print(check_target(str1 , 'Dino'))
print(check_target(str2 , 'Dino'))