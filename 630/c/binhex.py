n = int(input())
temp = '1'
output = 0
for i in range(n):
    output += 1
    output += int(temp, 2)
    temp += '1'
print(output)
