import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO REMOVE AFTER TESTING

print("Guess a number between 1 and {}:".format(highest))
guess = int(input())

if guess == answer:
    print("GJ!!")
else:
    if guess < answer:
        print("Go higher")
    else:
        print("Go lower")
    guess = int(input())
    if guess == answer:
        print("CORRECT well done champ")
    else:
        print("Try again loser")
#
# for value in range(21):
#     value = value * 2
#     print(value)