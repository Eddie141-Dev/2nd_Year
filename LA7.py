# Activity 7

students = ["Edward", "Ally", "Jaypee", "Xyrus", "Nuella"]
grades = [96, 95, 100, 95, 10]


# Part A
def student_list(students):
    if not students:
        return 0
    students.pop()
    return 1 + student_list(students)

count = student_list(students)
print("There are", count, "students in this class")

# Part B
def student_total_grades(grades):
    if not grades:
        return 0
    return grades[0] + student_total_grades(grades[1:])

print(f"The total grades of all students are: {student_total_grades([96, 95, 100, 95, 10])}")
average = student_total_grades([96, 95, 100, 95, 10]) / 5
print(f"The average grade of the entire class is: {average}")

# Part C


