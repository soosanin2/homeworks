# homework_05

# 1

in_text = input("input your text: ")

for i in in_text:

    if i.isdigit():
        i = int(i)
        if i % 2 == 0:
            print(f'This is the number "{i}" it is even')
        else:
            print(f'This is the number "{i}" it is odd')

    elif i.isalpha():
        if i. istitle():
            print(f'This is the letter "{i}" it is capital')
        else:
            print(f'This is the letter "{i}" it is not capital')

    else:
        print(f'This is the symbol "{i}"')

# =====================


# 2.1

# import time
#
# while True:
#     print("I love Python")
#     time.sleep(4.2)

# ==========================


# 2.2
#
# import time
#
# timing = time.time()
# while True:
#     if time.time() - timing > 4.2:
#         timing = time.time()
#         print("I love Python")