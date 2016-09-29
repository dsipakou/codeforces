n = int(input())
l = list(map(int, input().split()))
swap = 0
for i in range(n - 1, 0, -1):
    for j in range(i):
        if l[j] > l[j + 1]:
            tmp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = tmp
            swap += 1
print('Array is sorted in {0} swaps.'.format(swap))
print('First Element: {0}'.format(l[0]))
print('Last Element: {0}'.format(l[-1]))