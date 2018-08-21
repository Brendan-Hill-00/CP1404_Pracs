"""
Brendan
"""
MIN_LENGTH = 8
password = input('Enter a password: ')
while len(password) < MIN_LENGTH:
    password = input('Enter a password that is at least 8 characters: ')
for char in password:
    print('*', end=" ")