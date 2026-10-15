# Activity #7

# Part 1
students = ["Edward","Ally","Xyrus","Isip","Nuella"]
# students = []
grades = [94,67,89,100,10]
class Student_LMS():
    def count_students(students):
        if students == []:
            print("None")
            return
        else:
            num = 0
            for num in students:
                num += 1
                return num

    def total_student_grades(grades):
        sum(grades)

lms = Student_LMS()

lms.count_students()