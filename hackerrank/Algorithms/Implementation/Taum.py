t = int(input())
for i in range(t):
    b, w = map(int, input().split())
    x, y, z = map(int, input().split())
    if x + z < y:
        print(x * b + (x + z) * w)
    elif y + z < x:
        print((y + z) * b + y * w)
    else:
        print(x*b + y*w)