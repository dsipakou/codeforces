# http://codeforces.com/problemset/problem/3/A
start = input()
end = input()
rows = [1, 2, 3, 4, 5, 6, 7, 8]
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
start_row = rows.index(int(start[1:]))
start_col = cols.index(start[:1])
end_row = rows.index(int(end[1:]))
end_col = cols.index(end[:1])
steps = []
diag = min(abs(start_row - end_row), abs(start_col - end_col))
all_steps = max(abs(start_row - end_row), abs(start_col - end_col))
vertical_pref = ''
horiz_pref = ''
if start_row > end_row:
    vertical_pref = 'D'
else:
    vertical_pref = 'U'
if start_col > end_col:
    horiz_pref = 'L'
else:
    horiz_pref = 'R'
print(all_steps)
for _ in range(diag):
    print(horiz_pref + vertical_pref)
if abs(start_row - end_row) != abs(start_col - end_col):
    if abs(start_row - end_row) > abs(start_col - end_col):
        for _ in range(all_steps - diag):
            print(vertical_pref)
    else:
        for _ in range(all_steps - diag):
            print(horiz_pref)
