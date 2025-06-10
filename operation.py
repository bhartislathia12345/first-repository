num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 == 0:
    division = "undefined"
else:
    division = num1 / num2

print("addition:",addition)
print("subtraction:",subtraction)
print("multiplication:",multiplication)
print("division:",division)

