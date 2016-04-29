a = input()
b = ""
c = False
for index in range(len(a)):
    if int(a[index]) > 0 or c:
        b += str(1)
        if int(a[index]) > 1:
            c = True
    else:
        b += str(0)
print(int(b,2))
