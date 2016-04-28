#http://codeforces.com/problemset/problem/585/A
n = int(input())
children = []
counter = 0
children_index = []
for _ in range(n):
    children.append(list(map(int, input().split())))
for i in range(len(children)):
    y = i + 1
    if children[i][2] >= 0:
        counter += 1
        children_index.append(i + 1)
        while y < len(children) and children[i][0] > 0:
            children[y][2] -= children[i][0]
            children[i][0] -= 1
            y += 1
    else:
        for z in range(y, len(children)):
            children[z][2] -= children[i][1]
print(counter)
print(' '.join(str(children_index[i]) for i in range(len(children_index))))
