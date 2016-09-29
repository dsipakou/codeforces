import math
s = str(input()).replace(' ', '')
rows = math.floor(math.sqrt(len(s)))
cols = math.ceil(math.sqrt(len(s)))
output = []
for i in range(cols):
    output.append(s[i::cols])

print(*output)