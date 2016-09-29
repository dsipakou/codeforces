n = int(input())
d = dict()
for i in range(n):
    s = list(set(input()))
    for j in range(len(s)):
        d[s[j]] = d.get(s[j], 0) + 1

print(len(list(x for x in d.values() if x > n - 1)))