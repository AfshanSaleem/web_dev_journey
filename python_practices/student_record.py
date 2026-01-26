students = {}

def menu():
    print("Student Record System")
    print("1. Add student")
    print("2. Update marks")
    print("3. View students")
    print("4. Exit")

def add_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("This roll number already exists.")
        return

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[roll] = [name, marks]
    print("Student added.")

def update_marks():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found.")
        return

    new_marks = float(input("Enter new marks: "))
    students[roll][1] = new_marks
    print("Marks updated.")

def view_students():
    if len(students) == 0:
        print("No records found.")
        return

    print("\nRoll  Name   Marks")
    print("------------------")
    for roll in students:
        print(roll, students[roll][0], students[roll][1])

while True:
    menu()
    choice = int(input("Choose option (1-4): "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_marks()
    elif choice == 3:
        view_students()
    elif choice == 4:
        print("Program closed.")
        break
    else:
        print("Invalid choice.")
