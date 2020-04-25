def main():
    numbers=[]
    for i in range(1,6):
        num = int(input("Enter number {}: ".format(i)))
        numbers.append(num)
    length = len(numbers)
    print("The first number: {} ".format(numbers[0]))
    print("The last number: {} ".format(numbers[length-1]))
    print("The smallest number: {}".format(min(numbers)))
    print("The largest number: {}".format(max(numbers)))
    print("The average of the numbers: {}".format(sum(numbers)/5))
main()
