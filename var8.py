a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The three number are", a, b, c)
a, b = a + b, b + c
print("Numbers after swapping are", a, b, c)