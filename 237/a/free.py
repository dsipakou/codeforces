n = int(input().strip())
current = ''
output = 1
tmp1 = 1
for i in range(n):
    tmp = input()
    if current == tmp:
        tmp1 += 1
    else:
        current = tmp
        output = max(output, tmp1)
        tmp1 = 1
print(max(output, tmp1))