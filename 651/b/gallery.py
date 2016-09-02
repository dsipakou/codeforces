n = int(input())
l = list(map(int, input().split()))
output = 0
while len(l) > 0:
    tmp = list(set(l))
    output += len(tmp) - 1
    [l.remove(x) for x in tmp]
print(output)
