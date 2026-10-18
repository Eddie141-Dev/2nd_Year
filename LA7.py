# Activity 7

students = ["Edward", "Ally", "Jaypee", "Xyrus", "Nuella"]
grades = [96, 95, 100, 95, 65]
passing_grade = 75
records = [list(item) for item in zip(students, grades)]
# Part A
def student_list(student):
    if not student:
        return 0
    student.pop()
    return 1 + student_list(student)

# Part B
def student_total_grades(grades):
    if not grades:
        return 0
    return grades[0] + student_total_grades(grades[1:])

# Part C
def highest_student_grade(student_records):
    if len(student_records) == 1:
        return student_records[0]
    highest_of_remaining = highest_student_grade(student_records[1:])
    current_record = student_records[0]
    if current_record[1] > highest_of_remaining[1]:
        return current_record
    else:
        return highest_of_remaining
                                             
# Part D
def student_indexing(name, index=0):
    if index >= len(records):
        print("This student is not enrolled in this class.")
        return
    if records[index][0].lower() == name.lower():
        print("This student is enrolled in this class.")
        print(f"Name: {records[index][0]}\nGrade: {records[index][1]}")
        return
    student_indexing(name, index + 1)

# Part E
def display(student_records):
    if not student_records:
        return
    row = student_records[0]
    print(f"{row[0]} {row[1]}")
    display(student_records[1:])

# Part G
def student_standing(student_records):
    if not student_records:
        return
    current_student = student_records[0]
    name = current_student[0]
    grade = current_student[1]
    status = "Passed" if grade >= passing_grade else "Failed"
    print(f"Name: {name:<10} | Grade: {grade:^10} | Status: {status:>10}")
    student_standing(student_records[1:])

# Part F
while True:
    print("="*32)
    print("RECURSIVE STUDENT RECORD SYSTEM")
    print("="*32)
    print()
    print("1. Display Student Records\n2. Count Students\n3. Calculate Total Grades\n4. Calculate Average Grade\n5. Find Highest Grade\n6. Search Student\n7. Student Standing\n8. Exit\n")
    print("="*32)
    choice = input("Action    : ")
    if choice.isdigit():
        if choice == "1":
            print("="*32)
            print("Student Record")
            print("="*32)
            display(records)
            print("="*32)
        elif choice == "2":
            count = student_list(students)
            print(f"There are {count} students in this class")
        elif choice == "3":
            print(f"The total grades of all students are: {student_total_grades(grades)}")
        elif choice == "4":
            average = student_total_grades(grades) / 5
            print(f"The average grade of the entire class is: {average:.2f}")
        elif choice == "5":
            top_student = highest_student_grade(records)
            print(f"The highest grade from this class is {top_student[1]} obtained by {top_student[0]}.")
        elif choice == "6":
            name = input("Student to search: ")
            student_indexing(name)
        elif choice == "7":
            student_standing(records)
        elif choice == "8":
            print("Exiting...")
            print("Exited Successfully!")
            break
        else:
            print("Invalid Option! Choose between 1-8.")
    else:
        print("Invalid Input/Range!")
