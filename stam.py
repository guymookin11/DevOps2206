
name = input("enter name: ")
while name == "" or any(n.isdigit() for n in name):
    if name == "":
        name = input("you need to enter a name: ")
    elif any(n.isdigit() for n in name):
        name = input("you can't use numbers: ")
    else:
        break

name = str(name)
print("Hello " + name + " what do you want to buy?")

houses = ["1. apartment, $9000", "2. house, $50000", "3. villa, $80000"]
for house in houses:
    print(house)

choice = input("choose: ")
while not choice.isdigit or int(choice) not in range(1, 4) or choice == "":
    choice = input("you need to choose something")

choice = int(choice)
if choice == 1:
    choice = "apartment in $9000"
elif choice == 2:
    choice = "house in $50000"
elif choice == 3:
    choice = "villa in $80000"

print("good, you choose to but " + choice)
