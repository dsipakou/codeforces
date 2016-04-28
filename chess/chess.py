s = [[0 for x in range(8)] for y in range(8)]
for i in range(8):
    s[i] = list(input())
arr = []
arr = list(map(list, zip(*s)))
white = 7
black = 7
for i in range(8):
    if 'W' in arr[i]:
        if "B" not in arr[i][:arr[i].index("W")]:
            white = min(white, arr[i].index("W"))
    if "B" in arr[i]:
        if "W" not in arr[i][::-1][:arr[i][::-1].index("B")]:
            black = min(black, arr[i][::-1].index("B"))
if white > black:
    print("B")
else:
    print("a")