from math import sqrt


a = int(input())
b = int(input())
c = int(input())
d = b*b - 4*a*c
x1 = (-b + sqrt(d))/(2*a)
x2 = (-b - sqrt(d))/(2*a)
print(x1)
print(x2)


