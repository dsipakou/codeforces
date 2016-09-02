n, m = map(int, input().split())
x = set()
y = set()
for i in range(m):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
    print((n - len(x)) * (n - len(y)), end=' ')