n = int(input())
arr = list(map(int, input().split()))
output = -1
i = arr.count(min(arr))
for j in range(i - 1):
    index = arr.index(min(arr))
    arr = arr[index + 1:]
    if output > 0:
        output = min(output, arr.index(min(arr)) + 1)
    else:
        output = arr.index(min(arr)) + 1
print(output)