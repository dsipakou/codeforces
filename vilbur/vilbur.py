# http://codeforces.com/problemset/problem/596/B

n = int(input())
output = 0
lst = list(map(int, input().split()))
output += abs(lst[0])
for i in range(1, n):
    output += abs(lst[i] - lst[i - 1])

print(output)