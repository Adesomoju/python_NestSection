#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list and a tuple which contains every number

print('\t pls, separated by a comma')

user_input = input('input your values: ')
list_value = user_input.split(',')
tuple_value = tuple(list_value)

print(list_value)
print(tuple_value)

