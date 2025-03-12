'''
Write a function that takes a short line of text and prints it within a box.
'''

def print_in_box(message):
    horizontal_rule = f'+-{'-' * len(message)}-+'
    vertical_rule = f'| { " " * len(message)} |'
    message_line = f'| {message} |'
    print(horizontal_rule)
    print(vertical_rule)
    print(message_line)
    print(horizontal_rule)






print_in_box('To boldly go where no one has gone before.')
print_in_box('')