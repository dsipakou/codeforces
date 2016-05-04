n = input()
n2 = input()
n = sorted(n)
for x in range(len(n)):
    if n[0] == '0' and x:
        if n[x] != '0':
            temp = n[x]
            n[x] = '0'
            n[0] = temp
            break
n = ''.join(n)
if n == n2:
    print('OK')
else:
    print('WRONG_ANSWER')