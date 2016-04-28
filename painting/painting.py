# http://codeforces.com/problemset/problem/560/B
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
print(a, b, c)
if max(b[1], c[1]) <= a[1] and b[0] + c[0] <= a[0] or max(b[1], c[0]) <= a[1] and b[0] + c[1] <= a[0]:
    print("YES")
else:
    print("NO")


