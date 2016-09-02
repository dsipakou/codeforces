from bisect import *
n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())
for i in range(q):
    print(str(bisect_right(x, int(input()))))