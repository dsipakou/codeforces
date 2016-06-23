n, m = map(int, input().split())
arr = list()
ans = True
for i in range(n):
    number = list(input())
    if len(set(number)) > 1:
        ans = False
        break
    else:
        arr.append(number[0])
for i in range(1, len(arr) - 1):
    if arr[i] == arr[i - 1] or arr[i] == arr[i + 1]:
        ans = False
        break
print('YES' if ans else 'NO')