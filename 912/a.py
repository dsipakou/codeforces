a, b = map(int, input().split())
x, y, z = map(int, input().split())
a1 = 2 * x + y
b1 = 3 * z + y
print(max(0, a1 - a) + max(0, b1 - b))