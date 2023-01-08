# 1

numb = int(input("Your number: "))

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(numb))
print("Your fibonacci number: " + str(data[-1]))

# ----------------------


