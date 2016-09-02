t, s, x = map(int, input().split())
if x >= t and ((x + s - t) % s == 0 or (x >= (t + s) and (x + s - t - 1) % s == 0)):
    print('YES')
else:
    print('NO')
