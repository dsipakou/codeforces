from math import *

a, b = map(int, input().split())
n = int(input())
l = list()
for i in range(n):
    x, y, v = map(int, input().split())
    x1 = abs(x - a)
    y1 = abs(y - b)
    l.append(sqrt(x1**2 + y1**2) / v)
print(min(l))