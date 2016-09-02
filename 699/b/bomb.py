n, m = map(int, input().split())
l = list()
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == '*':
            l.append([i, j])
print(l)
