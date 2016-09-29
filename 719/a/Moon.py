n = int(input())
d = list(map(int, input().split()))
if len(d) < 2:
    if d[0] == 15:
        print('DOWN')
    elif d[0] == 0:
        print('UP')
    else:
        print(-1)
else:
    if d[-1] > d[-2]:
        if d[-1] == 15:
            print('DOWN')
        else:
            print('UP')
    elif d[-1] == 0:
        print('UP')
    else:
        print('DOWN')

