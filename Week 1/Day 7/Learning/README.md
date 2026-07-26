# Day 5 - Student Grade Calculator (Without Percentage)
## Task
Write a command-line program that takes student marks as input and calculates the grade using conditional statements.

The program should:

Accept marks between 0 and 100
Handle invalid input using exception handling
Prevent the program from crashing
Use functions and a menu-driven system
Code
Python

## Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'


def main():
    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Calculate Grade")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            try:
                marks = float(input("Enter student marks (0 - 100): "))

                if 0 <= marks <= 100:
                    grade = calculate_grade(marks)
                    print(f"\nResult: Marks: {marks} | Grade: {grade}")
                else:
                    print("Error: Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == '2':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


main()
## Output
## Example 1 (Valid Input)
text

--- Student Grade Calculator ---
1. Calculate Grade
2. Exit

Enter your choice (1-2): 1
Enter student marks (0 - 100): 85

Result: Marks: 85.0 | Grade: B
Example 2 (Invalid Input)
text

Enter student marks (0 - 100): ninety
Invalid input! Please enter numbers only.
Example 3 (Out of Range Input)
text

Enter student marks (0 - 100): 150
Error: Marks must be between 0 and 100.
## Concepts Used
- Functions
- Conditional statements (if-elif-else)
- While loop
- Exception handling (try-except)
- User input
- Comparison operators
- Menu-driven program
## Learning Outcome
This project helped me understand how to:

- Use functions to organize code
- Apply conditional logic for grading systems
- Handle invalid input using exception handling
- Validate user input
- Build a simple command-line application