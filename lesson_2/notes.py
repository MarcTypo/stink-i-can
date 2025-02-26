
# greeting = 'hello'

# def change(message):
#     return message.upper()

# change(greeting)
# print(greeting)

# #problem 1 

# var = 10

# def function1():
#     print(var)

# function1()

# def function2():
#     var = 20
#     print(var)

# function2()
# print(var)


# #problem 2 
# lst = [1, 15, 24]

# def function1():
#     print(lst)

# function1()

# def function2():
#     lst[0] = 100
#     print(lst)

#     def function3():
#         lst1 = [1, 2, 3]
#         print(lst1)

# function2()
# function3()

# #nextproblem 

# lst = [1, 15, 24]

# def function1():
#     print(lst)

# function1()

# def function2():
#     lst[0] = 100

#     def function3():
#         lst = [1, 2, 3]

#     function3()
#     print(lst)

# function2()
# print(lst)



# # What does it print and why? what concept does the code snippet demonstrate?

# ages = {
#     "dimo": 31,
#     "olena": 32,
#     "tetiana": 28
# }

# def get_val_of_dimo(info):
#     try:
#         # info['ivan']
#         return info['ivan']
#     except KeyError:
#         return "Typo"

# print(get_val_of_dimo(ages))


names = ['kim', 'joe', 'sam']
for _ in names:
    print('Got a name!')