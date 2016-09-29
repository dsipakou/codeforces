n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))
min_for_each = []
for i in range(n):
    for j in range(len(c)):
        if i >= c[j]:
            min_for_each.append(min(abs(i - c[j]), abs(i - c[j + 1])))
            break
    if i == n - 1:
        min_for_each.append(abs(i - c[-1]))
print(max(min_for_each))