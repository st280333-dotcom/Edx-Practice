import sys

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
    break

if len(names) == 1:
    formatted_names = names[0]
elif len(names) == 2:
    formatted_names = f"{names[0]} and {names[1]}"
else:
    formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"

print(f"Adieu, adieu, to {formatted_names}")
