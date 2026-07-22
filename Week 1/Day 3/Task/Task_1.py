# Fibonacci serires using loop
num = int(input("Enter a number: "))

def fib(num):
    a = 0
    b = 1

    if num < 0:
        print("Please enter a positive number.")

    elif num == 0:
        print("No terms to display.")

    elif num == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)

fib(num)