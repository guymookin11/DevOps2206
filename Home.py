name = ""
age = ""
while len(name) == 0:
    name = input("Enter your name: ")
while len(age) == 0:
    age = input("Enter your age: ")
print("Hello " + "%s" % (name) + ", your age is: " + "%s" % (age) +".")
Q = input("How can I help you? ")
while len(Q) == 0:
    Q = input("You need to write something...: ")
#if Q == "I dont need help" or "no" or "dont need":
#    print("Ok")
else: print("You got it, I'll help you. Your request is: " + "%s" % (Q))

#list = {"name": "guy", "age": 23, "city":"ramat gan", "job":"IT"}
#list2 = f"my name is: {list['name']}, and my age is {list['age']}. I'm from {list['city']} and my job is: {list['job']}"
#print(list2)























