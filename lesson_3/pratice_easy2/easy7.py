# Write a one-liner to count the number of lower-case t characters in each of the following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

#Solution 1
print(statement1.count('t'))
print(statement2.count('t'))


#Solution 2 
def counting_letters(string , given_letter):
    result = 0
    for letter in string:
        if letter == given_letter:
            result += 1
    return result 

print(counting_letters(statement1 , 't'))
print(counting_letters(statement2 , 't'))
