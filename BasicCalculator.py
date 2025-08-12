num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
opt = input("Enter operator: ")

if opt == "+":
    print(f"The addition is: {num1+num2}")
if opt == "-":
    print(f"The substraction is: {num1-num2}")
if opt == "*":
    print(f"The multiplication is: {num1*num2}")
if opt == "/":
    print(f"The division is: {abs(num1/num2)}")
else:
    print("Invalid oprator!")
