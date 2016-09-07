n = int(input().strip())
l = list(map(int, input().split()))
num = l[-1]
for i in range(n - 1, 0, -1):
    if num < l[i - 1]:
        l[i] = l[i - 1]
        print(' '.join(str(x) for x in l))
    else:
        l[i] = num
        print(' '.join(str(x) for x in l))
        break
    if i == 1:
        l[i - 1] = num
        print(' '.join(str(x) for x in l))