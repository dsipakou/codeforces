n = int(input())
l = list(map(int, input().split()))
count = 0
i = 0
while(i < n - 1):
    count += 1
    if l[min(i + 2, n - 1)] == 0:
        i += 2
    else:
        i += 1
print(count)