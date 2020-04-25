def main():
    store_email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        check = input("Is your name {}? (Y/n) ".format(name))
        if check.upper() != "Y" and check != "":
            name = input("Name: ")
        store_email_and_name[email] = name
        email = input("Email: ")

    for email, name in store_email_and_name.items():
        print("{} ({})".format(name, email))


def extract_name_from_email(email):
    prefix = email.split('@')[0]
    parts_of_email = prefix.split('.')
    name = " ".join(parts_of_email).title()
    return name


main()