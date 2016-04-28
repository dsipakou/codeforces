# http://codeforces.com/problemset/problem/558/B
# not finished
n = int(input())
arr = list(map(int, input().split()))
minimum = len(arr)
left = 1
right = len(arr)
for i in range(n):
    indices = [i for i, x in enumerate(arr) if x == arr[i]]
    if max(indices) - min(indices) < minimum:
        minimum = max(indices) - min(indices)
        left = min(indices) + 1
        right = max(indices) + 1


print(left, right)
