n = int(input())
l = sorted(list(map(int, input().split())))
s = sorted(list(set(l)))
for i in range(len(s)):
    print(len([x for x in l if x >= s[i]]))
