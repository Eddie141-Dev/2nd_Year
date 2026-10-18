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
def student_indexing(name):
    if not records:
        return 0
    records.pop()
    result = any(name in sublist for sublist in records)
    if result == True:
        print(f"This student is enrolled in this class.")
    try:
        r, c = next((r, sublist.index(name)) for r, sublist in enumerate(records) if name in sublist)
        print(f"Name: {records[r][c]}\nGrade: {records[r][1]}")
    except StopIteration:
        print("This student is not enrolled in this class.")

# Part E
def display(item):
    for row in records:
        for item in row:
            print(item, end=' ')
        print()

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
    print("1. Display Student Records\n2. Count Students\n3. Caculate Total Grades\n4. Calculate Average Grade\n5. Find Highest Grade\n6. Seach Student\n7. Student Standing\n8. Exit\n")
    print("="*32)
    choice = input("Action    : ")
    if choice.isdigit():
        if choice == "1":
            print("="*32)
            print("Student Record")
            print("="*32)
            print(display(records))
            print("="*32)
        if choice == "2":
            count = student_list(students)
            print("There are", count, "students in this class")
        if choice == "3":
            print(f"The total grades of all students are: {student_total_grades(grades)}")
        if choice == "4":
            total_students = len(students)
            average = student_total_grades(grades) / total_students 
            print(f"The average grade of the entire class is: {average}")
        if choice == "5":
            top_student = highest_student_grade(records)
            print(f"The highest grade from this class is {top_student[1]} obtained by {top_student[0]}.")
        if choice == "6":
            name = input("Student to search: ")
            student_indexing(name)
        if choice == "7":
            student_standing(records)
        if choice == "8":
            print("Exiting...")
            print("Exited Successfuly!")
            break
    else:
        print("Invalid Input/Range!")