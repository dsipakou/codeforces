n = int(input())
a = list(map(int, input().split()))
output = n + 1
for i in range(n - 1):
    try:
        output = min(a[i + 1:].index(a[i]) + 1, output)
    except():
        pass
print(-1 if output > n else output)