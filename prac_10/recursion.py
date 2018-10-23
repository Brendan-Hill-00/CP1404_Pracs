"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


"""
Expected output:
1 + 0 + 1 + 0 + 1 = 3
"""

print(do_it(5))

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


"""
Expected output
Endlessly printing the squares of all the numbers from -1 onwards
"""
do_something(4)


def calculate_blocks(rows):
    if rows <= 0:
        return 0
    return rows + calculate_blocks(rows - 1)


def build_pyramid():
    number_of_rows = int(input("Would you like to build a pyramid? Enter a number of rows: "))
    print("To build a pyramid {} rows tall, you will need {} blocks".format(number_of_rows,
                                                                            calculate_blocks(number_of_rows)))


build_pyramid()
