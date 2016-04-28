#http://codeforces.com/problemset/problem/580/A
n = int(input())
a = list(map(int, input().split()))
output = 0
counter = 1
for i in range(len(a) - 1):
    if not a[i] > a[i + 1]:
        counter += 1
    else:
        output = max(output, counter)
        counter = 1
output = max(output, counter)
print(output)
