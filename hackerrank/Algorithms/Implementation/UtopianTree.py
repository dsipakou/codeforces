t = int(input())
for i in range(t):
    start = 1
    n = int(input())
    for j in range(n):
        if j % 2 == 0:
            start = start * 2
        else:
            start += 1
    print(start)