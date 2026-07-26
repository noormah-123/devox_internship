# Function to compute grade using conditionals
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

# Simple command-line program
def main():
    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Calculate Grade")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            try:
                # Ask for marks and try converting to a number (float)
                marks_input = input("Enter student marks (0 - 100): ")
                marks = float(marks_input)

                # Check if marks are inside the real range (0 to 100)
                if 0 <= marks <= 100:
                    grade = calculate_grade(marks)
                    print(f"\n Result: Marks: {marks} | Grade: {grade}")
                else:
                    print("\n Error: Marks must be between 0 and 100.")

            except ValueError:
                # This prevents crashes if the user types letters instead of numbers
                print("\n Error: Invalid input! Please enter numbers only.")

        elif choice == '2':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the program
main()
