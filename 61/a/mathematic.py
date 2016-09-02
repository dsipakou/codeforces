a = input()
b = input()
output = bin(int(a, 2) ^ int(b, 2))
print(('0' * (len(a) - len(output[2:]))) + output[2:])


