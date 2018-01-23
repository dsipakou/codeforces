n = int(input())
left = 0
right = 0
for i in range(n):
    x = list(map(int, input().split()))[0]
    if x > 0:
        right += 1
    else:
        left += 1
print('YES' if right <= 1 or left <= 1 else 'NO')