import json
from logger import logger
from Utils.Validation import validate_name, validate_marks
from Services.Calculator import calculate_grade
from Models.student import Student
from config import APP_NAME, DEBUG

def load_student():
    with open("data/student.json", "r") as file:
        student = json.load(file)
    return student 

def main():
    logger.info("Application started")
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}\n")

    name = input("Enter student name: ")

    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered")
        print("Error: Marks must be a number.")
        return
    
    if not validate_marks(marks):
        logger.warning(f"Invalid marks entered: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return
    
    grade = calculate_grade(marks)
    
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()