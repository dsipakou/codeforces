a = list(map(int, input().split()))
number = max(a)
print(('1/1', '5/6', '2/3', '1/2', '1/3', '1/6')[number - 1])