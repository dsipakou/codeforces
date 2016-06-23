n, m = map(int, input().split())
output = list()
l = 51
r = 51
t = None
b = 0
for x in range(n):
    output.append(input())
for x in range(n):
    if '*' in output[x]:
        if t is None:
            t = x
        l = min(l, output[x].index("*"))
        r = min(r, output[x][::-1].index('*'))
        b = x
for x in range(t, b + 1):
    print(output[x][l:len(output[x]) - r])


