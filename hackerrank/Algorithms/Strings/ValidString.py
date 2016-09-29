s = list(input())
occ = []
cur = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == cur:
        count += 1
    else:
        occ.append(count)
        count = 1
        cur = s[i]
    if i == len(s) - 1:
        occ.append(count)
print(occ)