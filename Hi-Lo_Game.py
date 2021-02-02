low = 1
high = 1000

print("Think of a number between {} and {}".format(low, high))
input("Press ENTER to start the deadly game")

guesses = 1
while low != high:
    # print("\tSo, it is between {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower Sergio master of the Universe? "
                     "Enter h or l,or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":  # guess higher
        low = guess + 1
    elif high_low == "l":  # guess lower
        high = guess - 1
    elif high_low == "c":
        print("I got in in {} guesses!".format(guesses))
        break
    else:
        print("Enter h, l or c")

    guesses += 1
    # guesses = guesses + 1     not the best way
else:
    print("Your number is {}".format(low))
    print("I got it in {} guesses".format(guesses))