number = "3,345;463:422,345 765;223"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)