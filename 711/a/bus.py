n = int(input())
found = False
output = list()
for i in range(n):
    s = list(input().split('|'))
    for j in range(len(s)):
        if 'OO' in s[j] and found is False:
            s[j] = s[j].replace('OO', '++')
            print('YES')
            found = True
    output.append('|'.join(s))
if found is False:
    print('NO')
else:
    print('\n'.join(str(s) for s in output))
