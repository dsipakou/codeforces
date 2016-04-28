n = int(input())
price = 0
cost = 0
for i in range(n):
    a, p = map(int, input().split())
    if i == 0:
        price = p
    else:
        price = min(price, p)
    cost += a * price
print(cost)

