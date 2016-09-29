n = int(input().strip())
l = list(map(int, input().split()))
for i in range(1, n):
    currentVal = l[i]
    pos = i
    while pos > 0 and l[pos-1] > currentVal:
        l[pos] = l[pos - 1]
        pos -= 1
    l[pos] = currentVal
    print(' '.join(str(x) for x in l))
