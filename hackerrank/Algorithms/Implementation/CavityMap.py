n = int(input())
l = []
output = []
for i in range(n):
    l.append(list(int(x) for x in list(input())))
output.append(l[0])
for i in range(1, n - 1):
    tmp = []
    tmp.append(l[i][0])
    for j in range(1, n - 1):
        if l[i][j] > l[i - 1][j] and l[i][j] > l[i + 1][j] and l[i][j] > l[i][j - 1] and l[i][j] > l[i][j + 1]:
            tmp.append('X')
        else:
            tmp.append(l[i][j])
    tmp.append(l[i][n - 1])
    output.append(tmp)
output.append(l[n - 1])
for i in range(n):
    print(''.join(str(x) for x in output[i]))