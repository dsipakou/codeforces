a, b, c = map(int, input().split())
print ('YES' if (not c == 0 and (b - a) % c == 0 and ((b > a and c > 0) or (b < a and c < 0))) or (a == b) else 'NO')
