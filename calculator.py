print("This is Calculator")
first =int(input("Enter Your First number: "))
operator=input("Enter Your Operator (+,- *, /,%,**): ")
second =int(input("Enter Your Second Number: "))
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
elif operator == "**":
    print(first / second)
elif operator == "**":
    print(first ** second)
else:
    print("Please choose Correctly operator")