# 1. До завдання, в якому ви реалізовували телефонну книгу,
# додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX
import re
import json


def ubd_dict(data_j):
    data_j = json.dumps(data_j)
    with open('phone_book.json', 'w+') as new_file:
        new_file.write(data_j)
    return


def r_dict():
    with open('phone_book.json', 'r+') as file:
        text = file.read()
        if text == '':
            return {}

        else:
            json_data = json.loads(text)
            return json_data


while True:
    user_input = input('\n Select and enter a command \n'
                       '(stats, add, delete, list, show): ')
    print(user_input)

    try:
        file = open('phone_book.json')
    except FileNotFoundError:
        print('File not found, created a new phone book')
        with open('phone_book.json', 'x'):
            pass

    phone_book = r_dict()

    # stats: кількість записів
    # add: додати запис
    # delete <name>: видалити запис за іменем (ключем)
    # list: список всіх імен в книзі
    # show <name>: детальна інформація по імені

    try:
        if user_input == "add":
            try:
                add_input = input("enter a name and number: ")
                add_split = add_input.split()
                name = add_split[0]
                num =add_split[1]
            except:
                print("Invalid data entered, please try again")

            try:
                v_namb = re.fullmatch(r'(0|380|\+380)(\d{9})', num)
                str_v_namb = str(v_namb[0])
                add_sub = phone_book.get(name)

                if add_sub == None:
                    phone_book[name] = str_v_namb
                    print("The subscribers " + add_split[0] + " is added to the phone book")
                    ubd_dict(phone_book)

                else:
                    print("a subscriber with the name " + name + " already exists, try another name")

            except:
                print("wrong number dialed")


        elif user_input == "stats":
            len_dct = str(len(phone_book))
            print("there are " + len_dct + " subscribers in this phone book")


        elif user_input == "list":
            sub_list = list(phone_book.keys())
            all_sub = ""
            for key_dct in sub_list:
                if all_sub == "":
                    all_sub = key_dct
                else:
                    all_sub = all_sub + ', ' + key_dct
            print("All subscribers : " + all_sub)

        if phone_book == {}:
            print("Sorry, phone book is empty or you entered the wrong request")


        else:
            if user_input == "show":
                show_input = input("enter a name: ")
                show_sub = phone_book.get(show_input)
                if show_sub != None:
                    str_num = str(phone_book.get(show_input))
                    print("Name " + show_input + " number " + str_num)
                else:
                    print("The subscribers " + show_input + " does not exist")

            elif user_input == "delete":
                del_input = input("enter a name: ")
                del_sub = phone_book.get(del_input)
                if del_sub != None:
                    print("The subscribers " + del_input + " removed from the phone book")
                    del phone_book[del_input]
                    ubd_dict(phone_book)
                else:
                    print("The subscribers " + del_input + " does not exist")


    except ValueError:
        print("Sorry invalid request, try again")
