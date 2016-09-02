n = int(input())
a = list(map(int, input().split()))
cur = 1001
i, j = 0, 0
for index in range(n - 1):
    b = abs(a[index] - a[index + 1])
    if b < cur:
        i, j = index + 1, index + 2
        cur = b
if abs(a[0] - a[-1]) < cur:
    i, j = len(a), 1
print(i, j)
