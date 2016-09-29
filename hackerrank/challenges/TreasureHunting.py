x, y = map(int, input().split())
a, b = map(int, input().split())
n2 = (a*y - b*x) / (a**2 + b**2)
n1 = (x + b*n2) / a
print(n1)
print(n2)
