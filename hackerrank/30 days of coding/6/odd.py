n = int(input())
for i in range(n):
    o1 = ''
    o2 = ''
    s = input()
    for j in range(len(s)):
        if j % 2 == 0:
            o1 += s[j]
        else:
            o2 += s[j]
    print(o1 + ' ' + o2)