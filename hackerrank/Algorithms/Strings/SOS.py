import re
count = 0
s = input()
print(s[1::3])
tmp = re.findall('...', s)
for i in range(len(tmp)):
    if tmp[i][0] != 'S':
        count += 1
    if tmp[i][1] != 'O':
        count += 1
    if tmp[i][2] != 'S':
        count += 1
print(count)