n, x = map(int, input().split())
child = 0
for i in range(n):
    sym, amount = map(str, input().split())
    if sym == '+':
        x += int(amount)
    else:
        if x - int(amount) < 0:
            child += 1
        else:
            x -= int(amount)
print(x, child)
