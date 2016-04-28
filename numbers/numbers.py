# http://codeforces.com/problemset/problem/588/B
n = int(input())
for i in range(2, n):
    if n % (i * i) == 0:
        n //= i
print(n)
