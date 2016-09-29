p = int(input())
q = int(input())
output = []
for i in range(p, q + 1):
    tmp = list(str(i**2))
    i1 = (int(''.join(x for x in tmp[:len(tmp) // 2])) if len(tmp[:len(tmp) // 2]) > 0 else 0)
    i2 = (int(''.join(x for x in tmp[len(tmp) // 2:])) if len(tmp[len(tmp) // 2:]) > 0 else 0)
    if i1 + i2 == i:
        output.append(i)
print(' '.join(str(x) for x in output) if len(output) > 0 else 'INVALID RANGE')