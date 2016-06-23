n = int(input())
a = list(map(int, input().split()))
print(max(max(abs(a.index(1) - 0), abs(a.index(1) - (n - 1))), max(abs(a.index(n) - 0), abs(a.index(n) - (n - 1)))))
