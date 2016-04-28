n, m = map(int, input().split())
output = 0
for i in range(n):
    win = list(map(int, input().split()))
    for j in range(0, 2 * m, 2):
        if win[j] + win[j + 1] > 0:
            output += 1
print(output)
