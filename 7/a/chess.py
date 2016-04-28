result = 0
m = 0
for x in range(8):
    input_str = input()
    if (input_str.count('B') == 8):
        result += 1
    else:
        m = max(m, input_str.count('B'))
print(result + m)