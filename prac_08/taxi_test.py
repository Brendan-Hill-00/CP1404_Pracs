from prac_08.taxi import Taxi


def main():
    print("Taxi Testing")
    new_taxi = Taxi("Prius 1", 100, 1.23)
    new_taxi.drive(40)
    print(new_taxi)
    print("The price of that trip was {}".format(new_taxi.get_fare()))
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print("The price of that trip was {}".format(new_taxi.get_fare()))


main()
