# 1 Написати власний декоратор, задачею якого має бути друк назви функції і
# часу, коли вона була викликана. Декоратор має працювати для різних функцій однаково.

import time


def deco_time_and_name(func_to_deco):
    def print_time_and_name(*args, **kwargs):
        str_name = func_to_deco.__name__
        print(f"function name - {str_name}")
        str_time = time.ctime()
        print(f"start function time - {str_time}")
        func_to_deco()
        return
    return print_time_and_name

@ deco_time_and_name
def standard_func():
    print("this is a standard function")

standard_func()



# # 2 Написати кастомний Exception клас, MyCustomException, який
# # має повідомляти "Custom exception is occured".

class MyCustomException(Exception):
    print("Custom exception is occured")


# raise MyCustomException()



# # # 3 Написати власний менеджер контексту, задачею якого буде
# # # друкувати "==========" – 10 знаків дорівнює перед виконанням коду та
# # # після виконання коду, таким чином виділяючи блок коду символами дорівнює.
# # У випадку виникнення будь-якої помилки вона має бути надрукована текстом,
# # проте програма не має завершити своєї роботи.
# #

class MyManager:
    def __enter__(self, *args, **kwargs):
        print("==========")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != None:
            print(f'this exception: {exc_val}')

        print("==========")
        return True


with MyManager():
    some_text = "some_text"
    print(some_text)



# 4 Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
# що і менеджер контексту із попереднього завдання.

some_text = "some_text"
try:
    print("==========")
    print(some_text)

except Exception as oll_exception:
    print((f'this exception: {oll_exception}'))

finally:
    print("==========")