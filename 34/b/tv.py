n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
output = 0
for i in range(m):
    if l[i] < 0:
        output += abs(l[i])
    else:
        break
print(output)
