a = list(map(int, input().split()))
output = 0
while 1:
    a = sorted(a)
    if a[1] < 3:
        break
    time = (a[1] - 1) // 2
    a[0] += time
    a[1] -= time * 2
    output += time
print(output if a[0] < 2 and a[1] < 2 else output + 1)
