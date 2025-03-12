def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


lst_1 = [4 , 5, 7 ]

lst_1 += [55]
lst_1 + [55]

print(lst_1)


