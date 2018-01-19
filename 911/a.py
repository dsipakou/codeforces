n = int(input())
arr = list(map(int, input().split()))
indexes = [i for i, value in enumerate(arr) if value == min(arr)]
output = -1
for i in range(len(indexes) - 1):
    if output < 0:
        output = indexes[i + 1] - indexes[i]
    else:
        output = min(output, indexes[i + 1] - indexes[i])
    if output == 1:
        break
print(output)