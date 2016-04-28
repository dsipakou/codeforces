# http://codeforces.com/problemset/problem/2/A
n = int(input())
names = {}
history = []
output = ''
for i in range(n):
    username, score = input().split()
    score = int(score)
    names[username] = names.get(username, 0) + score
    history.append([username, names[username]])
maximum = max(names.values())
for name, value in history:
    if value >= maximum and names[name] == maximum:
        print(name)
        break
