# Student Management System - Project Evolution

This repository tracks the evolution of a Student Management Application through various stages of development, from a single script to a fully modular package with configuration, logging, and unit testing.

---

## Phase 02: Project Structure

### Stage 01: Everything in Single File
```python
def main():
    name = input("Enter student name: ")
    # Validation
    if name == "":
        print("Invalid name")
        return
    # Calculation
    marks = 80
    bonus = 5
    total_marks = marks + bonus
    print(f"Student: {name}")
    print(f"Total Marks: {total_marks}")

if __name__ == "__main__":
    main()