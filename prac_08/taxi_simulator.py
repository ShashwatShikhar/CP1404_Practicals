from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choose_menu = input(">>> ").upper()
    while choose_menu != "Q":
        if choose_menu == "C":
            print("Taxis available: ")
            taxis_to_show(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choose_menu == "D":
            current_taxi.start_fare()
            distance_to_go = float(input("How far driving "))
            current_taxi.drive(distance_to_go)
            trip_costs = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_costs))
            total_bill += trip_costs
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        choose_menu = input(">>> ").upper()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    taxis_to_show(taxis)


def taxis_to_show(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()