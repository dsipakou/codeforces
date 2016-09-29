n, k = map(int, input().split())
num = [int(x) for x in input()]
back_num = num[::-1]
change = 0
rep = 0
for i in range(n // 2):
    if num[i] != back_num[i]:
        change += 1
if change <= k:
    diff = k - change
    for i in range(n // 2):
        if diff > 1:
            if num[i] != 9:
                num[i] = 9
                diff -= 1
            if num[-(i + 1)] != 9:
                num[-(i + 1)] = 9
                diff -= 1
        elif num[i] != num[-(i + 1)]:
            if diff > 0:
                num[i] = 9
                num[-(i + 1)] = 9
                diff -= 1
            else:
                num[i] = max(num[i], num[-(i + 1)])
                num[-(i + 1)] = max(num[i], num[-(i + 1)])
    if len(num) % 2 == 1 and diff > 0:
        num[(n // 2)] = 9
    print(*num, sep='')
else:
    print('-1')
