#http://codeforces.com/problemset/problem/583/B
n = int(input())
computers = list(map(int, input().split()))
keys = 0
steps = 0
index = 0
while keys < n:
    if not index > len(computers) - 1:
        if not computers[index] > keys:
            del computers[index]
            keys += 1
        else:
            index += 1
    else:
        computers.reverse()
        index = 0
        steps += 1
print(steps)
