# Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2, 
# so that the list becomes [1, 2, 4, 5].


numbers = [1, 2, 3, 4, 5]

# numbers.pop(2)
# print(numbers)


def pop_index(lst , given_index):
    index = 0 
    while index < len(lst):
        if given_index == index:
           lst.pop(index)
           print(index)
        index +=1 
    return lst




print(pop_index(numbers , 2))
    