n = int(input())
output = 0
r = 0
l = 0
s = 0
tmp = 0
lst = list(input())
for i in range(n):
    if lst[i] is 'L':
        if r is not 0:
            output += tmp % 2
            r = 0
            l = 0
        tmp = 0
    if lst[i] is 'R':
        r = 1
        output += tmp
        tmp = 0
    if lst[i] is '.':
        tmp += 1
print(output + tmp if r is 0 else output)