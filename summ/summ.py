# http://codeforces.com/problemset/problem/598/A
t = int(input())
for _ in range(t):
    n = int(input())
    output = (n * (n + 1)) // 2
    tmp = 1
    while tmp <= n:
        output -= 2 * tmp
        tmp *= 2
    print(output)



