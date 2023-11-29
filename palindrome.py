n =(input("enter number="))
n1 = n
reverse = 0
while n > 0:
    rem = n % 10
    n = n // 10
    reverse = rem + reverse * 10
    
if n1 == reverse:
    print(f"{n1} is palindrome Number")
else:
    print(f"{n1} is not palindrome number")