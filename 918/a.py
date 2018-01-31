n = int(input())
s = ''.join(str(s) for s in ['o'] * n)
arr = [1]

a, b = 1, 1

while b < n:
    a, b = b, a + b
    arr.append(b)
for i in range(len(arr)):
    if arr[i] <= n:
        s = s[:arr[i] - 1] + 'O' + s[arr[i]:]
print(s)