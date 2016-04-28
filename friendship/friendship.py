# http://codeforces.com/problemset/problem/580/B
n,d = map(int, input().split())
friends = []
output = 0
for _ in range(n):
    friends.append(list(map(int, input().split())))
friends = sorted(friends)
for i in range(len(friends)):
    friendship = sum(friends[y][1] for y in range(i, len(friends)) if abs(friends[y][0] - friends[i][0]) < d)
    output = max(friendship, output)
print(output)

