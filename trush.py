
# LIST (mutable)

# create a list

# empty
# my_empty_list = []
# my_second_empty_list = list()

# from string

# my_name = "Oleksii"
# my_name_list = list(my_name)
# print(my_name)
# print(my_name_list)
#
# some_text = "This is a simple text"
# split_text = some_text.split()

# print(split_text)

# different types

# lst = ['Strint', 123, True, 1.23, 1.23, 1.23, 1.23]

# print(lst)

# list in list

# new_list = ['New list2', lst, 'New list', 'New list', 'New list', 'New list']

# print(new_list)
# print(new_list[0])
# print(new_list.index('New list'))

# for item in new_list:
#     if type(item) == list and 123 in item:
#         print(item.index(123))


# swap elements of the list

# intermediate = new_list[0]
# new_list[0] = new_list[1]
# new_list[1] = intermediate
# print(new_list)
# print(new_list[0])


# list append

# small_list = [1]
#
# small_list.append(1)
# print(small_list)
# small_list.append([1])
# print(small_list)
# small_list[2].append(2)
# print(small_list)


# list extend

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
# big_list.extend(other_list)
# print(big_list)

# merge lists

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
# third_list = big_list + other_list
# print(third_list)

# iteration

# my_numbers = [1, 2, 3, 4, 5]
#
# for item in my_numbers:
#     print(item)
#     print(my_numbers.index(item))


# indexes and slices [:::]

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(my_numbers)
# new_numbers = my_numbers[0:9]
#
# for item in new_numbers:
#     print(new_numbers.index(item))

last_index = len(my_numbers) - 1
# print(my_numbers[len(my_numbers) - 1])
# print(my_numbers[-1])
# print(my_numbers[9])
# print(my_numbers[-3])

# new_numbers = my_numbers[0:9:3]
# print(new_numbers)

# new_numbers = my_numbers[::3]
# print(new_numbers)

# new_numbers = my_numbers[::3]
# print(new_numbers)


# new_numbers = my_numbers[::-1]
# print(new_numbers)


# in list

# my_list = ['apple', 'banana', 1, True, False, 1.234]

# print('apple' in my_list)
# print(my_list.index('pear'))


# fruit = 'apple'
#
# if fruit in my_list:
#     print(f'The index of {fruit} is {my_list.index(fruit)}')
# else:
#     print(f'{fruit} in not in the list')


# DICT (mutable)

# === create a dict

# my_dict = {}
# my_second_dict = dict()

# === create a program to read, update and create spends by category

# my_spends = {
#     'travel': 0,
#     'food': 0,
#     'transport': 0,
# }

# print(my_spends.get('travel'))
# print(my_spends['travel'])

# print(my_spends['subscriptions'])
# print(my_spends.get('subscription'))

# while True:
#     user_input = input('Enter a command: ') # format "command amount category" commands: add, remove
#     split_input = user_input.split()
#
#     command = split_input[0]
#     amount = int(split_input[1])
#     category = split_input[2]
#
#     if my_spends.get(category) is None:
#         my_spends[category] = 0
#
#     if command == 'add':
#         my_spends[category] += amount
#     elif command == 'remove':
#         my_spends[category] -= amount
#     elif command == 'get':
#         print(my_spends.get(category))


# === create a dict from list of lists
# users_list = [
#     ["Tom Riddle", "+111123455"],
#     ["Bob", "+384767557"],
#     ["Alice", "+958758767"]
# ]


#
# print(dict(users_list))
# users_tuple = (
#     ["+111123455", "Tom"],
#     ["+384767557", "Bob"],
#     ["+958758767", "Alice"]
# )

# users_tuple = ['aa', 'bb', 'cc']

# print(dict(users_tuple))


# === get element by key: get() and []

# my_dict = {'first': 1, 'second': 2, 'third': 3}
# print(my_dict['first'])
# print(my_dict.get('first'))


# === update element by key: update and []

# my_dict = {'first': 1, 'second': 2, 'third': 3}
# my_dict['first'] = 10
# my_dict['fourth'] = 4
# print(my_dict)


# === dict keys(), values(), items()

# my_dict = {'first': 1, 'second': 2, 'third': 3}

# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# print(list(my_dict.keys()))

# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

# print(my_dict.items())

# for key, value in my_dict.items():
#     print(key)
#     print(value)

#
# dct = {'one': 1}
# dct.update({'one': 2})
# print(dct)


# dct.update({'one': 3, 'two': 2})
# print(dct)

# === delete items from dict: del

