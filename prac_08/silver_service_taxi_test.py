from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Testing")
    taxi = SilverServiceTaxi("A Fancy Hummer", 50, 2)
    taxi.drive(18)
    print(taxi)
    print("The price of that trip was ${}".format(taxi.get_fare()))


main()
