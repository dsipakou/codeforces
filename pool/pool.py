# http://codeforces.com/problemset/problem/596/A
n = int(input())
lst_x = []
lst_y = []
output = -1
for _ in range(n):
    x,y = map(int, input().split())
    if x not in lst_x:
        lst_x.append(x)
    if y not in lst_y:
        lst_y.append(y)
    if len(lst_x) == len(lst_y) == 2:
        output = abs(lst_x[0] - lst_x[1]) * abs(lst_y[0] - lst_y[1])
print(output)
