"""CP1404/CP5632 Practical - Client code to use the Car class."""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    print("Car Details")
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    #print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    #print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(my_car)

    print("\nLimo Details")
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("The amount of fuel in the limo is {}".format(limo.fuel))
    limo.drive(115)
    print("The ododmeter of the limo is {}".format(limo.odometer))
    print(limo)

main()