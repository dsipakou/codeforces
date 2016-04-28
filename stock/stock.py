#http://codeforces.com/problemset/problem/572/B
n,s = map(int, input().split())
buy = {}
sell = {}
for _ in range(n):
    temp = list(map(str, input().split()))
    if temp[0] == 'B':
        buy[int(temp[1])] = buy.get(int(temp[1]), 0) + int(temp[2])
    else:
        sell[int(temp[1])] = sell.get(int(temp[1]), 0) + int(temp[2])
for key,value in reversed(sorted(sell.items())[:s]):
    print('S', key, value)
for key,value in sorted(buy.items(), reverse=True)[:s]:
    print('B', key, value)


