# Write a function that takes two strings as arguments,
# determines the length of the two strings, and then returns the result
# of concatenating the shorter string, the longer string, and the shorter string once again. 
# You may assume that the strings are of different lengths.


def short_long_short(str1, str2):
    if len(str1) > len(str2):
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1 

    return shorter_str + longer_str + shorter_str
    
    


# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

