n = int(input())
l = list(map(int, input().split()))
t = 0
for i in range(n):
    t = (t + l[i]) % 2
    print(2 if t == (i + 1) % 2 else 1)