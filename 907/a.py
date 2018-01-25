v1, v2, v3, vm = map(int, input().split())
if v1 > v2 > max(v3, vm):
    if 2 * min(v3, vm) < max(vm, v3):
        print('-1')
    else:
        print(v1)
        print(v2)
        print(max(vm, v3))

else:
    print('-1')
