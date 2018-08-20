def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            converted_temperature = convert_celsius(celsius)
            print("Result: {:.2f} F".format(converted_temperature))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            converted_temperature = convert_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(converted_temperature))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")

def convert_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return(celsius)

def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return(fahrenheit)

main()