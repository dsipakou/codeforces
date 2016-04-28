n,t = map(int, input().split())
low = 10**(n - 1)
high = 10**n
start = low // t + 1
for i in range(1, 3):
    if low <= i * t * start < high:
        print(i * t * start)
        exit()
print("-1")
