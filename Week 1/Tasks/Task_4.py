class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks = marks
    def compute_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >=70:
            return 'C'
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
student1 = Student("Ali",89)
print("Name:",student1.name)
print("Marks:",student1.marks)
print("Grade:",student1.compute_grade())