# del dct['one']
# print(dct)
# 0
# comments
# on
# commit
# 2312368
# LIST (mutable)

# create a list

# empty
# my_empty_list = []
# my_second_empty_list = list()

# from string

# my_name = "Oleksii"
# my_name_list = list(my_name)
# print(my_name)
# print(my_name_list)

# some_text = "This is a simple text"
# split_text = some_text.split()

# print(split_text)

# different types

# lst = ['Strint', 123, True, 1.23, 1.23, 1.23, 1.23]

# print(lst)

# list in list

# new_list = ['New list2', lst, 'New list', 'New list', 'New list', 'New list']

# print(new_list)
# print(new_list[0])
# print(new_list.index('New list'))

# for item in new_list:
#     if type(item) == list and 123 in item:
#         print(item.index(123))


# swap elements of the list

# intermediate = new_list[0]
# new_list[0] = new_list[1]
# new_list[1] = intermediate
# print(new_list)
# print(new_list[0])


# list append

# small_list = [1]
#
# small_list.append(1)
# print(small_list)
# small_list.append([1])
# print(small_list)
# small_list[2].append(2)
# print(small_list)


# list extend

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
# big_list.extend(other_list)
# print(big_list)

# merge lists

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
# third_list = big_list + other_list
# print(third_list)

# iteration

# my_numbers = [1, 2, 3, 4, 5]
#
# for item in my_numbers:
#     print(item)
#     print(my_numbers.index(item))


# indexes and slices [:::]

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(my_numbers)
# new_numbers = my_numbers[0:9]
#
# for item in new_numbers:
#     print(new_numbers.index(item))

# last_index = len(my_numbers) - 1
# print(my_numbers[len(my_numbers) - 1])
# print(my_numbers[-1])
# print(my_numbers[9])
# print(my_numbers[-3])

# new_numbers = my_numbers[0:9:3]
# print(new_numbers)

# new_numbers = my_numbers[::3]
# print(new_numbers)

# new_numbers = my_numbers[::3]
# print(new_numbers)


# new_numbers = my_numbers[::-1]
# print(new_numbers)


# in list

# my_list = ['apple', 'banana', 1, True, False, 1.234]

# print('apple' in my_list)
# print(my_list.index('pear'))


# fruit = 'apple'
#
# if fruit in my_list:
#     print(f'The index of {fruit} is {my_list.index(fruit)}')
# else:
#     print(f'{fruit} in not in the list')


# DICT (mutable)

# === create a dict

# my_dict = {}
# my_second_dict = dict()

# === create a program to read, update and create spends by category

my_spends = {
    'travel': 0,
    'food': 0,
    'transport': 0,
}

# print(my_spends.get('travel'))
# print(my_spends['travel'])

# print(my_spends['subscriptions'])
# print(my_spends.get('subscription'))

while True:
    user_input = input('Enter a command: ') # format "command amount category" commands: add, remove
    split_input = user_input.split()

    command = split_input[0]
    amount = int(split_input[1])
    category = split_input[2]

    if my_spends.get(category) is None:
        my_spends[category] = 0

    if command == 'add':
        my_spends[category] += amount
    elif command == 'remove':
        my_spends[category] -= amount
    elif command == 'get':
        print(my_spends.get(category))

    print(my_spends)




# === create a dict from list of lists
# users_list = [
#     ["Tom Riddle", "+111123455"],
#     ["Bob", "+384767557"],
#     ["Alice", "+958758767"]
# ]


#
# print(dict(users_list))
# users_tuple = (
#     ["+111123455", "Tom"],
#     ["+384767557", "Bob"],
#     ["+958758767", "Alice"]
# )

# users_tuple = ['aa', 'bb', 'cc']

# print(dict(users_tuple))


# === get element by key: get() and []

# my_dict = {'first': 1, 'second': 2, 'third': 3}
# print(my_dict['first'])
# print(my_dict.get('first'))


# === update element by key: update and []

# my_dict = {'first': 1, 'second': 2, 'third': 3}
# my_dict['first'] = 10
# my_dict['fourth'] = 4
# print(my_dict)


# === dict keys(), values(), items()

# my_dict = {'first': 1, 'second': 2, 'third': 3}

# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# print(list(my_dict.keys()))

# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

# print(my_dict.items())

# for key, value in my_dict.items():
#     print(key)
#     print(value)

#
# dct = {'one': 1}
# dct.update({'one': 2})
# print(dct)


# dct.update({'one': 3, 'two': 2})
# print(dct)

# === delete items from dict: del

# del dct['one']
# print(dct)