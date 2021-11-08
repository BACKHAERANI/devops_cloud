def make_powered_list(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers


def make_powered_list2(numbers):
    make_porwer = lambda number: number ** 2
    return list(map(make_power, numbers))

    # new_numbers=[]
    # for number in numbers:
    #     new_numbers.append(number**2)
    # return new_numbers
