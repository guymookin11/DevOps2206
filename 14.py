try:
    a = int(input("enter name: "))
    b = int(input("enter name: "))
    print(a / b)
except ZeroDivisionError as e:
    print("you tried to divide by zero, nu nu nu")
    print(e.args)
except ValueError as e:
    print("bad input")
    print(e.args)
except BaseException as e:
    print(e.args)
print("aviel")
