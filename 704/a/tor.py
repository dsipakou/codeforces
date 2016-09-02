n, q = map(int, input().split())
l = list()
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        l.append(x)
        print(len(l) - l.count(0))
    elif t == 2:
        for index, item in enumerate(l):
            if item == x:
                l[index] = 0
        print(len(l) - l.count(0))
    else:
        l[:x] = (0 for x in range(len(l[:x])))
        print(len(l) - l.count(0))