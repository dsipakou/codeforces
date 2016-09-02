n = int(input())
output = 'I'
for i in range(n):
    if output[len(output) - 1] == 'e':
        output += ' that I'
    if (i % 2) == 1:
        output += ' love'
    else:
        output += ' hate'
print(output + ' it')
