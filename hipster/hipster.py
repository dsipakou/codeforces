a,b = map(int, input().split())
x = min(a, b)
y = (max(a, b) - min(a, b)) // 2
print(x, y)