s = input()
find = input()
output = 0
for i in range(len(s) - len(find) + 1):
    if s[i:i+len(find)] == find:
        output += 1
print(output)
