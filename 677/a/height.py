n, h = map(int, input().split())
a = list(map(int, input().split()))
output = 0
for i in range(len(a)):
    output += 1 if a[i] <= h else 2
print(output)
