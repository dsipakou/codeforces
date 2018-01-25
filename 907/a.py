v1, v2, v3, vm = map(int, input().split())
if v1 > v2 > max(v3, vm):
    if 2 * min(v3, vm) < max(vm, v3):
        print('-1')
    else:
        print(2 * v1)
        print(2 * v2 if 2 * v2 < v1 else v1 - 1)
        print(max(vm, v3))

else:
    print('-1')
