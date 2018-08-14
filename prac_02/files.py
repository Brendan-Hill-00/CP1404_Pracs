# Task 1
new_file = open('name.txt', 'w')
name = input("Enter your name: ")
print(name, file=new_file)
new_file.close()

# Task 2
file_contents = open('name.txt', 'r')
output = file_contents.read()
print("Your name is", output)
file_contents.close()

# Task 3
numbers_file = open('numbers.txt', 'r')
total = 0
for line in numbers_file:
    line = int(line)
    total += line
print(total)
numbers_file.close()
