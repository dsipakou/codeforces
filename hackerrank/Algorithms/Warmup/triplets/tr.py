a = list(map(int, input().split()))
b = list(map(int, input().split()))
out1, out2 = 0, 0
for i in range(len(a)):
    out1 += int(a[i] > b[i])
    out2 += int(b[i] > a[i])
print(out1, out2)