'''
Write a function that takes a string argument and returns a new string that 
contains the value of the original string 
with all consecutive duplicate characters collapsed into a single character.

loop through each character if the character is the same as next character save character. if it's not move to next
'''

def crunch(text):
    index = 0 
    crunch_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunch_text += text[index]

        index +=1 

    return crunch_text




# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')