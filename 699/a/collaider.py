n = int(input())
d = list(input())
p = list(map(int, input().split()))
output = -1
for i in range(1, n):
    if d[i - 1] == 'R' and d[i] == 'L':
        if output > 0:
            output = min(output, (p[i] - p[i - 1]) / 2)
        else:
            output = (p[i] - p[i - 1]) / 2
print(int(output))