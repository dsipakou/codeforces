n, x = map(int, input().split())
l = 0
r = 1001
for _ in range(n):
    a = sorted(list(map(int, input().split())))
    l = max(l, a[0])
    r = min(r, a[1])
if l > r:
    print('-1')
elif x >= l and x <= r:
    print('0')
else:
    print(min(abs(x - l), abs(x - r)))