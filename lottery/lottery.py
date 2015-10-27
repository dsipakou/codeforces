#http://codeforces.com/problemset/problem/589/I
n,k = map(int, input().split())
seq = list(map(int, input().split()))
step = int(n / k)
counter = 0
color = 1
for _ in range(k):
    tmp = list(seq[i] for i in range(len(seq)) if seq[i] == color)
    if step > len(tmp):
        counter += step - len(tmp)
    color += 1
print(counter)
