a = list(map(int, input().split()))
n,p1,p2,p3,t1,t2 = map(int, a)
output = 0
prev = 0
for index in range(n):
    safe_mode = 0
    line = list(map(int, input().split()))
    output += (line[1] - line[0]) * p1
    if prev != 0:
        safe_mode = line[0] - prev
        output += min(t1, safe_mode) * p1
        output += min(max(0, safe_mode - t1), t2) * p2
        output += max(0, safe_mode - t1 - t2) * p3
    prev = line[1]
print(output)