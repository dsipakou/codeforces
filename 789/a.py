n, k = map(int, input().split())
w = sorted(list(map(int, input().split())))
output = 0
for i in range(n):
    output += w[i] // k
    if w[i] % k > 0:
        output += 1
print(int(output) // 2 if int(output) % 2 == 0 else (int(output) // 2) + 1)