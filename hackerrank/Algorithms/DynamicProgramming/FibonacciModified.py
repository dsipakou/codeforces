t1, t2, n = map(int, input().split())
l = list()
l.append(t1)
l.append(t2)
for _ in range(n-2):
    l.append(l[-2] + l[-1]**2)
print(l[-1])