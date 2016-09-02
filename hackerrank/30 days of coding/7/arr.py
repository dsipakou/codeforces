n = int(input())
l = list(map(int, input().split()))
print(' '.join(str(x) for x in reversed(l)))