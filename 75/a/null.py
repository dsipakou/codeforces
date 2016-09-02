a = int(input())
b = int(input())
c = a + b
a1 = int(''.join(str(x) for x in str(a) if x != '0'))
b1 = int(''.join(str(x) for x in str(b) if x != '0'))
c1 = int(''.join(str(x) for x in str(c) if x != '0'))
print('YES' if a1 + b1 == c1 else 'NO')