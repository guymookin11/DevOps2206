names = ["ofek", "idan", "eden", "aviran"]
if "guy" in names:
    print("found")
else:
    print("not found")


names2 = ["ofek", "idan", "eden", "aviran"]
if names2[0] == "guy" or names2[2] == "guy":
    print("found")
else:
    print("not found")


a = 1
b = 1
c = [1,2,3]
d = [1,2,3]
if c == d and a == b:
    print("c equals d and a equals b")