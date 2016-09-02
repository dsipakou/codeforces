n = int(input())
l = list(map(int, input().split()))
s = int(sum(l) / n * 2)
tmp = list()
for i in range(n):
    a = l[i]
    l[i] = 0
    if a > 0:
        b = l.index(s - a)
        print(i + 1, l.index(s - a) + 1)
        l[l.index(s - a)] = 0


