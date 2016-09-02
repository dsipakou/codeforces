n, d = map(int, input().split())
output = 0
t = 0
for i in range(d):
    l = input()
    if l.count('0') > 0:
        t += 1
    else:
        output = max(output, t)
        t = 0
print(max(output, t))