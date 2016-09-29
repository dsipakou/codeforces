t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    l = [1 if int(x) <= 0 else 0 for x in input().split()]
    print('YES' if sum(l) < k else 'NO')
