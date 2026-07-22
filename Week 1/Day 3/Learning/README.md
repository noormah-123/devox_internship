# Fibonacci

## Tasks

This folder contains three different Fibonacci tasks implemented in Python:

1. Fibonacci Series Using Recursion
2. Fibonacci Series Using a Loop
3. Find the nth Fibonacci Number Using Recursion

---

## Task 1: Fibonacci Series Using Recursion

### Description

Generate the Fibonacci series using a recursive function.

### Logic

The Fibonacci sequence follows this rule:

```text
F(n) = F(n - 1) + F(n - 2)
```

The function uses base cases:

* If `n == 0`, return `0`.
* If `n == 1` or `n == 2`, return `1`.
* Otherwise, calculate the result recursively.

### Example

For input:

```text
5
```

Output:

```text
0, 1, 1, 2, 3
```

---

## Task 2: Fibonacci Series Using a Loop

### Description

Generate the Fibonacci series using a loop instead of recursion.

### Logic

* Start with `a = 0` and `b = 1`.
* Print the current values.
* Calculate the next Fibonacci number using:

```text
c = a + b
```

* Update the values:

```text
a = b
b = c
```

* Repeat the process using a loop.

### Example

For input:

```text
5
```

Output:

```text
0, 1, 1, 2, 3
```

---

## Task 3: Find the nth Fibonacci Number Using Recursion

### Description

Find the Fibonacci number at a specific position using recursion.

### Logic

The function recursively calculates:

```text
fib(n) = fib(n - 1) + fib(n - 2)
```

The base cases are:

```text
fib(0) = 0
fib(1) = 1
fib(2) = 1
```

### Example

For input:

```text
7
```

Output:

```text
The Fibonacci number is: 13
```

The sequence is:

```text
Position: 0  1  2  3  4  5  6  7
Value:    0  1  1  2  3  5  8  13
```

---

## Concepts Used

* Functions
* Recursion
* Loops
* `if-elif-else` statements
* User input
* Variables
* Arithmetic operators
* Fibonacci sequence

---

## Learning Outcome

This task helped me understand how the Fibonacci sequence can be implemented using both recursion and iteration. I learned how recursion repeatedly calls a function to solve a problem and how loops can be used to efficiently generate a sequence. I also learned how to find the Fibonacci number at a specific nth position using recursion.
