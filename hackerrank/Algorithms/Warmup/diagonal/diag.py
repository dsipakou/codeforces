n = int(input())
matrix = list()
for i in range(n):
    matrix.append(list(map(int, input().split())))
d1, d2 = 0, 0
for i in range(n):
    d1 += matrix[i][i]
    d2 += matrix[i][len(matrix) - 1 - i]
print(abs(d1 - d2))