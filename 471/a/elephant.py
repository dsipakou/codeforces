l = list(map(int, input().split()))
s = list(set(l))
if len(s) == 1:
    print('Elephant')
elif len(s) == 2:
    if l.count(s[0]) == 4 or l.count(s[1]) == 4:
        print('Elephant')
    elif l.count(s[0]) == 5 or l.count(s[1]) == 5:
        print('Bear')
    else:
        print('Alien')
elif len(s) == 3:
    if l.count(s[0]) == 4 or l.count(s[1]) == 4 or l.count(s[2]) == 4:
        print('Bear')
    else:
        print('Alien')
else:
    print('Alien')
