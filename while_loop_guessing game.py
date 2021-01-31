import random

highest = 100
answer = random.randint(1, highest)
print(answer)   # TODO REMOVE AFTER TESTING
guess = 0  #initialize to any number
print("Guess a number between 1 and {}:".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("You quitter!!")
        break
    if guess == answer:
        print("GJ!!")
        break
    elif guess > answer:
        print("Go lower")
    else:
        print("Go Higher")
# else:
#     print("try again"+
#     6)

#     if guess < answer:
#         print("Go higher")
#     else:
#         print("Go lower")
#     guess = int(input())
#     if guess == answer:
#         print("CORRECT well done champ")
#     else:
#         print("Try again loser")
