'''
a = int(input())
b = int(input())
str = input()

x = a + b
y = a - b
z = a * b
d = a / b

if str == '/' and a * b == 0:
    print('На ноль делить нельзя!')
else:
    print(d)
if str == '+':
    print(x)
elif str == '-':
    print(y)
elif str == '*':
    print(z)
else:
    print('Неверная операция')
'''

a = int(input())
b = int(input())
str = input()

if str == '+':
    x = a + b
    print(x)
elif str == '-':
    y = a - b
    print(y)
elif str == '*':
    z = a * b
    print(z)
elif str == '/' and b == 0:
    print('На ноль делить нельзя!')
elif str == '/':
    d = a / b
    print(d)
else:
    print('Неверная операция')
