#better code:

choice = "-"

while choice != "0":
    if choice in ("1234567""10"):
        print("You choose {}".format(choice))
    else:
        print("Choose an option")
        print("1:\tPython")
        print("2\tJava")
        print("3\tGym")
        print("4\tswimming")
        print("5\tdancing")
        print("6\tlearning")
        print("7\twork")
        print("10:\tsexo")


    choice = input()


# choice = "-"
#
# while True:
#     if choice == "0":
#         break
#     elif choice in "1234567":
#         print("You choose {}".format(choice))
#     else:
#         print("Choose an option")
#         print("1:\tPython")
#         print("2\tJava")
#         print("3\tGym")
#         print("4\tswimming")
#         print("5\tdancing")
#         print("6\tlearning")
#         print("7\twork")
#
#
#     choice = input()