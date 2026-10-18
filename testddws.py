nested_list = [[1, 5, 8], [3, 12, 2], [9, 4, 7]]
target = 6
count = 0

# Loop through each sublist, then each number
for sublist in nested_list:
    for num in sublist:
        if num > target:
            count += 1

print(count)  # Output: 4
numbers = [5, 12, 18, 25, 30]
threshold = 20

# Find all numbers greater than the threshold
greater_than = [x for x in numbers if x > threshold]
print(greater_than)  # Output: [25, 30]

# Find all numbers less than or equal to the threshold
less_or_equal = [x for x in numbers if x <= threshold]
print(less_or_equal)  # Output: [5, 12, 18]
