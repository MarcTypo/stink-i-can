'''
Write a function that returns a list that contains every other element of a list that is passed in as an argument. 
The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.
'''

# #solution using for loop 
def oddities(lst):
    new_list = []
    for index in range(len(lst)):
        if index % 2 == 0: 
            new_list.append(lst[index])
    return new_list

# #solution using while loop
def oddities(lst):
    index = 0
    new_list = []
    while index < len(lst):
        if index % 2 == 0:
            new_list.append(lst[index])
        index += 1
    return new_list


#solution using comprehension
def oddities(lst):
    return [ lst[index] for index in range(len(lst)) if index % 2 == 0 ]
            

print(oddities([2, 3, 4, 5, 6]) )
print(oddities([1, 2, 3, 4]) )
print(oddities(["abc", "def"]))
print(oddities([123])  )          
print(oddities([]) == [])              



