num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print('choose from operations available to perform')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
operation=int(input("Enter Option number: "))
if operation==1:
    print(num1+num2)
    print("Addition of two numbers is",num1+num2)
if operation==2:
    print(num1-num2)
    print("Subtraction of two numbers is",num1-num2)
if operation==3:
    print(num1*num2)
    print("Multiplication of two numbers is",num1*num2)
if operation==4:
    print(num1/num2)
    print("Division of two numbers is",num1/num2)
if operation>=5:
    print("Invalid Option")

print("Thank you for using")