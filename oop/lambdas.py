l = lambda x: x > 5
print(l(10))

def alter(values, check):
    return [val for val in values if check(val)]

my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)

print(another_list)

list2 = list(filter(lambda x: x != 5, my_list))
print(list2)  # same as another_list!

list3 = [val for val in my_list if val != 5]
print(list3)  # same thing

def remove_numbers(value):
    # removes the numbers in a string
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)

