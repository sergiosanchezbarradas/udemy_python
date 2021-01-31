answer = 39

print("Guess a number between 1 and 100")
guess = int(input())

if guess < answer:
    print("Higher!!!!go higher!!")
elif guess > answer:
    print("Lower!!!! gooo loweeer!!")
else:
    print("You got it matey")