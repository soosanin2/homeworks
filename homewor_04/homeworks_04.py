# homewor_04


# 1

print("May not work correctly with fractional numbers!")

in_text = input("input your text: ")

if in_text.isnumeric():
    print("your nomber is " + in_text)
    in_text = int(in_text)
    if in_text % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")
else:
    print("It's yuor text: " + in_text)

    print("the length of your text is " + str(len(in_text)) + " symbol")
# ===============


# # 2

# print("May not work correctly with fractional numbers!")

# in_text = input("input your text: ")
#
# if in_text == "0":
#     print("your nomber is " + str(in_text))
#     print("your number is even")
#
# try:
#     if float(in_text):
#         in_text = float(in_text)
#         print("your nomber is " + str(in_text))
#         if in_text % 2 == 0:
#             print("your number is even")
#         else:
#             print("your number is odd")
#
# except ValueError:
#     print("It's yuor text: " + in_text)
#     print("the length of your text is " + str(len(in_text)) + " symbol")
# ==============





