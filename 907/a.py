v1, v2, v3, vm = map(int, input().split())
if v1 > v2 > v3:
    if vm > v3 or 2 * vm < v3:
        print('-1')
    else:
        print(v1)
        print(v2)
        print(v3)

else:
    print('-1')
