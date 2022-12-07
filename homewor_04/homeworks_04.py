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





# whether given floating
# point number is even or odd

# def isEven(s):
#     l = len(s)
#     dotSeen = False
#     for i in range(l - 1, -1, -1):
#         if (s[i] == '0'
#                 and dotSeen == False):
#             continue
#         if (s[i] == '.'):
#             dotSeen = True
#             continue
#     if ((int)(s[i]) % 2 == 0):
#         return True
#     return False
#
# s = "100.70"
# if (isEven(s)):
#     print("Even")
# else:
#     print("Odd")

