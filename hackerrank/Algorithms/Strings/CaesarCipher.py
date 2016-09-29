n = int(input())
s = list(input())
k = int(input())
low = list(range(ord('a'), ord('z') + 1))
high = list(range(ord('A'), ord('Z') + 1))
for i in range(len(s)):
    if ord(s[i]) in low:
        s[i] = chr(low[(k + low.index(ord(s[i]))) % len(low)])
    elif ord(s[i]) in high:
        s[i] = chr(high[(k + high.index(ord(s[i]))) % len(high)])
print(''.join(str(x) for x in s))
