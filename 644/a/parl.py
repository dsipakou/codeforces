n,b,a = map(int, input().split())
mem = list(x for x in range(n))
if len(mem) > a * b:
    print("-1")
else:
    tmp_list = list(0 for _ in range(a*b))
    for i in range(len(mem)):
        tmp_list[i] = mem[i] + 1
    index = 0
    output = ""
    for row in range(b):
        if a % 2 == 0 and (row + 1) % 2 == 0:
            tmp = tmp_list[index:index + a]
            tmp = tmp[::-1]
            output += " ".join(str(x) for x in tmp)
            index += a
        else:
            tmp = tmp_list[index:index + a]
            output += " ".join(str(x) for x in tmp)
            index += a
        output += '\n'
    print(output)