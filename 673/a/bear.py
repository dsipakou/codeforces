n = int(input())
t = list(map(int, input().split()))
t.append(0)
t = sorted(t)
output = 0
for i in range(len(t) - 1):
    output = t[i] + 15
    if t[i + 1] - t[i] > 15:
        break
    else:
        output = t[i + 1] + 15
print(min(output, 90))
