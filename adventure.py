available_exits = ["north", "south", "west", "east"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Choose a direction: ")

print("You are out!! gj well played")