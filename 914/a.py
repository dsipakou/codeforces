import math

n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
if arr[0] <= 0:
    print(arr[0])
    exit()
for i in range(len(arr)):
    if arr[i] <= 0:
        print(arr[i])
        exit()
    if str(math.sqrt(arr[i]))[-2] != '.':
        print(arr[i])
        exit()
