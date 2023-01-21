# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
#
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
# і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.

import json
import time



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
            add_input = input("enter a name and number: ")
            add_split = add_input.split()
            name = add_split[0]
            num = int(add_split[1])
            add_sub = phone_book.get(name)
            if add_sub == None:
                phone_book[name] = num
                print("The subscribers " + add_split[0] + " is added to the phone book")
                ubd_dict(phone_book)

            else:
                print("a subscriber with the name " + name + " already exists, try another name")

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



# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.



def deco_time_and_name(func_to_deco):
    def print_time_and_name(*args, **kwargs):
        str_name = func_to_deco.__name__
        name_f = "function name " + str_name
        print(name_f)
        str_time = time.ctime()
        name_t = "start function time " + str_time
        print(name_t)
        rez = func_to_deco(*args, **kwargs)

        try:
            with open('data_func.json', 'x+') as file:
                file.write(name_t + '\n' + name_f)

        except FileExistsError:
            with open('data_func.json', 'w') as file:
                file.write(name_f + '\n' + name_t)
        return rez
    return print_time_and_name

@ deco_time_and_name
def standard_func():
    print("this is a standard function")

standard_func()


# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

class MyManager:
    def __enter__(self, *args, **kwargs):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != None:
            exc_name = "this exception " + str(exc_val)
            print(exc_name)
            str_time = time.ctime()
            exc_time = "start function time " + str_time
            print(exc_time)

            try:
                with open('exc_data.json', 'x+') as file:
                    file.write(exc_name + '\n' + exc_time)

            except FileExistsError:
                with open('exc_data.json', 'w') as file:
                    file.write(exc_name + '\n' + exc_time)
                return True
        else:
            pass


with MyManager():
    some_text = "some_text"
    print(some_text)

