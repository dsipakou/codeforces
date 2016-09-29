n = int(input())
for i in range(n):
    s = list(input())
    current = s[0]
    i = 1
    count = 0
    while i < len(s):
        if s[i] == current:
            count += 1
        else:
            current = s[i]
        i += 1
    print(count)
