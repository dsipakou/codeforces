cycle = int(input())
numbers = list(map(int, input().split()))
compare = 0
res = 0
for x in range(3):
    res += numbers[x] % 2
if res < 2:
    compare = 1
for index in range(cycle):
    if numbers[index] % 2 == compare:
        print(index + 1)
        break
