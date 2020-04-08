def fahrenheit_to_celsius(fahrenheit):
    celsius=5/9*(fahrenheit-32)
    return celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit=celsius*9.0/5+32
    return fahrenheit

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            celsius=float(input("Celsius: "))
            convert= celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} f".format(convert))
        elif choice == "f":
            fahrenheit=float(input("Fahrenheit: "))
            convert= fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} c".format(convert))
        else:
            print("Invalid")
        print(MENU)
        choice=input(">>> ").lower()
    print("Thank you.")

main()