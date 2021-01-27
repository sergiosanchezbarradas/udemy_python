answer = 39

print("Guess a number between 1 and 1000")
guess = int(input())

if guess == answer:
    print("Correct good one")

else:
    if guess < answer:
        print("go higher")
    else:
        print("go lower")
    guess = int(input())
    if guess < answer:
        print("go higher")
    guess = int(input())
    if guess == answer:
        print("you got it second time")
    else:
        print("Nope, no luck today")


# if guess != answer:
#     if guess < answer:
#         print("Go higher")
#     else: #guess must be higher
#         print("Go lower!!")
#     guess = int(input())
#     if guess == answer:
#         print("correct")
#     else:
#         print("Incorrect")
# else:
#     print("Damn you are good")

# if guess < answer:
#     print("Go higher")
#     guess = int(input())
#     if guess == answer:
#         print("You got it")
#     else:
#         print("Nope,no good")
# elif guess > answer:
#     print("Go lower")
#     guess = int(input())
#     if guess == answer:
#         print("correct!!")
#     else:
#         print("Nope, too hight, better luck next time")
# else:
#     print("Bingo bingo bingo tin tin tin!!")