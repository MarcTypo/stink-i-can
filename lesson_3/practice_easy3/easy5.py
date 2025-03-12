
# The following function unnecessarily uses two return statements 
# to return boolean values. Can you rewrite this function so it only has 
# one return statement and does not explicitly use either True or False?

#solution 1 
def is_color_valid(color):
    return color == "blue" or color == "green"

#solution 2
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    


#solution 3
def is_color_valid(color):
    return color in ['blue', 'green']