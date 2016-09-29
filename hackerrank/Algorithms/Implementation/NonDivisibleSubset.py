n, k = map(int, input().split())
l = list(map(int, input().split()))
output = list()
for i in range(n - 1):
    for j in range(i + 1, n):
        if (l[i] + l[j]) % k == 0:
            pass
