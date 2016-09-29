n, k = map(int, input().split())
b = [int(x) for x in list(input())]
id = list(map(int, input().split()))
for i in range(len(id)):
    if b[id[i] - 1] == 0:
        print('YES')
        exit()
print('NO')
