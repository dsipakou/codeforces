n = int(input())
for i in range(n):
    found = False
    s1 = list(set(input()))
    s2 = list(set(input()))
    for j in range(len(s1)):
        if s1[j] in s2:
            found = True
            break
    print('YES' if found else 'NO')