n = int(input())
rad = 0
output = 0
matrix = []
u = []
d = []
l = list()
r = list()
for i in range(n):
    s = list(input())
    matrix.append(s)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '.':
            u.append([i, j])
            d.append([i, j])
            l.append([i, j])
            r.append([i, j])
            search = True
            while(search):
                for t in range(len(u)):
                    if (u[t][1] - 1) >= 0 and (l[t][0] - 1) >= 0 and (r[t][0] + 1) < n and (d[t][1] + 1) < n:
                        pass
                    else:
                        search = False
                        output = max(output, rad)
print(output)