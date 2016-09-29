import math

n, k = map(int, input().split())
t = list(map(int, input().split()))
pages = []
output = 0
for i in range(n):
    cur_pages = math.ceil(t[i] / k)
    cur_pr_set = list(range(1, t[i] + 1))
    for j in range(cur_pages):
        pages.append(cur_pr_set[j * k:j * k + k])
for i in range(len(pages)):
    if i + 1 in pages[i]:
        output += 1
print(output)