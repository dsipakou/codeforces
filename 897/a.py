n, m = map(int, input().split())
s = input()
for i in range(m):
    l, r, c1, c2 = map(str, input().split())
    s = s[:int(l) - 1] + s[int(l) - 1: int(r)].replace(c1, c2) + s[int(r):]
print(s)