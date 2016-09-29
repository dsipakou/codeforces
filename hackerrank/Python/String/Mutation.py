s = list(input())
i, c = map(str, input().split())
s[int(i)] = c
print(*s, sep='')
