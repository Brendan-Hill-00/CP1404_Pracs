"""
3
2
1
2
[3, 1, 4, 1, 5, 9]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"
numbers[-1] = 1
number_selection = numbers[2:]
print(numbers)
print(number_selection)
print(9 in numbers)
