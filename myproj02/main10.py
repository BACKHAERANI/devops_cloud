def get_max_number(number_list):
    number = number_list[0]
    for current_number in number_list:
        if current_number > number:
            number = current_number
    return number


def get_max_index(number_list):
    number = number_list[0]
    index = 0
    max_index = 0
    for current_number in number_list:
        if current_number > number:
            number = current_number
            max_index = index
        index += 1
    return max_index


numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_number(numbers))
print(get_max_index(numbers))
