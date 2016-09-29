t = int(input())
for i in range(t):
    n = 1
    output = 0
    a, b = map(int, input().split())
    while n**2 <= b:
        if n**2 >= a:
            output += 1
        n += 1
    print(output)