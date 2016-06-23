i = int(input())
n = list(map(int, input().split()))
n = sorted(list(set(n)))
result = 'NO'
for x in range(len(n) - 2):
    if (n[x + 2] - n[x + 1] >= n[x + 1] - n[x] > 0) and (n[x + 2] - n[x + 1] <= n[x + 1] - n[x] < 2):
        result = 'YES'
print(result)
