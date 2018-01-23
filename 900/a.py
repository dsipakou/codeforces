n = int(input())
left = 0
right = 0
for i in range(n):
    x = list(map(int, input().split()))[0]
    if x > 0:
        right += 1
    else:
        left += 1
    if right > 1 and left > 1:
        print('NO')
        exit()
print('YES')