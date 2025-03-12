famous_words = "seven years ago..."

# new_string = f'Four score and' + famous_words

# print(new_string)

new_famous = famous_words.split(" ").insert( 0,'Four score and')
print(new_famous)
