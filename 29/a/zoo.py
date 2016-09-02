n = int(input())
l = list()
for i in range(n):
    x, d = map(int, input().split())
    if [x + d, x] in l:
        print('YES')
        exit()
    l.append([x, x + d])
print('NO')
