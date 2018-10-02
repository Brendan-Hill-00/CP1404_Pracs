from prac_08.unreliable_car import UnreliableCar


def main():
    print("Testing")
    new_unreliable_car = UnreliableCar("Prius 1", 100, 55)
    new_unreliable_car.drive(40)
    print(new_unreliable_car)
    new_unreliable_car.drive(5)
    print(new_unreliable_car)
    new_unreliable_car.drive(52)
    print(new_unreliable_car)
    new_unreliable_car.drive(100)
    print(new_unreliable_car)


main()
