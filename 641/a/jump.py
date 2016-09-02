n = int(input())
s = list(1 if x == '>' else -1 for x in input())
l = list(map(int, input().split()))
summ = 1
cur = 0
next = 0
for i in range(n):
    if cur < 0 or cur > n - 1:
        print('FINITE')
        exit()
    if l[cur] == 0:
        print('INFINITE')
        exit()
    next += l[cur] * s[cur]
    l[cur] = 0
    cur = next
print('INFINITE' if 0 <= cur < n else 'FINITE')
