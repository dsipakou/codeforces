ans = 0
n, k = map(int, input().split())
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 2, n + 1):
            ans += 1
print(ans)