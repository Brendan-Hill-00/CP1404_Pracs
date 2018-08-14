finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a whole number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)