n, k, q = map(int, input().split())
a = list(map(int, input().split()))
index = abs(k % len(a) - len(a))
b = a[index:] + a[:index]
output = list()
for i in range(q):
    output.append(b[int(input())])
print('\n'.join(str(x) for x in output))