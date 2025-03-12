'''''
How can you determine whether a given string ends with an exclamation mark (!)?
Write some code that prints True or False depending on whether the string ends with an exclamation mark. '''''


str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

#solution 1 
def ends_with(str):
    if str.endswith("!"):
        return True 
    return False


print(ends_with(str1))
print(ends_with(str2))

#solution 2 
def ends_with(str):
    if str[-1] == '!':
        return True
    return False


print(ends_with(str1))
print(ends_with(str2))

#solution 3 
def ends_with(str):
    if len(str1) - 1 == '!':
        return True
    return False


print(ends_with(str1))
print(ends_with(str2))


def ends_with(str):
    if str[len(str) -1] == '!':
        return True
    return False


print(ends_with(str1))
print(ends_with(str2))

