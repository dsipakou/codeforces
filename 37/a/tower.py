n = int(input())
l = sorted(list(map(int, input().split())))
count = n - (len(l) - len(set(l)))
h = 1
d = 1
for i in range(1, n):
    if l[i] == l[i - 1]:
        d += 1
    else:
        h = max(h, d)
        d = 1
print(max(h, d), count)
