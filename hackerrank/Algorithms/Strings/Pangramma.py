s = input().lower()

l = list(chr(x) for x in range(ord('a'), ord('z') + 1))
for i in range(len(s)):
    if s[i] in l:
        l.remove(s[i])
print('pangram' if len(l) == 0 else 'not pangram')