class Student:
    def __init__(self, name, obtained_marks, total_marks):
        self.name = name
        self.obtained_marks = obtained_marks
        self.total_marks = total_marks
    def compute_grade(self):
        try:
            # 1. Handle invalid inputs (Type/Value errors) by trying to convert to float
            obtained = float(self.obtained_marks)
            total = float(self.total_marks)
            
            # Logic check: Marks shouldn't be negative
            if obtained < 0 or total < 0:
                return "Error: Marks cannot be negative."

            # 2. Calculate percentage (risks ZeroDivisionError if total is 0)
            percentage = (obtained / total) * 100

            # Determine grade
            if percentage >= 90:
                return "A"
            elif percentage >= 80:
                return "B"
            elif percentage >= 70:
                return "C"
            elif percentage >= 60:
                return "D"
            else:
                return "F"

        except ZeroDivisionError:
            return "Error: Total marks cannot be zero (Division by Zero)."
        except (ValueError, TypeError):
            return "Error: Invalid input. Marks must be numerical values."


# --- Test Cases ---

# 1. Normal Valid Case
student1 = Student("Alice", 85, 100)
print(f"{student1.name}: {student1.compute_grade()}")

# 2. Division by Zero Case (Total marks is 0)
student2 = Student("Bob", 50, 0)
print(f"{student2.name}: {student2.compute_grade()}")

# 3. Invalid Input Case (Strings instead of numbers)
student3 = Student("Charlie", "eighty", 100)
print(f"{student3.name}: {student3.compute_grade()}")

# 4. Invalid Input Case (Unsupported types like None)
student4 = Student("Diana", None, 100)
print(f"{student4.name}: {student4.compute_grade()}")

# 5. Negative Marks Case
student5 = Student("Evan", -5, 100)
print(f"{student5.name}: {student5.compute_grade()}")