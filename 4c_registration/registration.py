i = int(input())
dct = dict()
for x in range(i):
    input_str = input()
    dct[input_str] = dct.get(input_str, 0) + 1
    if dct[input_str] == 1:
        print('OK')
    else:
        print(input_str + str(dct[input_str] - 1))

