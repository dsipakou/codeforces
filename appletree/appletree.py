# http://codeforces.com/problemset/problem/558/A
n = int(input())
left = 0
right = 0
trees_pos = []
trees_neg = []
for _ in range(n):
    trees_pos.append(tuple(map(int, input().split())))

trees_pos = sorted(trees_pos)
for tree in trees_pos:
    if tree[0] < 0:
        trees_neg.append(tree)
        trees_pos.remove(tree)



