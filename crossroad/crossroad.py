#http://codeforces.com/problemset/problem/583/A
n = int(input())
x_roads = list()
y_roads = list()
days = list()
for index in range(n * n):
    x,y = map(int, input().split())
    if not x in x_roads and not y in y_roads:
        x_roads.append(x)
        y_roads.append(y)
        days.append(index + 1)
print(' '.join(str(e) for e in days))
