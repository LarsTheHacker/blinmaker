# <configuration>

# Set custom minimum amounts
# Order:            = [ Eggs,   Milk (mL),  Flour (g) ]
# Default Values:   = [ 1,      200,        100       ]
minimumValues       = [ 1,      200,        100       ]

# Set custom portion size
portionSize = 4

# </configuration>

def Ask(query):
    var = int()
    while True:
        try:
            var = int(input(query + "\n> "))
            return var
            break
        except ValueError:
            print("Try again")
def SmolVar(f, e, m):
    if e <= m and m <= f: return e
    if m <= f and m <= e: return m
    return f
def Exit():
    input("\nBlinmaker shuttng down...\nPress a key to continue...")
    exit()
def Main():
    eggsAmount = Ask("How many eggs you have?")
    milkAmount = Ask("How much milk you have? (in milliliters)")
    flourAmount = Ask("How much flour you have? (in grams)")
    if eggsAmount < eggsMin or milkAmount < milkMin or flourAmount < flourMin: print("Sorry, no blin today. :("); Exit()
    flourAmount = flourAmount / flourMin
    milkAmount = milkAmount / milkMin
    smallest = SmolVar(flourAmount, eggsAmount, milkAmount)
    print("\nYou can make " + str(smallest * portionSize) + " portions of blins\n\nYou will need:")
    print(" - " + str(smallest * eggsMin) + " eggs")
    print(" - " + str(smallest * flourMin) + "g of flour")
    print(" - " + str(smallest * flourMin) + "mL of milk")
    Exit()
def Init():
    import getpass
    global eggsAmount; eggsAmount = int()
    global milkAmount; milkAmount = int()
    global flourAmount; flourAmount = int()
    global eggsMin; global milkMin; global flourMin
    try:
        eggsMin = int(minimumValues[0])
    except ValueError:
        print("Invalid minimum milk amount; using default values"); eggsMin = int(1)
    try:
        milkMin = int(minimumValues[1])
    except ValueError:
        print("Invalid minimum milk amount; using default values"); milkMin = int(200)
    try:
        flourMin = int(minimumValues[2])
    except ValueError:
        print("Invalid minimum flour amount; using default values"); flourMin = int(100)
    try:
        portionSizeReal = int(portionSize)
    except ValueError:
        print("Invalid portion amount; using default values"); portionSizeReal = int(4)
    print("Hello, " + getpass.getuser() + "!\nBlinmaker is starting up...\n")
    Main()
Init()
