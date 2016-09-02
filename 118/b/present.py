n = int(input())
l = [list(range(n)) + [n] + list(reversed(range(n)))]

for i in reversed(range(n)):
    l = [list(range(i)) + [i] + list(reversed(range(i)))] + l
    l.append(list(range(i)) + [i] + list(reversed(range(i))))

for i in range(len(l)):
    print(' ' * ((n - max(l[i])) * 2) + ' '.join(str(x) for x in l[i]))
