name = input("Whats your name? ")
age = int(input("Hold old are you {}".format(name)))

if 18 <= age <= 31:
    print("Welcome to the titty bar, {0}".format(name))
else:
    print("Too green, can't help ya rookie")

