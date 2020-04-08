def score_status(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter Score: "))
    else:
        if score >= 90:
            print("Excellent")
        if score >= 50 and score < 90:
            print("Passable")
        if score < 50:
            print("Bad")


def main():
    score = float(input("Enter score: "))
    score_status(score)
main()