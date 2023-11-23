print('arithmatic operattor')
a = 2
b = 3
print("addition of a + b: ", a + b)
print("substraction of a - b: ", a - b)
print("divison of a / b: ", a / b)
print("mulatiplication of a * b: ", a * b)
print("modulas of a % b:", a % b)
print("floor of a // b: ", a // b)
print("power  of a ** b: ", a ** b)
print("------- relational opeartor")
a = 5 
b = 5
print(a > b) # false grater than
print(a >= b) # false greater than equal to
print(a < b) # true less than
print(a <= b) #true less than and equal to
print(a == b) #false equal to
print(a != b) # true not equal and 
print("--------assignment operator")
x = 5
y = 6
x += y
print('x += y', x) #11
x -= y
print('x -= y', y) #5
x *= y
print('x *= y', x) # 30
x /= y
print('x /= y', x) # 5.0
x %= y
print('x %= y', x) # 5.0
x **= y
print('x **= y', x) #15625
print(x)

print("logical opertaor")
a = 6
b = 5
print(a > b and b >= a) # both value same then true
print(a < b or b <= a ) # any one value true then true values
print(a != b)
print('membership operator')
a="this is python tutorial"
print("python" in a)
print("python" not in a)

b="2458585658"
print("9" in b)
print("9" not in b)
c=2,4,5,7,5,5,4,7,5,4
print(9 in c)
print(9 not in c)
print("identity operator")
a=5
b=5
c=4
d=a
print(a is b)
print(d is a)
print(a is c)

print(b is d)
print(a is not b)
print(b is not c)