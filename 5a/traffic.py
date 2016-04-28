dct = dict()
output = 0
while(True):
    try:
        input_str = input()
        if input_str[:1] == '+':
            dct[input_str[1:]] = 0
        elif input_str[:1] == '-':
            if dct[input_str[1:]] == 0:
                dct.pop(input_str[1:], None)
        else:
            output += len(input_str[input_str.index(":") + 1:]) * len(dct)
    except:
        break
print(output)