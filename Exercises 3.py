# Conditionals Exercise

mark = int(input("What mark did you get, Mark?"))

if mark > 85: 
    print("Distinction")
elif mark > 65 and mark < 85:
    print("You passed. Kinda...")
else:
    print("Did you even study???")


# Without elif would be

if mark > 85: 
    print("Distinction")

if mark > 65 and mark < 85:
    print("You passed. Kinda...")

if mark < 65:
    print("Did you even study???")