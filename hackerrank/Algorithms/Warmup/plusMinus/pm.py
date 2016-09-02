n = int(input())
l = list(map(int, input().split()))
d = dict()
for i in range(n):
    if l[i] < 0:
        d[-1] = d.get(-1, 0) + 1
    elif l[i] > 0:
        d[1] = d.get(1, 0) + 1
    else:
        d[0] = d.get(0, 0) + 1

print(d.get(1, 0) / len(l))
print(d.get(-1, 0) / len(l))
print(d.get(0, 0) / len(l))