"""
1. When will a ValueError occur?
    When an integer is not entered e.g a letter or a float
2. When will a ZeroDivisionError occur?
    When Trying to divide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add a loop for the denominator, if the user's enter a zero they have to re-enter a number (continues until the
    number is not zero)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
