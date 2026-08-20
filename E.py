# Week 3: Lesson 2
# Time complexity: Steps, in soving a problem (Sec, Min)
#       Depends on the algorithim 
# Memory Space: How much RAM it uses
# Big O Notation
#       Measures how fast a funtion grows/ rate of growth
#       Efficiency of an algorithim
# 0(1) = constant
numbers = [10,20,30,40]
print(numbers[2])

# 0(n) = linear 
students = ['Ally','Cenon','Arzaga','Isip','Anthony','Pelicano','Miral','Judie','Xyrus','Nuella','Kate']
for student in students:
    print(student)

# 0(n^2) = quadratic
for i in numbers:
    for j in numbers:
        print(i,j)

# 0(n!) = factorial
from itertools import permutations
city = ['A','B','C']
for p in permutations(city):
    print(p)
