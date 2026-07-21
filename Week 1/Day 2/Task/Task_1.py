num = int(input("Enter a number: "))

# Check palindrome
if str(num) == str(num)[::-1]:
    is_palindrome = True
else:
    is_palindrome = False

# Check prime
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Final result
if is_prime and is_palindrome:
    print(num, "is both a prime number and a palindrome.")
else:
    print(num, "is not both prime and palindrome.")