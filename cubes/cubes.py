#http://codeforces.com/problemset/problem/573/B
n = int(input())
h = list(map(int, input().split()))
temp = [0 for x in range(len(h))]
counter = 0
while sum(h) > 0:
    temp = list(h)
    counter += 1
    for i in range(len(h)):
        if i == 0 or i == len(h) - 1:
            temp[i] = 0
        else:
            if temp[i] > min(h[i - 1], h[i + 1]):
                temp[i] = min(h[i - 1], h[i + 1])
            elif temp[i] > 0:
                temp[i] -= 1
    h = list(temp)
print(counter)

