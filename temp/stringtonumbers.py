n = input()
intstr = ''.join(c for c in n if c.isdigit())
result = 0
for i in range(len(intstr)):
    result += int(intstr[i])
print(result)
3456789