n, k = map(int, input().split())
l = list(map(int, input().split()))
output = 0
for i in range(len(l[::k])):
    output += 1
    if l[i*k] == 1:
        output += 2
print(100 - output)