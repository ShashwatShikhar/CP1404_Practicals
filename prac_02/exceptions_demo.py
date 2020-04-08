"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? - If numerator or denominator is not a valid integer.
2. When will a ZeroDivisionError occur? - If denominator is zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
    else:
        fraction = 0
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")