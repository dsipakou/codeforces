n = int(input())
a = sorted(list(map(int, input().split())))
if a[0] is not 1:
    print(1)
    exit()
for i in range(1, n):
    if a[i] - a[i - 1] > 1:
        print(a[i - 1] + 1)
        exit()
print(a[n - 1] + 1)
