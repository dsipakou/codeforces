t = int(input())
for i in range(t):
    output = 0
    d = int(input())
    n = [int(x) for x in list(str(d))]
    for j in range(len(n)):
        if n[j] != 0 and d % n[j] == 0:
            output += 1
    print(output)