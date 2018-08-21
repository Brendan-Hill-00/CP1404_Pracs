"""
Brendan
"""
MIN_LENGTH = 8

def main():

    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(MIN_LENGTH):
    password = input('Enter a password: ')
    while len(password) < MIN_LENGTH:
        print("Your password is too short")
        password = input('Enter a password that is at least {} characters: '.format(MIN_LENGTH))
    return password

def print_asterisks(password):
    for i in password:
        print('*', end=" ")

main()