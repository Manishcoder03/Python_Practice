range n 
n1 = n
sum = 0
while n > 0:
    rem = n % 10
    n = n // 10
    sum = rem**3 + sum
    if n1 ==sum:
        print(f"this is {n1} armstrong")
    else:
        print(f"this is not {n1} armstrong")