#http://codeforces.com/problemset/problem/586/B
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []

for index in range(len(b)):
    res.append(b[index] + sum(a1[:index]) + sum(a2[index:]))

res.sort()
print(res[0] + res[1])

