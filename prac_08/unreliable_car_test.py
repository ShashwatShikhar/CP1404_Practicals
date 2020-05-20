from prac_08.unreliable_car import UnreliableCar


def main():
    best_car = UnreliableCar("Better", 100, 90)
    bad_car = UnreliableCar("unreliable", 100, 9)
    for i in range(1, 12):
        print("drive {}km:".format(i))
        print("{:14} drove {:2}km".format(best_car.name, best_car.drive(i)))
        print("{:14} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(best_car)
    print(bad_car)

main()