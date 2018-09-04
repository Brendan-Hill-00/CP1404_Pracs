from prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Tanglewood Acoustic", 2017, 430)
print("Details")
print("{}, {}, {}".format(my_guitar.name, my_guitar.year, my_guitar.cost))
print("Testing")
print("{} get_age() - Expected 96. Got {}".format(my_guitar.name, my_guitar.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(my_guitar.name, my_guitar.is_vintage()))
print("{} get_age() - Expected 1. Got {}".format(another_guitar.name, another_guitar.get_age()))
print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
