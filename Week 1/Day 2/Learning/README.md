# Day 2 - Prime and Palindrome Programs

## Description

In Day 2, I practiced checking whether numbers are prime numbers and palindromes using Python.

The main task checks whether a number is both a **prime number** and a **palindrome**. Two additional related tasks were also completed separately to understand each concept individually.

## Project Structure

```text
Day 2 \ Task
│
├── Task_1.py
├── Task_2.py
└── Task_3.py
## Task 1: Prime AND Palindrome

The first program checks whether a number is both a prime number and a palindrome.

A number must satisfy both conditions:

It must be a prime number.
It must be a palindrome.

For example:

131

131 is a prime number and reads the same forwards and backwards, so it is both prime and palindrome.

## Task 2: Prime Number Checker

The second program checks whether a number is a prime number.

A prime number is a number greater than 1 that has only two factors:

1
The number itself

For example:

7

The number 7 is prime because it is only divisible by 1 and 7.

The modulo operator % is used to check the remainder after division:

num % i == 0

If the remainder is 0, the number is divisible by another number and is not prime.

## Task 3: Palindrome Checker

The third program checks whether a number is a palindrome.

A palindrome reads the same forwards and backwards.

Examples:

121 → Palindrome
1331 → Palindrome
123 → Not a Palindrome

The number is reversed using:

num[::-1]

Then the original number is compared with its reversed version:

num == num[::-1]

If both values are the same, the number is a palindrome.

## Concepts Learned
input()
int()
if-else statements
for loops
range()
Modulo operator %
String slicing
Reverse slicing [::-1]
Boolean variables
Logical operator and
Checking prime numbers
Checking palindrome numbers
Conclusion

These tasks helped me understand how to combine multiple conditions and how to solve problems using loops, conditional statements, operators, string slicing, and Boolean logic in Python.