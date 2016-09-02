x = int(input())
if x < 6:
    print(1)
else:
    print(x // 5 if not x % 5 else (x // 5) + 1)
