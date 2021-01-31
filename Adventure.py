# exits = ["north", "south", "east", "west"]
#
# chosen_exit = ""
# while chosen_exit not in exits:
#     chosen_exit = input("Choose your destiny")
#     if chosen_exit.casefold() == "quit":
#         print("Gameover")
#         break
#
# print("You are out!")

for i in range(0,21):
    if i%3!=0 and i%5!=0:
        print(i)