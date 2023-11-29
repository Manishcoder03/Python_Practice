n =int(input("enter number: "))
n1 = n
reverse = 0
while n > 0:
    rem = n % 10
    n = n // 10
    reverse = rem + reverse * 10
print(f"reverse of {n1}={reverse}")