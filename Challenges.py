#write a program that prints numbers between 0-20 divisible by 3 and 5


for i in range(0,21):
    if i%3!=0 and i%5!=0:
        print(i)


using continue
for x in range(21):
    if x % 3 == 0 or x % 5 ==0:
        continue
    print(x)

not using continue
for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)