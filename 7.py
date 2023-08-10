prefix = "my name is"
names = ["ofek", "idan", "eden", "aviran","or", "avidan", "daniel"]
for name in names:
    print(("looking for or..."))
    if name == "or":
        pass
    else:
        ("did not find or")
    print("did not foind or yet...")
else:
    print("did not find or at all")

    name = name + "z"
    print(f"{prefix} {name}")

for i in range(len(names)):
    names[i] = names[i] + "z"
    print(f"{prefix} {names[i]}")

print(names)
result = []
for name in names:
    if name.find("dan") > -1:
        result.append(name)

names_with_z_containing_dan = [name + "z" for name in names if name.find("dan") > -1]
print(result)
print(names_with_z_containing_dan)

age = int(input("enter your age:"))
while age < 50:
    print("you are still ok")
    age = int(input("enter your age:"))
else:
    print("your are old")
