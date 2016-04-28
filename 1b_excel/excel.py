# http://codeforces.com/problemset/problem/1/B
# INCOMPLETE
import string
n = int(input())
values = {}
for i, l in enumerate(string.ascii_uppercase):
    values[l] = i + 1
inp = []
for i in range(n):
    divider = 26
    tmp = input()
    if tmp.startswith('R'):
        cindex = tmp.index('C')
        col = int(tmp[cindex + 1:])
        while col >= 1:
            rest = int(col % divider)
            divider *= 26
            col //= 26
print()




