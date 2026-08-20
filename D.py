data = [ 17, 24, 35, 42, 51, 68, 73, 80, 91, 14, 27, 36, 45, 52, 63, 70, 81, 96, 11, 20, 33, 48, 55,
62, 77, 84, 19, 26, 39, 40, 57, 64, 71, 88, 93, 12, 29, 34, 47, 50, 61, 72, 79, 86, 95, 16, 23, 38,
49, 60, 13, 28, 31, 44, 53, 66, 75, 82, 97, 10, 21, 32, 43, 54, 65, 74, 85, 90, 99, 18, 25, 46, 59,
78, 87, 94, 15, 30, 37, 56, 69, 76, 83, 92, 9, 22, 41, 58, 67, 89, 6, 7, 8, 98, 3, 2, 1, 4, 5, 100]

#Algorithm A
def count_even_A(data):
    count = 0
    for num in data:
        if num % 2 == 0:
            count += 1
    return count
print(count_even_A(data))
#Algorithm B
def count_even_B(data):
    even_numbers = [x for x in data if x % 2 == 0]
    return len(even_numbers)
print(count_even_B(data))