HEX_COLOURS = {"Brown": "#a52a2a", "Grey": "#bebebe", "White": "#ffffff", "Black": "#000000", "Blue":
                "#0000ff", "Yellow": "#ffff00", "Pink": "#ffc0cb", "Green": "#00ff00", "Red": "#ff0000",
               "Orange": "#ffa500", "Purple": "#a020f0", }
for colour in HEX_COLOURS:
    print("{:6} is {}".format(colour, HEX_COLOURS[colour]))

colour = input("Enter colour name: ").title()
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").title()
