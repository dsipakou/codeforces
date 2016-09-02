n = int(input())
h = list(map(int, input().split()))
m = int(input())
x = sorted(set(map(int, input().split())))
i = 0
for j in x:
    j -= 1
    while i < j:
        h[i] = min(h[i], abs(i - j))
        i += 1
print(sum(h))
