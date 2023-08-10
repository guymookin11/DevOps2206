#Question 1
#1. Create a variable name first with value 7.
#2. Create a variable name second with value 44.3.
#4. Print result of multiplying first by second
#3. Print result of adding first to second.
#5. Print result of dividing second by first

first = 7
second = 44.3
print (first+second)
print (first*second)
print (second/first)

#Question 2
#What will be the values of a, b, c at the end?
#a = 8
#a = 17
#a = 9
#b = 6
#c = a + b
#b = c + a
#b = 8

a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print (f"a: {a}, b:{b} c: {c}")

#Question 3
#Is there a difference between the two lines below? Why?
#name = “john”
#name = ‘john’

#What is the issue with the code below?
#my_number = 5 + 5
#print(“result is: “ + my_number)
#Suggest an edit.

#The difference is "", ''.

#The issue with the code is that it's can't print string with integer.
my_number = 5 + 5
print("result is: " + str(my_number))
print(f"result is: {my_number}")

#Question 4
#What will be the output?
#x = 5
#y = 2.36
#print(x + int(y))

x = 5
y = 2.36
print (x + int(y)) # output: 7

#Challenge 1
#Fix the following code, without changing a or b
#a = 8
#b = “123”

print(a + b)
a = 8
b = "123"
#print(f"{a} + {b}")


numbers = [5, 10, 2, 15, 7]

maximum = max(numbers)
#print(maximum)



