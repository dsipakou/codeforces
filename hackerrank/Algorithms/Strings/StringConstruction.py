n = int(input())
for i in range(n):
    s = list(input())
    ss = set(s)
    print(len(s) - (len(s) - len(ss)))