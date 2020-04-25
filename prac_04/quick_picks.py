import random

MINIMUM_NUMBER=1
MAXIMUM_NUMBER=45

def main():
    number_of_quick_picks = int(input("Enter number of quick picks "))
    while number_of_quick_picks<0:
        print("Enter number greter than zero.")
        number_of_quick_pics=int(input("Enter number of quick picks "))
    for i in range(number_of_quick_picks):
        quick_picks_numbers = []
        for i in range(6):
            numbers = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while numbers in quick_picks_numbers:
                numbers= random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_picks_numbers.append(numbers)
        quick_picks_numbers.sort()
        print(" ".join("{:2}".format(numbers) for numbers in quick_picks_numbers))

main()

