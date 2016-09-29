t = int(input())
for i in range(t):
    l = []
    n = int(input())
    a = int(input())
    b = int(input())
    for j in range(n):
        l.append((a * j) + (b * (n - (j + 1))))
    print(*sorted(set(l)))