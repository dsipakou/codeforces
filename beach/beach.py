# http://codeforces.com/problemset/problem/599/C

n = int(input())
h = list(map(int, input().split()))
h1 = h[:]
h1.sort()
s1 = 0
s2 = 0

part = 0
for i in range(n):
    s1 += h[i]
    s2 += h1[i]
    if s1 == s2:
        part += 1
print(part)