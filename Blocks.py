name = input("What's your name man? ")
age = int(input("How old are ya punk, {0}?".format(name)))
print(age)

# if age >=18:
    # print("You are old enought to vote wey! chingale a votar")
# else:
#     print("Vuelve en {0} years y puedes votar chamaco de miercoles".format(18 - age))

if age < 18:
    print("Vuelve en {0} years y puedes votar chamaco de miercoles".format(18 - age))
elif age == 900:
    print("Yoga estas viejorro")
else:
    print("You are old enought to vote, good job")