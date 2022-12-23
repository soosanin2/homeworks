# homework_07

phone_book = {}

while True:
    user_input = input('\n Select and enter a command \n'
                       '(stats, add, delete, list, show): ')
    print(user_input)

    # stats: кількість записів
    # add: додати запис
    # delete <name>: видалити запис за іменем (ключем)
    # list: список всіх імен в книзі
    # show <name>: детальна інформація по імені

    # user_input = user_input.split()
    # print(user_input)

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
                str_num = str(phone_book.get(show_input))
                print("Name " + show_input + " number " + str_num)

            elif user_input == "delete":
                del_input = input("enter a name: ")
                del_sub = phone_book.get(del_input)
                if del_sub != None:
                    print("The subscribers " + del_input + " removed from the phone book")
                    del phone_book[del_input]
                else:
                    print("The subscribers " + del_input + " does not exist")

            # else:
            #     print("Please select a command from the available")

    except ValueError:
        print("Sorry invalid request, try again")



