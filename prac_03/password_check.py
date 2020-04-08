MINIMUM_LENGTH=5

def main():
    password = get_password()
    asterick(password)


def asterick(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password greater than {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Your Password is short")
        password = input("Enter password greater than {} characters: ".format(MINIMUM_LENGTH))
    return password


main()