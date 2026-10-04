from Utils.Validation import validate_name, validate_marks 
from Services.Calculator import calculate_grade 
from Models.student import Student 

def display_report(student):
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"Grade: {student.grade}")

def main(): 
    name = input("Enter student name: ")
    
    if not validate_name(name):
        print("Invalid name")
        return

    marks = int(input("Enter marks: "))

    if not validate_marks(marks):
        print("Invalid marks")
        return

    grade = calculate_grade(marks)
    student = Student(name, marks, grade)

    display_report(student)
 
if __name__ == "__main__": 
    main()