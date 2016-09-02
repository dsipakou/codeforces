x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(max(max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)))
