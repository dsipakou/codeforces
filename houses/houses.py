n = int(input())
input = list(map(int, input().split()))
output = [0 for x in range(len(input))]
m = 0
for i in range(n - 1, -1, -1):
    output[i] = max(0, m - input[i] + 1)
    m = max(m, input[i])
print(' '.join(str(output[i]) for i in range(len(output))))
