# number = input("Enter numbers")
# separators = ""
#
# for char in number:
#     if not char.isupper():
#         separators = separators + char
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char.isupper():
        print(char)