n = int(input().strip())
c = list(map(int, input().split()))
x, y = map(int, input().split())
size = list(range(x, y + 1))
for i in range(n):
    if sum(c[:i]) in size and sum(c[i:]) in size:
        print(i + 1)
        exit()
print(0)

