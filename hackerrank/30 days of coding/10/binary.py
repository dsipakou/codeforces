n = str(bin(int(input())))[2:]
tmp = 0
output = 0
for i in range(len(n)):
    if n[i] == '1':
        tmp += 1
    else:
        output = max(output, tmp)
        tmp = 0
print(max(output, tmp))
