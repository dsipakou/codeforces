s = list(input())
ss = list(set(s))
found = False
for i in range(len(ss)):
    if s.count(ss[i]) % 2 == 1:
        if found:
            print('NO')
            exit()
        else:
            found = True
print('YES')