"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter Score: "))
else:
    if score >= 90:
        print("Excellent")
    if score >= 50 and score <90:
        print("Passable")
    if score < 50:
        print("Bad")